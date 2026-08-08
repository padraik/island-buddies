# Research: BILI (Bilibili Inc.), Aug 7 to 8, 2026

**Verdict: KILL. Rule 6 fail, on a corrected earnings date. Not queued.**

## Setup

- Price: $18.73 (Aug 7, 2026 close, live re-verified)
- 52-week range: $15.79 to $36.40
- Percentile: 14.3rd, bottom quartile

## Earnings-date correction

`get_earnings_results` returns BILI's Q2 2026 print at **2026-08-27, AM, verified: true** (company-announced). This corrects the pre-screen's assumption of Aug 26: the real, verified date is one day later. Small on its own, but it changes the buffer math against the Aug 28, 2026 expiry: an AM release on Aug 27 prices its reaction into that same session, leaving roughly one trading day (the rest of Aug 27 plus Aug 28) before expiry rather than the two days originally assumed. Tight, not structurally broken like HIVE, but tighter than briefed, and it is exactly the kind of one-day slip that goes unnoticed until it matters, per the binder's standing lesson on TRMB.

## The Unified Screen

**Step 1 (Range percentile):** 14.3rd percentile. Clears: CALLS candidate.

**Step 2 (Rule 2):** Confirmed above, verified true. Clears.

**Step 3 (Rule 3):** Not scored. See Rule 6.

## Rule 6 (Reachability)

Candidate instrument: **$20.00C Aug 28 2026, ask $0.78 (STRETCH-flagged in the pre-screen), bid $0.32** (live re-verified, matches). Breakeven $20.78. Needed move from $18.73: **+10.94%.**

Four real, verified earnings-day reactions (all AM releases, same-session reaction):
- Aug 21, 2025: close $25.305 to $23.76, -6.11%
- Nov 13, 2025: close $27.19 to $25.89, -4.78%
- Mar 5, 2026: close $27.50 to $25.55, -7.09%
- May 19, 2026: close $19.63 to $20.00, +1.88%

Median absolute move: **5.44%.** 1.5x cap: **8.17%.**

**Rule 6: fail.** The required move (10.94%) is about **1.34 times** the cap. Not the lopsided kill CPRT or HIVE produced, but a real fail: three of BILI's last four prints moved the stock 4.8 to 7.1%, well short of what this contract needs, and the one quarter that came close to a double-digit move (the 6.11% Aug 2025 print) still falls short of the 10.94% requirement.

## Decline category, Rule 3, Rule 4, Rule 5, straddle

Not scored. Rule 6 fails cleanly enough, and independently enough of the STRETCH-flagged ask price already noted in the pre-screen, that further research spend would not change the outcome. Per binder precedent, the categorical kill makes it moot.

## What would reopen this

A strike close enough to need under roughly 8% would fit Rule 6 on this history. The $18.50 or $19.00 strikes would need re-checking against live asks if BILI comes back around for a future cycle, since the current $20.00 candidate is priced too far out of the money for what this stock's earnings history can actually deliver.

## GLOSSARY

- **52-week range / percentile:** where the current price sits between the stock's low and high over the trailing year; 0% equals the low, 100% equals the high.
- **Rule 2 (confirmed catalyst):** the Iron Rule requiring a dated earnings event before the option's expiration, verified via `get_earnings_results` first.
- **Rule 6 (reachability):** the move required to reach breakeven must not exceed 1.5x the stock's median historical earnings-day reaction, checked against real price bars.
- **verified flag:** `get_earnings_results`' indicator of whether an earnings date is company-announced (true) or estimated from reporting cadence (false).
- **Breakeven:** strike price plus premium paid per share, the price at which the option holder neither gains nor loses at expiration.
- **STRETCH flag:** the pre-screen's marker for an ask price sitting toward the expensive end of what the sizing tier can afford, a liquidity and cost caution rather than a rule failure on its own.
