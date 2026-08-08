# Research: PFLT (PennantPark Floating Rate Capital Corp.) -- Aug 8, 2026

**Verdict: KILL (Rule 6, decisive and structural). Not queued.**

## Setup

- Price: $7.53 (Aug 7, 2026 close)
- 52-week range: $6.83 - $10.60
- Percentile: **19th** -- bottom quartile, CALLS candidate on Step 1
- Confirmed catalyst: **Q3 FY2026 earnings, Aug 10, 2026, PM**, `get_earnings_results` verified: true -- matches the date supplied at the start of tonight's run, no drift.

## The Unified Screen

**Step 1:** 19th percentile, clears. **Step 2:** Aug 10 PM, verified true, 11 days ahead of the Aug 21 expiry -- clears with plenty of room. **Step 3 (Rule 3):** clean. Six analysts polled, consensus Buy, lowest individual target $9.00, no Sell/Underperform found. Every rule up through Rule 3 clears without argument.

## Rule 4 (Bear Floor)

Candidate instrument: $7.50C Aug 21 2026, ask $0.15. Breakeven $7.65, needs +1.6% from $7.53. Lowest Buy target found, Keefe Bruyette (Outperform, $10.00, though recently trimmed from $10.50), clears breakeven by 30.7%. **Rule 4 passes easily** -- this was never the problem.

## Rule 6 (Reachability): the decisive kill

Four real, verified earnings-day moves pulled from actual daily closes:
- **Aug 11, 2025:** -1.05%
- **Nov 24, 2025:** -0.98%
- **Feb 9, 2026:** -3.50%
- **May 7, 2026:** -0.56%

Median absolute move: **1.02%.** 1.5x cap: **1.52%.** Current requirement: **+1.6%.**

**Rule 6 fails.** The required move sits above the ceiling, not below it -- by a small margin in percentage-point terms, but the direction is the wrong way, and there is no version of "give it a wider strike" that fixes this, because the underlying problem isn't the strike. It's the instrument.

## Why this isn't close, structurally

PFLT is a business development company (BDC) -- a closed-end fund that lends to middle-market companies at floating rates and trades close to its net asset value. BDCs are built to be low-volatility income vehicles, not event-driven equities. Every one of the four real earnings reactions pulled above is under 3.5%, and three of the four are under 1.1%. That isn't bad luck on a sample of four; it's what the instrument is supposed to do. A catalyst-reachability strategy built around "the stock needs to move X% on a specific day" doesn't have a home in a security class engineered to not move much on any day, including earnings day. This would fail Rule 6 on almost any strike that costs enough to be worth trading.

## Decline category

Not applicable in the usual sense. PFLT's slow drift from roughly $11 (Feb 2025) to $7.30 (Aug 2026) tracks base-rate-driven NAV erosion typical of the floating-rate BDC sector over that period, not a single dislocatable event. There is no "overreaction" to trade because there was no reaction in the first place -- just a long, quiet slide that options reachability can't capture regardless of catalyst date.

## What would reopen this

Nothing about this specific print. The structural mismatch (BDC low earnings-day volatility vs. the fund's reachability requirement) applies to essentially any PFLT entry, any quarter. Not worth re-screening unless the fund changes what kinds of instruments it will consider.

## GLOSSARY

- **52-week range / percentile:** where the current price sits between the stock's low and high over the trailing year; 0% = at the low, 100% = at the high.
- **Rule 4 (bear floor):** the lowest price target among Buy-rated analysts must sit above the option's breakeven.
- **Rule 6 (reachability):** the move required to reach breakeven must not exceed 1.5x the stock's median historical earnings-day reaction.
- **Business development company (BDC):** a closed-end investment company that lends to and invests in small and mid-sized businesses, typically trading near its net asset value with income-fund-like volatility.
- **Breakeven:** strike price plus premium paid per share -- where the option holder neither gains nor loses at expiration.
- **Net asset value (NAV):** the per-share value of a fund's holdings; BDC share prices tend to track NAV closely rather than swinging on sentiment the way growth-stock equities do.
