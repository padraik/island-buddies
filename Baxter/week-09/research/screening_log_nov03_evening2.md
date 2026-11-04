# Screening log: Tue Nov 3, EVENING 2 (8:00pm ET)

**Source:** EVENING 1 left no name past the chain stage, so there was no doc to write; this session started EVENING 3's refill. Three live scan previews with the print window moved forward to **Nov 10 - Mar 12** and R1 < 0.25 (market cap $300M+): under $8.45 (call volume >= 30, 100 rows), $8.45-25 (call volume >= 100, 70 rows), $25+ (call volume >= 300, 86 rows). A slide-in preview (R1 0.25-0.32, under $8.45, call volume >= 30, 6 rows). Every row was diffed against the week-09 logs. Then the watch names were re-quoted, and ONDS and RCAT were re-chained on Dec18.
**Reserve / lines:** spendable $539.11 -> R5 line at 3.5/5 = **$0.539**.
**Data:** Tuesday closing option quotes (stamped 20:59 UTC), official closes and after-hours quotes, analyst counts, earnings dates, daily closes May 2025 - Aug 2026 for the ONDS and RCAT print reactions. All pulled live this run. 0 web searches.

## Scan diff

- **Under $8.45 (100 rows):** 98 already in this week's logs. Never logged: **ABUS, UROY.**
- **$8.45-25 (70 rows):** 69 already logged. Never logged: **HMY.** Short tickers grep-checked by hand: SA, TV, QS and OI (O-I Glass) had no verdict on file, so they were rated too.
- **$25+ (86 rows):** 84 already logged. Never logged: **LOGI, INTC.**
- **Finding:** the bottom quartile with prints through Mar 12 is fished out at every price band. 9 names out of 256 rows were new, and none survived the free screen.

## Free screen

| Ticker | Stock | R1 | Print | R3 (B/H/S) / low | Result |
|---|---|---|---|---|---|
| ABUS | 3.885 | 0.197 | Nov 13 | no coverage | **KILLED, R3** (no coverage) |
| UROY | 3.215 | 0.221 | Dec 11 | no coverage | **KILLED, R3** (no coverage) |
| SA | 23.50 | 0.173 | Nov 12 | no coverage | **KILLED, R3** (no coverage) |
| TV | 2.17 | 0.070 | Feb 26 | 3/6/0, $2.20 | **KILLED, R3** (Holds outnumber Buys) |
| QS | 4.11 | 0.022 | Feb 11 | 0/6/2 | **KILLED, R3** |
| OI | 5.13 | 0.011 | Feb 10 | 3/4/1, $5 (stamp Nov 2025) | **KILLED, R3** (Holds > Buys); R4 proxy too |
| HMY | 15.24 | 0.170 | Mar 11 (scanner) | 7/3/0, $19.19 | **KILLED, R2.** 6-K filer (semi-annual); `get_earnings_results` returns nothing, so neither the tool date nor last year's date exists, and 6-K filers need both. |
| LOGI | 91.48 | 0.176 | Jan 27 | 7/8/5 | **KILLED, R3** (5 Sells) |
| INTC | 59.79 | 0.246 | Jan 22 | 17/33/1 | **KILLED, R3** (Holds outnumber Buys) |

## Slide-in preview (R1 0.25-0.32, under $8.45): 6 rows, none passes R1

| Ticker | Stock | R1 | Print | R3 / low | Result |
|---|---|---|---|---|---|
| AVR | 5.60 | 0.298 | Mon Nov 16 PM (f) / LY Nov 12 | 4/2/0, $9.19 | **Watch.** Out on R1 tonight. Never logged before. Dec18 would pass R2 on dates. Only six prints on file; no chain pulled. |
| ANGX | 3.47 | 0.303 | **Tue Nov 10 PM `verified: true`** | 6/0/0, $6 | **Out, R1 + R2 timing.** Even if it slid in Wednesday, the ramp sell would be Tue Nov 10 3:35pm. Back next quarter (Mar 11 (f)). |
| LYG | 4.98 | 0.256 | Jan 29 | 14/6/1, $4.92 | **KILLED, R4 proxy** (low $4.92 under the stock). |
| TRTX | 6.78 | 0.315 | Feb 17 | 5/0/1, $8 | **Out, R1.** mREIT; NLY and DX died on structural R6, so expect the same here. |
| SVRA | 4.78 | 0.293 | Nov 12 | 9/0/0, $9 | **Stays dead** (R6 Oct 23: 3.04% median). |
| GALT | 3.35 | 0.260 | Nov 13 | no coverage | **Stays dead** (no coverage). |

## Chain re-tests (real-money band)

R6 cap = 1.5 x median absolute earnings reaction (AM prints: prior close to print-day close; PM prints: print-day close to next-day close).

