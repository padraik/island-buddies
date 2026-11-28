# Screening log: Fri Nov 27, EVENING 2 (8:00pm ET)

**Job:** EVENING 2 writes research docs for names past the chain stage. None exist (EVENING 1 ended with 0 survivors), so this session started EVENING 3's job: queue item 1 (re-run the Jan 15 - Mar 31 A/B scans, diff for never-worked names), then queue item 2 (the last 7 band D parks), then BBUC and the CHRW R1 re-check. Nothing held. R5 line: 10% x $715.96 / 100 = **$0.716/share** (3.5/5).

**Source:** Robinhood tools, run ~01:00-01:10 UTC Nov 28 on Friday's 1pm close (Fri daily bar not yet posted; Friday's last regular trade from `get_equity_quotes` used as the close). 0 web searches.

## 1. Re-run of the Jan 15 - Mar 31 A/B scans

| Scan | ID | Window | Rows Nov 24 | Rows now |
|---|---|---|---|---|
| Band A $1-8.19 | `b7b61d9f-7278-4bbb-92bd-c096eddf2ee3` | Jan 15 - Feb 12 | 60 | 53 |
| Band B $8.19-25 | `770b42be-6b18-4508-974c-6c2e135e1703` | Jan 15 - Feb 12 | 100 | 93 |
| Band A $1-8.19 | `01ce0035-28a6-49c0-aed8-0ee1b83da395` | Feb 13 - Mar 20 | 162 | 149 |
| Band B $8.19-25 | `fccfd39a-e704-451e-8e48-72719f90258a` | Feb 13 - Mar 20 | 196 | 184 |
| Bands A+B $1-25 | `a7226397-cbb5-4ff4-b12d-01f39cd0455a` | Mar 21 - Mar 31 | 42 | 43 |

522 rows diffed (whole-word) against every `week-*/research/*.md`, passes.md, paper_book.md and the queue. **2 never-worked names.** Same caveat as Nov 24: one- and two-letter tickers (F, KT, OI, DX, CX, BV, UA, CV, TE) can hide in the grep.

| Ticker | Name | Fri close | Next print (tool) | B/H/S | Low target | Verdict |
|---|---|---|---|---|---|---|
| PINE | Alpine Income Property Trust | 16.92 | Feb 5 (scanner) | 9/3/0 | 17.00 | **KILLED R4 proxy** (low $17.00 is 0.5% over the stock) |
| ALVO | Alvotech | 3.70 (-12.1% Fri) | Mar 17 PM (f); LY Mar 18 PM | 7/1/0 | 4.00 | R1 0.222, R3 pass, R4 proxy +8.1%. Median 5.6% (cap 8.4%). To the chain (below). |

## 2. Band D parks, the last 7 (paper size)

Moves from daily closes, last 6 prints (PM = print day to next day; AM = prior close to print day). R1 on daily closes Nov 28 2025 - Nov 27 2026.

| Ticker | Next print (f) | Moves | Median | R1 | B/H/S | Low | Verdict |
|---|---|---|---|---|---|---|---|
| NVT | Feb 5 AM | +14.6 / +9.6 / -1.1 / +11.2 / +6.2 / -8.8 | **9.2%** | 0.142 | 21/1/0 | 125 (Nov 4) | to the chain |
| WMS | Feb 4 AM | +17.2 / +8.8 / +6.1 / -1.2 / -0.8 / -14.9 | **7.45%** | 0.157 | 14/0/0 | 145 (no stamp) | to the chain |
| ENS | Feb 3 PM | +3.2 / +1.9 / -13.9 / +11.3 / +5.7 / +0.1 | 4.45% | 0.068 | 6/1/0 | 210 | **KILLED R6 structural** |
| PCAR | Jan 26 AM | +6.1 / +2.4 / -1.1 / -6.0 / +3.6 / -0.6 | 3.0% | 0.223 | 12/10/0 | 104 | **KILLED R6 structural** |
| PLD | Jan 20 AM | +1.4 / +6.3 / +0.3 / +1.7 / +4.6 / -2.7 | 2.2% | 0.163 | 15/3/0 | 136 | **KILLED R6 structural** |
| CBRE | Feb 11 AM | +7.8 / +0.3 / -8.8 / -2.7 / +0.5 / -2.5 | 2.6% | **0.365** | 13/1/0 | 155 | **KILLED R1** (and R6 structural) |
| BX | Jan 28 AM | +3.6 / -4.2 / -2.6 / -5.7 / +1.4 / +8.4 | 3.9% | **0.324** | 16/11/1 | 111 | **KILLED R1** (and R6 structural) |

## 3. Other queue items

| Ticker | Fri close | B/H/S | Low target | Verdict |
|---|---|---|---|---|
| BBUC | 28.86 | 5/2/1 | 28.00 | **KILLED R4 proxy** (low $28 is under the stock). Last band C park, off the queue. |
| CHRW | 147.00 | (EVENING 1) | | R1 re-check: 0.264 on Friday's close, same read as EVENING 1 (no new session since). Stays on the queue; needs a close under ~$145.80. |

## 4. Chains (Friday 12:59pm quotes; needs = BE at the ask vs the Friday close)

