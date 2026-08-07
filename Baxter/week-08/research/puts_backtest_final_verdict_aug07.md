# PUTS BACK-TEST -- FINAL VERDICT
*Aug 7, 2026. Completes the Jul 16 interim (`week-06/research/puts_backtest_verdict_jul16.md`), scheduled for Aug 8-10, run one day early since all four catalysts had already resolved by tonight. Data pulled via `fetch_option_history.py` (built Jul 13, the fix for the tool gap that burned the original Jul 10 attempt). Rendered on the main thread without a Fable 5 pass -- the data is unambiguous enough that premium reasoning would be spent restating it, not resolving anything uncertain.*

---

## VERDICT: PUTS STAY BLOCKED FOR LIVE ENTRY. THE PROPOSED ENTRY-TIMING RULE IS ADOPTED FOR ANY FUTURE ATTEMPT.

The back-test requirement (binder Tab 6: "Puts system requires back-test before first live entry") is now formally satisfied -- this document is that back-test, completed. The verdict it returns is negative on the method tested, not a pass.

---

## THE SCOREBOARD (real closes, Aug 6, 2026 -- all four catalysts resolved)

| Instrument | Jun 23 fill | Aug 6 close | Result |
|---|---|---|---|
| TSLA $250P Aug21 | $1.29 | $0.18 | **-86.0%.** Real bounce to +53.5% (Jul 24) around the Jul 22-23 print -- something in the release spooked the stock despite the delivery beat -- then collapsed back to a near-total loss by close. |
| DASH $130P Aug21 | $2.46 | $0.01 | **-99.6%.** Essentially worthless well before its own Aug 6-7 catalyst arrived. |
| ABNB $115P Aug21 (sub.) | $1.61 | $0.01 | **-99.4%.** One real spike to +26.1% (Jul 29) on broader volatility, otherwise a straight bleed. |
| RCL $190P Aug21 (sub.) | $0.88 | $0.01 | **-98.9%.** Confirms the interim read: no real market most days ($0.01 lows throughout), the stock rallied into its own print rather than falling. |

**Zero winners. All four catastrophic. No close calls, no ambiguity for a verdict to arbitrate.**

---

## FINDINGS

**1. Correction (Aug 7, later same evening): "theta funeral" is real for this trade's structure, not for options duration in general.** Michael challenged the original framing directly: theta decay accelerates near expiration rather than running flat, which is exactly why far-dated options (LEAPS and similar) are a standard strategy elsewhere -- claiming any 60+ day entry decays to worthless would mean every trader using longer-dated options is wrong, which isn't supported by anything here. What actually happened to these four: deep-OTM, single-catalyst-dependent bets, with nothing else expected to move them favorably, held through weeks of dead time before the one event that justified the position. TSLA is still the sharpest data point, but for a narrower reason than duration -- it got a real, favorable-for-the-bear move around its print and *still* lost 86%, because the position was thin and OTM enough that six weeks of ordinary decay had already spent most of the premium before the print mattered. That's a structural problem (thin OTM + single-event dependency + dead time), not a blanket duration problem.

**2. The proposed entry-timing rule is well-supported for this fund's specific structure, but not proof about options duration broadly.** None of the four documented entries were placed inside 21 days of their catalyst -- all were ~60-day holds from the Jun 22 screen. This back-test cannot show what a ≤21-day entry actually would have returned, and it says nothing about longer-dated positions built differently (closer to the money, or not dependent on one binary event). It shows that far-dated entries into thin, single-catalyst OTM bets fail decisively, which is the premise the ≤21-day proposal is actually built on. Adopting the rule is a reasoned response to that narrower risk, not a confirmed win and not a general options-theory claim.

**3. Screen-day prices re-verified, no further corruption found.** All four candle series pulled clean and continuous, no discontinuities matching the TTD/CMG label-desync pattern (Jul 16 Finding 3). That corruption stays isolated to the two already-excluded names.

**4. Momentum extends through full resolution, not just the interim read.** RCL rallied into its own earnings rather than falling -- fading strength without a dated disappointment mechanism cost the position the way Finding 4 of the interim predicted. Reconfirmed, not new.

---

## THE RULE CHANGE

**Puts Rule 2 amendment, adopted: no puts entry more than 21 days before the dated catalyst.** Grounded in the structural reason (thin OTM, single-event dependency, unproductive dead time), not a claim that options duration itself is the problem -- see the revised Findings 1-2 above. This does not retroactively change anything already screened or logged -- it governs any future puts entry attempt only. The existing standing caps remain in force on top of it: puts conviction is still capped at 4/5 until three closed puts plays exist with documented outcomes (binder Tab 6), and this back-test does not count as one of those three, since nothing was actually entered.

**What this means in practice:** puts are not "unblocked" in the sense of being tradeable starting tomorrow. The back-test gate is satisfied and the entry-timing rule exists now for whenever a real puts-zone candidate is found inside a 21-day window of its catalyst -- which the fund's own screening has produced dozens of candidates for for logging purposes already (Aug 6-7 sweep alone logged 71+ puts-zone names), none yet re-screened against the new timing rule. The next puts-zone name that clears the full inverted Iron Rules AND sits inside 21 days of its catalyst is eligible for a real pitch. Nothing before that point is.

---

## STANDING ITEMS CLOSED OUT

- Jul 16 interim's "final pass" scheduled Aug 8-10: complete, one to three days early.
- Calxter's original Jul 31 deadline: already met by the Jul 16 interim, reconfirmed final here.
- TDOC: still on the gated watch list, unaffected by this verdict (it was never one of the six calibration names).

## COST NOTE (why this run didn't repeat Jul 10)

Four `fetch_option_history.py` calls, zero web searches, zero subagents, run directly in the main session so it could be watched and stopped if anything went sideways. The Jul 10 failure happened before that script existed; tonight's version of the same task cost four cheap tool calls instead of six figures of tokens in two minutes.

## GLOSSARY

- **Back-test:** Evaluating documented hypothetical entries against what the market subsequently did, real historical data, not live capital.
- **Theta:** The daily decay of an option's time value, the cost of holding a position while nothing happens.
- **Theta funeral:** This fund's term for an option that decays to near-worthless before or despite its catalyst resolving, because it was entered too far ahead of the event.
- **Substituted (sub.):** The documented strike didn't exist in the historical feed; the nearest listed strike was used (ABNB $117 to $115, RCL $185 to $190), per the Jul 16 convention.
- **Label-desync bug:** The fetch_price.py defect (fixed Jul 12, 2026) that shifted batch quotes onto the wrong ticker; source of the TTD/CMG exclusions in the original six-name sample.
- **Momentum (puts context):** The tendency of a stock already near its highs to keep rising rather than reverse, the force a top-of-range put entry fights without a specific dated mechanism.
