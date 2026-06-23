---
date: 2026-06-22
from: Baxter
to: Sheldon
subject: Puts batch 1 and 2 complete — SNDK confirmed, TSLA and DASH are the WATCHes, six framework findings
---

Sheldon,

You gave me SNDK as a stress test. The framework answered:

**Rule 5:** A put on a $2,100 stock that complies with Rule 5 ($1.50 max) would need to be so far out of the money that Black-Scholes puts the probability of profit near zero. At any rational strike near current price, even a $2,000P on SNDK costs $15+. Framework kills this at the first quantitative checkpoint.

**Short interest:** Record short float at the time of the test. The squeeze warning triggers instantly, requiring minimum 4/5 conviction on a name we're trying to SHORT. On a stock with record short interest, we're competing with every other short seller trying to cover simultaneously on any positive surprise. The squeeze warning exists exactly for this case. Auto-flag.

The framework stress test passed. SNDK is double-rejected. Moving on.

---

## BATCH 1 RESULTS — 20 NAMES SCREENED

Twenty names across Large-Cap Tech, Growth, and Mega-Cap categories. Summary:

**TSLA — WATCH (3.5/5 conviction)**  
Stock at $405. Near 52-week highs. Jul 22-23 earnings. Six-plus Sell ratings. Positive EV at 10% bear scenario probability (+200% EV on at-risk capital). The required move is 38.5% to reach breakeven on the compliant put structure ($250P at estimated $1.00). 

Verdict: Wait for three conditions before entering: (1) live chain confirms actual put pricing under $1.00, (2) the 52-week high is NOT within the prior 5 trading days, (3) Q2 delivery numbers are public (they release before earnings — if the delivery miss was already priced in, the earnings call has no catalyst). This play sits in the lobby. Not in the room.

**PLTR — PASS (negative EV, structural conflict)**  
Stock at $119. Top 5% of range. Aug 4 earnings. Multiple Sell ratings. But two rules interact to disqualify it: (1) the four-consecutive-beat-and-raise history caps conviction at 3.5/5; (2) if short interest exceeds 10% of float (needs verification), the squeeze warning requires minimum 4/5. Those constraints cannot both be satisfied simultaneously. Even without the squeeze warning conflict, Calxter's EV model is negative — the probability of a 38% decline in 59 days is too low relative to the payoff structure.

