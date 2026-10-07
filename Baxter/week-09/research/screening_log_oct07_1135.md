# SCREENING LOG — Wed Oct 7, 2026, 11:35am ET (VM MIDDAY)

**Source:** research_queue.md plan written by the 10:35 run: date checks on COUR / QUBT / ONDS, then write `research_QUBT.md` (best live candidate past the chain stage), ONDS doc if time, no new slice names unless both docs are done.

**Rule 5 line this run:** reserve = spendable $741.32 (unsettled $0.00). 3.5/5 line **$0.741**, 4/5 $1.00 (lock), screen $1.00.

## What ran

| Step | Names | Tool |
|---|---|---|
| Dates | COUR, QUBT, ONDS | get_earnings_results |
| Ratings | 15 queue names (COUR, QUBT, ONDS, FUBO, FINV, BRSL, TME, OBDC, GAU, SERV, FRMI, ADTN, MLCO, PCT, ENVX) | get_equity_analyst_ratings (1 call) |
| Requotes | COUR, QUBT, ONDS, FUBO, FRMI, SERV | get_option_quotes, get_equity_quotes |
| R1 + R6 rebuild | QUBT (1 year daily) | get_equity_historicals, get_equity_fundamentals |
| Web | QUBT date, QUBT news | WebSearch (2) |
| Doc written | **QUBT** | `research_QUBT.md` |
| Moved this run | **QUBT** (chain passed -> DOC COMPLETE, blocked on R2 verification) | |
| Killed | none | |

## Dates

| Name | Tool date | Verified | Note |
|---|---|---|---|
| COUR | Oct 22 PM | false | Unchanged. No company announcement yet (Q2 date came out 14 days ahead; expected ~Oct 8). |
| QUBT | Nov 13 PM | false | **One web search: aggregators say Nov 9 PM**, also an estimate. Two candidates, so the ramp-sell date can't be pinned. |
| ONDS | Nov 12 AM | false | Unchanged. |

## Requotes (11:35am)

| Name | Stock | Contract | Bid / Ask | Cap / max BE / max price | Verdict |
|---|---|---|---|---|---|
| COUR | $5.03 | $5C Nov20 | 0.40 / 0.65 | 19.89% / $6.03 / $1.03 | Passes R5/R6 at the ask (BE $5.65, +12.3%). **Date gate only.** |
| QUBT | $7.555 | $8C Nov20 | 0.53 / 0.55, OI 769 | 13.88% / $8.60 / **$0.60** | Passes R5/R6 at the ask (BE $8.55, +13.2%, 95% of cap). **Doc written; date gate only.** |
| ONDS | $7.055 | $8C Nov20 | 0.42 / 0.43, OI 10,604 | 20.89% / $8.53 / $0.53 | Passes R5/R6 at the ask (BE $8.43, +19.5%, 93% of cap). Doc next. Date unverified. |
| FUBO | $8.895 | $10C Nov20 | 0.58 / 0.77 | 23.84% / $11.02 / $1.02 | Ask fails R5 ($0.77 > $0.741); mid passes. |
| FRMI | $3.995 | $4C Nov20 | 0.55 / 0.60 | ~20.1% / $4.80 / $0.80 | Passes R5/R6 at the ask. Still blocked on R4 dating. |
| SERV | $4.55 | $5C Nov20 | 0.31 / 0.35 | 15.1% / $5.24 / $0.24 | **Fails R6 at mid and ask.** Floor stale after Fri Oct 9. |

## Ratings (all 15 unchanged from 10:35)

COUR 8/4/0 low $6; QUBT 5/2/0 low $10; ONDS 11/0/0 low $13; FUBO 8/2/0 low $12; FINV 6/1/0 low $4.11; BRSL 7/3/0 low $11.90; TME 22/14/0 low $9.04; OBDC 11/2/0 low $11; GAU 5/1/0 low $2.99; SERV 6/2/0 low $7; FRMI 6/2/0 low $6; ADTN 7/2/0 low $11; MLCO 11/4/0 low $5.30; PCT 3/3/0 low $6; ENVX 7/3/1 low $5.

## QUBT R6 rebuild (from daily closes, all PM prints)

| Print | Close print day | Close next day | Move |
|---|---|---|---|
| Q3 2025, Nov 14 2025 (Fri) | $10.60 | $11.50 (Nov 17) | +8.5% |
| Q4 2025, Mar 2 2026 | $8.59 | $7.73 | -10.0% |
| Q1 2026, May 11 2026 | $10.18 | $11.78 | +15.7% |
| Q2 2026, Aug 10 2026 | $8.93 | $8.95 | +0.2% |

Median absolute 9.25%, cap 13.88%. Matches the Oct 6 EVENING 2 numbers.

## GLOSSARY

- **Requote:** a fresh bid/ask on a contract already chain-checked.
- **R1 (52w):** (price - 52-week low) / (52-week high - 52-week low); calls need <= 0.25.
- **R2:** a confirmed earnings date before expiry. `verified: false` means the date is estimated from the company's cadence, not announced.
- **R3:** at most 1 Sell, at least 3 Buys, Buys at least equal to Holds.
- **R4 / floor:** the lowest analyst Buy target must sit above the call's breakeven, dated inside 60 days and set after the decline (binder Tab 6).
- **R5 line:** max ask per share for one contract at the conviction tier (10% of reserve / 100 at 3.5/5).
- **R6 cap:** 1.5x the median earnings-day move over the last 4 prints; the needed move to breakeven must fit under it.
- **Max BE:** stock price x (1 + R6 cap). **Max price:** max BE minus the strike.
- **BE:** breakeven, strike + premium. **OI:** open interest. **AM / PM print:** earnings before the open / after the close.
