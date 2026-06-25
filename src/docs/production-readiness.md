# Production Readiness Review

FDN MVP는 의사결정 흐름을 증명하는 데 초점을 맞췄습니다. 프로덕션 수준에서는 사용자가 실제 돈과 생활 결정을 다루기 때문에, 아래 영역은 API 기반 데이터 또는 명시적인 사용자 입력 없이는 단정적으로 답하지 않아야 합니다.

For the implementation stack and build phases, see `production-stack.md`.

## More API-Backed Areas Needed

### 1. Home Ownership

Current coverage:

- Finlife mortgage rates.
- ECOS rates, inflation, FX, and macro snapshots.
- User-provided price, cash, loan amount, income, expenses.

Production gaps:

- Regional home price history and transaction volume.
- Jeonse and monthly rent market levels.
- Region code normalization.
- Apartment/officetel/house type differences.
- Mortgage eligibility, LTV, DSR, and policy-loan constraints.
- Maintenance fees, taxes, acquisition costs, moving costs.
- Jeonse loan and rent-house loan products.

API direction:

- Add `get_home_market_snapshot(region, home_type, contract_type, ym_range)`.
- Add `get_rent_or_jeonse_snapshot(region, home_type, ym_range)`.
- Extend Finlife wrapper to `rentHouseLoanProductsSearch`.
- Add policy/eligibility rules as versioned local rule tables, not free-form LLM text.

Do not fill these gaps with general web search. If the API is unavailable, ask the user for the value or label the response as an assumption.

### 2. Retirement

Current coverage:

- Alpha Vantage monthly proxy series.
- ECOS inflation and rate indicators.
- Static helper for rough strategy framing.

Production gaps:

- Korean pension products, IRP, pension savings, annuity terms.
- Tax benefits, withdrawal constraints, and contribution limits.
- KRW-based portfolio proxy data beyond US ETFs.
- FX impact for foreign ETF paths.
- User spending floor and healthcare reserve assumptions.

API direction:

- Add `get_retirement_product_terms(product_type, provider_filter)`.
- Add `get_asset_proxy_returns(symbols, currency, years)` with caching.
- Add `get_pension_rule_snapshot(year, user_age, income_band)` as a governed rules endpoint.

Use Alpha Vantage as a market proxy only. Do not describe it as a product recommendation source.

### 3. Marriage Fund

Current coverage:

- Finlife deposit and saving rates.
- ECOS inflation indicators.
- Local mock spending categories.

Production gaps:

- Wedding cost category ranges by region and event scale.
- Housing deposit assumptions for newlyweds.
- Shared contribution model between partners.
- Timing risk for short horizon investments.
- Gift/loan/family support assumptions.

API direction:

- Add `get_marriage_cost_benchmark(region, event_scale, ym)`.
- Add `get_housing_deposit_snapshot(region, contract_type, home_type)`.
- Keep deposit/saving product rates API-backed through Finlife.

### 4. Behavior Insight

Current coverage:

- Local SQLite mock spending data.

Production gaps:

- Real user consent and account linking.
- Spending categorization quality.
- Recurring versus one-off spending separation.
- Income, cash flow, and account balance stability.
- Privacy, deletion, audit log, and data minimization.

API direction:

- Add `get_user_cashflow_summary(user_id, consent_scope, months)`.
- Add `get_recurring_spending_summary(user_id, months)`.
- Add consent status and data freshness to every response.

Do not compare users to peers. This product's edge is self-clarification and behavior options, not ranking.

## AX Reverse Question Standard

FDN should not only answer. It should help users articulate what they actually mean.

Every vague decision response should end with one four-choice reverse question:

```text
주거문제를 이야기하시는데 어떤 형태의 주거를 원하시나요?
1. 아파트
2. 주택
3. 오피스텔
4. 직접 입력
```

Rules:

- Ask one question at a time, or at most two when the user explicitly wants a full checklist.
- Use exactly four options.
- The fourth option is `직접 입력`.
- Ask about preference, constraint, or missing decision variable.
- Do not ask for sensitive numbers before the user understands the decision frame.

Recommended first reverse questions:

| Decision | Question | Options |
|---|---|---|
| home | 주거문제를 이야기하시는데 어떤 형태의 주거를 원하시나요? | 아파트, 주택, 오피스텔, 직접 입력 |
| home | 어떤 형태의 계약을 우선 고려하시나요? | 매매, 전세, 월세, 직접 입력 |
| retirement | 은퇴 후 현금흐름은 어떤 방식에 더 끌리시나요? | 배당/이자 수입, 연금 중심, 자산 일부 인출, 직접 입력 |
| marriage | 결혼 준비 기간은 어느 쪽에 가깝나요? | 1년 안, 2년 안, 3년 이상, 직접 입력 |

## Production Data Contract

Every API-backed response should include:

- `source`
- `as_of` or source period such as `dcls_month`, `cycle`, `first_date`, `last_date`
- `freshness_status`
- `assumptions`
- `decision_use`
- `not_recommendation_reason`

If any of these are missing, the LLM should phrase the result as a provisional assumption instead of a fact.
