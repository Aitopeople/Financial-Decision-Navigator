# Alpha Vantage API Notes for FDN

This document summarizes the Alpha Vantage APIs that are useful for Financial Decision Navigator(FDN). The goal is not product recommendation. Alpha Vantage data should be used as public-market proxy data for `historical-backtest` and as supplementary global scenario inputs.

Sources checked:

- Context7 library: `/websites/alphavantage_co`
- Official documentation: https://www.alphavantage.co/documentation/
- Official MCP entry point listed by Alpha Vantage: https://mcp.alphavantage.co

## Fit for FDN

Alpha Vantage is useful for:

- US ETF/equity price series used as simple backtest proxies.
- Dividend-adjusted or monthly adjusted return calculations.
- ETF profile and holdings metadata for explaining what a proxy represents.
- USD/KRW-adjacent FX context through major FX pairs when needed.
- US treasury yield, federal funds rate, CPI, and inflation as global macro scenario inputs.

Alpha Vantage is not the primary source for:

- Korean mortgage rates. Use Finlife.
- Korean macro indicators. Use ECOS.
- Korean real estate transaction data. Deferred for now.
- Personalized advice or product recommendation.

## Auth and Free Tier Handling

All requests use:

```text
https://www.alphavantage.co/query
```

Common parameters:

| Parameter | Required | Notes |
|---|---:|---|
| `function` | yes | API function name, e.g. `TIME_SERIES_MONTHLY_ADJUSTED` |
| `apikey` | yes | Store in `.env`, never in logs or README |
| `datatype` | no | `json` default, `csv` optional where supported |

Add this to `.env` when implementing the client:

```env
ALPHAVANTAGE_API_KEY=
ALPHAVANTAGE_CACHE_DIR=.cache/alphavantage
```

Free usage is limited. For examples and development, prefer cached responses and monthly series over repeated daily calls.

## Recommended Initial Endpoints

### 1. Monthly Adjusted Equity/ETF Series

Use for:

- Retirement backtest proxies.
- Marriage fund investment-path proxy.
- Long-term asset growth assumptions.

Endpoint:

```text
GET /query?function=TIME_SERIES_MONTHLY_ADJUSTED&symbol={symbol}&apikey={key}
```

Required:

- `function=TIME_SERIES_MONTHLY_ADJUSTED`
- `symbol`, for example `SPY`, `QQQ`, `SCHD`, `BND`, `TLT`
- `apikey`

Optional:

- `datatype=json|csv`

Useful response fields:

- Monthly open/high/low/close
- Adjusted close
- Volume
- Dividend amount

FDN usage:

- Calculate monthly total-return-like proxy from adjusted close.
- Estimate CAGR, volatility, maximum drawdown.
- Explain limitations clearly: proxy ETF data is not a personalized portfolio recommendation.

Preferred over daily data because it is smaller and naturally fits long-term decisions.

### 2. Daily Equity/ETF Series

Use for:

- Shorter backtest windows.
- Volatility and drawdown examples.

Endpoint:

```text
GET /query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={key}
```

Required:

- `function=TIME_SERIES_DAILY`
- `symbol`
- `apikey`

Optional:

- `outputsize=compact|full`
- `datatype=json|csv`

Notes:

- Official docs state `compact` returns latest 100 data points.
- Full-length daily history is premium for `TIME_SERIES_DAILY`.
- For free-tier usage, avoid relying on `outputsize=full`.

FDN usage:

- Use only if a short recent-period illustration is enough.
- For long-term initial backtests, prefer monthly adjusted series.

### 3. Daily Adjusted Equity/ETF Series

Use for:

- Adjusted close and dividend/split-aware daily analysis.

Endpoint:

```text
GET /query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&apikey={key}
```

Required:

- `function=TIME_SERIES_DAILY_ADJUSTED`
- `symbol`
- `apikey`

Optional:

- `outputsize=compact|full`
- `datatype=json|csv`
- `entitlement`

Important:

- The official docs mark this as a premium API function.
- Do not make this the default dependency unless the available API key supports it.

FDN usage:

- Nice-to-have for more precise daily total-return analysis.
- Fallback to `TIME_SERIES_MONTHLY_ADJUSTED` when unavailable.

### 4. ETF Profile and Holdings

Use for:

- Explaining what an ETF proxy represents before showing historical metrics.
- Differentiating equity, bond, dividend, or growth proxies.

Endpoint:

```text
GET /query?function=ETF_PROFILE&symbol={symbol}&apikey={key}
```

Required:

- `function=ETF_PROFILE`
- `symbol`, for example `QQQ`
- `apikey`

Useful response concepts:

- Net assets
- Expense ratio
- Turnover
- Holdings/constituents
- Asset-type and sector allocation

FDN usage:

- Show why a proxy was selected.
- Example: `SCHD` for dividend-oriented proxy, `SPY` for broad US equity, `BND` or `TLT` for bond proxy.
- Keep wording neutral: "proxy characteristics", not "recommended ETF".

### 5. Global Quote

Use for:

- Current price snapshot in examples.
- Sanity check that symbol exists.

Endpoint:

```text
GET /query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={key}
```

Required:

- `function=GLOBAL_QUOTE`
- `symbol`
- `apikey`

Optional:

- `datatype=json|csv`

Important:

- Official docs state the quote endpoint is updated at end of trading day by default for all users.
- Realtime or 15-minute delayed US quotes require premium access.

