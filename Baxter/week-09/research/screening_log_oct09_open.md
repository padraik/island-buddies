# Screening log, Fri Oct 9, 9:35am ET (OPEN, DO)

**Session job:** ARDX entry decision first, then the queue: STOK/VRDN/ENOV chains (0h-0j), CTMX requote (0l), then the 0k R6 batch, up to 10 names.
**Rule 5 line:** reserve = spendable = $676.28 -> 3.5/5 line **$0.676**. Quotes pulled live 9:35-9:37am ET (opening spreads; official Oct 8 closes listed alongside so the kills don't rest on a wide opening quote).
**Names moved: 10.**

## 1. Entry candidate
| Ticker | Contract | Live quote | Close Oct 8 | Stock | Verdict |
|---|---|---|---|---|---|
| ARDX | $3C Nov20 `e500baad` | **0.10 / 0.70** (twice, 9:36 and 9:37), mark 0.40, OI 49, vol 0 | 0.35 | $3.255 | **NO ORDER: ask $0.70 > $0.676 (R5, doc checklist line 2).** Mid $0.40 passes the $0.45 ceiling; BE at mid $3.40 vs max $4.10 (R6 ok); 11/0/0 low $8.00; Q3 `actual: null`, Oct 29 PM (f) unchanged. Everything passes but the ask. Doc stays buyable through Fri Oct 16; MIDDAY requotes. |

## 2. Chain stage
| Ticker | Stock | Ratings / low | Print | Max BE (R6) | Chain (live / Oct 8 close) | Verdict |
|---|---|---|---|---|---|---|
| STOK | $24.10 | 14/0/0, $35 | Nov 3 PM (f), LY Nov 4 | $26.59 | **No Dec18 or Jan15 listed** (Oct16, Nov20, Feb19, May21, Dec17). Nov20 fails R2 (Nov 4 + 21 = Nov 25). Feb19 $25C 1.10 / 5.50, close **3.30**, BE $28.30 | **KILL, R5 + R6** |
| VRDN | $18.26 | 17/0/0, $22 | Nov 4 AM (f), LY Nov 5 | $20.35 | No Dec18 (Oct16, Nov20, Jan15, Apr16). Jan15 $20C 1.05 / 4.80, close **2.18**, BE $22.18 | **KILL, R5 + R6** |
| ENOV | $17.19 | 12/1/0, $24 (data 2022) | Nov 5 AM verified | $20.31 | Dec18 $17.5C 0.90 / 3.00, close **2.15**; $20C 0.95 / 1.90, close **1.45**, BE $21.45 | **KILL, R5 + R6** |
| ADNT | $17.49 | 9/3/1, $21 | (not pulled) | n/a | Dec18 $20C 0.35 / 1.05, mark 0.70, close **0.75**, BE $20.70 (+18.4%); $17.5C close 1.73 | **KILL, R5** (mark and close both over $0.676; nearest-strike-first, no R6 pull needed) |
| EYE | $16.70 | 9/3/0, $20 | (not pulled) | n/a | No Dec18. Jan15 $17.5C 0.60 / 2.90, close **1.98**, BE $19.48 (+16.6%) | **KILL, R5** |
| CTMX | $2.47 | 8/0/0, $6 | Nov 5 PM (f) | $2.94 | Jan15 $2C 0.45 / 1.20 (OI 270), mark 0.825, close **0.78** | **PARKED, R5** (now fails at mid as well as the ask; was 0.55 / 1.00) |

## 3. Expiry lookup (0k batch, first three)
| Ticker | Stock | Listed expiries | Next step |
|---|---|---|---|
| PRVA | $20.43 | Oct16, Nov20, **Feb19**, May21 (no Dec18/Jan15) | Feb19 $22.5C ask first; expect R5 kill (2.5 grid, 4 months of time value) |
| BILI | $15.47 (+4.2% today) | Oct16, Nov20, **Jan15**, Apr16 (no Dec18) | Jan15 $17.5C ask first (6-K filer: both dates needed for R2) |
| TNDM | $15.69 | Oct16, Nov20, **Jan15**, Feb19 (no Dec18) | Jan15 $17.5C ask first |

## 4. Tally
10 moved: **5 killed** (STOK, VRDN, ENOV, ADNT, EYE: all R5, three also R6), **1 no-order** (ARDX, ask a nickel-and-a-half over the line), **1 still parked** (CTMX), **3 expiries located** (PRVA, BILI, TNDM). Most of the Dec18-window list doesn't even have a Dec18 expiry; the next-out contract is 3-4 months of time value, which is where Rule 5 kills on a $676 reserve.

## GLOSSARY
- **R2 / Rule 2 (Oct 8):** expiry at least 21 days after the later of the tool's date and last year's (LY) date; 10-Q deadline at least 5 trading days before expiry. "(f)" = `verified: false`.
- **R5 / Rule 5:** one contract's ask must fit the tier budget ($0.676/share at 3.5/5 on a $676.28 reserve).
- **R6 / Rule 6:** move to breakeven no more than 1.5x the median earnings-day move. Max BE = stock x (1 + cap).
- **Mark / mid:** halfway between bid and ask. The rules price off the real bid/ask, not the mark.
- **Close:** the official Oct 8 settled option price, listed because opening spreads are wide.
- **Nearest-strike-first:** on $12+ stocks, check the first OTM strike's price before pulling print history; if it fails R5, R6 doesn't matter.
- **6-K filer:** a foreign company with no 10-Q deadline, so R2 needs both the tool date and last year's date.
- **Dec18 / Jan15 / Feb19:** monthly expirations Dec 18 2026, Jan 15 2027, Feb 19 2027.
