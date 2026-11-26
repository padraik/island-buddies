# Screening log: Wed Nov 25, EVENING 2 (8:00pm ET)

**Job:** queue item 1 (write the NOW paper doc and log the paper entry), then, with that done early, queue item 2 (band C parks, median-first). Nothing held. R5 line: 10% x $715.96 / 100 = **$0.716/share** (3.5/5), so everything below is paper-book size.

**Source:** Robinhood tools, run ~01:00-01:30 UTC Nov 26 on Wednesday's close (market closed Thu Nov 26 for Thanksgiving). 1 web search (NOW's $100 owner).

## 1. NOW: doc written, paper entry logged

Doc: `week-09/research/research_NOW_paper.md`. **NOW $70C Mar19 entered on paper at the $27.40 closing ask** (25.90 / 27.40, OI 376, spread 5.6%). Stock $92.16. R1 0.101, R2 Q4 Jan 27 PM (f) / LY Jan 28, 10-K Mar 1; R3 45/4/1; R4 tool low $100 vs BE $97.40; R6 +5.69% vs 14.91% (median 9.94%, 7 prints); R7 pass. Five-Baxter vote 3-2.

The one search: the tool's $100 low is **UBS, downgraded Buy -> Neutral, $170 -> $100** (TIKR summary). It's a Hold target, so the lowest Buy is at or above $100. Same summary: Needham $155 -> $115, KeyBanc $115 -> $85 (under the tool's low; rating unconfirmed, probably the one Sell).

| Contract | Bid / Ask | Spread | OI | BE at ask | R4 (low $100) | Verdict |
|---|---|---|---|---|---|---|
| $70C Mar19 `deca0cea` | 25.90 / 27.40 | 5.6% | 376 | $97.40 (+5.69%) | +$2.60 | **PAPER ENTRY** |
| $75C Mar19 `16d51634` | 22.30 / 23.70 | 6.1% | 251 | $98.70 (+7.10%) | +$1.30 | passes, less room |
| $80C Mar19 `cf99017d` | 18.95 / 20.25 | 6.6% | 363 | $100.25 | -$0.25 | R4 fail |

## 2. Band C parks, median-first (18 names)

Moves from daily closes (Oct 2025 - Nov 24 2026; PM = print day to next day, AM = prior close to print day), the last 5 prints (4 where the oldest fell before the pull). R1 = closing-range percentile over the last 52 weeks, on the Nov 24 close.

| Ticker | Next print (f) | Moves (oldest first) | Median | R1 | Verdict |
|---|---|---|---|---|---|
| BFAM | Feb 11 PM | -18.3 / -18.7 / -4.4 / -17.9 | **18.09%** | 0.048 | to the chain -> **KILLED R7** |
| ZWS | Feb 2 PM | +4.2 / +10.0 / +9.5 / +4.5 / -11.5 | **9.47%** | 0.227 | to the chain -> **KILLED R4 structural** |
| SCI | Feb 10 PM | +4.6 / -6.7 / -6.2 / -0.5 / -8.7 | 6.20% | 0.133 | **KILLED R6 structural** |
| STEP | Feb 4 PM | -1.8 / +5.5 / +5.3 / -7.8 / +10.8 | 5.51% | 0.190 | **KILLED R6 structural** |
| LTM | Feb 2 PM | -0.1 / -5.3 / +12.1 / +3.7 / +8.4 | 5.31% | 0.159 | **KILLED R6 structural** |
| STC | Feb 3 PM | +2.9 / +3.9 / -7.8 / -6.3 | 5.10% | 0.142 | **KILLED R6 structural** |
| TCBX | Jan 20 PM | +5.2 / -4.7 / +5.6 / -1.9 | 4.94% | 0.131 | **KILLED R6 structural** |
| UNM | Feb 2 PM (verified) | +7.2 / -1.5 / +4.5 / -4.9 / -17.8 | 4.89% | 0.367 | **MID-OUT (R1)** |
| IP | Jan 28 AM | -6.0 / -9.4 / +1.2 / +3.3 | 4.65% | 0.081 | **KILLED R6 structural** |
| RRR | Feb 9 PM | -2.9 / -3.8 / -5.1 / -5.3 | 4.44% | 0.054 | **KILLED R6 structural** |
| CIGI | Feb 12 AM | -2.3 / -4.1 / -5.6 / -1.8 / -4.5 | 4.09% | 0.109 | **KILLED R6 structural** |
| NTES | Feb 10 AM | +0.4 / -4.1 / -2.1 / -5.9 / -11.4 | 4.06% | 0.092 | **KILLED R6 structural** |
| HCC | Feb 11 PM | +23.1 / +0.2 / -4.1 / +6.3 / -0.2 | 4.06% | 0.107 | **KILLED R6 structural** |
| GHM | Feb 5 AM | +0.4 / +12.9 / -11.0 / +0.5 / +3.7 | 3.71% | 0.277 | **MID-OUT (R1)** |
| FBK | Jan 20 PM | -1.4 / -2.3 / +3.2 / -4.2 | 2.77% | 0.171 | **KILLED R6 structural** |
| FR | Feb 3 PM | +2.2 / -0.8 / -2.0 / -6.9 | 2.14% | 0.133 | **KILLED R6 structural** |
| BG | Feb 3 AM | +1.8 / +0.3 / -0.0 / -8.2 / -4.7 | 1.78% | 0.000 | **KILLED R6 structural** |
| TEVA | Jan 27 AM | 0.0 / 0.0 / 0.0 / 0.0 / +3.0 | n/a | 0.762 | **OUT (R1, top quartile; puts are off)** |

**BFAM (5/5/1, low $57, no stamp in the tool):** Mar19 (R2: LY Feb 12 + 21 = Mar 5, 10-K Mar 1) calls at the close: $45C 9.50 / 13.00 (BE $58.00 at the ask, $1.00 over the $57 low), $50C 6.00 / 9.90 (BE $59.90), $55C 3.50 / 7.50 (BE $62.50). **Every strike OI 0**, spreads 31-73% of mid. Dead on R7, and on R4 at the ask as well (the $56.25 BE the quote shows is at the mark). Stock $52.91.

**ZWS (6/6/0, low $47):** stock $46.13, so the floor is $0.87 over the price. Expiries Dec18, Jan15, Feb19, May21: no Mar19, Feb19 fails R2 (LY Feb 3 + 21 = Feb 24), so May21 is forced, and no May21 strike's BE can sit under $47 with five months of time value on a 9.5% mover. R4 structural.

**TEVA:** the reaction column is four flat zeros, which looks like a data gap in the bars, not real flat prints. It doesn't matter: R1 at 0.762 is top quartile, which is the puts side, and puts are closed.

**Two coincidences checked live:** STEP and LTM both showed $46.52 in the bars (quotes: STEP $46.52, LTM $46.43 on Nov 24); UNM and HCC both showed $80.16 (quotes confirm both $80.16 Nov 24). Real, not a data error.

## Totals

19 names moved (NOW to doc + paper entry; 18 parks). 1 advanced (NOW, paper), 0 buyable for real money. Kills: 13 R6 structural, 3 R1, 1 R7 (BFAM), 1 R4 structural (ZWS).

Band C parks left: BBUC (thin). Stale stamps skipped: SW, PKX, CCJ, BDC. Band D parks are in the Nov 21 log.

## GLOSSARY

- **R1-R7:** the Iron Rules, binder Tab 1. R1 range (bottom 25%), R2 earnings before expiry, R3 analyst consensus, R4 lowest Buy target above breakeven, R5 price cap on reserve, R6 move to breakeven no more than 1.5x the median earnings move, R7 liquidity (OI >= 250, spread <= 25% of mid).
- **Median print / median move:** the middle of the absolute one-day stock moves on recent earnings reports.
- **R6 structural:** the median is so small that no affordable strike could fit inside 1.5x of it, so the name dies before any chain check.
- **R4 structural:** the lowest target is so close to the stock that no listed contract's breakeven can sit under it.
- **MID-OUT:** the stock sits in the middle of its 52-week range (25-74%), so it isn't a calls or puts candidate.
- **BE (breakeven):** strike + premium paid. At the ask = using the price you'd actually pay.
- **OI (open interest):** contracts currently outstanding on that strike. Low OI means a thin market.
- **Spread:** ask minus bid, as a percent of the midpoint.
- **Deep ITM:** in the money by a lot. Most of the price is intrinsic value, and the option moves almost like the stock.
- **Large accelerated filer (LA):** a big SEC filer with a 60-day 10-K deadline (Mar 1 for a December year-end).
- **(f):** the earnings date is estimated, not announced (`verified: false`).
- **Paper book:** `Baxter/paper_book.md`, entries with no money, used to test the rules on names the real fund can't afford.
- **Stamp:** the `updated_at` date on the analyst-ratings aggregate.
