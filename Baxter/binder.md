# BAXTER'S BINDER
*The green three-ring binder. Every tab is here. Read this before entering the room.*
*Last updated: June 20, 2026*

---

## TAB 1 — THE IRON RULES (CALLS)

Five rules. All five must pass. One fail kills the play regardless of everything else.

**Rule 1:** Stock within bottom 20-25% of its 52-week range. Price dislocation is the entry signal. We are not buying stocks we think are good. We are buying catalysts in stocks the market currently thinks are bad.

**Rule 2:** Confirmed earnings catalyst before expiry. No substitutes. Not product launches, not FDA dates, not analyst days, not macro events. Earnings forces resolution on a specific day. Everything else is narrative, and the market prices narrative before it happens. *BOTZ rule: themes without data mechanisms are dead money.*

**Rule 3:** Near-zero Sell ratings. Zero or one Underperform in the covering universe. When credentialed analysts who have full access to management all rate it Buy and the stock is at its 52-week low, the market has made an error that professionals do not support.

**Rule 4 (Bear Floor):** Lowest Buy target must be ABOVE call breakeven (strike + premium). The most pessimistic bull on the Street must still believe the stock exceeds our breakeven. Check at entry AND monitor throughout the hold. If the bear floor drops below breakeven after entry: **exit same day. No waiting.**

**Rule 5 (Chain Filter):** Option ask at or below $1.00/share. This is a chain quality gate, not a position sizing rule. If no instrument in the chain passes both Rule 4 and Rule 5 at the same strike, the play fails. Rule 5 does not get waived for a good thesis.

*Full reference: `Baxter/iron_rules_calls.md`*

---

## TAB 2 — THE IRON RULES (PUTS)

Inverted from calls. Entry on strength, not weakness.

**Rule 1:** Stock in top 20-25% of 52-week range AND no new 52-week high within prior 5 trading days. A fresh breakout has momentum buyers behind it. Wait for the stock to stall at its high before entering.

**Rule 2:** Confirmed earnings before expiry, minimum 21 DTE at entry. Same mechanism requirement as calls.

**Rule 3:** Minimum 2 Sell/Underperform ratings, OR documented Buy-to-Sell downgrade within 30 days. Buy-to-Hold downgrades do NOT satisfy Rule 3 -- a Hold analyst cannot contribute a bull ceiling. Rule 3 is load-bearing: fails here means Rule 4 cannot be evaluated.

**Rule 4 (Bull Ceiling):** Highest Sell target must be BELOW put breakeven (strike - premium). The most optimistic bear must still expect the stock to fall past our breakeven.

**Rule 5 (Chain Filter):** Option ask at or below $1.50/share. Raised from $1.00 to reflect premium environment on stocks near 52-week highs.

**Puts protocol (applied after all five rules pass):**

- **Short interest warning:** High short interest (>10% of float) is a squeeze risk, not a positive signal. Any positive earnings surprise triggers violent short-covering that wipes out the put. If present: minimum 4/5 conviction required, explicitly documented.
- **M&A/buyout disqualifier:** A takeover premium sends the stock up 20-40% immediately and the put expires worthless with no time to exit. Before entry, confirm no M&A rumors, no strategic review, no activist running a public campaign. If any are present, the play is disqualified regardless of Iron Rules scores.
- **IV timing advantage:** Stocks near 52-week highs often carry lower IV (market complacency at highs). Buying puts when IV is low means a falling stock delivers both intrinsic value AND IV expansion. This is a structural advantage relative to calls and should be noted in the research file.
- **Catalyst direction:** The earnings catalyst must specifically be expected to disappoint -- guidance cut, margin compression, subscriber miss, beat-and-guide-down structure. "Earnings catalyst exists" passes Rule 2. "The catalyst is specifically expected to be negative" determines whether conviction reaches 4/5. Cannot exceed 3.5/5 without a documented specific disappointment thesis.
- **Earnings history cap:** A company that has beaten and raised EPS estimates for four or more consecutive quarters cannot receive 4/5 conviction regardless of other factors. The earnings history is structurally against the short thesis.
- **Estimate revision check:** Verify direction of consensus EPS estimate movement in the 30 days prior to earnings. If estimates have been revised upward, the market has priced in optimism and a beat becomes more likely. Caps conviction at 3.5/5 unless a specific fundamental reason overrides the revision trend.

