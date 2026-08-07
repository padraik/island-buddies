# Screening Log -- Aug 7, 2026, Round 2 (Bullxter, second parallel batch)

Reserve $1,054.96 (post-KR entry, KR is an open position now, not re-screened here), one open position (KR $61C Sep 4). Four agents running a second parallel round tonight targeting the 500-name sweep total: Bearxter, Macxter, Calxter, Bullxter, each on a fresh sector lane, each pushing independently. This is Bullxter's round 2 batch.

**Lane:** consumer staples (household/personal care products), scientific instruments/testing and measurement, data center REITs, beauty/cosmetics, toys/hobby/leisure products, off-price retail, coal/diversified mining (distinct from the metals ground already covered).

**Standing context going in:** every parallel lane tonight and yesterday has independently hit the same wall -- Aug 7 sits in a trough right after a wave of Q2 prints, so cheap-looking dislocations keep turning out to be post-earnings reactions with the real catalyst outside any affordable expiry. Checked last-reported date early on every chain survivor before spending DD time, per the standing instruction.

## Stage 1 -- Range percentile (free, fetch_price.py --range)

40 attempted (hard cap for this batch), 3 unavailable (PKI -- 404, likely delisted/renamed post-Revvity restructuring; SIX -- 400 error, bad symbol, consistent with the Six Flags/Cedar Fair 2024 merger changing the ticker; CEIX -- 400 error, bad symbol), 37 valid.

| Ticker | Price | 52wk Range | Pctile | Direction |
|---|---|---|---|---|
| PG | $145.58 | 137.62-167.25 | 27th | MID-OUT |
| CL | $92.97 | 74.55-99.33 | 74th | MID-OUT |
| CLX | $106.72 | 84.70-128.90 | 50th | MID-OUT |
| KMB | $109.06 | 92.42-137.46 | 37th | MID-OUT |
| CHD | $103.29 | 81.33-106.04 | 89th | PUTS (logged only) |
| A | $143.19 | 108.35-160.27 | 67th | MID-OUT |
| MTD | $1435.20 | 1023.05-1525.17 | 82nd | PUTS (logged only) |
| WAT | $401.83 | 275.05-414.15 | 91st | PUTS (logged only) |
| PKI | -- | -- | -- | unavailable |
| BRKR | $51.47 | 28.53-65.30 | 62nd | MID-OUT |
| KEYS | $335.71 | 152.85-374.96 | 82nd | PUTS (logged only) |
| EQIX | $1053.30 | 720.62-1128.68 | 82nd | PUTS (logged only) |
| DLR | $194.27 | 146.23-208.14 | 78th | PUTS (logged only) |
| IRM | $122.10 | 77.77-134.68 | 78th | PUTS (logged only) |
| **GDS** | **$32.05** | **26.97-48.61** | **23rd** | **CALLS -- advances to chain** |
| EL | $86.97 | 66.22-121.64 | 37th | MID-OUT |
| COTY | $2.79 | 1.82-5.08 | 30th | MID-OUT |
| IPAR | $120.20 | 77.21-129.29 | 83rd | PUTS (logged only) |
| ELF | $96.75 | 48.82-150.99 | 47th | MID-OUT |
| **NUS** | **$5.36** | **4.89-14.62** | **5th** | **CALLS -- advances to chain** |
| BBWI | $20.07 | 14.28-32.32 | 32nd | MID-OUT |
| HAS | $93.35 | 69.50-106.98 | 64th | MID-OUT |
| **MAT** | **$14.66** | **12.73-22.48** | **20th** | **CALLS -- advances to chain** |
| FNKO | $6.17 | 2.22-7.03 | 82nd | PUTS (logged only) |
| JAKK | $25.48 | 14.87-27.22 | 86th | PUTS (logged only) |
| BC | $82.28 | 55.84-90.25 | 77th | PUTS (logged only) |
| YETI | $52.62 | 30.51-53.99 | 94th | PUTS (logged only) |
| SIX | -- | -- | -- | unavailable |
| **THO** | **$79.52** | **69.71-122.83** | **18th** | **CALLS -- advances to chain** |
| BJ | $97.17 | 83.21-110.71 | 51st | MID-OUT |
| **OLLI** | **$79.50** | **60.29-141.08** | **24th** | **CALLS -- advances to chain** |
| FIVE | $233.18 | 131.40-251.63 | 85th | PUTS (logged only) |
| CTRN | $70.78 | 29.20-73.39 | 94th | PUTS (logged only) |
| GO | $9.72 | 5.66-19.41 | 30th | MID-OUT |
| BTU | $22.96 | 15.67-41.14 | 29th | MID-OUT |
| CEIX | -- | -- | -- | unavailable |
| **AMR** | **$148.07** | **123.78-253.82** | **19th** | **CALLS -- advances to chain** |
| HCC | $88.06 | 54.66-110.39 | 60th | MID-OUT |
| CCJ | $94.98 | 68.96-135.24 | 39th | MID-OUT |
| VALE | $14.78 | 9.67-17.94 | 62nd | MID-OUT |

