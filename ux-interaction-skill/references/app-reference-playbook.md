# App Reference Playbook

When recommending improvements, cite a named app and specific practice. This file is the authoritative source for app-pattern citations. Do not cite apps for practices not listed here.

---

## By Dimension

### Useful — Apps that best answer "does this solve the real problem?"

**Robinhood**
- Default to line chart over candlestick (97% of users don't use candlestick — behavior data overrules power user feedback)
- Inline single-sentence stock descriptions on first view

**Betterment**
- Every data point anchored to a user's personal financial goal
- Market downturns trigger contextual copy ("This is normal; your long-term goal is unchanged") rather than more data

**Monzo**
- Weekly spending digest: "You spent X on coffee this week vs. last month" (not just a bank statement)
- Proactive savings nudges based on observed spending patterns

**且慢**
- Portfolio "diagnosis" (what's wrong with what you have) instead of product recommendation
- Sunk cost surface: days on platform, benefits used — visible to the user

**Acorns**
- Removes the "what to invest in" decision from the user entirely
- Round-up mechanism: micro-investing through existing spending behavior

---

### Usable — Apps that best answer "can users complete the task?"

**Robinhood**
- Dollar-first input: enter dollar amount, see equivalent shares/coins in real time
- Inline education card: one sentence, collapsible, once per concept per user
- Error recovery: every error includes a "try this instead" path

**Revolut**
- KYC broken into micro-steps with microcopy explaining why each piece of info is needed
- Full onboarding in 10–15 minutes vs. 3–4 weeks for traditional banks

**Rudy** (German crypto app)
- Read-only dashboard before KYC requirement — users explore before committing
- Registration required only when user wants to act, not when they want to look

**Trade Republic**
- Core transaction flow: 3 steps (tap asset → enter amount → swipe to confirm)
- Swipe-to-confirm gesture prevents accidental execution

**Cash App**
- 2-step transfer: amount → confirm
- Single large send button, nothing else on the action screen

**Freetrade**
- Dollar-amount entry (not shares) for buying stocks
- Fractional shares — removes "I can't afford one share of Apple" barrier

---

### Equitable — Apps that best answer "does it work for everyone?"

**Nubank**
- Design system (NuDS): every component supports screen reader, variable font size, high contrast by default
- Accessibility is a first-class requirement, not a post-launch audit

**Nemo** (learning disability-focused app)
- Registration asks about user preferences (ATM usage, reading challenges)
- Auto-enables accessibility modes based on answers
- Features unlock progressively as user confidence builds

**Coinbase**
- Tiered homepage: new user sees "Learn & Earn"; experienced user sees portfolio and market data
- "Understand before you buy" — educational video must complete before purchase unlocks

**且慢**
- All tier benefits visible to all users; lower tiers see lock icon + unlock condition
- No benefits hidden without explanation

**Betterment**
- Market downturns: primary metric display shrinks and dims automatically; contextual message appears
- Platform actively reduces emotional reactivity in high-stress moments

---

### Enjoyable — Apps that best answer "does it feel good to use?"

**Monzo**
- Early salary arrival: confetti animation
- Card freeze: "freezing" animation
- "Early paycheck" uses drag gesture instead of button — tactile, memorable
- Savings Pot: user names the goal ("Barcelona trip") and adds a photo
- Error copy: "Oops, that didn't work" not "Error 403"
- Good friction: large payment confirmation screen with deliberate design

**Wealthsimple**
- First screen: one large number (portfolio value) + two buttons — nothing else
- Asset transfer uses drag gesture between accounts
- Downturns trigger empathetic copy: "Markets dip. Your goal hasn't changed."

**Cash App**
- High-saturation accent color, large send button — feels fast and confident
- Gen Z copy register — conversational, not financial-institution stiff

**Trade Republic**
- Transaction complete: green checkmark + subtle haptic — brief, appropriate
- No celebration for routine actions; delight is reserved for earned moments

**Acorns**
- Visual metaphor: the app is named after an acorn; growth is shown as a growing tree
- Turns abstract portfolio value into a living visual over time

---

## By Scenario

### New user onboarding

| Pattern | App | Key Detail |
|---|---|---|
| Experience before commitment | Rudy | Read-only mode before registration |
| Progressive step disclosure | Revolut | Micro-steps with context for each |
| Education before purchase | Coinbase | 60-second video unlocks buy button |
| Minimal required questions | Acorns | 2 questions → automatic portfolio |

### Financial data display

| Pattern | App | Key Detail |
|---|---|---|
| Goal contextualization | Betterment | Data always relative to user's stated goal |
| Sunk cost surfacing | 且慢 | Days active, benefits used, made visible |
| Downside-aware defaults | Wealthsimple | Metric shrinks during market downturns |
| Simple default, expert option | Robinhood | Line chart default, candlestick available |

### Transaction flow

| Pattern | App | Key Detail |
|---|---|---|
| Dollar-first input | Robinhood | Fiat as primary, asset as secondary display |
| 2-step minimalism | Cash App | Amount → confirm, nothing else |
| Swipe-to-confirm | Trade Republic | Tactile confirmation prevents accidental taps |
| Good friction | Monzo | Extra confirmation screen for large/irreversible payments |

### Empty states

| Pattern | App | Key Detail |
|---|---|---|
| Neutral empty state | Freetrade | Shows popular choices without pushing them |
| Goal-driven empty state | Betterment | "Set your first goal to get started" |
| Feature explanation | Wealthsimple | Explains what the feature does before asking to use it |

### Risk communication

| Pattern | App | Key Detail |
|---|---|---|
| Equal weight risk display | Betterment | Upside and downside shown with equal visual weight |
| Active downgrade | Wealthsimple | Platform reduces emotional reactivity during market stress |
| Proactive education | Coinbase | Understand-before-buy flow for every asset |
