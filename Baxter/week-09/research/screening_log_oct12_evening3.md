# SCREENING LOG: Mon Oct 12, 2026, EVENING 3 (10:00pm ET, VM)

**Session job:** EVENING 3 = refill the queue and leave PREMARKET a plan. The job EVENING 1 and 2 handed over: the **sub-$10 slice with no call-volume floor** (the only band where a real-money contract under the Rule 5 line can exist), then the **$10-25 band with no call-OI floor** (the 12:35 run screened it with OI >= 2,000). Market closed: every quote is Monday's regular-session close. Reserve (spendable) $676.28: Rule 5 3.5/5 line $0.676. 0 web searches.

**Scans** (saved, re-runnable): prints Oct 28 - Dec 11, market cap >= $300M, 52-week range pct < 0.25, no volume or OI floor.
- `Baxter Oct12 sub-10 Oct28-Dec11 prints, no vol floor` (`f0d34288`): $1-10 = 285 names (200 returned, $3.36-$10) + $0.50-3.37 = 94 names. **29 not seen anywhere in week-09 logs or passes.md.**
- `Baxter Oct12 10-25 Oct28-Dec11 prints, no OI floor` (`96ccaf83`): $10-25 = 227 names (200 returned, $10.63-$25) + $10-10.63 = 28. **21 not seen.**

So the no-floor slices were almost entirely names this week's runs already killed: 50 new out of ~400.

## Sub-$10, 29 new names

