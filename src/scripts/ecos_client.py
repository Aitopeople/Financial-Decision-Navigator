#!/usr/bin/env python3
"""Bank of Korea ECOS API adapter for Financial Decision Navigator."""
from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any


BASE_URL = "https://ecos.bok.or.kr/api"
DEFAULT_LANGUAGE = "kr"
DEFAULT_START = 1
DEFAULT_END = 100


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


def load_payload(fixture: str | None, service: str, auth: str | None, language: str, start: int, end: int, args: list[str]) -> dict[str, Any]:
    if fixture:
        return json.loads(Path(fixture).read_text(encoding="utf-8"))

    key = auth or os.environ.get("ECOS_API_KEY")
    if not key:
        raise RuntimeError("ECOS_API_KEY 환경변수 또는 --auth 값이 필요합니다. API 키는 로그에 남기지 마세요.")

    encoded_args = [urllib.parse.quote(str(item), safe="") for item in args]
    path = "/".join([service, key, "json", language, str(start), str(end), *encoded_args])
    url = f"{BASE_URL}/{path}"
    with urllib.request.urlopen(url, timeout=15) as response:  # noqa: S310 - configured public API endpoint
        return json.loads(response.read().decode("utf-8"))


def ecos_rows(payload: dict[str, Any], service: str) -> list[dict[str, Any]]:
    error = payload.get("RESULT")
    if isinstance(error, dict):
        code = str(error.get("CODE", ""))
        if code and code not in ("INFO-000", "000"):
            raise RuntimeError(f"ECOS API error {code}: {error.get('MESSAGE')}")

    body = payload.get(service)
    if not isinstance(body, dict):
        raise ValueError(f"ECOS response does not contain {service} object")

    result = body.get("RESULT")
    if isinstance(result, dict):
        code = str(result.get("CODE", ""))
        if code and code not in ("INFO-000", "000"):
            raise RuntimeError(f"ECOS API error {code}: {result.get('MESSAGE')}")

    rows = body.get("row") or []
    if isinstance(rows, dict):
        return [rows]
    if isinstance(rows, list):
        return rows
    return []


def as_float(value: Any) -> float | None:
    if value in (None, ""):
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def summarize_key_stats(payload: dict[str, Any]) -> dict[str, Any]:
    rows = ecos_rows(payload, "KeyStatisticList")
    important_terms = ("금리", "물가", "환율", "GDP", "소득", "소비", "가계", "채권")
    selected = []
    for row in rows:
        name = str(row.get("KEYSTAT_NAME") or "")
        class_name = str(row.get("CLASS_NAME") or "")
        if any(term in name or term in class_name for term in important_terms):
            selected.append(
                {
                    "class_name": row.get("CLASS_NAME"),
                    "name": row.get("KEYSTAT_NAME"),
                    "value": as_float(row.get("DATA_VALUE")),
                    "cycle": row.get("CYCLE"),
                    "unit": row.get("UNIT_NAME"),
                }
            )
    return {
        "source": "한국은행 ECOS Open API",
        "service": "KeyStatisticList",
        "indicator_count": len(rows),
        "selected_indicators": selected,
        "decision_use": "금리, 물가, 환율, 경기 흐름을 시나리오 변수로 사용합니다.",
    }


def summarize_search(payload: dict[str, Any]) -> dict[str, Any]:
    rows = ecos_rows(payload, "StatisticSearch")
    return {
        "source": "한국은행 ECOS Open API",
        "service": "StatisticSearch",
        "count": len(rows),
        "values": [
            {
                "time": row.get("TIME"),
                "value": as_float(row.get("DATA_VALUE")),
                "unit": row.get("UNIT_NAME"),
                "stat_name": row.get("STAT_NAME"),
                "item_name": row.get("ITEM_NAME1"),
            }
            for row in rows
        ],
        "decision_use": "과거 거시 지표 흐름을 백테스트 해석과 시나리오 분석에 사용합니다.",
    }


def summarize_table_list(payload: dict[str, Any]) -> dict[str, Any]:
    rows = ecos_rows(payload, "StatisticTableList")
    return {
        "source": "한국은행 ECOS Open API",
        "service": "StatisticTableList",
        "count": len(rows),
        "tables": [
            {
                "stat_code": row.get("STAT_CODE"),
                "stat_name": row.get("STAT_NAME"),
                "cycle": row.get("CYCLE"),
                "searchable": row.get("SRCH_YN"),
                "org_name": row.get("ORG_NAME"),
            }
            for row in rows
        ],
    }


