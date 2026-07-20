# SCREENING LOG: JUL 20, 2026 (Monday, second batch)
## Untouched sectors: food/beverage, consumer durables, aerospace parts, materials/forest products

**Batch:** 15 names sourced from sectors not touched by any prior batch (checked against the Jul 13 and Jul 16 exclusion lists): consumer staples/food-beverage, durable goods, materials/forest products.

**Protocol:** cost-ordered funnel. Free range-percentile screen, free chain geometry, searches only for chain-stage survivors.

---

## STAGE 1: RANGE PERCENTILE (free)

| Ticker | Price | 52wk range | Pctile | Zone |
|--------|-------|-----------|--------|------|
| CAG | $14.60 | $12.53-$20.32 | 27th | MID-OUT |
| SJM | $112.50 | $88.25-$119.39 | 78th | PUTS zone (logged, no search) |
| CPB | $22.17 | $19.55-$34.17 | 18th | CALLS zone |
| HRL | $25.28 | $19.70-$29.78 | 55th | MID-OUT |
| KHC | $25.89 | $21.04-$29.19 | 60th | MID-OUT |
| LANC | -- | -- | -- | KILL: no instrument (API 404, no viable quote) |
| TAP | $41.70 | $38.04-$54.82 | 22nd | CALLS zone |
| UAA | $7.28 | $4.13-$8.15 | 78th | PUTS zone (logged, no search) |
| TXG | $42.79 | $11.16-$46.32 | 90th | PUTS zone (logged, no search) |
| WHR | $36.80 | $36.01-$100.49 | 1st | CALLS zone |
| MAS | $77.49 | $58.16-$83.20 | 77th | PUTS zone (logged, no search) |
| SEE | -- | -- | -- | KILL: no instrument (API 400, no viable quote) |
| PCH | -- | -- | -- | KILL: no instrument (API 400, no viable quote) |
| WY | $23.96 | $21.16-$27.75 | 43rd | MID-OUT |
| GATX | $178.14 | $148.20-$205.56 | 52nd | MID-OUT |

**Tally:** 15 attempted, 12 valid. 5 MID-OUT, 4 PUTS-zone (logged to watch list only, zero searches, per the no-dedicated-puts-pools rule), 3 CALLS-zone survivors, 3 no-instrument kills.

---

## STAGE 2: CHAIN GEOMETRY (free) -- the 3 CALLS survivors

- **CPB:** cheapest reachable near-term strike ($22C, several expiries) needs as little as 0.6-3.8% -- unusually tight geometry.
- **TAP:** $45C Aug21 at $0.70, needs +9.6%.
- **WHR:** $48C Aug21 at $0.65, needs +30.8% -- the cheapest reachable strike is already a stretch.

All three earned a search.

---

## STAGE 3: SEARCHES (3 spent) -- ALL THREE KILLED ON RULE 3

**CPB: KILL, Rule 3.** 19-analyst breakdown: 2 Strong Buy, 13 Hold, 1 Moderate Sell, 3 Strong Sell -- 4 Sell-class ratings, fails the max-1 outright. Also likely fails Rule 2: Campbell's fiscal Q4 (year-end late July/early Aug) typically reports in September, outside every affordable expiry checked -- not confirmed, moot given the Rule 3 kill. [Source: TipRanks/consensus scan, Jul 2026 data.]

**TAP: KILL, Rule 3.** 29-analyst breakdown: 6 Buy, 13 Hold (wait -- alternate source: 5/10/2 on a smaller sample), consistently **2 Sell ratings** across both sources. Fails max-1. This one stings a little -- Aug 6 earnings confirmed inside the Aug 21 expiry, and Q1 was a real beat (EPS 100% above estimate, revenue +1.1% above estimate) while the stock sits at the 22nd percentile on soft-2026-guidance fears. That's the real dislocation shape the funnel hunts for. But 2 Sells is 2 Sells -- the rule doesn't have a discretion clause for a name Baxter likes. [Sources: MarketBeat, TipRanks TAP forecast pages, Jul 2026.]

**WHR: KILL, Rule 3 (and Rule 6 for good measure).** 13-analyst breakdown: 2 Buy, 7 Hold, 4 Sell -- fails max-1 badly. Also would have failed Rule 6 independently: +30.8% required against a company that just posted a 13.6% single-day drop on weak results, meaning the stock already demonstrated its violent-move ceiling and it still wouldn't have cleared this strike. Double kill, no ambiguity. [Source: Daily Political/MarketBeat 52-week-low coverage, Jul 2026.]

---

## VERDICT

**15 attempted, 12 valid, 0 advance.** Clean batch -- no borderlines, no DATA-INSUFFICIENT. Rule 3 did all the work at the search stage; Rule 6 geometry alone (TAP, CPB) would not have been enough to kill on its own, a reminder that the funnel's lines are independent gates, not a single score.

**Combined with the queue-8 earlier today: 23 names screened this session, 0 advances, 5 searches total.**

---

## GLOSSARY

- **Range percentile:** where the current price sits inside the 52-week low-to-high range, 0th = at the low.
- **MID-OUT:** stock in the 25th-74th percentile; neither calls nor puts candidate.
- **CALLS zone / PUTS zone:** bottom quartile / top quartile of 52-week range, eligible for the respective funnel.
- **No-instrument kill:** ticker returns no viable quote/chain from the broker API (delisted, renamed, or unsupported); killed without spending a search.
- **Rule 3 (ratings):** max 1 Sell/Underperform rating for a calls candidate (mirrored for puts).
- **Rule 6 (reachability):** the strike's required move to breakeven must be plausible against the stock's own historical earnings-day moves.
- **Breakeven:** strike + premium paid.
- **STRETCH:** chain-script label for an ask at the top of the affordable band ($0.90-$1.00).
- **No-dedicated-puts-pools rule:** PUTS-zone names get logged to the watch list only; no searches spent until the puts back-test unblocks live puts entries.
