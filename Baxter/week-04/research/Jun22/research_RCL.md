---
date: 2026-06-22
ticker: RCL
type: PUT
conviction: CONDITIONAL — sizing conflict likely disqualifies under current fund size if earnings history cap applies
verdict: CONDITIONAL WATCH — most interesting batch 2 candidate. Positive EV, achievable required move, good macro alignment. Blocked by: (1) earnings history cap likely applies (cruise recovery = 4+ beats), which combined with current reserve size makes no strike enterable within binder rules; (2) Rule 3 needs verification; (3) Rule 4 needs verification. Full entry path requires earnings history to have fewer than 4 consecutive beats — verify before proceeding.
---

# RCL (Royal Caribbean Cruises) — PUTS RESEARCH
*June 22, 2026. Royal Caribbean at $230. The cruise industry's most profitable operator has rerated from "COVID recovery story" to "luxury travel secular growth thesis." The Baxters found something interesting here, then found the wall.*

---

## THE PLAY AT A GLANCE

| | |
|---|---|
| **Ticker** | RCL |
| **Proposed Option** | $185P Aug21 (put, strike $185, expires Aug 21 2026) |
| **Cost per contract (estimated)** | ~$0.75/share — **NEEDS LIVE CHAIN VERIFICATION** |
| **At risk** | ~$75 (1 contract estimated) |
| **Breakeven** | ~$184.25 (requires -19.9% from $230) |
| **Catalyst date** | Q2 2026 earnings est. ~July 25 (27 days before Aug 21 expiry) |
| **Conviction** | **CONDITIONAL** — see sizing conflict analysis below |
| **Verdict** | **CONDITIONAL WATCH** — the play passes on many dimensions but is blocked by a structural sizing conflict if RCL has beaten estimates 4+ consecutive quarters (very likely given cruise recovery trajectory). Under that scenario, max conviction is 3.5/5, but 3.5/5 sizing cap ($61) is below the minimum contract cost ($75). Entry is not possible within binder rules. If earnings history is less than 4 consecutive beats, 4/5 conviction is available, the $185P fits at $75 within the 4/5 range ($73-$98), and this becomes a WATCH. |

---

## SIZING CONFLICT — THE STRUCTURAL ISSUE

*This is the most important section. Read before the rules check.*

**Binder sizing table (from binder.md):**
- 3.5/5 conviction: 6-10% of reserve = $37-$61 at current $614 reserve
- 4/5 conviction: 12-16% of reserve = $74-$98 at current $614 reserve
- 5/5 conviction: 17-20% of reserve = $104-$123 at current $614 reserve

**5/5 conviction is not available on puts yet** (binder rule: 3 closed puts plays required before 5/5 is accessible; current closed puts = 0).

**Back-test requirement update:** RCL is research play #4 in the back-test process. Even if entered, it contributes to the 3 closed plays required for 5/5 unlock.

**The gap for RCL:**

Cheapest Rule-5-compliant put on RCL at $230 (estimated):
- $185P at ~$0.75 per share = **$75 per contract**
- $190P at ~$1.07 per share = **$107 per contract**

At 3.5/5 conviction (max if earnings history cap applies):
- Sizing cap: $61 maximum
- $75 is ABOVE $61. Entry not permitted within binder rules.

At 4/5 conviction (only available if RCL has fewer than 4 consecutive beat-and-raise quarters):
- Sizing range: $74-$98
- $75 per contract fits. Just barely (bottom of range).

**The critical question:** Has Royal Caribbean beaten EPS estimates four consecutive times?

Almost certainly yes. The cruise industry recovery has exceeded analyst expectations for 6-8 straight quarters. Bookings at record levels, pricing holding above pre-COVID, occupancy 100%+, new ships outperforming. RCL specifically has been a consistent beat-and-raise story.

If 4+ beats → 3.5/5 cap → no strike enterable → **the play is mechanically blocked** regardless of all other factors.

If fewer than 4 beats (unlikely) → 4/5 possible → $185P at $75 fits within $74-$98 range → WATCH.

**Conclusion of sizing analysis:** This is almost certainly a PASS on sizing grounds alone, unless the earnings history data shows fewer than 4 consecutive beats. Verify before writing this into the entry queue.

---

## THE RULES CHECK

