# Jun 13 Weekend Screening Log

Baxter tracking what has been screened so context compacts don't lose the work.
Updated continuously. Last updated: Jun 13, 2026 (batch 11 complete, 3 passes written).

---

## Double-Check List (Aug21 May Be Missing Due to Script Issue)

Patrick flagged that the chain script may not always return Aug21 options even when they exist.
These need manual chain pull or re-run when Patrick is back:

| Ticker | Why Flagged | Fundamentals |
|--------|-------------|--------------|
| ZTS | Chain: Jun18, Jul17, Sep18 only -- no Aug21. Aug 11 earnings. 0 sells. 6.3% from 52-wk low. Sep18 cheapest OK ($110C) breakeven above bear floor ($95). If Aug21 $80-85C exists at ~$0.75, passes all rules. **HIGH PRIORITY** |
| FLUT | No Aug21 in chain. Sep18 options over $1.00. 21/26 buys. August earnings. **HIGH PRIORITY** |
| CE | No Aug21 in chain. Jul16 earnings (captured by Jul17), but stock 51% from low. Fails criterion 1. Lower priority. |
| DHR | Jul24 and Jul31 show "no calls in range." Aug21 exists ($230C at $0.65) but breakeven ($230.65) exceeds bear floor ($220). Jul24 might have options at lower breakevens. Check. |
| STE | Chain: Jun18, Jul17, Sep18 only -- no Aug21. **Aug 10 earnings. 0 sells. 16.7% from 52-wk low.** Sep18 $280C breakeven $280.80 above bear floor. If Aug21 $215-230C exists, this could be a 4/5 pass. **HIGH PRIORITY** |
| EFX | Chain: Jun18 only in useful range (Jul17 empty, no Aug21). July 21 earnings. 8% from 52-wk low. 0 sells from April data (needs verify). **MEDIUM PRIORITY** |
| GEHC | No Aug21 in chain. **Aug 5 earnings (16 days before Aug21). 0-1 sell ratings (conflicting -- needs verify). 18.5% from 52-wk low ($66.12 vs $58.75 low, $89.91 high).** Avg analyst target ~$79.72. If Aug21 ~$70C exists at $0.90, breakeven $70.90 likely below lowest bull target. **HIGH PRIORITY** |
| EQT | No Aug21 in chain. **Jul 28 earnings. 0-1 sell (conflicting sources). 15.5% from 52-wk low.** Jul31 $59C at $1.00 (breakeven $60.00) technically captures earnings but expires only 3 days post -- too tight. Need Aug21 if it exists. **HIGH PRIORITY** |
| PODD | Aug21 chain sparse -- deep OTM issue on $160 stock. **8.9% from 52-wk low. 0 sells. 21 Buy. Q2 earnings late Jul/early Aug (date unconfirmed).** $1.00 max premium forces very deep OTM on a $160 stock. Lowest bull target ~$165. Any Aug21 option near $160-170 at $0.70-1.00 has breakeven right at bear floor. Needs manual chain pull to find exact strikes. **MEDIUM PRIORITY** |

---

## Screening Results

