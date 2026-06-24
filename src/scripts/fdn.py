#!/usr/bin/env python3
"""Financial Decision Navigator command helper.

The helper is intentionally deterministic so plugin behavior can be validated
without external APIs or credentials.
"""
from __future__ import annotations

import argparse
import json
import math
from dataclasses import dataclass
from typing import Any


DECISION_KEYWORDS = {
    "retirement": ("은퇴", "노후", "연금", "배당", "생활비", "fire", "retire", "retirement"),
    "home": ("집", "주택", "아파트", "청약", "전세", "매수", "대출", "home", "house"),
    "marriage": ("결혼", "신혼", "예식", "혼수", "marriage", "wedding"),
    "education": ("교육", "학자금", "유학", "자녀", "education", "tuition"),
    "wealth_growth": ("목돈", "투자", "자산", "불리", "wealth", "invest"),
}

PATHS = {
    "retirement": [
        {"name": "배당 수입형", "strength": "현금흐름을 이해하기 쉽습니다.", "risk": "배당 삭감과 주가 변동을 함께 감수해야 합니다."},
        {"name": "연금 수입형", "strength": "예측 가능한 월 현금흐름을 만들기 쉽습니다.", "risk": "유동성과 물가상승 대응력이 제한될 수 있습니다."},
        {"name": "자산 인출형", "strength": "전체 자산을 유연하게 운용할 수 있습니다.", "risk": "초기 하락장에서 인출하면 회복력이 약해질 수 있습니다."},
        {"name": "혼합형", "strength": "현금흐름과 성장성을 나눠 관리할 수 있습니다.", "risk": "관리해야 할 기준과 리밸런싱 규칙이 필요합니다."},
    ],
    "home": [
        {"name": "청약 중심", "strength": "초기 자금 부담을 계획적으로 관리할 수 있습니다.", "risk": "당첨 불확실성과 대기 시간이 있습니다."},
        {"name": "투자 병행", "strength": "구매 시점 전까지 자산 성장 가능성을 열어둡니다.", "risk": "시장 하락 시 매수 자금이 줄어들 수 있습니다."},
        {"name": "즉시 매수", "strength": "거주 안정성과 가격 상승 참여 가능성이 있습니다.", "risk": "대출 부담과 가격 하락 리스크가 즉시 발생합니다."},
        {"name": "관망", "strength": "가격과 금리 변화를 더 확인할 수 있습니다.", "risk": "원하는 지역의 가격이 먼저 오를 수 있습니다."},
    ],
    "marriage": [
        {"name": "예적금 중심", "strength": "원금 변동을 줄이고 목표 날짜에 맞추기 쉽습니다.", "risk": "물가 상승이나 비용 증가를 따라가기 어려울 수 있습니다."},
        {"name": "투자 병행", "strength": "기간이 충분하면 일부 성장 가능성을 가져갈 수 있습니다.", "risk": "예식 일정이 가까울수록 손실 회복 시간이 부족합니다."},
        {"name": "단기 집중", "strength": "소비 조정과 저축률 상승으로 실행력이 높습니다.", "risk": "생활 만족도 저하나 지속 가능성 문제가 생길 수 있습니다."},
    ],
}

