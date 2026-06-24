#!/usr/bin/env python3
"""FDN local MCP server.

Provides two integration layers:
- SQLite-backed anonymized sample spending data.
- Safe fetch wrappers for Finlife, ECOS, and allowlisted JSON APIs.

The implementation uses only the Python standard library so the plugin does not
depend on package installation.
"""
from __future__ import annotations

import argparse
import csv
import json
import os
import sqlite3
import sys
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
DEFAULT_DB = DATA_DIR / "mock_spending.sqlite"
DEFAULT_CSV = DATA_DIR / "mock_spending.csv"
ALLOWED_FETCH_HOSTS = {
    "finlife.fss.or.kr",
    "ecos.bok.or.kr",
    "www.alphavantage.co",
    "alphavantage.co",
}


def load_env_file(start: Path | None = None) -> None:
    current = (start or Path.cwd()).resolve()
    candidates = [current, *current.parents]
    if ROOT not in candidates:
        candidates.append(ROOT)
    if ROOT.parent not in candidates:
        candidates.append(ROOT.parent)

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


def db_path() -> Path:
    configured = os.environ.get("FDN_MOCK_SPENDING_DB")
    return Path(configured).expanduser() if configured else DEFAULT_DB


def ensure_spending_db(path: Path | None = None) -> Path:
    target = path or db_path()
    target.parent.mkdir(parents=True, exist_ok=True)
    with sqlite3.connect(target) as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS spending (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id TEXT NOT NULL,
                date TEXT NOT NULL,
                category TEXT NOT NULL,
                amount INTEGER NOT NULL,
                merchant TEXT NOT NULL
            )
            """
        )
        count = conn.execute("SELECT COUNT(*) FROM spending WHERE user_id = ?", ("sample-user",)).fetchone()[0]
        if count == 0:
            with DEFAULT_CSV.open(encoding="utf-8-sig", newline="") as fh:
                rows = list(csv.DictReader(fh))
            conn.executemany(
                """
                INSERT INTO spending (user_id, date, category, amount, merchant)
                VALUES (:user_id, :date, :category, :amount, :merchant)
                """,
                rows,
            )
    return target


def get_mock_spending_summary(user_id: str = "sample-user", months: int = 3, goal: str = "home") -> dict[str, Any]:
    path = ensure_spending_db()
    limit_months = max(1, months)
    with sqlite3.connect(path) as conn:
        conn.row_factory = sqlite3.Row
        latest = conn.execute(
            "SELECT substr(max(date), 1, 7) AS latest_month FROM spending WHERE user_id = ?",
            (user_id,),
        ).fetchone()
        if latest is None or latest["latest_month"] is None:
            return {"user_id": user_id, "goal": goal, "message": "분석 가능한 mock 소비 데이터가 없습니다."}

        rows = conn.execute(
            """
            SELECT category, SUM(amount) AS total_amount, COUNT(*) AS transaction_count
            FROM spending
            WHERE user_id = ?
              AND date >= date((SELECT max(date) FROM spending WHERE user_id = ?), ?)
            GROUP BY category
            ORDER BY total_amount DESC
            """,
            (user_id, user_id, f"-{limit_months * 31} days"),
        ).fetchall()

    categories = [
        {
            "category": row["category"],
            "total_amount": int(row["total_amount"]),
            "monthly_average": round(int(row["total_amount"]) / limit_months),
            "transaction_count": int(row["transaction_count"]),
        }
        for row in rows
    ]
    top = categories[0]["category"] if categories else None
    return {
        "source": "local SQLite mock spending data",
        "user_id": user_id,
        "goal": goal,
        "months": limit_months,
        "categories": categories,
        "most_adjustable_category": top,
        "insight": f"현재 목표 달성을 위해 조정 가능한 소비 영역은 {top}입니다." if top else None,
        "guardrail": "타인 비교 없이 사용자의 목표 달성을 위한 조정 가능성만 설명합니다.",
    }


def list_mock_spending_transactions(user_id: str = "sample-user", limit: int = 20) -> dict[str, Any]:
    path = ensure_spending_db()
    safe_limit = min(max(1, limit), 100)
    with sqlite3.connect(path) as conn:
        conn.row_factory = sqlite3.Row
        rows = conn.execute(
            """
            SELECT date, category, amount, merchant
            FROM spending
            WHERE user_id = ?
            ORDER BY date DESC, id DESC
            LIMIT ?
            """,
            (user_id, safe_limit),
        ).fetchall()
    return {
        "source": "local SQLite mock spending data",
        "user_id": user_id,
        "transactions": [dict(row) for row in rows],
    }


def safe_url(url: str) -> urllib.parse.ParseResult:
    parsed = urllib.parse.urlparse(url)
    if parsed.hostname not in ALLOWED_FETCH_HOSTS:
        raise ValueError(f"Host is not allowlisted: {parsed.hostname}")
    if parsed.scheme == "https":
        return parsed
    if parsed.scheme == "http" and parsed.hostname == "finlife.fss.or.kr":
        return parsed
    raise ValueError("Only https URLs are allowed, except Finlife's documented HTTP endpoint")


def redacted_url(url: str) -> str:
    parsed = urllib.parse.urlparse(url)
    pairs = urllib.parse.parse_qsl(parsed.query, keep_blank_values=True)
    redacted = []
    for key, value in pairs:
        if key.lower() in {"apikey", "auth", "key"}:
            redacted.append((key, "REDACTED"))
        else:
            redacted.append((key, value))
    return urllib.parse.urlunparse(parsed._replace(query=urllib.parse.urlencode(redacted)))


def fetch_json(url: str, max_bytes: int = 200_000) -> dict[str, Any]:
    safe_url(url)
    with urllib.request.urlopen(url, timeout=15) as response:  # noqa: S310 - allowlisted URL
        raw = response.read(max(1, max_bytes) + 1)
    truncated = len(raw) > max_bytes
    if truncated:
        raw = raw[:max_bytes]
    text = raw.decode("utf-8", errors="replace")
    try:
        payload: Any = json.loads(text)
    except json.JSONDecodeError:
        payload = {"text_preview": text[:2000]}
    return {
        "source": "allowlisted HTTPS fetch",
        "url": redacted_url(url),
        "truncated": truncated,
        "payload": payload,
    }


def get_finlife_mortgage_rate_range(principal: int = 140_000_000, years: int = 30, fixture: str | None = None, limit: int = 5) -> dict[str, Any]:
    import finlife_client

    load_env_file()
    service = finlife_client.SERVICE_NAMES["mortgage"]
    payload = finlife_client.load_payload(
        fixture,
        service,
        None,
        os.environ.get("FINLIFE_TOP_FIN_GRP_NO") or finlife_client.BANK_GROUP,
        int(os.environ.get("FINLIFE_PAGE_NO") or "1"),
    )
    return finlife_client.summarize_mortgage(payload, principal, years, limit)


def get_ecos_key_stats(fixture: str | None = None) -> dict[str, Any]:
    import ecos_client

    load_env_file()
    payload = ecos_client.load_payload(
        fixture,
        "KeyStatisticList",
        None,
        os.environ.get("ECOS_LANGUAGE") or "kr",
        int(os.environ.get("ECOS_START") or "1"),
        int(os.environ.get("ECOS_END") or "100"),
        [],
    )
    return ecos_client.summarize_key_stats(payload)


TOOL_SCHEMAS: dict[str, dict[str, Any]] = {
    "get_mock_spending_summary": {
        "description": "Summarize local SQLite mock spending categories without peer comparison.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "user_id": {"type": "string", "default": "sample-user"},
                "months": {"type": "integer", "default": 3, "minimum": 1},
                "goal": {"type": "string", "default": "home"},
            },
        },
    },
    "list_mock_spending_transactions": {
        "description": "List recent transactions from local SQLite mock spending data.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "user_id": {"type": "string", "default": "sample-user"},
                "limit": {"type": "integer", "default": 20, "minimum": 1, "maximum": 100},
            },
        },
    },
    "fetch_json": {
        "description": "Fetch JSON from allowlisted HTTPS API hosts for controlled integration.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "url": {"type": "string"},
                "max_bytes": {"type": "integer", "default": 200000, "minimum": 1},
            },
            "required": ["url"],
        },
    },
    "get_finlife_mortgage_rate_range": {
        "description": "Fetch/summarize Finlife mortgage rate options for decision variables.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "principal": {"type": "integer", "default": 140000000},
                "years": {"type": "integer", "default": 30},
                "fixture": {"type": "string"},
                "limit": {"type": "integer", "default": 5},
            },
        },
    },
    "get_ecos_key_stats": {
        "description": "Fetch/summarize ECOS key macro statistics for scenario inputs.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "fixture": {"type": "string"},
            },
        },
    },
}


def call_tool(name: str, arguments: dict[str, Any] | None = None) -> dict[str, Any]:
    args = arguments or {}
    if name == "get_mock_spending_summary":
        return get_mock_spending_summary(
            user_id=str(args.get("user_id") or "sample-user"),
            months=int(args.get("months") or 3),
            goal=str(args.get("goal") or "home"),
        )
    if name == "list_mock_spending_transactions":
        return list_mock_spending_transactions(
            user_id=str(args.get("user_id") or "sample-user"),
            limit=int(args.get("limit") or 20),
        )
    if name == "fetch_json":
        return fetch_json(str(args["url"]), int(args.get("max_bytes") or 200_000))
    if name == "get_finlife_mortgage_rate_range":
        return get_finlife_mortgage_rate_range(
            principal=int(args.get("principal") or 140_000_000),
            years=int(args.get("years") or 30),
            fixture=args.get("fixture"),
            limit=int(args.get("limit") or 5),
        )
    if name == "get_ecos_key_stats":
        return get_ecos_key_stats(fixture=args.get("fixture"))
    raise ValueError(f"Unknown tool: {name}")


def tools_list() -> list[dict[str, Any]]:
    return [
        {
            "name": name,
            "description": schema["description"],
            "inputSchema": schema["inputSchema"],
        }
        for name, schema in TOOL_SCHEMAS.items()
    ]


def mcp_content(payload: Any) -> list[dict[str, str]]:
    return [{"type": "text", "text": json.dumps(payload, ensure_ascii=False, indent=2)}]


def handle_request(request: dict[str, Any]) -> dict[str, Any] | None:
    method = request.get("method")
    request_id = request.get("id")
    try:
        if method == "initialize":
            result = {
                "protocolVersion": request.get("params", {}).get("protocolVersion") or "2024-11-05",
                "capabilities": {"tools": {}},
                "serverInfo": {"name": "fdn-data", "version": "0.1.0"},
            }
        elif method == "tools/list":
            result = {"tools": tools_list()}
        elif method == "tools/call":
            params = request.get("params") or {}
            result = {"content": mcp_content(call_tool(params.get("name"), params.get("arguments") or {}))}
        elif method in {"notifications/initialized", "initialized"}:
            return None
        else:
            return {"jsonrpc": "2.0", "id": request_id, "error": {"code": -32601, "message": f"Method not found: {method}"}}
        return {"jsonrpc": "2.0", "id": request_id, "result": result}
    except Exception as exc:  # noqa: BLE001 - JSON-RPC boundary
        return {"jsonrpc": "2.0", "id": request_id, "error": {"code": -32000, "message": str(exc)}}


def serve() -> int:
    load_env_file()
    ensure_spending_db()
    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            request = json.loads(line)
        except json.JSONDecodeError as exc:
            response = {"jsonrpc": "2.0", "id": None, "error": {"code": -32700, "message": str(exc)}}
        else:
            response = handle_request(request)
        if response is not None:
            print(json.dumps(response, ensure_ascii=False), flush=True)
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="FDN data MCP server and test helper")
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("serve")
    sub.add_parser("init-db")
    call = sub.add_parser("call-tool")
    call.add_argument("name")
    call.add_argument("--arguments", default="{}")
    call.add_argument("--arg", action="append", default=[], help="Tool argument as key=value. Can be repeated.")
    return parser


def parse_scalar(value: str) -> Any:
    lowered = value.lower()
    if lowered == "true":
        return True
    if lowered == "false":
        return False
    if lowered in {"none", "null"}:
        return None
    try:
        return int(value)
    except ValueError:
        pass
    try:
        return float(value)
    except ValueError:
        return value


def parse_call_arguments(raw_json: str, pairs: list[str]) -> dict[str, Any]:
    try:
        payload = json.loads(raw_json)
    except json.JSONDecodeError as exc:
        if pairs:
            payload = {}
        else:
            raise exc
    if not isinstance(payload, dict):
        raise ValueError("--arguments must be a JSON object")
    for pair in pairs:
        if "=" not in pair:
            raise ValueError("--arg must use key=value format")
        key, value = pair.split("=", 1)
        key = key.strip()
        if not key:
            raise ValueError("--arg key must not be empty")
        payload[key] = parse_scalar(value.strip())
    return payload


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    load_env_file()
    if args.command == "serve":
        return serve()
    if args.command == "init-db":
        path = ensure_spending_db()
        print(json.dumps({"db_path": str(path), "status": "ready"}, ensure_ascii=False, indent=2))
        return 0
    if args.command == "call-tool":
        payload = call_tool(args.name, parse_call_arguments(args.arguments, args.arg))
        print(json.dumps(payload, ensure_ascii=False, indent=2))
        return 0
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
