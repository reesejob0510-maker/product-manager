<div align="center">

# UX Interaction Skill

### 让 AI 成为你的 UX 分析师和交互设计师

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Agent Skill](https://img.shields.io/badge/Agent%20Skill-SKILL.md-black)](SKILL.md)
[![中文优先](https://img.shields.io/badge/README-%E4%B8%AD%E6%96%87%E4%BC%98%E5%85%88-red)](README.md)
[![English](https://img.shields.io/badge/English-README.en.md-lightgrey)](README.en.md)

</div>

看到一个界面，你能感受到「这个用着别扭」，却很难说清楚：哪个维度出了问题？应该参考哪个 App 怎么改？这个设计稿覆盖了所有边界状态吗？

UX Interaction Skill 把 Google UX 四维度框架（Useful / Usable / Equitable / Enjoyable）、12 个来自头部 App 的可复用设计模式、10 个高频反模式，做成 Agent Skill。给它一张截图，它会从四个维度打分，指出具体用户场景下的问题，推荐有名字有出处的修复方向，最后给出中英双语总结。

> UX 分析和设计辅助工具。UX Interaction Skill 负责评估、模式推荐和设计指导；最终产品决策由你的团队决定。

## 为什么是 Google UX 四维度

四个维度覆盖了一个产品功能的完整体验质量：

- **Useful 有用**：这个功能真正解决了用户的实际问题吗？
- **Usable 可用**：用户能顺利完成任务吗？路径是否清晰？
- **Equitable 公平**：不同背景、能力的用户都能用吗？有无暗模式？
- **Enjoyable 愉悦**：关键时刻有情感反馈吗？文案有人情味吗？

UX Interaction Skill 在这四个维度上叠加了来自 Robinhood、Monzo、Trade Republic、Coinbase、Wealthsimple、Acorns、Cash App、Betterment、且慢等头部 App 的具体模式库，把抽象原则变成可执行的改进方向。

## 它能帮你做什么

| 你现在遇到的问题 | 可以这样问 AI | Skill 会帮你看什么 |
|---|---|---|
| 看到一个界面，感觉用着别扭 | `分析一下这张截图的交互设计` | 四维度打分 + 具体问题 + 参考 App 修复建议 |
| 竞品做了某个功能，想拆解它好在哪里 | `帮我分析 [App 名] 的 [功能] 设计` | 提炼设计决策和可复用模式 |
| 两个 App 同类功能，想知道哪个更好 | `对比 A 和 B 的 [功能] 交互` | 按维度对比，找差距和各自优势 |
| 设计稿出来了，想做走查 | `帮我 review 这个设计方案` | 四维度走查 + 多路径覆盖检查 |
| 要从头设计一个功能 | `帮我设计 [功能] 的交互流程` | 应用模式库 + 多路径清单，输出覆盖所有状态的方案 |
| 想挑战某个设计有没有暗模式 | `检查这张截图里有没有暗模式` | 逐一对照反模式清单，P0 优先标记 |

## 直接复制这个 Prompt

```text
分析一下这张截图的交互设计。
用 UX 四维度框架（Useful / Usable / Equitable / Enjoyable）逐维打分（1-5），
指出每个维度的具体问题和用户场景，
参考头部 App 的做法给出改进建议，
最后给出中英双语总结。
```

```text
帮我 review [功能] 的设计方案，
检查多路径覆盖情况（入口路径/用户状态/数据状态/交互流程/降级），
用 UX 四维度找出体验缺口，输出优先级排序的问题清单。
```

```text
对比 [App A] 和 [App B] 的 [功能] 设计，
按 Useful / Usable / Equitable / Enjoyable 四个维度分别比较，
找出各自的优势和可以互相借鉴的地方。
```

更多可复制模板见 [assets/research-prompt-pack.md](assets/research-prompt-pack.md)。

## 输出长什么样

```
### Usable 可用性　⭐⭐⭐ 3/5

**做得好的地方**
- 分步引导有明确进度指示（2/3 → 3/3）

**问题**
- Tooltip 文案超过 50 字，移动端用户不会读完

**改进建议**
- 参考 Robinhood 的 Inline 教育卡片模式：控制在 25 字以内 + 一个数字示例

---

### 总结 · Summary

**中文版**
> 引导方向正确，但文案密度和风险信息缺失是核心短板。

**优势**：上下文锚定精准；分步渐进披露；去术语化表达
**问题**：未解释亏损后果；引导结束无 CTA；文案过长
**最高优先级改进**：补充亏损提示，这是合规底线

---

**English**
> Onboarding direction is right, but copy density and missing loss disclosure are critical gaps.

**Strengths**: Contextual anchoring; step-by-step progressive disclosure; plain language framing
**Issues**: No loss disclosure; no post-onboarding CTA; tooltip copy too dense
**Top Priority Fix**: Add loss disclosure — required for compliance and user fairness
```

完整示例：

- [预测市场引导分析](examples/prediction-market-onboarding-demo.md)
- [邀请裂变页面分析](examples/invite-vip-page-demo.md)
- [研究伙伴式对话](examples/demo-conversation.md)

## 安装

### Codex / OpenAI Agent Skills / 通用 Agent Skills 客户端

用户级安装：

```bash
SKILL_DIR="$HOME/.agents/skills/ux-interaction-skill"
mkdir -p "$SKILL_DIR"
cp -R SKILL.md LICENSE references assets scripts examples agents "$SKILL_DIR"/
```

项目级安装：

```bash
SKILL_DIR=".agents/skills/ux-interaction-skill"
mkdir -p "$SKILL_DIR"
cp -R SKILL.md LICENSE references assets scripts examples agents "$SKILL_DIR"/
```

### Claude Code

用户级安装：

```bash
SKILL_DIR="$HOME/.claude/skills/ux-interaction-skill"
mkdir -p "$SKILL_DIR"
cp -R SKILL.md LICENSE references assets scripts examples agents "$SKILL_DIR"/
```

项目级安装：

```bash
SKILL_DIR=".claude/skills/ux-interaction-skill"
mkdir -p "$SKILL_DIR"
cp -R SKILL.md LICENSE references assets scripts examples agents "$SKILL_DIR"/
```

### Cursor Agent Skills

```bash
SKILL_DIR="$HOME/.cursor/skills/ux-interaction-skill"
mkdir -p "$SKILL_DIR"
cp -R SKILL.md LICENSE references assets scripts examples agents "$SKILL_DIR"/
```

### OpenClaw / 其他 AgentSkills-compatible 客户端

把 `SKILL.md`、`LICENSE`、`references/`、`assets/`、`scripts/`、`examples/`、`agents/` 放进对应客户端的 `ux-interaction-skill/` 目录即可。README 和项目维护文档只用于 GitHub 展示，不需要安装到运行目录。

## 本地工具

生成打分模板：

```bash
python scripts/ux_scorecard.py --template > my-screen.json
```

运行评分：

```bash
python scripts/ux_scorecard.py --format md my-screen.json
```

校验 Skill 结构：

```bash
python scripts/validate_skill.py .
```

## 仓库结构

```text
ux-interaction-skill/
├── SKILL.md                          ← 核心 Skill 定义（入口文件）
├── README.md                         ← 中文 README（GitHub 展示）
├── README.en.md                      ← English README
├── LICENSE
├── CHANGELOG.md
├── CONTRIBUTING.md
├── SECURITY.md
├── agents/
│   └── openai.yaml                   ← OpenAI / Codex Agent 配置
├── references/
│   ├── ux-four-dimensions.md         ← 四维度深度定义、评分标准、App 案例
│   ├── pattern-library.md            ← 12 个命名设计模式
│   ├── anti-patterns.md              ← 10 个反模式（含优先级分级）
│   ├── multi-path-checklist.md       ← 五类路径覆盖检查清单
│   ├── app-reference-playbook.md     ← App 案例库（按维度 + 场景索引）
│   ├── output-style.md               ← 输出格式规范（含双语总结格式）
│   ├── ux-dialogue-protocol.md       ← 对话和学习模式协议
│   └── risk-and-compliance.md        ← 金融产品暗模式边界
├── assets/
│   ├── analysis-template.md          ← 分析输出模板
│   ├── ux-scorecard.json             ← JSON 打分模板
│   └── research-prompt-pack.md       ← 可复制的 Prompt 模板集
├── scripts/
│   ├── ux_scorecard.py               ← 本地打分脚本
│   └── validate_skill.py             ← Skill 结构校验脚本
├── examples/
│   ├── prediction-market-onboarding-demo.md
│   ├── invite-vip-page-demo.md
│   └── demo-conversation.md
└── evals/
    └── test-cases.md
```

## 研究边界

UX Interaction Skill 提供设计分析、模式推荐和 UX 指导。它不：

- 保证设计改动会产生特定转化率提升
- 做无障碍合规认证
- 建议移除法规要求的披露内容
- 捏造模式或把虚构功能归因于真实 App

## License

MIT
