# Changelog

## 2.0.0 — 2026-07-01

- Restructured skill to match Agent Skill standard (Core promise, Default behavior, Request router, Generation workflow, Animation standards, Platform styles, Output style, Quality boundary, Bundled references).
- Added `references/` directory: animation-tokens, platform-css-tokens, slide-templates, html-engineering-guide, keyword-animation-reference, output-style-and-language.
- Added `assets/`: keyword-animation-map, prompt-pack.
- Added `examples/xhs-skill-intro-demo.md` with annotated walkthrough.
- Added `evals/test-cases.md` with 7 behavior tests.
- Phase 0 (script generation) now requires confirmation before proceeding to Phase 1.
- Added `cntUpDec()` for decimal countUp values.
- Page transition changed from full-viewport slide to fade + 28px translate.
- Added first-slide initialization requirement to quality boundary.
- Platform styles updated: 小红书 now includes 4 content sub-styles (严谨科普/生活分享/投资笔记/好物种草).
- Added platform restriction: 小红书 style prohibits引流 to external platforms.

## 1.0.0 — 2026-06-30

- Initial release with Phase 0, Phase 1, Phase 2 pipeline.
- Four platform styles: 小红书, X/Twitter, TikTok, Dark Pro.
- Keyword animation mapping for 8 keyword types.
- Canvas design philosophy applied: flat surfaces, no box-shadow, no gradient, single accent color.
