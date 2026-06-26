# Pattern Library

12 named, reusable design patterns extracted from top-tier fintech apps. Each pattern is named, sourced, scoped to a scenario, and includes implementation notes.

When recommending a fix, cite the pattern by name: "参考 Robinhood 的 **Dollar-First Input** 模式".

---

## Pattern 01: Dollar-First Input
**Source**: Robinhood  
**Dimension**: Usable  
**Scenario**: Any screen where users need to input a quantity in an unfamiliar unit (crypto amount, shares, tokens)

**What it does**: Ask for the familiar unit (fiat currency) as the primary input. Display the equivalent amount in the target unit in real time alongside.

**Why it works**: Users think in dollars, not in 0.00092 BTC. Asking for an unfamiliar unit requires mental conversion and causes errors. Shifting the input to dollars removes that conversion burden entirely.

**Measured impact**: Order error rate ↓42%, first-time trade conversion rate ↑37%

**Implementation**: Primary input field labeled in fiat currency. Below or beside: real-time conversion display in smaller text. "Max" button in fiat, not in asset units.

**Do not**: Ask for the asset unit as primary input. Do not make users calculate manually.

---

## Pattern 02: Inline Education Card
**Source**: Robinhood  
**Dimension**: Usable  
**Scenario**: First time a user encounters a professional term, concept, or unfamiliar data point

**What it does**: Displays a one-sentence plain-language explanation directly in the page, collapsible, appearing once per concept per user.

**Why it works**: Popups are dismissed without reading. Separate documentation pages are never visited. Inline cards interrupt nothing and persist as long as needed.

**Implementation**: Collapsed by default (one line visible). Expandable via tap. Once the user expands and reads, never shown again for that concept. Maximum 25 characters in collapsed state, maximum 60 characters when expanded. No jargon.

**Do not**: Use a modal popup. Link to an external FAQ. Show the same card repeatedly after the user has seen it.

---

## Pattern 03: Progressive Step Disclosure
**Source**: Revolut, Polymarket  
**Dimension**: Usable  
**Scenario**: Onboarding flows, multi-concept education sequences, KYC processes

**What it does**: Breaks a multi-step flow into one concept per screen with a clear position indicator (2/3) and an explicit completion signal on the final step.

**Why it works**: Cognitive load is reduced when only one thing needs to be understood at a time. Position indicators reduce anxiety about length. Explicit completion signals ("Done" button) signal the end clearly.

**Implementation**: One concept per screen. Position indicator (e.g., "2 / 3"). Navigation arrows for forward/back. On the final step: a named completion button ("完成" or "Done"), not just a forward arrow. Always include a skip option for experienced users.

**Do not**: Explain multiple concepts on one screen. End the last step with only a ">" arrow. Show all steps simultaneously.

---

## Pattern 04: Experience-Before-Commitment
**Source**: Rudy  
**Dimension**: Usable, Equitable  
**Scenario**: Products that require registration or identity verification before use

**What it does**: Allows users to explore core read-only functionality before requiring them to complete the registration or KYC step.

**Why it works**: Users are being asked to pay a cost (filling forms, uploading documents) before they understand the value. Letting them see the value first makes the cost feel worthwhile.

**Implementation**: "Browse as guest" or read-only dashboard mode. KYC prompt appears only after the user has engaged with core content. The prompt references what they've seen: "Start trading [asset they viewed]."

**Do not**: Gate all content behind registration. Show KYC prompts before users have experienced any value.

---

## Pattern 05: Magic Moments
**Source**: Monzo  
**Dimension**: Enjoyable  
**Scenario**: Key completion points — transaction successful, goal reached, reward received, first deposit

**What it does**: At the moment of task completion, adds a lightweight emotional signal: micro-animation, haptic feedback, or contextually relevant visual metaphor.

**Why it works**: Silent completions leave users uncertain ("did that work?") and emotionally flat. A single moment of delight at the right time builds strong emotional memory of the product.

**Implementation**: Keep it brief (0.3–0.8 seconds). Make it contextually relevant (confetti for a savings goal reached, not for every tap). No autoplay sound. Never block the user's next action.

**Do not**: Show no feedback at all on task completion. Play celebration animations for routine actions. Block the UI with a fullscreen animation.

---

## Pattern 06: Good Friction
**Source**: Monzo  
**Dimension**: Equitable, Enjoyable  
**Scenario**: Irreversible actions, large financial transactions, sensitive permission grants

**What it does**: Adds one deliberate confirmation step — typically a drag gesture or an extra screen — that requires the user to actively choose to proceed, not just accidentally tap.

**Why it works**: Accidental execution of high-stakes actions damages trust permanently. A single extra step protects users at critical moments and makes them feel the platform is looking out for them.

**Implementation**: Swipe-to-confirm gesture (right swipe to execute) rather than a tap. Or: a dedicated confirmation screen stating the exact amount, destination, and consequence. The confirmation screen should feel more serious than the previous screens.