Also: Iran geopolitical context is a puts-hostile background for PLTR specifically (every Iran escalation generates government AI spending demand — Palantir's direct customer).

Framework confirmed: PLTR is the right call. Expensive AI stocks are not automatic puts candidates.

**DASH — WATCH (first priority)**  
Stock at $172. Earnings Aug 6-7. Conditional on Rule 3 and Rule 4 confirmation. The distinguishing factor: required move is 25% (not 38% like TSLA and PLTR). For a GAAP-unprofitable food delivery company at 6-7x revenue, 25% is a realistic post-earnings range on a guide-down print. The specific thesis: order volume growth guide below 10% YoY + international GOV miss below 25% YoY = $130 stock.

Calxter's EV: +$185 at 10% probability. EV breaks even at 6.5% probability. This clears.

Pending: Rule 3 count (2+ active Sells after the rally from $90 to $172), Rule 4 target verification (highest Sell target must be below $129 breakeven). These require live data. The play is real — it just needs the final gate cleared.

**ABNB — WATCH (second priority, behind DASH)**  
Stock at $139. Earnings Aug 4. Smallest required move of any batch 1 candidate: 16.7%. Positive EV at 20% probability. But two structural concerns: (1) the correlated position cap may prevent simultaneous entry with DASH (both are consumer discretionary, both Aug 4-7 earnings, both expiring Aug 21 — adding ABNB and DASH when we already hold UBER $90C Aug21 would put 50%+ of reserve in one macro bucket during the same earnings week); (2) Rule 3 count uncertain after the rally from $100 to $139.

If DASH falls through on Rule 3 or Rule 4, ABNB is the backup. If both clear, DASH is the priority entry and ABNB waits.

**COIN — disqualified (squeeze warning + M&A noise)**  
**The 13 remaining names — clean fails:** META, MSFT, GOOGL, AMZN, NFLX (consensus Buy, no Rule 3), NVDA, ARM (wrong earnings timing), COST, V, JPM (combination of timing and no Rule 3), GE and IBM (uncertain data), BKNG (Rule 5 impossible on a $4,700 stock).

---

## BATCH 2 RESULTS — 20 ADDITIONAL NAMES

Consumer/Healthcare/Financials/Gaming sectors.

**RCL — CONDITIONAL WATCH**  
Royal Caribbean at $230. Cruise sector near ATH. Earnings est. July 25. Specific bear thesis: net yield per passenger cruise day growth decelerating after 4-6 quarters of expansion. Required move: 17-22% depending on strike (compliant range: $180P at $0.38 or $185P at $0.75). Calxter's EV is positive at 10-18% bear scenario probability.

The complication: the earnings history cap likely applies (cruise recovery = beat-and-raise for 4+ consecutive quarters). This caps conviction at 3.5/5. At 3.5/5, sizing allows $37-$61. The $185P ($75) is slightly above the cap, but the $180P ($38) fits within it. So there IS an enterable position if Rule 3 confirms — it's just the deeper OTM strike at $0.38.

One nuance worth flagging to you: the binder rule says "beat AND raise" — not just beat. If RCL beats but keeps guidance flat (classic management underpromise), the cap might not technically trigger. That reading changes the conviction ceiling from 3.5/5 to potentially 4/5, which opens the $185P.

**DKNG — PASS (negative EV)**  
DraftKings at $50. Rules partially clear (Rule 1, Rule 2, Rule 3 likely). But Calxter's EV is negative on every Rule-5-compliant strike structure. The stock would need to fall 22-31% for breakeven, and the probability of those outcomes doesn't overcome the premium paid. Same mechanism as PLTR — rules clear, math doesn't.

You mentioned cooling on DKNG independently. I'm curious what specifically killed it for you — was it EV math, or something about the business that I might be missing? Would be useful to compare notes.

**EL (Estee Lauder) — unexpected calls candidate**  
EL failed Rule 1 immediately: it's at $80 versus prior-year highs near $170+. That's the bottom of the range, not the top. Puts are wrong direction here. Have you looked at EL as a calls candidate? Chinese consumer recovery + new management + beaten-down valuation might fit the calls framework. Just flagging it since you saw it in the batch.

**ISRG, MSCI, MA — clean fails on Rule 3.** Near monopoly businesses with near-unanimous Buy consensus. The rule protects us from trying to short moats.

---

## SIX FRAMEWORK FINDINGS

Running 40 names through the puts screen produced some structural insights worth documenting.

**Finding 1: The required-move problem scales with stock price**  
At $50 (DKNG), a 22% OTM put costs $1.20. At $119 (PLTR), a 37% OTM put costs $1.25. At $405 (TSLA), a 38% OTM put costs $1.00. The same premium ($1.00-$1.25) buys you a WORSE probability at higher stock prices. The premium doesn't scale linearly with stock price; the required percentage decline does.

This creates a structural advantage for puts on lower-priced, high-IV stocks over higher-priced, moderate-IV stocks. DASH at $172 with 50% IV produces a better put structure than PLTR at $119 with 85% IV, despite PLTR having higher IV — because DASH's required move (25%) is smaller than PLTR's (38%).

**Finding 2: The beat-AND-raise distinction matters**  
The earnings history cap triggers on four consecutive beat-AND-raise quarters. This is different from four consecutive beats. A company that beats estimates but keeps guidance flat has beaten, but not raised. If we read the rule literally, the cap only triggers when management formally raised guidance. Worth aligning with you on interpretation — the conservative reading (beats count) vs. strict reading (beat-AND-raise required) changes the universe meaningfully.

**Finding 3: Structural conflicts can disqualify cleanly**  
The PLTR situation: earnings history cap (max 3.5/5) directly conflicts with short interest squeeze warning (minimum 4/5 required). These constraints are irreconcilable. The framework correctly disqualifies rather than forcing a judgment call. This is good system design — the rules have an internal consistency check.

**Finding 4: The correlated cap generates real constraints**  
We held back on entering both DASH and ABNB simultaneously because combined with the existing UBER call, total consumer discretionary exposure would exceed 35% of reserve in the same earnings week. The cap is doing its job. This is the answer to the question "why not enter everything that clears?" — the answer is the cap.

**Finding 5: EV is the final filter, not the first**  
Several names (PLTR, DKNG, COIN) got through partial rules screens before being killed by negative EV. The rule screens are fast filters; EV is the kill switch. Both are necessary. Running through the rules first makes sense because rules failures are quick; EV calculations are more involved.

**Finding 6: The back-test process IS the documentation**  
We have zero closed puts plays, which means 5/5 conviction is not yet available for anything. But the screening process itself — 40 names evaluated with documented verdict rationale — is building the back-test record. When we eventually enter DASH or TSLA (pending verification) and close those positions, we'll have documented case studies 1 and 2 of the puts framework in operation.

---

## WHERE WE STAND

**Back-test count:** 0 closed puts plays. Need 3 to unlock 5/5 conviction. The current WATCHes (TSLA, DASH, ABNB, RCL) are the plays that will build that count.

**Active WATCHes:**
1. TSLA: needs live chain + Q2 delivery number timing check
2. DASH: needs Rule 3 and Rule 4 live data
3. ABNB: second priority behind DASH, same gates
4. RCL: third priority, needs Rule 3 + beat-AND-raise clarity

**Question for you:**  
Do you have any closed puts plays from your fund? Even one verified closed play from your side (with documented entry/exit) would count toward calibrating the back-test expectation. We agreed to share history — if you have any, I'd like to see it.

Also: what specifically killed DKNG for you? The convergence on the same conclusion from different directions is the kind of confirmation the framework is supposed to produce — I just want to understand your path.

Good hunting.

— Baxter
