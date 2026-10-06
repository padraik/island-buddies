# Screening log, Tue Oct 6, 3:35pm ET (LASTCALL, PREPARE)

LASTCALL slot: no chains, no searches. Free steps only: requotes on the queue's live contracts, ratings, and `get_earnings_results` dates on the last three Tier B names. Reserve $741.32 settled, 3.5/5 line $0.741.

## Requotes (queue)

| Ticker | Stock | Contract | Bid / Ask | Ratings (B/H/S, low) | Date (tool) | Status |
|---|---|---|---|---|---|---|
| COUR | $5.045 | $5C Nov20 | 0.50 / 0.75 | 8/4/0, $6.00 | Oct 22 PM, `verified: false` | Doc complete. Date gate and R5 at the ask (0.75 > 0.741) both still shut. |
| BRSL | $10.23 (+3.0%) | $10C Nov20 | 0.20 / 0.80, OI 87 | 7/3/0, $11.90 | Nov 3 AM, `verified: false` | Doc next (EVENING 2). Mid BE $10.50. |
| BRSL | | $11C Nov20 | 0.20 / 0.35, OI 53 | | | Prior close $0.01 = phantom print. Mid BE $11.275 vs max $11.35. |
| MLCO | $4.266 | $4C Nov20 | 0.40 / 0.60, OI 10 | 11/4/0, $5.30 | | Blocked, stale floor. Unchanged. |
| PCT | $3.99 | $4C Nov20 | 0.55 / 0.65 | 3/3/0, $6.00 | | Blocked, stale floor. Unchanged. |
| ENVX | $2.685 | $3C Nov20 | 0.26 / 0.29 | 7/3/1, $5.00 | | Blocked, stale floor. Unchanged. |
| BXMT | $11.18 | $11C Nov20 | 0.50 / 0.75 | | | Fails R5 at the ask. |
| CWH | $4.505 | $4C Nov20 | 0.75 / 1.05 | | | Fails R5. |
| ADTN | $7.615 | $7C Nov20 | 0.90 / 1.25 | | | Fails R5. |

## Tier B, free steps

| Ticker | Stock | Ratings (B/H/S) | Low target | Print (tool) | R3 | Next |
|---|---|---|---|---|---|---|
| SUZ | $8.42 | 11/0/0 | $10.39 (+23%) | **Nov 5 PM, `verified: true`** | Pass | R1, 4-print R6, chain |
| RKT | $11.535 | 10/8/0 | $13.00 (+12.7%) | Oct 29 PM, unverified (sweep said 10/30) | Pass | R1, R6, chain |
| EFC | $11.62 | 5/2/0 | $14.00 (+20.5%) | Nov 4 PM, unverified (sweep said 11/05) | Pass | R6 first (mREIT) |

No kills, no advances. All three carried to the next DO run.

## GLOSSARY

- **Requote:** a fresh bid/ask on a contract already chain-checked.
- **R1 (52w):** (price - 52-week low) / (52-week high - 52-week low); calls need <= 0.25.
- **R3:** at most 1 Sell, at least 3 Buys, Buys at least equal to Holds.
- **R5 line:** max ask per share for one contract at the conviction tier (10% of reserve / 100 at 3.5/5).
- **R6 cap:** 1.5x the median earnings-day move over the last 4 prints.
- **Max BE:** stock price x (1 + R6 cap).
- **Stale floor:** a price target set before the stock's decline, or more than 60 days ago; it doesn't count for Rule 4.
- **Phantom print:** a last-trade or close price no real bid/ask supports.
- **BE:** breakeven, strike + premium. **OI:** open interest.
- **AM / PM print:** earnings released before the open / after the close. **verified:** company-announced date (true) vs estimated from cadence (false).
