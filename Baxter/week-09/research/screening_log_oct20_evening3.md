# Screening log: Tue Oct 20, EVENING 3 (10:00pm ET), queue refill

*EVENING session 3 of 3. Job: refill the queue (it was 3 live) and leave PREMARKET a plan. Market closed; every quote below is the 4:00pm close unless marked AH. No searches.*

**What ran:** (1) a fresh scan, market cap >= $300M, earnings 20261022-20261225, last $0.50-12, 52w range pct < 0.25, call volume >= 100: **193 rows**. (2) Free R3 + R4-proxy pass on all 193 (3 ratings calls). (3) Chain re-tests on the six R3 passers under $9 whose old kills were price-sensitive (R5/R6, not structural). (4) Free R1-R3 + earnings dates on six paper-size names EVENING 1 flagged.

## Part 1: the scan

193 rows, ~70 pass R3. Every R3 passer under $12 has been chained at least once in week 09. The structural R6 kills (KEEL, SOC, HIVE, TE, GRAB, DNN, NXE, SANA, AQST, MNKD, ALLO, LUNR, RKT) all closed lower than at their kill, so their math got worse, not better. They stay dead. Re-tested only the names where price or a missing strike was the problem.

## Part 2: chain re-tests (real-money shape: sub-$10, near-money strike, OI >= 250)

| Ticker | Close | R3, low | Print (tool) | Contract | Bid / ask | OI | Spread | Verdict |
|---|---|---|---|---|---|---|---|---|
| CTMX | $2.51 | 8/0/0, $6 | Nov 5 PM (f) | Dec18 $2C | 0.20 / 1.15 | **0** | 141% | R7 |
| | | | | Jan15 $2C | 0.45 / 1.20 | **243** | 91% | R7 + R5 (ask $1.20) |
| | | | | Jan15 $3C | 0.25 / 0.55 | 489 | **75%** | **KILL R7** (+ R6: BE $3.40 mid = +35% vs 19.1% cap) |
| BTDR | $7.84 | 13/1/0, $10 | Nov 10 | Dec18 $7.5C | 1.35 / 1.60 | **149** | 17% | R7, R5 |
| | | | | Dec18 $9C | 0.75 / 0.95 | 1,691 | 23.5% | **KILL (real) R5** ($0.95 > $0.676). R7 passes. BE $9.95 = +26.9%: R6 table not pulled. Paper-size queue |
| FRMI | $2.94 | 6/2/0, $6 | Nov 12 | Dec18 $2.5C | 0.60 / 0.95 | **246** | 45% | R7 |
| | | | | Dec18 $3C | 0.45 / 0.70 | **141** | 43% | **KILL R7** ($3.5C OI 28) |
| BTGO | $5.74 | 11/2/0, $7.50 | Nov 30 | Dec18 $5C | 0.85 / 1.40 | **0** | 49% | R7 |
| | | | | Dec18 $7.5C | 0.15 / 0.25 | **123** | 50% | **KILL R7** (strikes only every $2.50) |
| EXK | $8.20 | 6/1/0, $10.65 | Nov 9 | Dec18 $7.5C | 1.05 / 1.55 | **0** | | R7 |
| | | | | Dec18 $9C | 0.50 / 0.60 | **2** | 18% | **KILL R7** |
| RGNX | $7.40 | 10/2/0, $10 | Nov 5 | Dec18 $7C / $8C | 0.00 / 4.90 | **0** | no market | **KILL R7** |

**6 chain re-tests, 6 out of the real-money pool.** Five on R7 (no open interest near the money), BTDR on R5 (its only liquid strike costs $0.95). The R5 line is $0.676, and the sub-$10 names with real OI near the money all fail R6. QUBT Dec18 $7C is still the only real-money contract on the board.

## Part 3: paper-size names (free R1-R3, earnings)

