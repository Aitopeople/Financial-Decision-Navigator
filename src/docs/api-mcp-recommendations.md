# API and MCP Integration

FDN은 사용자 동의 기반 금융/소비 데이터와 공개 금융 API를 조합해 의사결정 시나리오를 구성합니다. 현재 구현은 무료 또는 free tier가 있는 API와 로컬 MCP를 우선 사용합니다.

## Recommended Stack

### 1. Financial Supervisory Service Finlife API

- Provider: 금융감독원 금융상품통합비교공시
- Use for: 예금, 적금, 주택담보대출, 전세자금대출 상품 조건
- FDN use: 대출 상환액 계산의 금리 후보, 저축 대기 전략의 예금/적금 금리 가정
- Notes: 상품 추천이 아니라 의사결정 변수로만 사용합니다.

### 2. Bank of Korea ECOS API

- Provider: 한국은행
- Use for: 기준금리, 시장금리, 물가, 환율, 거시 통계
- FDN use: `scenario-simulator`에서 금리 상승/하락, 인플레이션, 경기 흐름의 외부 변수
- Notes: 금리/물가 시나리오에 가장 설득력이 좋습니다.

### 3. Alpha Vantage API and MCP

- Provider: Alpha Vantage
- Use for: US equities, ETFs, FX, technical indicators
- FDN use: `historical-backtest`에서 S&P 500, 배당 ETF, 채권 ETF 프록시
- Free tier: official support page states most datasets are free up to 25 requests/day.
- MCP: Alpha Vantage has an official MCP server for AI agents.
- Notes: 무료 한도가 낮으므로 데모에서는 daily/monthly endpoint와 cache를 사용합니다.

### 4. Local SQLite MCP

- Provider: project-local MCP server
- Use for: anonymized sample spending data
- FDN use: `behavior-insight`에서 외식비, 쇼핑비, 구독비, 교통비 등 카테고리 분석
- Implementation: `src/scripts/fdn_data_mcp.py`, `src/data/mock_spending.csv`
- Notes: 실제 개인 금융 데이터 대신 익명 샘플 CSV/SQLite를 사용합니다.

### 5. Fetch MCP

- Provider: project-local MCP server
- Use for: REST API 호출 결과를 Codex/agent가 읽을 수 있게 변환
- FDN use: Finlife, ECOS, Alpha Vantage 같은 HTTP API 연결
- Implementation: `fetch_json`, `get_finlife_mortgage_rate_range`, `get_ecos_key_stats`
- Notes: API 키는 `.env`에서만 읽고, fetch URL 출력에서는 `auth`, `apikey`, `key` 값을 마스킹합니다. 기본은 HTTPS만 허용하되, Finlife 공식 문서의 HTTP endpoint는 해당 host에 한해 허용합니다.

## Deferred APIs

공공데이터포털 API는 현재 범위에서 제외합니다. 부동산 실거래가, 지역 코드, 주택 데이터는 어떤 데이터가 실제 결정 품질을 높이는지 더 좁힌 뒤 등록하는 편이 낫습니다. 각 API를 별도로 신청해야 하므로 초기 운영 단계에서는 시간 대비 효율이 낮습니다.

FRED API도 현재 범위에서 제외합니다. 공공데이터포털을 제외하면 주택 의사결정에서 가장 중요한 실거래가, 지역 가격, 매물/전세 흐름 같은 메인 변수가 비어 있습니다. 이 상태에서 미국 거시지표를 보조 변수로 붙이는 것은 사용자의 주택 의사결정 품질을 충분히 높이지 못합니다.

Home ownership 플로우에서는 현재 Finlife의 대출 금리와 ECOS의 금리/물가/경기 지표, 사용자가 직접 입력한 집값/대출액/소득/지출을 우선 사용합니다. 실거래가 데이터는 추후 확정된 내부 데이터 소스 또는 외부 API로 교체할 수 있는 `get_home_market_snapshot` 인터페이스만 남겨둡니다.

## Suggested Flow by Skill

| Skill | Data source |
|---|---|
| decision-framing | local deterministic classifier |
| path-explorer | local rules |
| historical-backtest | ECOS, Alpha Vantage, cached ETF data |
| scenario-simulator | BOK ECOS, Finlife, user-provided home variables |
| action-planner | local calculator plus Finlife rates |
| behavior-insight | local SQLite MCP mock spending data |

## MCP Shape for FDN

For production use, keep one thin project MCP server named `fdn-data` instead of exposing every external API directly.

Tools:

- `get_home_market_snapshot(region, ym)`; deferred until source is fixed
- `get_mortgage_rate_range(loan_type)`
- `get_macro_scenario_inputs(country)`
- `get_asset_proxy_returns(symbols, years)`
- `get_mock_spending_summary(user_id, months)`

Current MCP implementation:

- `get_mock_spending_summary(user_id, months, goal)`
- `list_mock_spending_transactions(user_id, limit)`
- `fetch_json(url, max_bytes)`
- `get_finlife_mortgage_rate_range(principal, years, fixture, limit)`
- `get_ecos_key_stats(fixture)`

This keeps the plugin workflow stable. Later, the implementation behind those tools can move from public/free APIs to private production data sources without changing the user-facing skills.
