---
name: text-to-animated-html
description: >-
  Turn any text or topic into a voiceover script, then into a keyword-animated
  interactive HTML page. Trigger on: "帮我做成 HTML"、"生成动画网页"、"帮我写口播稿"、
  "做成小红书风格"、"做成可交互页面"、"结构化展示"、/html-animate、/voiceover、
  /structured-html。Supports full pipeline (topic → script → HTML) or
  partial (script only, or HTML only from existing script). Platform styles:
  小红书 / X·Twitter / TikTok / Dark Pro.
license: MIT
compatibility: Agent Skills-compatible clients. Shell, Write, and browser-open access recommended.
metadata:
  version: "2.0.0"
  short-description: Topic or text → voiceover script → keyword-animated HTML
---

# text-to-animated-html

Turn a topic or existing script into a keyword-animated, platform-styled HTML page.

`topic / text → voiceover script → keyword animation map → platform HTML`

The output should feel like a short-video slide deck: each page carries one idea, key data points animate in, and the visual style matches where the content will live.

---

## Core promise

Given a topic, raw text, or an existing voiceover script, run the generation pipeline and return a self-contained HTML file that:

- structures the content into full-screen slides, one idea per page;
- auto-detects keywords (numbers, contrasts, questions, emotion words) and assigns each an animation;
- matches the visual style of the target platform (小红书, X/Twitter, TikTok, or Dark Pro);
- works offline, zero external dependencies, drop-in to any browser.

---

## Default behavior

Full pipeline is the default.

When the user gives a topic or raw text without a clear time-coded script, generate the voiceover script first before building HTML.

When the user already has a script (time-coded or segmented), skip script generation and go directly to keyword mapping.

Always show the keyword-animation table and platform style choice to the user before writing the HTML file — unless the user explicitly says "直接生成" or "skip confirmation".

When platform is not specified, infer from content type and state the recommendation with a one-line reason.

---

## Request router

Classify the request, then work in the matching mode.

- **Full pipeline**: User gives a topic, article, or data dump with no script. Run Phase 0 → Phase 1 → Phase 2.
- **Script + HTML**: User provides an existing script. Run Phase 1 → Phase 2.
- **Script only**: User says "帮我写口播稿" or "只要脚本". Run Phase 0, stop, return the script.
- **HTML only**: User says "直接做 HTML" and provides structured content. Run Phase 2 only.
- **Style switch**: User asks to change platform style on an existing HTML. Swap the CSS token block only; preserve all content and animation logic.
- **Animation edit**: User asks to adjust a specific animation (speed, type, delay). Edit the relevant CSS keyframe or JS trigger only.

---

## Generation workflow

### Phase 0 — Voiceover script

Run when the user has no existing script.

Structure the script with time markers at natural-language pacing (Mandarin: ~3.5–4 characters/second):

```
[0:00–0:08]  Opening hook       — one sentence that creates suspense or contrast
[0:08–0:22]  Core identity      — define the subject in 1–2 sentences, emphasize the differentiator
[0:22–0:50]  Body               — 3–5 points, each ≤2 sentences; use analogy or hard data
[0:50–1:08]  Data anchor        — 2–4 key figures with a one-line interpretation each
[1:08–1:22]  Cognitive twist    — reveal a common misread or unexpected comparison
[1:22–1:30]  Closing hook       — open question that invites reflection or reply
```

Rules:
- Never invent numbers. Use only figures the user provided or that are publicly verifiable.
- Every sentence should carry information. Cut filler.
- Show the draft to the user and wait for confirmation before proceeding.

### Phase 1 — Keyword animation mapping

Scan the script and assign an animation to each detected keyword type.

| Keyword type | Detection signal | Animation |
|-------------|-----------------|-----------|
| Amount / metric | number + unit (亿、%、×、万、B、T) | `countUp` large numeral |
| Contrast pair | "不是…而是…"、"反而"、"A vs B" | myth-card: ✕ strike → ✓ reveal |
| Time anchor | decade, quarter, "去年", "上季度" | timeline node `fadeUp` |
| Share / rank | "第一"、"占 X%"、"市占率" | `progressBar` fill |
| Emotion word | "悄悄"、"超预期"、"翻倍"、"震惊" | `highlightPulse` |
| Question / suspense | ends with "？", contains "为什么"、"到底" | `typewriter` char-by-char |
| Named entity (first mention) | proper noun on first appearance | `stampIn` large reveal |
| Misconception frame | "误解"、"以为"、"真相"、"实际上" | myth-card sequence |

