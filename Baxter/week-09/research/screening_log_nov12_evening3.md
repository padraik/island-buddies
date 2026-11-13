# Screening log, Thu Nov 12 EVENING 3 (10:00pm ET)

*Session 3 of 3. Job (from EVENING 2): the Nov 16 - Dec 22 window is fished out, so don't re-scan Thursday's close. Start the ~Dec 15 re-sweep early: run base scan `a5439121` (prints Feb 13 - Mar 20) and date-stage anything new against the Nov 9 EVENING 2 parks, so the December runs only have to chain-check. Nothing held. Real-money reserve $715.96 spendable, so the 3.5/5 R5 line is $0.716. Prices: Thursday 4pm close (scanner `Last`), after-hours where quoted. Spring chains (Mar19 / Apr16) don't carry real OI yet, so no chain checks tonight; every pass is a park.*

## Source: base scan `a5439121-241f-4a3d-8c3e-7fffa1a56e26` ("Baxter Nov9 E2 just-reported R1<0.25 Feb13-Mar20 prints callvol>=100")

Filters unchanged: market cap $300M+, earnings Feb 13 - Mar 20 2027, stock, R1 expression < 0.25, call volume >= 100. **200 rows, which is the scanner's cap** (162 on Nov 9). The result is truncated, so the December run has to use the four price-band copies defined in `screening_log_nov11_evening2.md` (Source 2), not this base scan. 129 of the 200 rows are under $25.

Diffed against every week-09 log: **9 never-worked names.** One free ratings call covered them plus the 24 real-money-sized parks from `screening_log_nov09_evening2.md`.

### New names

| Ticker | Last | R1 | B/H/S, low | Next print (`get_earnings_results`) | LY same quarter | Verdict |
|---|---|---|---|---|---|---|
| LOPE | $117.77 | 0.041 | no coverage | (scanner Feb 18) | | **KILLED R3** (no coverage) |
| MCY | $86.41 | 0.148 | no coverage | (scanner Feb 17) | | **KILLED R3** |
| PRDO | $29.07 | 0.231 | no coverage | (scanner Feb 19) | | **KILLED R3** |
| GRPN | $12.21 | 0.147 | no coverage | (scanner Mar 10) | | **KILLED R3** |
| GNW | $8.41 | 0.200 | no coverage | (scanner Feb 23) | | **KILLED R3** |
| DDD | $1.68 | 0.016 | no coverage | (scanner Mar 9) | | **KILLED R3** |
| HIMS | $19.73 | 0.207 | 5/14/0, $24 (stamp Nov 10) | (scanner Feb 23) | | **KILLED R3** (Holds 14 > Buys 5) |
| **COGT** | $29.08 | 0.084 | 11/1/0, $45 (55% over) | Q4 **Tue Feb 16 AM** `verified: false` | Feb 17 2026 AM | **PARK (Mar19 if large accelerated, else Apr16).** Later date Feb 17 + 21 = Mar 10, inside Mar19. Paper size at $29. |
| **CGEM** | $10.39 | 0.197 | 13/0/0, $23 (121% over) | Q4 **Tue Mar 9 AM** `verified: false` | Mar 10 2026 AM | **PARK (Apr16 only).** Mar 10 + 21 = Mar 31, past Mar19. Real-money size possible on a cheap OTM strike. |

### Nov 9 parks, re-rated on Thursday's close

Ratings are unchanged on all 24 (same counts and same lows as Nov 9). Every lowest target is still over the stock, so the R4 proxy holds on all of them. Thin ones: **ALHC $8 vs $7.50 (6.7%)**, **WULF $14 vs $13.05 (7.3%)**, CORZ $16 vs $14.46 (10.6%), EFC $13 vs $11.01 (18%).

