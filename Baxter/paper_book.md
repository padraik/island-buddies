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
| Oct 9 6:00pm (EVENING 1, closing quote 3:59pm) | **APP $290C Dec18** | **$27.40** ($2,740) | 26.10 / 27.40, OI 350, vol 62, spread 4.9% | $277.02 | $317.40 (+14.58%) | $326.58 (cap 17.89%) | $375 Jefferies Buy (Oct 8, post-drop) | **Wed Nov 4 PM, verified** (LY Nov 5) | **Wed Nov 4, 3:35pm** | `07e4b5a0-3754-41a4-9b0a-8d9c1999952d` |
| Oct 12 9:35am (OPEN) | **BABA $110C Dec18** | **$8.55** ($855) | 7.90 / 8.55, OI 8,961, spread 7.9% | $110.07 | $118.55 (+7.70%) | $122.18 (cap 11.00%) | Baird $160 (Aug 21, ages out Oct 20), then Bernstein $165 (Sep 7) (45/1/0) | Tue Nov 24 AM (f) (LY Nov 25), 6-K filer | **Mon Nov 23, 3:35pm** | `5c993f3b-5208-4386-b2d3-0e6dad26a30b` |
| Oct 12 9:35am (OPEN) | **CAVA $50C Dec18** | **$7.55** ($755) | 6.80 / 7.55, OI 468, spread 10.5% | $52.54 | $57.55 (+9.54%) | $59.36 (cap 12.99%) | JPM OW $80 (Sep 18) (20/9/1) | **Wed Nov 4 PM, verified** (changed EVENING 1 Thu Oct 29; was Tue Nov 3 PM (f)) (LY Nov 4) | **Wed Nov 4, 3:35pm** (was Mon Nov 2) | `b0d2e74a-f193-4989-a547-e8e13a1cccbc` |
| Oct 13 10:00pm (EVENING 3, closing quote 3:59pm) | **BURL $270C Dec18** | **$18.60** ($1,860) | 16.10 / 18.60, OI 386, vol 2, spread 14.4% | $263.31 | $288.60 (+9.60%) | $291.98 (cap 10.89%) | Tool $290 (undated, binding, $1.40 over BE); dated post-print Buys: Bernstein OP $355, BofA Buy $365 (Aug 27-28) (15/6/0) | Tue Nov 24 AM (f) (LY Nov 25) | **Mon Nov 23, 3:35pm** | `51a66bd6-72d6-42d3-8e85-3d7c078df118` |
| Oct 17 9:00am (SATURDAY, Friday closing quote 3:59pm) | **AVGO $280C Jan15** | **$60.90** ($6,090) | 58.90 / 60.90, OI 836, vol 55, spread 3.3% | $328.81 | $340.90 (+3.68%) | $368.83 (cap 12.17%) | Tool $350 (50/3/0; undated; DA Davidson's $350 is a Neutral, so the Buy-side low is >= $350) | **Wed Dec 9 PM, verified** (LY Dec 11) | **Wed Dec 9, 3:35pm** | `507842e4-dbff-41d1-8e36-a5bd67171a18` |
| Oct 21 8:00pm (EVENING 2, closing quote 3:59pm) | **NRG $105C Dec18** | **$7.10** ($710) | 6.20 / 7.10, OI 511, vol 1, spread 13.5% | $99.80 | $112.10 (+12.32%) | $113.21 (cap 13.44%) | Tool $131 (16/4/0; stamp Oct 3) = Jefferies Buy $131 (cut from $160, Sep 28 - Oct 19, post-slide); Seaport Buy $160 | Thu Nov 5 AM (f) (LY Nov 6 AM) | **Wed Nov 4, 3:35pm** | `6fa30201-0a25-46b0-91c9-ec10f7cb6620` |
| Oct 23 6:00pm (EVENING 1, closing quote 3:59pm) | **PAAS $40C Jan15** | **$3.90** ($390) | 3.50 / 3.90, OI 6,343, vol 120, spread 10.8% | $40.125 | $43.90 (+9.41%) | $43.93 (cap 9.48%) | RBC Buy $56 (Oct 14, post-slide); tool low $51 (6/2/0) | **Wed Nov 4 PM, verified** (LY Nov 12), 6-K filer | **Wed Nov 4, 3:35pm** | `7e29c70a-671f-4457-a7cb-b73c0e903ad1` |

Paper deployed (open): **$13,400** after MSTR closed Thu Oct 29 LASTCALL (-$2,205); **$15,605** after FSLR closed Wed Oct 28 LASTCALL (-$1,650); **$17,255** after TMUS closed Tue Oct 27 LASTCALL (-$520); **$17,775** after PAAS opened Fri Oct 23 EVENING 1 (+$390); **$17,385** after NRG opened Wed Oct 21 EVENING 2 (+$710); **$16,675** after CMG closed Wed Oct 21 WRAP on Rule 4 (-$123); **$16,823** after LVS closed Tue Oct 20 3:35pm (-$135); **$16,958** after MSTR opened Oct 19 EVENING 2 ($14,753 after BA closed Oct 19, + MSTR $2,205; was $15,523: BA, CMG, LVS $1,053 + FSLR $1,650 + APP $2,740 + BABA $855 + CAVA $755 + TMUS $520 + BURL $1,860 + AVGO $6,090). (For scale: the real fund's whole reserve is $676.)

*SATURDAY (Oct 17) note:* **AVGO $280C Jan15** entered at Friday's closing ask (doc `week-09/research/research_AVGO_paper.md`, Five-Baxter vote 4-1, Bearxter against on the deep-ITM shape and the down-reacting prints). The $280C was picked over the queue's $300C for R4 room ($9.10 vs $2.90 over BE). It's the book's first deep-ITM entry ($48.81 of the $60.90 is intrinsic, delta 0.81), so its result tests the rules on a liquid mega-cap, not the cheap-OTM shape the real fund buys. Log: `week-09/research/screening_log_oct17_saturday.md`.

*EVENING 2 (Mon Oct 19, 8pm) note:* **MSTR $120C Nov20** entered at Monday's closing ask (doc `week-09/research/research_MSTR_paper.md`, Five-Baxter vote 3-2, Bearxter against on the print being mostly a bitcoin readout, Macxter against on the shared bitcoin driver with RIOT/CLSK). Picked over the Dec18 $120C for R6 room (3.39 pt vs 0.48) and spread (8.0% vs 12.9%). R1 0.242 at $136.02; the 52-week line is falling as Oct 2025's highs roll off ($137.86 Tue, $136.31 Wed, $130.44 by Oct 29), so this was the last clean night to enter. R2 passes exactly (LY Oct 30 + 21 = Nov 20). First bitcoin-driven name in the book.

*EVENING 2 (Wed Oct 21, 8pm) note:* **NRG $105C Dec18** entered at Wednesday's closing ask (doc `week-09/research/research_NRG_paper.md`, Five-Baxter vote 3-2, Bearxter against on two straight EPS misses behind the slide, Macxter against as the third AI-power/capex name with FSLR and AVGO). Picked over the $100C on spread (13.5% vs 20%; the extra spread eats most of the $100C's R6 edge). R1 0.067; R6 passes thin (+12.32% vs 13.44%); R4 has the book's clearest floor this week: Jefferies Buy $131, cut after the slide, $18.90 over BE. EVENING 1's Siebert Williams Shank $184 turned out to be a Jul 6 initiation (stale), not used. First power producer in the book.

*EVENING 1 (Thu Oct 29, 6pm) CAVA date fix:* `get_earnings_results` now says Q3 **Wed Nov 4 PM, `verified: true`**, `actual: null` (the entry row had Tue Nov 3 PM unverified). The ramp sell moves **Mon Nov 2 3:35pm -> Wed Nov 4 3:35pm** (last trading run before the after-close print). Thursday's +9.1% ($59.19) is not a print: the quarter is unreported. One search found only last quarter's "jumps 9% after earnings beat" story, so the cause is still unread. Stock $59.19 is now over the $57.55 BE; the $80 pre-earnings target is far.

*CAVA note: the doc's $55C failed R6 at the open (BE $60.10 vs max $59.36, stock -2.1%); the $52.5C isn't listed for Dec18, so the entry is the one-strike-ITM $50C. Docs: `week-09/research/research_BABA_paper.md`, `research_CAVA_paper.md` (Oct 12 OPEN addenda).*

*TMUS note (Oct 12 MIDDAY): parked since the Oct 9 -13% day because no Buy target had been published after the drop. Raymond James upgraded to Outperform $170 this morning (MarketBeat; one web search did not independently confirm it). R6 margin is thin: needs +7.85% vs the 8.95% cap. No paper doc yet; EVENING 2 writes `research_TMUS_paper.md` (drop cause, Five-Baxter meeting, EXIT PLAN). Log: `week-09/research/screening_log_oct12_midday.md`.*

*EVENING 2 (Mon Oct 12, 8pm) notes:* **TMUS** doc written: `week-09/research/research_TMUS_paper.md` (drop cause read: SpaceX's ~$8B purchase of Grain Management's 800 MHz spectrum, Oct 9, sector-wide; Five-Baxter vote 4-1 hold, Bearxter wanted out on the single-sourced $170 floor; tool low $169 is stamped Oct 8, pre-drop). **APP** competitor headline read (Meta bidding harder on in-game inventory, Unity ruling, CloudX); addendum in `research_APP_paper.md`, Rule 4 holds. **LVS** tool date moved Oct 21 PM (f) -> **Oct 26 PM (f)**; Sands hasn't announced (one search). Paper ramp sell **held at Tue Oct 20 3:35pm** (an Oct 21-22 print stays plausible until Sands announces; LY Oct 22). Still no docs for the Oct 9 paper entries BA, CMG, LVS (entered on the 1:35pm Oct 9 start-up run); EVENING 3 or Saturday.

*EVENING 2 (Tue Oct 13, 8pm) notes:* the three owed docs are written: `week-09/research/research_BA_paper.md`, `research_CMG_paper.md`, `research_LVS_paper.md` (decline cause, Five-Baxter meeting, EXIT PLAN each). Re-measured at the close, **BA and CMG no longer pass R6** (BA needs +8.69% vs 6.85%, CMG +11.96% vs 11.65%); R6 is an entry test, so both stay open to their ramp sells. LVS passes every rule tonight. BA's tool low $206 (owner unidentified, $3.30 over BE) is treated as the floor until identified. CMG has an unread "unconfirmed deal talk" headline (calls: flag, not kill). LVS's 14,115-contract day is still unexplained. Votes: BA 4-1 hold (Bearxter out on R6), CMG 5-0, LVS 5-0.

*EVENING 3 (Tue Oct 13, 10pm) notes:* **BURL** entered (doc `week-09/research/research_BURL_paper.md`, Five-Baxter vote 4-1, Bearxter against on the undated $290 floor). The EVENING 2 park was Barclays' $254: one search showed it is a May 12 2025 Overweight cut, since raised, so not a current target. R1 0.241, R6 +9.60% vs 10.89%, R7 OI 386 / 14.4%. Theta -$0.16/day over 28 trading days to the Nov 23 ramp sell is the cost of entering early; this is the first paper entry that tests it on a Dec expiry this far out. **CMG** deal-talk headline: one search found nothing (only catering-rollout and Q3-date items); stays a flag.

*EVENING 2 (Wed Oct 14, 8pm) notes:* **PAAS $40C Jan15** doc written (`week-09/research/research_PAAS_paper.md`, Five-Baxter vote 4-1, Bearxter against: a silver miner coming off a Q2 miss). R2 Nov 4 PM verified (LY Nov 12; no Dec18 chain, so Jan15), R3 7/2/0, R4 dated RBC Buy $56 (Oct 14) over BE $45.30 (tool low $51), R6 +7.02% vs 9.48%, R7 OI 5,369 / 9.9%. **No entry tonight:** R1 is 0.251 at the $42.33 close, a hair over 0.25. Thursday's OPEN enters it at the live ask if the stock is <= $42.31 and R6/R7 re-pass; ramp sell would be Wed Nov 4 3:35pm. **TTWO** still parked on R4 (Argus: one search shows Buy $284 undated; the Oct 7 $192 neither confirmed nor ruled out). First commodity name in the book.

*EVENING 1 (Fri Oct 23, 6pm) note:* **PAAS $40C Jan15** entered at Friday's closing ask (doc `week-09/research/research_PAAS_paper.md`, Oct 14 vote 4-1, addendum tonight). The Oct 22 park on "undated floor" was wrong: the doc already had RBC Buy $56 dated Oct 14. R6 passes by $0.03. First precious-metals name in the book. **TMUS** drop read: SpaceX is reportedly negotiating access to ~80,000 US tower sites for a fourth wireless network (Bloomberg via Forbes/Benzinga/Fool, Oct 23); TMUS -7.7%, T -8%, VZ -1.2%. Same driver as the Oct 9 drop the entry was built on, now bigger. Tool ratings unchanged (27/4/0, low $169 vs BE $165.20), RJ $170 still the dated floor, so Rule 4 holds and the paper ramp sell Tue Oct 27 3:35pm stands. Any Buy target cut under $165.20 Monday = same-run paper exit.

*EVENING 2 (Fri Oct 23, 8pm) note:* **CDE $12.5C Jan15** doc written (`week-09/research/research_CDE_paper.md`), **no entry**: R1 -0.006 (52-week low), R2 Nov 4 PM verified, R3 10/3/0, R6 passes by $0.40 (BE $14.75 at the $2.25 closing ask vs line $15.15), R7 OI 4,597 / 11.8%. R4 rests on the tool's undated, unowned $18 low; two searches found only undated moves, two of them downgrades (Cantor to Hold, Cormark to Market Perform). Tab 6 gate: entry the first evening run that finds a dated post-slide Buy above $14.75. Vote 3-2 to hold. Driver bucket: precious metals, which would make two names with PAAS ($615 at the asks); the correlation proposal still waits on a local session. Holdings unchanged: PAAS and TMUS floors hold (tool lows $51 and $169).

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

**Marks (WRAP Tue Oct 13, close, at the bid; quotes 3:59pm ET):**

| Contract | Bid / ask | Stock | Paper P&L at bid | Rule 4 low vs BE | Ramp-sell deadline |
|---|---|---|---|---|---|
| BA $195C Nov20 | 5.25 / 5.40 (OI 1,495, vol 220) | $186.54 (-1.6%) | **-$245** | $240 vs $202.70, holds (tool low $206, stamp Oct 3, unchanged) | Mon Oct 26 3:35pm |
| CMG $32.5C Nov20 | 0.97 / 1.06 (OI 5,653) | $30.365 (-0.1%) | **-$51** | $35 vs $33.98, holds (stamp Oct 12 14:30 UTC) | Wed Oct 28 3:35pm |
| LVS $37.5C Nov20 | 1.50 / 1.71 (OI 2,258, vol 14,115) | $37.04 (+2.5%) | **+$15** | $47 vs $38.85, holds | **Tue Oct 20 3:35pm** (nearest; tool still Oct 26 PM (f), LY Oct 22) |
| FSLR $175C Nov20 | 19.20 / 21.00 (OI 269) | $186.61 (+3.8%) | **+$270** | Evercore $218 (ages out Oct 16) / Piper $251 vs $191.50, holds | Wed Oct 28 3:35pm |
| APP $290C Dec18 | 23.80 / 27.80 (OI 447) | $272.14 (+0.5%) | **-$360** | Jefferies $375 vs $317.40, holds | Wed Nov 4 3:35pm |
| BABA $110C Dec18 | 8.65 / 9.00 (OI 8,952) | $110.85 (+0.1%) | **+$10** | Baird $160 vs $118.55, holds | Mon Nov 23 3:35pm |
| CAVA $50C Dec18 | 6.85 / 8.15 (OI 451) | $52.985 (+0.8%) | **-$70** | JPM $80 vs $57.55, holds | Mon Nov 2 3:35pm |
| TMUS $160C Nov20 | 4.80 / 5.10 (OI 556) | $153.74 (+1.2%) | **-$40** | RJ $170 (tool low $169) vs $165.20, holds | Tue Oct 27 3:35pm |

Paper book at the bid: **-$471** on $7,573 (-6.2%), up $624 from Monday. FSLR (+3.8%) is the first paper position with real profit: $186.61 is past the $175 strike and $4.89 short of breakeven, nowhere near the ladder (+150% for one contract). LVS's volume (14,115 against 2,258 OI) came with a +2.5% stock day and a 32% move in the mark; whatever it was, it's flow, not a print, since Q3 is still unreported. APP's $4.00 spread is still the biggest single cost in the book. BA is the one that moved against us (-1.6%, $16 under breakeven). No Rule 4 breach. Nothing hits a ladder or a deadline before LVS on Tue Oct 20.

**Marks (WRAP Wed Oct 14, close, at the bid; quotes 3:59pm ET):**

| Contract | Bid / ask | Stock | Paper P&L at bid | Rule 4 low vs BE | Ramp-sell deadline |
|---|---|---|---|---|---|
| BA $195C Nov20 | 4.20 / 4.85 (OI 1,570, vol 242) | $184.60 (-1.0%) | **-$350** | $240 vs $202.70, holds (tool low $206, stamp Oct 3, unchanged) | Mon Oct 26 3:35pm |
| CMG $32.5C Nov20 | 0.97 / 1.19 (OI 5,873, vol 1,024) | $30.515 (+0.5%) | **-$51** | $35 vs $33.98, holds (stamp Oct 12 14:30 UTC) | Wed Oct 28 3:35pm |
| LVS $37.5C Nov20 | 1.56 / 1.69 (OI 16,308, vol 214) | $37.02 (-0.1%) | **+$21** | $47 vs $38.85, holds (tool low reads $40, stamp Oct 3, also above BE) | **Tue Oct 20 3:35pm** (nearest; tool still Oct 26 PM (f), LY Oct 22) |
| FSLR $175C Nov20 | 14.35 / 17.85 (OI 250) | $179.01 (-4.1%) | **-$215** | Evercore $218 (ages out Oct 16) / Piper $251 vs $191.50, holds | Wed Oct 28 3:35pm |
| APP $290C Dec18 | 18.80 / 22.50 (OI 445) | $262.11 (-3.7%) | **-$860** | Jefferies $375 vs $317.40, holds (tool $325 also above) | Wed Nov 4 3:35pm |
| BABA $110C Dec18 | 8.75 / 9.50 (OI 8,914) | $111.18 (+0.3%) | **+$20** | Baird $160 vs $118.55, holds (tool $140.59) | Mon Nov 23 3:35pm |
| CAVA $50C Dec18 | 6.10 / 6.75 (OI 451, vol 0) | $51.59 (-2.6%) | **-$145** | JPM $80 vs $57.55, holds (tool $58) | Mon Nov 2 3:35pm |
| TMUS $160C Nov20 | 6.00 / 7.70 (OI 501, vol 278) | $157.88 (+2.7%) | **+$80** | RJ $170 (tool low $169) vs $165.20, holds | Tue Oct 27 3:35pm |
| BURL $270C Dec18 | 17.20 / 19.50 (OI 386) | $263.20 (-0.0%) | **-$140** | Tool $290 vs $288.60, holds ($1.40 margin); Bernstein $355 / BofA $365 | Mon Nov 23 3:35pm |

Paper book at the bid: **-$1,640** on $9,433 (-17.4%). Like-for-like with Tuesday (-$471 on the first eight, plus BURL's -$250 entry spread = -$721), today cost **$919**. APP is half of it: the stock fell $10 (-3.7%) and the call lost $500 at the bid on the day, with the spread still $3.70 wide. BA (-$105 on the day) and FSLR (-$485 on the day, -4.1%, back under its breakeven path after Tuesday's +$270) are the rest. TMUS is the bright spot (+2.7%, now $7.32 under its $165.20 breakeven, +$120 on the day). No Rule 4 breach anywhere. Nothing hits the +150% ladder. The first paper deadline is still LVS, Tue Oct 20 3:35pm; the run that day closes it at the bid unless Sands announces a later date first.

**Marks (WRAP Thu Oct 15, close, at the bid; quotes 3:59pm ET):**

| Contract | Bid / ask | Stock | Paper P&L at bid | Rule 4 low vs BE | Ramp-sell deadline |
|---|---|---|---|---|---|
| BA $195C Nov20 | 5.65 / 6.00 (OI 1,693, vol 208) | $188.705 (+2.2%) | **-$205** | $240 vs $202.70, holds (tool low $206, stamp Oct 3, unchanged) | Mon Oct 26 3:35pm |
| CMG $32.5C Nov20 | 0.98 / 1.10 (OI 6,168, vol 425) | $30.56 (+0.1%) | **-$50** | $35 vs $33.98, holds (stamp Oct 12 14:30 UTC) | Wed Oct 28 3:35pm |
| LVS $37.5C Nov20 | 2.17 / 2.36 (OI 16,383, vol 651) | $38.315 (+3.5%) | **+$82** | $47 vs $38.85, holds (tool low $40, also above BE) | **Tue Oct 20 3:35pm** (Q3 now **Oct 21 PM, verified: true**, was Oct 26 (f); deadline confirmed) |
| FSLR $175C Nov20 | 13.80 / 16.35 (OI 262, vol 8) | $178.79 (-0.2%) | **-$270** | Evercore $218 (ages out Oct 16) / Piper $251 vs $191.50, holds (tool $197 is the Bernstein Sell) | Wed Oct 28 3:35pm |
| APP $290C Dec18 | 24.50 / 29.00 (OI 452, vol 69) | $279.20 (+6.5%) | **-$290** | Jefferies $375 vs $317.40, holds (tool $325) | Wed Nov 4 3:35pm |
| BABA $110C Dec18 | 8.55 / 8.85 (OI 8,609) | $111.11 (-0.1%) | **$0** | Baird $160 vs $118.55, holds (tool $140.59) | Mon Nov 23 3:35pm |
| CAVA $50C Dec18 | 8.50 / 9.00 (OI 451, vol 70) | $55.42 (+7.4%) | **+$95** | JPM $80 vs $57.55, holds (tool $58) | Mon Nov 2 3:35pm |
| TMUS $160C Nov20 | 5.80 / 7.50 (OI 555, vol 81) | $157.01 (-0.5%) | **+$60** | RJ $170 (tool low $169) vs $165.20, holds | Tue Oct 27 3:35pm |
| BURL $270C Dec18 | 17.90 / 20.60 (OI 387) | $267.63 (+1.7%) | **-$70** | Tool $290 vs $288.60, holds ($1.40 margin); Bernstein $355 / BofA $365 | Mon Nov 23 3:35pm |

Paper book at the bid: **-$648** on $9,433 (-6.9%), up **$992** from Wednesday's -$1,640. APP got back $570 of it (+6.5%, though its closing spread is $4.50 wide, so the bid understates it), CAVA turned green (+$240 on the day, +7.4%, $2.13 under breakeven), BA +$145, LVS +$61. FSLR is the laggard (-$55 on the day, closing spread 17%). No Rule 4 breach, nothing near the +150% ladder (LVS is the best at +61% at the bid). **LVS:** Sands confirmed Q3 for **Wed Oct 21 PM** (`verified: true`), so the paper ramp sell is Tue Oct 20 3:35pm for real now. The stock closed $0.815 over the $37.50 strike, so on Tuesday the Tab 4 question is ITM-or-not: if it's still in the money that run, holding through the print is allowed (Tab 4), and that run writes the hold-vs-sell call; if it's OTM, it's sold at the bid.

**Marks (WRAP Fri Oct 16, close, at the bid; quotes 3:59pm ET):**

| Contract | Bid / ask | Stock | Paper P&L at bid | Rule 4 low vs BE | Ramp-sell deadline |
|---|---|---|---|---|---|
| BA $195C Nov20 | 6.30 / 6.70 (OI 1,730, vol 596) | $190.04 (+0.7%) | **-$140** | $240 vs $202.70, holds (tool low $206, stamp Oct 3) | Mon Oct 26 3:35pm |
| CMG $32.5C Nov20 | 0.70 / 0.79 (OI 6,356, vol 880) | $29.88 (-2.3%) | **-$78** | $35 vs $33.98, holds (stamp Oct 12) | Wed Oct 28 3:35pm |
| LVS $37.5C Nov20 | 1.94 / 2.30 (OI 16,268, vol 11) | $38.01 (-0.8%) | **+$59** | $47 vs $38.85, holds (tool low $40, also above BE) | **Tue Oct 20 3:35pm** (Q3 Wed Oct 21 PM, `verified: true`, re-checked tonight) |
| FSLR $175C Nov20 | 11.45 / 13.30 (OI 262, vol 5) | $172.64 (-3.5%) | **-$505** | Evercore $218 aged out today (Aug 17 + 60); Piper $251 (Sep 30) vs $191.50, holds | Wed Oct 28 3:35pm |
| APP $290C Dec18 | 19.00 / 23.50 (OI 412, vol 58) | $266.26 (-4.7%) | **-$840** | Jefferies $375 vs $317.40, holds (tool $325) | Wed Nov 4 3:35pm |
| BABA $110C Dec18 | 7.35 / 7.65 (OI 8,618) | $109.10 (-1.8%) | **-$120** | Baird $160 (ages out Oct 20) vs $118.55, holds (tool $140.59) | Mon Nov 23 3:35pm |
| CAVA $50C Dec18 | 9.55 / 10.60 (OI 481, vol 25) | $57.25 (+3.3%) | **+$200** | JPM $80 vs $57.55, holds (tool $58) | Mon Nov 2 3:35pm |
| TMUS $160C Nov20 | 6.30 / 7.50 (OI 522, vol 104) | $159.03 (+1.3%) | **+$110** | RJ $170 (tool low $169) vs $165.20, holds | Tue Oct 27 3:35pm |
| BURL $270C Dec18 | 15.30 / 18.00 (OI 384) | $262.45 (-2.0%) | **-$330** | Tool $290 vs $288.60, holds ($1.40 margin); Bernstein $355 / BofA $365 | Mon Nov 23 3:35pm |

Paper book at the bid: **-$1,644** on $9,433 (-17.4%), down **$996** from Thursday's -$648, back to Wednesday's level. APP is more than half of it again (-$550 on the day, stock -4.7%, and its closing spread is $4.50 wide so the bid overstates the damage), then BURL (-$260) and FSLR (-$235, stock -3.5%). CAVA is now $0.30 from breakeven at the stock and +$200 at the bid, the best in the book; TMUS and BA were green too. No Rule 4 breach. Nothing near the +150% ladder (CAVA is +26% at the bid). FSLR's floor of record is now Piper $251 only (Evercore $218 aged out today). **LVS on Tuesday:** the stock closed $0.51 over the $37.50 strike; Tue Oct 20 3:35pm closes it at the bid if it's OTM, and writes the ITM hold-vs-sell call if it's ITM.

**Marks (WRAP Mon Oct 19, close, at the bid; quotes 3:59pm ET):**

| Contract | Bid / ask | Stock | Paper P&L at bid | Rule 4 low vs BE | Ramp-sell deadline |
|---|---|---|---|---|---|
| BA $195C Nov20 | 6.55 / 7.40 (OI 2,011, vol 221) | $191.51 (+0.7%) | **-$115, CLOSED** | **Tool low now $195 (was $206; stamp still Oct 3) vs $202.70: BREACH** under the doc's own trigger | closed |
| CMG $32.5C Nov20 | 0.64 / 0.74 (OI 6,902, vol 130) | $29.84 (-0.2%) | **-$84** | $35 vs $33.98, holds (stamp Oct 12) | Wed Oct 28 3:35pm |
| LVS $37.5C Nov20 | 1.90 / 2.12 (OI 16,263, vol 1) | $38.005 (0.0%) | **+$55** | $47 vs $38.85, holds (tool low $40) | **Tue Oct 20 3:35pm (tomorrow)**; Q3 Wed Oct 21 PM `verified: true`, re-checked |
| FSLR $175C Nov20 | 10.75 / 11.40 (OI 264, vol 5) | $171.80 (-0.5%) | **-$575** | Piper $251 (Sep 30) vs $191.50, holds | Wed Oct 28 3:35pm |
| APP $290C Dec18 | 19.20 / 24.00 (OI 369, vol 73) | $268.985 (+1.1%) | **-$820** | Jefferies $375 vs $317.40, holds (tool $325) | Wed Nov 4 3:35pm |
| BABA $110C Dec18 | 6.80 / 7.00 (OI 8,782, vol 182) | $108.53 (-0.5%) | **-$175** | Baird $160 (ages out Oct 20) / Bernstein $165 (Sep 7) vs $118.55, holds (tool $140.60) | Mon Nov 23 3:35pm |
| CAVA $50C Dec18 | 9.50 / 10.90 (OI 465, vol 0) | $57.885 (+1.1%) | **+$195** | JPM $80 vs $57.55, holds (tool $58) | Mon Nov 2 3:35pm |
| TMUS $160C Nov20 | 5.10 / 5.60 (OI 521, vol 55) | $156.10 (-1.9%) | **-$10** | RJ $170 (tool low $169) vs $165.20, holds | Tue Oct 27 3:35pm |
| BURL $270C Dec18 | 15.90 / 18.00 (OI 385, vol 7) | $262.74 (+0.0%) | **-$270** | Tool $290 vs $288.60, holds ($1.40 margin) | Mon Nov 23 3:35pm |
| AVGO $280C Jan15 | 62.85 / 65.50 (OI 874, vol 5) | $334.64 (+1.8%) | **+$195** | Tool $350 vs $340.90, holds | Wed Dec 9 3:35pm |

Paper book at the bid: **-$1,604** on $15,523 (-10.3%), including BA's realized -$115. Like-for-like with Friday's close (all ten, AVGO at Friday's 58.90 bid = -$1,844), today made **$240**, and AVGO (+1.8%, +$395 on the day) is all of it and more; TMUS gave back $120 (-1.9%), FSLR $70, BABA $55. **BA closed** at the $6.55 bid: `research_BA_paper.md` set the trigger on Oct 13 ("if the tool's low drops below $202.70, the paper position closes at that run's bid"), and the low read $195 tonight. The tool's stamp didn't move (still Oct 3), so the change may be a data refresh rather than a new cut; the rule doesn't ask why. **LVS tomorrow:** the stock closed $0.505 over the $37.50 strike; Tue 3:35pm closes it at the bid if OTM, or writes the ITM hold-vs-sell call if ITM.

**Marks (WRAP Tue Oct 20, close, at the bid; quotes 3:59pm ET):**

| Contract | Bid / ask | Stock | Paper P&L at bid | Rule 4 low vs BE | Ramp-sell deadline |
|---|---|---|---|---|---|
| CMG $32.5C Nov20 | 0.58 / 0.65 (OI 6,935, vol 109) | $29.655 (-0.7%) | **-$90** | $35 vs $33.98, holds (stamp Oct 12) | Wed Oct 28 3:35pm |
| FSLR $175C Nov20 | 12.00 / 12.35 (OI 267, vol 69) | $174.43 (+1.5%) | **-$450** | Piper $251 (Sep 30) vs $191.50, holds (tool $197 is the Bernstein Sell) | Wed Oct 28 3:35pm |
| APP $290C Dec18 | 22.80 / 27.10 (OI 312, vol 89) | $272.48 (+1.2%) | **-$460** | Jefferies $375 vs $317.40, holds (tool $325) | Wed Nov 4 3:35pm |
| BABA $110C Dec18 | 6.90 / 7.15 (OI 8,858, vol 318) | $108.67 (+0.1%) | **-$165** | Baird $160 ages out today; Bernstein $165 (Sep 7) vs $118.55, holds (tool $140.69) | Mon Nov 23 3:35pm |
| CAVA $50C Dec18 | 8.95 / 11.55 (OI 465, vol 0) | $57.46 (-0.8%) | **+$140** | JPM $80 vs $57.55, holds (tool $58, $0.45 over BE) | Mon Nov 2 3:35pm |
| TMUS $160C Nov20 | 5.20 / 6.70 (OI 523, vol 49) | $157.76 (+1.1%) | **$0** | RJ $170 (tool low $169) vs $165.20, holds | Tue Oct 27 3:35pm |
| BURL $270C Dec18 | 13.30 / 15.80 (OI 390, vol 212) | $258.83 (-1.5%) | **-$530** | Tool $290 vs $288.60, holds ($1.40 margin) | Mon Nov 23 3:35pm |
| AVGO $280C Jan15 | 62.35 / 64.75 (OI 873, vol 4) | $334.51 (0.0%) | **+$145** | Tool $350 vs $340.90, holds | Wed Dec 9 3:35pm |
| MSTR $120C Nov20 | 26.10 / 26.40 (OI 1,764, vol 11) | $142.72 (+4.9%) | **+$405** | Tool $165 / Barclays $175 vs $142.05, holds | Thu Oct 29 3:35pm |

Paper book at the bid: open **-$1,005**, plus realized BA -$115 and LVS +$52 = **-$1,068** on $17,728 ever deployed (-6.0%). Like-for-like with Monday's close (MSTR at its $20.35 entry-night bid, LVS at today's close price), today made **$706**: MSTR +$575 (stock +4.9%, already through its $142.05 BE), APP +$360, FSLR +$125; BURL gave back $260 (-1.5%). MSTR at +18.4% is nowhere near the +150% single-contract line. No paper ramp deadline tomorrow; nearest is TMUS Tue Oct 27. BABA's Baird $160 ages out of the 60-day window today; Bernstein $165 (Sep 7) is the floor of record now.

**Marks (WRAP Wed Oct 21, close, at the bid; quotes 3:59pm ET):**

| Contract | Bid / ask | Stock | Paper P&L at bid | Rule 4 low vs BE | Ramp-sell deadline |
|---|---|---|---|---|---|
| ~~CMG $32.5C Nov20~~ | 0.25 / 0.37 (OI 6,960, vol 139) | $28.095 (-5.2%) | **-$123, CLOSED** | **Tool low $32 vs $33.98: BREACH** (was $35; Buys 27 -> 26, Holds 12 -> 13; stamp still reads Oct 12) | closed |
| FSLR $175C Nov20 | 11.80 / 13.20 (OI 281, vol 59) | $174.75 (+0.2%) | **-$470** | Piper $251 (Sep 30) vs $191.50, holds (tool $197 is the Bernstein Sell) | Wed Oct 28 3:35pm |
| APP $290C Dec18 | 20.60 / 24.00 (OI 290, vol 84) | $267.90 (-1.7%) | **-$680** | Jefferies $375 vs $317.40, holds (tool $325) | Wed Nov 4 3:35pm |
| BABA $110C Dec18 | 4.90 / 5.05 (OI 8,888, vol 628) | $104.39 (-3.9%) | **-$365** | Bernstein $165 (Sep 7) vs $118.55, holds (tool $140.76) | Mon Nov 23 3:35pm |
| CAVA $50C Dec18 | 7.75 / 9.10 (OI 465, vol 0) | $55.015 (-4.2%) | **+$20** | JPM $80 vs $57.55, holds (tool $58, $0.45 over BE) | Mon Nov 2 3:35pm |
| TMUS $160C Nov20 | 4.00 / 4.60 (OI 528, vol 22) | $153.76 (-2.5%) | **-$120** | RJ $170 (tool low $169) vs $165.20, holds | Tue Oct 27 3:35pm |
| BURL $270C Dec18 | 10.00 / 11.80 (OI 266, vol 3) | $248.09 (-4.2%) | **-$860** | Tool $290 vs $288.60, holds ($1.40 margin) | Mon Nov 23 3:35pm |
| AVGO $280C Jan15 | 66.05 / 68.15 (OI 876, vol 27) | $337.68 (+1.0%) | **+$515** | Tool $350 vs $340.90, holds | Wed Dec 9 3:35pm |
| MSTR $120C Nov20 | 34.50 / 37.75 (OI 1,755, vol 70) | $153.355 (+7.5%) | **+$1,245** | Tool $165 / Barclays $175 vs $142.05, holds | Thu Oct 29 3:35pm |

Paper book at the bid: open **-$715** on 8 positions, plus realized BA -$115, LVS +$52, CMG -$123 = **-$901** on $17,728 ever deployed (-5.1%). Today made **$167** like-for-like (CMG counted at its close): MSTR +$840 and AVGO +$370 against BURL -$330, APP -$220, BABA -$200, CAVA -$120, TMUS -$120. MSTR is +56.5% at the bid, short of the +150% single-contract line ($55.13), and the stock ($153.36) is still under the $165 floor, so no pre-earnings target fires. BURL's R7 is slipping (OI 266, closing spread 16.5%); it's an entry test, so it stays open. No paper ramp deadline in the next two trading days; nearest is TMUS Tue Oct 27.

**Marks (WRAP Thu Oct 22, close, at the bid; quotes 3:59pm ET):**

| Contract | Bid / ask | Stock | Paper P&L at bid | Rule 4 low vs BE | Ramp-sell deadline |
|---|---|---|---|---|---|
| FSLR $175C Nov20 | 10.50 / 11.30 (OI 337, vol 96) | $171.12 (-2.1%) | **-$600** | Piper $251 (Sep 30) vs $191.50, holds (tool $197 is the Bernstein Sell) | Wed Oct 28 3:35pm |
| APP $290C Dec18 | 16.90 / 23.40 (OI 294, vol 73) | $264.35 (-1.3%) | **-$1,050** | Jefferies $375 vs $317.40, holds (tool $325) | Wed Nov 4 3:35pm |
| BABA $110C Dec18 | 3.90 / 4.15 (OI 9,136, vol 452) | $101.815 (-2.5%) | **-$465** | Bernstein $165 (Sep 7) vs $118.55, holds (tool $140.88) | Mon Nov 23 3:35pm |
| CAVA $50C Dec18 | 7.05 / 9.00 (OI 465, vol 0) | $54.67 (-0.6%) | **-$50** | JPM $80 vs $57.55, holds (tool $58, $0.45 over BE) | Mon Nov 2 3:35pm |
| TMUS $160C Nov20 | 4.80 / 6.90 (OI 534, vol 116) | $158.81 (+3.3%) | **-$40** | RJ $170 (tool low $169) vs $165.20, holds | **Tue Oct 27 3:35pm** |
| BURL $270C Dec18 | 12.50 / 13.40 (OI 266, vol 2) | $252.67 (+1.8%) | **-$610** | Tool $290 vs $288.60, holds ($1.40 margin) | Mon Nov 23 3:35pm |
| AVGO $280C Jan15 | 54.25 / 56.15 (OI 888, vol 7) | $323.34 (-4.3%) | **-$665** | Tool $350 vs $340.90, holds | Wed Dec 9 3:35pm |
| MSTR $120C Nov20 | 28.40 / 29.75 (OI 1,798, vol 17) | $145.88 (-5.0%) | **+$635** | Tool $165 / Barclays $175 vs $142.05, holds | Thu Oct 29 3:35pm |
| NRG $105C Dec18 | 4.00 / 4.50 (OI 511, vol 2) | $94.32 (-5.5%) | **-$310** | Tool $131 (Jefferies) vs $112.10, holds | Wed Nov 4 3:35pm |

Paper book at the bid: open **-$3,155** on 9 positions, plus realized BA -$115, LVS +$52, CMG -$123 = **-$3,341** on $18,438 ever deployed (-18.1%). Today lost **$2,350** like-for-like (NRG counted from its $6.20 entry-night bid): AVGO -$1,180 (stock -4.3%, the deep-ITM shape takes the stock's move nearly dollar for dollar), MSTR -$610, APP -$370 (closing spread blew out to 32% of mid), NRG -$220 (-5.5% on its first full day), FSLR -$130, BABA -$100, CAVA -$70, against BURL +$250 and TMUS +$80. A broad AI/power/crypto down day: AVGO, NRG, MSTR and FSLR are four of the five worst lines, and that's Macxter's correlation objection from the NRG meeting showing up on day one. No Rule 4 floor moved on any of the nine. MSTR is +28.8% at the bid, nowhere near the +150% line. Next paper ramp deadline: **TMUS Tue Oct 27 3:35pm**, then FSLR Wed Oct 28, MSTR Thu Oct 29. Nothing due in the next two trading days.

**Marks (WRAP Fri Oct 23, close, at the bid; quotes 3:59pm ET):**

| Contract | Bid / ask | Stock | Paper P&L at bid | Rule 4 low vs BE | Ramp-sell deadline |
|---|---|---|---|---|---|
| FSLR $175C Nov20 | 9.50 / 12.20 (OI 341, vol 113) | $171.99 (+0.4%) | **-$700** | Piper $251 (Sep 30) vs $191.50, holds (tool $197 is the Bernstein Sell) | Wed Oct 28 3:35pm |
| APP $290C Dec18 | 15.50 / 21.80 (OI 295, vol 15) | $260.18 (-1.6%) | **-$1,190** | Jefferies $375 vs $317.40, holds (tool $325) | Wed Nov 4 3:35pm |
| BABA $110C Dec18 | 3.20 / 3.35 (OI 9,151, vol 598) | $99.63 (-2.2%) | **-$535** | Bernstein $165 (Sep 7) vs $118.55, holds (tool $140.88) | Mon Nov 23 3:35pm |
| CAVA $50C Dec18 | 6.75 / 7.55 (OI 465, vol 1) | $53.51 (-2.1%) | **-$80** | JPM $80 vs $57.55, holds (tool $58, $0.45 over BE) | Mon Nov 2 3:35pm |
| TMUS $160C Nov20 | 2.20 / 2.35 (OI 587, vol 50) | **$146.61 (-7.7%)** | **-$300** | RJ $170 (tool low $169, 27/4/0, unchanged) vs $165.20, holds | **Tue Oct 27 3:35pm** |
| BURL $270C Dec18 | 8.00 / 10.60 (OI 267, vol 1) | $247.52 (-2.0%) | **-$1,060** | Tool $290 vs $288.60, holds ($1.40 margin) | Mon Nov 23 3:35pm |
| AVGO $280C Jan15 | 52.60 / 54.65 (OI 888, vol 32) | $321.73 (-0.5%) | **-$830** | Tool $350 vs $340.90, holds | Wed Dec 9 3:35pm |
| MSTR $120C Nov20 | 28.65 / 29.45 (OI 1,801, vol 64) | $146.04 (+0.2%) | **+$660** | Tool $165 / Barclays $175 vs $142.05, holds | Thu Oct 29 3:35pm |
| NRG $105C Dec18 | 3.20 / 4.00 (OI 513, vol 14) | $92.315 (-2.2%) | **-$390** | Tool $131 (Jefferies; 17/4/0, one Buy added) vs $112.10, holds | Wed Nov 4 3:35pm |

Paper book at the bid: open **-$4,425** on 9 positions, plus realized BA -$115, LVS +$52, CMG -$123 = **-$4,611** on $18,438 ever deployed (-25.0%). Today lost **$1,270**: BURL -$450 (stock -2.0%, and the closing spread opened to 28% of mid, so the bid overstates it), TMUS -$260, AVGO -$165, APP -$140 (closing spread 34% of mid again), FSLR -$100, NRG -$80, BABA -$70, CAVA -$30; MSTR +$25. **TMUS fell 7.7% ($158.79 -> $146.61) with its print five days out** (Wed Oct 28 PM, verified, `actual: null`); the tool's ratings didn't move (27/4/0, low $169), so Rule 4 holds on paper, but the cause is unread (daytime runs don't search) and the stock is now 12.7% under the $165.20 BE against an 8.95% R6 cap. EVENING 1 should read the drop before Tuesday's 3:35pm ramp sell. No Rule 4 floor moved on any of the nine. Next paper ramp deadline: **TMUS Tue Oct 27 3:35pm**, then FSLR Wed Oct 28, MSTR Thu Oct 29.

**Marks (WRAP Thu Oct 29, close, at the bid; quotes 3:59pm ET):**

| Contract | Bid / ask | Stock | Paper P&L at bid | Rule 4 low vs BE | Ramp-sell deadline |
|---|---|---|---|---|---|
| APP $290C Dec18 | 11.80 / 19.50 (OI 325, vol 7) | $254.91 (-1.9%) | **-$1,560** | Jefferies $375 vs $317.40, holds (tool $325, 32/7/0) | Wed Nov 4 3:35pm |
| BABA $110C Dec18 | 2.87 / 2.96 (OI 8,953, vol 467) | $99.515 (-1.4%) | **-$568** | Bernstein $165 (Sep 7) vs $118.55, holds (tool $141.12, 45/1/0) | Mon Nov 23 3:35pm |
| CAVA $50C Dec18 | 10.55 / 11.60 (OI 482, vol 15) | $59.19 (+9.1%) | **+$300** | JPM $80 vs $57.55, holds (tool $58, 20/9/1) | **Mon Nov 2 3:35pm** (next) |
| BURL $270C Dec18 | 8.30 / 9.70 (OI 269, vol 3) | $242.31 (+3.5%) | **-$1,030** | Tool $290 vs $288.60, holds ($1.40 margin; 16/5/0) | Mon Nov 23 3:35pm |
| AVGO $280C Jan15 | 70.95 / 74.55 (OI 871, vol 30) | $345.05 (-1.9%) | **+$1,005** | Tool $400 (53/2/0) vs $340.90, holds | Wed Dec 9 3:35pm |
| NRG $105C Dec18 | 4.50 / 5.00 (OI 497, vol 0) | $97.53 (+0.6%) | **-$260** | Tool $131 (17/4/0) vs $112.10, holds | Wed Nov 4 3:35pm |
| PAAS $40C Jan15 | 3.70 / 4.00 (OI 6,346, vol 16) | $40.745 (-2.9%) | **-$20** | RBC $56 (Oct 14) vs $43.90, holds (tool $51, 6/2/0) | Wed Nov 4 3:35pm |

Paper book at the bid: open **-$2,133** on 7 positions, plus realized BA -$115, LVS +$52, CMG -$123, TMUS -$325, FSLR -$515, MSTR +$140 = **-$3,019** on $18,828 ever deployed (-16.0%). Today lost **$933**: AVGO -$620, APP -$450 (its 11.80 / 19.50 closing spread is 49% wide; the bid is the honest mark, and it overstates the move), MSTR -$270 (Wednesday's 26.15 bid to its 23.45 LASTCALL close), PAAS -$60, BABA -$43, NRG -$10; CAVA +$320 (stock +9.1%, cause unread, daytime runs don't search) and BURL +$200. AVGO traded $333.67 after hours (-3.3% vs its close), cause unread; its BE is $340.90 and the tool low $400, so nothing fires, EVENING reads it. No Rule 4 floor moved on any of the seven. CAVA's pre-earnings target ($80) and +150% ladder (~$18.90) are both far. **Next paper ramp sell: CAVA Mon Nov 2 3:35pm.**

**Marks (WRAP Wed Oct 28, close, at the bid; quotes 3:59pm ET):**

| Contract | Bid / ask | Stock | Paper P&L at bid | Rule 4 low vs BE | Ramp-sell deadline |
|---|---|---|---|---|---|
| MSTR $120C Nov20 | 26.15 / 28.70 (OI 1,776, vol 5) | $145.22 (+2.7%) | **+$410** | Tool $165 (20/2/0) / Barclays $175 vs $142.05, holds | **Thu Oct 29 3:35pm** (Q3 Thu Oct 29 PM, `verified: true`, `actual: null`) |
| APP $290C Dec18 | 16.30 / 17.40 (OI 322, vol 16) | $260.21 (-1.0%) | **-$1,110** | Jefferies $375 vs $317.40, holds (tool $325, 32/7/0) | Wed Nov 4 3:35pm |
| BABA $110C Dec18 | 3.30 / 3.50 (OI 8,926, vol 683) | $100.98 (+0.7%) | **-$525** | Bernstein $165 (Sep 7) vs $118.55, holds (tool $141.04, 45/1/0) | Mon Nov 23 3:35pm |
| CAVA $50C Dec18 | 7.35 / 8.20 (OI 482, vol 2) | $54.275 (+4.7%) | **-$20** | JPM $80 vs $57.55, holds (tool $58, $0.45 over BE; 20/9/1) | Mon Nov 2 3:35pm |
| BURL $270C Dec18 | 6.30 / 8.30 (OI 269, vol 3) | $234.08 (-0.5%) | **-$1,230** | Tool $290 vs $288.60, holds ($1.40 margin; 16/5/0) | Mon Nov 23 3:35pm |
| AVGO $280C Jan15 | 77.15 / 79.70 (OI 879, vol 9) | $351.97 (+2.8%) | **+$1,625** | Tool $400 (53/2/0) vs $340.90, holds | Wed Dec 9 3:35pm |
| NRG $105C Dec18 | 4.60 / 5.50 (OI 508, vol 17) | $96.985 (+1.8%) | **-$250** | Tool $131 (17/4/0) vs $112.10, holds | Wed Nov 4 3:35pm |
| PAAS $40C Jan15 | 4.30 / 5.00 (OI 6,347, vol 2) | $41.97 (+0.7%) | **+$40** | RBC $56 (Oct 14) vs $43.90, holds (tool $51, 6/2/0) | Wed Nov 4 3:35pm |

Paper book at the bid: open **-$1,060** on 8 positions, plus realized BA -$115, LVS +$52, CMG -$123, TMUS -$325, FSLR -$515 = **-$2,086** on $18,828 ever deployed (-11.1%). Today made **$1,445** (FSLR counted from Tuesday's 10.70 bid to its 11.35 LASTCALL close, +$65): AVGO +$795 (stock +2.8%, its best mark yet, +26.7% on the contract), CAVA +$160 (stock +4.7%), MSTR +$155, APP +$110, BURL +$60, NRG +$60, BABA +$20, PAAS +$20. Every open line was green. No Rule 4 floor moved on any of the eight. **MSTR ramp sell is tomorrow, Thu Oct 29 3:35pm** (print Thu PM): stock $145.22 is $25.22 over the $120 strike, deep ITM, so LASTCALL writes the hold-vs-sell (default sell, no binary flag). CAVA Mon Nov 2 3:35pm is next after that.

**Marks (WRAP Tue Oct 27, close, at the bid; quotes 3:59pm ET):**

| Contract | Bid / ask | Stock | Paper P&L at bid | Rule 4 low vs BE | Ramp-sell deadline |
|---|---|---|---|---|---|
| FSLR $175C Nov20 | 10.70 / 13.60 (OI 382, vol 64) | $175.82 (+4.6%) | **-$580** | Piper $251 (Sep 30) vs $191.50, holds (tool $197 is the Bernstein Sell; 30/9/1) | **Wed Oct 28 3:35pm** |
| APP $290C Dec18 | 15.20 / 18.90 (OI 301, vol 35) | $262.91 (+0.8%) | **-$1,220** | Jefferies $375 vs $317.40, holds (tool $325) | Wed Nov 4 3:35pm |
| BABA $110C Dec18 | 3.10 / 3.25 (OI 9,331, vol 794) | $100.23 (0.0%) | **-$545** | Bernstein $165 (Sep 7) vs $118.55, holds (tool $141.04) | Mon Nov 23 3:35pm |
| CAVA $50C Dec18 | 5.75 / 6.35 (OI 480, vol 13) | $51.86 (+0.6%) | **-$180** | JPM $80 vs $57.55, holds (tool $58, $0.45 over BE) | Mon Nov 2 3:35pm |
| BURL $270C Dec18 | 5.70 / 7.50 (OI 268, vol 5) | $235.145 (-2.5%) | **-$1,290** | Tool $290 vs $288.60, holds ($1.40 margin; 16/5/0) | Mon Nov 23 3:35pm |
| AVGO $280C Jan15 | 69.20 / 71.20 (OI 883, vol 13) | $342.46 (+4.0%) | **+$830** | Tool low **$350 -> $400** (53/2/0, stamp Oct 27), raised, vs $340.90, holds | Wed Dec 9 3:35pm |
| MSTR $120C Nov20 | 24.60 / 24.85 (OI 1,819, vol 46) | $141.36 (+1.1%) | **+$255** | Tool $165 / Barclays $175 vs $142.05, holds | **Thu Oct 29 3:35pm** |
| NRG $105C Dec18 | 4.00 / 4.50 (OI 521, vol 277) | $95.27 (+1.8%) | **-$310** | Tool $131 (17/4/0) vs $112.10, holds | Wed Nov 4 3:35pm |
| PAAS $40C Jan15 | 4.10 / 4.60 (OI 6,341, vol 13) | $41.66 (+3.3%) | **+$20** | RBC $56 (Oct 14) vs $43.90, holds (tool $51, 6/2/0) | Wed Nov 4 3:35pm |

Paper book at the bid: open **-$3,020** on 9 positions, plus realized BA -$115, LVS +$52, CMG -$123, TMUS -$325 = **-$3,531** on $18,828 ever deployed (-18.8%). Today made **$1,280** (TMUS counted from Monday's 1.85 bid to its 1.95 close, +$10): AVGO +$1,110 (stock +4.0%; tool low raised to $400), FSLR +$225 (stock +4.6% the day before its ramp deadline), MSTR +$165, PAAS +$60, NRG +$50, CAVA +$30; against APP -$190 (closing spread 22% of mid), BURL -$160 (stock -2.5%, 27% closing spread), BABA -$20. No Rule 4 floor moved down on any of the nine. **FSLR ramp sell is tomorrow, Wed Oct 28 3:35pm** (print Thu Oct 29 PM); stock $175.82 is $0.82 over the $175 strike, so it is ITM by a hair and LASTCALL writes the hold-vs-sell (default sell, no binary flag). MSTR Thu Oct 29 3:35pm follows.

**Marks (WRAP Mon Oct 26, close, at the bid; quotes 3:59pm ET):**

| Contract | Bid / ask | Stock | Paper P&L at bid | Rule 4 low vs BE | Ramp-sell deadline |
|---|---|---|---|---|---|
| FSLR $175C Nov20 | 8.45 / 8.60 (OI 389, vol 63) | $168.15 (-2.2%) | **-$805** | Piper $251 (Sep 30) vs $191.50, holds (tool $197 is the Bernstein Sell; 30/9/1) | **Wed Oct 28 3:35pm** |
| APP $290C Dec18 | 17.10 / 18.20 (OI 301, vol 18) | $260.70 (+0.2%) | **-$1,030** | Jefferies $375 vs $317.40, holds (tool $325) | Wed Nov 4 3:35pm |
| BABA $110C Dec18 | 3.30 / 3.40 (OI 9,250, vol 210) | $100.27 (+0.6%) | **-$525** | Bernstein $165 (Sep 7) vs $118.55, holds (tool $141.04) | Mon Nov 23 3:35pm |
| CAVA $50C Dec18 | 5.45 / 6.00 (OI 465, vol 21) | $51.50 (-3.7%) | **-$210** | JPM $80 vs $57.55, holds (tool $58, $0.45 over BE) | Mon Nov 2 3:35pm |
| TMUS $160C Nov20 | 1.85 / 2.70 (OI 595, vol 29) | $146.92 (+0.3%) | **-$335** | Tool low $169 (27/4/0, unchanged) vs $165.20, holds | **Tue Oct 27 3:35pm** |
| BURL $270C Dec18 | 7.30 / 8.80 (OI 267, vol 2) | $241.23 (-2.6%) | **-$1,130** | Tool $290 vs $288.60, holds ($1.40 margin; 16/5/0) | Mon Nov 23 3:35pm |
| AVGO $280C Jan15 | 58.10 / 61.40 (OI 883, vol 0) | $329.29 (+2.4%) | **-$280** | Tool $350 vs $340.90, holds (52/3/0) | Wed Dec 9 3:35pm |
| MSTR $120C Nov20 | 22.95 / 24.95 (OI 1,750, vol 564) | $139.84 (-4.2%) | **+$90** | Tool $165 / Barclays $175 vs $142.05, holds | Thu Oct 29 3:35pm |
| NRG $105C Dec18 | 3.50 / 4.00 (OI 519, vol 2) | $93.63 (+1.4%) | **-$360** | Tool $131 (17/4/0) vs $112.10, holds | Wed Nov 4 3:35pm |
| PAAS $40C Jan15 | 3.50 / 3.90 (OI 6,328, vol 45) | $40.315 (+0.4%) | **-$40** | RBC $56 (Oct 14) vs $43.90, holds (tool $51, 6/2/0) | Wed Nov 4 3:35pm |

Paper book at the bid: open **-$4,625** on 10 positions, plus realized BA -$115, LVS +$52, CMG -$123 = **-$4,811** on $18,828 ever deployed (-25.6%; PAAS's $390 added). Today lost **$160** like-for-like (PAAS counted from its Friday entry-night bid): MSTR -$570 (stock -4.2%, the deep-ITM shape again), CAVA -$130, FSLR -$105, BURL -$70, TMUS -$35, against AVGO +$550, APP +$160, NRG +$30, BABA +$10. No Rule 4 floor moved on any of the ten. **TMUS ramp sell is tomorrow, Tue Oct 27 3:35pm** (print Wed Oct 28 PM); LASTCALL closes it at the bid. FSLR Wed Oct 28 3:35pm, MSTR Thu Oct 29 3:35pm follow.

*CMG close (WRAP Oct 21): same rule and same shape as BA on Oct 19. The tool's low target, the floor of record in `research_CMG_paper.md`, went from $35 to $32 under the $33.98 breakeven, and one Buy became a Hold, so it reads as a downgrade with a $32 target. Daytime runs don't search (standing order Oct 21), so the analyst wasn't named; the tool number is what the doc's exit plan keys on. Closed at the $0.25 closing bid. The stock was $31.39 at entry and $28.10 now: Bearxter's -13% and -18% print history never got a chance, the slide did it first.*

Entry notes:
- **BA:** R1 0.18; R2 Oct 27 + 21 = Nov 17 and LY Oct 29 + 21 = Nov 19, both <= Nov 20; 10-Q Nov 9 is 9 trading days before expiry. R6 on six AM prints (+6.06 / -4.37 / -4.37 / -1.56 / +5.53 / +4.76), median 4.56%. Tightest R6 margin of the three (95 cents). Spread 5.3% of mid.
- **CMG:** R1 0.23; stock -4.0% today; R4 margin $1.02 ($35 low vs $33.98 BE). Six PM prints (+1.60 / -13.34 / -18.18 / +1.94 / +3.03 / +12.50), median 7.76%. Spread 4.1% of mid.
- **FSLR (EVENING 1):** R1 ~0.05 (low $168.60). R2 Oct 29 / LY Oct 30 + 21 = Nov 20, passes exactly; 10-Q Nov 9 is 9 trading days before expiry. R3 29/10/1 (the one Sell is Bernstein Underperform $197, which is also the tool's "low target"; it was never a floor). R4 dated via MarketBeat: lowest Buy-side target after the Sep 21-25 leg down is Piper OW $251 (Sep 30); oldest inside 60 days is Evercore Positive $218 (Aug 17). R6 six PM prints (-8.32 / +5.29 / +14.28 / -13.61 / +4.86 / +2.44), median 6.80%. Nearest-OTM $180C / $185C fail R7, so it's one strike in-the-money. Doc: `week-09/research/research_FSLR_paper.md` (EVENING 2). Floor of record $218 (Evercore, ages out Oct 16) then $251 (Piper); Sep 24-25's -10% was a Treasury-yield sector move.
- **APP (EVENING 1):** R1 0.02 ($266.84-$738). R2 Nov 4 verified + 21 = Nov 25 <= Dec 18. R3 32/7/0. R4: the tool's $325 (Sep 11) predates the Sep 28 week's -17%; Jefferies cut to $375 on Oct 8 and kept Buy, which is the post-drop floor. R6 six PM prints (+11.88 / +11.97 / +0.70 / -19.68 / +6.41 / -19.66), median 11.93%. $290C chosen over $280C for the spread (4.9% vs 13%). Doc: `week-09/research/research_APP_paper.md` (EVENING 2). Unread: a "competitor concerns" headline; read it on the next DO run with a search to spare.
- **LVS:** R1 ~0 (at the low); the fund lost $67 on LVS in July (sold late, see binder Tab 5). Six PM prints (+6.49 / +4.31 / +12.39 / -13.96 / -8.62 / +1.72), median 7.55%. Spread 18.6% of mid, the widest of the three.

*LASTCALL (Tue Oct 20, 3:35pm) note: **LVS closed at the $1.87 bid, +$52 (+38.5%).** Hold-vs-sell, written: stock $38.03 vs the $37.50 strike, ITM by $0.53 (1.4%). Of the $1.87 bid, $0.53 is intrinsic and $1.34 is time value and IV (37.2%) that the Wed print crushes. The six-print median move is 7.55%, and two of the six were -8.6% and -14.0%. Hold scenarios, rough: +7.55% (stock ~$40.90) leaves the call ~$3.50; -7.55% (~$35.16) leaves ~$0.35; flat leaves ~$0.80. Average of the up and down cases is ~$1.93 against $1.87 in hand: no edge, all variance, on an ITM margin a one-percent dip erases. No binary flag at entry (paper, no 4/5 meeting for a hold). Default sell. The July LVS lesson (binder Tab 5) was a sell that never happened; this one happened on the minute.*

## CLOSED PAPER POSITIONS

| Opened | Closed | Contract | In (ask) | Out (bid) | P&L | Why closed |
|---|---|---|---|---|---|---|
| Oct 19 8:00pm | **Oct 29 LASTCALL (3:35pm quote, 19:35:52 UTC)** | MSTR $120C Nov20 | $22.05 | **$23.45** (23.45 / 24.70, OI 1,774, vol 75, IV 72.1%) | **+$140** | Ramp sell on its deadline (Q3 Thu Oct 29 PM, `verified: true`, `actual: null`). Stock $141.68 (-2.4% vs $145.16), ITM by $21.68 but $0.37 under the $142.05 BE, so the ITM hold was allowed; written hold-vs-sell said sell: of the 23.45 bid, $21.68 is intrinsic and only $1.77 is time value, and IV at 72% gets crushed tonight, so holding is a bet on direction alone, delta 0.85, on a print that is mostly a bitcoin mark-to-market (Bearxter's objection at entry). No binary flag was set, Tab 4 says out by the morning after anyway, and the 'pre-earnings profit target' never fired (stock peaked $153.36 Oct 22, under the $165 floor). Rule 4 held throughout (tool $165 / Barclays $175). Peak bid 34.50 (Oct 22, +56.5%); the +150% line ($55.13) never came close |
| Oct 9 6:00pm | **Oct 28 LASTCALL (3:35pm quote, 19:35:37 UTC)** | FSLR $175C Nov20 | $16.50 | **$11.35** (11.35 / 11.55, OI 388, vol 97) | **-$515** | Ramp sell on its deadline (Q3 Thu Oct 29 PM, `verified: true`, unreported). Stock $174.21 (-0.9%), $0.79 under the $175 strike, OTM, no binary-hold flag, so no hold-vs-sell case to write. Rule 4 held throughout (Piper $251 vs BE $191.50; tool 30/9/1, low $197 is the Bernstein Sell). The stock went $177.82 at entry -> $186.61 peak close Oct 13 -> $168.15 low Oct 26 -> $174.21; it never got within $4.89 of breakeven. 19 days of theta plus a 19.3% entry spread did the rest |
| Oct 12 10:36am | **Oct 27 LASTCALL (3:35pm quote, 19:35:38 UTC)** | TMUS $160C Nov20 | $5.20 | **$1.95** (1.95 / 2.20, OI 597, vol 11) | **-$325** | Ramp sell on its deadline (Q3 Wed Oct 28 PM, verified, unreported). Stock $146.66, $13.34 under the $160 strike, OTM, no binary-hold flag. Rule 4 held throughout (RJ $170 / tool $169 vs BE $165.20); the SpaceX tower-network news (Oct 9, Oct 23) took the stock from $153.17 at entry to $146.66 |
| Oct 9 1:37pm | **Oct 21 WRAP (3:59pm closing quote)** | CMG $32.5C Nov20 | $1.48 | **$0.25** (0.25 / 0.37, OI 6,960) | **-$123** | Rule 4: tool low target $35 -> $32, under the $33.98 BE (Buys 27 -> 26). Stock $28.095 vs $31.385 at entry |
| Oct 9 1:37pm | **Oct 20 LASTCALL (3:35pm quote, 19:35:37 UTC)** | LVS $37.5C Nov20 | $1.35 | **$1.87** (1.87 / 2.08, OI 16,262) | **+$52** | Ramp sell on its deadline (Q3 Wed Oct 21 PM, verified). Stock $38.03, ITM by $0.53 (1.4%), so the ITM hold was allowed; written hold-vs-sell said sell (below) |
| Oct 9 1:37pm | Oct 19 WRAP (3:59pm closing quote) | BA $195C Nov20 | $7.70 | $6.55 | **-$115** | Rule 4 per the doc's exit plan: tool low target $206 -> $195, under the $202.70 BE (stamp unchanged Oct 3) |

## GLOSSARY
- **Paper book:** trades written down as if placed, with no money. Fills are the live ask (buy) and bid (sell) at the time logged.
- **R1-R6:** binder Tab 1 Iron Rules. R1 range percentile, R2 earnings before expiry, R3 analyst consensus, R4 lowest Buy target above breakeven, R5 affordability (dropped here), R6 reachability (breakeven move <= 1.5x median earnings move).
- **BE (breakeven):** strike + premium paid.
- **OI (open interest):** contracts outstanding on that strike; a proxy for whether anyone trades it.
- **Spread % of mid:** (ask - bid) / mid. What you lose just by getting in and out.
- **Ramp sell:** selling before the print into the pre-earnings premium (Tab 4).
- **(f):** earnings date not yet company-verified (`get_earnings_results` verified: false).