| Rule | Requirement | RCL Status |
|------|-------------|------------|
| Rule 1 | Top 20-25% of 52-week range, no fresh 52wk high in 5 days | **LIKELY PASS** — cruise sector has had an extended rally; RCL near all-time highs |
| Rule 2 | Earnings before Aug 21, min 21 DTE at entry | **PASS** — est. July 25 earnings; 27 days to Aug 21 |
| Rule 3 | Min 2 Sell/Underperform ratings | **UNVERIFIED** — at ATH, some bears may have upgraded |
| Rule 4 | Highest Sell target below put breakeven ($184.25) | **UNVERIFIED** — if remaining bears have targets at $170-180, Rule 4 passes |
| Rule 5 | Put ask ≤ $1.50/share | **EST. PASS** — $185P est. at ~$0.75; $190P at ~$1.07 (needs live chain) |

**ADDITIONAL CONSTRAINT — Earnings history cap:**  
If RCL has beaten EPS estimates for 4+ consecutive quarters → maximum conviction 3.5/5 → sizing cap $61 → no enterable strike exists at current reserve level. Near-certain to apply given cruise recovery trajectory. **This constraint is the primary blocker.**

---

## THE CHAIN (CORRECTED)

*Note: The batch 2 screening log incorrectly estimated $165P at $0.90. That strike at RCL's ~35% IV costs approximately $0.09 — effectively worthless. The correct Rule-5-compliant strikes are $185P and $190P.*

*Theoretical estimates. Must be verified via `python scripts/fetch_puts_chain.py RCL` before any order.*

Estimated using Black-Scholes: RCL IV ~35% (consumer discretionary leisure stock, lower IV than tech), 59 days to Aug 21.

| Strike | Ask (est.) | At Risk | Break-even | Needs | Rule 5 | Fits 3.5/5 sizing? | Fits 4/5 sizing? |
|--------|-----------|---------|------------|-------|--------|---------------------|------------------|
| $200P | ~$2.10 | $210 | $197.90 | -13.9% | FAILS | No | No |
| $195P | ~$1.66 | $166 | $193.34 | -16.0% | FAILS | No | No |
| $190P | ~$1.07 | $107 | $188.93 | -17.9% | PASS | No | No ($107 > $98) |
| $185P | ~$0.75 | $75 | $184.25 | -19.9% | PASS | No ($75 > $61) | YES ($74-$98) |
| $180P | ~$0.38 | $38 | $179.62 | -21.9% | PASS | YES ($38 in range) | YES |
| $170P | ~$0.09 | $9 | $169.91 | -26.1% | PASS | YES | YES |

**The $180P at $0.38 technically fits 3.5/5 sizing.** But: breakeven $179.62 requires -21.9% decline. Does Rule 4 pass? The highest Sell target must be below $179.62. If bears have $170-180 targets, Rule 4 passes for $180P. If targets are $185+, Rule 4 fails.

The $180P also generates less payoff: if stock goes to $165, gain is $180 - $165 - $0.38 = $14.62/sh = $1,462 - $38 = $1,424. But EV at 10% probability: 0.10 × $1,424 - 0.90 × $38 = $142 - $34 = +$108. Still positive!

**Revised play if earnings cap applies:** $180P at $0.38 (fits 3.5/5, requires -21.9%, positive EV at 10%).

However: if earnings cap applies (3.5/5 max) AND conviction floor for puts is anything above 3/5 (which the binder implies through its structure), this still may be borderline. A $38 put on a company this large, requiring a 22% decline, is essentially a lottery ticket with marginal probability.

---

## BULLXTER'S TAKE

**The bear thesis:**

Royal Caribbean at $230 represents an 8-10x recovery from COVID lows and a 60% premium to pre-COVID highs (RCL was at ~$135 pre-COVID). The market is no longer pricing "recovery to prior highs" — it's pricing "structural premium to prior highs" because:
1. Fleet is newer and larger
2. Pricing power demonstrated above 2019 levels
3. North America consumer still willing to pay for experiential travel

The specific Q2 2026 disappointment scenario: **net yield per passenger cruise day** comes in flat or +1% YoY (vs. consensus +4-5%). This means RCL's pricing power is showing first signs of exhaustion. Management guides net yield for 2H 2026 at flat or +1% (vs. consensus +3-4%).

What causes this: (1) Alaska season capacity (RCL runs significant Alaska sailings in Q2) coming in at normalized volumes after post-COVID pent-up demand washed through; (2) Caribbean yield starting to reflect new-build capacity coming online from competitors (Celebrity, NCL, NCLH); (3) International sailings potentially seeing AUD/EUR weakness hurting reported dollar yields.

At 18x forward EV/EBITDA, a "peak yield" signal would reprice RCL to 14x = stock at $175-185.

That's our put territory.

**Why the cruise thesis is specific:**