PIPELINES = {
    "home": {
        "skills": ["decision-framing", "path-explorer", "scenario-simulator", "action-planner", "behavior-insight"],
        "required_inputs": [
            "home_price",
            "cash_on_hand",
            "loan_amount",
            "monthly_income",
            "fixed_expense",
            "monthly_saving_capacity",
            "desired_region_or_house_type",
            "expected_residence_years",
        ],
        "data_sources": ["Finlife mortgage rates", "ECOS macro indicators", "Local mock spending MCP"],
        "trigger_prompt": "집값, 보유현금, 예상 대출금액, 월소득, 고정지출, 저축 가능액을 알려주시면 매수와 관망 경로를 비교해보겠습니다.",
    },
    "retirement": {
        "skills": ["decision-framing", "path-explorer", "historical-backtest", "scenario-simulator", "action-planner"],
        "required_inputs": [
            "target_retirement_age",
            "target_retirement_amount",
            "current_asset",
            "monthly_budget",
            "risk_tolerance",
            "preferred_income_path",
        ],
        "data_sources": ["Alpha Vantage public-market proxies", "ECOS inflation and rate indicators"],
        "trigger_prompt": "목표 은퇴 나이, 목표 은퇴자금, 현재 자산, 매월 투입 가능 금액을 알려주시면 은퇴 경로를 비교해보겠습니다.",
    },
    "marriage": {
        "skills": ["decision-framing", "path-explorer", "scenario-simulator", "action-planner", "behavior-insight"],
        "required_inputs": [
            "target_marriage_budget",
            "target_date",
            "current_asset",
            "monthly_saving_capacity",
            "risk_tolerance",
            "major_cost_categories",
        ],
        "data_sources": ["Finlife deposit and savings rates", "ECOS inflation indicators", "Local mock spending MCP"],
        "trigger_prompt": "목표 결혼 예산, 준비 기간, 현재 모아둔 금액, 매월 저축 가능액을 알려주시면 저축 중심과 투자 병행 경로를 비교해보겠습니다.",
    },
    "education": {
        "skills": ["decision-framing"],
        "required_inputs": ["target_amount", "target_date", "current_asset", "monthly_budget"],
        "data_sources": [],
        "trigger_prompt": "교육 자금은 다음 단계 확장 범위입니다. 목표 금액과 시점을 알려주시면 우선 실행 계획 형태로 정리할 수 있습니다.",
    },
    "wealth_growth": {
        "skills": ["decision-framing"],
        "required_inputs": ["target_amount", "time_horizon", "current_asset", "monthly_budget", "risk_tolerance"],
        "data_sources": [],
        "trigger_prompt": "자산 성장 목표는 다음 단계 확장 범위입니다. 목표 금액, 기간, 현재 자산, 월 예산을 알려주시면 의사결정 프레임부터 정리하겠습니다.",
    },
    "uncertain": {
        "skills": ["decision-framing"],
        "required_inputs": ["primary_goal", "target_date", "current_asset", "monthly_budget"],
        "data_sources": [],
        "trigger_prompt": "은퇴, 내 집 마련, 결혼 자금 중 어느 목표에 가장 가까운지 먼저 알려주세요.",
    },
}

BACKTESTS = {
    "dividend": {"average_return": 7.1, "max_drawdown": -31.5, "volatility": 15.2, "proxy": "US dividend ETF proxy"},
    "pension": {"average_return": 3.4, "max_drawdown": -8.2, "volatility": 5.1, "proxy": "government bond and deposit proxy"},
    "withdrawal": {"average_return": 8.4, "max_drawdown": -36.8, "volatility": 17.4, "proxy": "S&P 500 and KOSPI blended proxy"},
    "mixed": {"average_return": 5.8, "max_drawdown": -18.6, "volatility": 9.7, "proxy": "equity, dividend, bond, and deposit blended proxy"},
    "deposit": {"average_return": 2.5, "max_drawdown": 0.0, "volatility": 0.7, "proxy": "deposit-rate proxy"},
}

SCENARIOS = {
    "rate_rise": {
        "label": "금리 상승",
        "impact": "대출 부담과 채권 가격 변동성이 커질 수 있습니다.",
        "watch": "변동금리 비중, 월 상환액, 현금성 자산 비중",
        "adjustment": "확정 지출을 먼저 계산하고 투자성 자금과 필수 자금을 분리합니다.",
    },
    "rate_fall": {
        "label": "금리 하락",
        "impact": "대출 부담은 완화될 수 있지만 자산 가격이 빠르게 움직일 수 있습니다.",
        "watch": "대출 갈아타기 조건, 목표 자산 가격, 예금 만기",
        "adjustment": "의사결정 가격대를 미리 정해 충동적 진입을 줄입니다.",
    },
    "recession": {
        "label": "경기 침체",
        "impact": "소득 안정성과 위험자산 회복 기간이 핵심 변수가 됩니다.",
        "watch": "비상금 개월 수, 고정비, 손실 허용 기간",
        "adjustment": "목표 날짜가 가까운 돈은 변동성을 낮추고 장기 자금은 규칙을 유지합니다.",
    },
    "high_growth": {
        "label": "고성장",
        "impact": "위험자산에는 우호적일 수 있으나 과도한 낙관이 생기기 쉽습니다.",
        "watch": "목표 대비 초과 위험, 레버리지, 자산 쏠림",
        "adjustment": "목표 달성률이 높아질수록 일부 금액을 안정 영역으로 옮깁니다.",
    },
}


@dataclass
class CategorySpend:
    name: str
    amount: int
    flexibility: float = 1.0


