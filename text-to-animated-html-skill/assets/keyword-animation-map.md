# Keyword Animation Map

Quick-reference table for all keyword → animation mappings.

## Complete mapping

| Keyword signal | Type | Animation | Notes |
|---------------|------|-----------|-------|
| 数字 + 亿/万/% /倍/B/T | Amount/metric | `countUp` large numeral | Decimal → `cntUpDec` |
| 不是…而是… / 以为…实际 | Contrast | myth-card ✕→✓ | Full sequence |
| 误解 / 真相 / 谣言 | Misconception | myth-card ✕→✓ | Full sequence |
| 市占率 / 占比 / 第一 | Share/rank | `progressBar` fill | Label with company name |
| 十年 / Q3 / 去年 / 上季度 | Time anchor | timeline `fadeUp` | Not animated if just context |
| 悄悄 / 超预期 / 翻倍 / 震惊 | Emotion | `highlightPulse` | Max 1 per slide |
| 疑问句 / 为什么 / 到底 | Question | `typewriter` | Great for closing slide |
| 品牌/公司 首次出现 | Entity reveal | `stampIn` large | First mention only |
| 场景类比 (工厂/公路/神经系统) | Metaphor | `fadeUp` + illustration box | No special anim needed |
| 数据来源 / 免责声明 | Disclaimer | tiny `.disc` class | `opacity:.6`, no animation |

## Animation class reference

| Class | Effect | Use on |
|-------|--------|--------|
| `.ai .d1–.d6` | fadeUp with 0.06s–0.78s delay | Most elements |
| `.al .d1–.d6` | fadeL (from left) with delay | List items, cards |
| `.mc1 .mc2 .mc3` | myth-card staggered fadeL | Myth cards only |
| `.mico1 .mico2 .mico3` | stampIn for ✕/✓ icons | Myth card icons |
| `.sl1 .sl2` | growLine strikethrough | Myth card wrong text |
| `.pulse-active` | highlightPulse | Closing key phrase |
| `data-cu` | countUp trigger | Metric spans |
| `.gn1–.gn4` | node fadeUp for diagrams | Architecture slides |
| `.oc1 .oc2` | optical connector animation | Diagram connectors |

## Per-platform animation checklist

### 小红书
- ✅ `fadeUp` with 100ms stagger steps
- ✅ `countUp` 2.0–2.5s duration
- ✅ `typewriter` 100ms/char
- ✅ myth-card (without box-shadow glow)
- ❌ No `stampIn` on body text
- ❌ No `bounce`, `rotate`, or spring easing
- ❌ No `truthGlow` (requires box-shadow)

### X / Twitter
- ✅ `fadeUp` 0.4s fast entry
- ✅ `countUp` 1.5s
- ✅ `progressBar`
- ✅ `highlightPulse` once at end
- ❌ No `typewriter` (too slow)
- ❌ No myth-card (too tall for 1:1 format)

### TikTok
- ✅ `stampIn` 0.35s for main word
- ✅ `countUp` 0.8s
- ✅ `fadeUp` caption at 350ms delay
- ❌ No stagger lists (only 1 element per slide)
- ❌ No `truthGlow`, `dotTravel`, `scaleV`

### Dark Pro
- ✅ All animations available
- ✅ `truthGlow` and `glowPulse` OK
- ✅ `dotTravel` for architecture diagrams
- ✅ `countUp` 3.0s
- ✅ myth-card full sequence
