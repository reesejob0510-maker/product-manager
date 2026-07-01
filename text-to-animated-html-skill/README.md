<div align="center">

# text-to-animated-html

### 把任何话题或口播文案，做成带关键词动效的可交互 HTML 网页

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Agent Skill](https://img.shields.io/badge/Agent%20Skill-SKILL.md-black)](SKILL.md)

</div>

你有一段口播文案，或者只是一个话题——这个 skill 帮你把它变成一个完整的动画 HTML 页面：数字会滚动，误解会被打叉，关键词会高亮，页面风格匹配目标平台。

核心流程：

`话题 / 文字 → 口播脚本 → 关键词动画映射 → 平台专属 HTML`

## 它能做什么

| 你遇到的场景 | 可以这样说 | skill 会帮你做什么 |
|---|---|---|
| 有个话题，想做成内容 | `帮我把"XX话题"做成小红书风格 HTML` | 先写口播脚本，再识别关键词，最后生成 HTML |
| 已有口播稿，想可视化 | `帮我把这段脚本做成动画 HTML` | 跳过脚本步骤，直接识别动画，生成文件 |
| 只需要脚本 | `帮我写一段 1分30秒 的口播稿，话题是XX` | 按时间轴生成完整脚本，停在这一步 |
| 想换平台风格 | `改成深色 Dark Pro 风格` | 只替换 CSS 样式，保留所有内容和动画 |
| 调整某个动画 | `翻页过渡再慢一点，渐入进入` | 只改 transition 时长，不动其他 |

## 关键词自动动画

skill 会扫描脚本，识别 8 类关键词并分配动画：

| 关键词类型 | 识别信号 | 动画 |
|-----------|---------|------|
| 金额 / 数字 | 数字 + 亿/万/%/倍/B/T | countUp 大字滚动 |
| 对比 / 误解 | 不是…而是… / 误解/真相 | 打叉卡片 → 打勾真相 |
| 占比 / 排名 | 市占率 / 占比 / 第一 | progressBar 填充 |
| 情绪词 | 悄悄 / 超预期 / 翻倍 | highlightPulse 高亮 |
| 疑问句 | 以"？"结尾 / 为什么 / 到底 | 打字机逐字 |
| 品牌首次出现 | 专有名词首次提及 | stampIn 弹出 |
| 时间节点 | 十年 / Q3 / 上季度 | 时间轴 fadeUp |
| 场景类比 | 工厂 / 公路 / 神经系统 | 图示 fadeUp |

## 四种平台风格

| 风格 | 画幅 | 适合内容 |
|------|------|---------|
| **小红书** · 温润笔记 | 3:4 竖版卡片 | 生活分享、知识笔记、投资日记、好物种草 |
| **X / Twitter** · 信息流 | 1:1 方版 | 财经评论、数据解读、热点分析 |
| **TikTok** · 竖版爆款 | 9:16 全屏 | 钩子冲击、认知颠覆、情绪共鸣 |
| **Dark Pro** · 暗黑专业 | 全屏分页 | 科技/金融分析、商业报告 |

## 直接复制这些 Prompt

```text
帮我把这个话题做成动画 HTML 页面，小红书风格：[话题]
请先生成口播脚本确认后再做 HTML。
```

```text
我已经有口播稿了，帮我直接做成 TikTok 竖版风格 HTML：
[粘贴脚本]
```

```text
用 /html-animate 把以下内容可视化，推荐一个合适的平台风格：
[粘贴内容]
```

更多可复制模板见 [assets/prompt-pack.md](assets/prompt-pack.md)。

## 输出长什么样

```text
关键词动画识别完成：

| 原文片段          | 类型   | 动画         | 页码 |
|-----------------|-------|-------------|-----|
| 成交 20 亿       | 金额   | countUp 大字 | 页 1 |
| 不是…而是…       | 对比   | myth card   | 页 2 |
| 这到底是哪个故事？ | 疑问   | 打字机逐字   | 页 6 |

推荐平台：Dark Pro（内容是财经分析，数据密集）。

确认后生成 HTML？
```

确认后生成文件，自动在浏览器打开预览，返回绝对路径。

完整示例：[小红书 Skill 自我介绍](examples/xhs-skill-intro-demo.md)

## 安装

### Cursor Agent Skills

```bash
SKILL_DIR="$HOME/.cursor/skills/text-to-animated-html"
mkdir -p "$SKILL_DIR"
cp -R SKILL.md LICENSE references assets examples evals "$SKILL_DIR"/
```

### Claude Code

```bash
SKILL_DIR="$HOME/.claude/skills/text-to-animated-html"
mkdir -p "$SKILL_DIR"
cp -R SKILL.md LICENSE references assets examples evals "$SKILL_DIR"/
```

### 通用 Agent Skills 客户端

把 `SKILL.md`、`LICENSE`、`references/`、`assets/`、`examples/`、`evals/` 放进对应客户端的 skill 目录即可。

## 仓库结构

```text
text-to-animated-html-skill/
├── SKILL.md
├── README.md
├── CHANGELOG.md
├── CONTRIBUTING.md
├── LICENSE
├── SECURITY.md
├── references/
│   ├── animation-tokens.md
│   ├── platform-css-tokens.md
│   ├── slide-templates.md
│   ├── html-engineering-guide.md
│   ├── keyword-animation-reference.md
│   └── output-style-and-language.md
├── assets/
│   ├── keyword-animation-map.md
│   └── prompt-pack.md
├── examples/
│   └── xhs-skill-intro-demo.md
└── evals/
    └── test-cases.md
```

## 质量边界

skill 生成的 HTML 文件：

- 完全自包含，零外部依赖，可离线打开
- 不含 `fetch()`、外部 `<script src>`、CDN 字体
- 不捏造用户未提供的数字或事实
- 小红书风格严格禁止引流到外部平台

## License

MIT
