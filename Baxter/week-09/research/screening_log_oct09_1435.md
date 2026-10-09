# Screening log, Fri Oct 9, 2:35pm ET (MIDDAY, DO)

**Session job:** first run under Rule 7 (liquidity floor, ratified on the ~2pm call). Finish the paper scan's 7 unchained advancers, and find out why TMUS fell 13% yesterday-to-today.
**Rule 5 line (real money):** reserve = spendable = $676.28 -> 3.5/5 line **$0.676**. Quotes pulled live 2:35-2:37pm ET. Ratings via `get_equity_analyst_ratings` this run. 2 web searches (TMUS, FSLR floor).
**Names moved: 8** (7 chained + TMUS).

## 1. Chain checks (7, from the 1:35 log's advancers)
R6 = six most recent prints, close-to-close reaction (PM: print day -> next day; AM: day before -> print day), daily bars pulled this run. Max BE = stock x (1 + 1.5 x median). Expiry = first listed one >= 21 days past the later of tool date and LY date. **R7 = OI >= 250 and spread <= 25% of mid.**

| Ticker | Stock | Ratings / low (stamp) | Print (tool, LY) | Six reactions / median / cap | Contract | Quote | BE at ask / max BE | R7 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| KGC | $23.755 | 18/2/1, $28 (Oct 3) | Oct 28 PM **verified**, LY Nov 4 | +2.70 / +3.76 / +7.12 / -3.21 / +1.27 / +1.77; 2.96%; 4.43% | Nov27 $24C `1d46306d` | 0.00 / 3.50, OI 0 | n/a / $24.81 | fail | **KILL, R6** (a 4.4% cap can't pay for 7 weeks of premium on any OTM strike) and R7 |
| ALB | $101.17 | 15/7/0, $130 (Oct 3) | Nov 4 PM **verified**, LY Nov 5 | +1.32 / -1.51 / -0.76 / -9.41 / +2.98 / +5.54; 2.25%; 3.37% | Nov27 $102C `0748a51f` | 7.05 / 9.20, OI 0 | $111.20 / $104.58 | fail | **KILL, R6** and R7 |
| TCOM | $38.815 | 31/3/0, $42 (Oct 3) | Nov 16 PM (f), LY Nov 17 (6-K, both present) | -5.54 / +14.92 / +2.19 / -2.59 / -12.55 / +3.01; 4.28%; 6.41% | Dec18 $40C `8383612f` | 1.65 / 2.10, OI 249 | $42.10 / $41.30 | fail by 1 OI | **KILL, R6** (80 cents over) |
| SE | $95.00 | 27/4/0, $105 (**Aug 12**, ages past 60 days Sun Oct 11) | Nov 10 AM (f), LY Nov 11 (6-K, both present) | +8.20 / +19.07 / -8.22 / -16.53 / +13.14 / +14.56; 13.85%; 20.78% | Dec18 $95C `4fe7f5f7` | 8.80 / 9.25, OI 157 | $104.25 / $114.74 | **fail (OI 157)**; $90C `bda428d8` 10.60 / 12.00 OI 122 also fails | **PARKED, R7.** Passes R6 easily; R4 passes by 75 cents ($105 vs $104.25) on a floor that goes stale Sunday. Needs OI to build AND a fresh floor. |
| BKNG | $160.42 | 32/8/0, $180 (Sep 23) | Nov 3 PM **verified**, LY Oct 28 | +3.87 / +0.40 / -0.87 / -6.15 / +0.35 / +6.56; 2.37%; 3.56% | Nov27 $165C `8a883159` | 8.00 / 8.70, OI 0 | $173.70 / $166.13 | fail | **KILL, R6** |
| FSLR | $177.99 | 29/10/1, $197 (**Jul 31, stale**) | Oct 29 PM (f), LY Oct 30 (+21 = Nov 20, passes) | -8.32 / +5.29 / +14.28 / -13.61 / +4.86 / +2.44; 6.80%; 10.21% | Nov20 **$175C** `99f5f557` | 15.10 / 15.90, **OI 282**, spread 5.2% | **$190.90 / $196.17** | **pass** | **PARKED, R4 dating.** Only name today that clears R1/R2/R3/R6/R7. $180C (13.00 / 14.35, OI 187) and $185C (10.80 / 11.90, OI 100) fail R7. One search returned only old cuts (BMO $187 Outperform, RBC $214, both referencing 2025 guidance); a current $187 Buy would put the floor UNDER the $190.90 BE. Needs a Buy target dated after the decline. |
| HD | $291.30 | 23/15/1, $310 (Oct 3) | Nov 17 AM **verified**, LY Nov 18 | -0.61 / +3.17 / -6.02 / +1.99 / +0.88 / -0.12; 1.44%; 2.15% | Dec18 $295C `752167a3` | 13.50 / 14.00, OI 355 | $309.00 / $297.56 | pass | **KILL, R6** (a 2% mover) |

## 2. TMUS (parked at 1:35)
Stock $149.45 vs Oct 8 close $171.31 (-12.8%). No SEC filing since Oct 5 (`get_sec_filing_index`, all forms). One search: no report of the Oct 9 drop; results were about the Q2 guidance hold and older downgrades. Ratings 27/5/0, low $169, stamp **Oct 8 23:11 UTC**, which is after yesterday's close but before today's move. **Still parked:** cause unknown, so there is no floor published after the decline. Next: check `get_sec_filing_index` again tomorrow (an 8-K often lands after the move) and whether the low target moves.

## 3. Result
8 moved: **0 paper entries**, **5 killed** (KGC, ALB, TCOM, BKNG, HD: all R6, three also R7), **3 parked** (FSLR R4 dating, SE R7 + floor aging, TMUS cause unknown). All 17 advancers from the paper scan's 62 liquid names have now been chained: 3 paper entries, 10 kills, 4 parked (APP, TMUS, SE, FSLR).

What it says: R6 killed five of seven again, and four of the five were slow movers (median reaction 1.4-3.0%). Rule 7 bit on its first real run: SE passes everything else by a wide margin and fails on OI 157. FSLR shows the floor can be met by moving one strike in-the-money ($175C, OI 282) instead of nearest-OTM. Nothing real: the cheapest contract checked today costs $165.

## GLOSSARY
- **R1 / range pct:** where the stock sits in its 52-week range; < 0.25 = bottom quartile (calls side).
- **R2:** earnings print proven to land before expiry (21 days past the later of tool date and last year's date; 10-Q deadline 5+ trading days before expiry; 6-K filers need both dates).
- **R3:** at most 1 Sell, at least 3 Buys, Buys >= Holds.
- **R4 / floor / low:** the lowest Buy-rated price target must be above breakeven, dated within 60 days and published after the decline.
- **R5:** one contract's ask <= tier % x reserve / 100 ($0.676 at 3.5/5 today). Dropped for paper.
- **R6 / cap / max BE:** the move to breakeven must be <= 1.5x the median earnings reaction; max BE = stock x (1 + cap).
- **R7:** liquidity floor, OI >= 250 and spread <= 25% of mid on the exact contract.
- **BE:** strike + premium. **OI:** open interest. **(f):** date not company-verified. **6-K:** foreign filer, no 10-Q deadline.
- **Parked:** alive, waiting on one specific check.
