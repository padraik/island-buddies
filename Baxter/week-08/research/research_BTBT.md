# Research: BTBT (Bit Digital, Inc.) -- Aug 11, 2026

**Verdict: ADVANCE. 4/5 conviction. Candidate: $1.00C Aug 21 2026, ask $0.35 (confirm live before entry). 4 contracts, $140 at risk.**

## Setup

- Price: $1.31 (Aug 11, 2026)
- 52-week range: $1.18 - $4.55
- Percentile: **3.9th**, deep bottom quartile
- Confirmed catalyst: **Q2 FY2026 earnings, Aug 13, 2026, PM, `get_earnings_results` verified: true**
- Sourced via the scanner sweep run earlier tonight (`screening_log_aug11_scanner_sweep.md`), not hand-picked

## The Unified Screen

**Step 1 (Range percentile):** 3.9th percentile. Clears, CALLS candidate.

**Step 2 (Rule 2, confirmed catalyst):** Aug 13, 2026 PM, verified true. Reaction lands at Friday Aug 14's open. Aug 21 expiry gives 7 real trading days after the reaction before the contract dies -- real post-catalyst buffer, not a same-day squeeze.

**Step 3 (Rule 3, ratings):** 5 analysts, 5 Buy, 0 Hold, 0 Sell. Clears clean.

## Rule 4 (Bear Floor)

Candidate instrument: **$1.00C Aug 21 2026, ask $0.35** (confirmed live). Breakeven $1.35, needs **+3.1%** from $1.31.

Lowest Buy-rated target found and independently corroborated fresh tonight: **Craig-Hallum, $3.50, raised from $3.00 in late July 2026** -- specifically dated, specifically reasoned (calls BTBT "significantly undervalued relative to its 70% White Fiber stake," flags unrecognized ETH holdings on the balance sheet as hidden upside), and it's a raise, not a hold-steady, issued after the worst of the sector's Q1 pain was already known. Clears breakeven by $2.15, a 159% cushion. **Rule 4: passes, and passes clean** -- this is a real, fresh, reasoned floor, not a stale pre-decline number.

**Contrast with BTGO, screened alongside this name tonight and killed:** BTGO's only dated post-Q1-miss analyst action found was KBW holding Market Perform (Hold, not Buy) at $12 after the earnings miss. Every Buy-rated BTGO target locatable predates the Q1 miss and the securities class-action lawsuit filed against it. No fresh Buy-rated floor exists for BTGO under the binder's own freshness rule (Tab 6: "a bear floor is only as good as its publication date"). BTBT is the opposite case -- the freshest analyst action is a Buy-side raise, not a hold-steady or a downgrade. That asymmetry is most of the reason this is BTBT's pitch and not BTGO's.

## Rule 5 (Chain Filter)

$0.35/share, $35/contract. Conviction 4/5, tier 12-16% of reserve, 14% standard. On tonight's $1,056.96 reserve: nominal budget $147.97, ceiling $169.11. **4 contracts = $140**, inside both. 5 contracts ($175) would breach the ceiling. Multi-contract sizing also satisfies the Tab 4 scale-out ladder's 2+-contract preference.

**Chain note:** no liquid OTM strike above $1.00 was priced inside the script's $0.10-$1.00 display window at this or the next expiry -- the $1.00 strike itself is already slightly in the money (intrinsic $0.31 of the $0.35 ask, ~$0.04 extrinsic). This is a lower-convexity structure than the fund's usual deep-OTM setups, closer to a leveraged stock position than a lottery ticket. Lower blow-up risk, lower max payoff, same Rule 6 discipline underneath it.

**Straddle cross-check: not usable.** Attempted at the nearest strikes to spot ($1.00 call, $1.50 put) -- neither sits close enough to the $1.31 stock price to give a clean market-implied-move read; both carry too much intrinsic value contamination. Same failure mode as DQ's unusable straddle in the Aug 8 batch. Not treated as a red flag on its own, just a gap -- the historical Rule 6 read below is what this trade actually rests on.

## Rule 6 (Reachability)

Four real, verified earnings-day moves pulled from actual daily closes (not estimated), via `get_equity_historicals`:

- **Aug 14, 2025 (PM):** -5.64% (close $3.19 to next-day close $3.01)
- **Nov 14, 2025 (AM):** -4.37% (prior close $2.52 to $2.41)
- **Mar 31, 2026 (PM):** +5.34% (close $1.31 to next-day close $1.38)
- **May 14, 2026 (PM):** -15.26% (close $2.13 to next-day close $1.80)

Median absolute move: **5.49%.** 1.5x cap: **8.24%.** Current requirement: **+3.1%.**

