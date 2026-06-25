# Financial Decision Navigator Plugin

이 디렉터리는 Codex 플러그인 루트입니다. 설치, 실행, 파이프라인 설명은 상위 [README.md](../README.md)를 기준으로 보세요.

## 구성

```text
src/
├── .codex-plugin/plugin.json
├── .mcp.json
├── data/mock_spending.csv
├── skills/*/SKILL.md
├── scripts/
│   ├── fdn.py
│   ├── finlife_client.py
│   ├── ecos_client.py
│   └── fdn_data_mcp.py
├── docs/
└── tests/test_fdn.py
```

## 핵심 명령

```bash
python src/scripts/fdn.py navigate "지금 집을 대출받아서 사야할까요 아니면 저축하면서 기다려야할까요"
python src/scripts/fdn_data_mcp.py call-tool get_mock_spending_summary
python -m unittest discover -s src/tests
```

## API 키

루트 `.env`에 저장합니다. `.env`는 git 추적에서 제외됩니다.

```env
FINLIFE_API_KEY=
ECOS_API_KEY=
ALPHAVANTAGE_API_KEY=
```

## 참고 문서

- [API/MCP recommendations](docs/api-mcp-recommendations.md)
- [Production readiness review](docs/production-readiness.md)
- [Production implementation stack](docs/production-stack.md)
- [Alpha Vantage notes](docs/alphavantage.md)
- [ECOS spec notes](docs/ecos.md)
- [Finlife spec notes](docs/finlife.md)
- [Flywheel](docs/flywheel.md)
