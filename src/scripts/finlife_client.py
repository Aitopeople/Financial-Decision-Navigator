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
    "annuity_saving": "annuitySavingProductsSearch",
    "mortgage": "mortgageLoanProductsSearch",
    "rent_house": "rentHouseLoanProductsSearch",
}

MORTGAGE_JOIN_KEYS = ("dcls_month", "fin_co_no", "fin_prdt_cd")
SAVING_JOIN_KEYS = ("dcls_month", "fin_co_no", "fin_prdt_cd")
ANNUITY_JOIN_KEYS = ("dcls_month", "fin_co_no", "fin_prdt_cd")


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
    return summarize_loan(
        payload=payload,
        service="mortgageLoanProductsSearch",
        principal=principal,
        years=years,
        limit=limit,
        decision_use="주택담보대출 상품 추천이 아니라 월 상환액과 금리 민감도 계산에 사용합니다.",
    )


def summarize_rent_house_loan(payload: dict[str, Any], principal: int, years: int, limit: int) -> dict[str, Any]:
    return summarize_loan(
        payload=payload,
        service="rentHouseLoanProductsSearch",
        principal=principal,
        years=years,
        limit=limit,
        decision_use="전세자금대출 상품 추천이 아니라 전세 선택지의 월 상환 부담과 금리 민감도 계산에 사용합니다.",
    )


def summarize_loan(payload: dict[str, Any], service: str, principal: int, years: int, limit: int, decision_use: str) -> dict[str, Any]:
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
        repayment_type = option.get("rpay_type_nm")
        payment = monthly_payment_by_repayment(principal, avg / 100, years, str(repayment_type or ""))
        rows.append(
            {
                "bank": base.get("kor_co_nm"),
                "product": base.get("fin_prdt_nm"),
                "join_way": base.get("join_way"),
                "mortgage_type": option.get("mrtg_type_nm"),
                "repayment_type": repayment_type,
                "rate_type": option.get("lend_rate_type_nm"),
                "rate_min": rate_min,
                "rate_avg": avg,
                "rate_max": rate_max,
                "monthly_payment_at_avg": payment["monthly_payment"],
                "payment_calculation": payment["calculation"],
            }
        )

    rows.sort(key=lambda item: (item["rate_avg"], item["monthly_payment_at_avg"]))
    selected = rows[:limit]
    rates = [item["rate_avg"] for item in rows if item["rate_avg"] is not None]
    return {
        "source": "금융감독원 금융상품통합비교공시 Finlife",
        "service": service,
        "dcls_month": result.get("baseList", [{}])[0].get("dcls_month") if base_list else None,
        "total_options": len(rows),
        "principal": principal,
        "years": years,
        "rate_avg_min": min(rates) if rates else None,
        "rate_avg_max": max(rates) if rates else None,
        "products": selected,
        "decision_use": decision_use,
    }


def text_contains(value: Any, needle: str | None) -> bool:
    if not needle:
        return True
    return needle.lower() in str(value or "").lower()


