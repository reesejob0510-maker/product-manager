# Example: Prediction Market Onboarding Analysis

> Demo output shape for a trading guidance / onboarding flow analysis.
> Trigger: "分析一下预测市场的交易引导"

---

## User prompt

```
分析一下这个预测市场的交易引导页面交互设计。
用 UX 四维度框架（Useful / Usable / Equitable / Enjoyable）逐维打分（1-5），
指出每个维度的具体问题和用户场景，参考头部 App 的做法给出改进建议。
```

---

## Skill output

### Useful 有用　⭐⭐⭐⭐ 4/5

**做得好的地方**
- 在用户首次接触合约前显示规则说明，提供了基础的知识铺垫
- 把「预测市场」定义和「如何参与」放在同一屏，信息层次合理

**问题**
- 没有显示真实的盈亏场景数字（「你买入 10 USDT，如果预测正确能得到多少？如果错误会怎样？」）
- 缺少「我为什么要做这件事」的价值锚定——对于新用户，参与预测市场的动机不明确

**改进建议**
- 参考 Robinhood Learn 的 Dollar-First Input 模式：用「投入 $10，如果预测正确赔率为 1.8x，可得 $18」替代纯文字说明
- 参考 Wealthsimple 的 Goal Contextualization：在引导首屏展示「历史上有 X% 的用户在类似预测中盈利」

---

### Usable 可用　⭐⭐⭐ 3/5

**做得好的地方**
- 引导步骤有明确的步骤指示（1/3 → 2/3 → 3/3）

**问题**
- 步骤 2 的规则说明文字密度高，平均每条超过 60 字，移动端用户不会读完
- 引导结束没有明确的下一步 CTA（用户不知道「读完引导后我该做什么」）
- 没有「跳过」选项，强制阅读降低了有经验用户的效率

**改进建议**
- 参考 Robinhood 的 Inline Education Card 模式：每条规则控制在 25 字以内 + 一个数字示例，复杂内容折叠到「了解更多」
- 参考 Trade Republic 的 Experience Before Commitment：引导最后一步用「现在试试→」直接接入一个低风险的模拟预测
- 加入「跳过」或「我已了解，直接开始」选项

---

### Equitable 公平　⭐⭐ 2/5

**做得好的地方**
- 引导内容使用白话文，没有大量专业术语堆砌

**问题**
- **P0**：整个引导只展示了「可能获利」的情景，没有提及亏损的可能性和范围——这是严重的单边风险披露（One-Sided Risk Disclosure 反模式）
- 色彩系统高度依赖绿色/红色作为盈亏指示，对红绿色盲用户不友好
- 没有「新手」/「有经验」的用户分流，所有用户走同一套引导

**改进建议**
- **优先级 P0**：在引导流程中明确加入亏损场景说明（如「预测错误将损失你投入的全部金额」），这既是合规要求也是设计诚信
- 用图案 + 颜色组合表示盈亏，不单独依赖颜色
- 在引导首屏增加「我是新手 / 我有经验」分流，有经验用户可快速进入

---

### Enjoyable 愉悦　⭐⭐⭐ 3/5

**做得好的地方**
- 插图风格统一，界面整洁，没有信息堆砌感

**问题**
- 完成引导后没有「成功时刻」（Magic Moment）设计——用户读完引导，感受不到「我已经准备好了」的仪式感
- 文案过于工具性，缺乏人情味（「您已完成阅读」vs「你现在已经了解规则，可以开始你的第一个预测了」）

**改进建议**
- 参考 Monzo 的 Magic Moments 模式：引导最后一屏用「✨ 你已经准备好了！开始你的第一个预测」加入轻量庆祝动效（confetti 或进度填满动画）
- 优化文案：把系统通知式语言替换为对话式语言

---

### 多路径覆盖检查

| 路径类型 | 覆盖情况 |
|---|---|
| 新用户（首次看引导） | ✅ 覆盖 |
| 有经验用户（强制看引导） | ❌ 缺少跳过机制 |
| 用户中途退出引导 | ❌ 没有保存进度，下次重新开始 |
| 用户完成引导但余额为 0 | ❌ 引导后无充值引导 CTA |
| 弱网/加载失败 | ❓ 未测试 |

---

### 总结 · Summary

**中文版**
> 引导框架设计合理，步骤划分清晰，但单边风险披露是 P0 合规问题，必须优先修复。文案密度和引导后无 CTA 是主要体验缺口。

**核心优势**：多步骤渐进式披露；插图风格统一；去术语化表达

**核心问题**：
1. **P0** — 没有亏损场景说明（合规+公平问题）
2. 引导结束无 CTA（用户迷失）
3. 规则文字过长（可用性问题）

**最高优先级改进**：立即在引导流程中加入亏损说明，这是合规底线。

---

**English**
> Onboarding structure is solid with clear step progression, but missing loss disclosure is a P0 compliance issue that must be fixed first. Copy density and lack of a post-onboarding CTA are the main experience gaps.

**Core strengths**: Multi-step progressive disclosure; consistent illustration style; plain language framing

**Core issues**:
1. **P0** — No loss scenario disclosure (compliance + equity issue)
2. No CTA after onboarding completion (user dead-end)
3. Rule copy too dense for mobile reading

**Top Priority Fix**: Add explicit loss disclosure to the onboarding flow — this is a compliance baseline, not optional.
