# Output Style and Language

Use this file when preparing and presenting outputs.

## Default response shape

Answer like a design partner. Lead with the plan, not a preamble.

Good flow for full pipeline:
1. Show the keyword-animation table (≤10 rows, most important first).
2. State the platform style and one-line reason.
3. Ask for confirmation OR note "直接生成" was requested.
4. Write the HTML file.
5. Start server and open browser.
6. Return file path.

Skip confirmation when the user says: "直接生成"、"skip"、"不用确认"、"就这样".

## Presenting the keyword table

Keep it tight. Show the most visually interesting mappings first.

```
| 原文片段          | 类型     | 动画            | 页码 |
|-----------------|---------|----------------|-----|
| 成交 20 亿       | 金额     | countUp 大字    | 页 1 |
| 不是…而是…       | 对比误解  | myth card      | 页 2 |
| 这到底是为什么？  | 疑问句   | 打字机逐字       | 页 6 |
```

If there are > 10 keywords, group minor ones: "其余 5 个情绪词统一用 highlightPulse，延迟错开".

## Platform recommendation language

Use plain, direct reasoning:

- "内容是财经分析，数据密集，推荐 Dark Pro 风格 — 暗色背景让数字更突出。"
- "这是生活分享类内容，推荐小红书风格 — 暖白卡片，节奏轻盈。"
- "用户明确说了 TikTok，每页只放一个核心词，节奏要快。"

## Post-preview adjustment patterns

When user asks to change something after viewing:

**Transition speed**: "页面过渡再慢一点"
→ Change transition duration (`1.1s → 1.4s`) and lock timeout. Nothing else.

**Animation feel**: "数字滚动快一点" / "入场太快了"
→ Change the specific countUp duration or animation-delay. Not the whole file.

**Style switch**: "改成深色版"
→ Replace the CSS `:root {}` token block and `.slide {}` canvas sizing. Preserve all HTML content and JS logic.

**Text fix**: Any content correction
→ Edit only that text node. Do not regenerate the file.

## Language rules

- Respond in Chinese unless the user writes in English.
- Use "页" not "slide" in Chinese contexts.
- Use "强调色" not "accent color" in Chinese.
- Avoid CSS/JS jargon in confirmations — say "数字会从 0 滚动到 20 亿" not "countUp from 0 to 20 with data-target=20".

## Strong judgment rules

Give a clear platform recommendation even when the user doesn't ask:
- "这类内容最适合 Dark Pro，因为数据量大，深色背景能让数字焦点更清晰。"
- "小红书风格节奏偏慢，和这段脚本的紧凑感不太匹配，建议用 X 风格。"

Say exactly what is missing when something can't be animated:
- "这里的 '超过十年' 是时间表达，不是数字指标，我会用 timeline fadeUp 而不是 countUp。"
