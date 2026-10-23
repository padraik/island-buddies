# SCREENING LOG: Thu Oct 22, 2026, EVENING 2 (8:00pm ET)

*Market closed; quotes are the 4:00pm close. Session 2's job: write a research doc for every name past the chain stage. There was one (APH, paper), and it died on R1 before a doc was worth writing. That finished session 2's job early, so this session started EVENING 3's refill: the $25-100 band, prints Oct 28 - Dec 4. 1 web search (APH floor).*

## Held (fact check)

| Contract | Close quote | Stock | Earnings | Ratings / low vs BE | SEC since Oct 15 | Verdict |
|---|---|---|---|---|---|---|
| COUR $5C Nov20 | 0.45 / 0.65 (OI 3,257) | $5.075, AH $5.08 | Thu Oct 29 PM `verified: true`, `actual: null` | 8/4/0, low $6.00 vs BE $5.65 | none | Nothing changed. Ramp sell Thu Oct 29 3:35pm. |
| QUBT $7C Dec18 | 0.38 / 0.58 (OI 1,125) | $6.595, AH $6.52 | Fri Nov 13 PM `verified: false` (LY Nov 14 PM), `actual: null` | 5/2/0, low $10 vs BE $7.54 | none | Nothing changed. Ramp sell Thu Nov 12 3:35pm. |

## APH: KILLED, R1 (the scanner's percentile isn't split-adjusted)

- **What I found:** Amphenol split **2-for-1 in September 2026**. Unadjusted monthly bars: Aug close $158.55, Sep high $163.29, Sep close $84.30.
- **Split-adjusted 52-week range** (weekly bars, Oct 20 2025 - Oct 16 2026): high **$89.93** (week of Oct 5 2026), low **$59.005** (week of May 18 2026). At $73.08: (73.08 - 59.005) / 30.925 = **0.455. MID-OUT.**
- **Where EVENING 1's 0.022 came from:** the unadjusted range. Post-split low $76.74, pre-split high $178.52: (78.98 - 76.74) / 101.78 = 0.022, exactly what was written. The scanner's `low(candlePeriod="1w", candleCount=52)` / `high(...)` expression uses unadjusted candles. Tonight's re-run of the scan shows APH at -0.036.
- **The EPS quirk explained too:** the tool's Q3 estimate ($0.71) is on the pre-split share count; the history ($0.34 for Q2) is adjusted.
- **Floor search (1):** tipranks/the fly show "BofA raised Amphenol to $90 from $82, Buy" and later "$100 from $90". These are pre-split notes, so they don't date the tool's $90 low. Moot after R1.
- **Exposure check:** I compared unadjusted and split-adjusted monthly bars for every name we hold or track: COUR, QUBT, AVGO, MSTR, APP, NRG, FSLR, BABA, CAVA, BURL, TMUS, TTWO, ONDS, BTBT, CLSK. **All 15 are identical**, so no position or open paper entry rests on a split-distorted R1. APH was never entered.
- **Fix going forward (practice from tonight, binder note for a local session):** before a name gets a doc, re-compute R1 from `get_equity_historicals` (split-adjusted by default), not from the scanner column.

## Refill: new scan, $25-100, prints Oct 28 - Dec 4

Saved scan **`Baxter Oct22 E2 25-100 Oct28-Dec4 prints`** (`18ff4e43-ae7c-4ac0-b179-a09800e27598`): cap >= $300M, stock, $25-100, earnings Oct 28 - Dec 4, scanner range pct < 0.25. **202 matches, 200 returned** (sorted by price, so the two cheapest, near $25, were cut off; EVENING 3 can split at $30 to catch them). Only 8 of the 200 had never appeared in a research file (ECG, FLEX, AAOI, CECO, VPG, FLR, NGS, OUST).

**Free R3 screen (all 200, three ratings calls):** 120 pass R3 (<= 1 Sell, >= 3 Buys, Buys >= Holds). The other 80 fail R3 or have no coverage. Ranked the 120 by low target / price and checked the top 30 against this month's logs: 16 already have a chain-stage kill on file (ACMR, CELC, RAPP, GHM, INSM, TBN, LGN, HROW, AAON, LASR, ESAB, SE, MP, ROAD, WYNN, TPB). 14 had none. Took the top 10 of those to the chain.

**R1 re-done on split-adjusted monthly bars for all 10** (none split; scanner and bars agree):

