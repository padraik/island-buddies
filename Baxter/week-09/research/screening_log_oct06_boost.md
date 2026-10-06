# Screening Log: Tue Oct 6, 2026, 10:38am ET run (VM, MIDDAY boost run)

**Source:** a one-time 25-name research boost (cap raised from 5 to 25 for this run only). The 12 names on the research queue, then 13 from Tier B of `full_sweep_oct05.md`, in table order. Already-dead Tier B names (BKSY, AMRC) were skipped.

**Rule 5 line:** spendable = cash $741.32 - unsettled $0.00 = **$741.32**. 3.5/5 line **$0.741**; 4/5 line $1.00 (lock); screen line $1.00.

**Quotes are 10:39-10:44am ET.** All chains are the Nov 20, 2026 monthly expiry.

**Rule 6 method:** prior regular close to the print-day close. For after-close (PM) prints, the reaction day is the next session. Four prints per name: Q2 2026, Q1 2026, Q3 2025, Q2 2025, except where noted. Median of the absolute moves; cap = 1.5 x median; max BE = stock x (1 + cap).

## Funnel

| Stage | Names | Tool |
|---|---|---|
| In | 25 (12 queue + 13 Tier B) | research_queue.md, full_sweep_oct05.md |
| Rule 3 / Rule 4 proxy refresh | 25, all still pass R3 (3+ Buys, Buys >= Holds, 0-1 Sell) | get_equity_analyst_ratings (1 call) |
| Rule 2 dates | 25 | get_earnings_results |
| Rule 6 history | 20 | get_equity_historicals |
| Chains / requotes | 24 contracts on 22 names | get_option_instruments + get_option_quotes |
| Web searches | 2 (COUR date, ENVX decline) | WebSearch |
| **Killed** | **19** | |
| **Alive** | **6: COUR, PCT, ENVX, BXMT, CWH, ADTN** | |

## Survivors

| Ticker | Stock | Print (tool) | R6 prints (abs) | Median / cap / max BE | Contract | Bid/ask | BE at ask | Needs | R4 low | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| **ENVX** | $2.665 | Nov 4 PM, unverified | -6.34, -13.58, -20.23, -20.11 | 16.85% / 25.27% / $3.34 | $3C | 0.25 / 0.30 (OI 1,956) | $3.30 | +23.8% | $5 | **Passes R1/R3/R4/R5/R6. New. Pre-doc.** |
| **PCT** | $3.98 | Nov 5 PM, unverified | (Oct 5 run) | 12.38% / 18.58% / $4.72 | $4C | 0.55 / 0.65 (OI 442) | $4.65 | +16.8% | $6 | **R5 passes now** (was 0.60/0.65 on Oct 5). Pre-doc. |
| **COUR** | $5.195 | Oct 22 PM, unverified | (Oct 5 run) | / 19.89% / | $5C | 0.60 / 0.70 (OI 3,137) | $5.70 | +9.7% | $6 | Doc written. Date gate still shut (see below). |
| BXMT | $11.165 | Oct 28 AM, unverified | -8.72, -4.65, +3.47, -3.77 | 4.21% / 6.32% / $11.87 | $11C | 0.50 / 0.85 (OI 33) | $11.85 | +6.1% | $16 | **Fails R5 at the ask** ($0.85). Needs ask <= $0.74 (R5 binds; R6 alone would allow $0.87). $12C 0.05/0.40 fails R6 (BE $12.40). |
| CWH | $4.475 | Oct 27 PM, unverified | (Oct 5 run) | / 23.90% / | $4C | 0.70 / 0.95 (OI 91) | $4.95 | +10.6% | $6 | Fails R5 ($0.95). Ratings still 11/2/0, low $6. |
| ADTN | $7.35 | Nov 2 PM, unverified | (Oct 5 run) | 10.95% / 16.42% / $8.26 | $7C | 0.85 / 1.05 (OI 1,021) | $8.05 | +9.5% | $11 | Fails R5 ($1.05). |