Cruise analysts live and die on net yield. It's not fuzzy like order growth. Management reports it explicitly. If Q2 net yield comes in below consensus, the stock moves. Bullxter likes this specificity.

Bullxter verdict: Strong specific thesis. Constrained by the sizing conflict. Worth watching if fund size grows.

---

## BEARXTER'S TAKE

**What I'm worried about:**

**The earnings history trap.** RCL has exceeded analyst expectations for at least 4-6 consecutive quarters. Every time, the bear thesis was "you can't sustain 100%+ occupancy and these yields" and every time, they did. The market has learned to believe RCL's management. This creates an asymmetric credibility problem: a miss would surprise dramatically (good for puts) but a miss is structurally LESS likely because management sandbagged guidance and the business is genuinely performing.

**The timing question.** July 25 earnings with August 21 expiry = 27 days post-catalyst. If RCL misses and drops 20-25% on July 25, does it stay down through August 21? Or does "buy the dip" money move into the stock within days? Historical pattern for cruise stocks at ATH: dips get bought quickly because institutional LVMH-era luxury travel believers are real.

**Rule 3 uncertainty.** At $230 near ATH, how many Sell-rated analysts remain? The ones who've had Sell ratings since $150 are either fired or upgraded. We may not have 2 active Sells. If Rule 3 fails, we never get to the sizing conflict.

**Bearxter verdict:** CONDITIONAL WATCH — but the sizing conflict is the real blocker. Even if all rules confirm, the entry math doesn't work under an earnings cap at the current reserve level. Watch this one for when the fund grows.

---

## CALXTER'S TAKE

**Revised expected value model (corrected strikes):**

**Scenario A: $185P at $0.75 (requires 4/5 conviction — earnings history cap must NOT apply)**

| Scenario | Probability | Stock at expiry | Option value | Net P&L |
|----------|-------------|-----------------|--------------|---------|
| Net yield miss + guide-down | 18% | ~$175 | $185 - $175 - $0.75 = $9.25/sh | +$850 |
| In-line, minor beats | 40% | ~$220 | $0 | -$75 |
| Beat + raise (yield expansion continues) | 42% | ~$255 | $0 | -$75 |

**EV:** 0.18 × $850 - 0.82 × $75 = $153 - $61.50 = **+$91.50**

Positive EV at 18% probability of bear scenario.

**Scenario B: $180P at $0.38 (fits 3.5/5 sizing)**

| Scenario | Probability | Stock at expiry | Option value | Net P&L |
|----------|-------------|-----------------|--------------|---------|
| Net yield miss + guide-down | 12% | ~$165 | $180 - $165 - $0.38 = $14.62/sh | +$1,424 |
| In-line or minor beats | 55% | ~$215 | $0 | -$38 |
| Beat + raise | 33% | ~$255 | $0 | -$38 |

**EV:** 0.12 × $1,424 - 0.88 × $38 = $170.88 - $33.44 = **+$137.44**

Also positive EV, and only $38 at risk. But the probability is lower (12%) because the required move is larger (21.9%).

**Calxter's actual conclusion:** The $180P at $0.38 has the most interesting EV structure — 3.8× better risk-adjusted return than the $185P if you trust the 12% probability estimate. But the conviction that underpins that probability estimate should be 4/5 (specific yield disappointment thesis). If we're capped at 3.5/5, the probability estimate should be more conservative. And at conservative probability (8%), $180P EV is 0.08 × $1,424 - 0.92 × $38 = $113.92 - $34.96 = +$78.96. Still positive.

**Kelly-implied position size for $180P:**
- p = 0.12, b = ($1,424/$38) = 37.47
- Kelly = (37.47 × 0.12 - 0.88) / 37.47 = (4.496 - 0.88) / 37.47 = 3.616 / 37.47 = 9.65%
- 9.65% of $614 = $59. That's $59 at risk. $38 per contract → under 2 contracts.
- 1 contract ($38) is below full Kelly implied position. Enter 1 contract.
- 1 contract at $38 within 3.5/5 sizing ($37-$61)? YES — barely fits.

**The $180P at $0.38 is the only strike that fits within 3.5/5 sizing constraints AND has positive EV.** But the required move (21.9%) requires specifically bad news at the yield level.

Calxter's conditional recommendation: If earnings history cap applies (3.5/5 max), enter 1 contract of $180P at $0.38 if Rule 3 and Rule 4 confirm. That's $38 at risk against $1,424 maximum gain. EV positive.

If earnings cap does NOT apply (4/5 available), enter 1 contract of $185P at $0.75 for better risk-adjusted return.

