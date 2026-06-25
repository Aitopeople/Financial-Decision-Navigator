import json
import subprocess
import sys
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "fdn.py"
FINLIFE_SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "finlife_client.py"
ECOS_SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "ecos_client.py"
MCP_SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "fdn_data_mcp.py"
FIXTURES = Path(__file__).resolve().parent / "fixtures"


def run_cli(*args):
    result = subprocess.run(
        [sys.executable, str(SCRIPT), *args],
        check=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    return json.loads(result.stdout)


def run_finlife(*args):
    result = subprocess.run(
        [sys.executable, str(FINLIFE_SCRIPT), *args],
        check=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    return json.loads(result.stdout)


def run_ecos(*args):
    result = subprocess.run(
        [sys.executable, str(ECOS_SCRIPT), *args],
        check=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    return json.loads(result.stdout)


def run_mcp(*args):
    result = subprocess.run(
        [sys.executable, str(MCP_SCRIPT), *args],
        check=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    return json.loads(result.stdout)


PRODUCTION_CONTRACT_KEYS = {
    "source",
    "source_url_or_provider",
    "as_of",
    "freshness_status",
    "assumptions",
    "decision_use",
    "not_recommendation_reason",
}


def assert_production_contract(testcase, data):
    testcase.assertTrue(PRODUCTION_CONTRACT_KEYS.issubset(data.keys()))
    testcase.assertIn(data["freshness_status"], {"fresh", "stale", "fixture", "user_assumption", "unavailable"})
    testcase.assertIsInstance(data["assumptions"], list)


class FinancialDecisionNavigatorTests(unittest.TestCase):
    def test_frame_retirement_question(self):
        data = run_cli("frame", "60세에 은퇴하고 싶어요")
        self.assertEqual(data["decision_type"], "retirement")
        self.assertGreaterEqual(data["confidence"], 0.8)
        self.assertNotIn("ETF", data["interpreted_concern"])

    def test_paths_supports_home(self):
        data = run_cli("paths", "home")
        self.assertEqual(data["decision_type"], "home")
        self.assertEqual([item["name"] for item in data["paths"]], ["청약 중심", "투자 병행", "즉시 매수", "관망"])

    def test_navigate_routes_home_to_triggering_pipeline(self):
        data = run_cli("navigate", "지금 집을 대출받아서 사야할까요 아니면 저축하면서 기다려야할까요")
        self.assertEqual(data["decision_type"], "home")
        self.assertTrue(data["supported_decision"])
        self.assertEqual(data["next_skill"], "path-explorer")
        self.assertIn("scenario-simulator", data["pipeline"])
        self.assertIn("behavior-insight", data["pipeline"])
        self.assertIn("집값", data["trigger_response"])
        self.assertIn("Finlife mortgage rates", data["data_sources"])
        self.assertEqual(data["clarifying_questions"][0]["options"], ["아파트", "주택", "오피스텔", "직접 입력"])

    def test_navigate_understands_residence_wording_as_home(self):
        data = run_cli("navigate", "주거 문제를 고민하고 있어요")
        self.assertEqual(data["decision_type"], "home")
        self.assertEqual(data["clarifying_questions"][1]["options"], ["매매", "전세", "월세", "직접 입력"])

    def test_navigate_routes_retirement_to_backtest_pipeline(self):
        data = run_cli("navigate", "60세에 은퇴하고 싶어요")
        self.assertEqual(data["decision_type"], "retirement")
        self.assertIn("historical-backtest", data["pipeline"])
        self.assertIn("목표 은퇴 나이", data["trigger_response"])
        self.assertIn("Alpha Vantage public-market proxies", data["data_sources"])

    def test_navigate_routes_marriage_to_savings_pipeline(self):
        data = run_cli("navigate", "결혼 자금을 어떻게 모아야 할까요")
        self.assertEqual(data["decision_type"], "marriage")
        self.assertIn("action-planner", data["pipeline"])
        self.assertIn("behavior-insight", data["pipeline"])
        self.assertIn("목표 결혼 예산", data["trigger_response"])

    def test_questions_returns_four_choice_reverse_questions(self):
        data = run_cli("questions", "home")
        self.assertEqual(data["question_style"], "four_choice_reverse_question")
        self.assertEqual(data["questions"][1]["id"], "contract_type")
        self.assertEqual(data["questions"][1]["options"], ["매매", "전세", "월세", "직접 입력"])

    def test_action_plan_reports_gap_and_required_monthly(self):
        data = run_cli(
            "action",
            "--goal",
            "retirement",
            "--target-amount",
            "700000000",
            "--current-asset",
            "100000000",
            "--monthly-budget",
            "500000",
            "--annual-return",
            "0.04",
            "--target-years",
            "20",
        )
        self.assertEqual(data["gap"], 600000000)
        self.assertGreater(data["required_monthly_amount"], data["monthly_budget"])
        self.assertEqual(data["budget_status"], "gap_exists_under_assumption")

    def test_behavior_insight_avoids_peer_comparison(self):
        data = run_cli(
            "behavior",
            "--goal",
            "marriage",
            "--category",
            "외식비=350000",
            "--category",
            "쇼핑비=500000",
            "--category",
            "구독비=70000",
        )
        self.assertEqual(data["most_adjustable_category"], "쇼핑비")
        self.assertNotIn("다른 사람", data["insight"])
        self.assertIn("조정 가능한 소비 영역", data["insight"])

    def test_finlife_mortgage_fixture_summarizes_monthly_payment(self):
        data = run_finlife(
            "--fixture",
            str(FIXTURES / "finlife_mortgage_sample.json"),
            "mortgage",
            "--principal",
            "140000000",
            "--years",
            "30",
            "--limit",
            "1",
        )
        self.assertEqual(data["service"], "mortgageLoanProductsSearch")
        self.assertEqual(data["products"][0]["bank"], "우리은행")
        self.assertGreater(data["products"][0]["monthly_payment_at_avg"], 0)
        self.assertIn("상품 추천이 아니라", data["decision_use"])

    def test_finlife_deposit_fixture_sorts_by_max_rate(self):
        data = run_finlife(
            "--fixture",
            str(FIXTURES / "finlife_deposit_sample.json"),
            "savings",
            "--type",
            "deposit",
            "--save-trm",
            "12",
            "--limit",
            "2",
        )
        self.assertEqual(data["service"], "depositProductsSearch")
        self.assertEqual(data["products"][0]["max_rate"], 3.5)
        self.assertIn("저축하며 기다리는", data["decision_use"])

    def test_ecos_key_stats_fixture_selects_macro_indicators(self):
        data = run_ecos("--fixture", str(FIXTURES / "ecos_key_stats_sample.json"), "key-stats")
        self.assertEqual(data["service"], "KeyStatisticList")
        self.assertEqual(data["indicator_count"], 4)
        self.assertGreaterEqual(len(data["selected_indicators"]), 4)
        self.assertIn("시나리오 변수", data["decision_use"])

    def test_ecos_search_fixture_summarizes_time_series(self):
        data = run_ecos(
            "--fixture",
            str(FIXTURES / "ecos_search_sample.json"),
            "search",
            "--stat-code",
            "200Y101",
            "--cycle",
            "A",
            "--from-time",
            "2020",
            "--to-time",
            "2023",
            "--item-code1",
            "10101",
        )
        self.assertEqual(data["service"], "StatisticSearch")
        self.assertEqual(data["count"], 4)
        self.assertEqual(data["values"][0]["time"], "2020")

    def test_mcp_mock_spending_summary_uses_local_sqlite(self):
        data = run_mcp(
            "call-tool",
            "get_mock_spending_summary",
            "--arguments",
            json.dumps({"user_id": "sample-user", "months": 3, "goal": "home"}, ensure_ascii=False),
        )
        assert_production_contract(self, data)
        self.assertEqual(data["source"], "local SQLite mock spending data")
        self.assertEqual(data["most_adjustable_category"], "쇼핑비")
        self.assertIn("타인 비교 없이", data["guardrail"])

    def test_mcp_finlife_wrapper_accepts_fixture(self):
        data = run_mcp(
            "call-tool",
            "get_finlife_mortgage_rate_range",
            "--arguments",
            json.dumps(
                {
                    "fixture": str(FIXTURES / "finlife_mortgage_sample.json"),
                    "principal": 140000000,
                    "years": 30,
                    "limit": 1,
                },
                ensure_ascii=False,
            ),
        )
        assert_production_contract(self, data)
        self.assertEqual(data["service"], "mortgageLoanProductsSearch")
        self.assertEqual(data["products"][0]["bank"], "우리은행")

    def test_mcp_finlife_savings_wrapper_accepts_fixture(self):
        data = run_mcp(
            "call-tool",
            "get_finlife_savings_rate_range",
            "--arguments",
            json.dumps(
                {
                    "fixture": str(FIXTURES / "finlife_deposit_sample.json"),
                    "product_type": "deposit",
                    "save_trm": "12",
                    "limit": 1,
                },
                ensure_ascii=False,
            ),
        )
        assert_production_contract(self, data)
        self.assertEqual(data["service"], "depositProductsSearch")
        self.assertEqual(data["products"][0]["max_rate"], 3.5)

    def test_mcp_finlife_rent_house_wrapper_accepts_fixture(self):
        data = run_mcp(
            "call-tool",
            "get_finlife_rent_house_loan_rate_range",
            "--arguments",
            json.dumps(
                {
                    "fixture": str(FIXTURES / "finlife_rent_house_sample.json"),
                    "principal": 100000000,
                    "years": 2,
                    "limit": 1,
                },
                ensure_ascii=False,
            ),
        )
        assert_production_contract(self, data)
        self.assertEqual(data["service"], "rentHouseLoanProductsSearch")
        self.assertEqual(data["products"][0]["bank"], "우리은행")
        self.assertIn("전세", data["decision_use"])
        self.assertEqual(data["products"][0]["payment_calculation"], "interest_only_until_maturity")
        self.assertLess(data["products"][0]["monthly_payment_at_avg"], 400000)

    def test_mcp_ecos_wrapper_accepts_fixture(self):
        data = run_mcp(
            "call-tool",
            "get_ecos_key_stats",
            "--arguments",
            json.dumps({"fixture": str(FIXTURES / "ecos_key_stats_sample.json")}, ensure_ascii=False),
        )
        assert_production_contract(self, data)
        self.assertEqual(data["service"], "KeyStatisticList")
        self.assertEqual(data["indicator_count"], 4)

    def test_mcp_ecos_statistic_search_accepts_fixture(self):
        data = run_mcp(
            "call-tool",
            "get_ecos_statistic_search",
            "--arguments",
            json.dumps(
                {
                    "fixture": str(FIXTURES / "ecos_search_sample.json"),
                    "stat_code": "200Y101",
                    "cycle": "A",
                    "from_time": "2020",
                    "to_time": "2023",
                    "item_code1": "10101",
                },
                ensure_ascii=False,
            ),
        )
        assert_production_contract(self, data)
        self.assertEqual(data["service"], "StatisticSearch")
        self.assertEqual(data["values"][-1]["time"], "2023")

    def test_mcp_alphavantage_monthly_series_accepts_fixture(self):
        data = run_mcp(
            "call-tool",
            "get_alphavantage_monthly_series",
            "--arguments",
            json.dumps(
                {
                    "fixture": str(FIXTURES / "alphavantage_monthly_sample.json"),
                    "symbol": "SPY",
                    "max_points": 4,
                },
                ensure_ascii=False,
            ),
        )
        assert_production_contract(self, data)
        self.assertEqual(data["source"], "Alpha Vantage TIME_SERIES_MONTHLY_ADJUSTED")
        self.assertEqual(data["first_date"], "2024-01-31")
        self.assertEqual(data["last_date"], "2024-04-30")
        self.assertLess(data["max_drawdown_pct"], 0)


if __name__ == "__main__":
    unittest.main()