def summarize_savings(
    payload: dict[str, Any],
    product_type: str,
    save_trm: str | None,
    limit: int,
    join_way: str | None = None,
    min_basic_rate: float | None = None,
    min_max_rate: float | None = None,
    sort_by: str = "max_rate",
) -> dict[str, Any]:
    result = finlife_result(payload)
    base_list = result.get("baseList") or []
    option_list = result.get("optionList") or []
    rows: list[dict[str, Any]] = []

    for option in option_list:
        if save_trm and str(option.get("save_trm")) != str(save_trm):
            continue
        base = join_base(base_list, option, SAVING_JOIN_KEYS)
        if not text_contains(base.get("join_way"), join_way):
            continue
        basic_rate = as_float(option.get("intr_rate"))
        max_rate = as_float(option.get("intr_rate2"))
        if basic_rate is None and max_rate is None:
            continue
        if min_basic_rate is not None and (basic_rate is None or basic_rate < min_basic_rate):
            continue
        if min_max_rate is not None and (max_rate is None or max_rate < min_max_rate):
            continue
        rows.append(
            {
                "bank": base.get("kor_co_nm"),
                "product": base.get("fin_prdt_nm"),
                "join_way": base.get("join_way"),
                "special_condition": base.get("spcl_cnd"),
                "join_member": base.get("join_member"),
                "max_limit": base.get("max_limit"),
                "save_term_months": option.get("save_trm"),
                "rate_type": option.get("intr_rate_type_nm"),
                "reserve_type": option.get("rsrv_type_nm"),
                "basic_rate": basic_rate,
                "max_rate": max_rate,
            }
        )

    sort_key = "basic_rate" if sort_by == "basic_rate" else "max_rate"
    rows.sort(key=lambda item: (item[sort_key] if item[sort_key] is not None else -1), reverse=True)
    return {
        "source": "금융감독원 금융상품통합비교공시 Finlife",
        "service": SERVICE_NAMES[product_type],
        "total_options": len(rows),
        "save_term_months": save_trm,
        "filters": {
            "join_way": join_way,
            "min_basic_rate": min_basic_rate,
            "min_max_rate": min_max_rate,
            "sort_by": sort_key,
        },
        "products": rows[:limit],
        "decision_use": "저축하며 기다리는 선택지의 기대 금리 범위를 잡는 데 사용합니다.",
    }