---

## MACXTER'S TAKE

**Macro alignment:**

**Consumer discretionary under pressure:** Warsh holding rates at 3.5-3.75% means cruise financing (many consumers use travel credit cards or BNPL for vacation deposits) is more expensive. Booking velocity for 2027 itineraries could show the first signs of rate-sensitivity. This is precisely the kind of forward-looking guidance item that could pressure the stock on the call.

**Oil prices:** The Iran situation is the critical variable. If crude prices spike on escalation, RCL's fuel cost base increases significantly. A 20% crude price increase would reduce RCL's EBITDA by approximately $200-300M annually. Management might guide this into 2027 capex/cost assumptions. This is a macro tailwind for the bear thesis.

**Reverse scenario — Iran deal/crude decline:** If oil drops 20%, cruise operating costs fall, margins expand, and the stock could re-rate higher. This is the specific macro tail risk against the puts thesis. Macxter files this as meaningful (not dismissible).

**USD strengthening:** If Warsh signals are positive for the dollar, international passengers (particularly European bookings for Caribbean sailings) find RCL more expensive in local currency terms. This could reduce booking velocity from international markets. Minor but directionally bearish.

**Macxter's net assessment:** The macro environment is FAVORABLE for the bear thesis. Consumer spending pressure, oil spike risk, and international yield compression are all pointing toward a potential yield-miss quarter. The Iran wildcard is real but goes both ways (escalation = fuel cost hit to RCL; de-escalation = positive for RCL).

Macxter verdict: FAVORABLE macro alignment. Flag the oil wildcard as a two-sided risk.

---

## THE FIVE-BAXTER MEETING

*Baxter opens the binder to a fresh page labeled "RCL." Five Baxters convene.*

---

**PRIME:** Royal Caribbean at $230. This is the most mechanically interesting puts candidate from batch 2.

Let me do the sizing conflict up front because it determines whether we even need to discuss the other rules.

RCL almost certainly has beaten EPS estimates four consecutive times. The cruise recovery produced consistent outperformance from Q3 2024 through Q2 2026. If that earnings history applies, we're capped at 3.5/5 conviction. At 3.5/5 cap, the only enterable strike is $180P at ~$0.38.

So here's the actual question for this meeting: is the bear thesis specific enough to justify 3.5/5 conviction on a $38 bet with a $1,424 maximum payoff?

**BEARXTER:** Let me state the exact earnings cap mechanism. The binder says: "A company that has beaten and raised EPS estimates for four or more consecutive quarters cannot receive 4/5 conviction regardless of other factors." This is about RAISING guidance, not just beating. If RCL beat estimates but kept guidance flat, the cap might not technically apply.

I'd need to see four consecutive quarters of explicit guidance raises (not just beats) to apply the cap. This is a subtle but important distinction in the rule text.

**PRIME:** That's a good catch. The cap is beat-AND-raise, not just beat. If RCL has been conservative on guidance (which cruise management tends to be), they might beat every quarter without formally raising guidance. That would leave 4/5 conviction available.

**CALXTER:** If 4/5 is available, the correct strike is $185P at $0.75 with EV of +$91.50. If capped at 3.5/5, the correct strike is $180P at $0.38 with EV of +$137.44 (larger percentage but smaller absolute gain). Both structures are positive EV.

**BULLXTER:** I want to make sure we're clear on the bear thesis specificity. Net yield per passenger cruise day. It's not "consumer spending is bad." It's "RCL's specific yield metric shows first signs of exhaustion after 4-6 quarters of expansion." That's specific and measurable. The Q2 call will report this number explicitly.

**MACXTER:** Flag on the oil wildcard. Iran escalation could hurt RCL (fuel costs) but also could hurt RCL differently — if conflict escalates, luxury travel demand from high-net-worth individuals pauses, and that's the core RCL customer. This is actually ambiguously puts-positive: conflict hurts the customer base AND the cost base.

**BEARXTER:** Rule 3 check. At $230 ATH, have bears maintained their Sell ratings? Every quarter they were wrong. The fundamental bear — "cruise valuations are unsustainable" — has been wrong for 6-8 consecutive quarters. Some of those analysts have been upgraded or reassigned. We need to verify 2 active Sells remain.

**PRIME:** Summary and verdict.

RCL has a specific bear thesis (net yield exhaustion), positive macro alignment, and positive EV on two strike structures. The primary unknowns are:
1. Whether the earnings history cap applies (beat-AND-raise required, not just beat)
2. Whether 2+ active Sell ratings remain after the ATH run
3. What current Sell targets are (Rule 4 for each strike)
4. Live chain confirmation of option prices