FDN usage:

- Use only as context.
- Do not base a decision flow on realtime trading signals.

### 6. FX Daily

Use for:

- Global scenario context when a user asks about USD exposure.
- Explaining currency risk in US ETF paths.

Endpoint:

```text
GET /query?function=FX_DAILY&from_symbol={from}&to_symbol={to}&apikey={key}
```

Required:

- `function=FX_DAILY`
- `from_symbol`, three-letter currency code, e.g. `USD`
- `to_symbol`, three-letter currency code, e.g. `KRW` if supported, or `EUR`, `JPY`, `USD`
- `apikey`

Optional:

- `outputsize=compact|full`
- `datatype=json|csv`

Useful response fields:

- Date
- Open
- High
- Low
- Close

FDN usage:

- Currency-risk explanation, not FX trading.
- If `USDKRW` support is insufficient, use ECOS exchange-rate data instead.

### 7. Treasury Yield

Use for:

- Bond scenario input.
- Retirement withdrawal-path stress discussion.
- Interest-rate environment context.

Endpoint:

```text
GET /query?function=TREASURY_YIELD&interval={interval}&maturity={maturity}&apikey={key}
```

Required:

- `function=TREASURY_YIELD`
- `apikey`

Optional:

- `interval=daily|weekly|monthly`; default is `monthly`
- `maturity=3month|2year|5year|7year|10year|30year`; default is `10year`
- `datatype=json|csv`

FDN usage:

- Use `10year` monthly as default global rate proxy.
- Use `3month` vs `10year` to explain short-rate/long-rate environment.

### 8. Federal Funds Rate

Use for:

- US policy-rate context.
- Scenario comparison with Korean rate data from ECOS.

Endpoint:

```text
GET /query?function=FEDERAL_FUNDS_RATE&interval={interval}&apikey={key}
```

Required:

- `function=FEDERAL_FUNDS_RATE`
- `apikey`

Optional:

- `interval=daily|weekly|monthly`; default is `monthly`
- `datatype=json|csv`

FDN usage:

- Supplement ECOS for global macro commentary.
- Use monthly interval for low call volume.

### 9. CPI

Use for:

- Inflation scenario input.
- Retirement real-income discussion.

Endpoint:

```text
GET /query?function=CPI&interval={interval}&apikey={key}
```

Required:

- `function=CPI`
- `apikey`

Optional:

- `interval=monthly|semiannual`; default is `monthly`
- `datatype=json|csv`

FDN usage:

- Explain why nominal return and real return differ.
- For Korean inflation, prefer ECOS. Use CPI only for US/global context.

### 10. Inflation

Use for:

- Long-run inflation assumption.
- Real return adjustment.

Endpoint:

```text
GET /query?function=INFLATION&apikey={key}
```

Required:

- `function=INFLATION`
- `apikey`

Optional:

- `datatype=json|csv`

FDN usage:

- Long-run US inflation proxy.
- Useful for retirement planning explanations where purchasing power matters.

## Suggested Symbols for Example Proxies

| FDN path | Proxy symbols | Purpose |
|---|---|---|
| Broad equity growth | `SPY`, `QQQ` | US equity return/risk proxy |
| Dividend income path | `SCHD`, `VIG` | Dividend-oriented proxy |
| Bond/stability path | `BND`, `TLT`, `IEF` | Rate-sensitive bond proxy |
| Mixed portfolio | `SPY` + `BND` or `SCHD` + `BND` | Simple blended path |
| Currency context | `USD` to target currency via FX endpoint, or ECOS for KRW | FX risk explanation |

These are proxy examples. The plugin should not say "buy this ETF".

## FDN Integration Design

Recommended wrapper commands/tools:

```text
get_asset_proxy_returns(symbols, interval="monthly", years=20)
get_etf_profile(symbol)
get_global_rate_context(maturity="10year", interval="monthly")
get_us_inflation_context(interval="monthly")
get_fx_context(from_symbol, to_symbol)
```

Recommended response normalized by FDN:

```json
{
  "source": "Alpha Vantage",
  "proxy": "SPY",
  "series": "TIME_SERIES_MONTHLY_ADJUSTED",
  "period": {
    "start": "YYYY-MM-DD",
    "end": "YYYY-MM-DD"
  },
  "metrics": {
    "cagr": 0.0,
    "volatility": 0.0,
    "max_drawdown": 0.0
  },
  "limitations": [
    "Public-market proxy, not product recommendation",
    "Past performance does not guarantee future results",
    "KRW investor outcomes can differ due to FX and tax"
  ]
}
```

## API Priority

For this plugin, implement in this order:

1. `TIME_SERIES_MONTHLY_ADJUSTED`
2. `ETF_PROFILE`
3. `TREASURY_YIELD`
4. `CPI` or `INFLATION`
5. `FX_DAILY`
6. `GLOBAL_QUOTE`
7. `TIME_SERIES_DAILY` only if short-window analysis is needed
8. `TIME_SERIES_DAILY_ADJUSTED` only if premium access is available

## Guardrails

- Store API keys in `.env` only.
- Cache responses to avoid rate-limit failures.
- Avoid realtime trading language.
- Never rank products as "best".
- Always label symbols as proxies.
- Prefer ECOS for Korean macro and Finlife for Korean rates.
- Mention that US data may not map cleanly to Korean household decisions.
