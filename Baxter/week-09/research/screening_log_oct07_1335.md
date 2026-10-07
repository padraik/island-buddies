# SCREENING LOG — Wed Oct 7, 2026, 1:35pm ET (VM MIDDAY run)

**Source:** research_queue.md plan written by the 12:35 run: date checks on COUR / QUBT / ONDS, then back to the Oct 7 slice (prints Nov 10-20, $2-25, bottom quartile, $300M+), the next 10 names cheapest first.

| Step | Names | Tool |
|---|---|---|
| Dates | COUR, QUBT, ONDS + 10 slice names | get_earnings_results |
| Ratings | 17 queue names + 10 slice names | get_equity_analyst_ratings (1 call) |
| Requotes | COUR, QUBT, ONDS, FUBO | get_option_quotes, get_equity_quotes |
| Chains | BZ, JBIO, HSAI, CTGO, BCAX, WYFI, LEGN, PPTA (Nov20 calls, first two OTM strikes) | get_option_instruments, get_option_quotes |
| R6 history | BZ, HSAI, CTGO, PPTA (4 prints each, daily closes) | get_equity_historicals |
| Moved this run | **10** slice names + 3 date checks + FUBO requote | |
| Killed | **10** | |

## Dates (queue)

| Ticker | Date (tool) | Verified | Note |
|---|---|---|---|
| COUR | Oct 22 PM | false | Unchanged. |
| QUBT | Nov 13 PM | false | Unchanged. |
| ONDS | Nov 12 AM | false | Unchanged. |

## Requotes (1:35pm ET)

| Ticker | Stock | Contract | Bid / Ask | R5 / R6 at the ask |
|---|---|---|---|---|
| COUR | $5.09 | $5C Nov20 | 0.40 / 0.70, OI 3,137 | Passes R5 ($0.70 <= $0.741). BE $5.70. Date gate only. |
| QUBT | $7.525 | $8C Nov20 | 0.51 / 0.54, OI 769 | Max price = 7.525 x 1.1388 - 8.00 = $0.570. Passes at the ask (BE $8.54, +13.5% vs 13.88%, 97% of cap). Date gate only. |
| ONDS | $7.115 | $8C Nov20 | 0.44 / 0.46, OI 10,604 | Max price = 7.115 x 1.2089 - 8.00 = $0.601. Passes (BE $8.46, +18.9% vs 20.89%). Date gate only. |
| FUBO | — | $10C Nov20 | 0.65 / 0.84 | Ask fails R5. |

**Ratings:** all 17 queue names unchanged (COUR 8/4/0 $6; QUBT 5/2/0 $10; ONDS 11/0/0 $13; FUBO 8/2/0 $12; FINV 6/1/0 $4.11; BRSL 7/3/0 $11.90; TME 22/14/0 $9.04; OBDC 11/2/0 $11; GAU 5/1/0 $2.99; SERV 6/2/0 $7; FRMI 6/2/0 $6; ADTN 7/2/0 $11; MLCO 11/4/0 $5.30; PCT 3/3/0 $6; ENVX 7/3/1 $5; BXMT 5/4/0 $16; CWH 11/2/0 $6).

## Oct 7 slice: 10 names

