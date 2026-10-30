# Screening log: Fri Oct 30, EVENING 1 (6:00pm ET)

**Source:** the live queue from Thursday EVENING 3 (HSAI, PL, NNE, INFQ, APLD, MIR, GLXY, HBAN, NLY, DX, FLG, TTWO), slide-in scan `696cbe51` (26 rows, R1 0.25-0.29), and early-sweep scan `e6411b30` on its $8.45-25 band (103 rows, up from 93 Thursday after today's selloff).
**Reserve / lines:** spendable $592.15 -> R5 line at 3.5/5 = **$0.59**. Nothing below clears it.
**Data:** Friday closing option quotes (stamped 19:59 UTC, so spreads are closing spreads), stock quotes with after-hours prints to ~22:00 UTC, analyst counts, earnings dates and 52-week ranges pulled live this run, earnings reactions from daily closes (`get_equity_historicals`). Searches this run went to holdings and the paper CAVA question, none to screening.

## Chain stage

| Ticker | Dir | Stock | Print | R3 / tool low | Contract | Bid / Ask | OI | Spread | BE / needs | Result |
|---|---|---|---|---|---|---|---|---|---|---|
| PL | CALLS | 13.45 (R1 0.071) | Wed Dec 9 PM (f), LY Dec 10 2025 PM; 10-Q deadline ~Dec 10 | 8/5/0, low $17, mean $30.36 (no date on the low) | **Jan15 $12C** / **$15C** / $17C | 2.70/2.90, 1.35/1.50, 0.85/1.00 | 2,329 / 1,815 / 1,445 | 7.1% / 10.5% / 16.2% | $14.90 +10.8%; $16.50 +22.7%; $18.00 +33.8% | **$12C and $15C pass R1, R2, R3, R4 (tool low, undated), R6 (median 26.0%, cap 39.0%), R7. R5 fails (paper only). ADVANCE to a paper doc, floor date is the gate.** $17C dead on R4 (BE $18 > low $17). |
| INFQ | CALLS | 8.88 (R1 0.039) | **Mon Nov 16 PM `verified: true`** (queue said Nov 30; first reported print was Aug 12 2026) | 6/1/0, low $12 | Dec18 $10C / $11C; Jan15 $9C / $10C / $11C | 0.60/0.80, 0.25/0.55; 1.25/1.40, 0.85/1.10, 0.65/0.75 | 1,036 / 1,016; 506 / 5,532 / 2,935 | 28.6% / 75.0%; 11.3% / 25.6% / 14.3% | Dec18 $10C $10.80 +21.6%, $11C $11.55 +30.1%; Jan15 $9C $10.40 +17.1% | **KILLED R6.** One print on record (Aug 12 -> 13, -1.5%). R6 asks for 4-8; even reading that one print, the cap is 2.2% against +17% or more. |
| HSAI | CALLS | 12.19 | Tue Nov 10 AM (v) | 24/1/0, low $15.51 | Dec18 $12.5C | 0.65/1.80 (vol 0) | **175** (was 226) | 93.9% closing | | **KILLED R7.** OI went the wrong way; the $12.5C can't reach 250 by a Nov 9 ramp sell without a real change. Paper watch ends. Saturday item 1 is gone. |
| NNE | CALLS | 11.64 (R1 0.013, $11.13 low printed today) | Thu Dec 17 PM (f), LY Dec 18 AM | 7/1/0, low $19 | Jan15 $12C / $13C / $14C / $15C | 1.20/1.55, 0.90/1.20, 0.65/0.90, 0.50/0.70 | 150 / 247 / 61 / 840 | 25.5% / 28.6% / 32.3% / 33.3% | $15C $15.70 +34.9% | **Parked, R7 at the close.** Every strike fails on spread, three on OI. Closing spreads run wide, and $13C is 3 OI short, so it stays on the queue, last in line. |
| ETOR | CALLS | 22.51 (R1 under 0) | Tue Nov 10 AM (v), LY Nov 10 | 10/5/0, low $27.50 | Dec18 $25C | 0.60/1.05 | 24 | 54.5% | $26.05 +15.7% | **KILLED R7 + R6** (last 5 prints -8.2, +8.2, +20.4, -2.9, -13.7, median 8.2%, cap 12.3%). |
| AIP | CALLS | 18.74 | Thu Nov 5 PM (v) | 7/0/0, low $25 | Dec18 $20C | 1.45/2.55 | 3 | 55.0% | | **KILLED R7** |
| BKSY | CALLS | 18.32 | Thu Nov 5 AM (v) | 6/1/0, low $33 | Dec18 $20C | 0.90/2.25 | 27 | 85.7% | | **KILLED R7** |

**PL reactions (close to close):** Sep 8 2025 AM +47.9%, Dec 10 2025 PM +35.0%, Mar 19 2026 PM +25.5%, Jun 4 2026 PM -26.0%, Sep 3 2026 PM -1.3%. Median of the absolute moves 26.0%, cap 39.0%. Sep 3 is the soft one: the stock fell 8.2% in that day's session on 32M shares, and the tool stamps the print PM. If the news actually hit during the session, that reaction is -8.2%, and the median holds at 26.0% either way. Jun 4 2025 was not pulled.

**What PL still needs before a paper doc passes:** a Buy-rated target dated inside 60 days and after the slide from $51 to $13. The tool's $17 carries no date. Ramp sell would be **Tue Dec 8 3:35pm** (trading day before the tool's Dec 9) until Planet announces.

## Already reported, next print in Jan/Feb

