# Research: CPRT (Copart, Inc.), Aug 7 to 8, 2026

**Verdict: KILL. Rule 6 decisive fail. Not queued.**

## Setup

- Price: $29.66 (Aug 7, 2026 close, live re-verified)
- 52-week range: $26.81 to $50.11
- Percentile: 12.2th, bottom quartile

## The Unified Screen

**Step 1 (Range percentile):** 12.2nd percentile. Clears: CALLS candidate.

**Step 2 (Rule 2, confirmed catalyst):** `get_earnings_results` returns 2026-09-03, PM, **verified: false** (estimated from cadence, not yet company-announced). A confirming WebSearch, run per the Aug 7 standing rule for unverified dates, found real disagreement rather than confirmation: TipRanks lists Sep 9, 2026 (labeled "Confirmed"); Unusual Whales lists Sep 3, 2026; a third source repeats Sep 9. This is the same shape of trap that put the wrong date on KR: multiple aggregators disagreeing rather than echoing one stale number, but still not a single trustworthy date. Flagging this as a real finding: **the true Q4 FY2026 earnings date is unresolved between Sep 3 and Sep 9, 2026**, and neither the tool nor a search confirmed it against Copart's own investor relations page. Practically moot for this play (see Rule 6 below), but it would need to be pinned down before any real entry on this name in a future cycle. Both candidate dates sit safely before the Sep 18, 2026 expiry either way.

**Step 3 (Rule 3, ratings):** Not scored. See Rule 6.

## Rule 6 (Reachability)

Candidate instrument: **$32.50C Sep 18 2026, ask $0.80, bid $0.55** (live re-verified, matches the pre-screen exactly). Breakeven $33.30. Needed move from $29.66: **+12.27%**.

Four real, verified earnings-day reactions pulled from actual daily bars (not estimated):
- Sep 4, 2025 (PM release, reaction next session): close $49.97 to $48.57, -2.80%
- Nov 20, 2025 (PM): close $41.02 to $40.73, -0.71%
- Feb 19, 2026 (PM): close $37.65 to $36.48, -3.11%
- May 21, 2026 (PM): close $34.40 to $33.79, -1.77%

Median absolute move: **2.29%.** 1.5x cap: **3.43%.**

**Rule 6: decisive fail.** The required move (12.27%) is roughly **3.6 times** the cap, the worst reachability mismatch of tonight's six names. Copart is a large, stable auto-salvage operator; its stock has not moved more than 3.1% on any of its last four prints. There is no plausible mechanism by which this earnings catalyst delivers a move four times larger than anything in its recent history.

## Decline category, Rule 4, Rule 5, straddle

Not scored. Per binder precedent (research_ZTS.md, Aug 4): once a name dies decisively on Rule 6, spending further searches on Rule 3/4 detail or a straddle cross-check would not change the verdict, and the standing token-budget rule says not to spend what a decision doesn't need.

Worth noting: the original screen flagged CPRT as "comfortable" on buffer (15 days to earnings) with only a liquidity caveat (35 shares volume). That read was correct as far as it went, but buffer was never the problem here. A stock that structurally moves 1 to 3% on earnings cannot be sized into a play that needs 12%, no matter how much time sits between the print and expiry.

## What would reopen this

A strike close enough to the money to need under 3.4% would fit Rule 6, but nothing that cheap exists near a 12th-percentile stock without also failing Rule 5's affordability screen at this reserve. Not worth requeuing absent a much larger dislocation or a strike search closer to the money.

## GLOSSARY

- **52-week range / percentile:** where the current price sits between the stock's low and high over the trailing year; 0% equals the low, 100% equals the high.
- **Rule 2 (confirmed catalyst):** the Iron Rule requiring a dated earnings event before the option's expiration, verified via `get_earnings_results` first, WebSearch only as a fallback or confirming check.
- **Rule 3 (ratings):** for calls, the requirement that near-zero analysts rate the stock Sell/Underperform.
- **Rule 4 (bear floor):** the lowest price target among Buy-rated analysts must sit above the option's breakeven.
- **Rule 5 (chain filter):** the cap on how much a single option contract can cost, scaled to the fund's reserve and conviction tier.
- **Rule 6 (reachability):** the move required to reach breakeven must not exceed 1.5x the stock's median historical earnings-day reaction, checked against real price bars.
- **Breakeven:** strike price plus premium paid per share, the price at which the option holder neither gains nor loses at expiration.
- **verified flag:** `get_earnings_results`' indicator of whether an earnings date is company-announced (true) or estimated from reporting cadence (false).
- **Decline category (Category 1 vs 2):** whether a stock's drop reflects a one-off market overreaction (tradeable) or real, ongoing business deterioration (not tradeable).
