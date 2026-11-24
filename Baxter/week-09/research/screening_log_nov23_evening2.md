# Screening log: Mon Nov 23, EVENING 2 (8:00pm ET)

**Job (from EVENING 1's plan):** nothing cleared the chain at 6pm, so there was no doc to write. Work queue item 1, the band B returning parks, median-first, up to 25. Taken in queue order, skipping LBRT and CX (stale stamps, left on the queue) and leaving OWL and LADR for EVENING 3.

**Source:** Robinhood tools only for the screen (Monday's close), run ~01:00-01:45 UTC Nov 24. **2 web searches**, both on TAL after it cleared the chain. R5 line: 10% x $715.96 / 100 = **$0.716/share** (3.5/5); the transitional lock caps every tier at $1.00.

**Method (same as Nov 20-23):** median print = median absolute earnings-day move from daily closes (AM print: prior close to print-day close; PM print: print-day close to next close). Tonight used the last **5** prints (daily bars from Sep 15 2025; KT has 4). R6 cap = 1.5 x median. Under 8% = killed R6 structural with no quote. 8%+ = R1 re-checked on Monday's close, R2 contract month, one near-money quote (two where the first one was close). Monday's daily bar came back interpolated for most names, so R1 uses Monday's official close from `get_equity_quotes`.

## 13 killed R6 structural (median < 8%)

| Ticker | Next print (tool) | Prints (oldest first) | Median | Cap |
|---|---|---|---|---|
| MDU | Feb 4 AM (f) | +4.7 / -4.1 / +0.7 / +3.7 / -6.5 | 4.1% | 6.1% |
| TSLX | Feb 11 PM (f) | -2.1 / -4.4 / -8.6 / +0.4 / -0.5 | 2.1% | 3.2% |
| NLY | Jan 27 PM (f) | -1.9 / -1.0 / +0.1 / -1.0 / -1.5 | 1.0% | 1.5% |
| BANC | Jan 20 PM (f) | -2.0 / -1.8 / +2.8 / -12.2 / +1.3 | 2.0% | 3.0% |
| KT | Feb 9 AM (f); tool also shows an unreported Q3 Dec 4 row | -1.2 / +4.1 / +0.7 / -0.1 | 0.95% | 1.4% |
| SLM | Jan 21 PM (f) | +3.3 / +3.4 / +1.8 / +0.5 / -10.8 | 3.3% | 4.9% |
| BTU | Feb 4 AM (f) | -4.2 / -2.2 / -5.7 / -10.4 / -17.6 | 5.7% | 8.6% |
| IRT | Feb 10 PM (f) | +4.3 / -5.3 / +0.1 / +1.8 / -0.9 | 1.8% | 2.7% |
| HBAN | Jan 21 AM (f) | +0.8 / -6.0 / +0.1 / -4.8 / -0.4 | 0.8% | 1.2% |
| NRIX | Jan 27 PM (f) | -10.1 / -1.6 / -4.6 / -6.6 / -0.1 | 4.6% | 6.9% |
| IREN | Feb 4 PM (f) | -6.8 / +5.1 / +7.7 / -12.5 / +20.0 | 7.7% | 11.6% |
| BXMT | Feb 10 AM (f) | +3.5 / +2.0 / -4.6 / -8.7 / +2.9 | 3.5% | 5.2% |
| FLG | Jan 29 AM (f) | +4.8 / -2.4 / -2.2 / -5.8 / -9.3 | 4.8% | 7.2% |

## 12 to the chain: 11 killed, TAL advanced

All pass R1 on Monday's close. Ratings live tonight (B/H/S, low, stamp).

| Ticker | Mon close | R1 | Ratings, low | Median / cap | Contract (R2) | Quote (bid / ask, OI) | Needs at ask | Verdict |
|---|---|---|---|---|---|---|---|---|
| **TAL** | 9.71 | 0.194 | 15/3/0, $11.50, Nov 1 | 9.3% / 14.0% | Feb19 (6-K; Jan 28 AM (f), LY Jan 29; 21 days exactly) | **$10C 0.55 / 0.70, OI 177**, spread 24% | **+10.2%** | **ADVANCED: doc written, gated on R7 OI + floor dating** |
| CLBT | 11.23 | 0.090 | 9/0/0, $14, none | 14.3% / 21.5% | Apr16 (6-K; no Mar19) | $12.5C 0.70 / 1.40, OI 79; $15C 0.20 / 0.70, OI 83 | +23.8%; +39.8% | KILLED R6 at ask + R7 (passes at mid, +20.7%) |
| MBUU | 19.30 | 0.053 | 5/5/0, $22, Nov 17 | 13.3% / 20.0% | May21 (Feb19 fails 21-day test) | $20C 1.25 / 4.90, OI 5; $22.5C 0.50 / 3.60, OI 5 | +29.0%; +35.2% | KILLED R6 at ask + R7 (no market) |
| UTI | 19.19 | 0.059 | 7/0/0, $25, none | 11.2% / 16.8% | Apr16 | $20C 2.75 / 3.10, OI 16; $22.5C 1.80 / 2.10, OI 118 | +20.4%; +28.2% | KILLED R6 |
| HAPN | 14.97 | 0.200 | 9/0/0, $20, none | 10.5% / 15.8% | Apr16 | $15C 1.70 / 2.50, OI 241, spread 38% | +16.9% | KILLED R6 at ask (passes at mid, +14.2%) + R7 |
| AORT | 19.25 | 0.038 | 9/0/0, $30, none | 10.0% / 15.0% | Apr16 | $20C 0.05 / 4.90, OI 0 | +29.4% | KILLED R6 + R7 (no market) |
| AIP | 19.20 (+16.4% Mon) | 0.180 | 7/0/0, $25, none | 9.6% / 14.4% | Apr16 | $20C 3.20 / 4.10, OI 8, IV 81% | +25.5% | KILLED R6 |
| GLXY | 12.55 | 0.058 | 15/1/0, $20.50, none | 9.6% / 14.4% | Apr16 (Mar19 only if LA) | $12.5C 2.25 / 3.90, OI 407, IV 97% | +30.7% | KILLED R6 |
| MIR | 17.08 | 0.230 | 10/1/0, $20, none | 10.2% / 15.3% | May21 (Feb19 fails) | $17.5C 2.00 / 3.60, OI 55 | +23.5% | KILLED R6 |
| ADNT | 15.29 | 0.064 | 9/3/1, $17, Nov 16 | 8.0% / 12.0% | Apr16 | $15C 1.90 / 2.30, OI 3 | +13.1% | KILLED R6 + R4 (BE $17.30 > $17 low) |
| ATS | 17.31 | 0.045 | 6/1/1, $18, none | 10.6% / 15.9% | Apr16 | not quoted | -- | KILLED R4 at the screen: $18 low is 4.0% over the stock, no strike's BE fits under it |
| DKNG | 15.76 | 0.000 | 28/13/1, $16, Nov 10 | 8.6% / 12.9% | Mar19 | not quoted | -- | KILLED R4 at the screen: $16 low is 1.5% over the stock |

## What stands out

**TAL.** A Chinese education ADR, down 25% into its Oct 29 print, 15 Buys, 9.3% median print, and spring IV of only 37.5%. That low IV is the whole reason it works: time value is 7.2% of the stock against a 9.3% median move (ratio 1.29). Every other name tonight had IV of 49-97% and died at the ask. It's the Nov 19 finding again: the near-misses are names whose IV is low for their print history. Doc: `research_TAL_feb19.md`. Blocks: OI 177 (needs 250), floor not dated (the $11.50 low is probably Citi's Neutral $11.54; Buy targets found at $12-13.20 but undated). R5 fits by 1.6 cents, R2 by zero days.

**The rest:** two more passed R6 at mid but not at the ask (CLBT, HAPN), both with books too thin for R7. The band B returning parks are done except OWL, LADR (never quoted) and LBRT, CX (stale stamps).

## GLOSSARY

- **R1-R7:** binder Tab 1 Iron Rules (range percentile, earnings before expiry, ratings mix, bear floor, price cap, reachability, liquidity).
- **Median print:** median absolute one-day stock move on earnings, last 5 prints here.
- **Cap:** 1.5x the median, the most R6 lets the stock need to move to breakeven.
- **R6 structural:** median under 8%, so no spring contract can fit; killed without a quote.
- **At the ask / at mid:** breakeven figured on the ask price (what we'd pay) or the bid-ask midpoint.
- **OI:** open interest. **IV:** implied volatility.
- **LA:** large accelerated filer (10-K due Mar 1, so Mar19 can clear R2's 5-day backstop).
- **6-K filer:** foreign issuer, no 10-Q deadline; R2 needs both the tool date and last year's date.
- **Stamp:** the `updated_at` on the ratings record. **(f):** estimated date, `verified: false`.
- **Ratio:** median print / time value as % of stock; >= ~0.67 at the ask clears R6.
