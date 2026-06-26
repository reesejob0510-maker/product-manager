# Anti-Patterns

10 named anti-patterns organized by user impact level. When identifying a problem in a UI, name the anti-pattern. This makes issues concrete and actionable for product teams.

Use in output: "这是 **教育弹窗（Education Popup）** 反模式——用弹窗解释复杂概念会打断用户主流程，用户习惯性关掉弹窗而非阅读。"

---

## High Impact (P0 / P1)

### Anti-Pattern 01: One-Sided Risk Disclosure
**Category**: Equitable  
**Impact**: High — compliance risk, user harm

**What it looks like**: A screen that prominently explains potential gains (1.47x return, +68% probability) but does not equally explain what happens when the user loses. The asymmetry is visual and semantic — green colors, large numbers for upside; no equivalent for downside.

**User damage**: New users make financial decisions with incomplete information. When losses occur, trust is permanently damaged. In many markets, this is a regulatory violation.

**Fix**: Add an equally weighted loss scenario immediately adjacent to the gain scenario. Same visual weight, same font size. "If you're right: $1 → $1.47. If you're wrong: you lose your $1."

---

### Anti-Pattern 02: Empty-State High-Risk Upsell
**Category**: Equitable  
**Impact**: High — dark pattern, user harm

**What it looks like**: A user with no position sees their portfolio or contract page, and the empty state immediately fills with AI-recommended high-risk products (leveraged contracts, volatile new coins) as if these are the natural next step.

**User damage**: New users who haven't made an active investment decision are pushed into high-risk products by the platform's default state. This is a conflict of interest disguised as a feature.

**Fix**: Replace with a neutral empty state (Pattern 12: Neutral Empty State). Explain what the feature does. Offer one clear, low-commitment action. If recommendations are offered, they must be clearly labeled as recommendations with risk disclosures.

---

### Anti-Pattern 03: Post-Onboarding Dead End
**Category**: Usable  
**Impact**: High — direct conversion impact

**What it looks like**: An onboarding or education flow ends with a "Done" or "完成" button that returns the user to an empty list or the home screen with no indication of what to do next.

**User damage**: The user has just invested attention in learning something. Returning them to a neutral state wastes that investment and causes confusion. Most users will not figure out the next step on their own.

**Fix**: The final step of any onboarding or education flow must lead directly to the first actionable step in the product. "Now that you understand prediction markets, here's one to try →" Reference Pattern 03 and Pattern 04.

---

### Anti-Pattern 04: Education Popup
**Category**: Usable  
**Impact**: High — directly lowers comprehension

**What it looks like**: A complex concept (leveraged trading, fee structure, risk level) is explained in a modal popup that appears over the main UI.

**User damage**: Users develop a reflex to dismiss modals without reading them. A popup explanation is functionally invisible to most users. The UI designer thinks they've communicated the information; they have not.

**Fix**: Replace with Pattern 02 (Inline Education Card). The explanation lives in the page, collapsible, no interruption to the flow.

---

### Anti-Pattern 05: First-Screen Overload
**Category**: Enjoyable, Usable  
**Impact**: High — primary navigation failure

**What it looks like**: A home screen with 5+ competing visual elements at the same weight: system notification banner, onboarding progress bar, large CTA card, icon grid, market tickers, widget hint bar, news bar — all visible without scrolling.

**User damage**: The squint test fails completely. Users cannot identify the primary content. Eye-tracking would show chaotic scanning. Task completion rates drop because the primary path is visually buried.

**Fix**: Apply the squint test. Exactly one element should dominate at each visual tier. Remove or move below-the-fold anything that isn't the primary action or primary content. Reference Cash App and Wealthsimple's first-screen philosophy.

---

## Medium Impact (P1 / P2)

### Anti-Pattern 06: Error Without Recovery
**Category**: Usable  
**Impact**: Medium — task abandonment

**What it looks like**: Error messages that state what went wrong ("Operation failed", "错误 403") without telling the user what to do next.

**User damage**: Users can't distinguish between a user error (fixable) and a system error (wait and retry). Without a clear next step, most users abandon.

**Fix**: Every error message must answer three questions: What happened? Why? What do I do now? Example: "Payment failed — your card limit was exceeded. Try a smaller amount or use a different card."

---

### Anti-Pattern 07: Dense Tooltip
**Category**: Usable  
**Impact**: Medium — comprehension failure on mobile

**What it looks like**: A tooltip, popover, or inline explanation that contains 40+ characters on a mobile screen. May include multiple sentences, parenthetical asides, or conditional clauses.

**User damage**: On mobile, a tooltip is a "glance" interaction. Users read the first few words and make a decision. Text beyond 25 characters is largely invisible.

**Fix**: Compress to 25 characters maximum. Add one concrete number example. "1 USD → 1.47 USD if correct." Reference Pattern 02.

---

### Anti-Pattern 08: Invisible Tier Benefits
**Category**: Equitable  
**Impact**: Medium — lost upgrade motivation

**What it looks like**: Premium or higher-tier features are completely hidden from lower-tier users. They don't know what they're missing and therefore have no reason to upgrade.

**User damage**: Users who would upgrade if they knew what was available never do, because the platform gave them no signal that something better exists.

**Fix**: Pattern 10 (Visible Upgrade Path): show all tiers' benefits, lock unavailable ones with a visible "unlock" condition.

---

### Anti-Pattern 09: Silent Success
**Category**: Enjoyable  
**Impact**: Medium — trust and confidence

**What it looks like**: A key user action (transaction, deposit, form submission) completes with no feedback — no animation, no confirmation message, no visual state change.

**User damage**: Users don't know if the action worked. They tap again (creating duplicate submissions) or feel anxious about what happened.

**Fix**: Pattern 05 (Magic Moments): lightweight visual feedback at every completion point. Does not need to be elaborate — even a simple checkmark animation and one line of confirmation text is enough.

---

### Anti-Pattern 10: Inconsistent Icon Grammar
**Category**: Enjoyable  
**Impact**: Medium — visual noise, brand trust

**What it looks like**: A feature grid or navigation bar mixing icons from multiple visual styles: 3D rendered icons next to flat line icons next to photographic images next to brand logos.

**User damage**: The visual inconsistency is read as lack of craft and attention to detail. It signals "this product was built by multiple teams with no coordination." Users lose confidence in the product's reliability, even if it works perfectly.

**Fix**: Establish one icon style for the grid. All icons should come from the same visual system — same line weight, same perspective, same color treatment. Photographic images and brand logos belong in content feeds, not icon grids.