| Ticker | Stock (Tue close) | R1 | Print / LY | R3 / low | Prints (R6) | Cap | Contracts (Dec18) | Bid / Ask | OI | BE / needs | Result |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ONDS | 5.79 | 0.079 | **Thu Nov 12 AM `verified: true`** (was `false`) / Nov 13 | 11/0/0, $13 | -2.19, +25.07, +19.06, +8.35, +26.52, -8.80; median 13.93% | 20.89% | $5C / $6C / $7C / $8C | 1.10 / 1.21; 0.65 / 0.77; 0.35 / 0.41; 0.21 / 0.23 | 2,827 / 4,519 / 10,044 / 46,041 | $6.21 +7.3%; $6.77 +16.9%; $7.41 +28.0%; $8.23 +42.1% | **Stays on watch.** $5C and $6C fail **R5** (1.21, 0.77 vs $0.539). $7C passes R5 and R7 but fails **R6** (+28.0% vs 20.89%). $8C fails R6. Revive math below. |
| RCAT | 4.46 | 0.021 | **Mon Nov 16 PM `verified: true`** / Nov 13 | 7/1/0, $6 | -2.41, -10.25, -7.49, -10.97, +0.10, +6.23; median 6.86% | 10.29% | $4C / $5C / $6C | 0.62 / 1.10; 0.35 / 0.43; 0.17 / 0.23 | 70 / 1,010 / 598 | $5.10 +14.3%; $5.43 +21.7%; $6.23 +39.7% | **KILLED, R6** (and R5 + R7 on the $4C). Four of its last six prints fell. Off the watch list this quarter. |

**ONDS revive math (delta-adjusted, ignores IV changes):**
- $6C: R5 needs the ask down 0.23, so the stock under ~$5.36. At that price R6 allows at most ~$0.47, so the stock has to be under ~$5.45 and the ask under that too. Those two conditions can't both hold, so there's **no window on the $6C**.
- $7C: R5 (ask <= $0.539) holds up to about $6.16. R6 needs about $6.27 or higher. So there's **no window tonight**. A week of theta (~$0.008/day) could open a sliver around **$6.20-6.30 by Mon Nov 9**.
- Either way the hold would be one to three days (ramp sell Wed Nov 11 3:35pm). Not worth a doc unless ONDS closes in that band. If it does, an evening session writes the addendum to `research_ONDS.md` for the $7C.

## Watch re-quotes (Tue close)

CLSK $8.15 (16/0/0, low $11.50; print Nov 25), BTBT $0.847 (6/0/0, low $3.50), NIO $3.19 (16/7/1, tool low $3.7091, stamp Sep 1: gate holds), PL $13.51 (8/5/0, low $17: gate holds; one search at EVENING 1 tonight), CRDO $150.91 (R1 still over its ~$142 line), SANM $164.49, WGS $68.64 (both print Nov 9, paper-size, still above R1).

## Tally

18 names moved to a verdict: 9 killed at the free screen (ABUS, UROY, SA, TV, QS, OI, LOGI, INTC on R3; HMY on R2), 1 killed on R4 proxy (LYG), 1 killed at the chain (RCAT, R6), 2 out on R1 (ANGX also on R2 timing, TRTX), 2 kept dead (SVRA, GALT), ONDS re-chained and kept on watch, AVR added to watch. **0 advanced.**

## GLOSSARY
- **R1-R7**: binder Tab 1 Iron Rules (calls). R1 range percentile, R2 earnings before expiry, R3 analyst consensus, R4 bear floor (lowest target above breakeven), R5 price cap on reserve, R6 reachability (needed move <= 1.5x median earnings move), R7 liquidity (OI >= 250, spread <= 25% of mid).
- **BE**: breakeven at expiry = strike + ask.
- **OI**: open interest, contracts outstanding.
- **(f)**: earnings date estimated from cadence, not announced.
- **LY**: last year's same-quarter report date.
- **6-K filer**: a foreign company that reports through 6-K forms rather than 10-Qs; Rule 2 needs both the tool date and last year's date for these.
- **R4 proxy**: at the free stage, a tool low target at or under the stock price means no strike can pass R4.
- **Floor gate**: R4 passes on the numbers, but no Buy target is dated after the stock's decline (binder Tab 6), so no entry until one is found.
- **Slide-in**: names sitting just above the R1 line that could slide into the bottom quartile on a down day.
- **R2 timing**: the print is too close (or already out) to buy, hold through the ramp, and sell before it.
- **Theta**: the daily time decay in an option's price.
- **Delta-adjusted**: estimating how far an option's price moves for a $1 move in the stock, using its delta.
- **Fished out**: every name in the scan has already been screened this week.