| Name | Price | Range pct | Ratings B/H/S, low target | Next fact | Result |
|---|---|---|---|---|---|
| MFI, LPTH, SUPV, XXI, HBNB, PSEC, TUYA, LVWR, OIO, SLI, EMAT, TRON, GERN, SNDL, WDH, LU, LOT, LDI | 0.59-9.20 | <0.25 | no coverage | | **KILLED, R3** (no coverage) x18 |
| MYGN | 4.12 | 0.235 | 1/5/3 | | **KILLED, R3** |
| BAK | 1.77 | 0.093 | 0/5/3 | | **KILLED, R3** |
| CLVT | 1.56 | 0.057 | 3/5/1 | | **KILLED, R3** (Buys < Holds) |
| EVO | 1.36 | <0 | 3/7/0 | | **KILLED, R3** |
| OPTU | 0.97 | 0.191 | 1/8/5 | | **KILLED, R3** |
| PROK | 1.67 | 0.170 | 4/2/1, low $1.00 | low under the stock | **KILLED, R4** (proxy) |
| NMG | 1.03 | 0.000 | 5/1/0, low $1.48 | Nov 11 AM (f) / LY Nov 12; Feb19 lowest strike $2.50 (only 2.50/5/7.50 listed) | **KILLED, R4** (every strike's BE > $1.48) |
| URG | 0.92 | <0 | 11/0/0, low $1.60 | `get_option_chains` empty | **KILLED, no options** |
| RLX | 1.72 | 0.079 | 5/2/0, low $2.09 | Nov 13 AM (f) / LY Nov 14 (ADR, both dates present); Jan15 $1.5C 0.15 / 0.75, OI 151; $2C 0.00 / 0.40 | **KILLED, R7** (OI 151, spread 133%) |
| ALLO | 1.39 | 0.102 | 10/1/0, low $4.00 | Nov 5 PM (f) / LY Nov 6: Nov20 fails R2 (14 days), Feb19 ok. Feb19 $1.5C 0.20 / 0.45, OI 930, BE $1.95 at the ask = **+40.3%**. Six prints (next-day close): -15.68, +2.88, +12.38, -2.83, -8.15, -4.35; median 6.25%, cap 9.38% | **KILLED, R6** (+40.3% vs 9.38%); also R7 at the close (spread 77%) |
| NFGC | 1.55 | 0.093 | 6/0/0, low $2.99 | tool has **no Q3 2026 row** (LY Nov 7); foreign filer, so both dates required. Jan15 $1.5C 0.25 / 0.35, OI 1,186, spread 33%; BE $1.85 = +19.4% | **KILLED, R2** (no tool date) + R7 (33%) |

## $10-25, 21 new names

| Name | Price | Ratings B/H/S, low target | Next fact | Result |
|---|---|---|---|---|
| CTEV, KELYB, EDN, FRPH, GLIBA, FG, TRC, ASIX, MEC, GTEN, IQMX | 10.10-24.33 | no coverage | | **KILLED, R3** (no coverage) x11 |
| OTEX | 24.04 | 2/13/0 | | **KILLED, R3** |
| MWA | 21.30 | 2/3/2 | | **KILLED, R3** (2 Sells) |
| CTRI | 20.54 | 3/2/2 | | **KILLED, R3** (2 Sells) |
| PRCT | 19.32 | 5/9/1 | | **KILLED, R3** |
| MCFT | 19.20 | 1/5/0 | | **KILLED, R3** |
| TIMB | 17.98 | 3/11/0 | | **KILLED, R3** |
| SNDX | 13.97 | 12/0/0, low $26 | Nov 2 PM (f) / LY Nov 3: Nov20 fails R2 (17 days). Jan15 $15C 2.30 / 5.70, OI 166 | **KILLED, R7** (paper; OI 166, spread 85%) |
| AIP | 21.34 | 7/0/0, low $30 | Nov 3 PM (f) / LY Nov 4: Nov20 fails R2. Jan15 $22.5C 2.65 / 3.80, OI 24 | **KILLED, R7** (paper; OI 24) |
| TYRA | 19.60 | 14/1/0, low $29 | Nov 4 PM (f) / LY Nov 5: Nov20 fails R2. Feb19 $20C 1.40 / 5.50, OI 7 | **KILLED, R7** (paper; OI 7) |
| BETA | 19.77 | 10/0/0, low $28 | Dec 3 AM (f) / LY Dec 4; Jan15 $20C 2.70 / 4.10, OI 322, BE $24.10 at the ask = **+21.9%** (+18.4% at the 3.40 mid). Four prints only (IPO Nov 2025; print-day close vs prior close): +1.15, +11.94, -2.58, -3.29; median 2.94%, cap 4.40% | **KILLED, R6** (paper; +21.9% vs 4.40%); also R7 at the close (spread 41%) |

**Moved:** 50 names, all killed. 0 advances. (Only 9 needed a chain: URG, RLX, ALLO, NFGC, NMG, SNDX, AIP, TYRA, BETA. The other 41 died free at the ratings screen.)

**Real-money check:** only ALLO, RLX, NFGC and NMG had a contract under the $0.676 line. ALLO's $1.5C ($0.45 ask) was the closest real-money contract tonight, and it needs a 40% move from a stock whose median print moves 6%.

**Pattern:** with the volume floor gone, the sub-$10 slice is mostly names with no coverage (18 of 29). The ones with coverage either have no Feb strike near the money (NMG), no December expiry, or an earnings history that can't reach breakeven. Under $10 and $10-25, the market is fished out through Dec 11 prints. The next new names come from moving the window: prints Dec 12 - Jan 31 (Jan/Feb/Mar expiries), which no run has scanned yet.

## GLOSSARY
- **R1-R7:** binder Tab 1 Iron Rules. R1 range percentile, R2 earnings before expiry, R3 analyst consensus, R4 lowest Buy target above breakeven, R5 affordability, R6 reachability (breakeven move <= 1.5x median earnings move), R7 liquidity floor (OI >= 250, spread <= 25% of mid).
- **R4 (proxy):** at screening, the lowest Buy target has to sit above the stock price, or no call strike can pass.
- **BE (breakeven):** strike + premium paid.
- **OI (open interest):** contracts outstanding on that strike.
- **Spread % of mid:** (ask - bid) / mid.
- **(f):** earnings date not company-verified.
- **LY:** the same quarter's report date last year.
- **Paper:** tracked-only, no money.
- **Foreign filer:** files 6-K/40-F instead of a 10-Q, so Rule 2 needs both the tool date and last year's date.
