---
name: path-explorer
description: Present structured financial decision paths for retirement, home ownership, or marriage fund planning without choosing for the user.
---

# Path Explorer

Use this skill after a decision type is known, or when the user asks what choices exist for a major financial decision.

## Goal

Show realistic option paths, tradeoffs, and when each path tends to fit. Do not pick one winner unless the user explicitly asks for prioritization.

## Supported Decisions

- `retirement`
- `home`
- `marriage`

## Output Shape

Use Korean and include:

1. A short restatement of the decision.
2. 3-4 paths.
3. For each path: core idea, strengths, risks, and required user data.
4. A four-choice reverse question asking which path or constraint the user wants to clarify next.

## Default Paths

Retirement:
- 배당 수입형
- 연금 수입형
- 자산 인출형
- 혼합형

Home:
- 청약 중심
- 투자 병행
- 즉시 매수
- 관망

Marriage:
- 예적금 중심
- 투자 병행
- 단기 집중

## Data Rule

This skill may describe decision paths without live data. When the user asks for exact product rates, dated market history, or macro values inside a path comparison, use the local `fdn-data` MCP tools instead of general web search:

- Mortgage path: `get_finlife_mortgage_rate_range`.
- Deposit/saving path: `get_finlife_savings_rate_range`.
- Macro scenario path: `get_ecos_key_stats` or `get_ecos_statistic_search`.
- Retirement market proxy path: `get_alphavantage_monthly_series`.

If a path is only conceptual, say that no live product recommendation is being made.

## Reverse Question Rule

End with one question that has exactly four options. The fourth option should be `직접 입력`.

For home ownership, prefer questions about housing type, contract type, region, timing, and monthly payment tolerance.

For retirement, prefer questions about income style, target timing, volatility tolerance, and spending floor.

For marriage funds, prefer questions about timeline, budget category, savings style, and required stability.

## Optional Local Helper

```bash
python src/scripts/fdn.py paths retirement
python src/scripts/fdn.py questions retirement
```
