# Screening log, Fri Oct 16, 2026, 10:00pm ET (EVENING 3, VM)

EVENING 3's job is the refill and the PREMARKET plan. The queue came in at 10 live, so the refill went to a window nobody has fished in Era 2: **December prints** (Dec 5 - Dec 23), which Jan15 contracts can carry under Rule 2. Plus the one CIFR news search EVENING 2 asked for. All quotes are Friday's closing book (stock from `get_equity_quotes` last trade, not the daily bar). 3 searches.

## Part 1: CIFR, why it halved (one search)

| Ticker | Contract | Search result | Verdict |
|---|---|---|---|
| CIFR | Dec18 $10C (paper) | The slide is partly company-specific: Cipher announced a large **zero-coupon convertible note offering (~$800-850M)** to fund the Barber Lake data center and its HPC pipeline; a result dated Oct 14, 2026 has the stock -12.8% that day on it. The rest is the miner tape (CLSK, WULF, RIOT, IREN all down hard Friday). No guidance cut, no lost hosting contract, no going-concern language found. | **Stays, floor gate tightened.** A convert raise is dilution, not a broken business, so it doesn't kill on thesis. But it's exactly the kind of event that gets analysts to re-cut, so the $18 low has to be dated **after Oct 14** to count. Re-test R6 Monday at the live quote |

## Part 2: fresh scan, December prints

Preview scan (not saved): market cap >= $300M, earnings **Dec 5 - Dec 23, 2026**, last $2+, 52w range pct < 0.25 (weekly bars), Friday call volume > 300. **19 names.**

Rule 2 for Jan15: the later of (tool date, LY date) must be on or before Dec 25; all of these are. 10-Q / 10-K deadlines land Dec 10 - Dec 29, at least 11 trading days before Jan 15.

- **No coverage (1):** VZLA.
- **Rule 3 fail (10):** RH 7/13/2, LULU 4/27/6, LEN 2/10/11, KBH 3/11/6, NKE 11/25/7, GIS 4/15/4, OXM 0/6/0, CPB 1/14/8, CAG 1/12/6, FCEL 7/3/2.
- **Rule 4 fail at the free screen (3):** ORCL 36/8/1 (low $110 vs $127.80 stock: no call can have a BE under the low), BIRK 20/4/1 (low $26.93 vs $34.10), CHWY 22/9/0 (low $21.00 vs $21.00).
- **Already queued (1):** PL (Jan15 $10C, floor gate).
- **To the chain (4):** AVAV, NNE, UEC, AVGO.

R6 base = median absolute one-day reaction over the last 4 prints (pm: print-day close to next close; am: prior close to print-day close).

