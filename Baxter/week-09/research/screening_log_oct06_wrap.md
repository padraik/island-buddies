# Screening log, Tue Oct 6, 4:15pm ET (WRAP, PREPARE)

WRAP slot: no order tools, no chains, no searches. Closing requotes on the queue's live contracts, ratings on all 11 queue names, and `get_earnings_results` on COUR and BRSL. Reserve $741.32 settled, 3.5/5 line $0.741.

## Closing requotes (queue)

| Ticker | Stock (close) | Contract | Bid / Ask | Ratings (B/H/S, low) | Date (tool) | Status |
|---|---|---|---|---|---|---|
| COUR | $5.115 (-1.3%) | $5C Nov20 | 0.50 / 0.75, OI 3,137 | 8/4/0, $6.00 | Oct 22 PM, `verified: false` | Doc complete. Date gate and R5 at the ask (0.75 > 0.741) both still shut. BE at ask $5.75, needs +12.4% vs R6 cap 19.89%. |
| BRSL | $10.22 (+2.9%) | $10C Nov20 | 0.20 / 0.80, OI 87 | 7/3/0, $11.90 | Nov 3 AM, `verified: false` | Doc next (EVENING 2). Mid BE $10.50. |
| BRSL | | $11C Nov20 | 0.20 / **0.30**, OI 53 | | | Ask down from 0.35. **R6 now passes at the ask:** BE $11.30 vs max $11.35 ($10.22 x 1.1102). Two contracts at the ask = $60. |
| MLCO | $4.26 | $4C Nov20 | 0.25 / 0.70, OI 10 | 11/4/0, $5.30 | | Blocked, stale floor. Spread widened (was 0.40/0.60). |
| PCT | $4.005 | $4C Nov20 | 0.50 / 0.65 | 3/3/0, $6.00 | | Blocked, stale floor. |
| ENVX | $2.70 | $3C Nov20 | 0.25 / 0.29 | 7/3/1, $5.00 | | Blocked, stale floor. |
| BXMT | $11.245 (+2.1%) | $11C Nov20 | 0.55 / 0.80 | 5/4/0, $16.00 | | Fails R5 at the ask (0.80). |
| CWH | $4.525 | $4C Nov20 | 0.75 / 1.00 | 11/2/0, $6.00 | | Fails R5. |
| ADTN | $7.625 (+6.6%) | $7C Nov20 | 1.05 / 1.25 | 7/2/0, $11.00 | | Fails R5; bid alone over the line. Stock ran two days: next DO run checks the $8C. |

## Tier B (ratings refreshed, no change)

| Ticker | Stock (close) | Ratings (B/H/S) | Low target | Print (tool) | Next |
|---|---|---|---|---|---|
| SUZ | $8.405 | 11/0/0 | $10.39 | Nov 5 PM, `verified: true` | R1, 4-print R6, chain |
| RKT | $11.575 | 10/8/0 | $13.00 | Oct 29 PM, unverified | R1, R6, chain |
| EFC | $11.67 | 5/2/0 | $14.00 | Nov 4 PM, unverified | R6 first (mREIT) |

No kills, no advances. Ratings unchanged on all 11 names versus 3:35pm.

## GLOSSARY

- **Requote:** a fresh bid/ask on a contract already chain-checked.
- **R1 (52w):** (price - 52-week low) / (52-week high - 52-week low); calls need <= 0.25.
- **R3:** at most 1 Sell, at least 3 Buys, Buys at least equal to Holds.
- **R5 line:** max ask per share for one contract at the conviction tier (10% of reserve / 100 at 3.5/5).
- **R6 cap:** 1.5x the median earnings-day move over the last 4 prints.
- **Max BE:** stock price x (1 + R6 cap).
- **Stale floor:** a price target set before the stock's decline, or more than 60 days ago; it doesn't count for Rule 4.
- **BE:** breakeven, strike + premium. **OI:** open interest.
- **AM / PM print:** earnings released before the open / after the close. **verified:** company-announced date (true) vs estimated from cadence (false).
