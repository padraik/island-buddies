# SCREENING LOG: Tue Oct 13, 2026, MIDDAY (10:35am ET, VM)

**Session job:** queue re-tests (BTBT, ONDS, ALGM on settled asks), then the first scan of the **Dec 12 - Jan 31 print window** (Jan/Feb/Mar/Apr expiries), which no run had touched. Reserve (spendable) $676.28: Rule 5 3.5/5 line $0.676. 0 web searches.

## Queue re-tests (live, ~10:35)

| Name | Contract | Quote | Stock | R6 | Result |
|---|---|---|---|---|---|
| BTBT | Jan15 $1C `25ebc8de` | 0.34 / 0.36, OI 2,252 | $1.235 (-0.4%) | BE $1.36 vs max $1.337 (x1.0823): needs +10.1% vs 8.23% | **PARK, R6** (closest it's been all week) |
| ONDS | Dec18 $8C `cfbc25b7` | 0.41 / 0.44, OI 37,782 | $6.635 (-0.5%) | BE $8.44 vs max $8.021: needs +27.2% vs 20.89% | **PARK, R6** |
| ALGM | Nov20 $35C `832a1519` | 1.90 / 2.40, OI 6,793 | $32.71 (-3.2%) | BE $37.40 vs max $36.14: needs +14.3% vs 10.5% | **PARK, R6** |

## Scanner: prints Dec 12 - Jan 31, market cap >= $300M, range pct < 0.25

Saved, re-runnable:
- `Baxter Oct13 sub-10 Dec12-Jan31 prints` (`fb230e63`): $0.50-10 = **6 names**.
- `Baxter Oct13 10-25 Dec12-Jan31 prints` (`1ffeb35d`): $10-25 = **5 names**.

Thin on purpose: most companies report calendar Q4 in February, so this window is mostly off-cycle fiscal years. The >$25 bands are still unscanned.

| Name | Price | Range pct | Ratings B/H/S, low | Next fact | Result |
|---|---|---|---|---|---|
| SPIR | 9.64 | 0.157 | no coverage | | **KILLED, R3** |
| EAD | 5.94 | 0.014 | no coverage (closed-end fund) | | **KILLED, R3** |
| HIX | 3.49 | 0.044 | no coverage (closed-end fund) | | **KILLED, R3** |
| TLRY | 3.32 | <0 | 3/7/0 | | **KILLED, R3** (Buys < Holds) |
| CAG | 13.63 | 0.141 | 1/12/6 | | **KILLED, R3** |
| APLD | 22.00 | 0.094 | 17/2/0, low $22.00 | low = the stock price; any call's BE sits above it unless deep ITM | **KILLED, R4** (proxy) |
| LEVI | 19.44 | 0.215 | 13/4/0, low $20.00 | BE must stay under $20 (+2.9%); a Feb/Mar strike near the money carries more than that in time value | **KILLED, R4** (proxy) |
| NG | 6.65 | 0.169 | 6/0/0, low $11.97 | Jan 21 AM (f) / LY Jan 22; 10-K (FY Nov 30) due ~Jan 29; **Mar19** passes R2. $7C 0.80 / 1.45 (OI 1,009, spread 58%); $8C 0.75 / 0.85 (OI 909), BE $8.85 = **+33.1%**. Print-day moves: -5.13, +15.00, +5.01, +4.23, -14.13, -1.26; median 5.07%, cap 7.61% | **KILLED, R6** (+33.1% vs 7.61%); $8C also over the R5 line |
| GLOO | 3.76 | 0.121 | 6/0/0, low $7.00 | Jan 13 PM (f) / LY Dec 17; Jan15 fails R2, **Apr16** ok. $5C 0.65 / 0.85 (OI 540, spread 27%), BE $5.85 = **+55.6%**; $7.5C 0.30 / 0.45 (OI 202). Four prints (next-day close): -3.05, +2.27, -5.91, -4.60; median 3.82%, cap 5.74% | **KILLED, R6** (+55.6% vs 5.74%); also R7 on both strikes |
| NNE | 13.86 | <0 | 7/1/0, low $22.00 | Dec 17 PM (f) / LY Dec 18 AM; **Jan15** passes R2 (28 days). $15C 1.65 / 1.85 (OI 611), BE $16.85 = **+21.6%**; $16C 1.35 / 1.45 (OI 305). Five prints: +1.96, +0.80, -0.63, -9.51, +7.94; median 1.96%, cap 2.94% | **KILLED, R6** (+21.6% vs 2.94%) |
| IPX | 14.80 | <0 | 6/0/0, low $26.00 | not worked this run (batch cap) | **QUEUED**: earnings (tool says Jan 29; foreign issuer? check 10-K vs 6-K), chain, print moves |

**Moved:** 13 (3 queue re-tests + 10 new). 10 kills (5 R3, 2 R4 proxy, 3 R6), 3 parked on R6. IPX queued for the next run. 0 entries.

**Pattern:** the near-the-money strike on every small cap in this window needs +20% to +55% to break even. Small caps with off-cycle fiscal years don't move that much on prints (median 2-5%). Expect the >$25 bands to do better on R6 and worse on R7, same as the Oct 28 - Dec 11 window did.

## GLOSSARY
- **R1-R7:** binder Tab 1 Iron Rules. R1 range percentile, R2 earnings before expiry (21-day cushion on the later of tool date and last year's date; 10-Q/10-K deadline at least 5 trading days before expiry; 6-K filers need both dates), R3 analyst consensus (calls: at most 1 Sell, at least 3 Buys, Buys >= Holds), R4 lowest Buy target above breakeven, R5 affordability (ask x 100 <= 10% of reserve at 3.5/5, $67.63 today), R6 reachability (breakeven move <= 1.5x median earnings move), R7 liquidity floor (OI >= 250, spread <= 25% of mid).
- **BE (breakeven):** strike + premium paid (at the ask).
- **(f):** the tool's date is `verified: false`, estimated from cadence.
- **LY:** last year's same-quarter report date.
- **Print-day move:** close-to-close change on the first session after the release (same day for AM prints, next day for PM).
- **R4 proxy:** a screening kill when the lowest Buy target is at or barely above the stock, so no normal call's breakeven can sit under it.
- **PARK:** alive, waiting on one specific price; stays on the queue.
- **OI:** open interest.