| Ticker | Price | 52Wk Low | 52Wk High | % From Bottom | Earnings | Buy/Sell | Verdict | Reason Failed |
|--------|-------|----------|-----------|---------------|----------|----------|---------|---------------|
| KHC | -- | -- | -- | -- | -- | multiple sells | FAIL | Multiple sell ratings |
| PINS | -- | -- | -- | -- | -- | 1 sell | FAIL | Insider selling, 1 sell |
| ULTA | -- | -- | -- | -- | -- | 1 underweight | FAIL | Earnings too late, 1 sell-equiv |
| ZBH | -- | -- | -- | -- | -- | 2 sells | FAIL | Hold consensus, 2 sells |
| CMG | ~$32 | ~$26 | -- | -- | -- | 0 sells | FAIL | Stock bounced, premiums inflated |
| FLUT | -- | -- | -- | -- | Aug 6 | 0 sells | FAIL | No Aug21 in chain, Sep18 options over $1 (double-check) |
| ZTS | $79.23 | $73.29 | $167.38 | 6.3% | Aug 11 | 0 sells | FAIL | No Aug21 in chain, Sep18 breakeven above bear floor (double-check) |
| NOW | $102.88 | $81.24 | $211.48 | 16.6% | Jul 22 | 43 buy/1 sell | FAIL | Jul17 expires before earnings, Jul24 cheapest OK = $175C (breakeven $176 > bear floor) |
| MRK | $119.63 | $76.66 | ~$140 | ~70% | Jul/Aug | 17 buy/0 sell/11 hold | FAIL | Too far from 52-wk low (~70% from bottom) |
| PFE | ~$25 | $23.11 | $28.75 | -- | Jun 6 (just reported) | 29 buy | FAIL | No near-term catalyst -- just reported, next is October |
| HSY | $181.66 | $160.07 | $239.48 | 27.2% | Jul 29 | 9 buy/1 sell | FAIL | 1 sell rating, Neutral consensus |
| EL | ~$78 | $62.57 | $121.64 | 26.5% | Aug 19 | 11 buy/1 sell | WATCH | 1 sell, earnings 2 days before Aug21 expiry -- borderline |
| CI | $294.84 | $239.51 | $338.89 | 55.7% | Jul 30 | 22 buy/0 sell | FAIL | Too far from 52-wk low (55.7% from bottom) |
| HUM | -- | $212.45 | $406.46 | -- | late Jul | 10% buy/5% sell | FAIL | Sell ratings, Hold consensus |
| DHR | $184.30 | $161.91 | $242.05 | 27.9% | late Jul | 0 sells | INSTRUMENT | Aug21 $230C breakeven $230.65 > bear floor $220. Jul24 options "no calls in range" (see double-check) |
| ALGN | $170.50 | $122 | $208.31 | 56.2% | Jul 30 | 0 sells | FAIL | Too far from 52-wk low |
| GNRC | $282.36 | $120.44 | $294.18 | 93.2% | Jul 29 | 1 sell | FAIL | Near 52-week HIGH, 1 sell |
| SLB | $56.25 | -- | -- | -- | Jul 24 | 0 sells | FAIL | Bear floor (~$50) below Aug21 $67.50C breakeven $68.29 |
| CE | $53.48 | $35.13 | $70.70 | 51.6% | Jul 16 | 0 sells | FAIL+DC | Too far from low. No Aug21 in chain. |
| CPRI | -- | $13-16 | $28.27 | -- | May 27 (past) | 4 buy/0 sell | FAIL | Just reported, next catalyst uncertain |
| VRTX | $444.57 | $362.50 | $507.92 | 56.4% | Aug 3 | 1 sell | FAIL | Too far from low, 1 sell |
| AMGN | -- | $261.43 | -- | -- | Jul 30 | 3 sells | FAIL | 3 sell ratings |
| ELV | $404.07 | $273.71 | $426.98 | 85.1% | Jul 22 | 0 sells | FAIL | Near 52-week HIGH (recovered fully) |
| CELH | $29.35 | $27.47 | $66.74 | 4.8% | Aug 6 | 1 sell (Stifel?) | **PASS 3/5** | Conditional -- bear floor $37 (Stifel buy) vs $44 (Bernstein). **Doc written under_4_5.** |
| LULU | $118.77 | $109.36 | -- | ~5% | Sep 3 | Hold consensus | FAIL | Earnings too late (Sep 3 after Aug 21), Hold consensus |
| PANW | -- | $139.57 | -- | -- | Aug (FY Q4) | 1 sell | FAIL | 1 sell, earnings after Aug21 |
| SNOW | $240.45 | $118.30 | $284.99 | 73.3% | Aug 26 | 1 sell | FAIL | Earnings after Aug21, too far from low, 1 sell |
| STE | $207.56 | $195.14 | $269.44 | 16.7% | Aug 10 | 0 sells | DOUBLE-CHECK | No Aug21 in chain. Strong fundamentals -- see double-check list. |
| EFX | $163.71 | $156.47 | $275.91 | 6.1% | Jul 21 | 0 sells (Apr data) | DOUBLE-CHECK | Jul17 empty, no Aug21. Possible sell ratings added since Apr. See double-check. |
| ROKU | $139.28 | $73.91 | -- | ~68% | Jul 30 | 2 sells | FAIL | Too far from low, 2 sells |
| GEHC | $66.12 | $58.75 | $89.91 | 18.5% | Aug 5 | 0-1 sell (conflict) | DOUBLE-CHECK | No Aug21 in chain. Strong if sell count confirmed 0. See double-check. |
| EQT | ~$52 | -- | -- | ~15.5% | Jul 28 | 0-1 sell (conflict) | DOUBLE-CHECK | No Aug21 in chain. Jul31 only 3 days post-earnings. See double-check. |
| PODD | ~$160 | -- | -- | ~8.9% | late Jul/Aug | 0 sells | DOUBLE-CHECK | Deep OTM problem on $160 stock. Aug21 chain sparse. See double-check. |
| INTU | -- | -- | -- | -- | Aug 20 | 1 sell (Goldman) | FAIL | Earnings Aug 20 = same day as Aug21 expiry (fails Rule 2). Goldman Sell. |
| ADSK | $198.91 | $194.18 | $277.69 | 2.4% | Aug 27 | 0 sells | FAIL | Earnings Aug 27 AFTER Aug21 (Rule 2). Sep18 cheapest OK = $340C, breakeven $341 >> avg target $319-335 (Rule 4). |
| SCHW | $91.36 | $83.96 | $107.50 | 31.4% | Jul 16 | 1 sell | FAIL | Rule 1 fails at current price (31.4% from bottom). Was 15.5% on Jun 3 -- stock recovered. Aug21 $105C exists but entry window closed. |
| DG | -- | -- | -- | -- | -- | multiple | FAIL | Screened -- failed screening criteria |
| UNH | -- | -- | -- | -- | -- | multiple | FAIL | Screened -- failed screening criteria |
| SBUX | -- | -- | -- | -- | -- | multiple | FAIL | Screened -- failed screening criteria |
| DXCM | -- | -- | -- | -- | -- | multiple | FAIL | Screened -- failed screening criteria |
| HRL | -- | -- | -- | -- | -- | multiple | FAIL | Screened -- failed screening criteria |
| GIS | -- | -- | -- | -- | -- | multiple | FAIL | Screened -- failed screening criteria |
| MNST | -- | -- | -- | -- | -- | multiple | FAIL | Screened -- failed screening criteria |
| GILD | -- | -- | -- | -- | -- | multiple | FAIL | Screened -- failed screening criteria |
| MRNA | -- | -- | -- | -- | -- | multiple | FAIL | Screened -- failed screening criteria |
| DOW | -- | -- | -- | -- | -- | multiple | FAIL | Screened -- failed screening criteria |
| NTR | -- | -- | -- | -- | -- | multiple | FAIL | Screened -- failed screening criteria |
| VTRS | -- | -- | -- | -- | -- | multiple | FAIL | Screened -- failed screening criteria |
| LNC | -- | -- | -- | -- | -- | multiple | FAIL | Screened -- failed screening criteria |
| AGCO | -- | -- | -- | -- | -- | multiple | FAIL | Screened -- failed screening criteria |
| HBI | -- | -- | -- | -- | -- | multiple | FAIL | Screened -- failed screening criteria |
| SNAP | -- | -- | -- | -- | -- | multiple | FAIL | Screened -- failed screening criteria |
| MTCH | -- | -- | -- | -- | -- | multiple | FAIL | Screened -- failed screening criteria |
| ADBE | $204.02 | $196.90 | $405.00 | 3.4% | Sep/Oct | 3 sells | FAIL | 3 sell ratings (Rule 3). Just reported Jun 11 -- next catalyst is Sept/Oct (Rule 2). |
| PTC | $114.47 | $108.50 | $219.69 | 5.4% | Jul 29 | 1 sell (JPM) | **PASS 2/5** | All 5 rules pass. Aug21 $165C at $0.70, breakeven $165.70. Bear floor $185 (Barclays Buy). Conviction low -- 44.8% required move. **Doc written under_4_5.** |
| ENPH | $53.65 | $25.78 | $73.74 | 58.1% | Jul 21 | 4 sells | FAIL | Way too far from 52-wk low. 4 sell ratings. Double fail. |
| ADM | -- | $51.34 | $85.37 | -- | Aug 4 | 50% sell | FAIL | Massive sell consensus (50% of ratings). Accounting issues. |
| DVN | $45.32 | $31.45 | $52.71 | 65.2% | Aug 4 | 0 sells | FAIL | Rule 1 fails -- 65.2% from bottom. Recovered too much after 2025 lows. |
| OXY | -- | $38.80 | $67.45 | -- | Aug 5 | 1 sell + many Hold | FAIL | 1 sell, 11 Hold, only 7 Buy. Not clean enough on Rule 3. |
| VZ | -- | $38.39 | $51.68 | -- | Jul 21 | multiple downgrades | FAIL | Erste downgraded to Hold. Hold consensus, insufficient Buy ratings. |
| T | $23.56 | $22.32 | $29.79 | 16.6% | Jul 22 | 0 sells | **PASS 3/5** | All 5 rules pass. Aug21 $25C at $0.56, breakeven $25.56. Bear floor $26+ (lowest overall target). 0 sells. **Doc written under_4_5.** |

