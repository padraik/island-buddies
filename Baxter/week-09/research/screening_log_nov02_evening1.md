# Screening log: Mon Nov 2, EVENING 1 (6:00pm ET)

**Source:** the queue's carried names (TCOM, AS, FPS, AGI, VKTX, IONS, APLD, NNE, B, plus the NIO and PL floor gates), then a diff run of saved scan `e6411b30` ($8.45-25 band, R1 < 0.25, prints Nov 2 - Feb 12, call volume >= 300: 101 rows, 12 not logged since Oct 20).
**Reserve / lines:** spendable $592.15 -> R5 line at 3.5/5 = **$0.592**.
**Data:** Monday closing option quotes (stamped 20:59 UTC), last-trade closes, 52-week ranges from fundamentals, analyst counts, earnings dates and daily closes, all pulled live this run. 0 web searches on candidates (1 on FRMI, a holding).

## Chain stage

| Ticker | Dir | Stock | Next print | R3 / tool low | Contract | Bid / Ask | OI | Spread | BE / needs | R6 cap | Result |
|---|---|---|---|---|---|---|---|---|---|---|---|
| TCOM | CALLS | 40.99, R1 0.082 | Mon Nov 16 PM (f), LY Nov 17 (6-K) | 32/3/0, $42.28 | Dec18 $40C `8383612f` | 2.70 / 2.95 | 308 | 8.8% | $42.95 | | **KILLED, R4** (BE over the $42.28 low at the ask). $42.5C OI 7 (R7), $37.5C OI 0. |
| IONS | CALLS | 41.21, R1 0.00 (new low today) | Fri Nov 13 AM (f); LY Oct 29; 10-Q due Nov 9 | 24/4/0, $58 | Dec18 $40C / $42.5C / $45C | 3.10 / 6.20, 1.55 / 4.30, 1.20 / 3.20 | 0 / 79 / 210 | 67-91% | | | **KILLED, R7** on every strike near the money. Also paper-size (R5). Print date is a mess: tool says Nov 13, the 10-Q deadline says by Nov 9. |
| NNE | CALLS | 10.97, R1 0.00 | Thu Dec 17 PM (f), LY Dec 18 | 7/1/0, $19 | Jan15 $10C / $12C / $13C | 1.45 / 2.35, 1.05 / 1.25, 0.65 / 0.95 | 188 / 150 / 247 | 47% / 17% / 37.5% | | | **KILLED, R7** (third straight close under 250). Don't bring back this quarter. |
| AGI | CALLS | 27.76, R1 0.029 | Wed Feb 17 PM (f), LY Feb 18 (40-F) | 12/1/0, $34.37 | Mar19 $28C / $29C / $30C | 3.10 / 3.50, 2.65 / 3.10, 2.30 / 2.65 | 37 / 2 / 141 | 12-16% | $30C BE $32.65, +17.6% | | **KILLED, R7** (and paper-size). Q3 already reported Oct 28. |
| APLD | CALLS | 16.23, R1 0.00 | Wed Jan 6 PM (f), LY Jan 7 | 18/2/0, $22 | Apr16 $18C `d4eee0a9` / $20C `3af76e53` | 3.40 / 3.95, 3.00 / 3.15 | 270 / 905 | 15% / 4.9% | $21.95 +35.2%; $23.15 +42.6% | 12.15% (7 prints: -35.9, +31.0, +16.0, +8.1, -8.0, +0.9, +0.2; median 8.1%) | **KILLED, R6.** No Feb19 expiry exists; Apr16 is the first that clears R2, and nothing near the money is reachable. |
| VKTX | CALLS | 26.82, R1 0.155 | Wed Feb 10 PM (f), LY Feb 11 | 19/2/0, $34 | (no Mar19; Feb19 fails R2, May21 is next) | | | | | 1.5% (7 prints: -0.5, +0.3, +8.0, +6.8, -0.5, -1.0, +5.9; median 1.0%) | **KILLED, R6 structural.** No strike can clear a 1.5% cap. Q3 already reported Oct 28. |