**ENVX notes.** Ratings 7 B / 3 H / 1 S (the Sell is JPMorgan's downgrade to underweight; one Sell is allowed). Range ~0.02. R6 margin is thin: needs +23.8% against a 25.27% cap. The $2C is 0.66 / 0.94 (fails R5 at the ask). **Bearxter:** all four prints went down (-6, -14, -20, -20), and the stock is down from ~$14 to $2.67 in a year. Web search: smartphone battery qualification reset pushed commercialization to 2027, Fab2 yields are a bottleneck, the company is still deeply unprofitable, and TD Cowen cut its target to $5.50 (Hold). Decline category: **fundamental (execution delay)**. The thesis would have to be "the Nov print is a relief print". That needs a written answer before any doc reaches 3.5/5.

**COUR date.** The tool still says Oct 22 PM, `verified: false`. One search turned up no Coursera "to announce" release. Aggregators again say Oct 26 PM. The gate stays shut until the company names the day.

## Kills (19)

| Ticker | Stock | Print (tool) | R6 median / cap / max BE | What the chain said | Rule |
|---|---|---|---|---|---|
| NG | $6.62 | **Oct 8 AM, verified** | | Not pulled | R2 timing: prints in 2 days. A ramp sell would be due tomorrow, before a doc could exist. |
| YUMC | $40.61 | Nov 3 AM | 1.91% / 2.86% / $41.77 (3 prints: 1.35, 2.85, 1.91) | No $41 strike in Nov20. $40C would need < $0.13 time value. | R6 |
| WRN | $2.14 | Nov 5 PM | 2.52% / 3.77% / $2.22 (1.05, 1.60, 3.43, 4.76) | No $2 strike in Nov20 | R6 |
| IE | $10.32 | Nov 4 PM | 2.22% / 3.32% / $10.66 (1.31, 1.44, 2.99, 3.15) | $10C 1.20 / 1.35 | R6 + R5 |
| PHAR | $9.71 | Nov 5, verified | | **No listed options.** Stock trades ~3-60k shares a day. | R5 (no chain) |
| TBLA | $3.225 | Nov 4 AM | 18.04% / 27.06% / $4.10 (5.30, 11.41, 24.67, 27.50) | Only $2.5 / $5 / $7.5 strikes. $2.5C 0.55 / 1.25 OI 1. $5C BE > $4.10. | R5 + R6 (strike grid) + liquidity |
| ARDX | $3.25 | Oct 29 PM | 17.36% / 26.04% / $4.10 (8.69, 16.86, 17.86, 20.96) | $3C **no bid** / 0.70, OI 20, prior close $0.01 (phantom). $4C no bid / 0.75. | R5 + liquidity (no two-sided market) |
| INDI | $2.895 | Nov 5 PM | 4.74% / 7.10% / $3.10 (0.43, 4.23, 5.24, 17.78) | $2.5C 0.45 / 0.75 (BE $3.25). $3C 0.25 / 0.40 (BE $3.40). | R6 (+R5 on $2.5C) |
| CARG | $29.135 | Nov 5 PM | 7.24% / 10.86% / $32.30 (0.63, 7.16, 7.32, 8.95) | $30C 1.50/2.20, $31C 1.20/1.95, $32C 0.85/1.60 | R5 + R6 |
| KRMN | $33.40 | Nov 5 PM | 5.67% / 8.50% / $36.24 (5.04, 5.60, 5.73, 7.68) | $35C 2.70 / 3.50 | R5 + R6 |
| OMCL | $34.64 | Oct 29 AM | 11.96% / 17.94% / $40.85 (4.41, 10.36, 13.56, 20.94) | 5-wide strikes. $40C no bid / 2.90, OI 8, prior close $0.01 (phantom). | R5 + liquidity |
| CALX | $34.70 | **Nov 2 PM, verified** | 9.34% / 14.01% / $39.56 (3 prints: 2.29, 9.34, 13.98) | $37.5C 1.20 / 1.65, OI 1 | R5 |
| BROS | $38.80 | Nov 4 PM | 14.07% / 21.10% / $46.99 (4.21, 9.35, 18.79, 21.60) | $42.5C 1.90/2.05, $45C 1.30/1.40. $47.5C BE > max. | R5 (+R6 above $45) |
| KTOS | $42.64 | Nov 3 PM | 7.74% / 11.60% / $47.58 (6.69, 7.35, 8.12, 14.20) | $45C 2.85 / 3.10 | R5 + R6 |
| APTV | $44.60 | Oct 29 AM | 6.08% / 9.11% / $48.66 (2.93, 4.25, 7.90, 16.62) | $47.5C 1.80 / 2.00 | R5 + R6 |
| CENX | $36.93 | Nov 5 PM | 7.13% / 10.69% / $40.88 (1.63, 2.76, 11.49, 14.04) | $40C 2.05 / 2.25 | R5 + R6 |
| USAR | $13.90 | Nov 5 PM | 6.03% / 9.04% / $15.16 (0.68, 2.32, 9.73, 23.32) | $14C 1.48 / 1.50 | R5 + R6 |
| TPB | $58.48 | Nov 4 AM | 8.66% / 12.98% / $66.07 (2.56, 6.28, 11.03, 14.22) | $65C 1.95 / 3.80, OI 0 | R5 + R6 + liquidity |
| LASR | $39.51 | Nov 5 PM | 20.12% / 30.17% / $51.43 (11.66, 14.67, 25.56, 27.75) | $45C 2.05/2.60, $50C 1.30/1.50 (BE $51.50) | R5 (+R6 at the $50C ask) |

**Pattern, again:** every name over ~$15 died on R5. When R6 leaves room, the stock's IV prices any reachable strike well over $0.74. The live candidates are all under $12 (ENVX, PCT, COUR, BXMT, CWH, ADTN). Tier B's remaining sub-$15 names (RITM, HLMN, VYX, ARLO, TKC, TRTX, GRNT, DX, MNTN) are the best next pool.

**Scanner dates:** the tool came back a day earlier than the sweep's date on most names again (CARG, KRMN, OMCL, BROS, YUMC, KTOS, APTV, ARDX, ENVX, WRN, USAR, IE, TBLA, CENX, INDI, BXMT). Unchanged on CALX (Nov 2) and PHAR (Nov 5). NG moved from the scanner's 10/08 to Oct 8 AM, verified.

## GLOSSARY

- **R1-R6:** the six Iron Rules for calls (binder Tab 1): range, earnings, ratings, bear floor, chain affordability, reachability.
- **Max BE (R6):** the highest breakeven a contract can have and still pass Rule 6 (stock price x (1 + 1.5 x median earnings move)).
- **Median earnings move:** the middle of the last four absolute print-day moves (prior close to print-day close).
- **Phantom quote:** a price that can't be real against its neighbors (a $0.01 close on a near-the-money strike). Never acted on.
- **Liquidity kill:** no bid, no volume, near-zero open interest. There's no real price to buy at and no one to sell to later.
- **Strike grid:** which strikes the exchange lists. If the only strikes are $2.50 apart, the one you need may not exist.
- **Bid/ask:** what buyers will pay / sellers will take right now.
- **OI:** open interest, contracts outstanding.
- **Verified:** the company itself announced the earnings date.
- **IV:** implied volatility, how much movement the option price already assumes.
- **Ramp sell:** selling before the print, into the pre-earnings premium (binder Tab 4).
- **Pre-doc:** passed the free checks and the chain; the research doc (Five-Baxter meeting, exit plan, sizing) isn't written yet, so no order is possible.
