# Screening log: Mon Oct 19, EVENING 3 (10:00pm ET)

**Session job:** refill the queue (7 live, under 10) and leave PREMARKET a plan. EVENING 2 already re-ran the Oct 22 - Dec 23 sweep (416 rows, 4 new), so tonight did two other things: (1) re-quoted 30 old R6 kills to see if any moved >5% toward their strike since the kill; (2) opened a print window nobody had swept, **Dec 24 - Feb 20**. Quotes are Monday's close / after-hours (~02:00 UTC Oct 20). Reserve (spendable) $676.28: Rule 5 3.5/5 line $0.676, so anything over that is paper only. 1 web search.

## Part 1: old R6 kills, re-quoted (free)

Kill price from the week-09 logs vs Monday's close. The test: did the stock move >5% toward the strike since it died?

| Ticker | Kill price | Mon close | Move | Verdict |
|---|---|---|---|---|
| XENE | $33.47 | $35.08 | +4.8% | stays dead (needed +15.0% vs a 4.20% cap; nowhere close) |
| ALNY | $224.42 | $233.39 | +4.0% | re-checked anyway (R6 was the near miss): see below. **KILL R7** |
| VERA | $27.91 | $28.95 | +3.7% | stays dead (needed +19.7% vs 2.67%) |
| WULF | $11.655 | $12.06 | +3.4% | stays dead (needed +24.4% vs 10.18%) |
| IREN | $27.00 | $27.73 | +2.7% | stays dead |
| NKTR, CRVS, IMCR, KKR, RKLB, NNE, CLSK | | | -0.5% to +2.1% | stay dead |
| CDE, VST, BWXT, LUNR, ECHO, KRMN, IONQ, MP, SMG, BTU, CENX | | | -3.0% to -0.2% | stay dead |
| FN, LEU, AVAV, AMKR, FIGR | | | -2% to -8% | further away |
| **ALGM** | $31.61 (Fri WRAP kill) | $33.18 | **+5.0%** | **re-opened**, see below |
| UEC | | $7.885 | | already dead on R4 (stale floor, EVENING 1) |

**ALNY** Nov20 $230C (`736ea6c9-92b6-4210-bfae-6969004da73e`): 16.70 / 20.70, BE $248.70 = +6.6% vs the 8.2% cap. R6 now passes. **OI 135** (spread 21%) -> **KILL R7.** $240C OI 55, $220C OI 9. Q3 Thu Oct 29 AM verified; 24/9/0, low $250.

**ALGM** Nov20 (Q3 FY27 **Thu Oct 29 AM `verified: true`**, LY Oct 30 AM; Nov20 is 22 days after the tool date and 21 after LY; 10-Q deadline ~Nov 5, 11 trading days before expiry: R2 passes).
- R1: 52-week low $22.41 (wk of Nov 17 2025), high $71.77 (wk of Jun 29 2026). $33.18 -> **0.218**. Line $34.75.
- R3: **14/1/0.** R4: tool low **$40** (it was **$48** at the Oct 16 WRAP, so somebody cut it in the last two sessions). `updated_at` missing.
- Chain: **$32.5C** `336afbdd-6e57-4535-9c1f-6f786c8e9984` 3.20 / 3.70, **OI 972**, spread 14.5% (R7 pass), BE **$36.20 = +9.1%** vs the **10.5% cap** (Oct 14 log). R6 passes. $35C 1.90 / 2.70, OI 6,823, spread 34.8% (R7 fail on the spread tonight; re-quote in daylight).
- R4: $40 vs BE $36.20 = $3.80 over. One search ("Allegro MicroSystems price target lowered $40 October 2026"): BofA $45 -> $38 (Sep 2025), Barclays cuts to $25 / $22 (2025), Mizuho $37 -> $40 (undated), an Aug 3 2026 MarketBeat downgrade headline. **The $40 has no owner or date yet.** It wasn't the low on Friday, so it's probably fresh, but "probably" isn't a dated floor.
- **ADVANCE (paper), floor-dating gate.** Ask $3.70 is ~5.5x the real-money line. Ramp sell would be **Wed Oct 28 3:35pm** (pre-market print Thu). Kill date **Mon Oct 26** if the floor isn't dated.

## Part 2: new print window, Dec 24 - Feb 20

