# Screening log: Mon Oct 12, 2026, 9:35am ET OPEN (VM, LIVE)

**Session job:** DO, 10 names off the top of the queue (PREMARKET's plan). Live quotes 13:35 UTC, about five minutes after the bell, so option spreads are still opening-wide; every test below is on the live ask anyway. Reserve (spendable) $676.28: Rule 5 3.5/5 line $0.676, screen line $1.353.

| # | Name | Direction | Contract | Live quote | Stock | Test | Result |
|---|---|---|---|---|---|---|---|
| 1 | **BTBT** | CALLS (real money) | Jan15 $1C `25ebc8de` | 0.30 / 0.42, OI 2,242 | $1.245 (-3.5%) | R6: BE at ask $1.42 vs max $1.3475 (stock x 1.0823): needs +14.1% vs cap 8.23% | **PARK, R6.** R5 ($42 < $67.63) and R7 (OI 2,242; spread 33% at the open, re-check) aside, the stock moved the wrong way. Needs stock ~$1.31+ at a $0.36 ask, or ~$1.39 at $0.42. |
| 2 | **CAVA** | CALLS (paper) | Dec18 $55C `8d6d4154` | 4.45 / 5.10, OI 2,361 | $52.54 (-2.1%) | R6: BE $60.10 vs max $59.36 | **$55C FAILS R6** by 74 cents. $52.5C not listed. |
| 2b | **CAVA** | CALLS (paper) | Dec18 $50C `b0d2e74a` | 6.80 / 7.55, OI 468, spread 10.5% | $52.54 | R1 0.058; R2 Nov 3 PM (f) / LY Nov 4 + 21 = Nov 25; R3 20/9/1; R4 $80 JPM vs BE $57.55; R6 +9.54% vs cap 12.99%; R7 pass | **PAPER ENTRY @ $7.55.** |
| 3 | **BABA** | CALLS (paper) | Dec18 $110C `5c993f3b` | 7.90 / 8.55, OI 8,961, spread 7.9% | $110.07 (-1.2%) | R1 0.185; R2 Nov 24 AM (f) / LY Nov 25 + 21 = Dec 16; R3 45/1/0; R4 Baird $160 vs BE $118.55; R6 +7.70% vs cap 11.00%; R7 pass | **PAPER ENTRY @ $8.55.** |
| 4 | **ALNY** | CALLS (paper) | Nov20 $230C `736ea6c9` | 17.30 / 21.40, OI **199** | $231.50 | R7: OI 199 < 250 (spread 21.2% passes). R6: BE $251.40 vs max 231.50 x 1.082 = $250.48 | **PARK, R7 + R6** (OI fell from 200; BE now 92 cents over). |
| 5 | **HII** | CALLS (paper) | Nov20 $270C `ad19b167` | 11.80 / 14.50, OI **232** | $266.50 | R7: OI 232 < 250 (spread 20.5% passes) | **PARK, R7** (OI went down, 235 -> 232). |
| 6 | **CARR** | CALLS (paper) | Nov20 $52.5C / $55C / $57.5C | 3.40 / 5.30 OI 9; 2.40 / 3.60 OI 101; 1.40 / 2.25 OI 286 | $55.61 | R7 on all three: $52.5C OI 9; $55C OI 101; $57.5C OI 286 but spread 0.85 / 1.825 = 46.6% | **KILLED, R7** (no listed strike with BE under the $67 Wells floor clears the liquidity floor). |
| 7 | **TMUS** | CALLS (paper) | n/a | n/a | $152.41 (+2.6%) | R4: ratings stamp still Oct 8 23:11 UTC (pre-drop). One search: latest dated Buy targets found are Deutsche $300 (Oct 2) and Goldman $286 (Sep 2), both before the Oct 9 SpaceX drop. No post-drop note found. | **PARK, R4 undated post-drop.** Next: MarketBeat price-target page for an Oct 9+ note. |
| 8 | **MTZ** | CALLS (paper) | Nov20 $220C `a75d9d97` | 12.20 / 15.50 | $208.04 (-2.2%) | R6: needed stock >= ~$218.2; now ~$10 short and moving away | **KILLED, R6.** |
| 9 | **RKT** | CALLS | n/a | n/a | $11.235 | Off-queue line $11.75 set Friday | **OFF THE QUEUE** (opened under $11.75). |
| 10 | **SE** | CALLS (paper) | Dec18 $95C | not requoted | $95.415 (bid/ask 95.32 / 96.50) | R4: tool stamp Aug 12, older than 60 days as of Oct 11. One search returned undated aggregator lists (Arete Buy $151, Morgan Stanley $153, Barclays $156); none dated after Aug 13 in the results. | **PARK, R4 undated.** Next: MarketBeat page for a dated Buy target; OI on the $95C (was 157). |

**Moved this run:** 10 names. 2 paper entries (BABA, CAVA $50C), 2 killed (CARR R7, MTZ R6), 1 off queue (RKT), 5 parked (BTBT R6, ALNY R7/R6, HII R7, TMUS R4, SE R4).

**Real-money entry:** none. The only real-money candidate (BTBT) failed R6 on the live ask. No research doc exists for it either.

## GLOSSARY
- **R1-R7:** binder Tab 1 Iron Rules. R1 range percentile, R2 earnings before expiry, R3 analyst consensus, R4 lowest Buy target above breakeven, R5 affordability, R6 reachability (breakeven move <= 1.5x median earnings move), R7 liquidity floor (OI >= 250, spread <= 25% of mid).
- **BE (breakeven):** strike + premium paid.
- **OI (open interest):** contracts outstanding on that strike.
- **Spread % of mid:** (ask - bid) / mid.
- **(f):** earnings date not company-verified.
- **PARK:** alive, waiting on one specific check or price; stays on the queue.
- **Paper entry:** logged in `paper_book.md` at the live ask, no money.
