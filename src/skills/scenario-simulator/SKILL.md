---
name: scenario-simulator
description: Simulate how retirement, home, or marriage fund decision paths may behave in rate-rise, rate-fall, recession, or high-growth scenarios.
---

# Scenario Simulator

Use this skill when the user asks "what happens if" under market or economic conditions.

## Supported Scenarios

- `rate_rise`: 금리 상승
- `rate_fall`: 금리 하락
- `recession`: 경기 침체
- `high_growth`: 고성장

## Output Shape

Use Korean and include:

1. Scenario name.
2. Expected impact on the selected path.
3. What the user should watch.
4. A practical adjustment option.
5. A caution that this is scenario reasoning, not a prediction.

## Data Rule

When the scenario depends on current rates, product rates, inflation, FX, or dated macro values, use the local `fdn-data` MCP tools first:

- `get_ecos_key_stats` for latest Korean macro snapshots.
- `get_ecos_statistic_search` for explicit historical Korean macro series.
- `get_finlife_mortgage_rate_range` for mortgage-rate decision variables.
- `get_finlife_savings_rate_range` for deposit/saving-rate decision variables.

Do not use general web search for these data points while the MCP/API tools can answer them. If an API call fails or a required statistic code is unknown, state that limitation rather than filling the gap with an unsourced web value.

## Guardrails

- Do not predict exact market levels.
- Do not recommend a specific security.
- Keep language supportive and non-judgmental.

## Optional Local Helper

```bash
python src/scripts/fdn.py scenario retirement dividend recession
```
