# Contributing

text-to-animated-html accepts contributions that improve animation quality, platform accuracy, keyword detection, reference documentation, examples, and evaluation coverage.

## Good contributions

- New animation patterns that work across platforms
- Additional platform styles (e.g. LinkedIn, Instagram Reels)
- Better keyword detection edge cases in `references/keyword-animation-reference.md`
- More slide template types in `references/slide-templates.md`
- New example demos in `examples/`
- Additional eval test cases in `evals/test-cases.md`
- Bug fixes to the HTML boilerplate in `references/html-engineering-guide.md`

## Not accepted

- Animations that require external libraries or CDN fonts
- Platform styles that contradict platform content policies
- Examples containing invented financial data

## Process

1. Fork the repository.
2. Make changes in a branch.
3. Test the HTML output against `evals/test-cases.md`.
4. Submit a pull request with a brief description.

## Code style

- CSS: use CSS custom properties (`var(--accent)`) for all colors. No hardcoded hex in slide content.
- JS: no external dependencies. All logic inline in the HTML file.
- Animations: always pair a CSS keyframe with a JS `trigger(n)` reset so animations replay on slide re-entry.