| Ticker | Close (AH) | R3, low | Low vs price | Q3 print (tool) | LY same Q | First expiry passing R2 | Verdict |
|---|---|---|---|---|---|---|---|
| GLXY | $15.76 ($16.30) | 15/1/0, $24 | +52% | **Tue Oct 27 AM, verified** | Oct 21 AM | Nov20 (24 days) | **ADVANCE to chain.** Ramp sell Mon Oct 26 3:35pm, so only Wed-Fri entries are worth it |
| MIR | $15.24 | 10/1/0, $20 | +31% | **Tue Oct 27 PM, verified** | Oct 28 PM | Nov20 (23 days past LY) | **ADVANCE to chain.** Ramp sell Tue Oct 27 3:35pm |
| HSAI | $13.99 ($14.41) | 24/1/0, $19.42 | +39% | Nov 10 AM, verified | Nov 11 AM | Dec18 (6-K filer, both dates present) | ADVANCE to chain |
| MLYS | $21.58 | 8/2/0, $29 | +34% | Nov 9 PM (f) | Nov 10 PM | Dec18 | ADVANCE to chain |
| LEGN | $19.01 | 12/5/0, $24 | +26% | Nov 11 AM (f) | Nov 12 AM | Dec18 (6-K filer, both dates present) | ADVANCE to chain |
| SARO | $21.43 | 13/3/0, $25 (stamp Oct 1) | +17% | Nov 9 PM (f) | Nov 10 PM | Dec18 | ADVANCE to chain (thin R4 room) |

All six were bottom quartile in EVENING 1's under-$25 pass. They're paper-size (any near-money strike costs over $0.676). Each still needs a dated floor (Tab 6), a print table (R6), and a live R7 quote.

Skipped: QXO (R6 kill Oct 9, stock about flat since), RIOT (R2 kill Oct 20 at 11:35: date moved to Nov 2, Dec18 R6).

## Watch line (AH, not used for math)

ONDS $6.10 close / $6.19 AH (line ~$6.90), BTBT $0.90 / $0.94 (~$1.10), CLSK $8.43 / $8.70 (~$9.20). None revived.

## QUBT note for OPEN

Close $6.50; AH $6.65 (bid 6.64 / ask 6.65 at 10pm). The Dec18 $7C closed 0.47 / 0.52. **R6 line = stock x 1.13875 - 7.00**: $0.40 at $6.50, **$0.573 at $6.65**. If the stock opens near the AH print and the ask holds near 0.52, it passes. Regular-session quote only, after 9:45.

## Moved this session

**12 names moved:** 6 chain re-tests (CTMX, BTDR, FRMI, BTGO, EXK, RGNX), all killed for real money; 6 paper-size names advanced to the chain stage (GLXY, MIR, HSAI, MLYS, LEGN, SARO). BTDR $9C goes back on the queue paper-size (R7 passes, R6 open).

## GLOSSARY

- **R1-R7:** the Iron Rules (binder Tab 1): range percentile, earnings before expiry, ratings consensus, bear floor, chain price cap, reachability, liquidity floor.
- **R3 a/b/c:** Buy / Hold / Sell counts from the ratings tool.
- **Low vs price:** the tool's lowest target over the close. A free R4 proxy; the real test is a dated Buy target over the breakeven.
- **(f):** the tool's earnings date is `verified: false` (estimated from cadence).
- **LY same Q:** last year's report date for the same quarter. Rule 2 needs the expiry 21+ days past the later of this and the tool date.
- **6-K filer:** a foreign issuer with no 10-Q deadline, so Rule 2 needs both dates present.
- **OI:** open interest. Rule 7 needs 250+.
- **Spread:** (ask - bid) / mid. Rule 7 needs 25% or less.
- **R5 line:** $0.676 per share = 10% of the $676.28 reserve (3.5/5 tier).
- **R6 line:** the highest ask at which the breakeven move stays inside 1.5x the median earnings move.
- **Paper-size:** passes everything testable except the real-money price cap; goes to the paper book instead.
- **AH:** after-hours, thin; never used for entry math.
