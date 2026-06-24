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

## Guardrails

- Do not predict exact market levels.
- Do not recommend a specific security.
- Keep language supportive and non-judgmental.

## Optional Local Helper

```bash
python src/scripts/fdn.py scenario retirement dividend recession
```