Expiry picked by R2. WMS: later of Feb 4 tool / LY Feb 5 + 21 = Feb 26 -> **Mar19**; fiscal Q3 10-Q deadline Feb 9, fine. NVT: later of Feb 5 / LY Feb 6 + 21 = Feb 27 -> Feb19 fails, **no Mar19 listed**, so **May21**; 10-K deadline Mar 1, fine. ALVO: later of Mar 17 / LY Mar 18 + 21 = Apr 8 -> Mar19 fails, no Apr listed, so **Jun17** (listed strikes only $2.5 / $5 / $7.5).

| Contract | Bid / Ask | OI | IV | BE at ask | Needs | Cap (1.5 x median) | Verdict |
|---|---|---|---|---|---|---|---|
| WMS $105C Mar19 | 19.20 / 22.00 | 0 | 37% | 127.00 | +4.8% | 11.2% | R4 (< $145), R6 pass; **R7 (OI 0)** |
| WMS $110C Mar19 | 15.60 / 18.50 | 0 | 37% | 128.50 | +6.0% | 11.2% | R4, R6 pass; **R7 (OI 0)** |
| WMS $115C Mar19 | 12.70 / 15.50 | 1 | 38% | 130.50 | +7.7% | 11.2% | R4, R6 pass; **R7 (OI 1)** |
| WMS $120C Mar19 | 10.00 / 12.70 | 1 | 37% | 132.70 | +9.5% | 11.2% | R4, R6 pass; **R7 (OI 1, spread 24%)** |
| WMS $125C Mar19 | 7.40 / 10.20 | 8 | 36% | 135.20 | +11.6% | 11.2% | R6, R7 |
| WMS $130C Mar19 | 5.60 / 8.50 | 4 | 37% | 138.50 | +14.3% | 11.2% | R6, R7 |
| NVT $100C May21 | 21.00 / 23.50 | 3 | 60% | 123.50 | +14.7% | 13.8% | **R6**, R7 |
| NVT $105C May21 | 18.40 / 20.90 | 0 | 59% | 125.90 | +16.9% | 13.8% | R6, R7 |
| NVT $110C May21 | 16.00 / 18.50 | 4 | 58% | 128.50 | +19.3% | 13.8% | R6, R7 |
| NVT $115C May21 | 14.00 / 16.50 | 100 | 58% | 131.50 | +22.1% | 13.8% | R6, R7 |
| ALVO $2.5C Jun17 | 1.45 / 6.30 | 0 | n/a | 8.80 | +138% | 8.4% | **R7 (OI 0, spread >100%)**, R6, R5 |
| ALVO $5C Jun17 | 0 / 4.90 | 0 | 21% | 9.90 | +168% | 8.4% | no market |

**WMS KILLED R7.** The cleanest R6 board of the night: 14 Buys, no Holds, no Sells, a $145 floor 19.6% over the stock, and four Mar19 strikes that need 4.8-9.5% against an 11.2% cap. Nobody trades them (OI 0-1). Paper size anyway ($1,850+ a contract). Goes on the weekly re-quote line with the RRX / TER group.
**NVT KILLED R6** at May21: R2 forces a six-month contract and the time value pushes the nearest passing BE past the cap.
**ALVO KILLED R7.** The only expiry that clears R2 (Jun17) has three strikes and no market. This was the one real-money-size name of the night; at $3.70 with a $4.00 floor the $2.5C would have needed an ask under $1.50 to pass R4.

## Tally

11 names moved: 2 never-worked from the A/B re-run (PINE R4 proxy, ALVO chain R7), 7 band D parks (ENS / PCAR / PLD R6 structural, CBRE / BX R1, WMS chain R7, NVT chain R6), BBUC R4 proxy, CHRW R1 re-check (unchanged). 0 advanced, 0 docs, 0 buyable, 0 searches.

**The finding:** the real-money universe added 2 never-worked names in four sessions, and both died. The band D parks are now finished. EVENING 3 needs fresh supply: a band C/D scan with the print window moved to Jan 15 - Mar 31, or Tier B of the latest sweep.

## GLOSSARY

- **R1-R7:** binder Tab 1 Iron Rules. R1 range percentile, R2 earnings before expiry, R3 ratings mix, R4 bear floor, R5 price cap on reserve, R6 reachability (needed move <= 1.5x median earnings move), R7 liquidity (OI >= 250, spread <= 25% of mid).
- **Park:** passed R3 and the R4 proxy; waits for the next check.
- **R4 proxy:** lowest analyst target vs the stock price, before any chain is pulled. If the low target is barely above the stock, no call's breakeven can clear it.
- **R6 structural:** the median move is so small that even a contract with almost no time value couldn't pass R6.
- **Median move:** the middle of the last 6 absolute one-day stock moves on earnings.
- **BE (breakeven):** strike + premium paid. The stock has to be above this at expiry for the call to make money.
- **OI (open interest):** contracts outstanding. Low OI means a thin market and a wide spread to get out.
- **IV (implied volatility):** the move the option market is pricing in, annualized.
- **(f):** the earnings date is the tool's estimate (`verified: false`), not company-announced.
- **LY:** last year's same-quarter report date.
- **Band A/B/C/D:** price bands for the scanner ($1-8.19 / $8.19-25 / $25-100 / $100+). A/B are real-money size; C/D are paper-book size.
