# Research: BKE (The Buckle, Inc.) -- Aug 8, 2026

**Verdict: KILL, hard flag. Earnings lands ON the only affordable expiry -- the exact KR structural problem, verified live and confirmed real, not glossed over. Triple-killed independent of that flaw. Not queued.**

## Setup

- Price: $45.92 (Aug 7, 2026 close)
- 52-week range: $40.73 - $61.69
- Percentile: **25th** -- right at the bottom-quartile boundary, CALLS candidate on Step 1
- Confirmed catalyst: **Q2 FY2026 earnings, Aug 21, 2026, AM**, `get_earnings_results` verified: true -- matches the date supplied at the start of tonight's run exactly.

## The structural flag, checked first because it was flagged going in

**Earnings (Aug 21, AM) and the nearest affordable expiry (Aug 21) are the same day.** Verified live via `get_earnings_results`, not assumed. This is the identical shape to KR's Sep 4 problem, which entered real money on a wrong assumption that room existed before expiry -- here the date is confirmed correct, but the zero-buffer structure is the same danger: there is no trading session between the reaction and the contract's expiration. A pre-market AM release on expiry day means the stock reaction is baked into the opening print, and the position must be exited into whatever the market gives at or near that open, with no ramp-then-decide window.

**Checked for a later expiry with an affordable strike, per the specific instruction not to gloss over this.** BKE's chain only goes Aug 21 -> Sep 18 -> Dec 18 -> Mar 19 next. Sep 18 is the first real post-earnings expiry (28 days of buffer). Pulled live quotes on the two nearest-the-money Sep 18 calls:

- **$45C Sep 18:** ask $3.30 ($330/contract). Breakeven $48.30, needs +5.2% from $45.92.
- **$47.50C Sep 18:** ask $1.85 ($185/contract). Breakeven $49.35, needs +7.5% from $45.92.

Both fail Rule 5 outright -- the transitional-lock ceiling is $1.00/share, and the cheaper of the two is still 85% over it. There is no strike at Sep 18 that is both affordable and meaningfully closer to the money; going further OTM to find a cheaper ask only makes Rule 6 worse, not better. **The later expiry does not rescue this name.** It trades the timing flaw for an affordability flaw, and Rule 6 fails at either expiry regardless (see below) because the stock's own historical earnings-day moves are simply too small for what any of these strikes need.

## The Unified Screen

**Step 1:** 25th percentile, right at the boundary but clears. **Step 2:** confirmed date, but see the structural flag above -- Rule 2 requires a catalyst *before* expiry, and this is a catalyst *on* expiry, which the binder treats as the KR-lesson danger zone, not an automatic disqualifier by the letter of the rule, but a hard flag by the spirit of the standing correction written after KR. **Step 3 (Rule 3):** thin and unfavorable -- see Rule 4 below.

## Rule 4 (Bear Floor): fails

Coverage on BKE is thin: as few as 2 Wall Street analysts actively rating the stock, and the most authoritative current read found is **UBS, Neutral, $47.00** (lowered from $52.00 in June 2026). Neutral is not Buy-rated and does not count toward Rule 4 by definition -- and even if it did, $47.00 sits below the Aug 21 $47.50C breakeven of $48.30. One aggregator mentioned an older "upgrade to Buy" from June 2, but no current, dated, Buy-rated target above any candidate breakeven was found anywhere in tonight's research. **There is no real bear floor here -- not a thin one, an absent one.**

## Rule 6 (Reachability): decisive fail at every expiry checked

Four real, verified earnings-day moves pulled from actual daily closes:
- **Aug 22, 2025:** +2.42%
- **Nov 21, 2025:** -1.29%
- **Mar 13, 2026:** -0.75%
- **May 29, 2026:** -9.13%

Median absolute move: **1.86%.** 1.5x cap: **2.78%.**

- Aug 21 $47.50C requirement: **+5.1%** -- 1.8x the cap.
- Sep 18 $45C requirement: **+5.2%** -- 1.9x the cap.
- Sep 18 $47.50C requirement: **+7.5%** -- 2.7x the cap.

This stock simply does not move enough on earnings for any strike in a realistic price band to clear the ceiling. Three of its last four prints moved under 2.5%; only one (the most recent, -9.1%) broke double digits, and that single outlier is what's propping the median up as high as it is.

## Verdict

Triple-killed: no real Rule 4 floor, Rule 6 fails by 1.8-2.7x at every expiry and strike checked, and the near-dated instrument carries the exact zero-buffer earnings-on-expiry structure that just cost the fund a clean entry on KR. Flagged hard, as instructed, not treated as a footnote.

## GLOSSARY

- **52-week range / percentile:** where the current price sits between the stock's low and high over the trailing year; 0% = at the low, 100% = at the high.
- **Rule 2 (confirmed catalyst):** the Iron Rule requiring a dated earnings event before the option's expiration.
- **Rule 4 (bear floor):** the lowest price target among Buy-rated analysts must sit above the option's breakeven.
- **Rule 5 (chain filter):** the cap on how much a single option contract can cost, currently locked at $1.00/share under the transitional rule.
- **Rule 6 (reachability):** the move required to reach breakeven must not exceed 1.5x the stock's median historical earnings-day reaction.
- **Zero-buffer earnings:** when a reported earnings date falls on or effectively on an option's own expiration date, leaving no trading session between the reaction and the contract's expiry -- the structural issue that put KR's Sep 4 2026 position at risk.
- **Neutral / Hold rating:** an analyst recommendation that does not count as either a Buy (for Rule 4 purposes) or a Sell/Underperform (for Rule 3 purposes).