| Ticker | Stock | Pct | Ratings / low | Print (tool), LY | Last 4 reactions | Median / cap | Contract | Bid / ask, OI | BE (ask) / needs | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| AVAV | $121.81 | -0.046 | 21/5/0, $165 | Dec 8 PM (f), Dec 9 | -12.85 / -6.25 / +18.76 / +4.45 | 9.55% / 14.33% | Jan15 $120C | 13.30 / 20.10, OI 138 | $140.10 / +15.0% | **KILLED, R6 + R7** ($125C +17.6%, OI 35; $130C +18.2%, OI 53; every spread 16-41%) |
| NNE | $12.88 | -0.040 | 7/1/0, $22 | Dec 17 PM (f), Dec 18 AM | +0.80 / -0.63 / -9.51 / +7.94 | 4.37% / 6.55% | Jan15 $12C | 2.20 / 2.55, OI 125 | $14.55 / +13.0% | **KILLED, R6 + R7** ($13C +17.2%, OI 246) |
| **UEC** | $7.91 | -0.089 | 8/3/0, $10 (undated) | Dec 9 AM (f), Dec 10 | -7.45 / +6.78 / -15.54 / +0.87 | 7.12% / 10.67% | **Jan15 $7C** `60caab3b-653a-4ae1-b8b1-37287ffb77c0` | 1.49 / 1.57, **OI 1,881** | $8.57 / **+8.3%** | **ADVANCE (paper), floor gate.** R1 (under its weekly-bar low), R2, R3, R4 ($10 > $8.57, 16.7% margin), R6 (2.4 pt margin), R7 (spread 5.2%) pass. $8C fails R6 (+14.7%). One search: aggregators show a $12 low and HCW $26.75 Buy dated Oct 6; nobody owns the tool's $10 with a date. Real money: $157 a contract, far over the $0.676 line |
| **AVGO** | $328.81 | 0.197 | 50/3/0, $350 (undated) | **Dec 9 PM (v)**, Dec 11 | -11.43 / +4.80 / -12.59 / -2.74 | 8.12% / 12.17% | **Jan15 $300C** `7871e0c1-cace-44bc-af55-ec8d57c26989` | 45.05 / 47.10, **OI 3,933** | $347.10 / +5.6% | **ADVANCE (paper), floor-owner gate.** R1, R2, R3, R6, R7 (spread 4.4%) pass; R4 $350 vs $347.10 is a **$2.90 margin**. The **$280C** `507842e4-dbff-41d1-8e36-a5bd67171a18` (58.90 / 60.90, OI 836, BE $340.90, +3.7%) has a $9.10 margin; the $310C+ all fail R4 ($320C BE $354.25). One search: DA Davidson cut to **$350 with a Neutral** (Sep 4). If that's the tool's $350, it's a Hold target and the real Buy-side low is higher; if a Buy analyst holds $350, the margin is thin. Settle the owner before a doc |

**What part 2 says:** December is a cleaner pool than November. Only 19 bottom-quartile names have real call volume, and the consumer names (LULU, NKE, LEN, CPB, GIS) are bottom-quartile because the Street agrees with the market: Rule 3 throws them out. The two survivors are the opposite kind. UEC is a uranium name under its 52-week low whose own prints move 7%, with a 1,881-OI January call that only needs 8.3%. AVGO is the biggest name the funnel has ever passed: it fell 4.5% Friday to $328.81, and its deep-in-the-money January calls clear every rule, with R4 the one to watch. The $300C is in the money ($28.81 of $47.10 is intrinsic; delta 0.72, ~5x leverage), which isn't the fund's usual out-of-the-money shape. Bearxter will want that said in any doc.

## Counts

19 names moved (18 new from the scan, PL already queued, plus CIFR): **16 killed** (10 R3, 1 no coverage, 3 R4 at the screen, AVAV and NNE on R6 + R7 at the chain), **2 advanced** (UEC, AVGO, both paper, both floor-gated), CIFR kept with a tightened gate. 3 searches (CIFR, UEC, AVGO).

## GLOSSARY
- **R1-R7**: Iron Rules, binder Tab 1. R1 range percentile, R2 earnings before expiry, R3 analyst consensus, R4 bear floor (lowest Buy target above breakeven), R5 affordability, R6 reachability (needed move <= 1.5x median earnings move), R7 liquidity (OI >= 250, spread <= 25% of mid).
- **Pct**: where the stock sits in its 52-week range (0 = at the low, 1 = at the high); negative means under the weekly-bar low.
- **BE**: breakeven = strike + ask.
- **Needs**: the stock move from Friday's close to BE.
- **Median / cap**: median absolute one-day earnings reaction over the last 4 prints, and 1.5x that (the most R6 allows).
- **(v) / (f)**: earnings date company-verified / forecast from cadence, per `get_earnings_results`.
- **LY**: last year's same-quarter report date.
- **Deep ITM**: a call whose strike is well below the stock price; most of its price is intrinsic value, so it moves almost like the stock.
- **Convertible note**: debt that can turn into shares later; it dilutes existing holders if converted.
- **Floor gate**: the play passes R4 on the number, but the lowest Buy target isn't dated after the stock's slide (binder Tab 6, 60-day dating rule), so it can't be trusted yet.