---

## Batches Run

- **Batch 1**: KHC, PINS, ULTA, ZBH, FLUT, CMG, ZTS
- **Batch 2**: ZTS (chain), NOW (chain), Sheldon letter intel
- **Batch 3**: MRK, PFE, HSY, EL, CI
- **Batch 4**: HUM, DHR (chain), ALGN, GNRC, SLB (chain)
- **Batch 5**: CE (chain), CPRI, VRTX, AMGN, ELV (chain), CELH (chain)
- **Batch 6**: LULU, PANW, SNOW, STE (chain), EFX (chain), ROKU
- **Batch 7**: GEHC (chain/double-check), EQT (chain/double-check), PODD (chain/double-check)
- **Batch 8**: INTU, ADSK (chain), SCHW (chain), DG, UNH, SBUX, DXCM, HRL, GIS
- **Batch 9**: MNST, GILD, MRNA, DOW, NTR, VTRS, LNC, AGCO, HBI, SNAP, MTCH
- **Batch 10**: ADBE, PTC (chain) -- PTC PASS, research doc written
- **Batch 11**: ENPH, ADM, DVN, OXY, VZ, T (chain) -- T PASS, research doc written

---

## Passes (Research Docs Written)

| Ticker | Conviction | Instrument | Catalyst | Doc Location |
|--------|------------|------------|----------|--------------|
| CELH | 3/5 (conditional) | Aug21 $40C at $1.00 | Aug 6 earnings | under_4_5/research_CELH.md |
| PTC | 2/5 (speculative) | Aug21 $165C at $0.70 | Jul 29 earnings | under_4_5/research_PTC.md |
| T | 3/5 | Aug21 $25C at $0.56 | Jul 22 earnings | under_4_5/research_T.md |

---

## Notes

- The fund has $200-300 of new capital coming from Patrick's weekend work.
- Target expiries: Jul17 (need catalyst by ~Jul 17), Aug21 (captures July earnings).
- Most instrument failures come from: no Aug21 in chain, or cheapest OK option has breakeven above bear floor.
- Many beaten-down stocks either have sell ratings (rightfully beaten down) or no nearby earnings catalyst.
- BSX WARNING (from Sheldon Jun 12): analyst floor dropped to $55, below our $60.73 breakeven. Flag for Patrick on return.
