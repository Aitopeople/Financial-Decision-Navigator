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
