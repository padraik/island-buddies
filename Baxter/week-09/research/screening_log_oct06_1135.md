# SCREENING LOG — Tue Oct 6, 2026, 11:35am ET (VM MIDDAY)

**Source:** research_queue.md top block. No new names screened: the run went to writing the PCT doc, per the queue's instruction ("best use of the next DO run is writing a doc").

**Rule 5 line this run:** reserve = spendable $741.32 (unsettled $0.00). 3.5/5 line **$0.741**, 4/5 $1.00 (lock), screen $1.00.

## Summary

| Step | Count | Tool |
|---|---|---|
| Requotes (chain checks) | 5 (COUR, PCT, ENVX, BXMT, CWH) | get_option_quotes |
| Ratings refresh | 5, no count changes | get_equity_analyst_ratings |
| Dates | COUR (Oct 22 PM, unverified), PCT (Nov 5 PM, unverified) | get_earnings_results |
| Web | 3 searches + 2 fetches, all PCT (decline cause, target dating) | WebSearch / WebFetch |
| Docs | **research_PCT.md written, verdict BLOCKED (R4 stale floor)** | |
| Killed | 0 | |

## Requotes

| Ticker | Stock | Contract | Bid / Ask | BE at ask | Needs | R6 cap | Ratings / low | Status |
|---|---|---|---|---|---|---|---|---|
| COUR | $5.23 | $5C Nov20 | 0.60 / 0.70 | $5.70 | +9.0% | 19.89% | 8/4/0, $6.00 | R5 passes. Blocked: date unverified, and the $6.00 low is undated (Tab 6). |
| PCT | $3.99 | $4C Nov20 | 0.50 / 0.65 | $4.65 | +16.5% | 18.58% | 3/3/0, $6.00 | Doc written. Blocked: R4 floor stale (see below). |
| ENVX | $2.685 | $3C Nov20 | 0.26 / 0.29 | $3.29 | +22.5% | 25.27% | 7/3/1, $5.00 | Passes R1/R3/R5/R6; doc next. Floor needs dating too. |
| BXMT | $11.19 | $11C Nov20 | 0.55 / 0.85 | $11.85 | +5.9% | 6.32% | 5/4/0, $16 | Fails R5 ($0.85). |
| CWH | $4.62 | $4C Nov20 | 0.75 / 0.95 | $4.95 | +7.1% | 23.90% | 11/2/0, $6 | Fails R5 ($0.95). |

## PCT Rule 4 dating (the finding)

MarketBeat's action list: TD Cowen **Hold** $7 -> $6 (May 8, 2026), Northland $13 (Jun 12), Alembic $16 (Jun 16), Cantor **Overweight $14 -> $12 (Aug 7, 2026)**, Weiss E+ Sell quant grade (Sep 2). The tool's $6.00 low is the TD Cowen Hold. The newest Buy-side target (Cantor, Aug 7) is 60 days old and predates the ~$6.90 -> $3.99 slide. Binder Tab 6 (Jul 10): floors must be dated within 60 days and published after the decline. **No qualifying floor -> Rule 4 fails on dating.** Kept on the queue as "waiting for a floor", not killed: a single fresh Buy target would unblock it.

**Process note:** the same standard applies to COUR (low $6.00, setter unknown) and ENVX (low $5.00). Earlier runs treated the tool's low as the floor without dating it. Both docs/queue entries now carry the dating check as a required gate.

## GLOSSARY

- **Requote:** a fresh bid/ask on a contract already chain-checked.
- **R5 line:** max ask per share for one contract at the conviction tier (10% of reserve / 100 at 3.5/5).
- **R6 cap:** 1.5x the median earnings-day move; the needed move to breakeven must fit under it.
- **Stale floor:** a price target set before the stock's decline, or more than 60 days ago; it doesn't count for Rule 4.
- **BE:** breakeven, strike + premium.
- **Quant grade:** model-generated rating (Weiss), not an analyst target.
