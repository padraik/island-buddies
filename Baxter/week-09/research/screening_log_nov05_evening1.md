# Screening log, Thu Nov 5, EVENING 1 (6:00pm ET, VM)

*Reserve (spendable) $539.11. R5 3.5/5 line $0.539 (real money). Stock prices are the 4:00pm closes unless noted; option quotes are the 3:59pm closes. Sources: the EVENING 3 queue (ETN, JBL, CRDO, NIO, PL, NVT, ONDS) and fresh runs of the early-sweep scan `e6411b30` (R1 < 0.25, prints Nov 2 - Feb 12, call vol >= 300: **179 rows, up from 147 last night**) and the slide-in scan `696cbe51` (R1 0.25-0.29: 26 rows). R6 medians use Robinhood daily closes around each `get_earnings_results` print date (AM reporters: prior close to print-day close; PM reporters: print-day close to next close).*

**Market context:** Thursday was a broad selloff, not a basket problem: SPY $766.81 -> $733.25 (**-4.4%**), QQQ $691.95 -> $647.77 (**-6.4%**), IWM $284.02 -> $271.05 (**-4.6%**). Semis and AI hardware led the drop (AVGO -10.5%, AMAT -13.6%, MRVL -16.6%, ALAB -20.0%, CRDO -17.7%, WDC -17.5%). Two searches did not find a dated cause. One hit ("Broadcom outlook and rate concerns send Nasdaq-100 down 4.1%") describes Broadcom's December 2025 print, not today, so it is not used. AVGO's Q4 is still unreported (Dec 9).

## Queue names

| # | Ticker | Dir | Price | R1 | Print (tool) | R/H/S, low | Result |
|---|---|---|---|---|---|---|---|
| 1 | ETN | CALLS (paper) | 326.63 | ~0.08 | Tue Feb 2 2027 AM (f); LY Feb 3 | 23/7/1, $381.62 | **KILLED R6 + R7 (Mar19).** Median of 6 prints 4.87% (7.36, 2.29, 0.86, 2.74, 7.32, 7.00), cap 7.31%, max BE $350.50. Best: $310C 45.60 / 49.00, BE $357.30 (+9.4%), OI 21. $320C-$350C BE $362-379, OI 5-90. No strike clears either rule. |
| 2 | JBL | CALLS (paper) | 236.37 | 0.195 | Wed Dec 16 AM (f); LY Dec 17 | 13/0/0, $378 | **R1 now passes (under the $249.43 line). KILLED R6 + R7 (Jan15).** Median 4.23% (8.89, 6.69, 1.76, 1.40, 0.14, 10.03), cap 6.34%, max BE $251.36. $220C 32.90 / 36.00 BE $256.00 at the ask (+8.3%), OI 19. $250C is the only OI >= 250 (326) and needs +13.7%. |
| 3 | CRDO | CALLS (paper) | 112.37 | well under 0.20 | Mon Nov 30 PM (f); LY Dec 1 | 21/1/0, $235 | **GATED (floor), R7 near-miss.** Jan15 $110C 19.30 / 25.40: BE $135.40 at the ask = +20.5% vs the 18.68% cap (BE $132.35 at the mark = +17.8%, inside). OI 209, spread 27% of mid: **R7 fails** on both counts. $115C OI 114, $120C OI 200 and BE +22.4%. Floor still undated (nothing after Oct 12). Doc `research_CRDO_paper.md` stays; no paper entry. |
| 4 | NIO | CALLS (real) | 3.195 | ~0.03 | Tue Nov 24 AM (f) | 16/7/1, $3.7131 | **GATED (R4 dating).** Tool low stamp still Sep 1. R6 max ask on the $3C at $3.195 = 1.0536 x 3.195 - 3.00 = $0.366. Gate unchanged; no search. |
| 5 | PL | CALLS (paper) | 11.365 | low | (doc) | 8/5/0, $17 | **GATED.** -10.2% today. DB $28 still ages out Sat Nov 7. No new search. |
| 6 | NVT | CALLS (paper) | 98.37 | low | Fri Feb 5 2027 AM (f) | 18/4/0, $167 | **WATCH, floor undated.** -12.8% today, the tool low is now 70% over the stock, which is a stale-floor shape (Tab 6). Needs a target dated after the drop. |
| 7 | ONDS | CALLS (real) | 4.52 | low | Thu Nov 12 AM (v) | 11/0/0, $13 | **$7C Dec18 dropped for this cycle.** Needed a $6.20-6.30 stock by Mon Nov 9; it closed 4.52 (-14.2%), 37% away. Name stays on watch for the Feb cycle. |

