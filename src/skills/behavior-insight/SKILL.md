---
name: behavior-insight
description: Analyze spending categories as adjustable behaviors for a user goal without comparing the user to other people.
---

# Behavior Insight

Use this skill when the user provides spending categories or asks how consumption data could support a financial goal.

## Goal

Identify behavior-level adjustment opportunities that can support the user's chosen goal.

## Output Shape

Use Korean and include:

1. Current goal.
2. Spending categories reviewed.
3. Most adjustable category based on amount and optional flexibility signal.
4. One practical action for the next month.

## Important Language Rule

Do not compare the user to other people.

Bad:

```text
다른 사람보다 외식비가 높습니다.
```

Good:

```text
현재 목표 달성을 위해 조정 가능한 소비 영역은 외식비입니다.
```

## Optional Local Helper

```bash
python src/scripts/fdn.py behavior --goal marriage --category "외식비=350000" --category "쇼핑비=500000" --category "구독비=70000"
```
