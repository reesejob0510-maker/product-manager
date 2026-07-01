<div align="center">

# text-to-animated-html

### Turn any topic or voiceover script into a keyword-animated interactive HTML page

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Agent Skill](https://img.shields.io/badge/Agent%20Skill-SKILL.md-black)](SKILL.md)

</div>

Give this skill a topic or an existing voiceover script. It generates a complete animated HTML file: numbers count up, misconceptions get struck through, key phrases highlight, and the visual style matches your target platform.

Core pipeline:

`topic / text → voiceover script → keyword animation map → platform HTML`

## What it does

| Your situation | What to say | What the skill does |
|---|---|---|
| Have a topic, want content | `Make "topic X" into a 小红书-style HTML` | Writes script, maps keywords, generates HTML |
| Have a script, want visuals | `Turn this script into animated HTML` | Skips script step, maps animations, generates file |
| Only need a script | `Write a 90-second voiceover script about X` | Generates time-coded script, stops there |
| Want to change platform | `Switch to Dark Pro style` | Replaces CSS tokens only, keeps all content and JS |
| Adjust one animation | `Make page transitions slower, fade in` | Changes only transition duration and lock timeout |

## Automatic keyword animation

The skill scans the script and assigns animations to 8 keyword types:

| Keyword type | Signal | Animation |
|-------------|--------|-----------|
| Amount / metric | number + unit (亿, %, ×, B, T) | `countUp` large numeral |
| Contrast / misconception | "not X but Y" / misbelief frames | myth-card ✕ → ✓ sequence |
| Share / rank | market share, "number one", percentage of total | `progressBar` fill |
| Emotion word | "quietly", "beyond expectations", "doubled" | `highlightPulse` |
| Question / suspense | sentence ending in "?", "why", "what really" | `typewriter` char-by-char |
| Named entity (first mention) | proper noun on first appearance | `stampIn` large reveal |
| Time anchor | decade, quarter, "last year", "Q3" | timeline `fadeUp` |
| Scene metaphor | factory, highway, nervous system | illustration `fadeUp` |

## Four platform styles

| Style | Canvas | Best for |
|-------|--------|---------|
| **小红书** · Warm Notes | 3:4 vertical card | Lifestyle, knowledge, investment diary, product reviews |
| **X / Twitter** · Feed Card | 1:1 square | Finance commentary, data breakdowns, hot takes |
| **TikTok** · Vertical Impact | 9:16 full screen | Hook slides, data shock, cognitive disruption |
| **Dark Pro** · Professional Dark | Full-screen paged | Finance/tech analysis, business reports |

## Copy these prompts

```text
Turn this topic into an animated HTML page, 小红书 style: [topic]
Generate the voiceover script first and wait for my confirmation.
```

```text
I already have a script. Make it into TikTok vertical style HTML:
[paste script]
```

```text
Use /html-animate to visualize this content. Recommend a platform style:
[paste content]
```

More templates: [assets/prompt-pack.md](assets/prompt-pack.md)

## Installation

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

## Repository structure

```text
text-to-animated-html-skill/
├── SKILL.md
├── README.md
├── README.en.md
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

## Quality boundary

Generated HTML files are:
- Fully self-contained, zero external dependencies, work offline
- Free of `fetch()`, external `<script src>`, or CDN font imports
- Never contain invented numbers or facts not provided by the user
- 小红书 style never引流 to external platforms

## License

MIT
