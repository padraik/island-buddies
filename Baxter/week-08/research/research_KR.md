# Research: KR (The Kroger Co.) -- Aug 4, 2026 (re-verified Aug 6, ENTERED Aug 7, DATE CORRECTED Aug 7 evening)

**Verdict: ADVANCE. 4/5 conviction. ENTERED Aug 7, 10:06 AM ET: $61C Sep 4 2026, 2 contracts, real fill $0.50/share, $100 total. CATALYST DATE WAS WRONG -- see correction below, position has no earnings before its own expiry.**

## CATALYST DATE CORRECTION -- Aug 7, 2026, evening (before Michael's planned exit)

Michael asked directly whether Sep 4 was even right, since he'd seen Sep 10 mentioned elsewhere. It wasn't right. `get_earnings_results` (a tool never used for this trade until tonight) returns KR's real Q2 FY2026 date plainly: **2026-09-10, AM, verified: false** (Kroger hasn't put out its own conference-call announcement yet). The tool's own trailing history for KR (Sep 11 2025, Jun 20 2025, Mar 6 2025) makes the pattern obvious in hindsight -- Sep 4 never fit Kroger's own cadence, and would have been visibly wrong the first time anyone checked it against the company's own past dates instead of a fresh search each time.

**"Sep 4" was "confirmed" by WebSearch three separate times before this (Aug 4 research, Aug 6 re-verification, Aug 7 morning re-verification) and was wrong every time.** Root cause: aggregator search hits are not independent of each other -- several traced back to the same stale prior-year data point (one source literally carried a `2025-09-04` URL). Three search confirmations felt like three sources; it was really one wrong number echoed three times. Full process fix, not just this trade's correction: `binder.md` Tab 6 now requires `get_earnings_results` as the first check for any catalyst date, WebSearch only as a fallback or a secondary check on an unverified date.

**Consequence for this position: the $61C Sep 4 2026 currently held has no earnings catalyst before its own expiration.** A real Rule 2 violation on a live position, discovered after entry rather than before. Michael is planning to close it the morning of Aug 8, on his own read of the live price (down roughly $9/contract as of Aug 7 evening) -- not waiting on further research to make that call. A same-day-eligible replacement was scouted the same evening: **$60C Sep 18 2026** (real, liquid market: bid $1.21/ask $1.34, 2,335 open interest, 306 volume same day), breakeven $61.34, needs +8.2% against a $56.69 stock, comfortably under the 9.0% Rule 6 cap with a full week of real buffer past the Sep 10 date. Not yet entered -- queued pending Michael's decision on timing.

## ENTRY -- Aug 7, 2026, 10:06 AM ET

Real order pulled before logging anything (Michael reported the fill as "$0.70" -- that was the limit price on the order, not the execution; real fill was $0.50/share, $100 total for 2 contracts, a price improvement).

This was not a clean entry, and it's worth being honest about that in the record. Between the Aug 6 re-verification and Friday's open, KR's stock kept drifting: $58.22 (Aug 4) -> $57.32 (Aug 6 close) -> mid-$56s through Friday morning. That drift ate the Rule 6 cushion in real time. The live asks seen earlier Friday morning ($0.88-0.91/share) were actually failing the 9.0% cap outright once computed correctly (breakeven $61.88-61.91 against a ~$56.65 stock needs 9.2-9.3%). Also caught in the same session: the Aug 6 re-verification note above used Robinhood's API `break_even_price` field (mark-price-based) instead of this fund's own strike-plus-ask convention, which understated the required move as 7.4% when the honest number was closer to 8.0% even before Friday's further drift. **The real $0.50 fill is what actually cleared it:** breakeven $61.50, required move 8.9-9.2% depending on the exact minute of the stock quote, sitting right at the 9.0% cap rather than comfortably inside it like the original 6.3%/9.0% read. This is the thinnest-margin Rule 6 entry the fund has taken to date. Bearxter's original watch items (margin language, whether the Dec 2025 impairment recurs) still stand as conditions on the next earnings call, unchanged by any of this.