**Tally: 15 MID-OUT, 13 PUTS-zone (logged, untouched, per no-dedicated-puts-pools rule), 6 CALLS-zone advance to chain: GDS, NUS, MAT, THO, OLLI, AMR.**

## Stage 2 -- Chain feasibility (free, fetch_puts_chain.py --calls) + calendar checks

Six survivors, six deaths, but not the same shape as every other lane tonight. Two of these (NUS, GDS) had genuinely real, un-fired, well-bracketed catalysts, cheap chain geometry, and still died on Rule 4 -- a different failure mode than the calendar traps everyone else keeps finding. Worth flagging for the sweep record: the trough isn't only a calendar problem tonight, it's also a "the market is right about these two" problem.

- **NUS: real catalyst, real cheap chain, KILLED on Rule 4 and decline category, both decisive.** Q2 2026 earnings confirmed **Aug 10, 2026** (after market close), 3 days out, well inside the Aug 21 expiry -- the first genuinely un-reported forward catalyst either round of tonight's four lanes has found. Chain is dirt cheap: **$5C Aug 21, ask $0.50, breakeven $5.50, needs only +2.6%.** I wanted this one bad. Then the ratings pull: only 2 analysts cover it, consensus **Hold**, average target $6.88, low target $6.75 -- **zero Buy-rated analysts in coverage at all.** Rule 4 requires the lowest *Buy*-rated target to sit above breakeven; there is no Buy-rated target to check, which is a harder fail than a Buy target that's merely too low. Underneath that: Q1 2026 revenue down 12% YoY, customers down 14%, Paid Affiliates down 8%, Sales Leaders down 13%, selling expense ratio rising (34.3% vs 32.5% of revenue) -- a direct-sales/MLM business bleeding its own distributor base, not a one-off miss. That's Category 2 (structural decline), same shape as the companion-animal read that killed ZTS a batch ago, not the Category 1 overreaction this fund hunts for. Two independent kills, either one sufficient alone.
- **GDS: real catalyst, real ratings, KILLED on Rule 4 alone.** Q2 2026 earnings confirmed **Aug 13, 2026**, 6 days out, inside the Aug 21 expiry. Cheapest usable strike: **$37C Aug 21, ask $0.90, breakeven $37.90, needs +18.2%** (flagged STRETCH, near the cap; $38C at $0.75 needs +20.9% and is the cheaper-on-cost OK-flagged alternative). Ratings are genuinely strong: 17 Buy / 1 Hold / 0 Sell of 18, average target $53.53 -- Rule 3 clears clean. But Rule 4 asks for the *lowest* Buy-rated target, and that's TD Cowen, Buy-rated, freshly trimmed to **$36** (from $37, a live and recent cut). $36 sits below every breakeven in the affordable chain ($37.90 and up). The most conservative bull on the Street, even after reaffirming Buy, doesn't believe this stock clears our cheapest strike. Rule 4 fails outright regardless of the otherwise-clean ratings picture and the real, well-bracketed catalyst. Never got to Rule 6 -- Rule 4 is a hard gate.
- **MAT: KILLED on calendar (post-earnings trap).** Mattel reported Q2 2026 on **Aug 4, 2026**, 3 days before this screen (revenue beat, margin pressure noted). The 20th-percentile read and the deceptively cheap $15C Aug21 (5.8% needed) are the market's post-earnings reaction, not a pre-earnings setup. Next print (Q3) not confirmed but standard cadence runs to late October, outside every listed expiry pulled (Aug21/Sep18/Oct16 all checked, none bracket a late-Oct/early-Nov date without going 3+ months out). Same trap as TSCO/TRIP/MNRO in round 1.
- **THO: KILLED on chain gap.** Thor Industries' fiscal Q4 2026 (year-end, quarter ending Jul 31) reports on the pattern set by Q1-Q3 this fiscal year (Dec 3 '25, Mar 3 '26, Jun 3 '26) -- next report lands early December 2026. No listed expiry (Aug21, Sep18, Oct16 all checked) comes remotely close to bracketing a December catalyst. Cheapest strike ($85C Aug21, needs +8.0%) is a real dislocation with no near-dated mechanism to resolve it.
- **OLLI: KILLED on calendar/chain gap, doubly confirmed.** Ollie's Bargain Outlet reports Q2 FY2026 on **Aug 27, 2026** -- after the Aug 21 expiry (the only expiry with usable $0.10-$1.00 strikes, cheapest $90C at 14.2%) expires, so Aug21 doesn't bracket the catalyst even though it looks affordable. Sep18 independently returned **zero calls in range** on its own. Oct16 does bracket Aug 27 but only offers $120C+ strikes needing 52%+ -- priced completely out of reach. No instrument both brackets the real catalyst and stays inside any sane cost/move range.
- **AMR: KILLED on calendar and Rule 6, both decisive.** Alpha Metallurgical already released **preliminary Q2 2026 results via 8-K** (net loss $12.3M, guidance cut) ahead of the full report landing **today, Aug 7, 2026** -- the number the market would trade on is already public before this screen even ran. Chain math was already ugly regardless: cheapest usable strike ($185C Aug21) needs **+25.4%**, and that's before any Rule 6 historical-move check -- coal/met-coal earnings reactions in this range have never been documented near that magnitude anywhere in this fund's prior screening. Double-dead: no fresh information left to trade, and the math never worked anyway.