**Do not**: Add friction to low-stakes, reversible actions (this becomes bad friction). Apply the same confirmation pattern to everything — it loses its signal value.

---

## Pattern 07: Goal Contextualization
**Source**: Betterment  
**Dimension**: Useful  
**Scenario**: Any screen displaying financial data, performance, or progress metrics

**What it does**: Never shows data in isolation. Every metric is displayed in the context of the user's personal goal: "You are 67% of the way to your down payment goal" instead of "Account balance: $34,200."

**Why it works**: Raw numbers require users to do their own interpretation. Contextualized numbers answer the question the user actually cares about: "Am I on track?"

**Implementation**: Every data display element is anchored to one user goal. Goal is shown prominently. Progress is expressed as a percentage of that goal. Historical data is shown relative to where the goal needed the portfolio to be.

**Do not**: Show data dashboards without any connection to the user's stated goals. Show performance percentages without explaining what they mean for the user.

---

## Pattern 08: Sunk Cost Surfacing
**Source**: 且慢  
**Dimension**: Useful, Enjoyable  
**Scenario**: Retention screens, user profile, account summary

**What it does**: Makes the user's accumulated investment on the platform visible: days active, number of benefits enjoyed, historical earnings, milestones reached.

**Why it works**: Users underestimate their own investment in a platform. Making it visible increases the perceived cost of leaving and builds a sense of belonging.

**Implementation**: "You've been investing for 847 days." "You've used 4 of your 6 premium benefits." Surface these numbers in a low-pressure way — status information, not promotional copy.

**Do not**: Fabricate or inflate numbers. Make it feel like manipulation ("You'll lose everything if you leave!"). Show sunk cost as the primary retention mechanism without genuine product value underneath.

---

## Pattern 09: Progressive Feature Unlock
**Source**: Nemo, Coinbase  
**Dimension**: Equitable  
**Scenario**: Products with many features that vary in complexity or risk

**What it does**: Starts users with a limited, simplified feature set and unlocks additional features as the user demonstrates confidence or meets criteria (time on platform, completed actions, verified identity).

**Why it works**: Showing all features at once causes cognitive overload and makes the product feel overwhelming for new users. Gradual unlock lets users build confidence at each stage before encountering the next level of complexity.

**Implementation**: Clear "what you unlock next" messaging. Progress visible to user. Unlock triggers based on verifiable behavior (completed first trade, passed KYC, reached X days). New features are announced when unlocked, not silently added.

**Do not**: Hide features with no explanation. Unlock features arbitrarily. Use unlock gates as a dark pattern to push users toward high-risk features.

---

## Pattern 10: Visible Upgrade Path
**Source**: 且慢  
**Dimension**: Equitable  
**Scenario**: Tiered products where some users have fewer features or benefits than others

**What it does**: Shows all tiers' benefits to all users, but locks unavailable ones with a clear unlock condition instead of hiding them entirely.

**Why it works**: Hidden benefits create no aspiration. Locked-but-visible benefits create motivation to upgrade. Users can see what they're working toward and understand how to get there.

**Implementation**: Feature list shows all tiers. Locked items are visible but clearly marked as locked. Unlock condition is stated inline ("Reach Silver tier to unlock this"). No guessing required.

**Do not**: Completely hide features from lower-tier users. Obscure unlock conditions. Show locked features without telling users how to unlock them.

---

## Pattern 11: Two-Step Minimalism
**Source**: Cash App, Trade Republic  
**Dimension**: Usable, Enjoyable  
**Scenario**: Core transactional flows (transfer, buy, sell, pay)

**What it does**: Reduces the core transactional flow to the absolute minimum: two to three steps, large tap targets, single focused decision per screen.

**Why it works**: Every additional step in a financial flow adds abandonment risk. The fewer the steps, the higher the completion rate.

**Implementation**: Step 1: enter amount (nothing else on screen). Step 2: confirm (summary of what will happen, confirm gesture). Done. No optional fields, no cross-sell, no educational popups inside the flow.

**Do not**: Add cross-sell or promotional content inside a transaction flow. Ask for information not required to complete the transaction. Show complex fee breakdowns mid-flow.

---

## Pattern 12: Neutral Empty State
**Source**: Freetrade, Wealthsimple  
**Dimension**: Equitable  
**Scenario**: First-time users viewing a portfolio, watchlist, or feature with no data

**What it does**: Shows a useful, non-pushy empty state that gives the user a starting point without pushing them toward any specific action — especially high-risk actions.

**Why it works**: Empty states that immediately push high-risk products (leveraged trading, new coins) are dark patterns. Neutral states that show popular choices or explain the feature give users agency.

**Implementation**: Show what others find popular (without forcing it). Explain what the feature does in 1-2 sentences. Provide a single clear action if one is appropriate. Never fill an empty portfolio with AI-recommended leveraged products.

**Do not**: Fill an empty state with promoted high-risk products. Show an empty list with no explanation. Use the empty state as a marketing opportunity.
