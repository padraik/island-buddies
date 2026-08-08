# Research: DQ (Daqo New Energy Corp.), Aug 7 to 8, 2026

**Verdict: KILL / hold at low conviction (approximately 2.5/5). Rule 6 marginal pass undercut by thin coverage, thin chain liquidity, and a one-day earnings buffer. Not queued.**

## Setup

- Price: $14.74 (Aug 7, 2026 close, live re-verified)
- 52-week range: $11.38 to $36.59
- Percentile: 13.2nd, bottom quartile
- The stock ran from $13.55 (Aug 6 close) to $14.74 (Aug 7 close), a same-week move of about +8.8%, with no DQ-specific news found in search beyond the Aug 20 earnings-date announcement. Reads as sector or momentum noise around Chinese polysilicon names rather than a DQ-specific catalyst, but it narrows the practical margin below relative to a read taken a few days earlier.

## Earnings-date check

`get_earnings_results` returns **2026-08-20, AM, verified: true.** A WebSearch (Stocktitan, citing Daqo's own release) independently confirms the same date and timing: results before market open Thursday, August 20, 2026, conference call 8:00 AM ET. No date discrepancy here, matches the pre-screen exactly.

## The Unified Screen

**Step 1 (Range percentile):** 13.2nd percentile. Clears: CALLS candidate.

**Step 2 (Rule 2):** Confirmed above. Expiry is Aug 21, 2026, one trading day after an AM release: the tightest buffer of tonight's six names next to HIVE's structural problem, but at least a real one-day window exists here.

**Step 3 (Rule 3, ratings):** Coverage is thin, only about 3 analysts found across sources, with a mixed and even contradictory consensus: one source cites a 3-analyst Buy consensus, another cites a 3-analyst Hold consensus (as of Apr 3, 2026), and the single most recent individual rating found is a Hold at a $25 target. No Sell/Underperform rating was identified anywhere, so Rule 3's letter (max 1 Sell) technically clears. But with coverage this thin, Rule 3 is not doing the job it is designed to do: three analysts, disagreeing with each other about Buy versus Hold, is not the kind of "credentialed professionals broadly endorse this" signal the rule exists to capture.

## Rule 4 (Bear Floor)

Price targets found across sources ranged from $25 to $37 (average cited around $32.50, one low-end figure of $30, another aggregator's low end at $25). All of these, if Buy-rated and fresh, would clear the $16.40 breakeven by a wide margin. But given the thin, contradictory coverage above, a specific dated, post-decline, Buy-rated target could not be pinned down with confidence in the time available. Flagging this as **unresolved rather than a clean pass**: the KR lesson here is not to write down a number that looks reassuring without checking it holds up.

## Rule 5 (Chain Filter)

Candidate instrument: **$16.00C Aug 21 2026, ask $0.40, bid $0.05** (live re-verified, matches the pre-screen exactly). At $0.40/share, $40 at risk, this fits easily inside even the 3.5/5 sizing tier on the current $1,054.96 reserve. Affordability is not the problem.

The bid/ask spread is the problem: a $0.05 bid against a $0.40 ask is an 8x spread. Open interest is 70, volume today 124, so the contract is real and has traded, but a market order to exit would likely fill far closer to the bid than the ask, which eats materially into whatever margin Rule 6 provides. This is exactly the "worth a hard look at real liquidity" flag the pre-screen raised, and it holds up under a closer look: real, but thin.

## Rule 6 (Reachability)

Breakeven $16.40. Needed move from $14.74: **+11.26%.**

Four real, verified earnings-day reactions (all AM releases, same-session reaction):
- Aug 26, 2025: close $23.90 to $23.72, -0.75%
- Oct 27, 2025: close $26.03 to $29.69, +14.06%
- Feb 26, 2026: close $25.10 to $23.95, -4.58%
- Apr 29, 2026: close $21.95 to $19.35, -11.85%

Median absolute move: **8.21%.** 1.5x cap: **12.32%.**

**Rule 6: marginal pass.** The required move (11.26%) uses about **91% of the cap**, the tightest pass of tonight's six names (versus GAP's 79% and ENVX's 42%). DQ's earnings-day moves are genuinely large and volatile (one print moved it over 14%), which is what makes the pass possible at all, but there is very little room for the stock to drift against the position before entry the way KR's did on Aug 7.

## Straddle cross-check

Attempted at the $15 strike (nearest to the $14.74 spot). The result is not usable: the $15 call shows **bid $0.00 (size 0), ask $0.60**, essentially no real two-sided market. The $15 put shows bid $0.65 / ask $1.50, itself a wide spread. A straddle computed off these numbers would range anywhere from roughly 9% to 14% implied move depending on which side is trusted, too wide to corroborate or contradict Rule 6 meaningfully. Recording this as its own finding: **the near-the-money DQ chain is too illiquid for a trustworthy straddle read**, a second, independent liquidity flag alongside the $16 strike's wide spread above.

## Decline category

Hard to classify cleanly. DQ is a Chinese polysilicon and solar-wafer producer whose stock trades heavily on Chinese solar-sector supply policy headlines (production curbs, "anti-involution" consolidation narratives) as much as on its own quarterly numbers, which is consistent with the wild swing between +14.06% and -11.85% in consecutive quarters. That pattern looks more like a policy-headline-driven trading vehicle than either a clean Category 1 overreaction or a clean Category 2 structural decline. With only 3 analysts covering the name, there is not enough professional signal to lean on for a confident read either way.

## Why this is a kill despite no single hard rule failure

Every individual factor here is defensible on its own (Rule 6 technically passes, Rule 3's letter technically clears, the chain is technically affordable), but they are all sitting at the edge rather than with margin: Rule 6 at 91% of its cap, Rule 3 built on only 3 disagreeing analysts, Rule 4 unresolved, the chain thin on both strikes checked, and only a one-day earnings buffer. Stacking five marginal factors is a different risk profile than one clean pass with real margin, which is what KR's Goldman-backed 32.5% Rule 4 cushion and 70%-of-cap Rule 6 looked like. This does not clear the bar for a real pitch tonight.

## GLOSSARY

- **52-week range / percentile:** where the current price sits between the stock's low and high over the trailing year; 0% equals the low, 100% equals the high.
- **Rule 2 (confirmed catalyst):** the Iron Rule requiring a dated earnings event before the option's expiration, verified via `get_earnings_results` first.
- **Rule 3 (ratings):** for calls, the requirement that near-zero analysts rate the stock Sell/Underperform.
- **Rule 4 (bear floor):** the lowest price target among Buy-rated analysts must sit above the option's breakeven.
- **Rule 5 (chain filter):** the cap on how much a single option contract can cost, scaled to the fund's reserve and conviction tier.
- **Rule 6 (reachability):** the move required to reach breakeven must not exceed 1.5x the stock's median historical earnings-day reaction, checked against real price bars.
- **Breakeven:** strike price plus premium paid per share, the price at which the option holder neither gains nor loses at expiration.
- **Straddle:** buying the at-the-money call and put together; its combined premium divided by the stock price gives the options market's own implied move for the period, a forward-looking cross-check against the backward-looking Rule 6 median.
- **Bid/ask spread:** the gap between what buyers will pay and sellers will accept; a wide spread relative to the price signals a thin, hard-to-fill market even when open interest and volume look real.
