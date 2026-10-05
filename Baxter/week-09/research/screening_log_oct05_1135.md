# Screening Log: Mon Oct 5, 2026, 11:35am ET run (VM, MIDDAY slot)

**Source:** the research queue as left by the 10:35 run plus Tier A of the Oct 5 full sweep. No fresh scanner pass: this run worked the queue top-down.

**Rule 5 line this run:** reserve = spendable cash $450.78 ($290.54 of stock-sale proceeds still unsettled until Tue Oct 6). Screen line 0.20 x 450.78 / 100 = **$0.90/share**. 3.5/5 tier top (10%) = **$0.45/share**. 4/5 tier top (16%) = **$0.72/share**. **Tuesday preview** (reserve ~$741.32 if the proceeds settle): 3.5/5 line **~$0.74**, 4/5 line ~$1.00 (transitional $1.00 lock).

**Prices pulled 11:35-11:38am ET.**

## Funnel

| Stage | Names | Tool |
|---|---|---|
| Queue in | 8 worked (CWH, LRMR, PCT, RWT, MFA, PRG, LVS, COUR) | research_queue.md |
| Rule 2 date check | 8, all unverified, all before Nov 20 | get_earnings_results |
| Rule 3 / Rule 4 proxy refresh | 10 | get_equity_analyst_ratings |
| Rule 1 + Rule 6 history (free) | 6 (PCT, RWT, MFA, PRG, LVS, COUR) | get_equity_historicals, daily, 6 prints each |
| Chain check (cap 5) | 5 (CWH, LRMR, PCT, RWT, COUR) | get_option_instruments / get_option_quotes, Nov 20 calls |
| Killed | 3 (LRMR, RWT, MFA) | |
| Alive | **COUR, PCT** (chain-passed, R5 waits on Tuesday's reserve); CWH (still blocked); PRG, LVS (R6 history done, chain next) | |

## Chain-checked (5 of 5)

| Ticker | Price | Earnings (tool) | Ratings B/H/S | Low tgt | Contract | Bid/Ask | BE (ask) | Needs | R6 cap | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| COUR | $5.205 | Oct 22 PM (unverified; scanner said 10/23) | 8/4/0 | $6.50 | $5C Nov20 | 0.60 / 0.70 | $5.70 | +9.5% | 19.89% | **ADVANCE (best on the board).** R1 0.103. R4 $6.50 > $5.70 (+14% margin). R6 at 48% of cap. OI 3,135, 10c spread. R5: $0.70 fails today's $0.45 3.5/5 line, fits the 4/5 $0.72 line and Tuesday's ~$0.74 3.5/5 line. $6C 0.20/0.30, BE $6.30 needs +21.0% > cap: fails R6. |
| PCT | $4.025 | Nov 5 PM (unverified) | 3/3/0 | $6.00 | $4C Nov20 | 0.60 / 0.65 | $4.65 | +15.5% | 18.58% | **ADVANCE.** R1 -0.017 (fresh 52w low, under the bar low $4.22). R3 passes the Oct 5 tightening exactly (3 Buys, Buys = Holds). R4 $6.00 > $4.65. R6 at 83% of cap. OI 417. R5: $0.65 fails today's $0.45, fits Tuesday's ~$0.74. $5C 0.30/0.35, BE $5.35, +32.9%: fails R6. |
| CWH | $4.145 (-17.6% vs Fri $5.03) | Oct 27 PM (unverified) | 11/2/0 | $6.00 | $5C / $4C Nov20 | 0.15/0.35, 0.50/0.75 | $5.35 / $4.75 | +29.1% / +14.6% | 23.90% | **HOLD, BLOCKED.** $5C now fails R6 (+29.1% > 23.9%). $4C passes R6 and R4 but $0.75 > $0.45 today and > ~$0.74 Tuesday (by a penny); OI 15. Oct 5 8-K still 404 (3rd try). Filing index shows only that one filing. One search: only old news (Truist $20->$15, Moody's, Feb print). Cause of the drop still unknown. |
| LRMR | $2.835 | Nov 4 AM (unverified) | 11/0/0 | $5.00 | $2.5C / $5C Nov20 | 0.00/1.40, 0.00/0.10 | $3.90 / $5.10 | +37.6% / +80% | n/a | **KILL, R5 + R4 + liquidity.** Only 2.5/5/7.5 strikes. $2.5C no bid, ask $1.40 > $0.90. $5C no bid, BE $5.10 > $5.00 floor. |
| RWT | $3.485 | Oct 28 PM (unverified) | 7/2/0 | $5.22 | $3C / $4C Nov20 | 0.25/1.00, 0.00/0.25 | $4.00 / $4.25 | +14.8% / +22.0% | 8.69% | **KILL, R6 + R5 + liquidity.** Whole-dollar strikes only. $3C OI 0, ask $1.00 over the screen line. |

## Rule 6 history only (no chain spent)

| Ticker | R1 pct | Print moves (oldest -> newest) | Median | Cap | Max BE at cap | Low tgt | Verdict |
|---|---|---|---|---|---|---|---|
| MFA | -0.088 | -5.35, +0.22, -3.13, +1.61, -6.00, -0.33 (AM) | 2.37% | 3.56% | $7.59 | $10.00 | **KILL, R6.** A $7.5C would need an ask of $0.09 or less. Mortgage REIT, same shape as MRP. |
| RWT | 0.071 | -6.12, -7.91, -2.73, +20.58, -0.89, -5.47 | 5.79% | 8.69% | $3.79 | $5.22 | Killed above on the chain. |
| PCT | -0.017 | +15.09, 0.00, +9.68, -22.29, +17.32, +4.95 (PM) | 12.38% | 18.58% | $4.77 | $6.00 | See chain table. The 0.00% (Aug 7-8 2025) is real: both closes $12.35, intraday high $14.23. |
| COUR | 0.103 | +13.6, +36.2, -12.9, -1.2, -11.6, -14.7 (PM) | 13.26% | 19.89% | $6.24 | $6.50 | See chain table. **Bearxter note: 4 of the last 4 prints went down.** |
| PRG | 0.240 | -7.0, +16.6, -0.4, +6.6, +24.1, -5.1 (AM) | 6.82% | 10.23% | $34.25 | $45.00 | ALIVE. Next: chain, $32.5/$33 strikes need ask <= $0.90 and BE <= $34.25. Print Oct 21 AM (scanner had 10/22). R1 0.24, right on the line. |
| LVS | 0.015 | +6.5, +4.3, +12.4, -14.0, -8.6, +1.7 (PM) | 7.55% | 11.33% | $40.89 | $47.00 | ALIVE. Next: chain, $38-40 strikes. Print Oct 21 PM (scanner had 10/22). Era 1 lost -$67 on LVS (R6 retro-block). |

## What COUR and PCT still need before a doc

- **COUR:** the confirmed Oct 22 date (one search), news on why it's at the bottom of its range, and **any pending merger** (I think a Coursera/Udemy combination was announced around Dec 2025; not checked this run. If it's live, the calls flag applies and the deal terms matter for Rule 4). The $6.50 low target needs a date (within 60 days, after the decline). Conviction is capped at 3.5/5 on this machine (revisions unverifiable), so R5 clears only on Tuesday's reserve.
- **PCT:** confirmed Nov 5 date, the cause of today's -8.3%, a date on the $6 target. Same 3.5/5 cap, same Tuesday R5 dependency. The Feb 2026 -22% print is the bear case to answer.

## GLOSSARY

- **Rule 1 (range percentile):** where the price sits between its 52-week low (0) and high (1). Under 0.25 is the calls zone; negative means today's price is under the lowest daily low of the last year.
- **Rule 2:** a confirmed earnings date before the option expires. "Unverified" means the tool estimated it from the company's cadence.
- **Rule 3 (calls):** 0-1 Sell ratings, at least 3 Buys, and Buys at least equal to Holds.
- **Rule 4 (bear floor):** the lowest analyst target must sit above the call's breakeven (strike + premium).
- **Rule 5:** one contract's ask must fit the cap for its conviction tier, computed on spendable cash (the reserve).
- **Rule 6 (reachability):** the move to breakeven can't exceed 1.5x the stock's median earnings-day move over its last 4-8 prints. AM prints: prior close to print-day close. PM prints: print-day close to next-day close.
- **Breakeven (BE):** strike + premium; where the call neither makes nor loses money at expiry.
- **Settled cash:** in a cash account, sale proceeds take one business day (T+1) to settle before they can be spent.
- **8-K:** a company's filing for a material event that can't wait for the quarterly report.
- **Open interest (OI):** contracts outstanding. Low OI plus a wide spread means there may be nobody to sell to.
- **Kill:** out for this cycle, with the rule that killed it.
