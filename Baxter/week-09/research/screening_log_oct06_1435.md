# SCREENING LOG — Tue Oct 6, 2026, 2:35pm ET (VM MIDDAY)

**Source:** research_queue.md (COUR gate check, MLCO R1 + floor dating, live-list requotes, then CWK, BRSL, PAR through dates + R6 + chain). 10 names moved.

**Rule 5 line this run:** reserve = spendable $741.32 (unsettled $0.00). 3.5/5 line **$0.741**, 4/5 $1.00 (lock), screen $1.00.

## Summary

| Step | Count | Tool |
|---|---|---|
| Requotes | 7 (COUR, MLCO, PCT, ENVX, BXMT, CWH, ADTN) | get_option_quotes |
| Ratings | 10 names; no count or low-target changes on the live seven | get_equity_analyst_ratings |
| Dates | COUR, MLCO, CWK, BRSL, PAR | get_earnings_results |
| R1 + R6 history | MLCO, CWK, BRSL, PAR: 52-week daily range, 4 prints each | get_equity_historicals |
| New chains | CWK $12.5C, BRSL $10C/$11C, PAR $14C/$15C/$16C | get_option_instruments + get_option_quotes |
| Web | 2 fetches (MarketBeat forecast pages, MLCO and BRSL) | WebFetch |
| Killed | 2 (CWK, PAR) | |
| Blocked | MLCO (R4 stale floor) | |
| Advanced | **BRSL** to research-doc stage | |

## Live list

| Ticker | Stock | Contract | Bid / Ask | BE at ask | Needs | R6 cap | Ratings / low | Status |
|---|---|---|---|---|---|---|---|---|
| COUR | $5.09 | $5C Nov20 | 0.50 / 0.75 | $5.75 | +13.0% | 19.89% | 8/4/0, $6.00 | Date still Oct 22 PM `verified: false`. Ask $0.75 > $0.741. Two gates shut. Floor (BMO $6, Oct 5) unchanged. |
| MLCO | $4.291 | $4C Nov20 | 0.40 / 0.60, OI 10 | $4.60 | +7.2% | 6.55% | 11/4/0, $5.30 | **Moved to BLOCKED, R4 stale floor** (below). R1 0.042 passes. R6 still fails at the ask. |
| PCT | $4.075 | $4C Nov20 | 0.55 / 0.70 | $4.70 | +15.3% | 18.58% | 3/3/0, $6.00 | Blocked, stale floor. Unchanged. |
| ENVX | $2.705 | $3C Nov20 | 0.26 / 0.29 | $3.29 | +21.6% | 25.27% | 7/3/1, $5.00 | Blocked, stale floor. Unchanged. |
| BXMT | $11.085 | $11C Nov20 | 0.45 / 0.75 | $11.75 | +6.0% | 6.32% | 5/4/0, $16 | Fails R5 at the ask. |
| CWH | $4.65 | $4C Nov20 | 0.85 / 1.10 | $5.10 | +9.7% | 23.90% | 11/2/0, $6 | Fails R5. |
| ADTN | $7.595 | $7C Nov20 | 0.85 / 1.25 | $8.25 | +8.6% | n/a | 7/2/0, $11 | Fails R5. Stock +6.2% today. |

**MLCO floor dating (MarketBeat):** the tool's $5.30 low doesn't appear in MarketBeat's history. Buy-side targets visible: Susquehanna $7.00 (Aug 14, stock $5.60 that day, -23% since), CLSA Outperform $6.00 (Jul 10, 88 days old), Citi Buy $9.40 (Jul 10), UBS Buy $9.50 (Feb 16). JPM's $5.70 is Neutral. No Buy-side target is both inside 60 days and set after the decline. Same verdict as PCT and ENVX: blocked on a stale floor, not killed.

## Tier B: dates, R6, chains

Print-move = prior close to first close after the print (AM prints: prior close to print-day close; PM prints: print-day close to next close).

| Ticker | Stock | R1 (52w) | Print (tool) | Last 4 print moves (%) | Median / cap | Max BE | Strikes / contract | Verdict |
|---|---|---|---|---|---|---|---|---|
| CWK | $12.145 | 0.099 | Oct 29 AM, unverified | 0.00, -3.17, -4.22, -0.36 | 1.76 / 2.64 | $12.47 | 2.5-wide; $12.5C 0.60 / 0.80 (BE $13.30) | **KILL, R6 (strike grid).** $12.5C BE over $12.47 at any price; $10C intrinsic $2.15 fails R5. |
| PAR | $14.545 | 0.102 | Nov 5 PM, unverified | +16.58, -27.03, -3.94, +4.03 | 10.31 / 15.46 | $16.79 | $14C 1.25 / 3.60, $15C 0.75 / 1.90, $16C 0.55 / 1.50, all OI 0 | **KILL, R5 + liquidity.** Every bid near the money is at or over the $0.741 line; $16C BE $17.03 also fails R6. |
| **BRSL** | $10.22 | 0.068 | Nov 3 AM, unverified | +0.42, +5.13, -9.55, +11.77 | 7.34 / 11.02 | $11.35 | $1-wide; **$10C 0.20 / 0.80, OI 87**; **$11C 0.20 / 0.35, OI 53** | **ADVANCE.** See below. |

**BRSL (Brightstar Lottery):**
- $10C: BE $10.80 at the ask (+5.7%, passes R6), but ask $0.80 > $0.741 fails R5 at the ask. Mid $0.50 (BE $10.50, +2.7%) passes both. 60-cent spread.
- $11C: ask $0.35 passes R5. BE $11.35 at the ask = max BE exactly (+11.06% vs 11.02% cap, fails by a hair); at mid $0.275, BE $11.275 (+10.3%) passes. Prior close $0.01 is a phantom print, ignore.
- R1 0.068. R3 7/3/0 (MarketBeat also shows a Weiss quant "Sell (D+)", Jul 10; the tool counts 0 Sells; note it in the doc).
- R4: tool low $11.90 (firm not shown on MarketBeat). Buy-side targets: **Stifel $19, Sep 25** (stock $9.96 that day, i.e. set after the decline; rating to confirm), Jefferies Buy $16, Aug 13 (stock $11.69, pre-decline). Holds: Truist $13 (Jul 20), BNP Neutral $12.60 (May 14). Every known target is above both contracts' breakevens; the post-decline Stifel target is the dated anchor.
- Next: research doc. Confirm Stifel's rating and who holds the $11.90; Nov 3 date (unverified) needs a company announcement before entry, same gate as COUR.

## GLOSSARY

- **Requote:** a fresh bid/ask on a contract already chain-checked.
- **R1 (52w):** (price - 52-week low) / (52-week high - 52-week low), from daily bars; calls need <= 0.25.
- **R5 line:** max ask per share for one contract at the conviction tier (10% of reserve / 100 at 3.5/5).
- **R6 cap:** 1.5x the median earnings-day move over the last 4 prints; the needed move to breakeven must fit under it.
- **Max BE:** stock price x (1 + R6 cap); the highest breakeven Rule 6 allows.
- **Strike grid:** the spacing of listed strikes; 2.5-wide grids often leave no strike that fits.
- **Stale floor:** a price target set before the stock's decline, or more than 60 days ago; it doesn't count for Rule 4 (binder Tab 6).
- **Phantom print:** a last-trade or close price that no real bid/ask supports (e.g. $0.01 on a contract quoting 0.20 / 0.35).
- **BE:** breakeven, strike + premium.
- **OI:** open interest, contracts outstanding.
- **AM / PM print:** earnings released before the open / after the close.