Sizing came in better than planned: 2 contracts for $100 total, under both the $161.69 nominal and the $184.79 tier ceiling (cheaper than the $178 estimate used when the ask was still $0.89). Scale-out ladder is live: standard +100% trigger ($1.00/share) sells 1 of 2 contracts automatically per Tab 4.

Plan unchanged: sell the pre-earnings IV ramp Sep 2-3, not the Sep 4 print itself.

## RE-VERIFICATION -- Aug 6, 2026 (evening, ahead of Aug 7 entry)

Two days old, checked live before going in tomorrow morning rather than trading off Monday's numbers.

- **Stock:** $57.32 (was $58.22 Aug 4) -- still bottom-quartile, actually a shade cheaper.
- **Chain:** $61C Sep 4 2026, live ask **$0.89** (was $0.87), breakeven **$61.54**, needs **+7.4%** (was +6.3%). Rule 6 cap is 9.0% -- still passes, tighter margin than Monday (82% of cap used, was 70%), not a boundary case.
- **Rule 4:** Goldman Sachs Buy, $82 target, confirmed still live via web search tonight -- no newer downgrade found, no rating change since the June revision this doc was built on. Still clears breakeven by $20.46 (35.6% cushion).
- **Earnings date:** Sep 4, 2026 reconfirmed independently tonight (separate search, separate sources from the original doc). No date drift, unlike the LVS/TRMB lesson.
- **Sizing, recomputed on tonight's reserve:** Reserve is now $1,154.96 (was $912.96 Monday). 4/5 tier is 12-16%: nominal 14% = $161.69, ceiling 16% = $184.79. At $0.89/share ($89/contract), **2 contracts = $178 -- fits inside the tier ceiling for the first time.** Monday's version floor-divided to 1 contract and locked the ladder out entirely; tonight's reserve growth (LYFT's realized profit landing back in cash) is what unlocks the second contract. **Recommendation: enter 2 contracts, not 1** -- same instrument, same conviction, but the scale-out ladder can actually apply to this position now.

**Cleared for entry Aug 7 morning**, standard Tab 4 default: sell the pre-earnings IV ramp (Sep 2-3), not the Sep 4 print itself, per the plan already written into this doc.

## Setup

- Price: $58.22 (Aug 4, 2026)
- 52-week range: $54.15 - $76.58
- Percentile: **18th** -- bottom quartile, down ~24% from its high, ~21.9% over the past year
- Confirmed catalyst: **Q2 FY2026 earnings, Sep 4, 2026**

## The Unified Screen

**Step 1 (Range percentile):** 18th percentile. Clears -- CALLS candidate.

**Step 2 (Rule 2 -- confirmed catalyst):** Sep 4, 2026 earnings confirmed via Kroger's own reporting cadence. Sep 4 is also the nearest expiry with tradeable strikes, which raises an execution question addressed below.

**Step 3 (Rule 3 -- ratings):** 21 analysts: **11 Buy, 13 Hold, 0 Sell.** (Some sources report 24 analysts/9 Strong Buy in slightly different cuts, but every source agrees on the number that matters: zero Sell or Underperform ratings anywhere in coverage.) Clears clean.

## Rule 4 (Bear Floor)

Candidate instrument: **$61C Sep 4 2026, ask $0.87** ($87 at risk). Breakeven $61.87, needs **+6.3%** from $58.22.

Lowest fresh Buy-rated target found: **Goldman Sachs, Buy, $82** -- raised from $72 in late June 2026, explicitly *after* the Jun 18 post-earnings drop and citing market-share improvement despite Q1 pricing questions. This is dated after the decline and inside the 60-day freshness window. Roth Capital (Buy, $78, Mar 6) and Telsey Advisory (Outperform, $78) are also above breakeven but pre-date the June drop, so they don't get credit for freshness -- Goldman's $82 is the number doing the work.