def emit(data: dict[str, Any]) -> None:
    print(json.dumps(data, ensure_ascii=False, indent=2))


def frame_question(question: str) -> dict[str, Any]:
    text = question.lower()
    scores: dict[str, int] = {}
    for decision_type, keywords in DECISION_KEYWORDS.items():
        scores[decision_type] = sum(1 for keyword in keywords if keyword.lower() in text)

    best_type = max(scores, key=scores.get)
    best_score = scores[best_type]
    if best_score == 0:
        return {
            "decision_type": "uncertain",
            "confidence": 0.35,
            "interpreted_concern": "금융 의사결정 고민으로 보이지만 목표 유형을 더 확인해야 합니다.",
            "next_question": "가장 먼저 정리하고 싶은 목표가 은퇴, 내 집 마련, 결혼 자금 중 어디에 가까운가요?",
        }

    total = sum(scores.values()) or 1
    confidence = min(0.95, 0.55 + (best_score / total) * 0.35)
    labels = {
        "retirement": "은퇴 준비",
        "home": "내 집 마련",
        "marriage": "결혼 자금 준비",
        "education": "교육 자금 준비",
        "wealth_growth": "자산 성장",
    }
    return {
        "decision_type": best_type,
        "confidence": round(confidence, 2),
        "interpreted_concern": f"{labels[best_type]}에 대한 의사결정으로 이해했습니다.",
        "next_question": "목표 시점, 현재 자산, 매월 투입 가능한 금액을 알려주시면 선택지를 더 구체화할 수 있습니다.",
    }


def list_paths(decision_type: str) -> dict[str, Any]:
    paths = PATHS.get(decision_type)
    if not paths:
        return {
            "decision_type": decision_type,
            "supported": False,
            "message": "현재 retirement, home, marriage 의사결정을 우선 지원합니다.",
        }
    return {
        "decision_type": decision_type,
        "paths": paths,
        "next_question": "어떤 경로를 기준으로 과거 특성이나 시나리오를 살펴볼까요?",
    }


def navigate(question: str) -> dict[str, Any]:
    frame = frame_question(question)
    decision_type = str(frame["decision_type"])
    pipeline = PIPELINES.get(decision_type, PIPELINES["uncertain"])
    supported_decision = decision_type in {"home", "retirement", "marriage"}
    next_skill = pipeline["skills"][1] if supported_decision and len(pipeline["skills"]) > 1 else "decision-framing"
    return {
        "question": question,
        **frame,
        "supported_decision": supported_decision,
        "pipeline": pipeline["skills"],
        "next_skill": next_skill,
        "required_inputs": pipeline["required_inputs"],
        "data_sources": pipeline["data_sources"],
        "trigger_response": pipeline["trigger_prompt"],
        "routing_intent": "사용자의 다음 입력이 필요한 스킬을 자연스럽게 호출하도록 유도합니다.",
    }


def backtest(decision_type: str, strategy: str) -> dict[str, Any]:
    data = BACKTESTS.get(strategy, BACKTESTS["mixed"])
    return {
        "decision_type": decision_type,
        "strategy": strategy,
        **data,
        "limitation": "정적 프록시입니다. 실제 투자 성과나 미래 수익을 보장하지 않습니다.",
        "interpretation": "숫자는 선택지의 변동성과 손실 가능성을 이해하기 위한 참고값입니다.",
    }


def scenario(decision_type: str, strategy: str, scenario_name: str) -> dict[str, Any]:
    data = SCENARIOS.get(scenario_name)
    if data is None:
        return {"supported": False, "message": "지원 시나리오: rate_rise, rate_fall, recession, high_growth"}
    return {
        "decision_type": decision_type,
        "strategy": strategy,
        "scenario": scenario_name,
        **data,
        "caution": "이 내용은 시나리오 사고를 돕기 위한 것이며 시장 예측이 아닙니다.",
    }


def future_value(monthly: float, years: float, annual_return: float) -> float:
    months = max(0, int(round(years * 12)))
    if months == 0:
        return 0.0
    monthly_return = annual_return / 12
    if abs(monthly_return) < 1e-12:
        return monthly * months
    return monthly * (((1 + monthly_return) ** months - 1) / monthly_return)


def required_monthly(gap: float, years: float, annual_return: float) -> float:
    months = max(1, int(round(years * 12)))
    monthly_return = annual_return / 12
    if abs(monthly_return) < 1e-12:
        return gap / months
    factor = ((1 + monthly_return) ** months - 1) / monthly_return
    return gap / factor


