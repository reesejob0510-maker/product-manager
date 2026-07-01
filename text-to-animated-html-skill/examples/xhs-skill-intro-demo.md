# Example: 小红书 Skill Self-Introduction

**Topic**: Introduce the `text-to-animated-html` skill itself  
**Platform**: 小红书 — 温润笔记  
**Pipeline entry**: Script + HTML (script was generated first, then confirmed)

## Voiceover script used

```
[0:00–0:06] 钩子
  有一个 AI skill，能把你的任何一段文字，做成会动的 HTML。

[0:06–0:20] 介绍
  它叫 text-to-animated-html。三步走：给个话题，它帮你写口播脚本；
  再扫描关键词，自动分配动画；最后生成一个完整的 HTML 文件。

[0:20–0:50] 能力主体
  能力一：口播脚本生成。给话题就能写，时间轴精确到每段。
  能力二：关键词自动动画。说了"20亿"，数字就会滚动；说了误解，就有打叉打勾卡片。
  能力三：4 种小红书内容风格可选：严谨科普、生活分享、投资笔记、好物种草。

[0:50–1:00] 触发方式
  对 AI 说"帮我做成 HTML"、"小红书风格"、或者 /html-animate，就能触发。

[1:00–1:06] 留钩
  你的下一篇内容，可以更有意思。
```

## Keyword animation map

| 原文片段 | 类型 | 动画 | 页码 |
|---------|------|------|-----|
| text-to-animated-html | 品牌首现 | typewriter 逐字 | 页 1 |
| 三步走 | 流程 | 三格 flow box 顺序 fadeUp | 页 2 |
| 口播脚本生成 / 关键词自动动画 / 4种风格 | 能力列表 | 时间轴节点顺序 fadeUp | 页 3-5 |
| 说了"20亿"，数字就会动 | 示例 | 页标题 highlightPulse | 页 4 |
| 4 种小红书风格 | 数字 | countUp 0→4 | 页 5 |
| 帮我做成 HTML / /html-animate | 触发词 | stagger phrase list | 页 6 |

## Platform chosen

小红书 · 温润笔记  
**Reason**: content is a tool introduction — warm, approachable, knowledge-sharing tone fits 小红书 perfectly.

## Output file

`/Users/admin/Desktop/skill-intro-xhs.html`

## Key design decisions

1. **Stage background**: `#E8E3DB` (slightly darker warm tone) creates a "card on paper" feel, making the white card pop without any shadow.

2. **Bottom page indicator**: Instead of a floating counter, each slide has a bottom bar with `TEXT-TO-ANIMATED-HTML` + `0N / 06` — keeps the 小红书 notebook aesthetic.

3. **Flow diagram (page 2)**: Three boxes with `→` arrows instead of a numbered list — more visual, one glance understands the pipeline.

4. **4-style grid (page 5)**: Each style gets a color dot (7px) + name + two-line description. The dot colors are informational (one per style), not decorative.

5. **No bounce/rotate**: Consistent with 小红书 "soft notes" feel — all entrances are `fadeUp` or `fadeL`, no `stampIn`.

## Adjustments made after preview

- **Transition**: Changed from full-viewport slide (`translateY(100vh)`) to fade + 28px translate. Duration 0.82s → 1.15s. Lock timeout extended to 1.3s.
- **Slide 5 content**: Replaced 4 platform style cards (小红书/X/TikTok/Dark Pro) with 4 小红书 content style cards (严谨科普/生活分享/投资笔记/好物种草) — per platform policy: no引流 to external platforms.