| Ticker | Direction | Stock | Print (tool) | Ratings B/H/S, low | Chain (Nov20) | R6 (4 prints) | Verdict |
|---|---|---|---|---|---|---|---|
| BZ | CALLS | $15.105 | Nov 17 AM, unverified | 19/3/0, $17.05 | $15C 0.70 / 0.95; $17.5C 0.10 / 0.25 (BE $17.75, +17.5%) | +1.3, -5.9, -0.3, +5.5: median 3.42%, cap 5.12%, max BE $15.88 | **KILL, R6 + R5**: $15C ask over the line and BE $15.95 > max; $17.5C needs 3.4x the cap. |
| VIPS | CALLS | $12.815 | Nov 19 AM, unverified | 13/10/0, $12.80 | not pulled | not pulled | **KILL, R4 (free)**: low target $12.80 is at the stock price; any OTM BE sits above it, and an ITM strike's intrinsic alone is over $0.741. |
| JBIO | CALLS | $13.805 | Nov 12 AM, unverified | 11/0/0, $40 | $15C no bid / 4.90, OI 1; $17.5C no bid / 4.60, OI 80 | not pulled | **KILL, liquidity + R5**: no market on the OTM strikes. |
| HSAI | CALLS | $15.96 | Nov 10 AM, unverified | 24/1/0, $21.89 | $17.5C 0.75 / 0.90; $20C 0.30 / 0.40 (BE $20.40, +27.8%) | -9.9, -14.2, -9.0, -5.3: median 9.46%, cap 14.18%, max BE $18.22 | **KILL, R6 + R5**: $17.5C ask over the line (BE $18.40 > max too); $20C needs 2x the cap. All four prints fell. |
| CTGO | CALLS | $16.39 | Nov 5 AM, unverified | 6/0/0, $28 | $17.5C 0.85 / 1.15; $20C 0.35 / 0.55 (BE $20.55, +25.4%) | -5.5, -2.6, -6.3, +3.7: median 4.61%, cap 6.91%, max BE $17.52 | **KILL, R6 + R5.** |
| BCAX | CALLS | $16.64 | Nov 9 AM, unverified | 12/1/0, $20 | $17.5C no bid / 4.90, OI 0; $20C no bid / 4.90, OI 0 | not pulled | **KILL, liquidity**: no market. |
| WYFI | CALLS | $16.65 | Nov 12 PM, unverified | 11/1/0, $32 | $17.5C 1.85 / 2.10; $20C 1.15 / 1.30 | not pulled | **KILL, R5**: both near strikes' bids over the line; next strike ($22.5C) needs +35%+. |
| PHI | CALLS | $18.61 | Nov 10 AM, unverified | 7/2/1, $14.41 | not pulled | not pulled | **KILL, R4 (free)**: low target $14.41 below the stock; only a deep-ITM strike clears it, and its intrinsic is over $4. |
| LEGN | CALLS | $19.04 | Nov 11 AM, unverified | 12/5/0, $24 | $20C 0.70 / 1.40 (ask size 10); $22.5C no bid / 1.15 | not pulled | **KILL, R5 + liquidity.** |
| PPTA | CALLS | $20.07 | Nov 16 AM, unverified | 6/0/0, $30 | $22.5C 0.85 / 1.00; $25C 0.30 / 0.45 (BE $25.45, +26.8%) | +4.8, +11.1, +5.3, -3.4: median 5.07%, cap 7.60%, max BE $21.60 | **KILL, R6 + R5.** |

**Takeaway:** the $12-25 band is close to useless at a $741 reserve. Every name had 2.5-wide strikes; the first OTM strike costs more than $0.741 and the one above it needs 2-4x what the stock's prints deliver. The 9 slice names left (UTI, ZTO, SARO, FLY, MLYS, LINC, QURE, BXSL, CAE, all $19.5-23.4) will almost certainly die the same way. Recommend a fresh sub-$10 scan instead of finishing them by hand.

## State of the top of the queue

Unchanged: COUR, QUBT, ONDS all DOC COMPLETE, all blocked only on a company-confirmed date. QUBT is now at 97% of its R6 cap at the ask with the stock at $7.525; another ~1% down in the stock and it fails at the ask (passes at mid).

## GLOSSARY

- **Requote:** a fresh bid/ask on a contract already chain-checked.
- **R1 (52w):** (price - 52-week low) / (52-week high - 52-week low); calls need <= 0.25.
- **R2:** a confirmed earnings date before expiry. `verified: false` means the date is estimated from the company's cadence, not announced.
- **R3:** at most 1 Sell, at least 3 Buys, Buys at least equal to Holds.
- **R4:** lowest Buy target, dated within 60 days, above breakeven. "Free" R4 kill: the tool's low target is already at or below where any affordable breakeven would sit.
- **R5:** one contract's ask <= 10% of reserve / 100 at 3.5/5 (today $0.741).
- **R6:** move to breakeven <= 1.5x the median earnings-day move (the "cap"); max BE = stock x (1 + cap). AM print: prior close to print-day close. PM print: print-day close to next-day close.
- **Strike grid kill:** strikes too far apart (here $2.50) for any one strike to be both affordable and reachable.
- **DOC COMPLETE:** research doc with Iron Rules, Five-Baxter meeting, EXIT PLAN, sizing and GLOSSARY committed; entry waits only on the named gates.
