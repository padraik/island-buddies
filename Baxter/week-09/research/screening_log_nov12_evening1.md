# Screening log: Thu Nov 12, EVENING 1 (6:00pm ET)

*Thursday's close. Real fund all cash, spendable $715.96. Rule 5 line: 10% x $715.96 = $0.716/share at 3.5/5, $1.00/share transitional lock at 4/5+. Sources: the live queue's gates, slide-in scan `696cbe51` (R1 0.25-0.29, prints Oct 28 - Dec 23, call vol >= 300), losers scan `2a4b3aa6` (R1 < 0.25, prints Nov 16 - Dec 22, call vol >= 100), each re-run on Thursday's close. Searches spent: 3 (POWL target, BABA cause, BZ cause).*

## Live queue gates

| Name | Book | Close (Thu) | Ratings / low / stamp | Print | Gate | Verdict |
|---|---|---|---|---|---|---|
| **POWL** | paper | $141.74 (-2.9%), R1 0.209 | 3/3/0, $235, no stamp | Mon Nov 16 PM verified | (1) Buy target dated after Oct 12 and above $150.20 | **Gate still shut.** One search. The only dated hit was "Roth MKM reissued Buy, $350, Wednesday November 19th," which is a future date tonight, so it's either last year's note or a broken aggregator. Not usable as a floor. Friday EVENING 1 is the last evening the window allows (ramp sell would be Mon Nov 16 3:35pm). |
| **NIO** | real | $3.04 (-6.2%), AH $3.06 | 16/7/1, $3.6983, stamp **Sep 1** | Q3 Nov 24 AM (f), LY Nov 25 | floor dated after the decline; date on or before Nov 27 | **Gate still shut.** No 6-K date notice yet (last year's came Nov 12). Tool date unchanged. No chain spent: the floor gate fails first. |
| **CRDO** | paper | $139.85, AH $140.64, R1 0.244 | 21/1/0, $235, no stamp | FQ2 Tue Dec 1 PM verified | floor dated after the slide | Gate shut. $235 is a target for a $250+ stock. |
| **PL** | paper | $13.90, R1 0.083 | 8/5/0, $17, no stamp | FQ3 Thu Dec 10 PM verified | dated floor | Gate shut. No dated floor since DB's $28 aged out Nov 7. |

## Watch list

| Name | Close | Ratings / low | Verdict |
|---|---|---|---|
| MRVL | $164.48 (AH $166.23) | 40/5/0, $175 (Nov 7) | R1 out (line ~$135.5). Watch. |
| GNRC | $192.84 | 19/5/0, $232 (Nov 5) | R1 out (line ~$175). Watch. |
| ONDS | $5.32 (-7.2%) | 11/0/0, $13 | Feb cycle. Watch. |
| NVDA | $166.04 (AH $166.89), R1 0.035 | 59/13/1, **$174** (stamp today; was $180) | Dead this quarter (R6 structural, median 3.2%, cap 4.8%). The low fell $6 today. Noted for the paper book's AI read only. |

## Slide-in scan `696cbe51` (10 rows, all R1 0.25-0.29, so none is a calls candidate tonight)

| Name | Last | R1 | Print | Ratings / low | Verdict |
|---|---|---|---|---|---|
| CIEN | $295.50 | 0.271 | Dec 11 | 19/5/0, $347 | R1 out; stays dead (paper-size R6, Nov 5) |
| ADBE | $238.61 | 0.281 | Dec 10 | (R3 kill Nov 6) | stays dead R3 |
| TJX | $135.98 | 0.280 | Nov 18 | (R1 + R4 proxy Nov 6) | stays dead |
| AMBA | $61.17 | 0.266 | Nov 25 | 7/5/0, $65 | R1 out; stays dead (R4 + R7, Nov 4) |
| BIRK | $35.80 | 0.282 | Dec 18 | 20/5/1, $27.04 | **R1 out, R4 proxy fails** (low under the stock) |
| CHWY | $22.83 | 0.272 | Dec 10 | (R4 proxy Nov 6) | stays dead |
| CPB | $22.19 | 0.267 | Dec 9 | 1/14/8 | **KILLED R3** |
| **GAP** | $21.28 | 0.282 | Nov 19 | 11/14/0, $21 | **New name. KILLED R3** (Holds > Buys) and R4 proxy ($21 low under $21.28). |
| CAG | $14.55 | 0.259 | Dec 18 | 1/12/5 | **KILLED R3** |
| SVRA | $4.83 | 0.289 | Nov 12 | 9/0/0, $9 | stays dead (R6, Oct 23) |

## Losers scan `2a4b3aa6` (65 rows, was 67 Wed; 0 never-worked; Thursday's biggest movers re-rated)

| Name | Last (chg) | R1 | Print | Ratings / low / stamp | Verdict |
|---|---|---|---|---|---|
| **BZ** | $12.51 (**-25.2%**) | -0.005 (under its 52w low) | Q3 Nov 24 AM (f); LY Nov 18 AM | 20/4/0, $16.99, stamp **Aug 26** | **KILLED R7 + R5.** First time in the Nov/Dec window with R1/R3/R4-proxy all passing. 6-K filer: R2 passes on Dec18 (Nov 24 + 21 = Dec 15). No 6-K since Nov 5, `actual: null`, so not already reported. Dec18 chain on a $2.50 grid: **$12.5C 0.50 / 1.80**, OI **0**, spread 113% of mid (R7 + R5 fail); **$15C 0.15 / 0.20**, OI 681, spread **28.6%** of mid (R7 fail), BE $15.20 = **+21.5%** (R6 would need a 14.3% median print; not computed, R7 kills first). Also the floor is stamped Aug 26, before the drop, so it would fail the dating rule anyway. **Cause of the -25% is unread**: one search returned only old-quarter guidance stories. Watch: if a Buy target lands after today and the $15C spread tightens, it's worth one more look before Dec 4. |
| GDS | $20.00 (-11.6%) | -0.020 | Nov 19 | 16/0/0, $30.00 (Oct 1) | stays dead R7 (Nov 6), no re-quote |
| VNET | $3.09 (-11.5%) | 0.016 | Nov 23 | 17/0/0, $4.60 (Oct 29) | stays dead R7 (Nov 6) |
| SHAZ | $23.57 (-10.8%) | 0.087 | Nov 16 | 8/0/0, $80 | stays dead R7 |
| ASMB | $20.22 (-9.6%) | 0.050 | Nov 17 | no coverage | **KILLED R3** |
| TME | $9.02 (-2.2%) | 0.095 | Nov 17 | 23/13/0, $9.109 (Oct 27) | R4 proxy now passes by 9c, but any call BE is over $9.11: **stays dead R4** |
| XP | $15.10 | 0.070 | Nov 17 | 9/4/0, $14.54 | stays dead R4 proxy |
| ORCL | $127.60 | 0.130 | Dec 10 | 36/5/1, $110 | R4 proxy fails |
| BIDU | $77.88 | 0.023 | Nov 16 | 29/6/1, $69.96 | R4 proxy fails |
| ALM | $7.81 (-4.3%) | 0.125 | **Q3 Nov 24 AM (f)**, LY Nov 3 | 11/1/0, $12.98 | Tool date moved from Nov 2 (f) to Nov 24 (f), still `actual: null`. Stays dead R7 (Oct 27 and Oct 28: no strike passed both halves). Not re-quoted. |
| DY | $225.26 | 0.103 | Nov 19 | 12/1/0, $375 | stays dead R7 (paper) |
| GGAL | $29.50 | 0.007 | Nov 25 | 5/3/0, $43 | stays dead R7 |
| AGX | $315.44 | 0.113 | Dec 4 | 4/2/1, $273 | stays dead R4 proxy |
| RCAT | $3.99 | 0.048 | Nov 16 | 7/1/0, $6 | stays dead R6 |
| no coverage (R3) | | | | | BMNR, CRML, POET, XXI, BULL, ASPI, UROY, VZLA, IESC, BBW, JMIA |

## Paper book

- **BABA cause (one search):** China tech risk-off. Weak consumer data and renewed worry about Alibaba's AI and cloud spending (negative free cash flow, a quarterly operating loss last print) hit China large-cap tech together: BABA -6.8%, BZ -25%, GDS -11.6%, VNET -11.5%, BIDU -2.4%, PDD -2.0%. Nothing company-specific found, and the search summary mixed dates, so treat the cause as **medium confidence**. Rule 4 holds (45/1/0, $140.92, stamp Nov 10, vs BE $118.55). Paper ramp sell Wed Nov 18 3:35pm.
- GOOGL $298.75 (AH $299.51), $1.25 under its $300 target; 64/8/0, low $300 (Nov 7).
- **FRMI reaction (real, closed Wed at $0.10):** Q3 Thu AM EPS -0.22 vs -0.07 (miss); the stock closed $2.065 (+14.1%) anyway, still $0.435 under the $2.50 strike. The $2.5C closed 0.15 / 0.25: +$5 at the bid if held. One counterfactual for the sweep agenda, not a rule question (WRAP wrote it up).

**Moved tonight:** 25 names got real work: 4 queue gates, 4 watch, 6 slide-ins re-pulled (CIEN, AMBA, BIRK, CPB, GAP, CAG), and 11 losers re-pulled (BZ chained; GDS, VNET, SHAZ, ASMB, TME, XP, ORCL, BIDU, ALM, DY). The other rows (SVRA, ADBE, TJX, CHWY, GGAL, AGX, RCAT, the 11 no-coverage names) carry earlier verdicts or were cut in the same free pulls, and aren't counted. Searches: 3. **Killed:** BZ (R7 + R5), GAP (R3, new), CPB, CAG, ASMB (R3). **Advanced:** 0. **Buyable real-money docs:** 0.

**Finding:** China tech fell as a group today, and two names with real Buy consensus went under their 52-week lows (BZ, GDS). Both died on the same thing as before: the chains near the money don't trade. The Nov/Dec window is still empty at real-money size.

## GLOSSARY

- **R1 (range percentile):** (price - 52-week low) / (52-week high - 52-week low). Under 0.25 = calls candidate.
- **R2:** earnings print proven to land before expiry: expiry 21+ days after the later of the tool date and last year's date, and the 10-Q / 10-K deadline 5+ trading days before expiry (6-K filers: both dates required, no deadline test).
- **R3:** at most 1 Sell, at least 3 Buys, Buys >= Holds.
- **R4 / floor gate:** the lowest Buy target must sit above the call's breakeven, and be dated within 60 days and after the stock's fall.
- **R4 proxy:** the screening version: lowest target above the stock price.
- **R5:** one contract's ask must fit the conviction tier on reserve ($0.716/share at 3.5/5 tonight, never above $1.00 until the unlock).
- **R6:** breakeven move no larger than 1.5x the median absolute earnings reaction over the last 4-8 prints.
- **R7:** open interest >= 250 and spread <= 25% of mid on the exact contract.
- **Ramp sell:** selling before the print into the pre-earnings premium (binder Tab 4).
- **(f) / verified:** `get_earnings_results` date is an estimate (false) or company-announced (true).
- **AH:** after-hours trading, after the 4pm close.
- **6-K:** the current-report form foreign issuers (NIO, BABA, BZ) file instead of an 8-K.
- **BE (breakeven):** strike + premium paid.
- **OI:** open interest, the number of contracts outstanding.
