# Evaluation Test Cases

Use these prompts to test trigger detection, pipeline routing, animation mapping, and output quality.

## Test 1: Full pipeline from topic

Prompt:
```
帮我把"比亚迪在欧洲的市场扩张"做成动画 HTML 页面，小红书风格。
```

Expected behavior:
- Classifies as full pipeline (no script exists).
- Generates a voiceover script with time markers before proceeding.
- Waits for user confirmation before generating HTML (unless "直接生成" was said).
- Detects: market share numbers → progressBar; brand first mention → stampIn or typewriter; any "增长X%" → countUp.
- Recommends 小红书 style (already specified by user).
- Outputs self-contained HTML with 小红书 CSS tokens.
- First slide is visible on load (opacity and transform initialized in JS).

## Test 2: Script provided, HTML only

Prompt:
```
我已经有口播稿了，帮我直接做成 TikTok 竖版风格 HTML：
[0:00] 有一个秘密，全球最顶尖的 AI 公司都知道…
[0:05] 光不够快，AI 就死了。
[0:12] 现在的传输速度是 800G。下一代 1.6T，翻倍。
[0:20] 做这件事超过十年的公司，叫迈威尔。
```

Expected behavior:
- Classifies as Script + HTML (script exists).
- Skips Phase 0, goes directly to keyword mapping.
- Detects: "800G" and "1.6T" → countUp + comparison; "翻倍" → highlightPulse; "迈威尔" first mention → stampIn; "秘密" → typewriter.
- Selects TikTok style (specified). One idea per slide. One large word per page.
- Uses spring easing `cubic-bezier(.16,1,.3,1)` for TikTok page transitions.
- Each slide has max 1 animated element entering at a time.

## Test 3: Keyword mapping accuracy

Prompt:
```
帮我识别这段脚本的关键词动画，不用生成 HTML：
"英伟达悄悄往一家公司砸了 20 亿美元。这家公司不是做手机芯片的，也不是英伟达的竞争对手——
它是 AI 数据中心里，芯片和芯片之间传数据的神经系统。FY2026 营收 82 亿美元，增长 42%。
数据中心业务占比已经达到 76%。你买迈威尔，你买的到底是哪个故事？"
```

Expected behavior:
- Returns keyword-animation table only (Script only route, no HTML).
- Must identify:
  - "20 亿美元" → countUp
  - "悄悄" → highlightPulse
  - "不是…也不是…" → myth-card (contrast pair)
  - "82 亿美元" → countUp
  - "增长 42%" → countUp or progressBar
  - "76%" → progressBar
  - "迈威尔" (first mention) → stampIn
  - "你买的到底是哪个故事？" → typewriter
- Table has ≤10 rows, most important first.

## Test 4: Style inference

Prompt:
```
帮我把这段分析做成 HTML：
"Broadcom 拿了定制 AI 芯片市场的 55-60%。Marvell 只有 13-15%。
但光学芯片这层，Marvell 才是真正难以被替代的。换一家供应商，认证周期以年来计算。"
```

Expected behavior:
- No platform specified. Agent must infer and state reason.
- Correct inference: Dark Pro (financial/tech analysis, data-heavy, English company names, contrast between market shares).
- Wrong inference: 小红书 (too casual), TikTok (too long per slide).
- Must name the reason: "内容是竞争格局分析，数据对比密集，推荐 Dark Pro 风格。"

## Test 5: Post-preview adjustment

Prompt (after viewing HTML):
```
页面和页面的过渡再缓慢一点，渐入进入。
```

Expected behavior:
- Edit only: transition duration (increase), transition style (add opacity fade), lock timeout (increase to match).
- Do NOT regenerate: HTML content, slide structure, animations, CSS token block.
- The `pos()` function should switch from `translateY(100vh)` to `opacity + 28px translate` style.

## Test 6: Platform restriction

Prompt:
```
小红书风格 HTML，内容里提到"大家也可以去 TikTok / X 上关注我"。
```

Expected behavior:
- Remove or omit external platform mentions in the HTML output.
- Optionally flag to user: "小红书 禁止引流到外部平台，已从内容中移除相关引导语。"
- Do not silently keep them.

## Test 7: No external dependencies

After generating any HTML file, verify:
- No `<link>` or `<script src>` tags pointing to external URLs.
- No `fetch()` calls.
- No `@import url(...)` for fonts.
- File works fully offline (open as `file://` in browser).
