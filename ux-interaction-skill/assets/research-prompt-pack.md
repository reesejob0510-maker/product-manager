# Research Prompt Pack

Copyable prompts for common UX analysis tasks. Paste directly into your agent.

---

## Screen Analysis

```
分析一下这张截图的交互设计。
用 UX 四维度框架（Useful / Usable / Equitable / Enjoyable）逐维打分（1-5），
指出每个维度的具体问题和用户场景，
参考头部 App 的做法给出改进建议，
最后给出中英双语总结。
```

```
Analyze the UX of this screenshot.
Score each of the four dimensions (Useful / Usable / Equitable / Enjoyable) from 1-5.
Describe specific user scenarios for each problem found.
Recommend fixes citing named apps and specific patterns.
End with a bilingual summary (Chinese + English).
```

---

## Flow Analysis

```
分析一下 [产品名] 的 [功能名] 流程，
找出用户在哪些步骤可能会卡住或放弃，
用 UX 四维度评估整个流程，
重点检查：新手引导是否清晰？错误状态是否有恢复路径？完成节点是否有情感反馈？
```

---

## Competitive Comparison

```
对比 [App A] 和 [App B] 的 [功能名] 设计，
按 Useful / Usable / Equitable / Enjoyable 四个维度分别比较，
找出各自的优势和可以互相借鉴的设计模式。
```

---

## Design Review

```
帮我 review 这个 [功能名] 设计方案，做以下检查：
1. UX 四维度走查：每个维度打分 + 具体问题 + 改进建议
2. 多路径覆盖检查：入口路径 / 用户状态 / 数据状态 / 交互流程 / 环境降级
3. 输出优先级排序的问题清单（P0 / P1 / P2）
4. 中英双语总结
```

---

## Prototype Design

```
帮我设计 [功能名] 的交互流程。
要求：
- 先检查多路径覆盖（5类路径）
- 应用相关的设计模式（pattern-library 里的命名模式）
- 避免常见反模式
- 输出每个状态的设计说明（不只是 happy path）
```

---

## Anti-Pattern Audit

```
帮我检查这张截图里有没有以下反模式：
1. 一侧性风险披露（只展示收益不展示亏损）
2. 空状态高风险推销
3. 引导结束无 CTA 死路
4. 教育弹窗（popup 解释概念）
5. 首屏信息过载（超过 4 个竞争视觉区块）
6. 错误无恢复路径
找到的话，说明它是哪个反模式、影响级别（P0/P1/P2）、以及修复方向。
```

---

## Learning Mode

```
我想学习 UX 四维度框架，每次只问我一个问题，
从「用户目标」开始，逐步带我走到「设计决策」。
```

```
帮我用 UX Interaction Skill 分析一下我自己设计的界面，
我来描述界面内容，你帮我找问题并推荐改进方向。
```

---

## New User Onboarding Specific

```
分析一下 [App名] 的新手引导设计，重点检查：
1. 有没有「先体验后承诺」的路径？
2. 新概念是否用了 Inline 教育卡片而非弹窗？
3. 引导结束后有没有明确的下一步 CTA？
4. 风险信息是否和收益信息对等展示？
参考头部 App 的做法给出优先改进建议。
```

---

## Financial Product Specific

```
从金融产品 UX 合规角度分析这张截图：
1. 是否存在「一侧性风险披露」暗模式？
2. 空状态有没有高风险产品推销？
3. 高波动资产（新币、杠杆产品）有没有风险提示？
4. 引导流程有没有「理解后才能操作」的机制？
标出 P0 级合规问题，推荐修复方向。
```