def estimate_years(gap: float, monthly_budget: float, annual_return: float) -> float:
    if gap <= 0:
        return 0.0
    if monthly_budget <= 0:
        return math.inf
    monthly_return = annual_return / 12
    if abs(monthly_return) < 1e-12:
        return gap / monthly_budget / 12
    months = math.log(1 + gap * monthly_return / monthly_budget) / math.log(1 + monthly_return)
    return months / 12


def action_plan(goal: str, target_amount: int, current_asset: int, monthly_budget: int, annual_return: float, target_years: float | None) -> dict[str, Any]:
    gap = max(0, target_amount - current_asset)
    years = estimate_years(gap, monthly_budget, annual_return)
    result = {
        "goal": goal,
        "target_amount": target_amount,
        "current_asset": current_asset,
        "gap": gap,
        "monthly_budget": monthly_budget,
        "annual_return_assumption": annual_return,
        "estimated_years": None if math.isinf(years) else round(years, 1),
        "next_action": "이번 달에는 목표 계좌와 생활비 계좌를 분리하고 자동 이체 기준을 먼저 정합니다.",
    }
    if target_years is not None:
        need = required_monthly(gap, target_years, annual_return)
        result["target_years"] = target_years
        result["required_monthly_amount"] = round(need)
        result["budget_status"] = "enough_under_assumption" if monthly_budget >= need else "gap_exists_under_assumption"
    return result


def parse_category(raw: str) -> CategorySpend:
    name, _, amount_text = raw.partition("=")
    if not name or not amount_text:
        raise argparse.ArgumentTypeError("category must look like 이름=금액")
    return CategorySpend(name=name.strip(), amount=int(amount_text.replace(",", "").strip()))


def behavior(goal: str, categories: list[CategorySpend]) -> dict[str, Any]:
    if not categories:
        return {"goal": goal, "message": "분석할 소비 카테고리가 필요합니다."}
    ranked = sorted(categories, key=lambda item: item.amount * item.flexibility, reverse=True)
    top = ranked[0]
    return {
        "goal": goal,
        "reviewed_categories": [{"name": item.name, "amount": item.amount} for item in categories],
        "most_adjustable_category": top.name,
        "insight": f"현재 목표 달성을 위해 조정 가능한 소비 영역은 {top.name}입니다.",
        "next_action": f"다음 한 달 동안 {top.name} 지출의 기준 금액을 정하고 초과분을 목표 자금으로 이동해 보세요.",
    }


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Financial Decision Navigator helper")
    sub = parser.add_subparsers(dest="command", required=True)

    frame = sub.add_parser("frame")
    frame.add_argument("question")

    nav = sub.add_parser("navigate")
    nav.add_argument("question")

    paths = sub.add_parser("paths")
    paths.add_argument("decision_type")

    bt = sub.add_parser("backtest")
    bt.add_argument("decision_type")
    bt.add_argument("strategy")

    sc = sub.add_parser("scenario")
    sc.add_argument("decision_type")
    sc.add_argument("strategy")
    sc.add_argument("scenario")

    action = sub.add_parser("action")
    action.add_argument("--goal", required=True)
    action.add_argument("--target-amount", type=int, required=True)
    action.add_argument("--current-asset", type=int, required=True)
    action.add_argument("--monthly-budget", type=int, required=True)
    action.add_argument("--annual-return", type=float, default=0.0)
    action.add_argument("--target-years", type=float)

    beh = sub.add_parser("behavior")
    beh.add_argument("--goal", required=True)
    beh.add_argument("--category", type=parse_category, action="append", default=[])

    return parser


def main() -> int:
    args = build_parser().parse_args()
    if args.command == "frame":
        emit(frame_question(args.question))
    elif args.command == "navigate":
        emit(navigate(args.question))
    elif args.command == "paths":
        emit(list_paths(args.decision_type))
    elif args.command == "backtest":
        emit(backtest(args.decision_type, args.strategy))
    elif args.command == "scenario":
        emit(scenario(args.decision_type, args.strategy, args.scenario))
    elif args.command == "action":
        emit(action_plan(args.goal, args.target_amount, args.current_asset, args.monthly_budget, args.annual_return, args.target_years))
    elif args.command == "behavior":
        emit(behavior(args.goal, args.category))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
