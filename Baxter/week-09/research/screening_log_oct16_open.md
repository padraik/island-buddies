# SCREENING LOG: Fri Oct 16, 9:35am ET (OPEN)

12 queue names quoted live (~13:35 UTC, opening book), Dec18 chains pulled for 5 (NRG, CRH, WYNN, TPB, VSEC), 3 web searches (COUR date, INSM floor, NRG floor), 1 price-path pull (NRG weekly bars). **4 killed (CRH, WYNN, TPB, VSEC), 1 advanced to the floor gate (NRG Dec18 $105C, paper).** Queue 13 -> 12 (9 live + 3 from behind the queue to date next).

Caution: these are 9:35 opening quotes, which run wide. The kills below hold at the mid as well, or fail on open interest, which the opening book doesn't change.

## Dec18 chain checks (new)

| Ticker | Contract | Direction | Stock | Bid / Ask | BE at ask | Needs | R6 cap | R7 (OI / spread) | Result |
|---|---|---|---|---|---|---|---|---|---|
| NRG | Dec18 $100C | CALLS | $102.81 | 10.00 / 11.50 | $111.50 | +8.45% | 13.42% | **206** / 14.0% | R7 (OI) |
| NRG | Dec18 $105C `6fa30201-0a25-46b0-91c9-ec10f7cb6620` | CALLS | $102.81 | 7.70 / 9.30 | $114.30 | **+11.18%** | 13.42% | 517 / 18.8% | **ADVANCE (paper), dated-floor gate** |
| NRG | Dec18 $110C | CALLS | $102.81 | 6.10 / 7.50 | $117.50 | +14.29% | 13.42% | 1,348 / 20.6% | R6 |
| CRH | Dec18 $80C | CALLS | $83.34 | 5.90 / 8.80 | $88.80 | +6.55% | 6.08% | **42** / 39.5% | R6 + R7 |
| CRH | Dec18 $82.5C | CALLS | $83.34 | 5.00 / 6.50 | $89.00 | +6.79% | 6.08% | **151** / 26.1% | R6 + R7 |
| CRH | Dec18 $85C | CALLS | $83.34 | 4.10 / 4.80 | $89.80 | +7.75% | 6.08% | **209** / 15.7% | R6 + R7 |
| WYNN | Dec18 $75C | CALLS | $76.81 | 6.00 / 7.10 | $82.10 | +6.89% | 4.88% | **107** / 16.8% | R6 + R7 |
| WYNN | Dec18 $77.5C | CALLS | $76.81 | 4.55 / 5.70 | $83.20 | +8.32% | 4.88% | **141** / 22.4% | R6 + R7 |
| WYNN | Dec18 $80C | CALLS | $76.81 | 3.60 / 4.60 | $84.60 | +10.14% | 4.88% | 1,433 / 24.4% | R6 |
| TPB | Dec18 $60C | CALLS | $60.31 (no print yet) | 4.90 / 8.70 | $68.70 | +13.9% | 18.9% | **4** / 55.9% | R7 |
| TPB | Dec18 $65C | CALLS | $60.31 | 2.45 / 5.90 | $70.90 | +17.6% | 18.9% | **3** / 82.6% | R7 |
| VSEC | Dec18 $160C / $165C / $170C | CALLS | $161.16 | 14.20 / 18.30 etc. | $178.30+ | +10.6%+ | 9.23% | **0** on all three | R6 + R7 |

**Kills:** CRH (R7 at every near-the-money strike; R6 at the ask too). WYNN (R6 at every strike; the median print is 3.25%, so no December strike can be reached). TPB (R7, OI 3-4). VSEC (R7, OI 0, as EVENING 3 expected).

## NRG dated floor (one web search + weekly bars)

Tool: 16/4/0, low $159, mean $189.81 (record updated Oct 3). Search: the latest target actions found are **Morgan Stanley $165 -> $162 (Aug 21)**, Scotiabank $226 -> $211 (Aug 5), and BNP Paribas $232 -> $221. Nothing from September or October.
Weekly bars: $134 (Jul 31) -> $118 (Aug 7, the print week) -> $113 (Aug 21, when MS cut) -> **$95.23 (Oct 2 low week, $93.36 intraday)** -> $107.97 (Oct 9) -> $102.81 now. So the stock fell another ~17% **after** the latest dated cut. Under Tab 6 a floor has to be published after the decline, and $159-162 wasn't. Same shape as RIOT. **Gate: a Buy target action dated after Sep 14 with the low above $114.30.** Q3 Nov 5 AM (f), LY Nov 6: a paper ramp sell would be Wed Nov 4 3:35pm. Kill if nothing by Mon Nov 2.

