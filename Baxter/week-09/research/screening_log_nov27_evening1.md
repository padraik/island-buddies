# Screening log: Fri Nov 27, EVENING 1 (6:00pm ET)

**Job (from the queue, item 1):** NOW follow-ups (one search max, paper only), then band D parks from the Nov 21 log, median-first, up to 25. Nothing held. R5 line: 10% x $715.96 / 100 = **$0.716/share** (3.5/5), so everything here is paper-book size; the paper book applies R7 (OI >= 250, spread <= 25% of mid).

**Source:** Robinhood tools, run ~23:00-23:10 UTC Nov 27 on Friday's 1pm early close. 1 web search (NOW).

**Picked:** the next 25 band D parks in queue order: PH, CAT, MLM, RBC, CW, HUBB, CMI, TT, ETN, AXP, HII, EVR, CI, LPLA, LHX, SXI, TEL, COF, TMUS, DLR, AEM, RRX, CHRW, HLI, OSK. None had been worked since Nov 21.

**Method (same as Nov 24/25):** moves from daily closes Oct 2025 - Nov 2026 (AM print: prior close to print day; PM print: print day to next day), last 5 prints. R1 = closing-range percentile over the last 252 bars, using **Friday's regular-session last trade** as today's bar (the daily-bar pull ended at Wednesday). Medians >= 8% go to one near-ATM call on the first expiry that passes R2. R6 at the ask vs Friday's price. R4 against the tool's low target.

## 0. NOW follow-up (paper position `deca0cea`, one search)

- **KeyBanc $85 is real:** KeyBanc reiterated **Underweight, $85**, after NOW's May 5 analyst day. That is the one Sell in the tool's 45/4/1. A Sell target never counts toward R4 (lowest *Buy* target), so the paper line's Rule 4 check is unchanged (tool low $100 is UBS's Neutral; the lowest Buy is at or above that).
- **Needham:** the search only turned up pre-split Buy targets ($1,150 and $1,200). Consistent with the $115 post-split figure being Needham's, but it isn't confirmed this run.
- **Q3 adjusted EPS beat or miss:** not resolved (search budget spent). Stays open, low priority: it doesn't move any rule on a paper line.

## 1. Medians and R1

| Ticker | Next print (f) | Moves (oldest first) | Median | Cap | R1 (Fri) | Verdict |
|---|---|---|---|---|---|---|
| RRX | none in tool (LY Feb 4 PM) | -3.7 / +12.2 / -10.9 / -16.7 / +11.8 | **11.8%** | 17.7% | 0.235 | to the chain |
| CHRW | Jan 27 PM | +19.7 / +5.1 / -2.5 / -15.4 / -11.1 | 11.1% | 16.65% | **0.264** ($147.00; 0.238 Wed) | **KILLED R1** (MID-OUT by 1.4 pts; re-check at the next pass) |
| HII | Feb 4 AM | +6.9 / -10.6 / -10.2 / +14.1 / +13.2 | **10.6%** | 15.9% | 0.241 | R4 (below) |
| CAT | Feb 2 AM `verified: true` | +11.6 / +3.4 / +9.9 / +5.6 / -9.3 | **9.3%** | 13.95% | 0.093 | to the chain |
| EVR | Feb 3 AM | -9.1 / +5.2 / -4.8 / -10.5 / +12.5 | 9.1% | | **0.340** | **KILLED R1** (MID-OUT) |
| TMUS | Feb 10 AM | 5.1% | | | 0.313 | KILLED R1 + R6 |
| PH | Jan 28 AM | 4.0% | | | 0.359 | KILLED R1 + R6 |
| AXP | Jan 29 AM | 4.3% | | | 0.261 | KILLED R1 + R6 |
| AEM | Feb 11 PM | 3.9% | | | 0.322 | KILLED R1 + R6 |
| MLM | Feb 10 AM | 2.4% | | | 0.301 | KILLED R1 + R6 |
| DLR | Feb 4 PM | 2.2% | | | 0.347 | KILLED R1 + R6 |
| OSK | Jan 28 AM | 1.9% | | | 0.435 | KILLED R1 + R6 |
| TEL | Jan 20 AM | 1.8% | | | 0.426 | KILLED R1 + R6 |
| RBC | Feb 4 AM | 5.4% | | | 0.249 | KILLED R6 structural |
| HUBB | Feb 2 AM | 4.9% | | | 0.200 | KILLED R6 structural |
| CMI | Feb 4 AM | 4.9% | | | 0.086 | KILLED R6 structural |
| LPLA | Jan 28 PM | 4.6% | | | 0.114 | KILLED R6 structural |
| CW | Feb 10 PM | 4.0% | | | 0.055 | KILLED R6 structural |
| TT | Jan 28 AM | 3.9% | | | 0.232 | KILLED R6 structural |
| LHX | Jan 28 AM | 3.1% | | | 0.223 | KILLED R6 structural |
| CI | Feb 4 AM `verified: true` | 3.0% | | | 0.243 | KILLED R6 structural |
| ETN | Feb 2 AM | 2.7% | | | 0.099 | KILLED R6 structural |
| SXI | Jan 28 PM | 2.5% | | | 0.065 | KILLED R6 structural |
| COF | Jan 21 PM | 2.4% | | | 0.110 | KILLED R6 structural |
| HLI | | | | | | **KILLED R3** (5 Buy / 6 Hold) |

