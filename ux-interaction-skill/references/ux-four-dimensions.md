# UX Four Dimensions — Deep Reference

Detailed checks, scoring guidance, and app examples for each of the four Google UX dimensions.

---

## Useful — Does this solve the real problem?

**Core question**: Is every element on this screen helping users make a better decision or complete their goal, or is it displaying data for the platform's benefit?

### Scoring guide

| Score | Condition |
|---|---|
| 5/5 | Every element directly supports the user's goal. Removing anything would reduce utility. |
| 4/5 | Core function effective; 1-2 supporting elements miss the mark. |
| 3/5 | Feature exists but requires effort to extract value from. |
| 2/5 | Major decisions appear based on assumptions, not behavior data. Content heavier than action. |
| 1/5 | Screen serves the platform, not the user. |

### Checks

- What is the user's goal on this screen? Is the primary action achieving that goal, or a different goal?
- Does data display help users decide, or just inform? Can the user answer "so what should I do?" after reading the screen?
- Would removing 30% of the content make the screen more useful?
- Is this designed around actual user behavior data? (Or: what data would a team need to justify every element on this screen?)
- Does each metric displayed connect to a user-meaningful outcome, or just a platform metric?

### App references

- **Robinhood**: Discovered 97% of users never looked at candlestick charts. Made line chart the default. Candlestick available but not default. Behavior data overruled power-user feedback.
- **Betterment**: Portfolio performance always shown relative to the user's stated goal. A user saving for retirement sees progress toward retirement, not just a percentage number.
- **Monzo**: Weekly spending summary shows category comparisons ("vs. last month") — answers the question "am I spending differently?" not just "how much did I spend?"
- **且慢**: Portfolio diagnosis shows what's wrong with your current holdings (e.g., 80% overlap in underlying stocks), not just what products to add.

### Anti-patterns in this dimension

- Data dashboard with all available metrics, no hierarchy or interpretation
- Feature added because competitor has it, not because users need it
- Empty state filled with promoted products rather than feature explanation

---

## Usable — Can users complete the task?

**Core question**: Can a first-time user complete the primary task in 3 steps or fewer, without help?

### Scoring guide

| Score | Condition |
|---|---|
| 5/5 | Path clear, labels self-explanatory, errors give recovery steps. Task completable in 3 steps. |
| 4/5 | Path mostly clear; one concept or label requires inference. |
| 3/5 | Some friction; users may try twice or look for help. |
| 2/5 | Significant confusion expected; terminology or flow requires prior knowledge. |
| 1/5 | Most users will fail or abandon on first attempt. |

### Checks

- Can the primary task be completed in 3 steps or fewer?
- Are any professional terms or platform-specific concepts left unexplained?
- Do error messages tell users how to fix the problem — not just that something failed?
- Is there an inline explanation for every non-obvious concept? (Not a popup, not a doc link, not a tooltip that disappears)
- Does the search bar do one thing? Or is it doubling as a content feed or ticker?
- Are navigation controls (arrows, back buttons, close) clearly visible and correctly sized for touch?

### App references

- **Robinhood Dollar-First Input**: Ask "how many dollars?" not "how many shares?" Reduces mental conversion work. Error rate ↓42%, first trade conversion ↑37%.
- **Robinhood Inline Education Card**: One sentence explanation, collapsible, appears once per concept. Never a popup. Never a link to docs.
- **Revolut KYC**: Split into micro-steps. Each step has microcopy explaining why the information is needed. Total time: 10–15 minutes.
- **Rudy**: Shows read-only dashboard before requiring registration. User experiences value before cost.
- **Trade Republic**: 3-step transaction (select → amount → swipe). Nothing added to the flow.
- **Cash App**: 2-step transfer. Single large button. Nothing else on the action screen.

### Anti-patterns in this dimension

- Search bar doubling as a news ticker or hot topic display
- Error message: "Operation failed" with no recovery path
- Professional terms (margin, gas fee, basis points) unexplained
- Tooltip more than 25 characters on mobile
- Onboarding ending with a "Done" button that returns to an empty list

---

## Equitable — Does it work for everyone?

**Core question**: Does this design protect users who don't have financial expertise, and avoid dark patterns that exploit psychological vulnerabilities?

### Scoring guide

| Score | Condition |
|---|---|
| 5/5 | Adaptive to user level; risk info complete and balanced; no dark patterns. |
| 4/5 | Mostly balanced; one user segment underserved or one risk disclosure incomplete. |
| 3/5 | Clear bias toward one user type; some users feel confused or excluded. |
| 2/5 | Significant information asymmetry; experienced users served, newcomers at risk. |
| 1/5 | Active dark pattern: FOMO manipulation, missing risk disclosure, high-risk upsell in empty states. |