## Queue re-tests (opening book)

| Ticker | Contract | Stock | Bid / Ask | BE at ask | Needs | R6 cap | R7 (OI / spread) | Result |
|---|---|---|---|---|---|---|---|---|
| INSM | Nov20 $105C (paper) | $98.42 (-0.8%) | 4.70 / 5.70 | $110.70 | +12.48% | 17.1% | 5,117 / 19.2% | PARK, dated-floor gate (search found only a May Truist cut; no Oct action) |
| RIOT | Nov20 $13C (paper) | $14.96 (-3.5%) | 2.69 / 3.95 | $16.95 | +13.3% | 10.69% | 568 / 38.0% | PARK, floor gate; R6/R7 fail on the opening book (re-test on a settled quote) |
| PL | Jan15 $10C (paper) | $14.315 (-1.5%) | 4.50 / 5.10 | $15.10 | +5.5% | 45.75% | 4,139 / 12.5% | PARK, floor gate |
| PAAS | Jan15 $40C (paper) | $43.71 | n/a | n/a | n/a | BE <= $46.34 | n/a | PARK, R1 ($1.40 over the $42.31 line) |
| TTWO | Dec18 $190C (paper) | $210.41 (+0.5%) | 28.40 / 31.80 | $221.80 | +5.41% | 7.35% | 850 / 11.3% | PARK, Argus gate; WRAP re-vote today. Note: tool low is $270 (record Aug 7); the $192 came from a search |
| ALGM | Nov20 $35C (paper) | $31.685 (-2.1%) | 1.70 / 2.10 | $37.10 | **+17.1%** | 10.5% | 6,822 / 21.1% | PARK, R6; over the 15% kill line at the open, WRAP decides on the close |
| BTBT | Jan15 $1C (real) | $1.05 (-2.8%) | 0.20 / 0.27 | $1.27 | +21.0% | 8.23% | 3,290 / 29.8% | PARK, R6 + R7 |
| ONDS | Dec18 $8C (real) | $6.32 (-0.5%) | 0.30 / 0.39 | $8.39 | +32.8% | 20.89% | 38,086 / 26.1% | PARK, R6 |

Ratings re-pulled (free): COUR 8/4/0 low $6; INSM 24/1/0 low $165; RIOT 24/1/0 low $22; PL 8/4/0 low $17; NRG 16/4/0 low $159; TPB 6/0/0 low $90; VSEC 10/2/0 low $229; CRH 24/2/0 low $100; WYNN 25/0/0 low $102; TTWO 29/1/1 low $270. All unchanged.

## COUR date corroboration (one web search)

Searched "Coursera to announce third quarter 2026 financial results October 29". It returned only the Q1/Q2 8-K exhibits and the Q2 10-Q, plus one aggregator listing **Oct 26 PM**. That's the tool's old estimate, so this is probably an echo, not a source. No Coursera release found. The tool still says Oct 29 PM `verified: true`. The Wed Oct 21 fallback stays (it covers both dates).

## GLOSSARY
- **R1-R7**: Iron Rules, binder Tab 1. R1 range percentile, R2 earnings before expiry, R3 analyst consensus, R4 bear floor, R5 affordability, R6 reachability (needed move <= 1.5x median earnings move), R7 liquidity (OI >= 250, spread <= 25% of mid).
- **BE**: breakeven = strike + ask.
- **Dated floor**: binder Tab 6: a Rule 4 target counts only if it's within 60 days and published after the stock's decline.
- **Opening book**: the first minutes' quotes, which run wide. Spread kills at 9:35 get re-tested on a settled quote; OI kills don't.
- **(f)**: earnings date from the tool, `verified: false`.
- **Paper / real**: paper-book candidate vs. a contract the real fund could afford.
