---
name: path-explorer
description: Present structured financial decision paths for retirement, home ownership, or marriage fund planning without choosing for the user.
---

# Path Explorer

Use this skill after a decision type is known, or when the user asks what choices exist for a major financial decision.

## Goal

Show realistic option paths, tradeoffs, and when each path tends to fit. Do not pick one winner unless the user explicitly asks for prioritization.

## Supported Decisions

- `retirement`
- `home`
- `marriage`

## Output Shape

Use Korean and include:

1. A short restatement of the decision.
2. 3-4 paths.
3. For each path: core idea, strengths, risks, and required user data.
4. A prompt asking which path the user wants to simulate.

## Default Paths

Retirement:
- 배당 수입형
- 연금 수입형
- 자산 인출형
- 혼합형

Home:
- 청약 중심
- 투자 병행
- 즉시 매수
- 관망

Marriage:
- 예적금 중심
- 투자 병행
- 단기 집중

## Optional Local Helper

```bash
python src/scripts/fdn.py paths retirement
```
