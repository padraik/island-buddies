# Screening log, Fri Oct 9, 11:35am ET (MIDDAY, DO)

**Session job:** ARDX requote first, then the cheapest-stock requotes the 10:35 plan named: RARE (last of 0k), RWT, TDUP (+ one floor search), FINV, UPBD, CTMX.
**Rule 5 line:** reserve = spendable = $676.28 -> 3.5/5 line **$0.676**. Quotes pulled live 11:35-11:37am ET, Oct 8 official closes alongside. Ratings via `get_equity_analyst_ratings` this run.
**Names moved: 6** (plus the ARDX requote). 1 web search (TDUP).

## 1. Entry candidate
| Ticker | Contract | Live quote | Close Oct 8 | Stock | Verdict |
|---|---|---|---|---|---|
| ARDX | $3C Nov20 `e500baad` | **0.30 / 0.65**, mark 0.475, OI 49, vol 0 (two pulls, 11:34 and 11:35) | 0.35 | $3.245 | **NO ORDER: mid $0.475 > the doc's $0.45 ceiling.** Ask $0.65 now passes the $0.676 line; the bid rose from 0.10 to 0.30 with it. Rest passes: 11/0/0 low $8.00, Q3 `actual: null`, Oct 29 PM (f), LY Oct 30 PM, BE at mid $3.475 vs max $4.09. Requote at 12:35. |

## 2. Requotes and chain checks
| Ticker | Stock | Ratings / low | Contract | Live quote | R6 / max BE | Verdict |
|---|---|---|---|---|---|---|
| RARE | $15.50 (+1.4%) | 11/10/0, $16 | Nov27 $15C `7b5fb72f` / Dec18 $15C `f0cecd94` | Nov27 0.20 / 3.30 (OI 0); Dec18 1.95 / 2.30 (OI 890) | not pulled | **KILL, R5 + R4.** Q3 Nov 3 PM (f), LY Nov 4. Any BE has to sit under the $16 low: the $15C would need a premium under $1.00 with $0.50 of intrinsic; the real Dec18 ask is $2.30 (BE $17.30). Nov27 has no market. Strikes above $15 can't pass R4 at all. |
| RWT | $3.27 (-1.8%) | 7/2/0, **$3.75 (was $4.25)** | Nov20 $3C `148a43c0` | 0.10 / 0.80, OI 1, vol 0 | cap 8.69%, max BE $3.554, max price $0.554 | **KILL, R5 + R6 + R4.** Ask $0.80 over both lines; the low target fell to $3.75, under BE at the ask ($3.80). Thin for four straight runs. |
| TDUP | $2.405 (+2.3%) | 6/1/0, $5.70 | Jan15 $2.5C `ba0a44c6` | 0.35 / 0.45, OI 414 | max price = 2.405 x 1.285 - 2.50 = **$0.590** | **Still FLOOR-BLOCKED.** Passes R5 and R6 at the ask (BE $2.95). One search for a Buy target dated after Aug 8: results were all 2025 (Roth $11 Oct 30 2025, Wells $13 Aug 5 2025, Telsey). Nothing dated after the Aug 2026 drop. Next: one more try in an EVENING session (MarketBeat forecast page via WebFetch). |
| FINV | $3.095 (-1.4%) | 6/1/0, $4.11 | Dec18 $2.5C `550a4ddc` | 0.40 / 1.15, OI 388 | not recomputed | **Parked, R5 at the ask** (1.15) and still floor-blocked (the $4.11 low is Citi's Neutral, not a Buy). |
| UPBD | $15.34 (-2.2%) | 5/1/0, $20 | Nov20 $17.5C `d768deac` | 0.30 / 0.50, OI 228 | cap 16.2%, max BE **$17.825** | **KILL, R6.** BE $18.00 at the ask (+17.3%), $17.90 at mid (+16.7%): fails at both. Reopen only if the stock gets back above ~$15.70 with the ask under $0.33. Also still floor-blocked (TD Cowen $28 is Jul 31). |
| CTMX | $2.485 | 8/0/0, $6 | Jan15 $2C `165e53a1` | 0.45 / 1.20, OI 270, vol 0 | max BE $2.96 | **Parked, R5** (ask and mid). Same quote all day. |

## 3. Tally
6 moved: **RARE, RWT, UPBD killed**; TDUP (floor), FINV (R5 + floor), CTMX (R5) parked. ARDX: no order, now on the mid ceiling instead of the ask. The 0k list is finished. The live queue with a buyable contract is down to ARDX alone; tonight's EVENING 1 needs the fresh sub-$10 source (prints Nov 2-25, Dec18/Jan15 expiries) the 10:35 plan named.

## GLOSSARY
- **R2 / Rule 2 (Oct 8):** expiry at least 21 days after the later of the tool's date and last year's (LY) date; 10-Q deadline at least 5 trading days before expiry. "(f)" = `verified: false`.
- **R4 / Rule 4:** the lowest Buy target must be above breakeven.
- **R5 / Rule 5:** one contract's ask must fit the tier budget ($0.676/share at 3.5/5 on a $676.28 reserve).
- **R6 / Rule 6:** move to breakeven no more than 1.5x the median earnings-day move. Max BE = stock x (1 + cap).
- **Doc ceiling:** a tighter max price a research doc sets for itself (ARDX: mid must be at or under $0.45, because the spread is the cost).
- **BE / breakeven:** strike + premium paid.
- **Mark / mid:** halfway between bid and ask. The rules price off the real bid/ask, not the mark.
- **OI:** open interest, contracts outstanding. OI 0-1 with no real bid means there's no market.
- **Floor-blocked:** the name passes on price but its lowest Buy target isn't dated within 60 days and after the drop (binder Tab 6), so Rule 4 can't be called passed.
- **Nov27 / Dec18 / Jan15:** expirations Nov 27 2026, Dec 18 2026, Jan 15 2027.
