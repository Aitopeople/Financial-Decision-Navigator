---
name: historical-backtest
description: Explain historical risk-return characteristics for financial decision paths using transparent public-market proxy assumptions.
---

# Historical Backtest

Use this skill when the user wants past performance context for a selected decision path or strategy.

## Goal

Provide historical comparison as context, not as a forecast or recommendation.

## Method

Use transparent public-market proxy assumptions from the bundled helper:

- S&P 500 proxy
- KOSPI proxy
- US dividend ETF proxy
- Korea/US government bond proxy
- Deposit-rate proxy

If exact live market data is required, say that the current helper uses static public-data proxy assumptions and ask whether the user wants live-data integration as a next step.

## Output Shape

Return Korean text plus a JSON-like summary:

- average_return
- max_drawdown
- volatility
- limitation
- interpretation

## Guardrails

- Say past performance does not guarantee future results.
- Avoid "this product is best".
- Compare paths by behavior under uncertainty, not by ranking the user.

## Optional Local Helper

```bash
python src/scripts/fdn.py backtest retirement mixed
```
