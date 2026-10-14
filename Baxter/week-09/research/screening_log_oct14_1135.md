# Screening log: Wed Oct 14, MIDDAY (11:35am ET)

*Live data pulled 15:35 UTC. Reserve $676.28 (3.5/5 line $0.676). Work: re-test the top 5 of the queue (NBIX gets its third R7 read), plus the early OI pull on SE and HII that the 10:35 run teed up. No web searches.*

| Ticker | Contract | Stock | Bid / Ask | OI | Spread % mid | BE at ask | Needs | R6 cap | Result |
|---|---|---|---|---|---|---|---|---|---|
| TTWO | Dec18 $190C | 202.59 (+1.1%) | 23.90 / 25.40 | 849 | 6.1% | 215.40 | **+6.32%** | 7.35% | R1/R3/R6/R7 pass live; **PARK on R4 dating** (paper doc goes to EVENING 1) |
| NBIX | Dec18 $135C | 136.06 (+0.7%) | 8.30 / 10.80 | 307 | **26.2%** | 145.80 | +7.16% | 12.91% | **KILL, R7.** Third read over 25% (44% open, 26.2% at 10:35, 26.2% now; size 6 x 5, vol 0) |
| ALGM | Nov20 $35C | 32.28 (-4.1%) | 1.90 / 2.10 | 6,812 | 10.0% | 37.10 | +14.9% | 10.5% | PARK, R6 (moving away) |
| BTBT | Jan15 $1C | 1.1295 (-6.7%) | 0.25 / 0.30 | 2,261 | 18.2% | 1.30 | +15.1% | 8.23% | PARK, R6 |
| ONDS | Dec18 $8C | 6.395 (-4.7%) | 0.33 / 0.36 | 38,059 | 8.7% | 8.36 | +30.7% | 20.89% | PARK, R6 |
| SE | Dec18 $95C | 94.90 (-1.1%) | 8.70 / 9.20 | **161** | 5.6% | 104.20 | +9.8% | n/a | PARK, R7 OI (161 < 250; was 163). R4 floor stamp also stale (Aug 12). |
| HII | Nov20 $270C | 262.375 (+1.8%) | 11.40 / 12.10 | **227** | 6.0% | 282.10 | +7.5% | n/a | PARK, R7 OI (227 < 250; was 230, still drifting down) |

**TTWO.** R1 about 0.19 (leaves the quartile above ~$207.2). R6 +6.32% vs 7.35%, a bit more room than at 10:35 because the ask came in to 25.40. R7 6.1%. R4 unchanged: the $270 low passes on level ($55 of room over BE) but nothing dated after Aug 15. Plan stands: EVENING 1 writes `research_TTWO_paper.md` with R4 flagged dating-unverified, and the meeting decides whether that's a fair paper test.

**NBIX kill.** The 10:35 run set the test: still over 25% on a third separate mid-session quote = kill on R7. It is: 8.30 / 10.80, mid 9.55, 26.2%, the same quote as 10:35 (updated 15:34 UTC, so it's live, but nobody is making a market there). The rule is written for exactly this. A thin Dec contract on a $136 stock charges $2.50 round trip on each side. Off the queue; if NBIX's spread tightens on a later scan it comes back as a new name.

**SE / HII.** OI on both is a once-a-day number, so these were never going to move intraday; pulled early because the top of the queue stayed parked. Both still fail R7 OI. Saturday Oct 17 reads them again, along with ALNY / FN / AVAV / LEU.

**Moved:** 7 (TTWO, NBIX, ALGM, BTBT, ONDS, SE, HII). **Killed:** 1 (NBIX, R7). **Parked:** 6.

**Pattern:** small caps are red for a second straight hour, and harder: COUR -4.4%, BTBT -6.7%, ONDS -4.7%, ALGM -4.1%. Large caps are flat to green (TTWO +1.1%, HII +1.8%, NBIX +0.7%). It's the tape, not the names.

## GLOSSARY
- **R1-R7:** binder Tab 1 Iron Rules (calls). R1 range percentile, R2 earnings before expiry, R3 ratings mix, R4 lowest Buy target above breakeven, R5 price cap on reserve, R6 required move vs 1.5x median print move, R7 liquidity floor (OI >= 250, spread <= 25% of mid).
- **BE:** breakeven, strike + ask.
- **Needs:** % move from the current stock price to BE.
- **R6 cap:** 1.5x the median absolute stock move on the last 4-8 print days. n/a = not computed this run (the name is blocked at R7 first).
- **Tab 6 dating:** a Rule 4 floor counts only if dated within 60 days and published after the stock's decline.
- **PARK:** fails one rule on today's numbers but could pass on a price move or a date; stays in the queue with its next check.
- **KILL:** fails a rule that won't fix itself in the window; comes off the queue.
- **Paper:** binder-rule entry in `paper_book.md`; no money moves.
- **OI:** open interest.
