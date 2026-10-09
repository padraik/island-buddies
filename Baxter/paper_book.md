# BAXTER'S PAPER BOOK

*Started Fri Oct 9, 2026, 1:35pm ET, at Michael's request. No money. Its job is to answer one question: do the Iron Rules pick winners on the larger, liquid names the real fund can't afford yet? Every paper entry runs the same funnel as a real one, on live data pulled that run, so when the reserve grows (or the call changes something) we already know whether the method works on those names.*

## HOW IT WORKS

- **Rules:** R1, R2, R3, R4, R6 exactly as binder Tab 1, checked on live data the run the entry is logged. **Rule 5 is dropped** (that's the whole point: these names cost $1-30 a share, the real line is $0.676). Hard limits 7-10 don't apply to paper (no fund value is at risk).
- **Liquidity test (the floor proposed to Michael Oct 9, applied here so we learn what it does):** open interest >= 250 on the contract, and spread <= 25% of mid. Fails it = no paper entry.
- **Fills are honest:** paper buys fill at the **ask**, paper sells at the **bid**, from a live quote with its timestamp. Never the mark. 1 contract per entry.
- **Exits:** binder Tab 4, same as real: sell the ramp (deadline = last trading run before the print, or the day before the earliest of tool date / last year's date while unannounced), Rule 4 live breach = same-day exit, +150% single-contract hold-vs-sell written, never into expiry.
- **Who updates it:** the WRAP run marks every open paper position at the bid daily; any run on a ramp-sell date closes the paper position at that run's bid. EVENING sessions add entries from the paper scan (`Baxter Oct9 PAPER large-cap Oct19-Nov20 prints`, `20e32def-9451-43e5-92b3-c8b4231d376e`).
- **What gets compared at the end:** paper P&L per trade, how often R6-passing liquid names actually made the move, and what the spread cost on entry + exit. That's the evidence for any later rule or sizing talk.

## OPEN PAPER POSITIONS

| Opened | Contract | Paper fill (ask) | Quote at entry | Stock | BE | R6 max BE | Low Buy target | Print | Ramp-sell deadline | Instrument |
|---|---|---|---|---|---|---|---|---|---|---|
| Oct 9 1:37pm | **BA $195C Nov20** | **$7.70** ($770) | 7.30 / 7.70, OI 1,695, vol 305 | $190.60 | $202.70 (+6.35%) | $203.65 (cap 6.85%) | $240 (28/5/0) | **Tue Oct 27 AM, verified** (LY Oct 29) | **Mon Oct 26, 3:35pm** | `a30375aa-c7ba-4af2-8005-110f42ab9f98` |
| Oct 9 1:37pm | **CMG $32.5C Nov20** | **$1.48** ($148) | 1.42 / 1.48, OI 5,109, vol 716 | $31.385 | $33.98 (+8.27%) | $35.04 (cap 11.65%) | $35 (27/12/0, stamp Oct 8) | **Wed Oct 28 PM, verified** (LY Oct 29) | **Wed Oct 28, 3:35pm** | `d09c051f-be72-4b1a-8c81-f83eeb9371d2` |
| Oct 9 1:37pm | **LVS $37.5C Nov20** | **$1.35** ($135) | 1.12 / 1.35, OI 1,417, vol 1,024 | $36.00 | $38.85 (+7.92%) | $40.08 (cap 11.33%) | $47 (17/7/0) | Wed Oct 21 PM (f) (LY Oct 22) | **Tue Oct 20, 3:35pm** | `5e7ad1e5-8080-48f8-8d3f-ea3f5e0b81f0` |

Paper deployed: $1,053. (For scale: the real fund's whole reserve is $676.)

**Marks (WRAP Fri Oct 9, close, at the bid):**

| Contract | Bid / ask | Stock | Paper P&L at bid | Rule 4 low vs BE | Ramp-sell deadline |
|---|---|---|---|---|---|
| BA $195C Nov20 | 7.15 / 7.55 | $190.41 (+1.4%) | **-$55** | $240 vs $202.70, holds | Mon Oct 26 3:35pm |
| CMG $32.5C Nov20 | 1.49 / 1.62 | $31.58 (-3.4%) | **+$1** | $35 vs $33.98, holds (stamp Oct 9 14:11 UTC, low unchanged) | Wed Oct 28 3:35pm |
| LVS $37.5C Nov20 | 0.81 / 1.36 | $36.17 (+0.2%) | **-$54** | $47 vs $38.85, holds | Tue Oct 20 3:35pm |

Paper book at the bid: **-$108** on $1,053 (-10.3%), day one. Almost all of it is spread, not movement: BA and LVS are roughly where they were at entry, and LVS's bid fell to 0.81 after the bell (closing spread 51% of mid vs 18.6% at entry). That is exactly the cost Rule 7 exists to price, and why "fills at the ask, marks at the bid" is the honest way to keep this book.

Entry notes:
- **BA:** R1 0.18; R2 Oct 27 + 21 = Nov 17 and LY Oct 29 + 21 = Nov 19, both <= Nov 20; 10-Q Nov 9 is 9 trading days before expiry. R6 on six AM prints (+6.06 / -4.37 / -4.37 / -1.56 / +5.53 / +4.76), median 4.56%. Tightest R6 margin of the three (95 cents). Spread 5.3% of mid.
- **CMG:** R1 0.23; stock -4.0% today; R4 margin $1.02 ($35 low vs $33.98 BE). Six PM prints (+1.60 / -13.34 / -18.18 / +1.94 / +3.03 / +12.50), median 7.76%. Spread 4.1% of mid.
- **LVS:** R1 ~0 (at the low); the fund lost $67 on LVS in July (sold late, see binder Tab 5). Six PM prints (+6.49 / +4.31 / +12.39 / -13.96 / -8.62 / +1.72), median 7.55%. Spread 18.6% of mid, the widest of the three.

## CLOSED PAPER POSITIONS

| Opened | Closed | Contract | In (ask) | Out (bid) | P&L | Why closed |
|---|---|---|---|---|---|---|
| | | | | | | |

## GLOSSARY
- **Paper book:** trades written down as if placed, with no money. Fills are the live ask (buy) and bid (sell) at the time logged.
- **R1-R6:** binder Tab 1 Iron Rules. R1 range percentile, R2 earnings before expiry, R3 analyst consensus, R4 lowest Buy target above breakeven, R5 affordability (dropped here), R6 reachability (breakeven move <= 1.5x median earnings move).
- **BE (breakeven):** strike + premium paid.
- **OI (open interest):** contracts outstanding on that strike; a proxy for whether anyone trades it.
- **Spread % of mid:** (ask - bid) / mid. What you lose just by getting in and out.
- **Ramp sell:** selling before the print into the pre-earnings premium (Tab 4).
- **(f):** earnings date not yet company-verified (`get_earnings_results` verified: false).