Present the mapping as a table before writing HTML:

```
| 原文片段          | 类型     | 动画            | 页码 |
|-----------------|---------|----------------|-----|
| 成交 20 亿       | 金额     | countUp + 大字  | 页 1 |
| 不是 X，而是 Y   | 对比     | myth card       | 页 3 |
| 这到底是为什么？  | 疑问     | typewriter      | 页 6 |
```

### Phase 2 — HTML generation

Write a single self-contained `.html` file to `~/Desktop/<topic>.html`.

**Slide architecture**

```html
<div class="deck">
  <div class="slide go" id="s0">…</div>   <!-- first slide: class="go" is required -->
  <div class="slide" id="s1">…</div>
  …
</div>
```

**Required JS initialization — never omit**

```javascript
// First slide must be positioned manually or it stays invisible
slides[0].style.opacity  = '1';
slides[0].style.transform = 'translateY(0)';
trigger(0); ui();
```

**Page transition**

Use opacity + subtle translate (not full-viewport slide) for a softer feel:

```javascript
function pos(el, p) {
  if (p === 'c') { el.style.opacity = '1';  el.style.transform = 'translateY(0)'; }
  else if (p === 'a') { el.style.opacity = '0'; el.style.transform = 'translateY(-28px)'; }
  else               { el.style.opacity = '0'; el.style.transform = 'translateY(28px)'; }
}
```

Transition duration: 1.0–1.2 s for 小红书/Dark Pro; 0.6 s for TikTok.

**Animation reset per slide**

Every time a slide becomes active, `trigger(n)` must reset and replay all animations on that slide — including countUp, progressBar, typewriter, and CSS class toggles:

```javascript
slides[cur].classList.remove('go');
void slides[cur].offsetWidth;          // force reflow before re-adding
slides[cur].classList.add('go');
trigger(cur);
```

---

## Animation standards

For every animated element, verify:

- `countUp` — element has `data-cu`, `data-target`, `data-suffix`; resets to `0` on each `trigger(n)` call.
- `typewriter` — text node clears to `''` before retyping; speed 80–120 ms/character.
- `progressBar` — width resets to `0%` with `transition:none` + reflow, then transitions to target.
- `highlightPulse` — keyframe goes transparent → accent-color background → transparent; single pass only.
- `stampIn` — `scale(0) rotate(-20deg)` → `scale(1.2) rotate(5deg)` → `scale(1) rotate(0)`, 0.35 s max.
- `myth-card` — ✕ stampIn → growLine strikethrough → dimText → ✓ checkIn → truth text fadeUp, in sequence.

Animation timing per platform:

| Platform | Single element max | Page entry target | countUp duration |
|---------|-------------------|------------------|-----------------|
| 小红书   | 0.6 s             | all in ≤ 0.8 s   | 2.0–2.5 s       |
| X        | 0.4 s             | all in ≤ 0.5 s   | 1.5 s           |
| TikTok   | 0.35 s            | all in ≤ 0.4 s   | 0.8 s           |
| Dark Pro | 0.6 s             | all in ≤ 1.0 s   | 3.0 s           |

---

## Platform styles

When platform is not specified, recommend based on content type and state the reason.

### 小红书 — 温润笔记
> Lifestyle, knowledge notes, investment diary, product reviews

- **Canvas**: `width: min(400px, 94vw); height: min(536px, 90dvh); border-radius: 18px`
- **Colors**: bg `#FAFAF8` · text `#1A1A1A` · accent `#E95C4B` · card `#F5F0EA` · border `#E2DAD0`
- **Type**: title `font-weight:900; clamp(27px,8vw,38px)` · body `14px, line-height:1.8`
- **Design rules**: flat surfaces only; no box-shadow; no gradient; accent color ≤ 10% of area; one visual focus per slide; generous whitespace
- **Animation**: `fadeUp` only — no bounce, no rotate; stagger 100 ms steps; countUp starts 500 ms after slide entry
- **Content styles within 小红书**: 严谨科普 / 生活分享 / 投资笔记 / 好物种草