## New and never-tabled names from `e6411b30` (18 worked)

| # | Ticker | Dir | Price | R1 | Print (tool) | R/H/S | Low tgt | Result |
|---|---|---|---|---|---|---|---|---|
| 8 | AMAT | CALLS (paper) | 319.33 | 0.220 | Thu Nov 12 PM (v) | 36/5/0 | $515 | **KILLED R6 (Dec18).** Median 5.19% (5.25, 14.07, 1.25, 8.08, 0.89, 5.12), cap 7.78%, max BE $344.17. $310C 34.90 / 39.65 BE $349.65 (+9.5%), OI 659. $320C BE $354.15. R7 passes; R6 doesn't. |
| 9 | SMTC | CALLS (paper) | 91.52 | 0.217 | Mon Nov 23 PM (f); LY Nov 24 | 16/1/0 | $186 | **KILLED R6 (+R7 at $85).** Median 7.48% (4.56, 15.14, 2.53, 11.00, 4.41, 10.41), cap 11.23%, max BE $101.80. $90C 13.40 / 15.50 BE $105.50 (+15.3%), OI 514. $85C BE $102.70 (+12.2%), OI 26. Low $186 has no stamp and is double the stock: would have needed dating anyway. |
| 10 | **MRVL** | CALLS (paper) | 133.32 | 0.242 | Tue Dec 1 PM (f); LY Tue Dec 2 PM | 40/5/0 | $175 | **ADVANCE to doc (paper), FLOOR-GATED.** Jan15 $130C (`58aa8b18-f266-481a-a745-967069362a51`) 20.60 / 20.95, BE **$150.95 = +13.2%** vs cap **13.61%** (median 9.07%: 5.55, 18.60, 7.87, 18.35, 3.09, 10.28). OI 4,124, spread 1.7%: R7 passes. R2: Jan15 is 44 days after Dec 2; 10-Q deadline ~Dec 11, well clear. R4: low $175 is $24 over BE, but the aggregate stamp (Nov 4) isn't a note date and the stock fell 16.6% today; needs one Buy target dated after the drop. $135C BE $153.50 fails R6. **R6 margin is thin (0.4 pts): a lower close fails it.** |
| 11 | AEHR | CALLS (paper) | 49.14 | 0.229 | Thu Jan 8 2027 (f) | 7/0/0 | $90 | **ADVANCE to chain** (Feb19 or Mar19). R3 and the R4 proxy pass with room. |
| 12 | LRCX | CALLS (paper) | 184.59 | 0.195 | Thu Jan 28 2027 (f) | 30/5/0 | $255 | **ADVANCE to chain** (Mar19). |
| 13 | WDC | CALLS (paper) | 267.31 | 0.198 | Fri Jan 29 2027 (f) | 23/7/0 | $405 | **ADVANCE to chain** (Mar19). |
| 14 | TER | CALLS (paper) | 212.54 | 0.177 | Tue Feb 2 2027 (f) | 15/5/0 | $340 | **ADVANCE to chain** (Mar19). |
| 15 | ALAB | CALLS (paper) | 178.64 | 0.198 | Wed Feb 10 2027 (f) | 19/7/0 | $225 | **ADVANCE to chain** (Mar19; Feb 10 + 21 = Mar 3). |
| 16 | BIDU | CALLS | 78.85 | 0.034 | Mon Nov 16 | 29/6/1 | $70.02 | **KILLED R4 proxy** (low under the stock). |
| 17 | NVDA | CALLS | 182.00 | 0.224 | Tue Nov 17 | 69/3/1 | $180 | **KILLED R4 proxy** (low under the stock). |
| 18 | ALK | CALLS | 38.07 | 0.203 | Fri Jan 22 2027 | 16/1/1 | $33 | **KILLED R4 proxy** (low under the stock; aggregate stamp 2019). |
| 19 | PDD | CALLS | 82.99 | 0.164 | Wed Nov 18 | 28/12/2 | | **KILLED R3** (2 Sells). |
| 20 | INTU | CALLS | 354.85 | 0.238 | Thu Nov 19 | 20/13/2 | | **KILLED R3** (2 Sells). |
| 21 | CRWV | CALLS | 43.11 | <0 | Tue Nov 10 | 33/11/3 | | **KILLED R3** (3 Sells). |
| 22 | TSLA | CALLS | 343.51 | 0.229 | Thu Jan 28 2027 | 24/23/3 | | **KILLED R3** (3 Sells). |
| 23 | NOW | CALLS | 100.35 | 0.185 | Thu Jan 28 2027 | 44/3/2 | | **KILLED R3** (2 Sells). |
| 24 | ARM | CALLS | 165.80 | 0.187 | Thu Feb 4 2027 | 32/15/2 | | **KILLED R3** (2 Sells). |
| 25 | SMCI | CALLS | 26.88 | 0.221 | Wed Feb 3 2027 | 4/13/4 | | **KILLED R3** (4 Sells, Holds over Buys). |

