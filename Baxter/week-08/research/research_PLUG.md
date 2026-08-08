# Research: PLUG (Plug Power Inc.) -- Aug 8, 2026

**Verdict: KILL (Rule 3, decisive). Neither candidate strike reopens it. Not queued.**

## Setup

- Price: $2.19 (Aug 7, 2026 close, up 5.8% same session from $2.07)
- 52-week range: $1.41 - $4.58
- Percentile: **25th** -- right at the edge of bottom-quartile, CALLS candidate on Step 1
- Confirmed catalyst: **Q2 2026 earnings, Aug 10, 2026, PM**, `get_earnings_results` verified: true

## Earnings date note (worth recording even though it doesn't change the verdict)

One web search tonight returned "Aug 12, before market open" for PLUG's next print -- directly contradicting the Robinhood-verified Aug 10 PM date. A second, independent search (MarketScreener, citing the company's own release) confirmed Aug 10. This is exactly the aggregator-echo failure mode the binder's Aug 7 standing rule was written to catch: `get_earnings_results` returned verified: true and was right; the WebSearch aggregator was stale and was wrong. Recorded as a clean real-world validation of the rule, not a problem with this trade.

## The Unified Screen

**Step 1:** 25th percentile, right at the boundary but still clears. **Step 2:** Aug 10 PM, verified true, 4 days ahead of the Aug 14 expiry -- clears, tight but real.

**Step 3 (Rule 3 -- ratings): FAILS.** BMO Capital Markets carries an explicit **Underperform** rating with a $1.00 target (reaffirmed Mar 3, 2026). Broader coverage breakdowns found tonight show as many as 3 Sell-class ratings among the analysts covering the stock, against a maximum of 1 allowed. The average rating across the full analyst pool is "Hold," not "Buy" -- a materially weaker consensus than every other name advanced tonight.

## Why the strike choice doesn't matter here

The brief flagged two real candidates at the same Aug 14 expiry: the $1.50 strike (deep ITM, ask $0.73, essentially pure intrinsic value with almost no time premium) and the $2.00 strike (ask $0.28, breakeven $2.28). Both were checked on today's math for completeness:

- **$2.00C:** breakeven $2.28, needs **+4.1%** from the live $2.19 (up from the ~2.2% figure quoted at the start of tonight's run -- the stock's own 5.8% rally today ate most of the cushion between last night's price check and now, the same kind of live-price drift that thinned KR's entry margin). Rule 6: four real prints (Aug 11 '25 -2.53%, Nov 10 '25 -1.17%, Mar 2 '26 +23.20%, May 11 '26 +1.14%) give a median absolute move of 1.85%, cap 2.78%. **Required 4.1% exceeds the cap** -- fails Rule 6 too, independently of Rule 3.
- **$1.50C:** breakeven $2.23, needs only +1.8% -- passes Rule 6, but for the wrong reason. At $0.73 ask against $0.69 of intrinsic value, this contract carries roughly $0.04 of time premium. It isn't really a bet on the earnings catalyst; it's a leveraged-but-barely stock proxy with almost no optionality left to price in the event. Economically weak, exactly as flagged going in.

Neither strike needs to be relitigated further, because **Rule 3 kills the underlying regardless of which strike is chosen.** A professional analyst community with an active Underperform call and multiple Sell-class ratings is not the "near-zero Sell" consensus the calls thesis requires.

## Decline category

Not reached. Rule 3 is a hard gate ahead of Rule 4/5/6 in the fund's own screen order, and it fails outright here.

## What would reopen this

A clean rating shift -- BMO or another Sell/Underperform shop moving off its bearish call, bringing the covering universe back under the 1-Sell ceiling. Nothing in tonight's research suggests that's imminent; the average consensus rating (Hold) reflects genuine, current disagreement about the business, not a stale outlier.

## GLOSSARY

- **52-week range / percentile:** where the current price sits between the stock's low and high over the trailing year; 0% = at the low, 100% = at the high.
- **Rule 3 (ratings):** for calls, the requirement that near-zero analysts rate the stock Sell/Underperform -- a proxy for whether professional consensus still backs the business.
- **Rule 6 (reachability):** the move required to reach breakeven must not exceed 1.5x the stock's median historical earnings-day reaction.
- **Deep ITM (in the money):** an option whose strike is well past the current stock price in the profitable direction, so its price is made up mostly of intrinsic value rather than time value tied to the catalyst.
- **Time premium / extrinsic value:** the portion of an option's price beyond its intrinsic value, reflecting the market's expectation of future movement before expiration.
- **Underperform / Sell rating:** an analyst's formal recommendation that a stock will underperform its sector or the market -- the rating class Rule 3 caps at a maximum of one.
