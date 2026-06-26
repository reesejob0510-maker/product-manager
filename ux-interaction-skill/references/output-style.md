# Output Style

Output format rules for all UX Interaction Skill responses.

---

## Screen / Flow Analysis Format

Use this structure for all screen analysis, flow analysis, and design review outputs.

```
## UX 体验分析 — [Screen or feature name]

---

### Usable 可用性　⭐[X]/5

**做得好的地方**
- [Specific observation, 1-2 items]

**问题**
- [Specific user scenario: "a user who has never seen X will not understand Y when Z happens"]

**改进建议**
- 参考 [App name] 的 [Pattern name] 模式：[1-2 sentences on how to change it]

---

### Equitable 公平性　⭐[X]/5
（同上格式）

### Enjoyable 愉悦感　⭐[X]/5
（同上格式）

### Useful 有用性　⭐[X]/5
（同上格式）

---

### 综合评分

| 维度 | 评分 | 核心问题 |
|---|---|---|
| Usable  | X/5 | one sentence |
| Equitable | X/5 | one sentence |
| Enjoyable | X/5 | one sentence |
| Useful  | X/5 | one sentence |

---

### 最高优先级改进建议

**P0（合规 / 用户安全）**
1. [If any P0 issue exists]

**P1（转化 / 完成率）**
1. [Primary path friction]
2. ...

**P2（留存 / 愉悦感）**
1. [Delight and retention improvements]

---

### 总结 · Summary

**中文版**
> 一句话定性：[25 字以内概括整体体验水平]
>
> **优势**：[2-3 条，每条 ≤ 20 字]
> **问题**：[2-3 条，每条 ≤ 20 字]
> **最高优先级改进**：[1 条最关键的改进方向]

---

**English**
> One-liner: [One sentence overall assessment, ≤ 20 words]
>
> **Strengths**: [2-3 items, ≤ 15 words each]
> **Issues**: [2-3 items, ≤ 15 words each]
> **Top Priority Fix**: [The single most critical improvement, ≤ 20 words]
```

---

## Bilingual Summary Rules

The bilingual summary is mandatory for all screen analysis and design review outputs. It is also mandatory when the user explicitly requests UX analysis, interaction analysis, or provides screenshots for feedback.

**Chinese summary rules**:
- One-liner: ≤ 25 characters, states the overall verdict clearly
- Strengths: 2-3 items, each ≤ 20 characters
- Issues: 2-3 items, each ≤ 20 characters
- Top priority fix: 1 item, the single most important change

**English summary rules**:
- One-liner: ≤ 20 words
- Strengths: 2-3 items, ≤ 15 words each
- Issues: 2-3 items, ≤ 15 words each
- Top priority fix: ≤ 20 words

**Not a translation**: The Chinese and English summaries convey the same meaning but are written naturally in each language. Do not translate sentence by sentence. Write each one fresh for its audience.

**Audience**: The English summary is written for international team members, handoff documents, or cross-border design reviews. It must be independently readable without the Chinese version.

---

## Competitive Comparison Format

```
## 竞品对比：[App A] vs [App B] — [Feature name]

### 维度对比

| 维度 | [App A] | [App B] | 胜出 |
|---|---|---|---|
| Useful | X/5 | X/5 | A / B / 平 |
| Usable | X/5 | X/5 | A / B / 平 |
| Equitable | X/5 | X/5 | A / B / 平 |
| Enjoyable | X/5 | X/5 | A / B / 平 |

### [App A] 的优势
- [Pattern name] 模式：[Description]

### [App B] 的优势
- [Pattern name] 模式：[Description]

### 可互相借鉴的点
- [App A] 可以从 [App B] 学：[Specific pattern]
- [App B] 可以从 [App A] 学：[Specific pattern]
```

---

## Priority Labels

Use these labels consistently in all output:

- **P0**: Compliance or user safety issue. Must fix before launch. Examples: missing risk disclosure, dark pattern, accessibility blocker.
- **P1**: Primary path friction. Causes measurable drop-off. Examples: confusing primary action, error without recovery, onboarding dead end.
- **P2**: Retention and delight. Important but not blocking. Examples: missing completion feedback, cold copy, visual noise.

---

## Language rules

- Respond in the user's language (Chinese for Chinese users by default).
- Use "护城河" style plain Chinese, not literal translations of English UX terms.
- "眯眼测试" not "squint test" in Chinese responses.
- "这是 X 反模式" not "this exhibits the X anti-pattern."
- Use "参考 [App] 的 [模式名] 模式" for all fix citations.

---

## What to avoid

- Vague observations: "the design feels cluttered" → replace with "the squint test fails: 5 competing visual blocks of equal weight, no dominant primary content"
- Vague recommendations: "simplify the UI" → replace with "remove the widget hint bar and the system notice banner; these two elements have no primary-action value and fragment the user's visual focus"
- Citing patterns not in `references/pattern-library.md` without naming them explicitly
- Inventing app behaviors ("Instagram does X") without certainty
- Making quantitative impact claims without data ("this will increase conversion by 30%")
