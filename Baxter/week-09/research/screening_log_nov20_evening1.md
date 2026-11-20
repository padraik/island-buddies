# Screening log: Fri Nov 20, EVENING 1 (6:00pm ET)

**Job (from Thursday EVENING 3's plan, pulled forward from Saturday):** books for the four R6-tabled stagers (CAPR, BRSL, EQX, NUVB), GLNG's second date pull, then the IV-vs-print ratio pass on the staged pool: median print move against the near-ATM spring contract's time value.

**Source:** Robinhood tools only, run ~23:00-23:30 UTC on Friday's closing books (option quotes stamped ~20:59 UTC Nov 20). 0 web searches. R5 line tonight: 10% x $715.96 reserve / 100 = **$0.716/share** (3.5/5). Daily bars ran through Nov 19 (no Nov 20 bar yet), so every max-BE below uses Friday's last regular-session trade from `get_equity_quotes`.

## (1) The four staged books (Friday close)

R6 tables from Nov 19 EVENING 3; max BE re-based on Friday's price.

| Contract | Stock | Bid / Ask | Spread % mid | OI | BE at ask | Needs | Max BE (cap) | Verdict |
|---|---|---|---|---|---|---|---|---|
| CAPR $7C Jun17 | 7.60 | 2.30 / 7.00 | 101% | 11 | 14.00 | +84% | 8.59 (13.0%) | R5, R6, R7 |
| CAPR $8C Jun17 | 7.60 | 2.20 / 5.30 | 83% | 0 | 13.30 | +75% | 8.59 | R5, R6, R7 |
| CAPR $9C Jun17 | 7.60 | 1.80 / 6.50 | 113% | 10 | 15.50 | +104% | 8.59 | R5, R6, R7 |
| BRSL $8C Apr16 | 8.565 | 0.65 / 1.55 | 82% | 0 | 9.55 | +11.5% | 9.54 (11.4%) | R5, R7; **R6 misses by 1 cent** |
| BRSL $9C Apr16 | 8.565 | 0.20 / 1.25 | 145% | 3 | 10.25 | +19.7% | 9.54 | R5, R6, R7 |
| BRSL $10C Apr16 | 8.565 | 0.00 / 1.00 | - | 10 | 11.00 | +28% | 9.54 | R6, R7 (no bid) |
| EQX $7.5C Apr16 | 8.38 | 1.60 / 2.25 | 34% | 176 | 9.75 | +16.3% | 9.34 (11.4%) | R5, R6, R7 |
| EQX $9C Apr16 | 8.38 | 1.00 / 1.40 | 33% | 66 | 10.40 | +24.1% | 9.34 | R5, R6, R7 |
| EQX $10C Apr16 | 8.38 | 0.55 / 1.05 | 63% | 2,343 | 11.05 | +31.9% | 9.34 | R5, R6, R7 |
| NUVB $2.5C Jun17 | 3.795 | 1.30 / 2.00 | 42% | 59 | 4.50 | +18.6% | 4.17 (9.9%) | R5, R6, R7 |
| NUVB $5C Jun17 | 3.795 | 0.40 / 0.95 | 81% | 45 | 5.95 | +56.8% | 4.17 | R5, R6, R7 |

CAPR's Jun17 book is dollar-wide junk (IV 178-218% on the marks). NUVB only lists $2.5 / $5 / $7.5 in June.

## (2) GLNG dates, second pull

`get_earnings_results` still returns mislabeled rows: a "2024 Q3" row dated 2026-11-18 (`verified: true`, no actual), "2024 Q4" dated 2026-02-25, and no upcoming Q4 2026 row. GLNG is a 6-K filer, so R2 needs both the tool date and last year's date. Second unusable pull = **killed R2** (the Nov 17 rule: twice = R2 kill). Paper-size anyway ($39.09).

## (3) Ratio pass: median print move vs spring time value

Earnings-day close-to-close (AM: prior close to print-day close; PM: print-day close to next close), last 7 reported prints (MWH has 4), all `verified: true` dates from `get_earnings_results`.

| Ticker | Fri | Prints (oldest first) | Median | R6 cap | Max BE | Next (tool, f) | Expiry |
|---|---|---|---|---|---|---|---|
| SSRM | 21.59 | +2.6, +17.3, -10.2, +2.6, +15.5, +9.1, +7.6 | **9.1%** | 13.6% | 24.53 | Feb 16 PM | Mar19-if-LA |
| IAG | 14.435 | -5.6, -2.8, +8.8, +2.2, +13.4, +14.3, +7.2 | 7.2% | 10.8% | 15.99 | Feb 16 PM | Mar19 |
| OPRA | 12.89 | +6.4, -4.9, -3.4, +23.4, +5.3, -7.1, -8.0 | 6.4% | 9.6% | 14.13 | Feb 25 AM | Apr16 |
| KGS | 39.66 | +3.8, -0.5, -6.5, +4.0, +8.4, +5.3, +7.2 | 5.3% | 7.9% | 42.79 | Feb 24 PM | Apr16 |
| MWH | 24.71 | -5.8, +2.3, +8.8, -2.9 (4) | 4.3% | 6.5% | 26.32 | Feb 13 PM | Apr16 |
| KBR | 31.46 | +5.1, +2.7, -3.2, +3.0, -5.4, -4.3, -4.5 | 4.3% | 6.4% | 33.47 | Feb 25 AM | Mar19 |
| ERO | 21.485 | +11.3, -0.8, +3.9, -4.0, +5.6, +2.2, +4.4 | 4.0% | 6.0% | 22.78 | Mar 4 PM | Apr16 |
| AUPH | 14.70 | +1.5, +2.2, +8.4, -3.2, -6.8, +6.2, -3.3 | 3.3% | 4.9% | 15.42 | Feb 25 AM | Apr16 |
| CLDX | 27.39 | -6.1, -2.6, +7.5, -0.6, +2.0, +0.4, +5.7 | 2.6% | 3.9% | 28.46 | Feb 24 PM | Mar19-if-LA |
| IDYA | 25.56 | -13.3, -3.5, -2.8, +1.6, -0.3, +2.0, -1.0 | 2.0% | 3.0% | 26.33 | Feb 16 AM | Apr16 |
| OBDC | 10.61 | +1.2, -0.2, -5.3, -1.0, -3.1, +3.1, +0.5 | 1.2% | 1.8% | 10.80 | Feb 17 PM | Apr16 |
| DNLI | 18.425 | +2.5, -0.3, +4.2, -1.1, -0.5, +0.4, +7.8 | 1.1% | 1.7% | 18.74 | Feb 25 PM | Mar19-if-LA |

Near-ATM quotes on the top five by median (Friday close):

| Contract | Bid / Ask | OI | IV | Time value at mid (% of stock) | BE at ask | Needs | Cap | Ratio (median / TV%) | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| SSRM $22C Mar19 | 2.60 / 3.20 | 0 | 60% | 2.90 (13.4%) | 25.20 | +16.7% | 13.6% | **0.68** | R5, R6, R7 |
| OPRA $12C Apr16 | 1.70 / 2.55 | 0 | 49% | 1.235 (9.6%) | 14.55 | +12.9% | 9.6% | 0.67 | R5, R6, R7 (BE at mid 14.125 = max BE) |
| KBR $32.5C Mar19 | 2.25 / 2.80 | 1 | 39% | 2.53 (8.0%) | 35.30 | +12.2% | 6.4% | 0.54 | R5, R6, R7 |
| IAG $15C Mar19 | 1.70 / 2.25 | 43 | 65% | 1.975 (13.7%) | 17.25 | +19.5% | 10.8% | 0.53 | R5, R6, R7 |
| KGS $40C Apr16 | 5.00 / 6.80 | 12 | 58% | 5.90 (14.9%) | 46.80 | +18.0% | 7.9% | 0.36 | R5, R6, R7 |

## Verdicts

- **Killed (14):** CAPR, EQX, NUVB (R5 + R6 + R7), BRSL (R5 + R7; R6 by one cent on the $8C), GLNG (R2: second unusable date pull), SSRM, OPRA, KBR, IAG, KGS (R6 at the ask, plus R7 on OI 0-43; R5 everywhere), OBDC, IDYA, DNLI, CLDX (R6 structural: caps 1.7-3.9%, and no Mar/Apr strike carries that little time value).
- **R6 table done, book not quoted (3):** MWH (cap 6.5%), ERO (6.0%), AUPH (4.9%). Expected to die the same way. Low priority.
- **Tally:** 17 moved, 14 killed, 3 staged, 0 advanced, 0 buyable, 0 searches.

## The finding (adds to Nov 19's, not a rule change)

The ratio has a clean pass line. R6 lets breakeven sit at most 1.5x the median above the stock, and an at-the-money contract's breakeven sits about one time value above it, so **median / (time value as % of price) has to be at least 1/1.5 = 0.67**, and that's at the ask, not the mid. The best two tonight hit it only at the mid (SSRM 0.68, OPRA 0.67). Spreads push both over the line, and their OI is zero. So the ratio works as a sort key and a free pre-quote kill: anything under ~0.6 at mid is dead before R7 is even checked. Applied to the 12 tonight, it would have saved four of the five quote lookups.

**Watch notes (not entries):**
- **AVGO** fell **-12.3%** Friday ($346.65 -> $304.17, AH $310.92), far under the old $338.85-341.08 window. Q4 is **Wed Dec 9 PM, `verified: true`**. 53/3/0, low $398.47, stamp still Oct 27, so the floor gate is shut on staleness. A Jan15 paper book at ~$305 is worth one look in EVENING 2 or Saturday, but only if the stamp moves.
- NIO $2.45 (-7.9%), 16/7/1, low $3.7026, stamp Nov 18 00:55Z: gate shut. Keep Watching until Mon Nov 30 3:35pm.
- Paper GOOGL closed $265.68 (AH $269.59), low target $300 (stamp Nov 7) vs BE $285.95: R4 holds.

## GLOSSARY

- **R1 (range percentile):** (price - 52-week low) / (52-week high - 52-week low). Under 0.25 = calls candidate.
- **R2:** the print is proven to land before expiry: expiry 21+ days after the later of the tool date and last year's date, with the filing deadline 5+ trading days before expiry. 6-K filers need both dates.
- **R5:** one contract's ask x 100 must fit the conviction tier on reserve (3.5/5 = 10% = $0.716/share tonight).
- **R6:** the move to breakeven (strike + ask) can be no more than 1.5x the median earnings-day move over the last 4-8 prints.
- **R7:** the exact contract needs open interest >= 250 and a spread <= 25% of mid.
- **Median print move:** the middle value of the absolute earnings-day moves; sign ignored.
- **Max BE:** stock price x (1 + R6 cap). Any contract whose strike + ask sits above it fails R6.
- **Time value:** the part of an option's price above what it's worth if exercised now. Breakeven can never sit closer to the stock than this.
- **Ratio (median / TV%):** median print move divided by the near-ATM contract's time value as a percent of the stock price. Needs >= 0.67 at the ask to pass R6.
- **IV (implied volatility):** the yearly move the option price assumes. High IV = expensive time value.
- **Mar19-if-LA:** the March expiry works only if the company is a large accelerated filer (earlier 10-K deadline); otherwise the fallback expiry applies.
- **Staged:** dated R2 verdict and a listed expiry, waiting for its chain to be checked.
- **Floor gate / stamp:** Tab 6 needs the lowest Buy target to be from a dated, recent update; `updated_at` on the ratings record is the stamp.