| Still in the scan (R1 < 0.25) | Price / R1 |
|---|---|
| OCGN | $0.88 / 0.093 (under $1; scanner floor is $1 elsewhere, check listing status in Dec) |
| ALLO | $0.86 / -0.034 (under $1, new low) |
| TMQ | $2.05 / 0.020 |
| SANA | $2.06 / -0.049 (new low) |
| WVE | $3.24 / 0.011 |
| AQST | $3.65 / 0.189 |
| NUVB | $4.07 / 0.016 |
| MFA | $5.61 / -0.142 (new low; 3/3/0 is on the R3 line) |
| CIFR | $7.23 / 0.086 |
| PUMP | $7.42 / 0.117 |
| SNDX | $9.27 / 0.003 |
| GLUE | $9.50 / -0.011 |
| WULF | $13.05 / 0.174 |
| CORZ | $14.46 / 0.195 |
| DNN | $2.09 / 0.062 |
| SOUN | $3.61 / -0.024 |
| UUUU | $6.75 / 0.025 |

**Dropped out of the scan** (quoted live, close): CTMX $2.04, ALHC $7.50, BLZE $8.79 (+8.8% vs Nov 9's $8.08), BKD $8.96, EFC $11.01, ARLO $11.83, ZURA $1.24. All but BLZE are within 4% of their Nov 9 prices, so the likely cause is the 200-row cap or Thursday's call volume under 100, not R1. BLZE may have risen out of the bottom quartile. **All seven stay parked**; the December banded run (no call-volume floor) settles it.

## Tally

**9 new names to a verdict: 7 KILLED R3 (LOPE, MCY, PRDO, GRPN, GNW, DDD no coverage; HIMS 5/14/0), 2 PARKED (COGT Mar19/Apr16, CGEM Apr16).** 24 Nov 9 parks re-rated free, no change. 0 advanced, 0 buyable, 0 chain checks (spring chains too early), 0 searches.

**Parks list for the ~Dec 15 run (real-money size, 26):** OCGN, ALLO, CTMX, TMQ, SANA, WVE, AQST, NUVB, MFA, CIFR, PUMP, ALHC, BLZE, BKD, SNDX, GLUE, EFC, ARLO, WULF, CORZ, ZURA, DNN, SOUN, UUUU, **CGEM** (new). Paper size: the Nov 9 list of 35 plus **COGT** (new).

**December run, first steps:** (1) run the four banded copies of `a5439121` (no call-volume floor); (2) `get_option_chains` expirations on every park (many skip Jan15 -> Feb19 / Mar19); (3) filer status for the Mar19 vs Apr16 call; (4) chains for R5 / R6 / R7.

## GLOSSARY

- **R1 (range percentile):** (price - 52-week low) / (52-week high - 52-week low). Under 0.25 = calls candidate. A negative number means the price is under the low the scanner's 52-week window recorded (a fresh low).
- **R2:** earnings print proven to land before expiry: expiry 21+ days after the later of the tool date and last year's date, and the 10-Q / 10-K deadline 5+ trading days before expiry.
- **R3:** at most 1 Sell, at least 3 Buys, Buys >= Holds. "No coverage" fails it.
- **R4 proxy / R4:** the lowest analyst target must sit above the stock (screen) and above the call's breakeven (rule).
- **R5:** one contract's ask x 100 fits the conviction tier's share of reserve ($0.716/share at 3.5/5 tonight).
- **R6:** breakeven move no larger than 1.5x the median absolute earnings reaction over the last 4-8 prints.
- **R7:** open interest >= 250 and spread <= 25% of mid on the exact contract.
- **Park:** the name passed what can be checked now; the next check waits on a date (here ~Dec 15, when spring chains carry OI).
- **10-K quarter / filer status:** a December-quarter print goes in the annual 10-K. Large accelerated filers must file by Mar 1, accelerated by Mar 16, others by Mar 31, which decides whether Mar19 clears R2(b) or the play needs Apr16.
- **(f):** the tool's date is `verified: false`, estimated from cadence.
- **Scanner cap:** `run_scan` returns at most 200 rows; a 200-row result is truncated.
