---
name: decision-framing
description: Classify vague Korean or English personal finance questions into a decision type before any product discussion.
---

# Decision Framing

Use this skill when the user asks a broad financial-life question such as retirement timing, buying a home, preparing marriage funds, education funds, wealth growth, or unclear money anxiety.

## Goal

Turn the user's wording into a structured decision frame. Do not recommend products in this step.

## Output

Return a concise Korean response with:

1. Interpreted concern.
2. `decision_type`: one of `retirement`, `home`, `marriage`, `education`, `wealth_growth`, `uncertain`.
3. Confidence from 0 to 1.
4. The next best question to reduce ambiguity.

## Classification Hints

- `retirement`: 은퇴, 노후, 연금, 배당 생활, 생활비, FIRE.
- `home`: 내 집, 주택, 아파트, 청약, 전세, 매수, 대출.
- `marriage`: 결혼, 신혼, 예식, 혼수, 전세자금.
- `education`: 자녀 교육, 학자금, 유학.
- `wealth_growth`: 목돈, 투자, 자산 증식, 돈 불리기.
- `uncertain`: insufficient context or mixed goals.

## Guardrails

- Avoid judging the user's financial status.
- Avoid comparative claims such as "평균보다 부족합니다".
- Avoid product-first phrasing such as "ETF를 사세요".
- Say this is decision support, not personalized investment advice.

## Optional Local Helper

If working in the plugin repository, you can run:

```bash
python src/scripts/fdn.py frame "60세에 은퇴하고 싶어요"
```

For the main plugin routing behavior, prefer:

```bash
python src/scripts/fdn.py navigate "지금 집을 대출받아서 사야할까요 아니면 저축하면서 기다려야할까요"
```

`navigate` returns the selected decision type, skill pipeline, required inputs, data sources, and a trigger response that guides the user into the next skill.