All six printed Q3 in October (`actual` filled). The next prints are `verified: false`, so these are next-quarter names.

| Ticker | Stock | Q3 reported | Next print (f) | R3 / tool low | Status |
|---|---|---|---|---|---|
| HBAN | 15.79 | Oct 22 AM | Thu Jan 21 AM | 16/7/0, $17 | Chain lists Feb19 and Mar19. Feb19 is 29 days past. Estimated R6 trouble: a bank's prints run small. Chain not pulled. |
| GLXY | 16.00 (-11.8% today) | Oct 27 AM | Tue Feb 2 AM | 15/1/0, $20.50 | Chain expiries not pulled |
| MIR | 18.35 | Oct 27 PM | Tue Feb 9 PM | 10/1/0, $20 | Chain expiries not pulled; low thin over the stock |
| NLY | 18.26 | Oct 20 PM | Wed Jan 27 PM | 9/4/0, $19.50 | Same, thin |
| DX | 10.68 | Oct 19 AM | Mon Jan 25 AM | 4/2/0, $11.50 | Same, thin |
| FLG | 10.50 | Oct 23 AM | Fri Jan 29 AM | 12/7/0, $11 | Same, thin |

**APLD** ($17.83, R1 0.005, new low $17.195 today): next print Wed Jan 6 PM (f), LY Jan 7. Jan15 is 9 days past, fails R2. The chain lists no Feb19 or Mar19; next expiry past that is Apr16. Stays on the queue until a February expiry lists. **TTWO:** low still $270, stamped Aug 7, 84 days old; not dated tonight. Saturday's call.

## Free screen: new or slid-in names

From `e6411b30` (R1 under 0.25, $8.45-25):

| Ticker | Buy/Hold/Sell | Tool low | Stock | Result |
|---|---|---|---|---|
| BLSH | 6/7/0 | $25 | 24.30 | KILLED R3 (Holds > Buys) |
| VITL | 5/6/0 | $8 | 8.74 | KILLED R3 |
| KLAR | 11/15/0 | $13 | 13.43 | KILLED R3 |
| JANX | 15/2/1 | $14 | 17.47 | KILLED R4 proxy (low under the stock) |
| ENOV | 12/1/0 | $24 | 19.85 | KILLED R4 dating: tool stamp is Apr 2022 |
| SA, WOLF, NN, HIMX, HNRG, CPS, PPTA, CEPU | none | | | KILLED no coverage |
| BETR, SHAZ, ELE, MLYS | re-rated | | | already logged this month, not re-chained |

From slide-in scan `696cbe51` (R1 0.25-0.29, all MID-OUT tonight):

- **R3 fails, off the watch:** MNDY 13/14, DOCS 8/13, AAP 2/23, BL 3/8, HUN 4/13, LYFT 15/33, SNAP 11/33, O 8/18, CAG 1/12.
- **R4 proxy fails:** VSH (low $26 vs $26.42).
- **No coverage:** AEHR, PSIX, RXT.
- **Clear R3 and the proxy, need R1 under 0.25:** B 15/5/1 low $42 ($37, Nov 9), WGS 8/0/0 low $83 ($69.06, Nov 9), HUT 24/1/0 low $90 ($59.40, Nov 4), BETA 10/0/0 low $28 ($20.05, Nov 3), SARO 13/3/0 low $25 ($23.48, Nov 10), COHR 25/6/0 low $262 ($211.50, Nov 4). HUT, BETA and COHR print too soon to be worth a chain. B and WGS go on the queue.

## Real-money read

Nothing under the $0.59 line passes R6. ONDS $6.32, SOUN $4.21, RCAT $4.62, BTBT $0.81 and CLSK $7.66 all moved further from their lines. SOUN's Dec18 $5C idea expires for the quarter: it needed ~$4.77 by about Mon Nov 2. OUST $29.74 prints Tue Nov 3, so it comes off too. QURE traded $27.10 after hours (+9.2% vs its $24.82 close), cause unread, and that puts it back in the middle of its range.

## Tally

14 names chain-checked or dated: PL advanced (paper), INFQ, HSAI, ETOR, AIP, BKSY killed, NNE and APLD parked, six moved to next quarter. 13 more killed free (BLSH, VITL, KLAR, JANX, ENOV, and 8 no coverage). 13 slide-ins cut (9 R3, VSH R4 proxy, 3 no coverage). 0 real-money candidates. PL is the one name for EVENING 2's doc.

## GLOSSARY
- **R1-R7**: binder Tab 1 Iron Rules (calls). R1 range percentile, R2 earnings before expiry, R3 analyst consensus, R4 bear floor (lowest target above breakeven), R5 price cap on reserve, R6 reachability (needed move <= 1.5x median earnings move), R7 liquidity (OI >= 250, spread <= 25% of mid).
- **BE**: breakeven at expiry = strike + ask.
- **OI**: open interest, contracts outstanding.
- **(v)/(f)**: earnings date verified by the company / estimated from cadence.
- **MID-OUT**: stock in the middle of its 52-week range, no play.
- **R4 proxy**: the screen-stage check that the tool's lowest target sits above the stock with room for a breakeven; the real R4 is on the exact contract.
- **R4 dating**: Tab 6, a floor only counts if it's dated inside 60 days and after the stock's decline.
- **Slide-in**: a name just above the R1 line that a further drop would bring in.
- **Ramp sell**: selling before the earnings print, into the elevated premium, instead of holding through it.
- **Closing spread**: the wider book quoted in the last minute of the session; not the same as a midday spread.
- **Paper**: tracked in the paper book, no money moves.