def summarize_item_list(payload: dict[str, Any]) -> dict[str, Any]:
    rows = ecos_rows(payload, "StatisticItemList")
    return {
        "source": "한국은행 ECOS Open API",
        "service": "StatisticItemList",
        "count": len(rows),
        "items": [
            {
                "stat_code": row.get("STAT_CODE"),
                "group": row.get("GRP_NAME"),
                "item_code": row.get("ITEM_CODE"),
                "item_name": row.get("ITEM_NAME"),
                "cycle": row.get("CYCLE"),
                "start_time": row.get("START_TIME"),
                "end_time": row.get("END_TIME"),
                "unit": row.get("UNIT_NAME"),
            }
            for row in rows
        ],
    }


def summarize_word(payload: dict[str, Any]) -> dict[str, Any]:
    rows = ecos_rows(payload, "StatisticWord")
    return {
        "source": "한국은행 ECOS Open API",
        "service": "StatisticWord",
        "count": len(rows),
        "words": [{"word": row.get("WORD"), "content": row.get("CONTENT")} for row in rows],
    }


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="ECOS adapter for FDN")
    parser.add_argument("--auth", help="ECOS API key. Prefer ECOS_API_KEY env var.")
    parser.add_argument("--fixture", help="Read a saved ECOS JSON response instead of calling the API.")
    parser.add_argument("--language", default=None)
    parser.add_argument("--start", type=int, default=None)
    parser.add_argument("--end", type=int, default=None)

    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("key-stats")

    table = sub.add_parser("table-list")
    table.add_argument("--stat-code")

    item = sub.add_parser("item-list")
    item.add_argument("--stat-code", required=True)

    word = sub.add_parser("word")
    word.add_argument("term")

    search = sub.add_parser("search")
    search.add_argument("--stat-code", required=True)
    search.add_argument("--cycle", required=True, help="A, S, Q, M, SM, or D")
    search.add_argument("--from-time", required=True)
    search.add_argument("--to-time", required=True)
    search.add_argument("--item-code1", default="?")
    search.add_argument("--item-code2", default="?")
    search.add_argument("--item-code3", default="?")
    search.add_argument("--item-code4", default="?")

    return parser


def main() -> int:
    load_env_file()
    parser = build_parser()
    args = parser.parse_args()
    language = args.language or os.environ.get("ECOS_LANGUAGE") or DEFAULT_LANGUAGE
    start = args.start or int(os.environ.get("ECOS_START") or str(DEFAULT_START))
    end = args.end or int(os.environ.get("ECOS_END") or str(DEFAULT_END))

    try:
        if args.command == "key-stats":
            payload = load_payload(args.fixture, "KeyStatisticList", args.auth, language, start, end, [])
            output = summarize_key_stats(payload)
        elif args.command == "table-list":
            service_args = [args.stat_code] if args.stat_code else []
            payload = load_payload(args.fixture, "StatisticTableList", args.auth, language, start, end, service_args)
            output = summarize_table_list(payload)
        elif args.command == "item-list":
            payload = load_payload(args.fixture, "StatisticItemList", args.auth, language, start, end, [args.stat_code])
            output = summarize_item_list(payload)
        elif args.command == "word":
            payload = load_payload(args.fixture, "StatisticWord", args.auth, language, start, end, [args.term])
            output = summarize_word(payload)
        elif args.command == "search":
            service_args = [
                args.stat_code,
                args.cycle,
                args.from_time,
                args.to_time,
                args.item_code1,
                args.item_code2,
                args.item_code3,
                args.item_code4,
            ]
            payload = load_payload(args.fixture, "StatisticSearch", args.auth, language, start, end, service_args)
            output = summarize_search(payload)
        else:
            raise ValueError(f"unknown command: {args.command}")
        print(json.dumps(output, ensure_ascii=False, indent=2))
        return 0
    except Exception as exc:  # noqa: BLE001 - CLI boundary
        print(json.dumps({"error": str(exc)}, ensure_ascii=False, indent=2), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
