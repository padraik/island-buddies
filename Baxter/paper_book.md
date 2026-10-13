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
| Oct 9 1:37pm | **LVS $37.5C Nov20** | **$1.35** ($135) | 1.12 / 1.35, OI 1,417, vol 1,024 | $36.00 | $38.85 (+7.92%) | $40.08 (cap 11.33%) | $47 (17/7/0) | **Mon Oct 26 PM (f)** (was Oct 21 PM (f) through Oct 12 WRAP; tool moved it, seen EVENING 2 Oct 12) (LY Oct 22) | **Tue Oct 20, 3:35pm** (held; rule-derived would be Wed Oct 21, the day before LY's Oct 22) | `5e7ad1e5-8080-48f8-8d3f-ea3f5e0b81f0` |
| Oct 9 6:00pm (EVENING 1, closing quote 3:59pm) | **FSLR $175C Nov20** | **$16.50** ($1,650) | 13.60 / 16.50, OI 282, vol 11, spread 19.3% | $177.82 | $191.50 (+7.69%) | $195.98 (cap 10.21%) | $251 Piper OW (Sep 30, post-drop); $218 Evercore (Aug 17) inside 60 days | Thu Oct 29 PM (f) (LY Oct 30) | **Wed Oct 28, 3:35pm** | `99f5f557-ba41-4590-acb3-0728c944c360` |
| Oct 9 6:00pm (EVENING 1, closing quote 3:59pm) | **APP $290C Dec18** | **$27.40** ($2,740) | 26.10 / 27.40, OI 350, vol 62, spread 4.9% | $277.02 | $317.40 (+14.58%) | $326.58 (cap 17.89%) | $375 Jefferies Buy (Oct 8, post-drop) | **Wed Nov 4 PM, verified** (LY Nov 5) | **Wed Nov 4, 3:35pm** | `07e4b5a0-3754-41a4-9b0a-8d9c1999952d` |
| Oct 12 9:35am (OPEN) | **BABA $110C Dec18** | **$8.55** ($855) | 7.90 / 8.55, OI 8,961, spread 7.9% | $110.07 | $118.55 (+7.70%) | $122.18 (cap 11.00%) | Baird $160 (Aug 21, ages out Oct 20), then Bernstein $165 (Sep 7) (45/1/0) | Tue Nov 24 AM (f) (LY Nov 25), 6-K filer | **Mon Nov 23, 3:35pm** | `5c993f3b-5208-4386-b2d3-0e6dad26a30b` |
| Oct 12 9:35am (OPEN) | **CAVA $50C Dec18** | **$7.55** ($755) | 6.80 / 7.55, OI 468, spread 10.5% | $52.54 | $57.55 (+9.54%) | $59.36 (cap 12.99%) | JPM OW $80 (Sep 18) (20/9/1) | Tue Nov 3 PM (f) (LY Nov 4) | **Mon Nov 2, 3:35pm** | `b0d2e74a-f193-4989-a547-e8e13a1cccbc` |
| Oct 12 10:36am (MIDDAY) | **TMUS $160C Nov20** | **$5.20** ($520) | 5.00 / 5.20, OI 540, vol 45, spread 3.9% | $153.17 | $165.20 (+7.85%) | $166.88 (cap 8.95%) | Raymond James Outperform $170 (Oct 12, first post-drop Buy target; MarketBeat) (27/4/0) | **Wed Oct 28 PM, verified** (LY Oct 23 AM) | **Tue Oct 27, 3:35pm** | `571117e7-6f1e-4733-be01-b46c852c4fff` |

Paper deployed: $7,573 (BA, CMG, LVS $1,053 + FSLR $1,650 + APP $2,740 + BABA $855 + CAVA $755 + TMUS $520). (For scale: the real fund's whole reserve is $676.)

*CAVA note: the doc's $55C failed R6 at the open (BE $60.10 vs max $59.36, stock -2.1%); the $52.5C isn't listed for Dec18, so the entry is the one-strike-ITM $50C. Docs: `week-09/research/research_BABA_paper.md`, `research_CAVA_paper.md` (Oct 12 OPEN addenda).*

*TMUS note (Oct 12 MIDDAY): parked since the Oct 9 -13% day because no Buy target had been published after the drop. Raymond James upgraded to Outperform $170 this morning (MarketBeat; one web search did not independently confirm it). R6 margin is thin: needs +7.85% vs the 8.95% cap. No paper doc yet; EVENING 2 writes `research_TMUS_paper.md` (drop cause, Five-Baxter meeting, EXIT PLAN). Log: `week-09/research/screening_log_oct12_midday.md`.*

*EVENING 2 (Mon Oct 12, 8pm) notes:* **TMUS** doc written: `week-09/research/research_TMUS_paper.md` (drop cause read: SpaceX's ~$8B purchase of Grain Management's 800 MHz spectrum, Oct 9, sector-wide; Five-Baxter vote 4-1 hold, Bearxter wanted out on the single-sourced $170 floor; tool low $169 is stamped Oct 8, pre-drop). **APP** competitor headline read (Meta bidding harder on in-game inventory, Unity ruling, CloudX); addendum in `research_APP_paper.md`, Rule 4 holds. **LVS** tool date moved Oct 21 PM (f) -> **Oct 26 PM (f)**; Sands hasn't announced (one search). Paper ramp sell **held at Tue Oct 20 3:35pm** (an Oct 21-22 print stays plausible until Sands announces; LY Oct 22). Still no docs for the Oct 9 paper entries BA, CMG, LVS (entered on the 1:35pm Oct 9 start-up run); EVENING 3 or Saturday.

*EVENING entries are logged at the session's latest real quote, which after the bell is the regular-session close. That's still the ask someone could have paid at 3:59pm, not a mark. FSLR's closing spread (19.3%) is wider than its 2:35pm spread (5.2%), so the paper fill is the worse of the two, which is the honest direction.*

**Marks (WRAP Fri Oct 9, close, at the bid):**

| Contract | Bid / ask | Stock | Paper P&L at bid | Rule 4 low vs BE | Ramp-sell deadline |
|---|---|---|---|---|---|
| BA $195C Nov20 | 7.15 / 7.55 | $190.41 (+1.4%) | **-$55** | $240 vs $202.70, holds | Mon Oct 26 3:35pm |
| CMG $32.5C Nov20 | 1.49 / 1.62 | $31.58 (-3.4%) | **+$1** | $35 vs $33.98, holds (stamp Oct 9 14:11 UTC, low unchanged) | Wed Oct 28 3:35pm |
| LVS $37.5C Nov20 | 0.81 / 1.36 | $36.17 (+0.2%) | **-$54** | $47 vs $38.85, holds | Tue Oct 20 3:35pm |

Paper book at the bid: **-$108** on $1,053 (-10.3%), day one. Almost all of it is spread, not movement: BA and LVS are roughly where they were at entry, and LVS's bid fell to 0.81 after the bell (closing spread 51% of mid vs 18.6% at entry). That is exactly the cost Rule 7 exists to price, and why "fills at the ask, marks at the bid" is the honest way to keep this book.

**Marks (WRAP Mon Oct 12, close, at the bid; quotes 3:59pm ET):**

| Contract | Bid / ask | Stock | Paper P&L at bid | Rule 4 low vs BE | Ramp-sell deadline |
|---|---|---|---|---|---|
| BA $195C Nov20 | 6.55 / 6.90 (OI 1,514) | $189.48 (-0.5%) | **-$115** | $240 vs $202.70, holds | Mon Oct 26 3:35pm |
| CMG $32.5C Nov20 | 0.98 / 1.11 (OI 5,314) | $30.40 (-3.8%) | **-$50** | $35 vs $33.98, holds (tool stamp Oct 12 14:30 UTC, low unchanged) | Wed Oct 28 3:35pm |
| LVS $37.5C Nov20 | 1.05 / 1.29 (OI 2,106) | $36.15 (-0.1%) | **-$30** | $47 vs $38.85, holds | **Tue Oct 20 3:35pm** (nearest) |
| FSLR $175C Nov20 | 15.75 / 18.50 (OI 271) | $179.64 (+1.0%) | **-$75** | Evercore $218 (ages out Oct 16) / Piper $251 vs $191.50, holds (tool $197 is the Bernstein Sell) | Wed Oct 28 3:35pm |
| APP $290C Dec18 | 22.10 / 25.30 (OI 377) | $270.84 (-2.2%) | **-$530** | Jefferies $375 vs $317.40, holds | Wed Nov 4 3:35pm |
| BABA $110C Dec18 | 8.25 / 8.70 (OI 8,961) | $110.81 (-0.5%) | **-$30** | Baird $160 vs $118.55, holds | Mon Nov 23 3:35pm |
| CAVA $50C Dec18 | 6.10 / 6.95 (OI 468) | $52.535 (-2.1%) | **-$145** | JPM $80 vs $57.55, holds | Mon Nov 2 3:35pm |
| TMUS $160C Nov20 | 4.00 / 4.70 (OI 540) | $151.86 (+2.2%) | **-$120** | RJ $170 (tool low now $169) vs $165.20, holds | Tue Oct 27 3:35pm |

Paper book at the bid: **-$1,095** on $7,573 (-14.5%). It's still mostly spread. Six of eight underlyings are within 2.2% of where they were at entry, and the bids sit 4-14% under the asks we paid. APP is the real mover: the stock is down $6 (-2.2%) since Friday's entry, and that $3.20 closing spread costs another $320. CMG is the only one where the stock moved against the thesis in a way that matters (-3.8% today, $3.58 under breakeven). No Rule 4 breach, no ramp deadline before Tue Oct 20 (LVS).

Entry notes:
- **BA:** R1 0.18; R2 Oct 27 + 21 = Nov 17 and LY Oct 29 + 21 = Nov 19, both <= Nov 20; 10-Q Nov 9 is 9 trading days before expiry. R6 on six AM prints (+6.06 / -4.37 / -4.37 / -1.56 / +5.53 / +4.76), median 4.56%. Tightest R6 margin of the three (95 cents). Spread 5.3% of mid.
- **CMG:** R1 0.23; stock -4.0% today; R4 margin $1.02 ($35 low vs $33.98 BE). Six PM prints (+1.60 / -13.34 / -18.18 / +1.94 / +3.03 / +12.50), median 7.76%. Spread 4.1% of mid.
- **FSLR (EVENING 1):** R1 ~0.05 (low $168.60). R2 Oct 29 / LY Oct 30 + 21 = Nov 20, passes exactly; 10-Q Nov 9 is 9 trading days before expiry. R3 29/10/1 (the one Sell is Bernstein Underperform $197, which is also the tool's "low target"; it was never a floor). R4 dated via MarketBeat: lowest Buy-side target after the Sep 21-25 leg down is Piper OW $251 (Sep 30); oldest inside 60 days is Evercore Positive $218 (Aug 17). R6 six PM prints (-8.32 / +5.29 / +14.28 / -13.61 / +4.86 / +2.44), median 6.80%. Nearest-OTM $180C / $185C fail R7, so it's one strike in-the-money. Doc: `week-09/research/research_FSLR_paper.md` (EVENING 2). Floor of record $218 (Evercore, ages out Oct 16) then $251 (Piper); Sep 24-25's -10% was a Treasury-yield sector move.
- **APP (EVENING 1):** R1 0.02 ($266.84-$738). R2 Nov 4 verified + 21 = Nov 25 <= Dec 18. R3 32/7/0. R4: the tool's $325 (Sep 11) predates the Sep 28 week's -17%; Jefferies cut to $375 on Oct 8 and kept Buy, which is the post-drop floor. R6 six PM prints (+11.88 / +11.97 / +0.70 / -19.68 / +6.41 / -19.66), median 11.93%. $290C chosen over $280C for the spread (4.9% vs 13%). Doc: `week-09/research/research_APP_paper.md` (EVENING 2). Unread: a "competitor concerns" headline; read it on the next DO run with a search to spare.
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
