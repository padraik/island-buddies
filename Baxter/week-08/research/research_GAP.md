# Research: GAP (The Gap, Inc.), Aug 7 to 8, 2026

**Verdict: KILL / low conviction (approximately 2.5 to 3/5). Rule 6 passes but the straddle disagrees with it, Rule 4's floor is unresolved, and the decline picture leans Category 2. The closest of tonight's six to a real pitch, but not there. Not queued.**

## Setup

- Price: $20.4546 (Aug 7, 2026 close, live re-verified, essentially flat versus the $20.52 prior close)
- 52-week range: $18.11 to $29.36
- Percentile: 21.0th, bottom quartile, the closest of tonight's six to the Rule 1 threshold's upper edge

## Earnings-date check

`get_earnings_results` returns **2026-08-27, PM, verified: true.** Matches the pre-screen exactly, no discrepancy.

## The Unified Screen

**Step 1 (Range percentile):** 21.0th percentile. Clears: CALLS candidate.

**Step 2 (Rule 2):** Confirmed above. Expiry Aug 28, 2026, the day after the print. A PM release on Aug 27 hits the tape after that session's close and prices into the Aug 28 open, the same day the option expires. This is not HIVE's true zero-buffer trap (the contract is alive for the full Aug 28 session and can be sold into the reaction), but it does mean the position must be assessed and closed same-day, with no second session to reconsider if the initial reaction misreads.

**Step 3 (Rule 3, ratings):** 19 analysts: **12 Buy, 7 Hold, 0 Sell.** Clean by the headline number, the best raw ratings count of tonight's six names. But the Street here is actively moving, not settled, see below.

## Rule 4 (Bear Floor)

The lowest price target found across sources is **$20**, but it belongs to **Evercore ISI (Michael Binetti), who downgraded Gap to In Line (Hold-equivalent) with that target.** A Hold-rated target does not count against Rule 4, which requires the lowest **Buy-rated** floor. JPMorgan also cut its rating, from Overweight to Neutral, with a $27 target, so that number is now Hold-rated too and also does not count.