**How we find puts candidates:**
The reverse of the calls screen. Screen for stocks in the top 20-25% of their 52-week range, then filter for minimum 2 Sell/Underperform ratings, then check for earnings inside the option window. The opportunity set is approximately symmetric with calls -- in a bull market it tilts calls; in a sector rotation or sector-specific weakness it tilts puts. Names currently near 52-week highs with active analyst skepticism are the starting pool.

**Status:** System ratified June 18, 2026. No live puts entry until back-test of passes.md runs. The back-test documents what would have been entered and what happened -- not to cherry-pick wins but to calibrate whether the rules select plays the market subsequently confirmed. Three closed puts plays required before 5/5 conviction and the top of the sizing tier become available.

*Full reference: `Baxter/iron_rules_puts_draft.md`*

---

## TAB 3 — POSITION SIZING

*Revised June 20, 2026. The fund compounds, not accumulates.*

Position size = **percentage of current reserve at time of entry.** Not fixed dollars. As the reserve grows, so do the bets. A fixed dollar bet on a growing fund accumulates. A percentage bet compounds.

| Conviction | Range | Standard |
|---|---|---|
| 3.5/5 | 6–10% of reserve | 8% |
| 4/5 | 12–16% of reserve | 14% |
| 5/5 | 17–20% of reserve | 19% |

**Contracts:** floor(sizing budget ÷ (ask × 100)). Minimum 1. The contract count is derived output, not a separate decision.

**Intra-score confidence:** Two 4/5 plays are not the same play. A play where every rule passed with significant margin goes to 15-16%. A play where one rule barely cleared, or where any data required correction, goes to 12-13%. Document the confidence level at entry in one sentence in the research file.

**Correlated position cap:** Total reserve deployed to plays sharing the same primary macro driver may not exceed 35%. Rate-sensitive plays count toward the same correlated bucket. When near the cap, new plays in the same theme size at the bottom of their conviction tier.

**Hard caps:** Single play never exceeds 20% of reserve. No averaging down ever.

*Full reference: `Baxter/iron_rules_calls.md` (POSITION SIZING section)*

---

## TAB 4 — EXIT PROTOCOLS

**Standard exit:** Sell at market open the morning after earnings. Not before, not after. The catalyst fired. The thesis resolved. Holding past that point is speculation without a mechanism.

**Rule 4 live breach:** Exit same day. No exceptions. The floor moved. This was written in blood after BSX.

**Pre-earnings profit target:** If the stock reaches the bear floor price before the earnings date, evaluate same-day exit. The thesis resolved early. Holding through a binary event to extract the final increment introduces risk that was not in the original pricing.

**BOTZ watch:** If the play is not trending toward breakeven within two weeks of expiry and the thesis has no remaining mechanism, sell into remaining time value. Theta is not a hold reason.

**M&A announcement (puts only):** Exit at open the next trading day. The thesis is structurally destroyed regardless of current price.

**Never:**
- Average down on a position moving against the thesis
- Hold past the morning after earnings
- Waive a Rule 4 breach because the stock looks like it might recover
- Accept AH price spikes as evidence the exit rule was wrong

---

## TAB 5 — LESSONS FROM THE FIELD

*One lesson per closed play. These are permanent entries. They do not get removed when they become inconvenient.*

**CCL (+$1 | Jun 3):** Bear floor broke (stock below Rule 4 threshold). Cut and rotated to MDT. Recovered $99. The early exit felt premature and was correct. When the floor goes, you go.

**DSGX (-$30 | Jun 5):** Entered post-earnings on a spike into a short-dated OTM position. Gap-and-fade is a structural pattern on this entry type. The play was wrong at the moment of entry, not at the moment of loss. Rule: never enter OTM on a stock that has already moved on the event the thesis requires.

**CHWY (-$23 | Jun 5):** Strike too far OTM for the stock's implied move range. Sold pre-earnings to redirect capital to DKNG. Recovered $33 vs $0 projected at expiry. Entry was wrong from the start. Cutting to redeploy capital was correct management of a bad entry.

**NKE (-$70 | Jun 10):** RBC downgraded to Sector Perform, cut target to $50. Bear floor moved below breakeven -- live Rule 4 breach. Exited with 20 days remaining rather than hold a broken thesis. Recovered $116. The exit felt early and was right. Credentialed analysis moving the floor is the signal. The stock's subsequent behavior is irrelevant to the exit decision.

