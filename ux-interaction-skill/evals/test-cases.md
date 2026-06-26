# Test Cases

Trigger and behavior tests for UX Interaction Skill. Use to verify the skill activates correctly and produces expected output structure.

---

## Trigger Tests

### Should activate

| Input | Expected behavior |
|---|---|
| 「分析一下这张截图」| Activates screen analysis mode, runs four-dimension scoring |
| 「这个交互设计有什么问题」| Activates screen analysis mode |
| 「帮我 review 这个设计」| Activates design review mode, includes multi-path checklist |
| 「帮我设计新手引导流程」| Activates prototype design mode, reads multi-path checklist first |
| 「对比一下 A 和 B 的设计」| Activates competitive comparison mode |
| 「UX critique of this screen」| Activates screen analysis mode (English) |
| 「交互引导怎么做」| Activates research partner conversation mode |
| 「我想学 UX 四维度」| Activates learning mode, asks one question per turn |

### Should not activate

| Input | Expected behavior |
|---|---|
| 「帮我写代码」| Not activated — pass to default code assistance |
| 「分析一下这家公司的财务」| Not activated — may activate Buffett.skill instead |
| 「发一封邮件」| Not activated |

---

## Behavior Tests

### Test 01: Four-dimension scoring completeness

**Input**: Screenshot of any mobile app screen

**Expected output must include**:
- [ ] Score for Useful (1-5)
- [ ] Score for Usable (1-5)
- [ ] Score for Equitable (1-5)
- [ ] Score for Enjoyable (1-5)
- [ ] At least one specific user scenario per dimension with a problem
- [ ] At least one named app + named pattern per recommendation
- [ ] Bilingual summary (Chinese + English)

**Fail if**:
- Any dimension is missing
- Recommendations do not cite a named app
- Bilingual summary is absent

---

### Test 02: Anti-pattern naming

**Input**: Screenshot with a visible popup/modal explaining a concept

**Expected output must include**:
- [ ] Named anti-pattern: "教育弹窗（Education Popup）反模式"
- [ ] Impact level stated (P0 / P1 / P2)
- [ ] Fix cites Pattern 02 (Inline Education Card) or equivalent named pattern

**Fail if**:
- Anti-pattern is described but not named
- Fix recommendation is vague ("make it less intrusive")

---

### Test 03: Dark pattern flagging

**Input**: Screenshot of a financial app with an empty state showing AI-recommended leveraged contracts

**Expected output must include**:
- [ ] P0 flag on the dark pattern
- [ ] Named anti-pattern: "空状态高风险推销（Empty-State High-Risk Upsell）反模式"
- [ ] Reference to Pattern 12 (Neutral Empty State) for fix direction
- [ ] Note that this may have regulatory implications

**Fail if**:
- Issue is rated P2 or lower
- No compliance note

---

### Test 04: Bilingual summary format

**Expected format**:

```
### 总结 · Summary

**中文版**
> 一句话定性：[≤ 25 字]
>
> **优势**：[item 1, ≤ 20 字]; [item 2]; [item 3]
> **问题**：[item 1, ≤ 20 字]; [item 2]; [item 3]
> **最高优先级改进**：[1 条]

---

**English**
> One-liner: [≤ 20 words]
>
> **Strengths**: [item 1, ≤ 15 words]; [item 2]; [item 3]
> **Issues**: [item 1, ≤ 15 words]; [item 2]; [item 3]
> **Top Priority Fix**: [≤ 20 words]
```

**Fail if**:
- Chinese and English are direct translations of each other word-for-word
- Summary repeats full analysis rather than distilling it
- One-liner exceeds stated character/word limits

---

### Test 05: Multi-path checklist in design tasks

**Input**: "帮我设计一个充值流程的交互方案"

**Expected output must include**:
- [ ] Multi-path coverage table with all 5 categories
- [ ] Coverage status (covered / partial / missing) per category
- [ ] Design includes at least: loading state, empty/first-use state, error state, happy path
- [ ] Not just the happy path

**Fail if**:
- Multi-path checklist is not run
- Design only covers the happy path

---

### Test 06: Squint test description

**Input**: Screenshot with high information density (5+ competing content blocks)

**Expected output must include**:
- [ ] Explicit squint test result: "fail" with explanation
- [ ] Count of competing visual blocks visible above fold
- [ ] Reference to at least one app with better first-screen hierarchy (Wealthsimple, Cash App, or Trade Republic)

**Fail if**:
- Squint test not mentioned
- Information density problem described but not quantified
