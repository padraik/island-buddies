# SCREENING LOG: Thu Nov 5, 2026, EVENING 2 (8:00pm ET, VM)

*Session 2 of 3: write docs for chain survivors, chain the names EVENING 1 advanced. Stocks: official Thursday closes plus ~8pm after-hours prints. Options: Thursday 3:59pm closing quotes. R6 here uses the last 4 prints (binder allows 4-8), close to close, all PM reporters (print day to next day).*

**Market context:** after-hours bounce across the semis that fell Thursday: SPY AH $734.58 (+0.2% vs $733.00), QQQ $651.00 (+0.6%), MRVL +3.8%, LRCX +5.8%, ALAB +1.9%, WDC +2.0%, AEHR +1.9%.

## Names moved

| # | Ticker | Dir | Close / AH | R1 (AH) | Print (tool) | R/H/S, low | Result |
|---|---|---|---|---|---|---|---|
| 1 | **MRVL** | CALLS (paper) | 133.55 / 138.68 | 0.2425 close, **0.262 AH** | Tue Dec 1 PM (f); LY Dec 2 | 40/5/0, $175 | **DOC WRITTEN (`research_MRVL_paper.md`), GATED TWICE.** Jan15 $130C 20.60 / 20.95, BE $150.95 = +13.03% vs 13.61% cap (max ask $21.73). OI 4,124, spread 1.7%. Floor still undated (search: 2025 notes and BofA $200 May 13 2026, all from before the decline). R1 fails at the AH price; line ~$135.48. Meeting 4-1 to wait. |
| 2 | AEHR | CALLS (paper) | 49.16 / 50.09 | ~0.24 | Thu Jan 7 2027 PM (f); LY Jan 8 | 7/0/0, $90 | **KILLED R7 (Mar19; no Feb19 listed).** Prints Jan 8 +15.9%, Apr 7 +25.7%, Jul 14 +21.9%, Nov 2 +26.5%: median 23.8%, cap 35.7%. R6 passes easily ($50C 12.40 / 13.20, BE $63.20 = +28.6%). OI: $45C 4, $50C 37, $55C 51, $60C 88, $70C 51. Nothing near 250. |
| 3 | LRCX | CALLS (paper) | 185.20 / 195.90 | 0.199 | Wed Jan 27 2027 PM (f) | 30/5/0, $255 | **KILLED R6 + R7 (Mar19).** Prints Jan 28 +3.6%, Apr 22 -2.6%, Jul 29 +18.0%, Oct 21 -11.8%: median 7.67%, cap 11.5%. $170C 36.60 / 39.20 BE $209.20 = +13.0% at the close, OI 6. $180C BE $214.05 (+15.6%), OI 18. |
| 4 | WDC | CALLS (paper) | 267.63 / 272.96 | 0.211 | Thu Jan 28 2027 PM (f) | 23/7/0, $405 | **KILLED R6 + R7 (Mar19).** Prints Jan 29 -10.1%, Apr 30 -0.7%, Aug 5 -13.0%, Oct 22 -3.0%: median 6.55%, cap 9.8%. $240C 62.35 / 71.10 BE $311.10 (+16.2%), OI 26, spread 13%. $260C BE $320.55, OI 10. |
| 5 | TER | CALLS (paper) | 212.74 / 216.65 | 0.194 | Mon Feb 1 2027 PM (f) | 15/5/0, $340 | **KILLED R6 + R7 (Mar19).** Prints Feb 2 +13.4%, Apr 28 -19.4%, Jul 28 -0.4%, Oct 27 -3.2%: median 8.3%, cap 12.45%. $190C 48.60 / 52.80 BE $242.80 (+14.1%), OI 1. $200C OI 2. |
| 6 | ALAB | CALLS (paper) | 179.47 / 182.92 | 0.212 | Tue Feb 9 2027 PM (f) | 19/7/0, $225 | **KILLED R6 + R7 (Mar19).** Prints Feb 10 -21.4%, May 5 -0.8%, Aug 4 -12.0%, Nov 3 -4.4%: median 8.2%, cap 12.3%. $160C 45.85 / 51.65 BE $211.65 (+17.9%), OI 4. $170C OI 11. |
| 7 | NVT | CALLS (paper) | 98.38 / 99.10 | low | Fri Feb 5 2027 AM (f) | 18/4/0, $167 | **WATCH, floor undated.** One search: Barclays $83/$65, KeyBanc $60, Citi $90, RBC $143, Seaport $130. All undated or from earlier cycles. Tool low $167 is 70% over the stock. |

**Holdings fact check (also in the journal):** QUBT, FRMI, ACHR dates, ratings, and SEC all unchanged.

**Tally:** 7 moved. 0 buyable with real money. 1 doc written (MRVL, paper, gated). 5 killed at the chain (AEHR R7; LRCX, WDC, TER, ALAB R6 + R7). NVT stays on watch.

**Finding:** Mar19 is a dead expiry for this pool. Every big-cap semi tonight had Mar19 OI under 30 near the money. These are quarterly-cycle names whose liquid expiries are Dec, Jan, and the Jan 2027 LEAPS. A Jan/Feb print needs Mar19 to clear R2's 21-day cushion, and Mar19 hasn't built open interest yet. Expect that to change in mid-December. Until then, a Jan/Feb reporter in this band can't pass R7. EVENING 3 shouldn't spend chain checks on Mar19 names before about Dec 15.

## GLOSSARY

- **R1:** (price - 52-week low) / (52-week high - 52-week low). <= 0.25 is the calls band.
- **R2:** expiry at least 21 days after the later of the tool date and last year's date, and the 10-Q/10-K deadline at least 5 trading days before expiry.
- **R3 (calls):** at most 1 Sell, at least 3 Buys, and Buys at least equal to Holds.
- **R/H/S:** Buy / Hold / Sell rating counts from `get_equity_analyst_ratings`.
- **Floor-gated:** R4 passes on the number, but no Buy target is dated after the stock's decline (binder Tab 6), so no entry until one is.
- **R5:** one contract's ask x 100 at or under the tier cap on reserve (real money only; paper skips it).
- **R6:** move to breakeven <= 1.5x the median absolute earnings reaction (last 4-8 prints).
- **R7:** open interest >= 250 and spread <= 25% of mid on the exact contract.
- **AH:** after-hours trading price.
- **(f):** date estimated from cadence (`verified: false`).
- **OI:** open interest, the number of contracts outstanding.
