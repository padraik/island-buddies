# Screening Log: Mon Oct 5, 2026, OPEN run (VM)

**Source:** live scanner, saved scan "Today's losers with earnings window" refreshed to market cap $300M-$150B, earnings Oct 12 - Nov 9. 395 matches, 200 returned with usable 52-week range data (scan sorts by today's % change ascending, so this is today's weakest 200). 91 in the bottom quartile = CALLS raw pool. Puts are off (hard limit: long calls only), so the top quartile wasn't pulled.

**Rule 5 line this run:** reserve = spendable cash $450.78. Under $500 the 20%-of-reserve cap governs: 0.20 x 450.78 / 100 = **$0.90/share max ask**.

**Prices pulled 9:35-9:38am ET, first minutes of the session.** Option spreads were opening-wide; the asks below are real but some will tighten.

## Funnel

| Stage | Names | Tool |
|---|---|---|
| Scanner, bottom quartile | 91 | run_scan / update_scan_filters |
| Rule 3 (max 1 Sell) + coverage | ~55 pass | get_equity_analyst_ratings (2 batches) |
| Rule 2 date check | 8 checked, all unverified, all fit cadence | get_earnings_results |
| Chain check (cap 5) | 5 | get_option_chains / instruments / quotes, Nov 20 calls |
| Rule 6 history | 2 (CWH pass, MIR kill) | get_equity_historicals, 6 prints |
| Survivors | **1: CWH**, research continues | |

## Chain-checked (5 of 5)

| Ticker | Direction | Price | Earnings (tool) | Low tgt | Contract tried | Bid/Ask | Breakeven | Needs | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| CWH | CALLS | $4.565 | Oct 27 PM (unverified) | $6.00 | $5C Nov20 | 0.30 / 0.45 | $5.45 | +19.4% | **ADVANCE.** R6 median 15.93%, cap 23.90%: passes at 81% of cap. R4 $6.00 > $5.45. |
| MIR | CALLS | $14.33 | Oct 27 PM (unverified) | $20.00 | $17.5C Nov20 | 0.05 / 0.75 | $18.25 | +27.4% | **KILL, R6.** $15C ask 1.45 fails R5; $17.5C needs +27.4% vs cap 16.00% (6-print median 10.67%: +1.0, -11.1, +18.1, -10.2, -0.1, -13.2) |
| CDRE | CALLS | $24.62 | Nov 3 PM (unverified) | $43.00 | $25C Nov20 | 0.05 / 4.90 | -- | -- | KILL, R5/liquidity: open interest 0 on the near strikes, $30C bid 0.00. No usable instrument. |
| BKSY | CALLS | $21.70 | Nov 5 AM (unverified) | $33.00 | $30C Nov20 | 0.50 / 1.05 | $31.05 | +43% | KILL, R5 ($1.05 > $0.90) and R6 (+43% on a strike that fits nowhere near a reachable move) |
| AMRC | CALLS | $20.93 | Nov 2 PM (unverified) | $32.00 | $25C Nov20 | 0.55 / 1.95 | $26.95 | +29% | KILL, R5 ($1.95 > $0.90); $30C would need +43%, R6 |

### CWH Rule 6 detail (prior close -> next-day close, all PM prints)

| Print | Close | Next close | Move |
|---|---|---|---|
| 2025-04-29 | 14.08 | 12.06 | -14.3% |
| 2025-07-29 | 17.64 | 14.93 | -15.4% |
| 2025-10-28 | 16.82 | 12.65 | -24.8% |
| 2026-02-24 | 10.85 | 9.06 | -16.5% |
| 2026-04-29 | 6.93 | 8.19 | +18.2% |
| 2026-07-29 | 6.05 | 6.30 | +4.1% |

Median |move| 15.93%, Rule 6 cap 23.90%. Passes on magnitude. **Direction flag: 4 of 6 down**, the two most recent up. Bearxter will have something to say.

**Open on CWH before any doc:** (1) why it's -9% this morning (one search found only older news: Truist cut $20 -> $15 keeping Buy, Moody's downgrade); (2) the date of the $6.00 low target (binder Tab 6: within 60 days and published after the decline); (3) one confirming search on Oct 27 (tool says unverified); (4) estimate revisions (no browser here: cap 3.5/5 if unverified).

## Rule 3 kills (2+ Sell ratings)

CHRW (2), SAH (2), GPI (2), OPEN (2), INFY (6), CCOI (2), NTLA (3), GPK (2), TROX (3), BRSP (2), ENPH (3), SEDG (6), MOS (2), ARE (4), WIT (19), HTZ (4), ROL (3).

## No analyst coverage (can't evaluate Rule 3/4)

ABR, NTGR, MRAM, ECX, ABAT, FBRT, WLFC, CLPT, NNI, MNRO, MBC, DFH, FIP, NN, VNDA, HYMC, ORC.

## Rule 3 pass, not chain-checked this run (queue candidates)

Strongest floor-over-price margins at a price where a sub-$0.90 call can be reachable: MRP ($22.68, low $35, Oct 22 AM), AEVA ($14.33, low $20, Nov 4 PM), CIFR ($15.27, low $18, 23 Buy/0 Sell), LRMR ($2.87, low $5), PRME ($2.94, low $4.25), RWT ($3.46, low $5.22), MFA ($7.24, low $10), PCT ($4.13, low $6), LASR ($40.01, low $81, likely R5 on price).
Others passing R3: NXH, LQDA, INSM, NVTS, GTN.A, OI, AN, UWMC, ABG, FER, TMDX, LUNR, ALGN, CORZ (low $16 vs $16.01, R4 effectively dead), CMG, NKTR, PRTA, EVEX, IREN, QBTS, ARRY, ALT, ORA (targets dated 2022, stale), EOSE, KREF, XRAY, VSEC, SITE, INDI, TKO, WSO, VMRK, CDRE, OWL, OSK, FAF, EFC, CRH, FNF, NXT, VITL, HLNE, RYAAY, ONT.

## GLOSSARY

- **Bottom quartile / range percentile:** where the price sits between the 52-week low (0%) and high (100%). Under 25% = calls candidate. Negative means it's trading below last year's weekly low, a fresh low.
- **Rule 3:** at most one Sell/Underperform rating among covering analysts.
- **Rule 4 (bear floor):** the lowest analyst target must sit above the call's breakeven (strike + premium). The tool reports the lowest target overall, which is at or below the lowest Buy target, so passing on it is conservative.
- **Rule 5:** one contract's ask must fit the cap, here $0.90/share (20% of a $450.78 reserve).
- **Rule 6 (reachability):** the move to breakeven can't exceed 1.5x the stock's median earnings-day move over its last 4-8 prints.
- **Breakeven:** strike + premium paid; the stock price at expiry where the call neither makes nor loses money.
- **Open interest (OI):** contracts currently outstanding. Zero means nobody holds any; a quote there isn't a market.
- **Unverified date:** `get_earnings_results` estimated it from the company's cadence; the company hasn't announced it.
- **Kill:** the name is out for this cycle, with the rule that killed it.
