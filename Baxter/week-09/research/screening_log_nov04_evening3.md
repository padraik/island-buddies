# Screening log: Wed Nov 4, 2026, EVENING 3 (10:00pm ET, VM)

*Reserve (spendable) $539.11. R5 3.5/5 line $0.539. Stock prices after hours ~10:00pm unless noted; option quotes are the 3:59pm closes. Sources: the EVENING 2 queue (NVT, DOX floor dating; NIO, CRDO re-reads), the slide-in scan `696cbe51` (R1 0.25-0.29, prints Oct 28 - Dec 23, call vol >= 300: 31 rows) and the early-sweep scan `e6411b30` (R1 < 0.25, $25+, prints Nov 3 - Feb 12, call vol >= 300: 147 rows). Both scans were diffed against every week-09 screening log; only names never logged, or logged names whose facts changed, were worked. R6 medians come from Robinhood daily closes around each `get_earnings_results` print date (PM reporters: print-day close to next close).*

| # | Ticker | Direction | Price | R1 | Next print (tool); LY | R/H/S | Verdict |
|---|--------|-----------|-------|----|-----------------------|-------|---------|
| 1 | NIO | CALLS (real) | 3.30 close, AH 3.40 | ~0.05 | Tue Nov 24 AM (f); LY Tue Nov 25 AM | 16/7/1 | **GATED (R4 dating).** Tool low $3.7131, stamp still Sep 1. No new search tonight (two last session found only undated/2025 notes). At $3.40 the R6 max ask on the $3C would be 1.0536 x 3.40 - 3.00 = $0.582, so price rules get easier, not harder. Gate unchanged. |
| 2 | CRDO | CALLS (paper) | 136.50 close, AH 133.09 | 0.209 | Mon Nov 30 PM (f); LY Dec 1 | 21/1/0 | **GATED, and R6 now fails at the AH price.** BE $159 at the 29.00 ask needs +19.5% from $133.09 vs the 18.68% cap. EVENING 2's warning line (~$133.50) is crossed after hours. Re-quote at Thursday's close before any paper entry. |
| 3 | NVT | CALLS (paper) | 112.82 close, AH 113.04 | 0.216 | Fri Feb 5 2027 AM (f); LY Fri Feb 6 AM | 18/4/0 | **WATCH, floor undated.** Tool low $167 (aggregate refreshed Nov 4 19:08 UTC, so the low survived the -12.9% day, but that's a refresh stamp, not a note date). One search: newest dated notes are Aug 2026 (Baird $200, UBS $225, RBC $200), all before the drop. Mar19 is the contract month. |
| 4 | DOX | CALLS (paper) | 43.66 close, AH 44.32 | ~0.0 | Tue Feb 2 2027 PM (f); LY Feb 3 PM | 4/4/0 | **KILLED R4 proxy.** Tool low $46 is only 3.8% over the AH price, 5.4% over the close; any Mar19 call's breakeven sits above it. R3 passes on the line (4 Buys = 4 Holds). One search: only 2025 and Feb 2026 notes (BofA/Stifel $97, Barclays $92), nothing after the Nov 3 print. |
| 5 | AMBA | CALLS (paper) | 60.36 | 0.249 | Tue Nov 24 PM (f); LY Tue Nov 25 PM | 7/5/0 | **KILLED R4 + R7 (Dec18).** New name. Low $65. Print moves: +16.8 / -18.8 / -14.9 / -21.4 / -0.8%, median 16.8%, cap 25.2%. Dec18: $57.5C 7.00 / 11.00 OI 9, $60C 5.80 / 9.80 OI 96, $62.5C 6.20 / 8.70 OI 8, $65C 3.70 / 7.70 OI 76. Every strike fails OI 250 and has a 34-70% spread, and every breakeven ($66.50-70.70) is above the $65 low. |
| 6 | JBL | CALLS (paper) | 255.79 | 0.277 | Wed Dec 16 AM (f); LY Wed Dec 17 2025 AM | 13/0/0 | **WATCH, R1.** New name. 52-week low $189.60 (wk of Nov 17 2025), high $428.93 (wk of Jun 15): the R1 0.25 line is **$249.43** (-2.5%). Tool low $378 is 48% over the stock: R3 and the R4 proxy pass with room. Jan15 expiry: 29 days after Dec 17, R2 passes. Paper-size (a $255 stock). If it closes at or under $249.43, an evening session pulls the Jan15 chain. |
| 7 | ETN | CALLS (paper) | 353.36 | 0.249 | Tue Feb 2 2027 AM (f); LY Tue Feb 3 AM | 23/6/1 | **ADVANCE to chain (paper).** New name. Tool low $381.62 (aggregate refreshed Nov 4) is 8.0% over the stock, on the proxy line. R3 passes (1 Sell). Mar19 is the first expiry that clears R2 (Feb 3 + 21 = Feb 24). Chain and R6 at Thursday EVENING 1. |
| 8 | ONTO | CALLS (paper) | 182.87 | 0.238 | Mon Nov 9 (tool) | 14/0/0 | **OUT on timing, next cycle.** New name. Prints in 3 trading days. Strong board (low $330). Recheck after the print for the Feb cycle. |
| 9 | SITM | CALLS (paper) | 427.30 | 0.279 | Wed Nov 4 (printed) | 13/1/0 | **OUT, quarter reported (+6.0% on the print).** New name. Recheck next cycle. |
| 10 | NBIS | CALLS (paper) | 136.01 | 0.276 | Thu Nov 12 | 17/8/1 | **KILLED R4 proxy.** New name. Tool low $84, under the stock. |
| 11 | RH | CALLS | 143.97 | 0.283 | Fri Dec 11 | 7/13/2 | **KILLED R3** (re-confirmed; 2 Sells, Holds over Buys). |
| 12 | BMNR | CALLS | 21.90 | 0.284 | Fri Nov 20 | none | **No coverage** (re-confirmed). |
| 13 | FWDI | CALLS | 6.44 | 0.260 | Fri Dec 11 | none | **No coverage** (re-confirmed; the only sub-$8.45 slide-in with a later print). |
| 14 | LZB | CALLS | 33.07 | 0.283 | Wed Nov 18 | none | **No coverage** (re-confirmed). |

**Scan diff:** `696cbe51` 31 rows, 3 never logged (JBL, SITM, NBIS). `e6411b30` 147 rows, 3 never logged (ETN, ONTO, AMBA). The other 172 rows are in this week's logs already with a kill or a timing note. Big movers in the rows that were already logged (not re-worked, facts noted): APP +20%, CAVA -12.6%, BROS -15.5%, Z -14.6%, HUBS -8.1%, SNAP -10.8%, QCOM -8.6%, VCYT -27.7%: all printed Nov 4, so they're out for this cycle.

**Holdings (fact check, not screening):** QUBT AH $6.38, FRMI AH $1.83, ACHR AH $4.15. Dates, ratings and SEC unchanged.

**Tally:** 14 moved. 0 buyable. 1 advanced to chain (ETN, paper). 2 to watch (JBL R1 line $249.43; NVT floor dating). 4 killed (DOX R4 proxy, AMBA R4 + R7, NBIS R4 proxy, RH R3). 3 no coverage. 2 out on timing (ONTO, SITM). NIO and CRDO gates unchanged; CRDO R6 now fails at the AH price.

**Finding:** the $25+ bottom quartile through Feb 12 is down to 3 never-logged names out of 147. Sub-$25 was fished out Tuesday. Saturday Nov 7's full sweep needs the print window rolled to Nov 16 - Mar 19 and new market-cap/price bands; re-running these scans again won't find anything.

## GLOSSARY

- **R1:** (price - 52-week low) / (52-week high - 52-week low). <= 0.25 is the calls band.
- **R2:** expiry at least 21 days after the later of the tool date and last year's date, and the 10-Q/10-K deadline at least 5 trading days before expiry.
- **R3 (calls):** at most 1 Sell, at least 3 Buys, and Buys at least equal to Holds.
- **R/H/S:** Buy / Hold / Sell rating counts from `get_equity_analyst_ratings`.
- **R4 proxy:** screening shortcut: tool low target well above the stock (more than ~8%) before a contract is picked.
- **R6:** move to breakeven <= 1.5x the median absolute earnings reaction (last 4-8 prints).
- **R7:** open interest >= 250 and spread <= 25% of mid on the exact contract.
- **(f):** date estimated from cadence (`verified: false`).
- **AH:** after-hours trade.
- **Slide-in scan:** names sitting just above the R1 line (0.25-0.29) that could drop into it with one bad day.
- **Paper:** tracked in `paper_book.md`, no money moves.
