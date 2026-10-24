# SCREENING LOG: Sat Oct 24, 2026, SATURDAY (9:00am ET)

*Market closed; every quote is Friday's 4:00pm close. Saturday's job: the full sweep across market-cap bands at prints Oct 28 - Dec 23, the chain stage on anything new, the carried queue (CWEN / STEP retests, TTWO, OUST, JFB, watch line), and a loaded plan for Monday. 20 names moved: 12 never-screened names from the sweep to the free screen, 5 of them to chains, 2 Jan15 retests, 2 carried retests on the next listed expiry, plus 6 free re-checks. 0 advanced. 0 web searches. No Discord messages.*

New saved scans (all: market cap >= $0.3B, stocks only, R1 < 0.25 by the scanner's expression, prints **Oct 28 - Dec 23**, columns add total call volume and market cap):
- `Baxter Oct24 SAT sweep all-cap Oct28-Dec23 prints` (`601b4513-0906-47d9-97d7-bb0433cb9ed9`): $1-10,000. Shows the top 200 by price ($49.61-$1,104.84).
- `Baxter Oct24 SAT sweep 1-49.6 Oct28-Dec23 prints` (`53b22af2-a717-4c0a-a544-5739baee05db`): 200 shown, $18.20-49.60.
- `Baxter Oct24 SAT sweep 1-18.19 Oct28-Dec23 prints` (`57ae12f7-ec19-47fc-b010-a908ae7c49c3`): 200 shown, $8.20-18.19.
- `Baxter Oct24 SAT sweep 1-8.19 Oct28-Dec23 prints` (`5ee16375-6b7a-457b-bd5b-32ecd37fe787`): 200 shown, $2.17-8.19.
- `Baxter Oct24 SAT sweep 1-2.16 Oct28-Dec23 prints` (`e6f7923f-8f3b-45f4-b008-2a9e26866f10`): 40 rows, complete.

The five bands cover $1 and up end to end (the only gaps are the $49.60-49.61 and $8.19-8.20 slivers). **839 bottom-quartile names. 827 were already in a week-09 screening log, a research doc, passes.md or the paper book. 12 were new.** (`total_items` on the price-split scans reads ~392-396 regardless of the price band, so it isn't a reliable count; the row lists are.)

## Held (fact check)

| Contract | Close quote | Stock | Earnings | Ratings / low vs BE | SEC since Oct 20 | Verdict |
|---|---|---|---|---|---|---|
| COUR $5C Nov20 | 0.45 / 0.60 (OI 3,257, IV 87%) | $5.085 (AH $5.08) | Thu Oct 29 PM `verified: true`, `actual: null` | 8/4/0, low $6.00 vs BE $5.65 | none | Nothing changed. Ramp sell Thu Oct 29 3:35pm. GTC $1.65 `confirmed`. |
| QUBT $7C Dec18 | 0.36 / 0.61 (OI 1,125) | $6.555 (AH $6.52) | Fri Nov 13 PM `verified: false` (LY Nov 14 PM), `actual: null` | 5/2/0, low $10 vs BE $7.54 | none | Nothing changed. Ramp sell Thu Nov 12 3:35pm. GTC $1.35 `confirmed`. |

Paper: PAAS 6/2/0 low $51 vs BE $43.90 (stock $40.125): holds. TMUS 27/4/0 low $169 vs BE $165.20 (stock $146.61, AH $146.96): holds; paper ramp sell **Tue Oct 27 3:35pm**.

## Free screen: R3 + R4 proxy (12 never-screened names)

| Ticker | Stock | Print | Ratings / low | Result |
|---|---|---|---|---|
| ASA | $48.63 | Oct 28 | none | **No coverage** |
| BELFA | $159.50 | Oct 28 | none | **No coverage** |
| ESE | $231.97 | Nov 19 | none | **No coverage** |
| AUR | $4.815 | Oct 28 | 8/6/0, low $3.59 | **R4 proxy** (low under the stock) |
| PCAR | $104.66 | Oct 28 | 10/12/1 | **R3** (Holds outnumber Buys) |
| MYRG | $254.62 | Oct 28 | 6/3/0, low $331 | Passes the screen; **parked on R7 proxy**: total call volume 6 Friday. No chain call spent. |
| SXI | $240.45 | Oct 30 | 6/1/0, low $310 | Passes the screen; **parked on R7 proxy**: total call volume 2. No chain call spent. |
| KLAC | $145.56 | Wed Oct 28 PM v | 21/10/0, low $180 | To chains |
| AEIS | $216.75 | Mon Nov 2 PM v | 14/1/0, low $360 | To chains |
| CAMT | $121.19 | Wed Nov 4 AM v (6-K filer; LY Nov 10) | 7/6/0, low $152 | To chains |
| SANM | $155.67 | Mon Nov 9 PM v | 4/4/0, low $210 | To chains |
| POWL | $150.84 | Tue Nov 17 PM unv. (LY Nov 18) | 3/3/0, low $235 | To chains |

**R1 from split-adjusted weekly bars** (rule since Oct 22, APH): every survivor got re-checked against adjusted 52-week ranges at the Friday close (no split artifacts found): AEIS 0.138, KLAC 0.192, MYRG 0.182, SXI 0.167, SANM 0.220, CAMT 0.236, POWL 0.247. All pass. Note: the adjusted weekly series stops at the week of Oct 12, so the Friday close was used as the price and the lows are the adjusted lows through Oct 16.

**What this cohort is:** seven AI-hardware / semi-cap / electrical names all down 20-25% in the last two weeks (AEIS $288.66 -> $216.75, KLAC $195.57 -> $145.56, SANM $217.49 -> $155.67, POWL $191.93 -> $150.84). Every Buy target on them likely predates the slide, so even a clean chain would have hit the Tab 6 dated-floor gate.

## R6: print medians (last 6 prints, close-to-close across the print)

| Ticker | Moves (%) | Median | R6 line (max BE = stock x (1 + 1.5 x median)) |
|---|---|---|---|
| KLAC | -3.75, +0.87, -1.69, -15.24, -3.63, -10.80 | 3.69% | $153.62 |
| AEIS | +11.19, +0.16, +15.77, +10.65, -10.70, +15.19 | 10.95% | $252.34 |
| POWL | -8.04, -3.56, -11.31, +16.34, +9.16, -3.80 | 8.60% | $170.30 |
| SANM | -2.13, +22.79, +16.56, -21.56, +14.56, -17.46 | 17.01% | $195.38 |
| CAMT | -0.85, -8.70, -6.65, +0.34, -15.83, +1.77 | 4.21% | $128.85 |

## Chain stage

R2 contract: KLAC Nov20 (print Oct 28, LY Oct 29 + 21 = Nov 19; 10-Q deadline Nov 9 is 9 trading days before expiry). The rest Dec18 (Nov 2 - 18 prints fail the Nov20 cushion).

| Ticker | Contract | Bid / ask | OI | Spread | BE at ask vs R6 line | Verdict |
|---|---|---|---|---|---|---|
| KLAC | Nov20 $145C | 9.50 / 11.90 | 14 | 22% | $156.90 vs $153.62 | **R6 + R7** (R6 structural: 3.7% median) |
| KLAC | Nov20 $150C | 7.10 / 9.50 | 138 | 29% | $159.50 vs $153.62 | **R6 + R7** |
| AEIS | Dec18 $220C | 21.80 / 23.80 | 21 | 9% | $243.80 vs $252.34 (passes) | **R7** |
| AEIS | Dec18 $230C | 17.40 / 20.00 | 6 | 14% | $250.00 vs $252.34 (passes) | **R7** |
| POWL | Dec18 $150C | 16.30 / 23.20 | 42 | 35% | $173.20 vs $170.30 | **R6 + R7** |
| POWL | Dec18 $160C | 11.60 / 17.80 | 14 | 42% | $177.80 vs $170.30 | **R6 + R7** |
| SANM | Dec18 $160C | 14.50 / 18.10 | 14 | 22% | $178.10 vs $195.38 (passes) | **R7** |
| SANM | Dec18 $170C | 10.10 / 13.70 | 0 | 30% | $183.70 vs $195.38 (passes) | **R7** |
| CAMT | Dec18 $120C | 13.10 / 16.10 | 0 | 21% | $136.10 vs $128.85 | **R6 + R7** |
| CAMT | Dec18 $125C | 10.60 / 13.60 | 0 | 25% | $138.60 vs $128.85 | **R6 + R7** |

Jan15 retests on the two R6 passers:

| Ticker | Contract | Bid / ask | OI | Verdict |
|---|---|---|---|---|
| AEIS | Jan15 $220C | 24.50 / 28.00 | 0 | **R7**. Dead this quarter. |
| SANM | Jan15 $160C | 17.60 / 20.40 | 11 | **R7**. Dead this quarter. |

None of these were ever real-money candidates (the cheapest ask is $7.10 vs the $0.622 line). They were paper-book tests, and the paper book uses R7 too.

## Carried queue

| Ticker | Check | Result | Verdict |
|---|---|---|---|
| CWEN | Jan15 retest | **No Jan15 expiry.** Chain lists Nov20, Dec18, Feb19, May21. Feb19 $30C 2.70 / 3.40, OI 126 (spread 23%); Feb19 $35C 0.65 / 1.10, OI 255 (spread 51%). Stock $31.12, 12/1/0 low $37. | **R7** on every listed expiry. Dead this quarter. |
| STEP | Jan15 retest | **No Jan15 expiry.** Chain lists Nov20, Dec18, Mar19, Jun17. Mar19 $45C 2.85 / 6.40, OI 17. Stock $42.065. | **R7**. Dead this quarter. |
| TTWO | free re-check | $203.69 (AH $204.98), 29/1/1, low $270, stamp still **Aug 7** | Parked on R4 dating, unchanged. |
| OUST | R1 re-entry line ~$28.25 | $29.695 (AH $29.60), 6/1/0 low $52 | Over the line. Unchanged. |
| JFB | quote | no quote returned. passes.md already moved it to **Stop Watching on Oct 19** (`inactive_instruments`). The queue carrying it was a stale line. | Off the queue. |
| ONDS / BTBT / CLSK | watch lines | $6.20 (needs >= ~$6.90) / $0.8486 (>= ~$1.10) / $7.87 (> ~$9.20) | All under. Unchanged. |

## Summary

20 names moved, 0 advanced, 0 searches. Killed: ASA, BELFA, ESE (no coverage), AUR (R4 proxy), PCAR (R3), KLAC, POWL, CAMT (R6 + R7), AEIS, SANM (R7, Jan15 too), CWEN, STEP (R7 on every listed expiry). Parked: MYRG, SXI (R7 proxy, call volume 6 / 2). JFB removed (already Stop Watching).

**Finding:** the bottom quartile at prints Oct 28 - Dec 23 is fished out. 827 of 839 names were already through this week's funnel, and the 12 new ones were mostly a fresh AI-hardware slide, whose chains are as thin as everything else outside miners, crypto and mega-caps. New names now only come from stocks falling **into** the bottom quartile day by day. So the cheapest refill next week is re-running these five saved scans and diffing against the logs, not building new ones.

## GLOSSARY

- **R1-R7:** the Iron Rules, binder Tab 1. R1 range percentile (bottom 25%), R2 earnings before expiry with the 21-day cushion, R3 Buy consensus, R4 lowest Buy target above breakeven, R5 price vs the conviction-tier cap, R6 required move <= 1.5x the median print reaction, R7 OI >= 250 and spread <= 25% of mid.
- **R4 proxy:** the free screen's version of R4, comparing the lowest Buy target to the stock price before any chain is pulled.
- **R7 proxy:** total call volume on the whole chain so small (single digits) that no single contract can have usable open interest; parked without spending a chain call.
- **Split-adjusted R1:** the scanner's 52-week range uses raw weekly candles, so a stock split fakes a 52-week low. R1 is re-checked on split-adjusted bars before the chain stage.
- **Tab 6 dated-floor rule:** an analyst floor only counts if the target was set after the decline and within 60 days.
- **Paper book:** liquid larger names traded on paper (every Iron Rule except R5) while the real fund is too small to afford them.
- **Print median:** the median absolute close-to-close move across a company's last six earnings reports.
- **6-K filer:** a foreign private issuer; no 10-Q deadline, so R2 needs both the tool date and last year's date.