**Rule 6: passes with real margin** -- the required move uses only 38% of the cap, on a full 4-quarter real sample (not a thin 2-print history like BTGO's).

## Decline category

**Category 1, sector-wide, with a real asset-recognition angle on top -- not a company-specific breakdown.** Bitcoin fell from its October 2025 all-time high near $126,300 to roughly $67,600, pushing the sector's all-in mining cost (~$84,300) above the current BTC price. This is squeezing every bitcoin miner's economics simultaneously, not a BTBT-specific failure. BTBT's own numbers are genuinely rough on the surface (Q1 2026: $27.9M revenue against a $146.7M net loss, EBIT margin near -316%), but Craig-Hallum's July raise argues the market is pricing BTBT as a pure, distressed BTC miner and ignoring two real assets underneath it: a 70% stake in White Fiber and unrecognized ETH holdings on the balance sheet. That is the textbook shape of a Category 1 dislocation -- the sector story is real and negative, but this specific name may have value the sector-wide selling isn't distinguishing.

**Real risk named directly:** if BTC keeps falling into the print, sector sentiment can drag BTBT down regardless of the White Fiber/ETH thesis being right on a 12-month view -- the option only cares about the next 10 days. Also worth flagging: the $146.7M net loss is large relative to a $27.9M revenue base, and no attempt was made tonight to separate how much of that is BTC mark-to-market versus real cash operating loss. That gap is real, not fatal at this conviction level, but it's why this sits at 4/5 rather than 5/5.

## Sizing

Conviction 4/5: 12-16% of reserve, 14% standard. On tonight's $1,056.96 reserve: nominal budget $147.97, ceiling $169.11. At the live $0.35/share ask ($35/contract): **4 contracts = $140** (13.2% of reserve), inside the nominal band and the ceiling. Confirm the live ask again immediately before any fill -- BTBT is thin enough that the quote can move between research and execution.

## THE FIVE BAXTERS

**BULLXTER:** Sector's getting killed and this name has an actual reason to be different from the rest of the miners: a 70% stake in something else entirely, plus ETH sitting on the books nobody's pricing. Craig-Hallum said it in writing three weeks ago, after the worst of the news was already out, not before it. Five analysts, zero Sell ratings, target more than double the stock. I'd size toward the ceiling, not sit at the standard 14%.

**BEARXTER:** Say the loss number plainly: $146.7 million against $27.9 million of revenue is not a rounding error, and nobody separated tonight how much of that is BTC mark-to-market noise versus a real cash burn problem. That gap should have been closed before this went to a pitch, and it wasn't -- flagging it as unfinished, not disqualifying. Also: this is a thin, low-priced name with sparse strike spacing. The straddle didn't work. I don't have an independent forward-looking check on the historical Rule 6 read, only the backward-looking one. Capping this at 4, not 5, until that loss breakdown gets done.

**CALXTER:** The math: needed move 3.1% against a 1.5x cap of 8.24%, built off four real quarters with a genuine median of 5.49%, not a cherry-picked one. That's 38% of the cap used, healthy. What I can't give the room tonight is a forward-looking implied-move number -- the straddle attempt failed on strike spacing, so this trade is resting entirely on the backward-looking historical read. That's a real, not a fatal, gap. Flag it and move on.

**MACXTER:** Nothing regulatory or political in play here specific to BTBT. The macro signal that matters is BTC's own price action into Friday -- this name's beta to the coin is high regardless of the White Fiber thesis, and I don't have a read on where BTC itself is trending into the print. Worth a same-day gut check before entry, not just a research-time snapshot.

**PRIME:** Verdict: four of five. $1.00C Aug 21 2026, ask $0.35 confirmed live at research time, confirm again before any fill. Rule 6 passes with real margin on a real four-quarter sample. Rule 4 clears with a fresh, dated, reasoned floor -- the exact opposite of what killed BTGO tonight. The two open items, Bearxter's loss-breakdown gap and Calxter's missing forward-looking check, are real and undone, not blocking. **Sizing: 4 contracts, $140 at risk, 13.2% of the $1,056.96 reserve.** Exit per Tab 4 default: sell the pre-print ramp 24-48 hours ahead of Thursday's PM release, don't hold through it, no binary-hold exception was earned here.

## The pitch

Sector-wide bitcoin miner selloff took every name in the space down together, and this is the one screening survivor tonight with a specific, dated, reasoned argument that the market's mispricing it worse than its peers: a real stake in another business plus real crypto holdings the stock price isn't reflecting, according to an analyst who raised the target *after* the bad news, not before it. Clean ratings, real Rule 6 margin on a full real sample, a floor with more than double the cushion of breakeven. The catch: this rests entirely on backward-looking history since the straddle didn't work, and nobody's pulled apart how much of the reported loss is real cash burn versus BTC accounting noise. Four out of five, not five, and worth the ask.

## GLOSSARY

- **52-week range / percentile:** where the current price sits between the stock's low and high over the trailing year; 0% = at the low, 100% = at the high.
- **Rule 2 (confirmed catalyst):** the Iron Rule requiring a dated earnings event before the option's expiration.
- **Rule 3 (ratings):** for calls, near-zero analysts rating the stock Sell/Underperform.
- **Rule 4 (bear floor):** the lowest price target among Buy-rated analysts must sit above the option's breakeven, and that target must be dated within 60 days and published after the stock's decline to count.
- **Rule 5 (chain filter):** the cap on how much a single option contract can cost, scaled to the fund's reserve and conviction tier.
- **Rule 6 (reachability):** the move required to reach breakeven must not exceed 1.5x the stock's median historical earnings-day reaction.
- **Breakeven:** strike price plus premium paid per share, where the option holder neither gains nor loses at expiration.
- **Decline category (Category 1 vs 2):** whether a stock's drop reflects a one-off market overreaction or sector-wide dislocation (tradeable) or real, ongoing company-specific deterioration (not tradeable).
- **Sell the ramp:** the fund's default exit, selling an OTM position into the elevated implied-volatility premium 24-48 hours before earnings, rather than holding through the reaction.
- **Straddle:** buying the at-the-money call and put together; its combined price divided by the stock price gives the market's own implied move for the event. Unusable here due to sparse strike spacing around the stock price.
- **AM/PM release:** whether a company reports before market open (reaction prices in same day) or after market close (reaction prices in at the next day's open).
- **`verified` flag:** on `get_earnings_results`, true means the date is company-announced; false means it is estimated from reporting cadence.