| Ticker | Stock | R1 (adj.) | R3 | Low tgt | Q3 print (tool) | LY | R2 contract | Chain (close) | OI | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| FLEX | $76.69 (-11.1%) | 0.21 | 14/1/0 | $135 | Oct 28 AM (v) | Oct 29 AM | Nov20 (23 d) | $75C 6.70 / 10.80; $80C 5.90 / 6.60 | **19; 31** | **KILLED, R7** |
| ICHR | $37.90 (-12.6%) | 0.24 | 8/1/0 | $80 | Nov 2 PM (v) | Nov 3 PM | Dec18 | $40C 3.80 / 5.40 | **18** | **KILLED, R7** |
| OUST | $27.75 (-8.4%) | 0.24 | 6/1/0 | $52 | Nov 3 PM (v) | Nov 4 PM | Dec18 | $30C 3.20 / 3.70 | **72** | **KILLED, R7** |
| TREE | $27.56 | 0.09 | 6/0/0 | $45 | Nov 3 PM (v) | Oct 30 AM | Dec18 | $30C 1.50 / 2.40 | **1** | **KILLED, R7** |
| CECO | $53.22 (-8.6%) | 0.13 | 8/0/0 | $85 | Nov 3 AM (unv.) | Oct 28 AM | Dec18 | $55C 3.50 / 6.90 | **1** | **KILLED, R7** |
| ECG | $97.05 (-8.4%) | 0.20 | 5/3/0 | $152 | Nov 3 PM (v) | Nov 4 PM | Dec18 | $100C 7.40 / 9.60 | **0** | **KILLED, R7** |
| AAOI | $67.18 (-13.1%) | 0.23 | 6/3/0 | $92 | Nov 5 PM (v) | Nov 6 PM | Dec18 | $70C 9.80 / 10.60 | **75** | **KILLED, R7** |
| TATT | $31.44 | 0.00 (new low) | 7/0/0 | $53 | Nov 11 PM (unv.) | Nov 12 PM | n/a | no option chain | - | **KILLED, no options market** |
| BGSI | $83.44 | 0.05 | 14/1/0 | $120 | Nov 11 AM (v) | Nov 12 AM | n/a | no option chain | - | **KILLED, no options market** |
| IONQ | $30.90 (-4.3%) | 0.09 | 13/3/0 | $43 | Nov 5 PM (v) | Nov 5 PM | Dec18 | $30C 4.15 / 4.45 (OI 1,353); $35C 2.24 / 2.38 (OI 5,785) | pass | **KILLED, R6** (below) |

**IONQ R6 print table** (PM prints; next-day close vs print-day close): May 7 2025 **+9.27%**, Aug 6 2025 **-1.79%**, Nov 5 2025 **+3.65%**, Feb 25 2026 **+21.70%**, May 6 2026 **-9.30%**, Aug 5 2026 **-0.53%**. Median of absolutes **6.46%**, cap **9.69%**, line **$33.89**. The $30C needs +11.5% at the ask ($34.45), the $35C needs +21.0% ($37.38). No $31-33 strike in Dec18. Dead on R6 at every listed strike.

**Pattern:** the day's AI/hardware selloff (FLEX -11%, ICHR -13%, AAOI -13%, ECG -8%, CECO -9%) pushed fresh names into the bottom quartile, but the floors on most of them were set at much higher prices (low targets 1.6-2.1x the stock), so they'd need Tab 6 dating anyway. R7 got there first on seven of them.

## Paper correlation proposal (from WRAP, for a local session, not decided here)

Written up in `paper_correlation_proposal_oct22.md` in this folder.

## Tally

Researched past the free screen: **11** (APH R1; FLEX, ICHR, OUST, TREE, CECO, ECG, AAOI R7; TATT, BGSI no options; IONQ R6). **11 killed, 0 advanced.** Free R3 screen on 200 names (80 out). 1 web search. Real-money candidates: none. No name in this band has a near-money call under the $0.622 line.

**Left for EVENING 3 from this scan (no kill on file, not chain-checked):** KRUS ($34.41, 6/3/0, low $51), CALX ($36.91, 8/1/0, low $52), LTM ($47.22, 12/0/0, low $62.90), BMA ($62.95, 7/1/0, low $85), plus the 2 cut-off rows under ~$26 (split the scan at $30).

## GLOSSARY
- **R1-R7:** the binder's Iron Rules (Tab 1). R1 range percentile, R2 earnings before expiry, R3 analyst consensus, R4 lowest Buy target above breakeven, R5 affordability, R6 reachability, R7 liquidity floor (OI >= 250, spread <= 25% of mid).
- **Range percentile (R1):** (price - 52-week low) / (52-week high - 52-week low). Bottom quartile (< 0.25) is a calls candidate; 0.25-0.75 is MID-OUT.
- **Split-adjusted:** historical prices divided by the split ratio so a 2-for-1 split doesn't look like a 50% crash. The scanner's high/low expression is not adjusted; `get_equity_historicals` is (default `adjustment_type: split`).
- **OI:** open interest, contracts outstanding. **Spread:** ask minus bid, as a share of the mid.
- **(v) / (unv.):** `get_earnings_results` verified flag: company-announced vs estimated.
- **LY:** last year's same-quarter report date.
- **Median print / cap:** median absolute next-day move over the last six prints; R6 allows a breakeven move up to 1.5x that.
- **Tab 6 dating:** a floor counts only if the Buy target is dated within 60 days and published after the decline.
- **Paper book:** tracked-only positions, entered at the ask and exited at the bid, no money.