Preview (not saved): market cap >= $300M, `FILTER_TYPE_EARNINGS_DATE` **20261224-20270220**, `FILTER_TYPE_TOTAL_CALL_VOLUME` > 300, 52w range pct < 0.25. **17 rows.** Already seen and dead: CALM (R3), MKC (R4+R7), SHAZ (R6), APLD (R4), ADUR (no coverage), NG (R6), TLRY (R3).

| Ticker | Direction | Last | R1 (scan) | R3 B/H/S, low target | R2 (tool, LY) | Verdict |
|---|---|---|---|---|---|---|
| PEP | CALLS | $134.25 | 0.225 | 8/17/1, $106 | -- | **KILL R3** (Buys < Holds) |
| PLD | CALLS | $123.96 | 0.080 | 13/5/0, **$140** | Jan 20 AM (f), LY Jan 21 | **ADVANCE** to chain (Mar19; Q4 = 10-K) |
| SCHW | CALLS | $89.88 | 0.194 | 19/6/1, $82 | -- | **KILL R4 proxy** (low $82 under the price) |
| BAC | CALLS | $50.46 | 0.227 | 23/5/0, **$55** | **Jan 15 AM (v)**, LY Jan 14 | **ADVANCE** to chain (Mar19) |
| AA | CALLS | $41.51 | 0.130 | 14/4/1, **$48** | Jan 21 PM (f), LY Jan 22 | **ADVANCE** to chain (Mar19) |
| GFI | CALLS | $36.60 | 0.180 | 8/6/2 | -- | **KILL R3** (2 Sells) |
| XRPN | CALLS | $15.08 | 0.116 | no coverage | -- | **KILL R3** |
| INFY | CALLS | $12.01 | 0.095 | 24/21/5 | -- | **KILL R3** (5 Sells) |
| SBSW | CALLS | $9.67 | 0.134 | 6/4/1, $9.60 | -- | **KILL R4 proxy** (low under the price) |
| TMQ | CALLS | $2.31 | 0.002 | 3/3/0, $4.30 | Feb 16 AM (f), LY Feb 17 | **KILL R7**: Mar19 $2C 0.50 / 0.85 OI 119 (spread 52%), $3C 0.15 / 0.40 OI 106, $4C 0.05 / 0.25 OI 192. The only real-money-priced name tonight, and nobody trades it |

**R2 note for the January prints:** these are fiscal Q4 reports, so the backstop is the **10-K** deadline (60 days for large accelerated filers: ~Mar 1), not a 10-Q. Feb19 fails part (b) (Mar 1 is after expiry); **Mar19 passes** (Mar 1 is 13 trading days before). Every January-print name needs the Mar19 chain.

PLD, BAC, AA are paper candidates at best (every Mar19 near-the-money call is several dollars). Next check: Mar19 chain (R7) and six-print R6 base. Big banks and REITs usually move 1-3% on a print, so BAC and PLD are R6 long shots; AA moves more.

## Moved this run

40 names touched: 30 old kills re-quoted (2 re-checked on chains: ALNY killed R7, **ALGM re-opened, paper, floor gate**); 10 new scan names: 7 killed (PEP, GFI, XRPN, INFY on R3; SCHW, SBSW on the R4 proxy; TMQ on R7), 3 advanced to the chain stage (PLD, BAC, AA). 1 search.

## GLOSSARY

- **R1-R7:** the Iron Rules in binder Tab 1. R1 range position, R2 earnings before expiry, R3 analyst consensus, R4 bear floor (lowest Buy target above breakeven), R5 price cap, R6 reachability (needed move vs 1.5x median print move), R7 liquidity (OI >= 250, spread <= 25% of mid).
- **Range pct / percentile:** where the price sits between the 52-week low (0) and high (1). Calls need under 0.25.
- **BE (breakeven):** strike + premium paid.
- **OI (open interest):** contracts outstanding on that exact strike and expiry.
- **Spread:** ask minus bid, as a % of the midpoint.
- **R4 proxy:** a free pre-chain check. If the lowest Buy target is already under the stock price, no call can have a breakeven under it.
- **Floor-dating gate (Tab 6):** a bear floor only counts if it was published within 60 days and after the decline.
- **10-K / 10-Q deadline:** the SEC's last legal filing day for an annual / quarterly report, used as the worst-case date the print must land before.
- **(v) / (f):** earnings date verified by the company / estimated from the cadence.
- **Paper:** tracked in `paper_book.md`, no money moves.
- **Ramp sell:** selling before the print to capture the pre-earnings premium, instead of holding through the IV crush.