Among analysts still Buy-rated, the visible numbers run higher: Citigroup at $27 (dated Mar 6, 2026, before the recent guide-down, so it fails the binder's 60-day freshness test and cannot be trusted as a current floor), UBS recently raised to $41 (upgrading to Buy, citing beauty and handbag momentum), and Barclays raised to $33 (citing lower rates and gas prices as consumer tailwinds). Both the UBS and Barclays figures, if fresh and Buy-rated as described, would clear the $23.20 breakeven with real room. But their exact dates could not be pinned down with confidence in the time available, and per the KR lesson, an unverified "it's probably fine" read is not the same as a checked one. **Recording Rule 4 as unresolved**, not a pass, until a specific Buy-rated target with a confirmed post-decline date is in hand.

## Rule 5 (Chain Filter)

Candidate instrument: **$22.50C Aug 28 2026, ask $0.70, bid $0.45** (live re-verified, matches the pre-screen exactly). At $0.70/share, $70 at risk, this fits comfortably inside the 3.5/5 sizing tier on the current reserve. Affordability is not the constraint.

## Rule 6 (Reachability)

Breakeven $23.20. Needed move from $20.4546: **+13.42%.**

Four real, verified earnings-day reactions (all PM releases, reaction next session):
- Aug 28, 2025: close $21.68 to $22.01, +1.52%
- Nov 20, 2025: close $23.06 to $24.96, +8.24%
- Mar 5, 2026: close $27.20 to $23.28, -14.41%
- May 28, 2026: close $25.00 to $21.15, -15.40%

Median absolute move: **11.33%.** 1.5x cap: **16.99%.**

**Rule 6: passes with real margin.** The required move (13.42%) uses about **79% of the cap**, the second-best Rule 6 read of tonight's six names. Gap's last two prints have both moved the stock over 14%, so the historical case for this move existing is genuinely strong.

## Straddle cross-check, and where it disagrees with Rule 6

At the $20.50 strike (nearest to the $20.4546 spot, effectively at the money): call mark $1.35 (bid $0.95 / ask $1.74) plus put mark $1.20 (bid $0.97 / ask $1.43) equals **$2.55 combined premium** on a $20.4546 stock, a market-implied move of **12.5%.** That is **below** the 13.42% this trade actually needs to reach breakeven. Unlike ENVX above, where the straddle confirmed the historical Rule 6 read, here the live options market is pricing in slightly **less** movement than the trade requires. This is a genuine, worth-taking-seriously disagreement between the two independent checks the binder's audit specifically added to catch this kind of gap, and it argues for caution rather than confidence, even though Rule 6's historical arithmetic technically clears.

## Decline category

Real, multi-part fundamental issues, not a single clean miss:

1. **Old Navy guided down.** The company cut its full-year net sales growth outlook to 1 to 2% from 2 to 3% after Old Navy's seasonal categories, specifically women's dresses, underperformed in Q1 2026.
2. **Athleta is a two-year decline, not a one-quarter stumble.** Comparable sales fell 11% in Q1 2026, on top of an 8% decline the year before. This is a supposed growth brand posting back-to-back negative comps.
3. **Tariffs are a real, quantified margin drag.** Management guided to a 150 to 200 basis point gross margin hit, with tariffs alone estimated at 200 basis points.
4. **The Street is actively split, not settled.** Evercore cut from Strong Buy to In Line; JPMorgan cut from Overweight to Neutral, both around the guide-down. At the same time, UBS and Barclays raised targets and, in UBS's case, upgraded to Buy, citing a different set of considerations (beauty and handbag momentum, macro tailwinds from lower rates and gas prices). That is a genuine disagreement playing out in real time, not a settled Category 1 overreaction where the consensus already agrees the drop was excessive.

The combination (a guided-down outlook, a second brand in a multi-year decline, a quantified cost headwind, and an actively divided analyst response) reads closer to **Category 2 (real, ongoing deterioration)** than Category 1, even though the stock clears Rule 1's dislocation test and Rule 6's historical arithmetic on its own.

## Why this still doesn't clear the bar

Every hard rule checked tonight (Rule 2, Rule 3, Rule 5, Rule 6) technically passes for GAP, which makes it the strongest name in the batch by rule count. But the two checks designed to catch exactly this kind of situation, the straddle cross-check and the decline-category test, both raise real flags: the live market is pricing a smaller move than this trade needs, and the underlying business has multiple genuine headwinds an analyst split has not resolved. Rule 4 is also unresolved rather than confirmed. Stacking those together argues for conviction below the 3.5 threshold rather than a real pitch, even on the best-scoring name of the night.

## What would reopen this

A specific, dated, Buy-rated target confirmed above breakeven (closing the Rule 4 gap) combined with either the straddle moving to imply 13.4%+ or a second data point suggesting the Old Navy and Athleta weakness is stabilizing (a same-store-sales print or preliminary guidance update ahead of Aug 27) would meaningfully improve this. Worth a second look closer to the print if the chain and ratings picture firms up.

## GLOSSARY

- **52-week range / percentile:** where the current price sits between the stock's low and high over the trailing year; 0% equals the low, 100% equals the high.
- **Rule 2 (confirmed catalyst):** the Iron Rule requiring a dated earnings event before the option's expiration, verified via `get_earnings_results` first.
- **Rule 3 (ratings):** for calls, the requirement that near-zero analysts rate the stock Sell/Underperform.
- **Rule 4 (bear floor):** the lowest price target among Buy-rated analysts must sit above the option's breakeven, dated within 60 days and published after the decline.
- **Rule 5 (chain filter):** the cap on how much a single option contract can cost, scaled to the fund's reserve and conviction tier.
- **Rule 6 (reachability):** the move required to reach breakeven must not exceed 1.5x the stock's median historical earnings-day reaction, checked against real price bars.
- **Breakeven:** strike price plus premium paid per share, the price at which the option holder neither gains nor loses at expiration.
- **Straddle:** buying the at-the-money call and put together; its combined premium divided by the stock price gives the options market's own implied move for the period, a forward-looking cross-check against the backward-looking Rule 6 median.
- **Decline category (Category 1 vs 2):** whether a stock's drop reflects a one-off market overreaction (tradeable) or real, ongoing business deterioration (not tradeable).
- **Comparable sales (comps):** sales growth at locations open at least a year, isolating underlying demand from store-count changes.
- **Basis point:** one hundredth of a percentage point, the standard unit for describing margin changes.
