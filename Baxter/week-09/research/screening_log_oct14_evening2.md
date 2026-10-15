# Screening log: Wed Oct 14, 8:00pm ET (EVENING 2)

**Source:** EVENING 1 left no new name past the chain stage (TTWO's doc was already written and parked on R4), so this session took EVENING 3's job early and refilled the queue from a new saved scan, `Baxter Oct14 E2 25-110 Oct20-Dec18 prints` (`4bc59b84-cc60-4619-870c-359c2daae902`): market cap $300M+, earnings Oct 20 - Dec 18, last $25-110, 52-week range pct < 0.25. 336 matches, split into two price bands to stay under the 200-row cap ($40.53-110: 200 rows; $25-40.60: 137 rows). Diffed against every week-09 log, `paper_book.md`, `passes.md` and the queue: **313 already screened, 23 new.** Data pulled 00:00-00:20 UTC Oct 15, market closed; option quotes are the 3:59pm Oct 14 closes. Reserve $676.28, 3.5/5 line $0.676. Searches: 2 web searches + 2 page fetches (1 TTWO search + 1 failed TTWO fetch, 1 PAAS search + 1 PAAS fetch).

**Moved this session: 24** (23 new + the TTWO R4 re-check). Killed 22. Advanced 1 (PAAS, doc written). Parked 1 (TTWO, unchanged). Paper entries: 0 (PAAS waits on R1 at the OPEN).

## Part 1: free ratings screen (23 new)

| Ticker | Last | Range pct | Print (scanner) | Ratings (B/H/S), low | Direction | Result |
|---|---|---|---|---|---|---|
| WH | $72.59 | 0.244 | Oct 21 | 17/3/0, $80 | CALLS | advance to R2 |
| BAH | $71.87 | 0.249 | Oct 23 | 4/9/3, $63 | CALLS | **KILLED, R3** (3 Sells) |
| BOH | $65.80 | 0.239 | Oct 26 | 1/5/2, $75 | CALLS | **KILLED, R3** |
| AMKR | $43.90 | 0.216 | Oct 26 | 9/7/0, $65 | CALLS | advance to R2 |
| CCS | $53.94 | 0.232 | Oct 28 | none | | **KILLED, no coverage** |
| RM | $33.38 | 0.242 | Oct 28 | none | | **KILLED, no coverage** |
| CWST | $82.16 | 0.239 | Oct 30 | 10/2/1, $91 | CALLS | advance to R2 |
| VOYG | $25.24 | 0.224 | Nov 3 | 8/0/2, $21 | CALLS | **KILLED, R3** (2 Sells) |
| PAAS | $42.10 | 0.244 | Nov 4 | 7/2/0, $51 | CALLS | advance to R2 |
| XRN | $31.29 | 0.233 | Nov 4 | 4/6/0, $37 | CALLS | **KILLED, R3** (Holds > Buys) |
| BCO | $102.05 | 0.243 | Nov 5 | none | | **KILLED, no coverage** |
| AKAM | $90.51 | 0.208 | Nov 5 | 18/8/1, $93 | CALLS | **KILLED, R4 proxy** (low $93 is 2.7% over the stock; no call's BE fits under it) |
| PSIX | $45.54 | 0.249 | Nov 5 | none | | **KILLED, no coverage** |
| POWI | $44.78 | 0.231 | Nov 5 | 5/1/0, $72 | CALLS | advance to R2 |
| ECHO | $86.01 | 0.248 | Nov 6 | 7/0/0, $103 | CALLS | advance to R2 |
| INOD | $52.86 | 0.205 | Nov 6 | none | | **KILLED, no coverage** |
| CLDX | $27.84 | 0.249 | Nov 10 | 14/1/0, $28 | CALLS | **KILLED, R4 proxy** (low $28 vs stock $27.84) |
| CWCO | $29.21 | 0.167 | Nov 11 | none | | **KILLED, no coverage** |
| FUTU | $108.35 | 0.228 | Nov 18 | 19/2/0, $121.93 | CALLS | advance to R2 |
| CLFD | $30.00 | 0.215 | Nov 25 | none | | **KILLED, no coverage** |
| BMA | $63.79 | 0.242 | Nov 26 | 7/1/0, $85 | CALLS | advance to R2 |
| FPS | $32.42 | 0.162 | Nov 30 | 10/2/0, $44 | CALLS | advance to R2 |
| PLAB | $28.36 | 0.231 | Dec 10 | none | | **KILLED, no coverage** |

No top-quartile names in this scan by construction (calls-side only). Puts stay off (hard limit 3).

## Part 2: R2 (earnings tool), R6 (six prints), chain (R6 + R7)

R6 = median absolute reaction over the last six prints (PM: print-day close to next close; AM: prior close to print-day close), cap = 1.5x. Stock = Oct 14 official close.

| Ticker | Tool date / LY | R2 contract | Six reactions (%) | Median / cap | Best strike checked (close bid / ask) | Needs | OI / spread | Result |
|---|---|---|---|---|---|---|---|---|
| WH | Oct 21 PM (v) / Oct 22 | Nov20 | +0.07, +3.12, -5.46, +5.57, -3.22, -2.91 | 3.17 / **4.75** | $70C 4.50 / 5.30 (BE $75.30); $65C 8.10 / 10.20 (BE $75.20) | +3.7% / +3.6% | **34** / 16% ; **0** / 23% | **KILLED, R7** (R6 passes; OI 0-34; ramp sell would be Tue Oct 20 anyway) |
| AMKR | Oct 26 PM (v) / Oct 27 | Nov20 | -2.63, +18.13, -3.07, +1.79, -5.63, -24.74 | 4.35 / **6.52** | $42C 5.50 / 6.30 (BE $48.30) at $44.82 | +7.8% (best) | 0-22 | **KILLED, R6 + R7** |
| CWST | Nov 9 PM (v) / Oct 30 | Dec18 | -0.49, -5.29, +6.92, -5.75, +9.56, -1.16 | 5.52 / **8.28** | $75C 9.20 / 10.60 (BE $85.60) at $81.85; $80C 4.60 / 7.70 | +4.6%; +7.1% | **2** / 14%; 2 / 50% | **KILLED, R7** (R6 passes; OI 2-11 across strikes) |
| PAAS | Nov 4 PM (v) / Nov 12 | **Jan15** (no Dec18; Nov27 is 15 days past LY) | +3.99, +7.12, +1.77, +5.52, +12.02, -9.70 | 6.32 / **9.48** | **$40C 4.80 / 5.30 (BE $45.30)** at $42.33 | **+7.02%** | **5,369 / 9.9%** | **ADVANCE: doc written.** R1 0.251 at the close (ceiling 0.25): entry waits for a live price <= $42.31 at OPEN. |
| POWI | Nov 4 AM (f) / Nov 5 | Dec18 | -6.20, -9.18, +1.62, +0.30, +2.02, -4.79 | 3.41 / **5.11** | $40C 5.70 / 9.80 (BE $49.80) at $44.78 | +11.2% | 1 | **KILLED, R6** (and R7) |
| ECHO | Nov 5 AM (f) / Nov 6 | Dec18 | +1.43, -17.37, -2.31, +2.73, +1.57, +1.83 | 2.07 / **3.11** | $80C 10.70 / 13.10 (BE $93.10) at $87.86 | +6.0% | 921 / 20% | **KILLED, R6** |
| FUTU | Nov 17 AM (f) / Nov 18 | Jan15 (no Dec18) | -0.32, +6.02, -0.49, -6.31, -4.82, +3.03 | 3.92 / **5.89** | $100.5C 12.75 / 18.90 (BE $119.40) at $109.45 | +9.1% | 213 / 39% | **KILLED, R6** (and R7) |
| BMA | Nov 25 PM (f) / Nov 26 | Jan15 (chain: Nov20, Jan15 only) | -5.66, +3.59, +4.34, -8.29, +2.98, -3.12 | 3.96 / **5.95** | $55C 9.70 / 14.00 (BE $69.00) at $63.79 | +8.2% | 5 / 36% | **KILLED, R6** (and R7) |
| FPS | tool: last print Sep 15 (v), next **Feb 6 2027 (f)**; scanner says Nov 30 | n/a | | | | | | **KILLED, R2** (the tool shows no print before February, and its quarter labels are scrambled; nothing provable inside an expiry) |

## Part 3: TTWO R4 re-check (queue #1)

- Tool tonight: 29/1/1, low **$270**, stamp still Aug 7.
- One search: "Argus has a BUY rating... target price of **$284**", undated; aggregate low $170 (likely the one Sell). The **Oct 7 $192** line from EVENING 1 did not reappear, and nothing confirmed or denied it.
- Benzinga analyst-ratings page: HTTP 403.
- **Still PARKED on R4.** The $284 Buy is probably the older Argus note (EVENING 1 had seen "Buy, $284 at some point"). Next: MarketBeat TTWO price-target page at OPEN/MIDDAY, or a local session with a browser.

## Real-money read

Nothing in tonight's 23 is close to the $0.676 line: the cheapest liquid contract that passed R6 (PAAS $40C) is $5.30. The real-money pipeline is still only BTBT and ONDS, both R6-parked.

## GLOSSARY
- **R1-R7**: Iron Rules, binder Tab 1. R1 range percentile, R2 earnings before expiry, R3 analyst consensus, R4 bear floor (lowest Buy target above breakeven), R5 affordability, R6 reachability (needed move <= 1.5x median earnings move), R7 liquidity (OI >= 250, spread <= 25% of mid).
- **R4 proxy**: at screening, the tool's lowest target at or below the current stock price means no near-the-money call can pass R4.
- **BE**: breakeven = strike + ask.
- **OI**: open interest, contracts outstanding; updates once a day.
- **(v) / (f)**: earnings date company-verified / not verified in `get_earnings_results`.
- **LY**: last year's same-quarter report date.
- **Paper / real**: paper-book candidate vs. a contract the real fund could afford.
- **Park**: stays on the queue, re-tested later; not killed.
- **Price band split**: the scanner returns at most 200 rows, so one scan is run twice over adjacent price ranges.
- **EVENING 2**: the 8pm ET research session; no orders.