**Out on timing, from the scan, not counted:** VIAV (printed Nov 4), MTSI (printed Nov 5), SEI (printed Nov 5).
**Not worked tonight (scan rows with no table row this week, Saturday's sweep picks them up):** CAT, DECK, IP, WHR, HESM, ENPH, FORM, BSX, MGM, ON, GNRC, TSEM, BWA, COIN, HOOD.
**Slide-in scan `696cbe51` (26 rows):** nearly all printed Nov 4-6 or print Nov 9-10. Later prints sitting just above the line: GIS (Dec 17), CHWY (Dec 10), AS and ZTO (Nov 17), CLBT (Nov 12). Watch only.

**Holdings (fact check, not screening):** QUBT $5.635, AH $5.55; FRMI $1.52, AH $1.52; ACHR $3.86, AH $3.84. Dates (Nov 9 PM / Nov 12 AM / Nov 9 PM, all `verified: true`), ratings (5/2/0 $10, 6/2/0 $6, 8/2/0 $7) and SEC (FRMI newest still the Nov 4 8-K; QUBT, ACHR nothing since Nov 4) unchanged.

**Tally:** 25 moved. 0 buyable with real money. 1 advanced to doc (MRVL, paper, floor-gated). 5 advanced to chain (AEHR, LRCX, WDC, TER, ALAB). 4 killed at the chain (ETN R6 + R7, JBL R6 + R7, AMAT R6, SMTC R6). 10 killed at the free screen (BIDU, NVDA, ALK R4 proxy; PDD, INTU, CRWV, TSLA, NOW, ARM, SMCI R3). Gates unchanged: NIO, PL, CRDO (now also R7). NVT watch. ONDS $7C dropped this cycle.

**Finding:** a -4.4% day refilled the $25+ bottom quartile (147 -> 179 rows), but almost all of it is AI semis and hardware, the same factor that just cost the paper book $1,965 on AVGO in one day. Every advancer tonight is that one trade. Also, IV jumped with the drop (AMAT Dec18 at 74%, MRVL Jan15 at 81%), which pushes breakevens out and is why AMAT and SMTC died on R6 the same day their R1 got good. For the real fund, nothing in this pool fits a $53.90 line.

## GLOSSARY

- **R1:** (price - 52-week low) / (52-week high - 52-week low). <= 0.25 is the calls band.
- **R2:** expiry at least 21 days after the later of the tool date and last year's date, and the 10-Q/10-K deadline at least 5 trading days before expiry.
- **R3 (calls):** at most 1 Sell, at least 3 Buys, and Buys at least equal to Holds.
- **R/H/S:** Buy / Hold / Sell rating counts from `get_equity_analyst_ratings`.
- **R4 proxy:** screening shortcut: tool low target well above the stock (about 10%+) before a contract is picked.
- **Floor-gated:** R4 passes on the number, but no Buy target is dated after the stock's decline (binder Tab 6), so no entry until one is.
- **R5:** one contract's ask x 100 at or under the tier cap on reserve (real money only; paper skips it).
- **R6:** move to breakeven <= 1.5x the median absolute earnings reaction (last 4-8 prints).
- **R7:** open interest >= 250 and spread <= 25% of mid on the exact contract.
- **BE:** breakeven, strike + premium.
- **IV:** implied volatility; higher IV = pricier options = breakeven further away.
- **(f) / (v):** date estimated from cadence (`verified: false`) / company-announced (`verified: true`).
- **AH:** after-hours trade.
- **Slide-in scan:** names sitting just above the R1 line (0.25-0.29) that could drop into it with one bad day.
- **Paper:** tracked in `paper_book.md`, no money moves.
