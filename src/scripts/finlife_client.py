#!/usr/bin/env python3
"""Finlife API adapter for Financial Decision Navigator.

Uses only the Python standard library. The live API key must be provided through
FINLIFE_API_KEY or --auth. For deterministic examples/tests, pass --fixture.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.parse
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from typing import Any


BASE_URL = "http://finlife.fss.or.kr/finlifeapi"
BANK_GROUP = "020000"

SERVICE_NAMES = {
    "deposit": "depositProductsSearch",
    "saving": "savingProductsSearch",
    "mortgage": "mortgageLoanProductsSearch",
    "rent_house": "rentHouseLoanProductsSearch",
}

MORTGAGE_JOIN_KEYS = ("dcls_month", "fin_co_no", "fin_prdt_cd")
SAVING_JOIN_KEYS = ("dcls_month", "fin_co_no", "fin_prdt_cd")


@dataclass(frozen=True)
class MonthlyPayment:
    principal: int
    annual_rate: float
    years: int
    monthly_payment: int


def load_env_file(start: Path | None = None) -> None:
    """Load simple KEY=VALUE lines from the nearest .env without overriding env."""
    current = (start or Path.cwd()).resolve()
    candidates = [current, *current.parents]
    script_root = Path(__file__).resolve().parents[2]
    if script_root not in candidates:
        candidates.append(script_root)

    for directory in candidates:
        env_path = directory / ".env"
        if not env_path.is_file():
            continue
        for raw_line in env_path.read_text(encoding="utf-8-sig").splitlines():
            line = raw_line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, value = line.split("=", 1)
            key = key.strip()
            value = value.strip().strip('"').strip("'")
            if key and key not in os.environ:
                os.environ[key] = value
        return


def load_payload(fixture: str | None, service: str, auth: str | None, top_fin_grp_no: str, page_no: int) -> dict[str, Any]:
    if fixture:
        return json.loads(Path(fixture).read_text(encoding="utf-8"))

    key = auth or os.environ.get("FINLIFE_API_KEY")
    if not key:
        raise RuntimeError("FINLIFE_API_KEY 환경변수 또는 --auth 값이 필요합니다. API 키는 로그에 남기지 마세요.")

    query = urllib.parse.urlencode({"auth": key, "topFinGrpNo": top_fin_grp_no, "pageNo": str(page_no)})
    url = f"{BASE_URL}/{service}.json?{query}"
    with urllib.request.urlopen(url, timeout=15) as response:  # noqa: S310 - configured public API endpoint
        return json.loads(response.read().decode("utf-8"))


def finlife_result(payload: dict[str, Any]) -> dict[str, Any]:
    result = payload.get("result")
    if not isinstance(result, dict):
        raise ValueError("Finlife response does not contain result object")
    err_cd = str(result.get("err_cd", ""))
    if err_cd and err_cd != "000":
        raise RuntimeError(f"Finlife API error {err_cd}: {result.get('err_msg')}")
    return result


def as_float(value: Any) -> float | None:
    if value in (None, ""):
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def join_base(base_list: list[dict[str, Any]], option: dict[str, Any], keys: tuple[str, ...]) -> dict[str, Any]:
    for base in base_list:
        if all(str(base.get(key)) == str(option.get(key)) for key in keys):
            return base
    return {}


def summarize_mortgage(payload: dict[str, Any], principal: int, years: int, limit: int) -> dict[str, Any]:
    result = finlife_result(payload)
    base_list = result.get("baseList") or []
    option_list = result.get("optionList") or []
    rows: list[dict[str, Any]] = []

    for option in option_list:
        avg = as_float(option.get("lend_rate_avg"))
        rate_min = as_float(option.get("lend_rate_min"))
        rate_max = as_float(option.get("lend_rate_max"))
        if avg is None:
            continue
        base = join_base(base_list, option, MORTGAGE_JOIN_KEYS)
        rows.append(
            {
                "bank": base.get("kor_co_nm"),
                "product": base.get("fin_prdt_nm"),
                "join_way": base.get("join_way"),
                "mortgage_type": option.get("mrtg_type_nm"),
                "repayment_type": option.get("rpay_type_nm"),
                "rate_type": option.get("lend_rate_type_nm"),
                "rate_min": rate_min,
                "rate_avg": avg,
                "rate_max": rate_max,
                "monthly_payment_at_avg": monthly_payment(principal, avg / 100, years).monthly_payment,
            }
        )

    rows.sort(key=lambda item: (item["rate_avg"], item["monthly_payment_at_avg"]))
    selected = rows[:limit]
    rates = [item["rate_avg"] for item in rows if item["rate_avg"] is not None]
    return {
        "source": "금융감독원 금융상품통합비교공시 Finlife",
        "service": "mortgageLoanProductsSearch",
        "dcls_month": result.get("baseList", [{}])[0].get("dcls_month") if base_list else None,
        "total_options": len(rows),
        "principal": principal,
        "years": years,
        "rate_avg_min": min(rates) if rates else None,
        "rate_avg_max": max(rates) if rates else None,
        "products": selected,
        "decision_use": "주택담보대출 상품 추천이 아니라 월 상환액과 금리 민감도 계산에 사용합니다.",
    }


def summarize_savings(payload: dict[str, Any], product_type: str, save_trm: str | None, limit: int) -> dict[str, Any]:
    result = finlife_result(payload)
    base_list = result.get("baseList") or []
    option_list = result.get("optionList") or []
    rows: list[dict[str, Any]] = []

    for option in option_list:
        if save_trm and str(option.get("save_trm")) != str(save_trm):
            continue
        base = join_base(base_list, option, SAVING_JOIN_KEYS)
        basic_rate = as_float(option.get("intr_rate"))
        max_rate = as_float(option.get("intr_rate2"))
        if basic_rate is None and max_rate is None:
            continue
        rows.append(
            {
                "bank": base.get("kor_co_nm"),
                "product": base.get("fin_prdt_nm"),
                "join_way": base.get("join_way"),
                "save_term_months": option.get("save_trm"),
                "rate_type": option.get("intr_rate_type_nm"),
                "basic_rate": basic_rate,
                "max_rate": max_rate,
            }
        )

    rows.sort(key=lambda item: (item["max_rate"] if item["max_rate"] is not None else -1), reverse=True)
    return {
        "source": "금융감독원 금융상품통합비교공시 Finlife",
        "service": SERVICE_NAMES[product_type],
        "total_options": len(rows),
        "save_term_months": save_trm,
        "products": rows[:limit],
        "decision_use": "저축하며 기다리는 선택지의 기대 금리 범위를 잡는 데 사용합니다.",
    }


def monthly_payment(principal: int, annual_rate: float, years: int) -> MonthlyPayment:
    months = years * 12
    monthly_rate = annual_rate / 12
    if months <= 0:
        raise ValueError("years must be positive")
    if abs(monthly_rate) < 1e-12:
        amount = principal / months
    else:
        amount = principal * monthly_rate * (1 + monthly_rate) ** months / ((1 + monthly_rate) ** months - 1)
    return MonthlyPayment(principal=principal, annual_rate=annual_rate, years=years, monthly_payment=round(amount))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Finlife adapter for FDN")
    parser.add_argument("--auth", help="Finlife API key. Prefer FINLIFE_API_KEY env var.")
    parser.add_argument("--fixture", help="Read a saved Finlife JSON response instead of calling the API.")
    parser.add_argument("--top-fin-grp-no", default=None)
    parser.add_argument("--page-no", type=int, default=None)

    sub = parser.add_subparsers(dest="command", required=True)

    mortgage = sub.add_parser("mortgage")
    mortgage.add_argument("--principal", type=int, required=True)
    mortgage.add_argument("--years", type=int, default=30)
    mortgage.add_argument("--limit", type=int, default=5)

    savings = sub.add_parser("savings")
    savings.add_argument("--type", choices=["deposit", "saving"], default="deposit")
    savings.add_argument("--save-trm", help="Savings term in months, for example 12, 24, 36.")
    savings.add_argument("--limit", type=int, default=5)

    payment = sub.add_parser("payment")
    payment.add_argument("--principal", type=int, required=True)
    payment.add_argument("--annual-rate", type=float, required=True, help="Percent value, for example 4.2")
    payment.add_argument("--years", type=int, default=30)

    return parser


def main() -> int:
    load_env_file()
    parser = build_parser()
    args = parser.parse_args()
    top_fin_grp_no = args.top_fin_grp_no or os.environ.get("FINLIFE_TOP_FIN_GRP_NO") or BANK_GROUP
    page_no = args.page_no or int(os.environ.get("FINLIFE_PAGE_NO") or "1")
    try:
        if args.command == "payment":
            data = monthly_payment(args.principal, args.annual_rate / 100, args.years)
            print(json.dumps(data.__dict__, ensure_ascii=False, indent=2))
            return 0

        service = SERVICE_NAMES["mortgage"] if args.command == "mortgage" else SERVICE_NAMES[args.type]
        payload = load_payload(args.fixture, service, args.auth, top_fin_grp_no, page_no)
        if args.command == "mortgage":
            output = summarize_mortgage(payload, args.principal, args.years, args.limit)
        else:
            output = summarize_savings(payload, args.type, args.save_trm, args.limit)
        print(json.dumps(output, ensure_ascii=False, indent=2))
        return 0
    except Exception as exc:  # noqa: BLE001 - CLI boundary
        print(json.dumps({"error": str(exc)}, ensure_ascii=False, indent=2), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