**MDT (+$23 | Jun 10):** Catalyst fired (June 3 earnings beat) and nothing remained in the window. No mechanism before expiry. Applied BOTZ rule. Cut at +52%, recovered $77. The position was working and we exited because the reason to hold disappeared. That is the correct behavior. A working trade with no remaining thesis is still a trade with no remaining thesis.

**DKNG (+$251 | Jun 12):** Sentiment window closed on World Cup Day 2. The handle is real but invisible until August 5 earnings -- no data mechanism existed inside the July 2 expiry window. Michael applied BOTZ. Sold at $3.00, recovered $600. The lesson: the thesis window has a close date that is not always the option expiry. Identify when the mechanism expires, not just when the option does. Sell the door when the door is open.

**BSX (-$15 | Jun 15):** Rule 4 breached on entry day -- Sheldon's June 12 letter revealed the bear floor had moved to $55, below $60.73 breakeven. Decision made Sunday. Exit Monday open. Cost: $6-12 in avoidable decay. **Permanent rule written: Rule 4 breach on a live position = same-day exit.** Not next morning. The delay was the error.

**HITI (-$12 | Jun 16):** Beat 42% on revenue. Stock ran to $3.14 AH. Sold limit at open: $0.22. Stock faded to $2.48 by mid-morning, below the $2.50 strike. Option would have gone to zero. The exit rule held and was right. AH spikes are noise. The rule is not noise.

---

## TAB 6 — STANDING DECISIONS

*These were debated and decided. They are not under review unless new evidence reopens them.*

**The BOTZ rule:** Themes without specific data mechanisms are dead money. Applies to entries (don't enter on a theme without a catalyst) and to hold decisions (when the mechanism expires, so does the reason to hold). Named for Sheldon's robotics ETF.

**Rule 4 live breach = same-day exit.** Written after BSX. No exceptions.

**Puts system requires back-test before first live entry.** Run every name in passes.md through the inverted Iron Rules. Document what would have been entered and what happened. The purpose is calibration, not cherry-picking.

**Puts conviction capped at 4/5 until three puts plays close with documented outcomes.** The calls system earned 5/5 sizing by demonstrating the rules work. The puts system has not yet.

**Puts system was debated and ratified June 18, 2026.** The question was whether Rule 1 inverts cleanly for puts -- it does. Entry logic for puts is that the stock is near highs instead of lows. The full debate (week-03/story/five_baxters_puts_debate_jun18.md) resolved with Prime drafting the inverted rules, Calxter validating the EV framework as structurally sound, Bearxter insisting on a back-test before the first live entry, and Macxter flagging the squeeze risk problem with short interest. Key corrections from independent review: Rule 3 OR clause restricted to Buy-to-Sell only (Buy-to-Hold analysts cannot contribute a bull ceiling); Rule 5 raised to $1.50 (high-priced stocks near highs carry different premium environments); short interest reframed from positive signal to squeeze warning.

**13F vs Form 4 are not the same signal.** A 13F is an institutional holdings filing -- what a fund owned at quarter-end. A Form 4 is an insider transaction -- what a named officer or director bought or sold in the open market, filed within 2 business days. Never conflate them in research or correspondence. Written after TRMB (Dave's letter, June 17).

**Data must be verified before it is written.** Stock prices, fill prices, analyst targets -- if it goes into a document, verify it live. The June 18 TRMB data failure (wrote $66.91, actual $49.15) is in the record and does not get forgotten.

**Intra-session data correction protocol:** If data from a prior session is found to be wrong, correct the source file first, then send correspondence. Do not paper over errors with follow-up letters that describe the error without fixing it.

**See-through risk:** The market may price past a good earnings quarter because it is already discounting the forward environment the quarter does not capture. When analysts have updated their models after a macro shift, their bear floors incorporate that shift. Watch guidance commentary on forward pipeline, not just headline beat/miss.

**Correlated position cap: 35%.** Total reserve deployed to any single primary macro driver. Rate-sensitive plays (construction tech, rideshare, anything rate-dependent) count toward the same bucket.

---

## TAB 7 — RISK

*(This section is intentionally short.)*

Maximum loss on any position is the premium paid. No margin. No borrowing. No averaging down. The worst case is always defined before entry and never changes after.

The risk of losing $76 on TRMB is that we lose $76.

The risk of not entering TRMB when it passed five Iron Rules at a 31% discount to the ask is that we never find out what the data was trying to tell us.

Baxter has thought about this more than the size of this section suggests.

---

*Update this file when: a rule changes, a decision is made permanent, a new lesson closes, or something in tabs 1-6 becomes stale.*
