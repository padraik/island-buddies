# Screening log: Wed Oct 14, OPEN (9:35am ET)

*Live data pulled 13:35-13:40 UTC, first five minutes of the session. Opening option spreads run wide (COUR, NBIX, ALGM all show it), so an R7 spread fail in this window gets a MIDDAY re-quote before it's final. Reserve $676.28 (3.5/5 line $0.676). Work: the top 5 of the queue on live quotes (items 6-11 wait for Saturday's OI check). Four web searches, all TTWO (GTA 6 headline date, R4 floor dating).*

| Ticker | Contract | Stock | Bid / Ask | OI | Spread % mid | BE at ask | Needs | R6 cap | Result |
|---|---|---|---|---|---|---|---|---|---|
| TTWO | Dec18 $190C | 205.10 | 25.70 / 27.90 | 849 | 8.2% | 217.90 | **+6.24%** | 7.35% | R1/R3/R6/R7 pass live; **PARK on R4 dating** (below) |
| BTBT | Jan15 $1C | 1.17 | 0.26 / 0.36 | 2,261 | 32% | 1.36 | +16.2% | 8.23% | PARK, R6 (stock moving away; was +14.5% at the close) |
| ONDS | Dec18 $8C | 6.505 | 0.36 / 0.40 | 38,059 | 10.5% | 8.40 | +29.1% | 20.89% | PARK, R6 (moving away: needs ~$6.95 at a $0.40 ask) |
| NBIX | Dec18 $135C | 132.57 | 6.70 / 10.50 | 307 | 44% | 145.50 | +9.75% | 12.91% | PARK, R7 spread at the open; MIDDAY re-quote as planned |
| ALGM | Nov20 $35C | 33.205 | 1.65 / 2.70 | 6,812 | 48% | 37.70 | +13.5% | 10.5% | PARK, R6 (+ opening spread) |

**TTWO in detail.**
- R1: 52-week range 187.63 (Mar 27) to 265.94 (Jul 7). At $205.10: (205.10 - 187.63) / 78.31 = **0.223**. Passes, near the edge: above ~$207.2 it leaves the bottom quartile.
- R2: Nov 9 PM verified, Dec18 expiry is 39 days later. Passes.
- R3: 29 / 1 / 1. Passes (one Sell allowed).
- R6: BE $217.90 at the $27.90 ask, needs +6.24% vs the 7.35% cap (median of the last six print moves 4.90%). **Passes**, with the stock up 2.4% today.
- R7: OI 849, spread 2.20 on a 26.80 mid = 8.2%. Passes.
- R4: tool low **$270** vs BE $217.90, $52 of room. Tab 6 dating: the two $270 targets found (DA Davidson Buy, Baird Outperform, both raised to $270) came "following Q4 results", i.e. May 2026, **before** the Jul 7 high and the decline. Dated post-print Buys found: **Roth $300 (Aug 10, 2026)** and **JPMorgan Overweight $310 (Aug 11, 2026)**. Both are after the Aug 7 print and inside the decline, but Oct 14 is 64-65 days later, **4-5 days past the 60-day window**. A Sep 4, 2026 headline (sentisense) says TTWO was in a correction "and not one analyst has cut a target". Other results (BMO $236, Morgan Stanley $210, DZ Bank Hold $105, Roth $130, Baird $172) are undated and on their numbers belong to the 2023-2025 price era; not used. **Verdict: the floor is very likely real, but nothing dated inside 60 days was found, so R4 isn't cleared this run.** Next: one search for a TTWO target action dated after Aug 15 (Q2 previews usually land late Oct, before the Nov 9 print).
- **GTA 6 headline (from PREMARKET), dated:** it's the **Nov 2025** delay (May 2026 -> **Nov 19, 2026**), announced on the Nov 6, 2025 print. Not new news, and not the cause of Monday's -4.2%. It matters to the doc anyway: the game ships Nov 19, ten days after the Nov 9 print and inside the Dec18 window. Bearxter's question: the last delay was announced *on a print*. If the Nov 9 call carries another delay, the stock gaps down. The paper doc has to answer that in writing.
- Paper only either way: $2,790 a contract against a $67.63 real-money line.

**Moved:** 5 (TTWO, BTBT, ONDS, NBIX, ALGM). **Killed:** 0. **Parked:** all 5 (TTWO R4 dating, BTBT/ONDS/ALGM R6, NBIX R7 spread at the open).

**Pattern:** the two real-money names (BTBT, ONDS) both fell 3% at the open and moved further from their R6 lines. TTWO is the only name moving toward us, and it's paper.

## GLOSSARY
- **R1-R7:** binder Tab 1 Iron Rules (calls). R1 range percentile, R2 earnings before expiry, R3 ratings mix, R4 lowest Buy target above breakeven, R5 price cap on reserve, R6 required move vs 1.5x median print move, R7 liquidity floor (OI >= 250, spread <= 25% of mid).
- **BE:** breakeven, strike + ask.
- **Needs:** % move from the current stock price to BE.
- **R6 cap:** 1.5x the median absolute stock move on the last 4-8 print days.
- **Tab 6 dating:** a Rule 4 floor counts only if dated within 60 days and published after the stock's decline.
- **PARK:** fails one rule on today's numbers but could pass on a price move or a date; stays in the queue with its next check.
- **Paper:** binder-rule entry in `paper_book.md`; no money moves.
- **OI:** open interest.
