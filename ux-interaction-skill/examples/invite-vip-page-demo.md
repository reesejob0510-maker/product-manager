# Example: Invite & VIP Page Analysis

> Demo output shape for an invite / referral / VIP upgrade page analysis.
> Trigger: "分析一下这张邀请好友页面的截图"

---

## User prompt

```
分析一下这张截图的交互设计。
用 UX 四维度框架（Useful / Usable / Equitable / Enjoyable）逐维打分（1-5），
指出每个维度的具体问题和用户场景，参考头部 App 的做法给出改进建议。
```

---

## Skill output

### Useful 有用　⭐⭐⭐ 3/5

**做得好的地方**
- 把「邀请好友」和「VIP 升级进度」放在同一页，让用户看到邀请行为的直接收益
- 显示了邀请人数（已邀请 X/N 人）作为目标锚定

**问题**
- 倒计时「还剩 XX:XX:XX」没有标注「距离什么截止」，用户不知道是「活动截止」还是「奖励领取截止」
- 规则说明层级混乱：核心规则（邀请 N 人得到什么）和细则（如何算有效邀请）在同一层展示，用户难以快速提取关键信息
- 看不到已邀请的具体好友状态（谁注册了？谁完成了条件？谁还差什么？）

**改进建议**
- 为倒计时加标签：「活动截止倒计时」或「本期奖励领取剩余时间」
- 参考 Acorns 的 Layered Rules（渐进式规则）模式：核心规则一句话展示（「邀请 3 人成功注册，得 50 USDT」），细则折叠到「查看详情」
- 参考 Robinhood Invite Tracker 的 Sunk Cost Surfacing 模式：为每个被邀请人显示进度（「李雷 — 已注册，待完成首笔交易」）

---

### Usable 可用　⭐⭐⭐ 3/5

**做得好的地方**
- 「复制链接」和「分享」按钮位置明确，操作路径短

**问题**
- 对于进度接近达标的用户（已邀请 2/3 人），没有「发送提醒」或「催促完成」的功能入口
- 已过期的邀请记录和有效记录混在一起，没有视觉区分
- VIP 升级进度条（如「距离 VIP3 还差 XX 交易量」）与邀请进度条在视觉层级上相近，用户难以分清两件事的关系

**改进建议**
- 在已邀请列表中为「已注册但未完成条件」的好友提供「发送提醒」按钮（可预览消息内容再发送）
- 为已过期的邀请记录加「已过期」标签，或移至折叠区
- 在页面层级上用分隔线或卡片区分「邀请进度」和「VIP 升级进度」两条独立的任务线

---

### Equitable 公平　⭐⭐⭐⭐ 4/5

**做得好的地方**
- 邀请规则对所有用户一视同仁，没有隐藏条件
- 奖励金额展示清晰，没有「最高可得 X」这类误导性表达

**问题**
- 对于已经完成邀请目标的用户，没有清晰的「你已完成，奖励何时到账」状态反馈（Silent Success 反模式）
- 规则没有说明「有效邀请」的完整定义，存在用户邀请后发现不满足条件导致的争议风险

**改进建议**
- 在完成邀请目标后立即展示「🎉 你已完成本期邀请目标！奖励将在 T+1 工作日内到账」
- 在规则展示区明确定义「有效邀请」：「好友通过你的链接注册并完成 1 笔 100 USDT 以上的交易」

---

### Enjoyable 愉悦　⭐⭐ 2/5

**做得好的地方**
- 整体色调统一，视觉整洁

**问题**
- 邀请成功后没有「成功时刻」设计（Magic Moment 缺失）——好友注册时用户没有实时通知和庆祝反馈
- 进度条是静态的，没有动效，让「快达标了」的成就感无从感受
- 页面整体偏「表单化」，没有传递出「帮你的朋友一起升级，你们都受益」的情感价值

**改进建议**
- 参考 Robinhood 的 Magic Moments：好友成功注册时推送「🎉 [好友昵称] 刚刚加入！你距离获得奖励还差 1 人」
- 进度条接近满格时加入填充动画（一个简单的 CSS transition 即可）
- 文案语气从「你已邀请 X 人」改为「X 位朋友已通过你加入了 BingX」，强调人际连接价值

---

### 多路径覆盖检查

| 路径类型 | 覆盖情况 |
|---|---|
| 首次打开邀请页（0 人已邀请） | ✅ 有引导 |
| 邀请进行中（部分完成） | ⚠️ 缺少进度驱动机制 |
| 邀请已全部完成，等待奖励 | ❌ 缺少「已完成」状态页 |
| 好友注册但未完成条件 | ❌ 缺少催促完成功能 |
| 活动已截止 | ❓ 未见截止后的状态处理 |
| 弱网/分享失败 | ❓ 未测试 |

---

### 总结 · Summary

**中文版**
> 核心功能完整，但进度感知和里程碑反馈是主要缺口，让「邀请行为」变成了无情感的表格填写。

**核心优势**：操作路径短；规则展示清晰；奖励金额透明

**核心问题**：
1. 倒计时标签缺失，用户不知道在倒什么
2. 好友进度不可见，无法催促完成
3. 成功时刻缺失（完成后无反馈）

**最高优先级改进**：为每个已邀请好友添加完成状态和「发送提醒」功能，把静态进度变成可操作的任务列表。

---

**English**
> Core functionality is complete, but progress visibility and milestone feedback are the main gaps — the invite flow feels like filling out a form, not an engaging referral experience.

**Core strengths**: Short action paths; clear rule display; transparent reward amounts

**Core issues**:
1. Countdown label missing — users don't know what it's counting toward
2. Friend progress invisible — no way to nudge incomplete invites
3. No success moment — completing the goal produces no feedback

**Top Priority Fix**: Add friend-level completion status and a "Send Reminder" CTA to turn static progress into an actionable task list.
