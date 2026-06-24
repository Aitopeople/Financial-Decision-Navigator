# Financial Decision Navigator Flywheel

FDN의 성장은 상품 추천 전환율만으로 측정하지 않습니다. 사용자가 더 나은 의사결정 흐름을 끝까지 완성했는지를 중심으로 개선합니다.

## Loop

```text
사용자 질문
-> decision-framing 분류
-> 선택지 탐색
-> 시나리오/백테스트 요청
-> 실행 계획 생성
-> 사용자가 선택한 다음 행동 기록
-> 자주 막히는 지점과 필요한 데이터 개선
```

## Signals

- `decision_type`: retirement, home, marriage, education, wealth_growth, uncertain
- `confidence`: 질문 분류 확신도
- `selected_path`: 사용자가 더 보고 싶다고 고른 경로
- `missing_inputs`: 실행 계획에 부족했던 숫자
- `completed_steps`: framing, paths, backtest, scenario, action
- `dropoff_step`: 사용자가 멈춘 단계
- `behavior_adjustment_category`: 조정 가능한 소비 카테고리

## Improvement Rules

- `uncertain` 비중이 높으면 decision-framing 예시와 질문을 개선합니다.
- `missing_inputs`가 반복되면 필요한 숫자를 더 작게 묶어 질문합니다.
- 특정 path에서 dropoff가 높으면 설명을 줄이고 예시를 보강합니다.
- behavior insight는 타인 비교를 추가하지 않습니다.
- 전환 목표는 상품 구매가 아니라 목표 생성, 계획 저장, 다음 행동 실행으로 둡니다.

## Why This Matches Popular Developer Tool Needs

최근 AI 코딩 도구와 플러그인 생태계의 공통 니즈는 재사용 가능한 워크플로, 명시적인 산출물, 검증 가능한 실행 경로입니다. FDN은 각 기능을 독립 스킬로 쪼개 Codex가 필요한 시점에만 로드하게 하고, CLI helper와 테스트로 결과를 재현 가능하게 만들었습니다.
