# SCREENING LOG: Tue Oct 27, 2026, EVENING 3 (10:00pm ET)

*Market closed; stock quotes are Tuesday's close (after-hours noted), option quotes are the closing book (~3:59pm). EVENING 2's finding was that open interest builds into a print (FRMI and RCAT cleared R7's OI line a week after their R7 kills), so this session re-quoted the rest of the Oct 14-21 R7 kills, then ran the daily slide-in scan. 0 searches.*

## Held (fact check)

| Contract | Close quote | Stock | Earnings | Ratings / low vs BE | Verdict |
|---|---|---|---|---|---|
| COUR $5C Nov20 | 0.20 / 0.35 (OI 3,357, closing-minute quote) | $4.75 close, AH $4.77 | Thu Oct 29 PM `verified: true`, `actual: null` | 8/4/0, low $6.00 vs BE $5.65 | Unchanged. Sell window opens Wed; hard deadline Thu Oct 29 3:35pm. GTC $1.65 `confirmed`. |
| QUBT $7C Dec18 | 0.56 / 0.70 (OI 1,175) | $6.87 close, AH $6.90 | Mon Nov 9 PM `verified: true`, `actual: null` | 5/2/0, low $10 vs BE $7.54 | Unchanged. Ramp sell Mon Nov 9 3:35pm. GTC $1.35 `confirmed`. |

## Committed doc (re-check)

| Contract | Close quote | Stock | Earnings | Ratings / low | Verdict |
|---|---|---|---|---|---|
| FRMI $2.5C Dec18 | 0.45 / 0.60, OI 345, spread 28.6% | $2.62 close, AH $2.64 | Thu Nov 12 AM `verified: true`, `actual: null` | 6/2/0, low $6 | Unchanged from 8pm. R7 still fails at the close; daytime gate. Max ask = min($0.622, stock x 1.2003 - 2.50) = $0.622 at $2.62. |

## Re-quote of the Oct 14-21 R7 kills (Dec18 calls, closing book)

| Ticker | Stock | Print | Ratings / low | Contract: bid / ask, OI, spread | Verdict |
|---|---|---|---|---|---|
| EXK | $7.82 | Nov 9 | 6/1/0, low $10.73 | $7.5C 0.90 / 1.00, OI 59; $9C 0.30 / 0.50, OI 33, 50% | **KILL STAYS, R7** (OI went down, not up). $7.5C also R5. |
| CTMX | $2.31 | Nov 5 PM (f) | 8/0/0, low $6 | $2C 0.15 / 1.05, OI 0; $3C no bid / 0.75, OI 200 | **KILL STAYS, R7** |
| BTGO | $5.65 | Nov 30 | 11/2/0, low $7.50 | $5C 0.70 / 1.45, OI 17, 70%; $7.5C no bid / 0.25 | **KILL STAYS, R7** (and R5) |
| RGNX | $6.60 | Nov 5 | 10/2/0, low $10 | $7C / $8C no bid / 4.90, OI 0 | **KILL STAYS, R7** (no market) |
| EQX | $10.43 | Nov 9 PM v | 12/0/0, low $13.74 | $11C 0.55 / 0.70, OI 150, 24%; **$12.5C 0.20 / 0.25, OI 490, 22%** | **KILL STAYS.** $11C: R7 (OI 150) and R5 ($0.70 > $0.622). $12.5C clears R7 now, but BE $12.75 = +22.2% vs the R6 cap (median 5.86-8.78%, cap <= ~13.2%): **R6**. |
| ANNX | $3.745 | Nov 9 PM (f) | 9/2/0, low $7 | $4C 1.15 / 1.55, OI 184; $5C 0.95 / 1.25, OI 7,048, 27% | **KILL STAYS, R5** (asks over $0.622) + R7 spread; $5C BE $6.25 = +67%, R6. |
| AESI | $9.08 | Nov 2 PM (f) | 7/6/1, low $11 | $10C 0.60 / 0.90, OI 103, 40%; $12.5C 0.15 / 0.30, OI 756, 67% | **KILL STAYS, R7** (spread on both) |
| SLDB | $6.19 | Nov 2 PM (f) | 14/0/0, low $11 | $6C 0.10 / 4.90, OI 3; $7C no bid, OI 18 | **KILL STAYS, R7** (no market) |
| ALM | $9.565 | Nov 2 AM (f) | 11/1/0, low $13.08 | $10C 1.00 / 1.45, OI 185, 37%; $12.5C 0.35 / 0.50, OI 125, 35% | **KILL STAYS, R7** |
| PUMP | $7.81 (Oct 21) | Wed Oct 28 AM v | 7/5/0 | not re-quoted | **DROPPED, R2 spent:** prints before Wednesday's open. |
| BOBS | $15.96 | Nov 6 PM (f) | 11/2/0, low $18 | not re-quoted (no Dec18; Feb19 OI 9 on Oct 21) | **KILL STAYS, R7** on the last quote. Stock +21% since Oct 21, so R1 has likely gone too (not computed). |
| ZVRA (queue #2) | $10.055 (AH $9.61) | Mon Nov 3 PM | 9/0/0, low $20 | $10C 0.80 / 1.80, OI 632, 77%; $11C 0.45 / 1.10, OI 1,123, 84% | **KILLED, R5 + R7.** Both asks are over the $0.622 line, both spreads are 3x R7's limit, and the print is Monday. No doc can be written in time. |

**Result: 12 names moved, 12 killed or kept dead, 0 advanced.** EVENING 2's finding held for only one of these 11 (EQX's $12.5C now clears R7, and it fails R6). The OI-builds-into-a-print effect is real on names with a crowd (FRMI, RCAT). On these, it didn't show up.

## Source: slide-in scan `696cbe51` (saved; R1 0.25-0.29, prints Oct 28 - Dec 23, call volume >= 300)

32 rows. Diff against every week-09 file, passes.md and paper_book.md: **0 never-logged names.** Nothing new slid toward the bottom quartile Tuesday.

## Pool status

Three sources tonight (EVENING 1's five Oct24 SAT scans, EVENING 2's call-volume scan, this slide-in), all diffed: 5 + 0 + 0 new names. passes.md Keep Watching holds only ONDS (already on the watch line). This month's bottom-quartile pool with prints before Christmas is fished out. The live queue can't honestly reach 10 tonight. The Saturday Oct 31 full sweep is the next real refill, and it should add January prints (Dec 24 - Feb 12) with the call-volume floor, since Jan15/Feb19 expiries are where next month's names will trade.

## GLOSSARY

- **R1-R7:** the Iron Rules, binder Tab 1. R1 range percentile (bottom 25%), R2 earnings before expiry with the 21-day cushion, R3 Buy consensus (<= 1 Sell, >= 3 Buys, Buys >= Holds), R4 lowest Buy target above breakeven, R5 price vs the conviction-tier cap, R6 required move <= 1.5x the median print reaction, R7 OI >= 250 and spread <= 25% of mid.
- **Range pct:** where the stock sits in its 52-week range, 0 = at the low, 1 = at the high.
- **(f) / v:** earnings date from the tool, `verified: false` (estimated) / `verified: true` (company-announced).
- **OI (open interest):** contracts outstanding on that exact strike and expiry.
- **Spread %:** (ask - bid) / midpoint.
- **Slide-in scan:** a saved scan of names sitting just above the bottom quartile (0.25-0.29), run daily to catch names about to cross into R1.
- **Kill stays:** a name killed earlier, re-checked tonight, still dead on the same rule.
- **R2 spent:** the earnings print happens before any entry could be made, so the catalyst is gone.
