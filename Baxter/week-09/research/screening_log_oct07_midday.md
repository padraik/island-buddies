# SCREENING LOG: Wed Oct 7, 2026, 10:35am ET (VM MIDDAY)

**Source:** research_queue.md MIDDAY plan (written by OPEN): COUR date gate, ONDS floor dating + income anomaly, QUBT/FRMI requotes, then the Oct 7 slice's sub-$12 names (GBDC, GRRR, CNL, MSIF) and the cheapest $12-25 name (RGTI).

**Rule 5 line this run:** reserve = spendable $741.32 (unsettled $0.00). 3.5/5 line **$0.741**, 4/5 $1.00 (lock), screen $1.00.

Quotes pulled 10:35-10:38am ET. Market is still down across the board (most names -1% to -4% on the day).

## Summary

| Step | Count | Tool |
|---|---|---|
| Queue gate (COUR date) | Oct 22 PM, still `verified: false` | get_earnings_results |
| Requotes + ratings | 12 queue contracts, 25 names' ratings: no count or low-target changes | get_option_quotes, get_equity_quotes, get_equity_analyst_ratings |
| Floor dating | ONDS, QUBT, FINV | WebFetch (MarketBeat forecast pages, 3) |
| Fundamentals | ONDS income anomaly | get_financials |
| Dates + R1 + R6 | GBDC, GRRR, CNL, MSIF, RGTI | get_earnings_results, get_equity_historicals |
| Chains | GBDC, GRRR, CNL (none listed), RGTI | get_option_chains, get_option_instruments, get_option_quotes |
| Web searches | none | |
| Moved this run | **10**: COUR, ONDS, QUBT, FINV, FRMI, MSIF, CNL, GBDC, GRRR, RGTI | |
| Killed | **5: MSIF, CNL, GBDC, GRRR, RGTI** | |
| Advanced | **QUBT** (now passes R4 dated / R5 / R6 at the ask: doc next), **ONDS** (floor dated, anomaly explained: doc next) | |
| Blocked | **FINV** (no Buy target after the decline: Citi went Buy -> Neutral $4.10 on Aug 28; that is the tool's $4.11 low) | |

## Queue requotes (10:35am)

| Ticker | Stock | Contract | Bid / Ask | Live R6 math | Status |
|---|---|---|---|---|---|
| COUR | $5.023 | $5C Nov20 | 0.40 / 0.65 | (doc) | Ask $0.65 now **passes** R5. Oct 22 PM still `verified: false`. **Date gate still shut. No order.** |
| QUBT | $7.616 | $8C Nov20 | 0.52 / 0.60 | cap 13.88%, max BE $8.67, max price $0.67 | **Passes R5 and R6 at the ask** (BE $8.60, needs +12.9%). Floor dated (below). Nov 13 PM unverified. **Doc next.** |
| ONDS | $7.07 | $8C Nov20 | 0.42 / 0.44, OI 10,604, vol 1,192 | cap 20.89%, max BE $8.55, max price $0.55 | Passes R5 and R6 at the ask (BE $8.44, needs +19.4%, 93% of cap). Floor dated (below). Nov 12 AM unverified. **Doc next.** |
| FINV | $2.965 | $2.5C Dec18 | 0.50 / 0.65 | cap 19.85%, max BE $3.55 | Now passes R5/R6 at the ask (BE $3.15, +6.2%). **Blocked on R4 dating** (below). |
| FRMI | $4.03 | $4C Nov20 | 0.60 / 0.70 | cap ~20.1%, max BE $4.84 | Passes R5/R6 at the ask (BE $4.70). Still blocked on R4 dating; ratings unchanged. |
| FUBO | $8.82 | $10C Nov20 | 0.55 / 0.79 | max BE $10.92 | Unchanged. Mid only; ask fails R5. |
| SERV | $4.59 | $5C Nov20 | 0.30 / 0.35 (ask size 2) | cap 15.1%, max BE $5.28 | **Fails R6 at mid and ask** (BE $5.35 at ask). Floor stale after Fri Oct 9. |
| GAU | $1.975 | $2C Nov20 | 0.10 / 0.25 | max BE $2.22 | Fails R6 at the ask. Blocked on R4 dating. |
| OBDC | $9.895 | $10C Nov20 | 0.35 / 0.45 | cap 4.28%, max BE $10.32 | Fails R6 at mid and ask. Blocked on R4 dating. |
| TME | $7.885 | $8C Nov20 | 0.35 / 0.60 | | Spread wide. Blocked (date; floor turns 60 days Oct 11). |
| BRSL | $10.054 | $11C Nov20 | 0.00 / 0.30 | | No bid. Blocked. |
| ADTN | $7.615 | $8C Nov20 | 0.35 / 0.95 | | Fails R5 at the ask. Blocked, stale floor. |

Ratings on all 25 names pulled: counts and low targets unchanged from OPEN.

## Floor dating (MarketBeat forecast pages)

- **ONDS: DATED, passes R4 with room.** Citizens JMP Market Outperform $14 (Oct 5, initiation), Citigroup Market Outperform (Oct 5, no target shown), Needham Buy $19 (Sep 14), Ladenburg Buy $22.75 (Aug 17), Oppenheimer Outperform $18 (Aug 14), Roth Buy (Aug 18, no target). Lowest dated Buy target **$14** vs BE $8.44. The tool's $13 low is an older target not in the recent table; even $13 clears BE by 54%. Weiss "Sell (D+)" (Aug 4) is a quant grade, not a covering analyst; the tool counts 0 Sells.
- **QUBT: DATED.** Ascendiant Buy $32 (Aug 26, 42 days; ages out Oct 25). Other Buys: Rosenblatt $22 (Jun 29), Northland Outperform $20 (Apr 20), Lake Street Buy (Jul 6, no target): all older than 60 days. Holds: Wedbush Neutral $12 (Aug 3), Cantor Neutral $10 (Aug 11, the tool's low). Every Buy target sits more than double BE $8.60. The only dated one is a single shop, so the doc carries that as a confidence note, and it has to enter before Oct 25 or re-date.
- **FINV: NOT DATED. Blocked.** The only post-decline analyst action is Citi (Aug 28) cutting **Buy -> Neutral**, $8.10 -> $4.10. That is the tool's $4.11 low, and it's a Hold. UBS Buy $12.10 dates to May 2025. No Buy target inside 60 days. Weiss Sell (Oct 2) is a quant grade.

## ONDS income-statement anomaly (passes.md flag since Jun 1)

Quarterly (get_financials): revenue $10.1M (Q3 2025) -> $39.0M (Q4) -> $50.1M (Q1 2026) -> $83.8M (Q2 2026). Net income -$7.5M / -$104.5M / **+$362.8M** / -$88.4M. The "TTM net income above revenue" is one quarter: Q1 2026's +$362.8M on $50M of revenue, sitting between two large losses. That shape is a one-time non-cash gain (warrant/derivative fair-value swing or a gain on an investment or deconsolidation), not operating profit. The operating story is revenue up ~8x year over year with real losses. **Answered well enough for the screen; the doc still has to name the Q1 line item from the 10-Q** before money goes in.

## Fresh slice: dates, R6, chains (5 names)

R6 uses daily closes; AM print = print-day close vs prior close, PM print = next-day close vs print-day close.

| Ticker | Stock | R1 | Print (tool) | Ratings / low | Last 4 prints | Median / cap / max BE | Contract | Bid / Ask | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| MSIF | $11.65 | | none upcoming (last row May 11 2026, unverified; 2025 Q2-Q4 blank) | 4/3/0, $12.50 | n/a | n/a | | | **KILLED, R2:** the tool has no upcoming report date and a broken history; no confirmable catalyst. |
| CNL | $11.60 | 0.20 | Nov 4 AM `verified: false` | 6/0/0, $18.45 | -1.9 / -3.3 / +4.8 / -6.2 | 4.05% / 6.07% / $12.30 | none | | **KILLED: no listed options.** |
| GBDC | $12.02 | 0.16 | Nov 17 PM `verified: true` | 6/1/0, $13 | -0.8 / -2.0 / -5.2 / -0.2 | 1.44% / 2.16% / $12.28 | Nov20, 2.5-wide strikes | | **KILLED, R6 + R5 strike grid** (free): $12.5C BE > $12.28; $10C intrinsic $2.02. |
| GRRR | $11.68 | 0.22 | Nov 16 PM `verified: false` | 6/0/0, $24 | -11.3 / -0.8 / -7.8 / +9.4 | 8.61% / 12.91% / $13.19 | $12.5C Nov20 (fa309492-5807-4744-be6f-445659699b34) | 1.05 / 1.45, OI 373 | **KILLED, R5 + R6 strike grid:** the bid alone is over $0.741 and BE $13.75 > $13.19; 2.5-wide, $15C BE > max. |
| RGTI | $14.545 | 0.04 | Nov 9 PM `verified: false` | 10/4/0, $18 | +8.5 / -7.0 / -4.4 / -5.1 | 6.05% / 9.08% / $15.87 | $15C Nov20 (0a07a70d-3c0e-4a66-82f8-4e3ab5463d76) | 1.23 / 1.29, OI 2,512 | **KILLED, R5 + R6:** the bid is over the line and BE $16.26 > $15.87; any strike above $15 would need an ask under $0.37. |

## What's left of the Oct 7 slice (19, unworked)

BZ $14.96 (Nov 17 AM unverified), HSAI $15.94, VIPS $12.70 (Nov 19 AM unverified), JBIO $13.16 (Nov 12 AM unverified), CTGO $16.32, BCAX $16.47, WYFI $16.75, PHI $18.29, LEGN $18.74, PPTA $19.55, UTI $19.57, ZTO $19.77, SARO $20.46, FLY $21.56, MLYS $21.92, LINC $22.51, QURE $22.71, BXSL $23.25, CAE $23.40. RGTI's result is the pattern to expect above $12: an ATM strike on a 70%+ IV name costs over $1. Check the strike grid and the ATM ask first; skip the R6 history pull if the nearest strike's bid is over $0.741.

## GLOSSARY

- **Requote:** a fresh bid/ask on a contract already chain-checked.
- **R1 (52w):** (price - 52-week low) / (52-week high - 52-week low); calls need <= 0.25.
- **R2:** a confirmed earnings date before expiry. `verified: false` means the date is estimated from the company's cadence, not announced.
- **R3:** at most 1 Sell, at least 3 Buys, Buys at least equal to Holds.
- **R4 / floor:** the lowest analyst Buy target must sit above the call's breakeven, and it has to be dated inside 60 days and set after the decline (binder Tab 6).
- **Floor dating:** finding the date and the firm behind each Buy target, to see whether any of them is recent enough to count.
- **Quant grade:** a rating produced by a model (Weiss), not by an analyst covering the company; it doesn't count in the Buy/Hold/Sell tally.
- **R5 line:** max ask per share for one contract at the conviction tier (10% of reserve / 100 at 3.5/5).
- **R6 cap:** 1.5x the median earnings-day move over the last 4 prints; the needed move to breakeven must fit under it.
- **Max BE:** stock price x (1 + R6 cap). **Max price:** max BE minus the strike.
- **Strike grid:** the spacing of listed strikes; a 2.5-wide grid often leaves no strike that fits.
- **Intrinsic:** how far a call is already in the money (stock minus strike).
- **Non-cash gain:** an accounting profit that isn't operating income (e.g. a warrant revaluation); it can make net income bigger than revenue for a quarter.
- **BE:** breakeven, strike + premium. **OI:** open interest. **AM / PM print:** earnings before the open / after the close.