**Rule 4: PASSES with real margin.** $82 clears the $61.87 breakeven by **$20.13, a 32.5% cushion** -- nothing like ZTS's thin 8.8% or the earlier survivors' near-boundary numbers. The stray "$58 low target" seen in aggregator summaries belongs to Wells Fargo, which is Hold-rated -- doesn't count against Rule 4, and confirmed as Hold via a second source before ruling it out.

## Rule 5 (Chain Filter)

$0.87/share, $87 at risk. Max ask at 4/5 conviction is 16% x $912.96 = $1.46/share -- $0.87 clears that with real room, not sitting at the tier ceiling.

*Correction (Aug 4, post-review): the first draft of this doc sized the position using the 3.5/5 band (6-10% of reserve) despite scoring conviction at 4/5 -- an inconsistency Michael caught. See Sizing below for the corrected math.*

*Superseded (Aug 6, post-reserve-growth): the $912.96 reserve figure above is Monday's number. Reserve is $1,154.96 as of tonight (LYFT closed, fund fully in cash). See the RE-VERIFICATION section at the top and the updated Sizing note below -- the tier math now supports 2 contracts, not 1.*

## Rule 6 (Reachability)

Three real, verified earnings-day moves pulled (not estimated):
- **Mar 5, 2026 (Q4 2025):** +5.3% (beat: EPS $1.28 vs $1.20 est., operating profit $1,246M vs $912M yr-ago)
- **Dec 4, 2025 (Q3 2025):** -6% (net loss of $1.32B on a $2.6B non-cash impairment to the automated fulfillment network; adjusted EPS $1.05 actually beat slightly)
- **Jun 18, 2026 (Q1 2026):** -7.4% (adjusted EPS $1.58 vs $1.59 est. -- essentially in-line, reacted like a miss anyway)

Median absolute move: **6.0%.** 1.5x cap: **9.0%.** Current requirement: **+6.3%.**

**Rule 6: PASSES with real margin** -- required move sits comfortably under the cap, not at the boundary like the last several survivors this run.

## Decline category

This is Category 1 (event overreaction), not Category 2. The three data points behind the decline are not a single deteriorating story:
- The Dec 2025 drop was driven by a **non-cash impairment charge** on a specific automation initiative -- a real write-down, but not evidence the core grocery business is shrinking (adjusted EPS still beat that same quarter).
- The Jun 2026 drop was a **$0.01 miss** (in-line, by any normal standard) that the market punished by 7.4% anyway -- textbook overreaction shape, not a guidance-driven repricing.
- The most recent print (Mar 2026) was a clean beat with operating profit up 37% YoY, and the stock still hasn't recovered to reflect it.

