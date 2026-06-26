# Risk and Compliance

Design boundaries for high-risk product categories. Use this file when the UI being analyzed involves financial products, health decisions, or users who may be vulnerable.

---

## Financial Product Design — Hard Rules

### Risk disclosure

**Rule**: Any screen displaying potential gains must display equivalent potential losses with equal visual weight.

- Same font size for gain and loss scenarios
- Same color treatment (not green for gains, grey for losses)
- Loss scenario must be specific: "If prediction is wrong: you lose your stake"
- This is both a UX principle and a regulatory requirement in most markets

**Flag as P0** when:
- A percentage gain is displayed without a loss scenario
- New coins or high-volatility assets display only upside performance
- Leveraged product promotion omits leverage risk

---

### Empty state upselling

**Rule**: Empty states in financial products must not push users toward high-risk actions.

An empty portfolio, empty watchlist, or empty position page is a moment of low engagement and potentially high risk. Users in this state may be:
- New and inexperienced
- Returning after a loss
- Exploring before committing

**Flag as P0** when:
- An empty contract/leveraged trading page shows AI-recommended trades
- An empty portfolio shows trending high-volatility assets as default content
- A "no position" state uses urgency language ("Don't miss this opportunity")

**Acceptable empty states**:
- Feature explanation (what does this feature do?)
- Neutral popular options (what do others find useful? — with risk disclosure)
- Clear, low-commitment first step

---

### FOMO and urgency manipulation

**Rule**: Urgency signals must be real. Scarcity must be genuine.

**Flag as P0** when:
- "Limited time" offers have no actual deadline
- "X people are viewing this" is displayed without real data
- High-percentage gains are shown without context (time period, volatility, survivorship bias)
- Countdown timers are present without a real consequence at expiry

---

## Dark Pattern Definitions

These specific design choices are categorized as dark patterns and must be flagged explicitly in output:

| Dark Pattern | Description | Flag Level |
|---|---|---|
| One-sided disclosure | Gains shown, losses not shown with equal weight | P0 |
| Empty state upsell | High-risk product recommended in empty state | P0 |
| Hidden tier benefits | Features hidden from lower tiers with no explanation | P1 |
| False urgency | Countdown timer / scarcity claim without real basis | P0 |
| Buried opt-out | Opt-out buried in settings 3+ levels deep while opt-in is default | P1 |
| Confirm-shaming | Decline button labeled as a negative self-description ("No, I don't want to save money") | P1 |
| Roach motel | Easy to sign up / invest, very difficult to withdraw / cancel | P0 |

---

## Platform-Specific Notes

### Crypto and prediction markets

- All assets with >50% annual volatility should have inline risk disclosure on the detail page
- "Group wisdom" or "crowd probability" displays (like Polymarket's 68%) must explain what they mean and their limitations
- New token listings with extreme percentage gains (>500%) require prominent risk warnings

### Trading apps (stocks, derivatives)

- Leveraged products (futures, options, margin) must have a mandatory "I understand the risks" step on first access — not just a checkbox, a deliberate action
- Paper trading / demo modes should be clearly labeled and not mixed with real-money flows

### Investment advisory

- AI recommendations must be labeled as such and include a disclaimer
- Portfolio rebalancing recommendations should not be presented as urgent unless there is a genuine reason

---

## Research Boundaries

UX Interaction Skill provides design analysis, pattern recommendations, and UX guidance. It does not:

- Certify that a design meets specific regulatory requirements in a given jurisdiction
- Provide legal advice on financial product disclosure requirements
- Guarantee that a design change will resolve compliance issues

Flag potential compliance concerns clearly, recommend consulting a legal or compliance team for confirmation, and continue with UX recommendations.

Use concise language when needed:
`这个问题可能涉及合规要求，建议与合规团队确认后再做最终决定。`
`This may touch on regulatory requirements. UX recommendation stands; confirm with your compliance team.`
