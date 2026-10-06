# SCREENING LOG — Tue Oct 6, 2026, 12:35pm ET (VM MIDDAY)

**Source:** research_queue.md (COUR and ENVX floor dating, requotes on the live list, then Tier B sub-$15 names DX, RITM, TRTX, HLMN). 10 names moved.

**Rule 5 line this run:** reserve = spendable $741.32 (unsettled $0.00). 3.5/5 line **$0.741**, 4/5 $1.00 (lock), screen $1.00.

## Summary

| Step | Count | Tool |
|---|---|---|
| Requotes (chain checks) | 6 (COUR, ENVX, PCT, BXMT, CWH, ADTN) | get_option_quotes |
| New chains | 3 (RITM $8C, TRTX $6C, HLMN $7.5C) | get_option_instruments + get_option_quotes |
| Ratings | 12 names, no count changes on the 6 live ones | get_equity_analyst_ratings |
| Dates | COUR, DX, RITM, TRTX, HLMN | get_earnings_results |
| R6 history | DX, RITM, TRTX, HLMN (4 prints each, daily closes) | get_equity_historicals |
| Web | 2 fetches (MarketBeat COUR, ENVX), 1 search (COUR Q3 date), 1 failed fetch (Coursera IR, 404) | WebFetch / WebSearch |
| Killed | 4 (DX, RITM, TRTX, HLMN) | |

## Live list

| Ticker | Stock | Contract | Bid / Ask | BE at ask | Needs | R6 cap | Ratings / low | Status |
|---|---|---|---|---|---|---|---|---|
| COUR | $5.195 | $5C Nov20 | 0.60 / 0.65 | $5.65 | +8.8% | 19.89% | 8/4/0, $6.00 | **Floor dated: BMO Outperform $8 -> $6, Oct 5, 2026. R4 passes the Tab 6 standard.** Only gate left: date (Oct 22 PM, `verified: false`). |
| ENVX | $2.69 | $3C Nov20 | 0.22 / 0.29 | $3.29 | +22.3% | 25.27% | 7/3/1, $5.00 | **Blocked, R4 dating** (below). |
| PCT | $4.035 | $4C Nov20 | 0.50 / 0.65 | $4.65 | +15.2% | 18.58% | 3/3/0, $6.00 | Still blocked, R4 stale floor. Counts unchanged. |
| BXMT | $11.135 | $11C Nov20 | 0.55 / 0.85 | $11.85 | +6.4% | 6.32% | 5/4/0, $16 | Fails R5 ($0.85) and now R6 at the ask (+6.4% > 6.32%). |
| CWH | $4.745 | $4C Nov20 | 0.85 / 1.00 | $5.00 | +5.4% | 23.90% | 11/2/0, $6 | Fails R5 ($1.00); stock +4.3% today pushed the ITM call up. |
| ADTN | $7.425 | $7C Nov20 | 0.85 / 1.25 | $8.25 | +11.1% | n/a | 7/2/0, $11 | Fails R5 ($1.25). |

## ENVX Rule 4 dating

MarketBeat, Jul-Oct 2026: TD Cowen upgrade to **Hold** (Oct 5, no target); BofA **Neutral $5** (Aug 17; this is the tool's $5.00 low, and it's not a Buy); Loop Capital upgrade to Strong Buy (Aug 17, no target); William Blair Outperform -> Market Perform (Aug 17); Canaccord **Buy $15 -> $10** (Aug 14); Craig Hallum set **$7** (Aug 13, rating not shown); B. Riley **Buy $10 -> $9** (Aug 13); Cantor **Overweight $25** (Aug 13). The lowest Buy-side target is Hallum $7 or B. Riley $9, both Aug 13-14, when ENVX closed $4.39-4.43. It closed $3.595 on Aug 17, $2.98 on Sep 15 and $2.67 on Oct 5: **down ~39% since every Buy target was set.** Binder Tab 6: the floor has to be published after the decline. None is. Same verdict as PCT: blocked, not killed. It also ages past 60 days on Oct 12-13, before the Nov 4 print. Unblocks only on a fresh Buy target above $3.29.

## Tier B kills

| Ticker | Stock | Print (tool) | Last 4 print moves | Median / cap | Contract checked | Verdict |
|---|---|---|---|---|---|---|
| DX | $10.805 | Oct 19 AM, verified | +0.37, -0.14, +0.81, -1.58 | 0.59% / 0.89% | none needed | **KILL, R6.** Max BE $10.90; the $11C strike alone is over it. An mREIT that moves under 1% on prints. |
| RITM | $8.69 | Oct 29 AM, unverified | +0.55, +1.39, -2.67, +5.96 | 2.03% / 3.04% | $8C 0.75 / 1.35, OI 102 | **KILL, R5 + R6.** Max BE $8.95; $9C fails at any price, $8C BE $9.35 at the ask and ask over $0.741. $1-wide strikes. |
| TRTX | $6.11 | Oct 27 PM, unverified | -2.80, -4.09, -0.84, -3.86 | 3.33% / 5.00% | $6C 0.05 / 0.80, OI 0, $0.01 phantom close | **KILL, R5 + liquidity.** Needs ask <= $0.42 for R6; no real market. All 4 prints fell. |
| HLMN | $7.095 | Nov 3 AM, unverified | -2.80, -10.14, -5.13, +14.44 | 7.63% / 11.45% | $7.5C 0.10 / 0.85, OI 0, $0.01 phantom close | **KILL, R5 + liquidity.** Needs ask <= $0.41 for R6; 2.5-wide strikes, no real market. |

R1 for all four: bottom of the trailing ~52-week daily-close range (DX $10.83-14.74, RITM $8.71-12.06, TRTX $6.02-9.31, HLMN $6.94-10.74). R3 passes on all four (DX 4/2/0, RITM 11/0/0, TRTX 5/0/1, HLMN 6/2/0).

Also pulled, not yet worked: GRNT 5/2/0 (low $6, stock $4.605), TKC 6/0/0 (low $7.07, stock $5.185). Both pass R3; dates and R6 next.

## GLOSSARY

- **Requote:** a fresh bid/ask on a contract already chain-checked.
- **R5 line:** max ask per share for one contract at the conviction tier (10% of reserve / 100 at 3.5/5).
- **R6 cap:** 1.5x the median earnings-day move (prior close to the first close after the print); the needed move to breakeven must fit under it.
- **Stale floor:** a price target set before the stock's decline, or more than 60 days ago; it doesn't count for Rule 4 (binder Tab 6).
- **BE:** breakeven, strike + premium.
- **Phantom close:** a $0.01 "previous close" on a contract with no open interest; not a real price.
- **OI:** open interest, contracts outstanding.
- **mREIT:** mortgage real estate investment trust.
