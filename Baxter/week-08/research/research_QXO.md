# Research: QXO (QXO, Inc.) -- Aug 8, 2026

**Verdict: KILL. Rule 6 clears the cap by 0.06 points -- inside measurement noise, not real margin -- stacked on the same zero-trading-day earnings-into-expiry problem flagged for BKE. Not queued.**

## Setup

- Price: $16.17 (Aug 7, 2026 close, up 6.5% same session from $15.18)
- 52-week range: $13.18 - $27.61
- Percentile: **21st** -- bottom quartile, CALLS candidate on Step 1
- Confirmed catalyst: **Q2 2026 earnings, Aug 13, 2026, PM**, `get_earnings_results` verified: true -- matches the date supplied at the start of tonight's run.

## The structural flag

**Aug 13 PM earnings, Aug 14 expiry.** The reaction to a PM release prices in at the next session's open -- Aug 14 -- which is also this contract's expiration day. There is no trading session between the print and expiry; the position must be resolved at or near the Aug 14 open, the same shape as BKE and the same shape that put real money into KR on a wrong assumption there was room. One calendar day further removed than BKE's literal same-day collision, but functionally identical: zero real time to sell into a post-reaction rally or reassess before the contract dies.

## The Unified Screen

**Step 1:** 21st percentile, clears. **Step 2:** confirmed date, but see the structural flag. **Step 3 (Rule 3):** clean on the surface -- 19 analysts, consensus Strong Buy, 86% buy percentage, no explicit Sell/Underperform identified, reinforced by Morgan Stanley reinstating an Overweight rating at $35 on Aug 4, 2026.

## Rule 4 (Bear Floor)

Candidate instrument: $16.50C Aug 14 2026, ask $0.60. Breakeven $17.10, needs +5.8% from $16.17. Lowest current Buy-side reads found range $25-28, all comfortably above breakeven. **Rule 4 passes with large margin** -- this was never the problem either.

## Rule 6 (Reachability): the real problem

Four real, verified earnings-day moves pulled from actual daily closes:
- **Aug 14, 2025:** -0.19%
- **Nov 6, 2025:** +6.51%
- **Feb 25, 2026:** -3.74%
- **May 12, 2026:** -4.06%

Median absolute move: **3.90%.** 1.5x cap: **5.85%.** Current requirement: **+5.79%.**

**This technically passes -- by 0.06 percentage points, on a median built from four data points where the smallest and largest differ by more than 30x (-0.19% to +6.51%).** That is not the kind of margin the fund has ever called a real pass. Compare to tonight's actual advances: UAMY uses 37% of its cap, BTDR uses 47%. QXO uses 99%. The straddle cross-check (the $16.50 call at mark $0.50 plus the $16.50 put at mark $0.925 = $1.425 on a $16.17 stock, an 8.8% implied move) is more generous than the historical read, but the binder treats the straddle as a corroborating cross-check on the historical-median method, not a replacement for it when the two disagree this much about how much room actually exists.

Stacking a boundary-level Rule 6 pass on top of a zero-trading-day earnings-to-expiry collision is the same combination of "technically cleared, actually fragile" that the fund has learned costs real money (KR) or would have (SOUN's single-data-point read before the real four-quarter pull reversed it). Treated as a kill on that basis, not carried forward as a marginal advance.

## Decline category

Not reached as the deciding factor -- Rule 6 margin and the timing structure are the actual kill reasons, and further decline-category research wouldn't change either.

## What would reopen this

A later, affordable expiry with real buffer past Aug 13 (chain runs Aug 14 -> Aug 21 -> Aug 28 -> Sep -- an Aug 21 or Aug 28 strike near $16.50-17.00 would remove the timing flaw entirely and is worth a fresh look with live pricing, since Rule 4's wide cushion means an OTM strike further out could still clear breakeven with room). Tonight's screen only checked the Aug 14 instrument named in the original candidate list; the later-expiry question is a same-session follow-up worth flagging to Michael rather than a dead end.

## GLOSSARY

- **52-week range / percentile:** where the current price sits between the stock's low and high over the trailing year; 0% = at the low, 100% = at the high.
- **Rule 3 (ratings):** for calls, near-zero analysts rating the stock Sell/Underperform.
- **Rule 4 (bear floor):** the lowest price target among Buy-rated analysts must sit above the option's breakeven.
- **Rule 6 (reachability):** the move required to reach breakeven must not exceed 1.5x the stock's median historical earnings-day reaction.
- **Straddle:** buying the at-the-money call and put together; its combined price divided by the stock price gives the options market's own implied move, an independent cross-check on Rule 6.
- **Zero-buffer earnings:** when a reported earnings date falls on or effectively on an option's own expiration date, leaving no trading session between the reaction and the contract's expiry.
- **Breakeven:** strike price plus premium paid per share -- where the option holder neither gains nor loses at expiration.
