# Contributing

UX Interaction Skill accepts contributions that improve design analysis quality, pattern coverage, app references, and local tooling.

## Good contributions

- Better pattern descriptions with clearer app examples.
- New named patterns or anti-patterns grounded in real observed behavior.
- Stronger examples that show normal research-partner communication.
- Updated app reference playbook with current app cases.
- Deterministic scripts that use local inputs.
- New evals that test trigger recognition and output quality.

## Contribution rules

- Keep the skill methodology-focused and grounded in observable design decisions.
- Use plain, practical language in all user-facing content.
- Every new pattern or anti-pattern must have a name, a description, and at least one real app example.
- Avoid invented app features — only reference observable behaviors in real apps.
- Avoid dark patterns in the skill's own communication and instructions.
- Avoid scripts that read secrets, make hidden network calls, or have side effects beyond local output.

## Suggested PR checklist

- [ ] `python scripts/validate_skill.py .` passes.
- [ ] New files are referenced from README or SKILL.md when useful.
- [ ] New patterns or anti-patterns include a real app example.
- [ ] New examples include a failure condition or main risk.
- [ ] No API keys, secrets, or private data.