## Free stage (carried names)

- **AS:** R1 **0.274** at $30.665 (low $26.10 Sep 18, high $42.76). OUT, mid-range now after +4.2% today. Back on only if it slides under ~$30.27.
- **B:** R1 **0.276** at $37.97 (low $31.61 is Nov 4 2025 and rolls off Wednesday, which will move the percentile). Print Mon Nov 9 AM verified, ramp would be Fri Nov 6, paper only (R5). Dropped for this quarter: two trading days of usable window, R1 failing today.
- **FPS:** only **3 reported prints** on the tool (Mar 16, May 14, Sep 15 2026; recent IPO). R6 needs 4 to 8. **KILLED, R6 unverifiable.** Print Thu Nov 12 AM verified, R1 0.033, 11/2/0, $36 low. Next quarter it has 4.
- **NIO (gate):** tool 16/7/1, low $3.7053, stamp still Sep 1. No dated Buy above BE. Gate holds. $3C Dec18 closed 0.35 / 0.39 (OI 698), stock $3.195.
- **PL (gate):** tool 8/5/0, low $17, unchanged. No new floor. Gate holds. Stock $12.97 (-3.7%).
- **ACHR (doc committed, Tuesday OPEN):** $4C Dec18 closed **0.53 / 0.72** (OI 426, closing spread 30%), stock $4.18, 8/2/0 low $7, Q3 Mon Nov 9 PM verified. Closing book is wider than the $0.59 line; OPEN re-quotes.

## Scan diff (12 never logged since Oct 20)

- **R3 fails (4):** BXSL (5/6/1), OLN (5/15/1), UPWK (3/6/0; reported today, +17.7%), GPK (2/10/1).
- **No coverage (4):** NTGR, MEC, CMRE, GPGI.
- **R4 proxy fails (2):** ACAD (15/5/1, low $16 under the $20.47 stock), SRAD (18/7/0, low $12.97 under $13.27). Both print this week anyway.
- **R2 timing (1):** STWD (6/2/0, $16 low) prints Fri Nov 6. Nothing to stand on, and an mREIT-style print history likely fails R6.
- **Carried (1):** BXMT (5/4/0, low $13 vs $11.30, R1 0.112), prints Wed Feb 11 (f). Next check: daily-close R6 on its prints first (NLY and DX died R6 structural at 0.8-1.0% medians; expect the same), chain only if the median clears ~4%.

## Watch line (price only)

ONDS $5.765 (-8.8%), RCAT $4.445, BTBT $0.7356, CLSK $7.15. All lower than their watch prices; nothing revives.

## Totals

24 names moved: 6 killed at the chain (TCOM R4; IONS, NNE, AGI R7; APLD, VKTX R6), 3 out free (AS, B R1; FPS R6 data), 2 gates held (NIO, PL), ACHR re-quoted, 12 scan-diff names (11 out, 1 carried). 0 advanced.

## GLOSSARY
- **R1-R7**: binder Tab 1 Iron Rules (calls). R1 range percentile, R2 earnings before expiry, R3 analyst consensus, R4 bear floor (lowest target above breakeven), R5 price cap on reserve, R6 reachability (needed move <= 1.5x median earnings move), R7 liquidity (OI >= 250, spread <= 25% of mid).
- **BE**: breakeven at expiry = strike + ask.
- **OI**: open interest, contracts outstanding.
- **(f)**: earnings date estimated from cadence, not announced.
- **LY**: last year's same-quarter report date.
- **6-K / 40-F filer**: foreign issuer, no 10-Q deadline, so R2 needs both the tool date and last year's date.
- **R4 proxy**: at the free stage, a tool low target at or under the stock price means no strike can pass R4.
- **Closing spread**: the wider book quoted in the last minute of the session.
- **Paper-size**: one contract costs more than the R5 line, so it can only go in the paper book.
- **mREIT**: mortgage REIT; these print tiny earnings moves, which is why R6 kills them.
