# Keyword Animation Reference

Complete detection rules and edge cases for Phase 1 keyword mapping.

## Detection rules

### Amount / metric → countUp
Match: digit(s) + unit in the same phrase.
Units: 亿、万、%、×、倍、B、T、M、K、百万、千万
Examples: "成交 20 亿"、"增长 42%"、"速度翻 2 倍"、"$8.2B revenue"
Animation: large numeral countUp + super-sized font display

Edge cases:
- Decimals (8.2B): use `cntUpDec()` function
- Ranges (13–15%): animate to midpoint, display as range in label
- "超过 70%": show `>` prefix, animate 0→70
- Year numbers (2026): do not animate — not a metric

### Contrast pair → myth-card
Match: explicit A-vs-B patterns
Patterns: "不是…而是…"、"以为…其实…"、"反而…"、"A vs B"、"误解…真相…"
Animation: two ✕ cards with strikethrough, one ✓ truth card with glow

Edge cases:
- Three-way contrast: use three ✕ cards, one ✓
- Subtle contrasts ("大家觉得…但…"): use highlightPulse on the twist word instead

### Time anchor → timeline fadeUp
Match: temporal reference without a number metric
Examples: "十年"、"上季度"、"去年底"、"Q3"、"2020 年以来"
Animation: timeline node with timestamp label, fadeUp with sequential delay

### Share / rank → progressBar
Match: relative position or percentage of a total
Examples: "市占率 55%"、"全球第一"、"占比 76%"、"Broadcom 拿了 60%"
Animation: horizontal bar fills from 0 to target %, labeled with company/category

### Emotion word → highlightPulse
Match: single high-impact word or phrase (not a number)
Examples: "悄悄"、"震惊"、"超预期"、"翻倍"、"不可或缺"、"难以替代"
Animation: word/phrase gets background-color pulse, single pass, 2.5s

Limit: one `highlightPulse` per slide. If multiple emotion words on one slide, pick the strongest.

### Question / suspense → typewriter
Match: sentence ending in "？" or containing "为什么"、"到底"、"真的吗"、"你知道吗"
Animation: text clears, then types char by char at 80–100ms/char
Best for: closing question, opening hook, rhetorical reveal

### Named entity (first mention) → stampIn
Match: proper noun (brand, company, product, person) appearing for the first time
Examples: "迈威尔科技"、"Marvell Technology"、"ChatGPT"
Animation: large display with stampIn (scale 0→1.2→1, rotate -20→0)

Only apply on first mention. Subsequent mentions use normal text.

### Misconception frame → myth-card sequence
Match: explicit framing of a misbelief being corrected
Signals: "误解"、"你以为"、"大家都认为"、"其实"、"真相是"
Animation: full myth-card sequence (same as contrast pair)

## Priority when multiple types apply

If a phrase matches multiple rules, apply in this priority:
1. Myth-card (strongest visual, use when frame is explicit)
2. countUp (always animate numbers)
3. highlightPulse
4. typewriter
5. stampIn
6. progressBar
7. timeline fadeUp

## What not to animate

- Source citations ("SEC 财报"、"据彭博报道")
- Dates used as context, not metrics ("2020 年成立")
- Filler transitions ("然后"、"接下来"、"总的来说")
- Every sentence — animation should highlight, not flood
