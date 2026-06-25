---
name: action-planner
description: Convert a financial goal into a gap, estimated timeline, and monthly action range using user-provided numbers.
---

# Action Planner

Use this skill when the user provides or can provide target amount, current assets, monthly budget, time horizon, or target date.

## Goal

Turn the decision into an executable plan with assumptions visible.

## Required Inputs

- goal
- target_amount
- current_asset
- monthly_budget

Optional:

- annual_return
- target_years

## Data Rule

If the plan uses real product rates or dated market/macro assumptions, use the local `fdn-data` MCP tools before answering:

- `get_finlife_mortgage_rate_range` for mortgage payment assumptions.
- `get_finlife_savings_rate_range` for deposit or saving-rate assumptions.
- `get_ecos_key_stats` or `get_ecos_statistic_search` for macro assumptions.
- `get_alphavantage_monthly_series` for public-market proxy history.

Do not substitute general web search for these values. If no API value is available, keep the calculation on user-provided assumptions and label them clearly.

## Output Shape

Use Korean and include:

- gap
- estimated_years
- required_monthly_amount
- whether the current monthly budget is enough under the stated assumption
- next action for the coming month

## Guardrails

- Treat return assumptions as scenario inputs, not promises.
- Avoid shame language.
- If data is missing, ask for the smallest missing set of numbers.

## Optional Local Helper

```bash
python src/scripts/fdn.py action --goal retirement --target-amount 700000000 --current-asset 100000000 --monthly-budget 500000 --annual-return 0.04
```
