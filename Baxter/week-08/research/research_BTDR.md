# Research: BTDR (Bitdeer Technologies Group) -- Aug 8, 2026

**Verdict: ADVANCE. 4/5 conviction. Candidate: $11.00C Aug 14 2026, ask $0.85 (STRETCH -- near the top of the affordable band), breakeven $11.85.**

## Setup

- Price: $10.89 (Aug 7, 2026 close, the most recent settled session -- research run over the weekend)
- 52-week range: $6.92 - $27.80
- Percentile: **19th** -- bottom quartile
- Confirmed catalyst: **Q2 2026 earnings, Aug 10, 2026, AM**, `get_earnings_results` verified: true

## Earnings date re-verification (per the Aug 7, 2026 standing rule)

Pulled `get_earnings_results` first. Result: 2026-08-10, AM, **verified: true** (company-announced). Matches the date supplied at the start of tonight's run. Company's own earnings-call notice (found independently via web search) confirms the same date.

**Buffer check:** AM release Aug 10 (Monday) means the reaction prices in the same day. That leaves Aug 11, 12, 13, and 14 itself -- four full trading days before the Aug 14 expiry. Comfortable, not tight. No structural timing concern here, unlike QXO or BKE below.

## The Unified Screen

**Step 1 (Range percentile):** 19th percentile. Clears -- CALLS candidate.

**Step 2 (Rule 2 -- confirmed catalyst):** Aug 10, 2026 AM, verified true, 4 trading days ahead of the Aug 14 expiry. Clears with real room.

**Step 3 (Rule 3 -- ratings):** 10 analysts covering: consensus **Strong Buy**, 80% Strong Buy, 10% Buy, 10% Hold. No Sell/Underperform found in current coverage -- Keefe, Bruyette & Woods' $17 target carries a "Market Perform" (Hold-equivalent) rating, not a Sell. Clears clean.

## Rule 4 (Bear Floor)

Candidate instrument: **$11.00C Aug 14 2026, ask $0.85** ($85 at risk). Breakeven $11.85, needs **+8.8%** from $10.89.

Lowest fresh Buy-rated target found: **Needham (John Todaro), Buy, $22.00** -- raised from $19.00 in early August 2026, referencing an Aug 3 close of $11.37. This is inside the 60-day freshness window and moving in the bullish direction (a raise, not a cut) right into this earnings week. Separately, the stock gapped up Aug 6 on an analyst upgrade -- a second, independent bullish data point in the same window.

**Rule 4: PASSES with the largest margin of anything screened tonight.** $22.00 clears the $11.85 breakeven by **$10.15, an 85.7% cushion.**

## Rule 5 (Chain Filter)

$0.85/share, $85 at risk. Under the Tab 1 transitional-lock ceiling of $1.00/share, but at 85% of it -- correctly flagged STRETCH in the original screen. Passes, but with less room than UAMY.

## Rule 6 (Reachability)

Four real, verified earnings-day moves pulled from actual daily closes (not estimated):
- **Aug 18, 2025 (Q2 2025):** +7.24%
- **Nov 10, 2025 (Q3 2025):** -19.74%
- **Feb 12, 2026 (Q4 2025):** -13.51%
- **May 14, 2026 (Q1 2026):** +11.57%

Median absolute move: **12.54%.** 1.5x cap: **18.81%.** Current requirement: **+8.8%.**

**Rule 6: PASSES with real margin** -- required move uses 47% of the cap, on a stock whose earnings-day moves run genuinely large in both directions.

**Straddle cross-check:** live Aug 14 at-the-money straddle (the $11 call, mark $0.775, plus the $11 put, mark $0.95) prices **$1.725 of combined premium on a $10.89 stock -- a market-implied move of ~15.9%.** The options market is pricing nearly double the move this trade needs. Corroborates the historical read.

## Decline category

Category 1. BTDR is a bitcoin-mining and hosting infrastructure name; its price action tracks sector-wide crypto sentiment and BTC price swings more than company-specific news, which is exactly what the four real earnings-day moves above show (two double-digit drops, two solid gains, no consistent direction). H.C. Wainwright, in the same recent note that trimmed its target, explicitly characterized the prior earnings-driven selloff as "overdone" -- a sell-side shop calling its own sector's reaction excessive is close to a textbook Category 1 signal. **Real caveat, not a decline-category problem but a business-risk one:** BTDR's own fundamentals carry real volatility tied to Bitcoin price and hosting-contract economics (one data point found: a flagged concern about a potential 30% quarter-over-quarter revenue decline tied to BTC price pressure). That risk is priced into the position sizing and the defined-max-loss structure of an option, not into the decline-category test.

## Sizing