## 2. Ratings and the chain

| Ticker | Stock (Fri) | Ratings / low | Expiry (why) | Contract | Bid / Ask | OI | BE at ask | Needs | Cap | R4 | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|---|
| HII | 304.53 | 10/6/0, low $300, stamp **Sep 24** (64 days) | | | | | | | | fail | **KILLED R4** (the low is under the stock, and the stamp fails Tab 6's 60-day dating) |
| CAT | 562.21 | 19/11/1, low $575, stamp Nov 7 (after the Oct 28 - Nov 5 drop, 713 -> 554) | Mar19 (Feb 2 + 21 = Feb 23) | $300C | 260.15 / 272.10 | **0** | 572.10 | +1.8% | 13.95% | pass ($2.90) | **R7** |
| | | | | $350C | 213.60 / 225.20 | 2 | 575.20 | +2.3% | | fail by $0.20 | R4 + R7 |
| | | | | $400C | 168.55 / 179.65 | 8 | 579.65 | +3.1% | | fail | R4 + R7 |
| | | | | $440C - $560C | e.g. $500C 90.15 / 99.65 | 11-109 | 585.65 - 622.00 | | | fail | R4 + R7 |
| RRX | 161.52 | 11/0/0, low $195 (**no stamp**) | May21 (Feb19 fails R2: LY Feb 4 + 21 = Feb 25; no Mar/Apr listed) | **$150C** `01c93b13-0b9e-4d49-9a02-37845e61b8db` | 31.10 / 34.20 | **3** | 184.20 | +14.0% | 17.7% | pass ($10.80) | **R7** |
| | | | | $155C `3d4ccfb8-a775-4363-8085-621051b2d9d2` | 28.70 / 31.70 | 3 | 186.70 | +15.6% | | pass | R7 |
| | | | | $160C `3ef5e4b8-9097-4c51-83c2-83abb1cf5a5a` | 26.10 / 29.40 | 1 | 189.40 | +17.3% | | pass | R7 |
| | | | | $165C | 23.90 / 27.00 | 2 | 192.00 | +18.9% | | pass | R6 fail |

- **RRX is the best shape in the batch:** 11 Buys, 0 Holds, 0 Sells, an 11.8% mover, R6 passes at the ask on three strikes, and the $195 low sits $10.80 over the $150C's breakeven. It dies only on R7 (OI 1-3), and its ratings carry no `updated_at`, so the floor gate would need a dated target too. The tool shows no upcoming print, so R2 runs on last year's Feb 4 PM date alone; a doc would need the tool date to show up first. Weekly re-quote line.
- **CAT** sits at 0.093 of its range after halving from the Jun 30 high ($1,064.90), with a fresh stamp, but the $575 low is only 2.3% over the stock. The one strike that clears R4 at the ask is the $300C, which is stock replacement with OI 0. Dead for now. If the low target rises, or the stock falls far enough below $575 to make a normal strike fit, it can come back.

## Totals

25 names moved. 0 advanced past the chain, 0 docs, 0 buyable (real or paper). Kills: 11 R6 structural, 10 R1 (8 with R6 too: TMUS, PH, AXP, AEM, MLM, DLR, OSK, TEL; EVR and CHRW on R1 alone), 1 R3 (HLI), 1 R4 (HII), 1 chain R4 + R7 (CAT). R7 only, to the weekly line: RRX.

**Band D parks left (paper only):** CBRE, ENS, PLD, WMS, BX (thin), NVT, PCAR (7). Skip stale stamps: CRS, HWM.

## GLOSSARY

- **R1-R7:** the Iron Rules (binder Tab 1). R1 range percentile, R2 earnings before expiry, R3 analyst consensus, R4 lowest Buy target above breakeven, R5 price cap vs reserve, R6 reachability (move to BE <= 1.5x median print), R7 liquidity (OI >= 250, spread <= 25% of mid).
- **Median print:** the middle value of the absolute earnings-day moves, sign ignored.
- **R6 structural:** a median so small (under ~8%) that no near-ATM contract can pass R6 once time value is paid.
- **BE (breakeven):** strike + premium paid, here at the ask.
- **Floor gate / stamp:** binder Tab 6: a Rule 4 target only counts if it's dated within 60 days and was published after the decline. A ratings record with no `updated_at` can't prove that.
- **MID-OUT:** R1 between 25% and 75% of the range: no direction, no play.
- **Stock replacement:** a call so deep in the money that it moves almost dollar for dollar with the stock (delta near 1). No leverage edge, and these strikes rarely have open interest.
- **OI:** open interest, the number of contracts outstanding.
- **LY:** last year's same-quarter report date.
- **Band D:** the scanner's $100+ price slice. Paper-book size at today's reserve.
- **Weekly re-quote line:** contracts that fail only on liquidity, checked once a week instead of every run.