**Verdict: CONDITIONAL WATCH** — specifically watching for Rule 3 confirmation and earnings history cap clarification. If 4/5 conviction is available (beat-only, no formal guidance raises), enter $185P at $75. If capped at 3.5/5 (4+ beat-and-raise), enter $180P at $38. Both are within binder sizing rules under their respective conviction scenarios.

*Baxter writes "RCL — CONDITIONAL WATCH, bet-AND-raise cap question, R3 verify." Two tabs from the DASH notes.*

---

## THE NUMBERS

| Metric | Value |
|--------|-------|
| Current price | ~$230 (June 22, estimated) |
| 52-week range | Est. $150-$235 (cruise recovery run — NEEDS VERIFICATION) |
| Position in range | ~96%+ of range (top 5%) |
| Analyst consensus | Est. 2-3 Sell/Underperform, 10-14 Hold, 12-16 Buy (NEEDS VERIFICATION) |
| Highest Sell target | Unknown — critical. Must be below $184.25 (for $185P) or $179.62 (for $180P) |
| Earnings date | ~July 25, 2026 (Q2 2026 — needs confirmation) |
| Earnings history | Likely 4+ beats; beat-AND-raise status must be verified. Determines conviction cap. |
| Short interest | Est. 1-3% of float. No squeeze warning. |
| Net yield metric | Q2 net yield per passenger day YoY growth: consensus est. ~4-5% |

---

## BEAR CASE

**The specific scenario:**  
Q2 2026 earnings (~July 25). Royal Caribbean reports:
- Net revenue yield per passenger cruise day: +1% YoY (vs. consensus +4-5%). Yield growth is decelerating as post-COVID pricing premium fades.
- 2H 2026 guidance: Net yield +1-2% (vs. consensus +3-4%). Booking trends softening for peak 2027 sailing season.
- International onboard revenue (casino, spa, excursions): flat YoY as mid-income consumers reduce discretionary spend onboard.

**Stock reaction:** -18-22% to $179-188. Multiple scenarios:
- $185P: In the money if stock goes to $180 or below. Maximum gain if stock reaches $160.
- $180P: In the money if stock goes to $175 or below.

**Maximum loss:**
- $185P: $75 per contract
- $180P: $38 per contract

---

## GLOSSARY

**Net yield per passenger cruise day:** The most important cruise industry profitability metric. Calculated as: (Revenue - Commissions - Transportation costs) / (Available passenger cruise days). Available PCDs = ships × berths × operating days. Net yield growth indicates pricing power and onboard revenue performance. When this metric stops growing, cruise stocks typically reprice.

**Available passenger cruise days (APCDs):** The denominator in net yield calculations. Total theoretical capacity available. New ships coming online increase APCDs, diluting the metric unless pricing growth outpaces capacity growth.

**Booking lead time:** Cruise customers typically book 6-18 months in advance. Q2 earnings calls often include "booking data" for future sailing seasons. If management shows that 2027 bookings are coming in at lower prices than 2026 bookings, the yield growth thesis breaks.

**Beat-and-raise:** Beating EPS estimates AND raising forward guidance in the same quarter. The Island Fund's earnings history cap requires both components. A company that beats estimates but keeps guidance flat does NOT trigger the 4+ consecutive cap under a strict reading of the rule. This distinction is critical for RCL's conviction ceiling.

**Net Revenue Yield vs. Net Cruise Cost:** Revenue yield is on the top line; cruise cost is on the bottom. The spread between these two determines EBITDA margin expansion. If yield is flat but costs rise (fuel, crew wages, port fees), margins compress even without a revenue miss. Analysts watch both metrics on the earnings call.

---

## SHELDON BEAT

RCL is worth mentioning to Sheldon as a case study in sizing constraints. The framework is finding plays where the required conviction level conflicts with minimum contract cost at the current reserve size. That's a genuine problem for small funds using the puts framework. The solution: start with cheaper underlying stocks (like DASH at $1.00 per contract vs. RCL at $0.75-$1.07 per contract — wait, both are similar). Actually the constraint is about the PERCENTAGE of reserve, not the absolute dollar amount. As the fund grows, RCL becomes more naturally sized.

Note for Sheldon: the beat-AND-raise distinction in the earnings history cap. If we're only looking for beats (not explicit guidance raises), many more companies clear this rule. The more conservative reading (beats only = cap) vs. the precise rule text (beat-AND-raise) changes the universe significantly.