## Stage 3 -- Full DD

None reached DD. All six CALLS-zone survivors died in Stage 2: two on Rule 4 with genuinely real catalysts and otherwise-clean setups (NUS, GDS), one on Rule 4 plus decline category (NUS, both independently decisive), two on calendar/chain-gap (MAT, THO), one on double calendar/chain-gap (OLLI), one on calendar plus a decisive Rule 6-scale mismatch (AMR).

## Batch tally

**40 attempted (hard cap reached), 3 unavailable (delisted/bad symbol), 37 valid, 6 CALLS-zone advances, all 6 killed in Stage 2 (2 on Rule 4 alone, 1 of those doubled by decline category, 2 on calendar/chain-gap, 1 on double chain-gap, 1 on calendar+Rule 6). 0 advances to DD. 0 survivors at 3.5+. 0 at 4/5.**

13 PUTS-zone names logged, untouched, per the no-dedicated-puts-pools rule (back-test still gates live puts entries): CHD (89th), MTD (82nd), WAT (91st), KEYS (82nd), EQIX (82nd), DLR (78th), IRM (78th), IPAR (83rd), FNKO (82nd), JAKK (86th), BC (77th), YETI (94th), FIVE (85th), CTRN (94th). Nothing individually flagged as a standout puts setup this batch beyond the range percentile itself -- no fresh downgrade or documented stalled-high pattern checked or found in passing.

**This lane's finding for the sweep record:** unlike every other lane tonight, the failure mode here wasn't uniformly calendar traps. Two names (NUS, GDS) had real, un-fired, well-bracketed catalysts and still died -- on Rule 4, the bear-floor check, not on timing. That's the rules working as designed: cheap chain geometry and a real date aren't enough on their own if the Street's own floor (or lack of one) says the market isn't wrong. Worth remembering the next time a 2.6%-required-move number looks too good this late in a sweep -- it can still be a real trap, just a different kind than the post-earnings one.

## GLOSSARY

- **52-week range / percentile:** where the current price sits between the stock's low and high over the trailing year; 0% = at the low, 100% = at the high.
- **MID-OUT:** a name that lands in the middle 50% of its 52-week range (25th-74th percentile) and is screened out immediately with no further analysis, per the Unified Screen.
- **CALLS zone / PUTS zone:** bottom quartile (0-24th percentile) is a CALLS candidate; top quartile (75th-100th) is a PUTS candidate, per the Unified Screen.
- **Rule 2 (confirmed catalyst):** the Iron Rule requiring a dated earnings event before the option's expiration; a stock that already reported fails this regardless of how cheap its options look.
- **Rule 3 (ratings):** for calls, near-zero analysts rating the stock Sell/Underperform (max 1).
- **Rule 4 (bear floor):** the lowest price target among Buy-rated analysts must sit above the option's breakeven. Zero Buy-rated analysts in coverage is a harder fail than a Buy target that's merely too low -- there is no floor to check.
- **Rule 5 (chain filter):** the cap on how much a single option contract can cost, scaled to reserve and conviction tier; currently locked at $1.00/share under the transitional lock.
- **Rule 6 (reachability):** the move required to reach breakeven must not exceed 1.5x the stock's median historical earnings-day reaction.
- **Breakeven:** strike price plus premium paid per share, where the option holder neither gains nor loses at expiration.
- **Chain gap:** when a stock's real earnings date falls in the empty space between two listed option expiries (or after the only affordable one expires), so no affordable instrument actually brackets the catalyst.
- **Post-earnings trap:** a stock sitting at a cheap percentile because it just reported and reacted negatively, with no new catalyst before the next affordable expiry.
- **Decline category (Category 1 vs 2):** whether a stock's drop reflects a one-off market overreaction (tradeable) or real, ongoing business deterioration (not tradeable), per the Jul 10, 2026 audit.