### Checks

- Are benefits and risks presented with equal visual weight? (Same font size, same color prominence, same information depth)
- Is there a path for users who don't understand the concept? (Not a hidden FAQ link — an in-flow path)
- Does an empty state push users toward high-risk products? (Dark pattern if yes)
- Do percentage gains display without equivalent loss scenarios?
- Is the platform accessible? (Screen reader support, contrast ratio, text size)
- Are tier-based features completely hidden from lower-tier users, or shown with unlock conditions?

### App references

- **Nubank NuDS**: Every design system component supports screen reader, variable font, high contrast by default. Accessibility is a requirement of the component library, not an audit add-on.
- **Nemo**: Onboarding asks about user preferences. Automatically enables accessibility modes. Features unlock progressively as confidence builds.
- **Coinbase**: Two-tier homepage. New users see "Learn & Earn." Experienced users see portfolio. Differentiation is behavioral, not a manual setting.
- **Coinbase Understand Before Buy**: Educational content (60-second video per asset) must complete before the buy button unlocks.
- **且慢**: All tier benefits visible to all users. Lower tiers see a lock icon with "unlock at Silver tier." No benefits hidden.
- **Betterment**: During market stress, primary metric display automatically reduces visual weight. Contextual calming copy appears.

### Dark patterns to flag (mark as P0)

- New coin section showing +4,000% gains without risk disclosure
- Empty contract position filled with AI-recommended leveraged products
- "You've been selected" framing for fee promotions
- Urgency indicators without genuine scarcity ("offer ends soon" with no actual deadline)
- Benefits presented without the associated costs or risks

---

## Enjoyable — Does it feel good to use?

**Core question**: At the key moments — completion, error, waiting, achievement — does the user feel supported and understood?

### Scoring guide

| Score | Condition |
|---|---|
| 5/5 | Key moments have emotional feedback; copy has warmth; information density feels breathable. Squint test passes. |
| 4/5 | Most moments land well; 1-2 feel flat or mechanical. |
| 3/5 | Functional but cold; no delight moments; copy reads like system output. |
| 2/5 | Cluttered or anxiety-inducing; competing elements create visual noise; squint test fails. |
| 1/5 | The experience makes users feel worse about themselves or their situation. |

### Checks

**Squint test**: Blur eyes until you can't read text. Can you identify: (1) the single dominant element, (2) the secondary content, (3) the background? If everything looks the same weight, the test fails.

**Information density**: Count the number of visually distinct content blocks visible without scrolling. More than 4 competing blocks = density problem.

**Copy register**: Does error copy sound like a person ("Oops, that didn't work") or a system ("Error: request failed")? Does success copy acknowledge the user's action ("Your transfer is on its way") or just confirm the system state ("Transaction completed")?

**Completion feedback**: Is there any visual signal when the primary action completes? Even a checkmark animation and one line of confirmation text counts.

### Three levels of delight

1. **Functional layer**: Task completed without error (covered by Usable)
2. **Feedback layer**: Key moments have emotional signals (animation, copy, haptic)
3. **Narrative layer**: The product helps users tell a story about themselves ("I'm saving for Barcelona")

### App references

- **Monzo Magic Moments**: Early paycheck → confetti. Card freeze → freeze animation. Large payment → confirmation screen that feels more serious than usual screens.
- **Monzo Savings Pot**: User names the goal and adds a cover photo. Turns "savings account" into "Barcelona trip fund."
- **Wealthsimple**: First screen is one large number and two buttons. Nothing else. Squint test: passes immediately.
- **Wealthsimple Drag Transfer**: Moving money between accounts uses a drag gesture. Physical metaphor reinforces what's happening.
- **Cash App**: High-saturation single accent color. Large single button. Fast, confident feeling.
- **Acorns**: App named after an acorn. Growth displayed as a growing tree. Abstract portfolio value becomes a living thing.
- **Trade Republic**: Transaction complete: green checkmark + subtle haptic. Brief. Proportionate. Not a celebration for every tap.

### Anti-patterns in this dimension

- First screen with 5+ equal-weight content blocks (squint test fails)
- Silent completion: primary action executes with no feedback
- Error message: technical code only, no human explanation
- Persistent banner that never dismisses (widget hint bar, system notice)
- Icon grid mixing 3+ different visual styles (3D, flat, photographic, brand logo)
