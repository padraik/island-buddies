# Screening log, Tue Oct 20, MIDDAY (2:35pm ET): DONE

*Quotes 2:35-2:37pm ET. Two web searches (INSM floor, PL $17). Live chains: APH Nov20 $80C; GFS Dec18 $45C/$50C/$55C; APTV Dec18 $45C; INSM Nov20 $100C; PL Jan15 $12C/$15C; CENX Dec18 $32.5C/$35C; BX Nov20 $110C. Earnings dates from `get_earnings_results`. Print bases and R1 ranges from daily bars (Apr 2025 to today).*

## Held: COUR $5C Nov20

| Check | Result |
|---|---|
| Quote (2:35) | 0.50 / 0.55 (bid size 13, ask size 44, vol 2), mark 0.525, OI 3,235, IV 87.0% |
| Stock | $5.03 (+0.6%), 5.03 / 5.04 |
| Q3 | Thu Oct 29 PM, `verified: true`, `actual: null` (LY Oct 23 PM) |
| Rule 4 | 8/4/0, low **$6.00** vs BE $5.65: holds |
| Filings | none since Oct 15 (index empty) |
| Tab 4 | nothing fires. Bid 0.50 = -23.1% |

## Queue: names moved

| # | Name | Contract | Stock (2:35) | Live quote | Ratings (B/H/S, low) | Result |
|---|---|---|---|---|---|---|
| 1 | GFS | Dec18 $45C `d0da77eb` / $50C `bd4f1841` / $55C `b1d4f4a7` | $47.51 (+3.0%) | 5.70/6.40 OI 11; 3.60/3.80 OI 42; 2.15/2.30 OI 65 | 14/9/1, **$51** (stamp Oct 15) | **KILLED (R2 on Nov20; R4 + R7 on Dec18).** Q3 Wed Nov 4 AM `verified: true`, but LY was **Nov 12**, so the 21-day cushion runs from Nov 12 to Dec 3 and Nov20 fails. On Dec18: $45C BE $51.40 at the ask is over the $51 low; $50C BE $53.80, $55C $57.30, also over. All three OI < 250. Six AM prints: -2.70, -9.34, -1.84, +16.32, +9.28, -4.92 (median 7.10%, cap 10.65%). |
| 2 | APH | Nov20 $80C `d254aa6a` | $79.21 (-1.3%) | 3.90 / 4.40, OI 5,713, spread 12.0% | 22/2/0, $90 (stamp Oct 3) | **PARK, R6 fails.** BE $84.40 at the ask = **+6.55%** vs 6.07% cap. The ask widened again (4.20 -> 4.40). Needs ask <= $4.02 at this stock price. Kill **Fri Oct 23**. |
| 3 | APTV | Dec18 $45C `6f545918` | $45.04 (+1.3%) | 3.20 / 3.40, OI **7** | 17/4/0, $50 | **KILLED (R7).** OI 2 -> 7 in a day. R2: Nov 3 AM verified, LY Oct 30, so Nov20 fails (17 days) and Dec18 is the first contract. |
| 4 | INSM | Nov20 $100C `a002982d` | $95.48 (+0.2%) | 5.00 / 5.70, OI 289, spread 13.1% | 24/1/0, $165 | **PARK, floor gate.** R1 0.042 (52-wk $90.39-$212.75). R2 passes by exactly 21 days: Q3 Thu Oct 29 AM `verified: true`, LY Oct 30, Nov 20 - Oct 30 = 21; 10-Q deadline Nov 9 is 9 trading days before expiry. R6 passes: BE $105.70 = +10.7% vs cap **17.16%** (six AM prints -3.88, -1.76, +16.33, +6.54, -23.41, +33.86, median 11.44%). R7 passes. R4: the $165 is +73% over the stock, the stale-floor shape. One search found only a **Truist cut on May 21, 2026** (target not in the result), nothing in Oct. Undated. Ramp sell would be **Wed Oct 28 3:35pm** (AM print). Paper-sized ($570 vs the $67.60 line). Kill **Fri Oct 23** unless a dated floor turns up. |
| 5 | PL | Jan15 $12C `da5f4375` / $15C `0d73590a` | $13.455 (-1.0%) | 2.80/3.00 OI 1,279; 1.50/1.60 OI 1,714 | 8/5/0, $17 | **KILLED (R4, Tab 6 stale floor).** Everything else passes: R1 0.071 (52-wk $10.52-$51.76); R2 Dec 9 PM (f), LY Dec 10, Jan15 = 36 days; R6 $12C BE $15.00 = +11.5%, $15C BE $16.60 = +23.4%, vs cap **45.74%** (six prints +49.37, +47.93, +35.01, +25.48, -25.98, -1.25, median 30.49%); R7 both pass (spreads 6.9% and 6.5%). But the one search put the $17 at **Northland and Deutsche Bank, both raised $16 -> $17 on Dec 11, 2025**, when the stock was about $17.47. That's a year-old raise from before the run to $51 and the fall back to $13. Not a floor. |
| 6 | CENX | Dec18 $32.5C `0c31583f` / $35C `be587554` | $33.48 (-2.6%) | 3.70/4.20 OI 5; 2.65/3.20 OI 42 | 6/1/0, $40 | **KILLED (R7).** R2: Nov 5 PM (f), LY Nov 6, so Dec18 is the first contract. OI hasn't built since Oct 16. |
| 7 | BX | Nov20 $110C `08ff8a64` | $110.53 (+3.2%) | 5.15 / 5.50, OI 976, spread 6.6% | 15/11/1, **$116** (stamp **Oct 13**) | **PASSES R1-R7 on live numbers, paper only, and the catalyst is Thursday.** R1 0.139 (52-wk $101.73-$165.14). R2: Q3 **Thu Oct 22 AM** `verified: true`, LY Oct 23, Nov20 = 29 days. R3 15/11/1 passes (one Sell, Buys >= Holds). R4: BE **$115.50** at the ask vs low **$116**, passes by $0.50; the stamp is Oct 13, inside 60 days, but whether the $116 is a cut or a raise isn't verified. R6: +4.50% vs cap **4.65%** (six AM prints -4.17, -2.62, -5.70, +1.37, +3.58, +0.78, median 3.10%). R7 passes. The problem is the clock: with an AM print Thursday, the ramp-sell deadline is **Wed Oct 21 3:35pm**, one day after any entry. Holding through needs a 4/5 binary flag, and a $0.50 R4 margin and a 0.15-point R6 margin don't support 4/5. $550 a contract against the $67.60 real line, so paper only. EVENING 1 decides whether a one-day paper ramp trade is worth logging (at the close ask, sell at Wednesday's 3:35 bid). The quarter is spent Thursday morning: **kill Thu Oct 22** either way. |
| 8 | TTWO | (none) | $206.19 (+0.6%) | n/a | 29/1/1, $270 (stamp **Aug 7**, unchanged) | **PARK**, free re-check only. |

**Moved this run:** 8 names. 4 killed (GFS R2/R4/R7, APTV R7, PL R4, CENX R7), 4 parked (BX paper/clock, INSM floor, APH R6, TTWO floor). 2 searches.

**Watch line (free re-quote):** ONDS $6.146 (revive >= ~$6.90), BTBT $0.915 (>= ~$1.10), CLSK $8.47 (> ~$9.20). None revived.

**Paper LVS** $37.5C Nov20: 1.87 / 2.08 (OI 16,262), stock $37.995 (0.0%), ITM by $0.495. The 3:35pm run closes it or writes the ITM hold-vs-sell call (Q3 Wed Oct 21 PM).

Queue after this run: **4 live + 3 watch** (BX, INSM, APH, TTWO; watch ONDS, BTBT, CLSK). Under 10: EVENING 3 refills.

**Pattern:** GFS was the hope from 1:35, and it died on the calendar before the floor even mattered. Last year's Q3 was Nov 12, a week later than this year's verified date, and the 21-day cushion runs from the later one. PL is the stale-floor bin again. BX is the first name all day to clear every rule on live numbers, and it clears two of them by less than a rounding error with the print 44 hours away.

## GLOSSARY

- **R1-R7**: binder Tab 1 Iron Rules. R1 range percentile, R2 earnings before expiry, R3 ratings consensus, R4 bear floor (lowest Buy target > breakeven), R5 price cap, R6 reachability (needed move <= 1.5x median print reaction), R7 liquidity (OI >= 250, spread <= 25% of mid).
- **BE**: breakeven = strike + premium paid (at the ask, for screening).
- **OI**: open interest, contracts outstanding.
- **(f)**: `verified: false` earnings date (estimated from cadence).
- **LY**: last year's same-quarter report date.
- **Stamp**: the `updated_at` on the analyst-ratings tool result, the last time the target set changed.
- **Floor gate / stale floor (Tab 6)**: a Rule 4 floor must be dated within 60 days and published after the decline; a year-old raise isn't a floor.
- **Ramp sell**: Tab 4 default exit, sell an OTM call before the print rather than hold through the IV crush.
- **Binary flag**: the Tab 4 exception that allows holding through a print; needs 4/5+ conviction and Bearxter's written condition at entry.
- **Paper**: tracked in `paper_book.md`, no money.