def summarize_annuity_savings(
    payload: dict[str, Any],
    start_age: int | None,
    monthly_pay: int | None,
    pay_period: int | None,
    receive_term: str | None,
    limit: int,
) -> dict[str, Any]:
    result = finlife_result(payload)
    base_list = result.get("baseList") or []
    option_list = result.get("optionList") or []
    rows: list[dict[str, Any]] = []

    for option in option_list:
        if start_age is not None and as_float(option.get("pnsn_strt_age")) != float(start_age):
            continue
        if monthly_pay is not None and as_float(option.get("mon_paym_atm")) != float(monthly_pay):
            continue
        if pay_period is not None and as_float(option.get("paym_prd")) != float(pay_period):
            continue
        if receive_term and not text_contains(option.get("pnsn_recp_trm_nm"), receive_term):
            continue
        base = join_base(base_list, option, ANNUITY_JOIN_KEYS)
        receive_amount = as_float(option.get("pnsn_recp_amt"))
        rows.append(
            {
                "company": base.get("kor_co_nm"),
                "product": base.get("fin_prdt_nm"),
                "join_way": base.get("join_way"),
                "pension_kind": base.get("pnsn_kind_nm"),
                "product_type": base.get("prdt_type_nm"),
                "average_profit_rate": as_float(base.get("avg_prft_rate")),
                "disclosed_rate": as_float(base.get("dcls_rate")),
                "guaranteed_rate": as_float(base.get("guar_rate")),
                "one_year_return": as_float(base.get("btrm_prft_rate_1")),
                "two_year_return": as_float(base.get("btrm_prft_rate_2")),
                "three_year_return": as_float(base.get("btrm_prft_rate_3")),
                "sale_company": base.get("sale_co"),
                "receive_term": option.get("pnsn_recp_trm_nm"),
                "entry_age": option.get("pnsn_entr_age"),
                "monthly_payment_unit": option.get("mon_paym_atm"),
                "monthly_payment": option.get("mon_paym_atm_nm"),
                "pay_period_years": option.get("paym_prd"),
                "start_age": option.get("pnsn_strt_age"),
                "expected_receive_amount": receive_amount,
            }
        )

    rows.sort(key=lambda item: (item["expected_receive_amount"] if item["expected_receive_amount"] is not None else -1), reverse=True)
    return {
        "source": "금융감독원 금융상품통합비교공시 Finlife",
        "service": SERVICE_NAMES["annuity_saving"],
        "dcls_month": result.get("baseList", [{}])[0].get("dcls_month") if base_list else None,
        "total_options": len(rows),
        "filters": {
            "start_age": start_age,
            "monthly_pay": monthly_pay,
            "pay_period": pay_period,
            "receive_term": receive_term,
        },
        "products": rows[:limit],
        "decision_use": "은퇴 현금흐름 경로를 비교하기 위한 연금저축 상품 조건이며 가입 권유가 아닙니다.",
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


def monthly_payment_by_repayment(principal: int, annual_rate: float, years: int, repayment_type: str) -> dict[str, Any]:
    if "만기일시" in repayment_type:
        return {
            "monthly_payment": round(principal * annual_rate / 12),
            "calculation": "interest_only_until_maturity",
        }
    return {
        "monthly_payment": monthly_payment(principal, annual_rate, years).monthly_payment,
        "calculation": "amortized_principal_and_interest",
    }


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

    rent_house = sub.add_parser("rent-house")
    rent_house.add_argument("--principal", type=int, required=True)
    rent_house.add_argument("--years", type=int, default=2)
    rent_house.add_argument("--limit", type=int, default=5)

    savings = sub.add_parser("savings")
    savings.add_argument("--type", choices=["deposit", "saving"], default="deposit")
    savings.add_argument("--save-trm", help="Savings term in months, for example 12, 24, 36.")
    savings.add_argument("--limit", type=int, default=5)
    savings.add_argument("--join-way", help="Filter products whose join_way contains this text, e.g. 스마트폰.")
    savings.add_argument("--min-basic-rate", type=float)
    savings.add_argument("--min-max-rate", type=float)
    savings.add_argument("--sort-by", choices=["basic_rate", "max_rate"], default="max_rate")

    annuity = sub.add_parser("annuity-saving")
    annuity.add_argument("--start-age", type=int)
    annuity.add_argument("--monthly-pay", type=int, help="Finlife mon_paym_atm unit, e.g. 20 for 200,000원.")
    annuity.add_argument("--pay-period", type=int)
    annuity.add_argument("--receive-term", help="Filter receive term text, e.g. 20년.")
    annuity.add_argument("--limit", type=int, default=5)

    payment = sub.add_parser("payment")
    payment.add_argument("--principal", type=int, required=True)
    payment.add_argument("--annual-rate", type=float, required=True, help="Percent value, for example 4.2")
    payment.add_argument("--years", type=int, default=30)

    return parser


def main() -> int:
    load_env_file()
    parser = build_parser()
    args = parser.parse_args()
    default_top_fin_grp_no = "060000" if args.command == "annuity-saving" else BANK_GROUP
    top_fin_grp_no = args.top_fin_grp_no or os.environ.get("FINLIFE_TOP_FIN_GRP_NO") or default_top_fin_grp_no
    page_no = args.page_no or int(os.environ.get("FINLIFE_PAGE_NO") or "1")
    try:
        if args.command == "payment":
            data = monthly_payment(args.principal, args.annual_rate / 100, args.years)
            print(json.dumps(data.__dict__, ensure_ascii=False, indent=2))
            return 0

        if args.command == "mortgage":
            service = SERVICE_NAMES["mortgage"]
        elif args.command == "rent-house":
            service = SERVICE_NAMES["rent_house"]
        elif args.command == "annuity-saving":
            service = SERVICE_NAMES["annuity_saving"]
        else:
            service = SERVICE_NAMES[args.type]
        payload = load_payload(args.fixture, service, args.auth, top_fin_grp_no, page_no)
        if args.command == "mortgage":
            output = summarize_mortgage(payload, args.principal, args.years, args.limit)
        elif args.command == "rent-house":
            output = summarize_rent_house_loan(payload, args.principal, args.years, args.limit)
        elif args.command == "annuity-saving":
            output = summarize_annuity_savings(payload, args.start_age, args.monthly_pay, args.pay_period, args.receive_term, args.limit)
        else:
            output = summarize_savings(
                payload,
                args.type,
                args.save_trm,
                args.limit,
                args.join_way,
                args.min_basic_rate,
                args.min_max_rate,
                args.sort_by,
            )
        print(json.dumps(output, ensure_ascii=False, indent=2))
        return 0
    except Exception as exc:  # noqa: BLE001 - CLI boundary
        print(json.dumps({"error": str(exc)}, ensure_ascii=False, indent=2), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
