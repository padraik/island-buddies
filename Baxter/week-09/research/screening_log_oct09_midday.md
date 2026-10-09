# Screening log, Fri Oct 9, 10:35am ET (MIDDAY, DO)

**Session job:** ARDX requote first, then the 0k batch (PRVA, BILI, TNDM, ATS, SRAD, MDU, KT, CPRI, KVYO, BEAM), nearest-OTM ask first, up to 10 names.
**Rule 5 line:** reserve = spendable = $676.28 -> 3.5/5 line **$0.676**. Quotes pulled live 10:34-10:37am ET, Oct 8 official closes alongside.
**Names moved: 10** (plus the ARDX and CTMX requotes).

## 1. Entry candidate
| Ticker | Contract | Live quote | Close Oct 8 | Stock | Verdict |
|---|---|---|---|---|---|
| ARDX | $3C Nov20 `e500baad` | **0.10 / 0.70**, mark 0.40, OI 49, vol 0 (10:32) | 0.35 | $3.245 | **NO ORDER: ask $0.70 > $0.676 (R5).** Same quote as the open; nobody has touched this strike all morning. Everything else still passes: 11/0/0 low $8.00, Q3 `actual: null`, Oct 29 PM (f), LY Oct 30 PM. Requote at 11:35. |
| CTMX | Jan15 $2C `165e53a1` | 0.45 / 1.20, mark 0.825, OI 270 | 0.78 | $2.475 | Still parked, R5 at the ask and the mid. |

## 2. Chain stage (0k batch)
Expiry used = the first listed one that clears R2 for a Nov print (Dec18 where listed, else Jan15, PRVA Feb19). Nearest OTM strike first; if it fails R5, the next one up is checked only if its BE could pass R6.

| Ticker | Stock | Ratings / low | Expiry | Chain (live / close Oct 8) | R6 | Verdict |
|---|---|---|---|---|---|---|
| PRVA | $20.45 | 17/1/0, $24 | Feb19 | $22.5C 0.50 / 2.20 (OI 95), close 0.98; $25C 0.00 / 1.50, no bid | not pulled | **KILL, R5** (ask 2.20; $25C has no bid and needs +22%) |
| BILI | $15.54 (+4.6%) | 34/1/0, $18.04 | Jan15 | $16C 1.32 / 1.56; $17C 0.99 / 1.19; $18C 0.81 / 0.91; $19C 0.55 / 0.73 | AM prints: +0.89, -6.11, -4.78, -7.09, +1.88, +3.81; median 4.29%, cap 6.44%, max BE **$16.54** | **KILL, R6** (cheapest passing-R5 strike would need BE > $19.2, +24%; even $16C at the bid is $17.32) |
| TNDM | $16.02 | 14/11/0, $18 | Jan15 | $17C 1.50 / 2.45 (OI 36); $18C 1.15 / 2.10 (OI 80) | not pulled | **KILL, R5** |
| ATS | $17.60 | 6/1/1, $20 | Dec18 | $20C 0.00 / 1.60, OI 0, close 1.43 | not pulled | **KILL, no market (R5)** |
| SRAD | $12.45 | 18/7/0, $13.69 | Dec18 | $12.5C 1.20 / 1.80; $15C 0.45 / 0.75 (OI 14,626), BE $15.75 at the ask (+26.5%) | not pulled | **KILL, R5** (ask 0.75), and $15.75 BE is above the $13.69 low (R4 too) |
| MDU | $18.76 | 6/3/0, $21 | Jan15 | $20C 0.30 / 0.75 (OI 120), mid 0.525 | AM prints: -6.69, +4.72, -4.14, +0.72, +3.70 (May 2025 bar missing); median 4.14%, cap 6.21%, max BE **$19.92** | **KILL, R6** (strike alone is above max BE) and R5 at the ask |
| KT | $17.99 | 20/2/0, $20.64 | Jan15 | $20C 0.00 / 2.95, OI 1 | not pulled | **KILL, no market (R5)** |
| CPRI | $14.61 | 10/8/0, $16 | Dec18 | $15C 1.20 / 1.65 (OI 621), close 1.58 | not pulled | **KILL, R5** (and $16 low under any $15C BE: R4) |
| KVYO | $17.62 | 23/2/0, $19 | Jan15 | $20C 1.55 / 1.95 (OI 1,296) | not pulled | **KILL, R5** ($20C BE $21.95 also above the $19 low: R4) |
| BEAM | $25.41 (+3.3%) | 14/2/0, $26 | Jan15 | $26C 3.40 / 3.70; $30C 1.25 / 3.60 | not pulled | **KILL, R5** (and the $26 low sits under every OTM BE: R4) |

## 3. Tally
10 moved, **10 killed** (PRVA, TNDM, ATS, SRAD, KT, CPRI, KVYO, BEAM on R5, several also R4; BILI and MDU on R6). ARDX: no order, ask still $0.70. CTMX still parked. 0k is finished except **RARE**. The $12-25 Dec/Jan pool is now fished out at this reserve: three to four months of time value on a $15-25 stock costs $1-3, and the line is $0.676.

## GLOSSARY
- **R2 / Rule 2 (Oct 8):** expiry at least 21 days after the later of the tool's date and last year's (LY) date; 10-Q deadline at least 5 trading days before expiry. "(f)" = `verified: false`.
- **R4 / Rule 4:** the lowest Buy target must be above breakeven.
- **R5 / Rule 5:** one contract's ask must fit the tier budget ($0.676/share at 3.5/5 on a $676.28 reserve).
- **R6 / Rule 6:** move to breakeven no more than 1.5x the median earnings-day move. Max BE = stock x (1 + cap). AM prints measured close-to-close on the print day.
- **BE / breakeven:** strike + premium paid.
- **Mark / mid:** halfway between bid and ask. The rules price off the real bid/ask, not the mark.
- **OI:** open interest, the number of contracts outstanding. OI 0-1 with no bid means there's no real market.
- **No market:** a $0.00 bid. Whatever you pay, you can't sell it back to anyone.
- **Dec18 / Jan15 / Feb19:** monthly expirations Dec 18 2026, Jan 15 2027, Feb 19 2027.
