# Research: ENVX (Enovix Corporation), Aug 7 to 8, 2026

**Verdict: KILL (decline category), despite the best Rule 6 and straddle profile of tonight's six names. Not queued.**

## Setup

- Price: $4.71 (Aug 7, 2026 close, live re-verified)
- 52-week range: $3.67 to $14.21
- Percentile: 9.8th, deep bottom decile, the lowest of tonight's six names

## Earnings-date check

`get_earnings_results` returns **2026-08-12, PM, verified: true.** Matches the pre-screen exactly, no discrepancy.

## The Unified Screen

**Step 1 (Range percentile):** 9.8th percentile. Clears: CALLS candidate, and the most dislocated name of the batch by this measure.

**Step 2 (Rule 2):** Confirmed above. Expiry Aug 14, 2026: a PM release on Aug 12 prices its reaction into Aug 13, leaving Aug 13 and Aug 14 before expiry, a genuine two-day buffer as briefed.

**Step 3 (Rule 3, ratings): a real conflict, not a clean pass.** An aggregator (stockanalysis, 6 analysts sampled) shows 2 Strong Buy, 2 Buy, 2 Hold, **0 Sell.** On its face that clears. But a direct search for recent analyst action found a specific, dated downgrade the aggregator's snapshot does not appear to reflect: **JPMorgan cut ENVX to Underweight from Neutral on May 6, 2026**, citing a slower-than-expected production ramp with Enovix's lead smartphone customer (Honor) and the risk that competing battery makers narrow Enovix's energy-density advantage. Underweight is JPMorgan's Sell-equivalent rating. Treating Rule 3 as a clean "0 Sell" pass would be wrong: with at least one confirmed Sell-class rating on the books, ENVX sits **at** Rule 3's maximum allowance (1), not comfortably clear of it. This is exactly the kind of stale-aggregator trap the binder's earnings-date lesson generalizes to ratings data too: a summary site's headline count is not the same as checking who actually said what and when.

## Rule 4 (Bear Floor)

Reported analyst targets are scattered and inconsistent across sources: one source's average is $12.00 with a $6 to $15 range after resets; another cites a 12-month consensus of $21.67 with individual targets from $16 (Northland) to $24 (Oppenheimer); a third describes targets "reset lower to a range of $6 to $15" specifically because of the slower revenue ramp. Even the lowest figures cited ($6 to $7) would clear the $5.21 breakeven if Buy-rated and fresh, but the spread across sources is too wide and too internally inconsistent to certify a specific, dated, Buy-rated floor with confidence tonight. Recording as **unresolved**, and notably less clean than KR's single, traceable Goldman number.

## Rule 5 (Chain Filter)

Candidate instrument: **$4.50C Aug 14 2026, ask $0.71, bid $0.37** (live re-verified, matches the pre-screen exactly). At $0.71/share, $71 at risk, this fits comfortably inside the 3.5/5 tier (6 to 10% of the $1,054.96 reserve, $63 to $105) with real room, and would also fit a 4/5 tier for two contracts ($142, inside the $126.60 to $168.79 range) if conviction supported it. Affordability is not a constraint here.

## Rule 6 (Reachability)

Breakeven $5.21. Needed move from $4.71: **+10.62%.**

Four real, verified earnings-day reactions (all PM releases, reaction next session):
- Jul 31, 2025: close $13.40 to $10.705, -20.11%
- Nov 5, 2025: close $11.32 to $9.03, -20.23%
- Feb 25, 2026: close $6.15 to $5.95, -3.25%
- May 13, 2026: close $7.29 to $6.30, -13.58%

Median absolute move: **16.85%.** 1.5x cap: **25.27%.**

**Rule 6: passes with the widest margin of tonight's six names.** The required move (10.62%) uses only **42% of the cap.** Enovix's earnings-day reactions have been genuinely violent, twice over 20%, which makes this the easiest Rule 6 pass of the batch by a wide margin.

## Straddle cross-check