Conviction 4/5, high-confidence end of the tier given every rule cleared with real-to-large margin and the freshest, largest Rule 4 cushion of the batch: **16% of reserve** (top of the 12-16% band) on today's $1,054.96 reserve = **$168.79 nominal.**

Contracts = floor(sizing budget / (ask x 100)) = floor($168.79 / $85) = **1.** A second contract would cost $170, $1.21 over the ceiling -- the floor-division rule (Tab 3) leaves roughly $84 of the nominal budget undeployed by design, the same shape as KR's first draft. Total at risk: **$85**, single contract, not eligible for the scale-out ladder until reserve growth or a cheaper strike allows a second.

## THE FIVE BAXTERS

**BULLXTER:** Eighty-five point seven percent cushion, a target that just went up into earnings week, and a stock the sell side is calling an overdone selloff on its own. Zero Sell ratings, Strong Buy consensus at 80%. This is the strongest floor of anything screened tonight, full stop. I'd want a second contract if the ask were forty cents cheaper.

**BEARXTER:** Eighty-five cents on a Rule 5 ceiling of a dollar is not "fits comfortably," it's "fits." One bad tick in the ask before the order fills and this trade doesn't clear the screen at all. And I want the crypto-miner risk said out loud, not buried in a parenthetical: this business's own revenue can swing 30% quarter to quarter on Bitcoin price alone. The option's max loss is defined and that's the whole point of using options here, but "the underlying story is volatile" and "the underlying story is broken" are different sentences, and I want the room to hear both before anyone gets comfortable.

**CALXTER:** Required move 8.8%, cap 18.81% -- 47% of ceiling used, and the straddle cross-check independently prices a 15.9% implied move, nearly double the requirement. Two methods agree with real distance to spare. One honest gap: the four historical prints have real dispersion (-19.74% to +11.57%), so the median is a reasonable central estimate but not a tight one -- this stock's earnings reactions are large and variable, not small and consistent like UAMY's recent prints. The cap already accounts for that by scaling off the median itself; I'm not revising the number, just naming the character of the distribution underneath it.

**MACXTER:** Nothing sector-specific from filings or Truth Social this pass. The macro read that matters here is Bitcoin price and hosting-contract demand, which is a market signal Calxter and Bearxter are already pricing, not a political one. No flag.

**PRIME:** Verdict: four of five. $11.00C Aug 14 2026. Rule 4 cushion is the best of the batch at 85.7%, freshly reinforced by an Aug upgrade. Rule 6 clears with real margin, corroborated by a straddle pricing nearly 2x the required move. Bearxter's two flags (Rule 5 tightness, underlying business volatility) are real and are exactly why this sits at 4/5 with a single contract rather than pushing for more size. Sizing: 16% of $1,054.96, floor-divides to one contract, $85 at risk. Exit per Tab 4: sell the ramp if still OTM 24-48 hours before Aug 10, though the 4-day post-earnings buffer also leaves room to let the print itself do the work if the position is already working by Friday morning.

## The pitch

The best bear-floor cushion of the night (85.7%, freshly raised into earnings week), a Rule 6 requirement using under half its ceiling, and a sell-side note calling the stock's own recent selloff overdone. The trade-off is real and disclosed: this is the most expensive contract in the batch relative to the Rule 5 ceiling, and the underlying business carries genuine crypto-linked volatility that the option's defined max loss contains but doesn't erase.

## GLOSSARY

- **52-week range / percentile:** where the current price sits between the stock's low and high over the trailing year; 0% = at the low, 100% = at the high.
- **Rule 2 (confirmed catalyst):** the Iron Rule requiring a dated earnings event before the option's expiration.
- **Rule 3 (ratings):** for calls, near-zero analysts rating the stock Sell/Underperform.
- **Rule 4 (bear floor):** the lowest price target among Buy-rated analysts must sit above the option's breakeven.
- **Rule 5 (chain filter):** the cap on how much a single option contract can cost, currently locked at $1.00/share under the transitional rule pending the sweep-based unlock.
- **Rule 6 (reachability):** the move required to reach breakeven must not exceed 1.5x the stock's median historical earnings-day reaction.
- **Breakeven:** strike price plus premium paid per share -- where the option holder neither gains nor loses at expiration.
- **Decline category (Category 1 vs 2):** whether a stock's drop reflects a one-off market overreaction (tradeable) or real, ongoing business deterioration (not tradeable).
- **Straddle:** buying the at-the-money call and put together; its combined price divided by the stock price gives the options market's own implied move, an independent cross-check on Rule 6.
- **Hosting (bitcoin mining context):** a business line where the company runs mining hardware on behalf of third-party owners for a fee, distinct from mining with its own owned equipment.
- **STRETCH flag:** the fund's internal note for a contract whose ask sits close to the Rule 5 ceiling, meaning less room for the ask to move before the trade fails the screen.
