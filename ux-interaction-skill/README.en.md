<div align="center">

# UX Interaction Skill

### Turn your AI agent into a sharp UX analyst and interaction designer

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Agent Skill](https://img.shields.io/badge/Agent%20Skill-SKILL.md-black)](SKILL.md)
[![中文](https://img.shields.io/badge/README-%E4%B8%AD%E6%96%87-red)](README.md)
[![English](https://img.shields.io/badge/English-README.en.md-lightgrey)](README.en.md)

</div>

You can feel when a screen is off — but it's hard to say exactly which dimension failed, which pattern to apply, or whether the design covers all edge states.

UX Interaction Skill packages the Google UX Four Dimensions (Useful / Usable / Equitable / Enjoyable), 12 named reusable design patterns drawn from leading apps, and 10 high-frequency anti-patterns into an Agent Skill. Give it a screenshot and it will score each dimension, identify issues by user scenario, recommend named fixes with app references, and return a bilingual summary.

> Design analysis and UX guidance tool. UX Interaction Skill handles evaluation, pattern recommendations, and design direction. Final product decisions stay with your team.

## Core promise

Given a screen, user flow, or design question, run a dimension-by-dimension UX analysis and return a clear, plain-language answer:

`screen → dimensions → specific issues → named patterns → improvement priorities → bilingual summary`

The answer should feel like a sharp design partner talking through the reasoning in normal language.

## What it does for you

| Problem | What to ask | What the skill looks at |
|---|---|---|
| Something feels off about a screen | `Analyze the UX of this screenshot` | Dimension scores + specific issues + pattern-backed fixes |
| You want to understand why a competitor's feature works | `Break down [App]'s [feature] design` | Design decisions and reusable patterns |
| You have two apps doing the same thing | `Compare A and B's [feature] interaction` | Dimension-by-dimension comparison, gaps, strengths |
| A design spec is ready and needs a walkthrough | `Review this design spec` | Four-dimension walkthrough + multi-path coverage check |
| You're designing a feature from scratch | `Help me design the [feature] interaction flow` | Pattern library + path checklist → all-state coverage |
| You suspect a design has dark patterns | `Check this screen for dark patterns` | Anti-pattern checklist, P0 items flagged first |

## Copyable prompts

```text
Analyze the UX of this screenshot using the Google UX Four Dimensions
(Useful / Usable / Equitable / Enjoyable). Score each dimension from 1-5,
identify specific issues with user scenarios, recommend improvements
referencing leading app patterns, and give a bilingual summary.
```

```text
Review the design spec for [feature]. Check multi-path coverage
(entry paths, user states, data states, interaction flows, degraded states),
find UX gaps using the four dimensions, and return a prioritized issue list.
```

```text
Compare [App A] and [App B]'s [feature] design across
Useful / Usable / Equitable / Enjoyable.
Find each one's strengths and what each can borrow from the other.
```

More copyable templates: [assets/research-prompt-pack.md](assets/research-prompt-pack.md)

## Output example

```
### Usable　⭐⭐⭐ 3/5

**What works**
- Step-by-step onboarding with a clear progress indicator (2/3 → 3/3)

**Issues**
- Tooltip copy exceeds 50 words; mobile users won't read it

**Improvement**
- Apply Robinhood's Inline Education Card pattern: keep under 25 words + one number example

---

### Summary

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

Full examples:

- [Prediction market onboarding analysis](examples/prediction-market-onboarding-demo.md)
- [Invite & VIP page analysis](examples/invite-vip-page-demo.md)
- [Design partner conversation](examples/demo-conversation.md)

## Installation

### Codex / OpenAI Agent Skills / generic Agent Skills clients

User-level:

```bash
SKILL_DIR="$HOME/.agents/skills/ux-interaction-skill"
mkdir -p "$SKILL_DIR"
cp -R SKILL.md LICENSE references assets scripts examples agents "$SKILL_DIR"/
```

Project-level:

```bash
SKILL_DIR=".agents/skills/ux-interaction-skill"
mkdir -p "$SKILL_DIR"
cp -R SKILL.md LICENSE references assets scripts examples agents "$SKILL_DIR"/
```

### Claude Code

User-level:

```bash
SKILL_DIR="$HOME/.claude/skills/ux-interaction-skill"
mkdir -p "$SKILL_DIR"
cp -R SKILL.md LICENSE references assets scripts examples agents "$SKILL_DIR"/
```

Project-level:

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

### OpenClaw / other AgentSkills-compatible clients

Copy `SKILL.md`, `LICENSE`, `references/`, `assets/`, `scripts/`, `examples/`, and `agents/` into the client's `ux-interaction-skill/` directory. README and maintenance docs are for GitHub only and do not need to be installed.

## Local tools

Generate a scoring template:

```bash
python scripts/ux_scorecard.py --template > my-screen.json
```

Run a score:

```bash
python scripts/ux_scorecard.py --format md my-screen.json
```

Validate skill structure:

```bash
python scripts/validate_skill.py .
```

## Repo structure

```text
ux-interaction-skill/
├── SKILL.md                          ← Core skill definition (entry point)
├── README.md                         ← Chinese README (GitHub)
├── README.en.md                      ← This file
├── LICENSE
├── CHANGELOG.md
├── CONTRIBUTING.md
├── SECURITY.md
├── agents/
│   └── openai.yaml                   ← OpenAI / Codex agent config
├── references/
│   ├── ux-four-dimensions.md         ← Deep dimension definitions, scoring, app examples
│   ├── pattern-library.md            ← 12 named design patterns
│   ├── anti-patterns.md              ← 10 anti-patterns (prioritized)
│   ├── multi-path-checklist.md       ← 5-category path coverage checklist
│   ├── app-reference-playbook.md     ← App case library (indexed by dimension + scenario)
│   ├── output-style.md               ← Output format rules (bilingual summary format)
│   ├── ux-dialogue-protocol.md       ← Conversation and learning mode protocol
│   └── risk-and-compliance.md        ← Financial product dark pattern boundaries
├── assets/
│   ├── analysis-template.md          ← Reusable analysis output template
│   ├── ux-scorecard.json             ← JSON scoring template
│   └── research-prompt-pack.md       ← Copyable prompt templates
├── scripts/
│   ├── ux_scorecard.py               ← Local scoring script
│   └── validate_skill.py             ← Skill structure validator
├── examples/
│   ├── prediction-market-onboarding-demo.md
│   ├── invite-vip-page-demo.md
│   └── demo-conversation.md
└── evals/
    └── test-cases.md
```

## Boundaries

UX Interaction Skill provides design analysis, pattern recommendations, and UX guidance. It does not:

- Guarantee that design changes will produce specific conversion rate improvements
- Perform accessibility compliance certification
- Recommend removing legally required disclosures
- Attribute fictional features to real apps

## License

MIT