At the $4.50 strike (the candidate itself, effectively at the money against a $4.71 stock): call mark $0.54 (bid $0.37 / ask $0.71) plus put mark $0.36 (bid $0.31 / ask $0.41) equals **$0.90 combined premium** on a $4.71 stock, a market-implied move of **19.1%**, nearly double the 10.62% this trade needs. This corroborates the historical Rule 6 read rather than contradicting it: two independent methods, backward-looking median reactions and forward-looking options pricing, both say the required move is well within reach.

## Decline category, the actual kill

This is where ENVX dies, and it dies despite the best numbers in tonight's batch.

The May 13, 2026 print **beat Wall Street on both EPS and revenue**, yet the stock still fell roughly 17% after hours. JPMorgan's Underweight downgrade came the week before that print and was not about the numbers: it was about **forward execution**, specifically a slower Honor smartphone-battery production ramp, weak manufacturing yields, and a narrowing energy-density edge versus competitors as rivals catch up. Coverage since has described "smartphone qualification delays" as a recurring, multi-quarter theme, with even bullish analysts pushing their timelines out by more than a year. This is the binder's own **see-through risk** pattern by name: the market is discounting a real forward problem that a good quarter cannot fix by itself, which is a Category 2 signal (real, ongoing deterioration) rather than Category 1 (the market overreacted to a headline on an otherwise-fine business).

Cash burn adds weight to the same read: roughly $33M in operating cash outflow and $36M in free cash flow outflow in the most recent quarter cited, offset for now by a strong liquidity position (current ratio 8.3, about $529M in cash and securities) but not the profile of a company just waiting to be proven right by its next print.

## Why the strong Rule 6 number does not save this

Rule 6 measures whether the stock's history can plausibly deliver the needed move. It says nothing about whether that move, if it comes, would be good news or bad news, or whether the company is actually improving. ENVX's violent earnings-day swings (twice over 20%) are exactly the profile of a stock whose next print could deliver either a blowout recovery or another leg down on the same chronic execution story, and the JPMorgan downgrade, the beat-and-still-drop pattern, and the qualification-delay narrative all point toward the latter being at least as likely as the former. Buying a call here is closer to betting on which way a real coin flip lands than buying a mispriced recovery.

## What would reopen this

A confirmed resolution to the Honor qualification timeline (a specific shipped-volume announcement, not another "on track" comment) or a second consecutive quarter where the stock's reaction is not dominated by forward guidance concerns would meaningfully change this read. Absent that, this is a business with a real open question the market has not resolved, not a stock the market got wrong.

## GLOSSARY

- **52-week range / percentile:** where the current price sits between the stock's low and high over the trailing year; 0% equals the low, 100% equals the high.
- **Rule 2 (confirmed catalyst):** the Iron Rule requiring a dated earnings event before the option's expiration, verified via `get_earnings_results` first.
- **Rule 3 (ratings):** for calls, the requirement that near-zero analysts rate the stock Sell/Underperform.
- **Rule 4 (bear floor):** the lowest price target among Buy-rated analysts must sit above the option's breakeven.
- **Rule 5 (chain filter):** the cap on how much a single option contract can cost, scaled to the fund's reserve and conviction tier.
- **Rule 6 (reachability):** the move required to reach breakeven must not exceed 1.5x the stock's median historical earnings-day reaction, checked against real price bars.
- **Breakeven:** strike price plus premium paid per share, the price at which the option holder neither gains nor loses at expiration.
- **Straddle:** buying the at-the-money call and put together; its combined premium divided by the stock price gives the options market's own implied move for the period.
- **Decline category (Category 1 vs 2):** whether a stock's drop reflects a one-off market overreaction (tradeable) or real, ongoing business deterioration (not tradeable).
- **See-through risk:** the binder's term for when the market prices past a good quarter because it is already discounting a forward problem the quarter itself does not resolve.
- **Underweight:** JPMorgan's Sell-equivalent rating tier, below Neutral (Hold) and Overweight (Buy).
