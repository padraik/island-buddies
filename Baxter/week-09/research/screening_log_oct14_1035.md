# Screening log: Wed Oct 14, MIDDAY (10:35am ET)

*Live data pulled 14:35 UTC (NBIX option quote stamped 14:21). Reserve $676.28 (3.5/5 line $0.676). Work: re-test the top 5 of the queue an hour past the open (the OPEN quotes carried opening spreads), plus the TTWO R4 dating search the OPEN run teed up. Two web searches (one TTWO targets, one COUR news for the holding).*

| Ticker | Contract | Stock | Bid / Ask | OI | Spread % mid | BE at ask | Needs | R6 cap | Result |
|---|---|---|---|---|---|---|---|---|---|
| TTWO | Dec18 $190C | 203.22 | 24.40 / 27.10 | 849 | 10.5% | 217.10 | **+6.83%** | 7.35% | R1/R3/R6/R7 pass live; **PARK on R4 dating** (search found nothing dated) |
| NBIX | Dec18 $135C | 135.77 | 8.30 / 10.80 | 307 | **26.2%** | 145.80 | +7.39% | 12.91% | PARK, R7 spread misses by 1.2 pts (size 3 x 3, quote 14:21) |
| BTBT | Jan15 $1C | 1.138 | 0.26 / 0.30 | 2,261 | 14% | 1.30 | +14.2% | 8.23% | PARK, R6 (stock -6.0% on the day) |
| ONDS | Dec18 $8C | 6.405 | 0.35 / 0.36 | 38,059 | 2.8% | 8.36 | +30.5% | 20.89% | PARK, R6 (stock -4.5%, moving away) |
| ALGM | Nov20 $35C | 32.996 | 2.20 / 2.35 | 6,812 | 6.6% | 37.35 | +13.2% | 10.5% | PARK, R6 (R7 now passes, the open's 48% spread was the open) |

**TTWO in detail.**
- R1: (203.22 - 187.63) / 78.31 = **0.199**. Passes, more room than at the open.
- R6: BE $217.10 at the $27.10 ask, needs +6.83% vs 7.35%. Passes, by less than at the open (stock gave back $1.88).
- R7: OI 849, spread 2.70 on 25.75 = 10.5%. Passes.
- R4: tool still 29/1/1, low $270 (tool `updated_at` 2026-08-07). One search ("Take-Two TTWO price target analyst October 2026") returned UBS $230 -> $275 Buy, JPMorgan $250 -> $275 OW, Morgan Stanley $210 -> $265 OW, **all undated**. The UBS note talks about GTA VI hype "ahead of the launch next May", so it predates the Nov 2025 delay: old. The JPM $275 is below the $310 JPM had on Aug 11, so it's an earlier step on the same ladder. **Nothing dated after Aug 15 found.** R4 stays open on Tab 6 dating, not on the level ($270 vs BE $217.10 is $53 of room).
- Next: EVENING 1 writes the paper doc **with R4 flagged as dated-floor-unverified** (paper-book only, so it's a test of the rule, not money), or waits for a Q2 preview (they usually land in the last two weeks of October). Bearxter's question stands: the last GTA 6 delay came on a print, and the game ships Nov 19.

**NBIX:** 8.30 / 10.80 on 3 x 3 contracts, mid 9.55, spread 26.2%. The open's 44% has mostly closed but it's still over 25%. R6 now +7.39% vs 12.91% (stock +0.5%). One more mid-session re-quote (12:35 or 1:35); if it's still over 25% at three separate quotes, kill on R7.

**ALGM:** the spread normalized (6.6%) and OI is 6,812, so R7 passes; it's R6 alone now, needs the stock at ~$34.04 with a $2.35 ask.

**Moved:** 5 (TTWO, NBIX, BTBT, ONDS, ALGM). **Killed:** 0. **Parked:** all 5.

**Pattern:** the whole small-cap tape is red this hour (COUR -3.3%, BTBT -6.0%, ONDS -4.5%, ALGM -1.9%). The real-money names are walking away from their lines; the two paper names (TTWO, NBIX) are steady or up.

## GLOSSARY
- **R1-R7:** binder Tab 1 Iron Rules (calls). R1 range percentile, R2 earnings before expiry, R3 ratings mix, R4 lowest Buy target above breakeven, R5 price cap on reserve, R6 required move vs 1.5x median print move, R7 liquidity floor (OI >= 250, spread <= 25% of mid).
- **BE:** breakeven, strike + ask.
- **Needs:** % move from the current stock price to BE.
- **R6 cap:** 1.5x the median absolute stock move on the last 4-8 print days.
- **Tab 6 dating:** a Rule 4 floor counts only if dated within 60 days and published after the stock's decline.
- **PARK:** fails one rule on today's numbers but could pass on a price move or a date; stays in the queue with its next check.
- **Paper:** binder-rule entry in `paper_book.md`; no money moves.
- **OI:** open interest.
