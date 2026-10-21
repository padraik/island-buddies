# Screening log: Tue Oct 20, EVENING 2 (8:00pm ET)

**Session job:** write research docs for every name that cleared the chain stage. Only one did: **QUBT Dec18 $7C** (parked by EVENING 1). Doc: `research_QUBT_dec18.md`. Finished early, so the session started the next job: the Dec18 strike lists EVENING 1 couldn't find for PONY, IE, FUN, STUB, ALMS, plus an APH re-check. Market closed; every option quote is the 4:00pm close (stamped 19:59-20:00 UTC). Reserve (spendable) $676.28: Rule 5 3.5/5 line **$0.676**. 1 web search.

## Part 1: the doc

| Ticker | Contract | Result |
|---|---|---|
| QUBT | Dec18 $7C (`d92fe604`) | **DOC COMPLETE, gated on R6 at a live regular-session quote and the floor's date (last day Fri Oct 23).** Close 0.47 / 0.52, OI 1,091, spread 10.1%. Stock **official close $6.50** (EVENING 1 used an intraday $6.57), AH $6.63. R1 0.033 (52w low $6.08 on Oct 15). R2: later of tool Nov 13 / LY Nov 14 -> Dec18 34 days; 10-Q by Nov 16 at the latest. R3 5/2/0. R4: tool low $10 is Cantor Hold; lowest dated Buy Ascendiant $32 (Aug 26, ages out Oct 25); one search found no newer target. R5 pass. R7 pass. **R6: needs +15.69% at the close vs 13.875% cap (fails by 1.8pt); +13.42% at the AH $6.63 (passes).** Line: ask <= stock x 1.13875 - 7.00 |

## Part 2: Dec18 strike lists (EVENING 1's leftovers)

All five pass R3 with lows 68-123% over the price (EVENING 1). R2 not re-pulled: each one dies on the chain first.

| Ticker | Stock (close) | Dec18 grid | Contract | Bid / Ask | OI | Spread | BE / needs | Verdict |
|---|---|---|---|---|---|---|---|---|
| PONY | $5.28 | $2.5 / 5 / 7.5 / 10 | $5C | 0.48 / 1.01 | **33** | 71% | $6.01 / +13.8% | **KILL R7** |
| | | | $7.5C | 0.07 / 0.14 | **11** | 67% | $7.64 / +44.7% | R7, R6 |
| IE | $8.45 | $2.5-17.5 by 2.5 | $7.5C | 1.30 / 1.70 | **4** | 27% | ask > $0.676 | R7, R5 |
| | | | $10C | 0.30 / 0.60 | 3,570 | **66.7%** | $10.60 / **+25.4%** | **KILL R7** (closing spread) **+ R6** (needs a 16.9% median print; not plausible for a $1.2B miner, not pulled) |
| FUN | $7.86 | $2.5-65 | $7.5C | 1.05 / 1.30 | **106** | 21% | ask > $0.676 | R7, R5 |
| | | | $10C | 0.30 / 0.45 | **187** | 40% | $10.45 / +33.0% | **KILL R7** (and R6) |
| STUB | $5.94 | $2.5-35 | $5C | 1.15 / 1.35 | 632 | 16% | ask $1.35 > $0.676 | R5 |
| | | | $7.5C | 0.20 / 0.30 | 1,547 | **40%** | $7.80 / **+31.3%** | **KILL R7 + R6** (needs a 20.9% median print) |
| ALMS | $6.70 | $1-17 by 1, then wider | $7C | 0.45 / 1.20 | 632 | **91%** | ask $1.20 > $0.676 | **KILL R5 + R7** |
| | | | $8C | 0.05 / 0.85 | **67** | 178% | | R7 |

## Part 3: APH re-check

| Ticker | Contract | Close | R6 line | Verdict |
|---|---|---|---|---|
| APH | Nov20 $80C (`d254aa6a`) | 4.00 / 4.30 (OI 5,713), stock **$79.32** close (AH $80.89) | ask <= 79.32 x 1.0607 - 80 = **$4.13** | **Still R6, by $0.17.** AH would pass, but no entry math off AH. Paper-size only. Kill Fri Oct 23 |

## Moved this session

**6 names moved:** QUBT (chain -> doc), PONY, IE, FUN, STUB, ALMS (strike list -> killed). **5 killed:** PONY (R7), IE (R7 + R6), FUN (R7), STUB (R7 + R6), ALMS (R5 + R7). APH unchanged.

## GLOSSARY

- **R1-R7:** the Iron Rules (binder Tab 1): range percentile, earnings before expiry, ratings consensus, bear floor, chain price cap, reachability, liquidity floor.
- **BE / needs:** breakeven (strike + ask) and the stock move required to reach it from the close.
- **R6 line:** the highest ask at which the breakeven move stays inside 1.5x the median earnings move.
- **OI:** open interest, contracts outstanding on the strike. Rule 7 needs 250+.
- **Spread:** (ask - bid) / mid. Rule 7 needs 25% or less on a live quote; closing spreads run wide, so a closing-only R7 fail on a name with OI gets a daytime re-check only if nothing else kills it.
- **AH:** after-hours trading, thin; never used for entry math.
- **Dated floor:** a Buy-rated analyst target published within 60 days and after the decline (binder Tab 6).