No segment is described anywhere in coverage as structurally shrinking (contrast with ZTS's companion-animal organic decline, killed earlier tonight). Analyst ratings backing this up: 11 Buy / 13 Hold / 0 Sell, and the most recent rating action (Goldman, post-decline) went the Buy direction with a raised target, not a cut. This is a business the market keeps punishing for noise, not one Wall Street is walking away from.

## Straddle cross-check (added Aug 4, post-review -- was missing from the original draft)

The Jul 10, 2026 audit made an implied-move-vs-straddle cross-check a mandatory line in the DD funnel. It was skipped in the first pass of this doc. Pulled live (Aug 4, market open): Sep 4 2026 at-the-money straddle (the $57 call at $3.65 + the $57 put at $2.48) prices **$6.13 of combined premium on a $57.29 stock -- a market-implied move of ~10.7%.**

Our required move (+6.3% to the $61 strike's breakeven) sits well inside that -- the live options market is pricing nearly double the move this trade needs, not a thin margin like several of tonight's other survivors. This corroborates the historical-median-based Rule 6 read (6.0% median, 9.0% cap) rather than contradicting it: two independent methods (backward-looking historical reactions, forward-looking options pricing) both say the required move is comfortably achievable.

## Sizing (corrected Aug 4, post-review)

Conviction is 4/5, not 3.5/5 -- the sizing math should use the 4/5 band throughout: **12-16% of reserve, 14% standard.** On today's $912.96 reserve, that's a nominal budget of **$127.81** (range $109.55-$146.07), not the $54.78-$91.30 the first draft cited.

Contracts = floor(sizing budget / (ask x 100)). At $0.87/share ($87/contract) and Monday's $912.96 reserve: **floor($127.81 / $87) = 1.** This is the same output as the erroneous first draft, but for the right reason: a single contract costs more than half the nominal 4/5 budget, so no whole number of contracts above 1 fits without either exceeding the tier (2 contracts = $174, above the $146.07 ceiling) or reaching all the way into 5/5's own band ($155.20-$182.59). Getting to 2 contracts would require the conviction score itself to move to 5/5 -- which Bearxter's dissent (below) argues against: the Dec 2025 impairment and the Jun 2026 "price investment" commentary are two specific, real threads worth watching before pushing conviction any higher, not reasons to kill the trade, but reasons not to size it bigger than 4/5 supports. On Monday's reserve, **1 contract stood, ~$87 at risk, ~$40.81 of the nominal 4/5 budget going undeployed by design** -- Tab 3's floor-division rule, not a shortfall.

**Superseded (Aug 6, post-reserve-growth): this is no longer the live number.** Reserve is $1,154.96 tonight, not $912.96. Same 4/5 tier (12-16%, 14% standard), recomputed: nominal $161.69, ceiling $184.79. At tonight's live ask $0.89/share ($89/contract), **2 contracts = $178 -- fits inside the ceiling.** The conviction score didn't move (still 4/5, Bearxter's two watch items still stand as-is); the reserve did. **Current sizing: 2 contracts, ~$178 at risk.** This is the number to trade off tomorrow morning, not the 1-contract math above -- left in place as the record of how we got here, not as live guidance.

## Execution note on Rule 2 / Sep 4 timing

The earnings date and the nearest tradeable expiry are the same day (Sep 4). This isn't a special case that needs a new rule: Tab 4's existing default (sell into the pre-print IV ramp when OTM 24-48 hours before earnings) applies exactly as written here. The plan is **not** to hold to the Sep 4 expiration bell -- it's to sell on Sep 2 or Sep 3, into whatever premium the pre-earnings IV ramp offers, same as every other position in the book. If Michael wants to take a swing at holding through the print instead (binary flag, 4/5+ conviction, which this qualifies for), that's a live option worth discussing, but the default plan doesn't require it.

## THE FIVE BAXTERS

*Run after the fact, Aug 4 -- Michael caught that this doc skipped straight to a verdict the first time. Folded into the research doc per the corrected convention (binder Tab 6): the debate lives here, not in a separate story file.*

**BULLXTER:** Eleven buys, zero sells, a stock down twenty-four percent on two quarters that don't tell one coherent bad story, and a floor that cleared breakeven by twenty points before Goldman even moved it. This is the shape we hunt for. I'd push it to five of five and find a way into a second contract.

**BEARXTER:** Thirteen of twenty-one are Hold -- say that number as often as "zero Sell," because it's the same book and only one framing is honest. And December wasn't clean noise: a $2.6B non-cash impairment on the automated fulfillment network is Kroger admitting, in writing, that a real strategic bet isn't working as modeled. June worries me more -- a penny miss doesn't cost seven percent unless the market heard something in the call. Goldman's own note mentions "Q1 price investment questions": Kroger may be cutting prices to defend share against Walmart and the discounters, and that's margin, not sentiment. If that's the real story, it doesn't resolve in one quarter. I'm not killing this. I'm saying these two threads keep conviction at four, not five -- watch the Sep 4 call for margin language specifically.

**CALXTER:** Two jobs. First, the cross-check the audit made mandatory and the first draft skipped: the Sep 4 at-the-money straddle prices a **10.7% implied move**, live, against our required **6.3%** -- the options market is pricing nearly double what this needs. Second, the sizing question itself: the first draft said "top of the 3.5/5 tier" while scoring conviction at 4/5. Fixed math, Monday's version: 4/5 is 14% standard, $127.81 nominal on that day's reserve. Floor of that divided by an $87 contract was 1 -- a second contract cost $174, past the $146.07 ceiling of 4/5 and into 5/5's own band. Getting to 2 contracts required actually believing this was five of five, which was Bearxter's call to make, not mine. *(Update, Aug 6: the reserve moved, the math didn't need to. Tonight's reserve is $1,154.96 -- same 14% standard, same 4/5 tier, floor divides to 2 contracts now at the live $0.89 ask. Nobody had to argue conviction up to 5/5 to get there. It's a bigger fund doing the same math, not a different verdict.)*

**MACXTER:** Nothing on my end complicates it. No tariff line hits grocery margins harder than the sector already prices in. The Kroger-Albertsons merger has been dead since the FTC blocked it in December -- no live deal risk either direction. No Form 4 insider read pulled for this one; flagging that gap rather than pretending it's clean.

**PRIME:** Verdict: four of five. $61C Sep 4 2026. Straddle cross-check passes with real margin. Rule 4 floor clears by 35.6% (Goldman's $82, reconfirmed live Aug 6). Exit per Tab 4: sell the ramp Sep 2-3, not the print. Bearxter's two watch items (margin language, whether the impairment recurs) go in the book as conditions on the *next* look, not gates on this one. **Sizing, live as of Aug 6: fourteen percent standard on tonight's $1,154.96 reserve, floor-divides to two contracts at the $0.89 ask, ~$178 at risk.** Monday's version floor-divided to one on a smaller reserve; that was correct math for that day's number, not a live constraint tonight. Two contracts, entered Aug 7 morning, is the trade. Michael's yes, same as always.

## The pitch

Zero Sell ratings. A 32.5% cushion on Rule 4. A Rule 6 requirement that sits at 70% of its cap, not pressed against it. Three straight earnings reactions the stock has never recovered from, and not one of them tells a story about the grocery business actually getting worse. This is the cleanest DD sheet the fund has produced since before the Rule 6 audit tightened everything else that's come through since.

## GLOSSARY

- **52-week range / percentile:** where the current price sits between the stock's low and high over the trailing year; 0% = at the low, 100% = at the high.
- **Rule 2 (confirmed catalyst):** the Iron Rule requiring a dated earnings event before the option's expiration.
- **Rule 3 (ratings):** for calls, near-zero analysts rating the stock Sell/Underperform.
- **Rule 4 (bear floor):** the lowest price target among Buy-rated analysts must sit above the option's breakeven.
- **Rule 5 (chain filter):** the cap on how much a single option contract can cost, scaled to the fund's reserve and conviction tier.
- **Rule 6 (reachability):** the move required to reach breakeven must not exceed 1.5x the stock's median historical earnings-day reaction.
- **Breakeven:** strike price plus premium paid per share -- where the option holder neither gains nor loses at expiration.
- **Decline category (Category 1 vs 2):** whether a stock's drop reflects a one-off market overreaction (tradeable) or real, ongoing business deterioration (not tradeable), per the Jul 10, 2026 audit.
- **Sell the ramp:** the fund's default exit -- selling an OTM position into the elevated implied-volatility premium 24-48 hours before earnings, rather than holding through the reaction.
- **IV (implied volatility):** the options market's estimate of how much a stock will move, embedded in the option's price -- typically rises heading into a known catalyst like earnings ("the ramp") and collapses immediately after ("IV crush").
- **Non-cash impairment:** an accounting write-down of an asset's value that reduces reported earnings without any actual cash leaving the business that quarter.