### X / Twitter — 信息流卡片
> Financial commentary, data breakdowns, opinion pieces

- **Canvas**: `width: min(480px, 94vw); aspect-ratio: 1/1`
- **Colors (dark)**: bg `#0F1117` · text `#E7E9EA` · accent `#1D9BF0` · border `rgba(255,255,255,.1)`
- **Type**: title `font-weight:700; clamp(20px,5vw,32px)` · data `font-weight:800; clamp(36px,10vw,64px); color:#1D9BF0`
- **Design rules**: corner radius ≤ 8px; dividers `1px solid rgba(255,255,255,.08)`; no decorative borders on cards
- **Animation**: fast entry (0.4 s total); `highlightPulse` once at end; no typewriter (too slow for X's pace)

### TikTok — 竖版爆款
> Impact hooks, cognitive disruption, emotion-driven content

- **Canvas**: `width: min(390px, 94vw); height: 100dvh`
- **Colors**: bg `#0A0A0A` · text `#FFFFFF` · accent: pick ONE per file from `#00F5FF / #FF2D55 / #FF9500 / #39FF14`
- **Type**: main word `font-weight:900; clamp(56px,18vw,96px); letter-spacing:-.03em` · caption `18px; rgba(255,255,255,.7)`
- **Design rules**: one idea per slide — one big word/number + 1–2 caption lines, nothing else; no side nav dots
- **Animation**: `stampIn` for large text (0.35 s); caption `fadeUp` at 350 ms delay; countUp 800 ms; page transition 0.6 s with spring easing `cubic-bezier(.16,1,.3,1)`
- **Forbidden**: multiple accent colors in one file; gradient text; glow that obscures text; any animation step > 1 s

### Dark Pro — 暗黑专业
> Finance/tech analysis, business reports, data-heavy decks

- **Canvas**: `position: fixed; inset: 0` (true full-screen)
- **Colors**: bg `#090d18` · accent `#6366f1` · accent2 `#818cf8` · card `#0f1626` · border `rgba(99,102,241,.18)`
- **Design rules**: dashed borders for internal containers; large numerals with clamp(60px,16vw,100px); myth-card animations available
- **Reference**: see `/Users/admin/Desktop/marvell-story.html` for full implementation

---

## Output style

Lead with the artifact, not the explanation.

- Show the keyword-animation table before HTML generation; keep it to ≤10 rows.
- State the platform style and one-line reason.
- Write the HTML file with `Write` or Python shell (if `Write` is hook-blocked).
- Start the HTTP server then open: `python3 -m http.server 8765 & sleep 1 && open http://localhost:8765/<file>.html`
- Return the absolute file path.
- Do not narrate what each CSS rule does. Code comments only for non-obvious intent.

When the user asks for adjustments after preview:
- Transition speed → change transition duration + lock timeout only
- Animation feel → change the specific `@keyframes` or `trigger()` call
- Style switch → replace CSS token block, preserve HTML structure

---

## Quality boundary

Never do:

- Invent numbers, dates, or facts not provided by the user
- Reference external URLs, CDNs, or web fonts in the HTML
- Use `alert()`, `fetch()`, or `eval()`
- Apply `box-shadow`, `text-shadow`, or gradient text in 小红书 or X styles
- Use more than one accent color per TikTok file
- Skip the `slides[0].style.opacity='1'` initialization

Always verify before writing:

- [ ] `slides[0]` opacity and transform initialized in JS
- [ ] Every `countUp` element has `data-cu`, `data-target`, `data-suffix`
- [ ] `trigger(n)` resets and replays all per-slide animations
- [ ] Font sizes use `clamp()` — no fixed `px` on headings
- [ ] File is fully self-contained; no external requests

---

## Bundled references

Load only what is needed:

- `references/animation-tokens.md` — keyframe library: fadeUp, stampIn, checkIn, growLine, scaleV, dotTravel, highlightPulse, dimText, truthGlow
- `references/platform-css-tokens.md` — ready-to-paste CSS variable blocks for each platform style
- `references/slide-templates.md` — HTML snippets for common slide types: hook, metric, myth-card, speed-bar, client-grid, closing
- `references/voiceover-examples.md` — example scripts by content type (finance, lifestyle, science, product)
