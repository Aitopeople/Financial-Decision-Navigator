---
name: historical-backtest
description: Explain historical risk-return characteristics for financial decision paths using transparent public-market proxy assumptions.
---

# Historical Backtest

Use this skill when the user wants past performance context for a selected decision path or strategy.

## Goal

Provide historical comparison as context, not as a forecast or recommendation.

## Method

When the user asks for exact past data, live historical values, or a dated comparison, use the local `fdn-data` MCP tools before answering:

- `get_alphavantage_monthly_series` for public-market proxy series such as SPY.
- `get_ecos_statistic_search` for Korean macro historical time series when the statistic code and item code are known.
- `get_ecos_key_stats` only for latest key macro snapshots, not for multi-period history.

Do not use general web search for historical market, macro, rate, or product values while these MCP/API tools can answer the request. If the required code, symbol, or API key is unavailable, say exactly what is missing and ask for the smallest missing input.

For rough strategy framing only, you may use transparent public-market proxy assumptions from the bundled helper:

- S&P 500 proxy.
- KOSPI proxy.
- US dividend ETF proxy.
- Korea/US government bond proxy.
- Deposit-rate proxy.

If a response uses the static helper instead of an MCP/API result, label it as a static proxy assumption and do not present it as live historical data.

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
