# Screening log: Mon Oct 12, 2026, 2:35pm ET MIDDAY (VM, LIVE)

**Session job:** DO. Live queue re-tests (BTBT, ONDS real money; ALGM paper), then the chain stage for the four R3 survivors the 1:35 run queued (KNF, TPG, NYAX, GGAL). Live quotes ~18:35 UTC. Reserve (spendable) $676.28: Rule 5 3.5/5 line $0.676. Ratings via `get_equity_analyst_ratings` this run. No web searches, no WebFetch. SE / HII / ALNY not re-quoted: their only blocker is OI, which updates overnight (Tuesday OPEN).

## Live queue re-tests

| # | Name | Direction | Contract | Live quote | Stock | Test | Result |
|---|---|---|---|---|---|---|---|
| 1 | **BTBT** | CALLS (real money) | Jan15 $1C `25ebc8de` | 0.34 / 0.38, OI 2,242, spread 11.1% | $1.24 (-3.9%) | R6: BE at ask $1.38 vs max $1.342 (stock x 1.0823): needs +11.3% vs cap 8.23%. R7 passes. | **PARK, R6.** Worse than 1:35. Passes at stock >= ~$1.275 with a $0.38 ask. |
| 2 | **ONDS** | CALLS (real money) | Dec18 $8C `cfbc25b7` | 0.47 / 0.49, OI 37,622 | $6.75 (+0.3%) | R6: BE at ask $8.49 vs max $8.160 (stock x 1.2089): needs +25.8% vs cap 20.89%. | **PARK, R6.** Needs stock ~$7.02 at a $0.49 ask. |
| 3 | **ALGM** | CALLS (paper) | Nov20 $35C `832a1519` | 2.75 / 2.90, OI 6,791, spread 5.3% | $34.00 (-4.4%) | R6: BE at ask $37.90 vs max $37.57 (stock x 1.105): needs +11.5% vs cap 10.5%. | **PARK, R6.** Passes at stock >= ~$34.30 with a $2.90 ask. |

## Chain stage: 1:35's R3 survivors

| Name | Stock | B/H/S, low | Earnings / R2 | Contract checked | Quote / OI | Result |
|---|---|---|---|---|---|---|
| **KNF** | $49.48 | 6/4/1, low $54 | Nov 3 AM (f), LY Nov 4 AM. Nov20 is 16 days past Nov 4: **fails R2**. Listed expiries: Oct16, Nov20, Feb19, May21 (no Dec). Feb19 passes R2. | Feb19 $45C / $50C | 6.70 / 10.10, **OI 0**; 4.10 / 7.40, **OI 0** | **KILLED, R7** (OI 0, spreads 41% / 57%) and **R4** (BE at ask $55.10 / $57.40 vs low $54). |
| **TPG** | $44.82 | 13/4/0, low $47 | Oct 29 AM **verified**, LY Nov 4 AM. Nov20 is 16 days past Nov 4: **fails R2**. No Dec listed; Jan15 passes R2. | Jan15 $42.5C / $45C | 4.10 / 6.30, OI 159; 2.80 / 5.10, OI 36 | **KILLED, R4** (BE at ask $48.80 / $50.10 vs low $47) and **R7** (OI 159 / 36, spreads 42% / 58%). |
| **NYAX** | $44.40 | 6/2/0, low $68 | Nov 18 AM (f), LY Nov 19 | none | `get_option_chains` returns no chain | **KILLED, no listed options** (R5/R7 can't be met). |
| **GGAL** | $36.95 | 5/3/0, low $50 | Tool labels scrambled (rows dated 2025-11-25, 2026-03-04, 05-13, 08-25 carry 2021-2023 quarter labels). Last year's Q3 print reads as **Nov 25, 2025**. 6-K filer: Jan15 is 51 days past Nov 25, so R2 passes if this year's Q3 lands within ~4 weeks of LY. Needs one confirming web check. | Jan15 **$40C** / $38C / $37C / $36C | **2.00 / 2.60, OI 736**; 2.80 / 3.40 OI 60; 3.10 / 3.90 OI 23; 3.00 / 4.40 OI 0 | **PARK, R7 by a hair** on the $40C: spread 0.60 / mid 2.30 = **26.1%** vs 25%. OI passes. R4 passes on the tool low (BE at ask $42.60 vs $50, undated). **R6 not yet tested** (tool can't give clean print dates). Paper only ($260/contract). |

**Moved:** 7 names (3 queue re-tests, 4 to the chain stage). 0 entries, 3 kills (KNF, TPG, NYAX), 4 parked (BTBT, ONDS, ALGM, GGAL).

**Real-money entry:** none. BTBT and ONDS, the only names under the $0.676 line, both fail R6 on the live ask. No doc with this-run numbers exists for either exact contract.

**Pattern worth writing down:** two of the four (KNF, TPG) died first on Rule 2 at Nov20 because last year's print came a week later than this year's tool date, and the Dec gap in their listings pushed them to Jan/Feb, where the extra premium blew through a thin bear floor. A $45-50 stock with a low target only $3-5 above it has no call that clears R4 once you have to buy two months of extra time.

## GLOSSARY
- **R1-R7:** binder Tab 1 Iron Rules. R1 range percentile, R2 earnings before expiry (21-day cushion on the later of tool date and last year's date), R3 analyst consensus (calls: at most 1 Sell, at least 3 Buys, Buys >= Holds), R4 lowest Buy target above breakeven, R5 affordability, R6 reachability (breakeven move <= 1.5x median earnings move), R7 liquidity floor (OI >= 250, spread <= 25% of mid).
- **BE (breakeven):** strike + premium paid.
- **OI (open interest):** contracts outstanding on that strike.
- **Spread % of mid:** (ask - bid) / mid.
- **(f):** earnings date not company-verified.
- **LY:** last year's same-quarter report date.
- **ADR / 6-K filer:** foreign company; no 10-Q deadline backstop, so R2 needs both dates.
- **PARK:** alive, waiting on one specific check or price; stays on the queue.
