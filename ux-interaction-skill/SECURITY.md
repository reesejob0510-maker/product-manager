# Security policy

This skill is designed to be safe to audit and easy to run locally.

## Security design

- Bundled scripts use Python standard library only.
- Bundled scripts run locally with user-provided JSON inputs.
- Bundled scripts have no network access, credential reading, or side effects beyond stdout output.
- The skill instructs agents to use design analysis and publicly observable app behaviors only.
- The skill does not instruct agents to access user accounts, perform purchases, or read private data.

## Reporting issues

Open an issue with:

1. File path.
2. Risk description.
3. Reproduction steps.
4. Suggested fix.

## Threat model

Agent Skills can contain executable code and instructions. Users should review all files before installing any third-party skill, especially skills that request shell access, credentials, or browser access.

This skill requires no special permissions. The local scripts (`scripts/ux_scorecard.py`, `scripts/validate_skill.py`) only read files you provide and write to stdout.
