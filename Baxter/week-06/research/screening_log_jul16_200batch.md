# SCREENING LOG: JULY 16, 2026 (THE 200-NAME BATCH, ROUND 2)

*Continuation of the fresh batch flagged in the Jul 16 (later morning) session note -- "the new 200-name batch Michael asked for, pending sector confirmation." Sectors confirmed this session, all untouched by prior batches (Jun 22 puts run, Jul 10 four-screener run, Jul 12, Jul 13 200-batch): utilities, telecom, metals & mining, ag/farm & food processing, shipping/marine, packaging, education, specialty finance/BDC, hotels & leisure, aerospace & defense, waste/water/environmental, engineering & construction.*

**Method:** Geometry-first, per standing protocol. `fetch_price.py --range` (free, local) settles Rule 1 for all 225 names first, batched ~25/call. `fetch_puts_chain.py --calls` (free, local) on every CALLS-zone survivor, Aug21 2026 target expiry (~36 DTE). Searches (hard cap 8) spent only on the most plausible Stage 2 survivors, lowest required-move first. Puts stay off-limits pending the back-test (Calxter deadline Jul 31) -- PUTS-zone names logged to watch list only, zero further work.

*Log written incrementally -- appended after every Stage 1 batch call and every Stage 2 chain check, per crash-protection protocol.*

---

## STAGE 1: RANGE PERCENTILE (224 attempted, 16 invalid/delisted, 208 valid)

| Outcome | Count | % of valid |
|---|---|---|
| MID-OUT (25-75th pctile) | 104 | 50.0% |
| PUTS zone (>=75th pctile) | 66 | 31.7% |
| CALLS zone (<=25th pctile) | 38 | 18.3% |

No negative-percentile (fresh new low) names this batch.

**Notably invalid/delisted (16):** USM, SATS, NGD, X (US Steel -- Nippon acquisition), SEE, BERY, ATGE, UDMY, DFS (Discover -- Capital One acquisition), PLYA, SIX, SEAS, DESP, SPR (Spirit AeroSystems -- Boeing acquisition), ERJ, SJW.

**PUTS-zone names, logged to watch list only, zero searches spent (66):** Utilities: D, AEP, ED, ES, LNT, EVRG, PNW, IDA, OGE, POR, AVA, BKH, NWE, SWX, NJR, MDU. Telecom: ATEX, IDT, IRDM. Metals: NUE, RS, ATI, CRS. Ag: VMI, ADM, ANDE, DAR. Shipping: MATX, KEX, GNK, GOGL, SBLK, DAC, GSL, FRO, INSW, DHT, STNG, NAT, TNK. Packaging: SON, AMBP, CCK, BALL. Education: LINC. Specialty finance: ALLY. Hotels: MAR, H, VAC, TNL, HGV, RHP, PK, APLE, SHO, DRH, XHR, LTH. Aerospace/waste: GD, HEI, CW, DCO, WM, CLH, CWT. Engineering: FIX. This sector mix skewed heavily PUTS in shipping/marine and hotels & leisure (both near multi-year highs on freight/travel strength) and utilities (rate-sensitive names near highs on the current rate environment).

## STAGE 2: LIVE CHAIN FEASIBILITY (38 CALLS-zone survivors, Aug21 2026 target expiry)

| Ticker | Price | Pctile | Cheapest Aug21 strike/ask | Breakeven | NEEDS% | Verdict |
|---|---|---|---|---|---|---|
| BTG | $3.68 | 12th | $3.50C $0.40 | $3.90 | 6.3% | Alive |
| TSLX | $17.41 | 15th | $18C $1.00 | $18.50 | 6.1% | Alive |
| BXSL | $23.62 | 11th | $24C $0.55 | $24.55 | 3.7% | Alive |
| PSEC | $2.28 | 13th | $2C $0.45 | $2.45 | 6.8% | Alive |
| T | $21.84 | 19th | $23C $0.47 | $23.47 | 7.4% | Alive |
| LAC | $3.00 | 7th | $2C $0.71 | $3.21 | 7.5% | Alive |
| PEG | $79.64 | 23rd | $85C $0.70 | $85.70 | 7.6% | Alive |
| UEC | $9.79 | 21st | $10C $0.83 | $10.83 | 11.2% | Alive |
| OI | $9.75 | 22nd | $10C $0.80 | $10.80 | 11.5% | Alive |
| CLF | $9.71 | 22nd | $10C $0.87 | $10.87 | 12.2% | Alive |
| PPC | $29.05 | 11th | $32C $0.65 | $32.65 | 12.2% | Alive |
| COUR | $5.59 | 7th | $6C $0.40 | $6.40 | 14.5% | Alive |
| SLRC | $13.08 | 20th | $15C $0.10 | $15.10 | 15.3% | Alive |
| GPK | $11.02 | 15th | $12C $0.25 | $12.75 | 15.5% | Alive |
| PNR | $64.95 | 13th | $75C $0.70 | $75.70 | 15.7% | Alive |
| NAVI | $8.72 | 18th | $10C $0.30 | $10.30 | 18.1% | Alive |
| LOPE | $144.05 | 7th | $170C $0.75 | $170.75 | 18.5% | Alive |
| GOGO | $3.56 | 4th | $4C $0.25 | $4.25 | 19.7% | Alive |
| ERII | $8.65 | 8th | $10C $0.55 | $10.55 | 21.8% | Alive -- **commodity-vol exception** (energy-linked) |
| WPM | $104.66 | 21st | $130C $0.80 | $130.80 | 25.6% | Alive -- **commodity-vol exception** (silver streamer) |
| AEM | $138.10 | 15th | $175C $0.80 | $175.80 | 27.9% | Alive -- **commodity-vol exception** (gold miner) |
| PLNT | $52.73 | 20th | $65C $0.90 | $65.90 | 25.3% | Deprioritized (queued) |
| INGR | $101.22 | 16th | $130C $1.00 | $131.00 | 29.5% | Deprioritized (queued) |
| LBRDK | $31.57 | 4th | $40C $0.90 | $40.90 | 30.0% | Deprioritized (queued) |
| MP | $46.20 | 3rd | $60C $0.79 | $60.79 | 32.6% | Deprioritized (queued -- commodity-adjacent but exceeds ~30% exception cap) |
| HII | $275.07 | 12th | $360C $1.00 | $360.75 | 31.0% | Deprioritized (queued) |
| ROAD | $103.70 | 18th | $135C $0.90 | $135.90 | 31.9% | Deprioritized (queued) |
| ACM | $69.65 | 5th | $95C $0.40 | $95.40 | 36.9% | Deprioritized (queued) |
| KTOS | $47.50 | 2nd | $65C $0.85 | $65.85 | 38.3% | Deprioritized (queued) |
| LRN | $86.29 | 23rd | $130C $1.00 | $131.00 | 51.0% | **KILL -- R6 feasibility glance** |
| NOC | $524.18 | 11th | $800C $0.75 | $800.75 | 52.3% | **KILL -- R6 feasibility glance** |
| AVAV | $146.12 | 4th | $240C $0.75 | $240.75 | 63.2% | **KILL -- R6 feasibility glance** |
| OBDC | $11.12 | 13th | $18C $0.75 | $18.25 | 63.9% | **KILL -- R6 feasibility glance** |
| CHTR | $134.38 | 4th | $220C $0.70 | $220.70 | 64.9% | **KILL -- R6 feasibility glance** |
| PRIM | $89.68 | 18th | $150C $0.95 | $150.95 | 69.8% | **KILL -- R6 feasibility glance** |
| FSK | $10.91 | 9th | none | -- | -- | **KILL -- R5 no viable instrument** |
| LHX | $284.52 | 20th | none | -- | -- | **KILL -- R5 no viable instrument** |
| TDG | $1236.14 | 22nd | none | -- | -- | **KILL -- R5 no viable instrument** |

**Stage 2 tally:** 21 alive (3 on commodity-vol exception), 8 deprioritized/queued, 6 KILL R6, 3 KILL R5.

---

## STAGE 3: SEARCHES ON THE EIGHT LOWEST-REQUIRED-MOVE SURVIVORS (hard cap 8/8 spent)

Sorted by NEEDS% ascending from the 21 alive names; the eight cheapest breakevens got the search budget. The other 13 alive names (OI, CLF, PPC, COUR, SLRC, GPK, PNR, NAVI, LOPE, GOGO, ERII, WPM, AEM) are untouched past Stage 2 -- queued below.

| Ticker | Earnings date | Ratings | Decline story | Verdict |
|---|---|---|---|---|
| BXSL | Aug 6, 2026 (inside window) | 4 Buy/5 Hold/1 Sell of 10 -- raw count passes | BDC/specialty-lending sector; no confirmed fresh target cut found specifically on BXSL, but same sector as TSLX below which has a live, confirmed sector-wide repricing story | **BORDERLINE** -- R2/R3 pass on what's confirmed, but decline category unresolved. Needs one more search to confirm/rule out a fresh BXSL-specific cut and pin the decline category. |
| TSLX | Aug 4-5, 2026 (inside window) | JPMorgan, Wells Fargo, and KBW all cut price targets inside the recent weeks; Weiss downgraded Buy->Hold | BDC dividend-reset / sector-wide NII-compression repricing as base rates fall -- explicitly named in coverage ("Dividend Reset And Sector Repricing") | **KILL -- R3 fails on fresh target cuts inside 30 days, and the decline story is Category 3 (macro beta / sector repricing), not event overreaction.** |
| BTG | Not confirmed in search (B2Gold's Q2 2026 date wasn't surfaced; Q1 pattern suggests early-mid August) | Buy consensus, 13 analysts, avg target $5.95 vs $3.90 breakeven -- large cushion, no downgrade found | Not established -- gold miner at 12th percentile despite a bullish Street; no company-specific negative catalyst surfaced | **BORDERLINE** -- earnings date unconfirmed (R2 open) and decline category unresolved. Needs a dedicated follow-up search. |
| PSEC | ~Aug 25, 2026 (falls AFTER the Aug 21 expiry) | Wells Fargo underweight; price target trimmed $2.50->$2.00; S&P and KBRA credit downgrades to BB+ | Repeated dividend cuts, concentrated portfolio, realized losses -- Category 2 secular decline | **KILL -- R2 fails (earnings falls outside the option window); decline story is Category 2 regardless.** |
| T | Jul 22, 2026 (inside window) | Oppenheimer cut Outperform->Perform in June 2026 (inside 30 days) | SpaceX/Starlink direct-to-consumer mobile service announced Jun 26, 2026 -- structural competitive threat to AT&T's subscriber base, stock fell 5.1% same week | **KILL -- R3 fails on the fresh downgrade; decline story reads as Category 3 (macro/competitive beta), not overreaction.** |
| LAC | Aug 12, 2026 (inside window) | Hold consensus (7 analysts); Goldman initiated Neutral Jul 1, 2026 at $4.50 (new coverage, not a downgrade) | Falling lithium prices, sector-wide underperformance vs peers, -26% over the trailing month | **KILL -- Category 4 (commodity/cycle unwind).** |
| PEG | Aug 4, 2026 (inside window) | Moderate Buy, 16 analysts: 7 Buy/1 Strong Buy/8 Hold/**0 Sell** -- clean pass; no fresh downgrade found | Not established -- PEG has underperformed both its utility-sector peers (Utilities SPDR +19% vs PEG's +7.9% over 52wk) and the S&P 500 despite a positive price return; no company-specific negative catalyst surfaced | **BORDERLINE** -- R2/R3 both clean, but the decline story (why PEG lags its own sector) is unresolved. Best-looking name of the batch on paper; needs the one line a follow-up search would settle. |
| UEC | ~Sep 22, 2026 (falls well AFTER the Aug 21 expiry) | Strong Buy, 8 Buy/0 Sell/1 Hold, avg target $18.25 vs $10.83 breakeven | Not reached -- moot given R2 | **KILL -- R2 fails (no catalyst inside the option window).** |

**Stage 3 tally: 0 ADVANCE, 5 KILL, 3 BORDERLINE.** No clean survivor this batch -- consistent with the Jul 10 (0 advance) and Jul 12 (0 advance) sessions; only Jul 13 produced a name that cleared the screen (and it later died on Rule 6 anyway).

---

## STAGE 4: BORDERLINE RESOLUTION (same session, Jul 16, six additional searches on the main thread)

All three borderlines resolved same day. **All three KILL. Batch final: 208 screened, 0 entered.**

| Ticker | Resolution | Verdict |
|---|---|---|
| **BXSL** | The sector suspicion was name-specific after all: KBW downgraded to Market Perform ($25 -> $24) on Q1 credit quality (non-accruals 3.1%, dividend coverage down to 100%), JPMorgan cut the target $24 -> $23 on **Jul 2** -- fresh cut inside 30 days. Analyst-estimated 20-30% odds of a 2026 dividend cut. | **KILL -- R3 fresh cuts, and the decline is the same Category 3 sector repricing that killed TSLX.** |
| **PEG** | The missing decline story surfaced and it's not tradeable: earnings-growth slowdown (6.2% forecast vs 26.8% five-year average), skepticism that only 10-20% of the data-center pipeline converts, PSEG Power volumes down -- and a Jefferies downgrade Buy -> Hold on reduced confidence in the nuclear data-center deals. The "cleanest ratings in the batch" read was stale. | **KILL -- R3 (Jefferies downgrade) and no Category 1 event. A utility needing +7.6% would also have faced a near-certain Rule 6 fail (utilities' median print reaction is 1-3%).** |
| **BTG** | Earnings date confirmed (Aug 6 AMC, call Aug 7 -- R2 passes) but the DD-tier lines kill it: no Category 1 event (the Goose fire was disclosed May 8 and the stock RALLIED through it; what holds it at the 12th percentile is chronic Mali risk + transition-year AISC that only 2027 fixes), Rule 6 fails on its own record (median confirmed print reaction ~2.5-3%, cap ~4.5% vs +6.3% required), and the ratings picture is source-conflicted (one read 7 Buy/4 Hold/**2 Sell** -- adverse read fails R3). Full doc: `research_BTG.md`. | **KILL -- Line 5, Line 8, Line 3 unresolved-adverse.** |

The pattern across both 200-batches is now unmistakable and worth stating once: every name that survives the geometry reaches DD carrying a story a 12-month price target can justify, and dies because its own earnings-day record can't cash a 5-6 week option's required move. The funnel is working. The calls-side ocean is what's thin.

## QUEUED / DEPRIORITIZED

**Stage 2 alive, never reached a search (13, in NEEDS% order -- next in line if the three BORDERLINEs don't pan out):** PSEC-tier already killed; remaining alive-but-unsearched are OI (11.5%), CLF (12.2%), PPC (12.2%), COUR (14.5%), SLRC (15.3%), GPK (15.5%), PNR (15.7%), NAVI (18.1%), LOPE (18.5%), GOGO (19.7%), ERII (21.8%, commodity-vol exception), WPM (25.6%, commodity-vol exception), AEM (27.9%, commodity-vol exception).

**Stage 2 deprioritized (20-40% band, feasibility-glance only, not yet fully screened):** LBRDK (30.0%), PLNT (25.3%), INGR (29.5%), MP (32.6%, commodity-adjacent but over the ~30% exception cap), HII (31.0%), ROAD (31.9%), ACM (36.9%), KTOS (38.3%).

**PUTS watch list (66 names, logged in Stage 1 above, zero further work per standing no-dedicated-puts-pools rule until the back-test unblocks puts, Calxter deadline Jul 31).**

---

## GLOSSARY

- **MID-OUT:** Killed at Stage 1 for sitting in the 25th-75th percentile of the 52-week range -- no directional edge in either direction, no further work done.
- **R1/R2/R3/R5/R6:** Funnel lines from the Jul 10 audit. R1 = range percentile (Stage 1 of this batch). R2 = confirmed earnings catalyst before the target expiry, minimum 21 DTE at entry. R3 = ratings-direction filter (calls: max 1 Sell rating AND no downgrade/target-cut inside the trailing 30 days). R5 = chain affordability (a real Aug21 strike with ask <=$1.00 must exist). R6 = reachability (feasibility-glance version this batch: required move to breakeven judged against a flat percentage band rather than a per-name historical-earnings-move calculation, which is next-stage work not performed here).
- **Feasibility glance:** The free, live-chain-sourced (not web-estimated) check of whether a name's cheapest reasonable near-the-money Aug21 strike requires a plausible move. <=20% stays alive, 20-40% is deprioritized/queued, >40% is a Stage 2 KILL. Advisory, not a substitute for the full Rule 6 historical-earnings-move scoring that happens in real DD.
- **Decline category:** Every CALLS candidate that reaches Stage 3 gets its decline named: (1) event overreaction -- the only tradeable category; (2) secular decline -- KILL; (3) macro beta -- KILL; (4) commodity/cycle unwind -- KILL. This batch found zero Category 1 stories among the eight searched names -- three (TSLX, T, LAC) landed cleanly in Categories 2-4, two (PSEC, UEC) died on Rule 2 before category mattered, and three (BXSL, BTG, PEG) never got far enough to name a category at all.
- **Fresh new low / negative percentile:** A stock trading below its own recorded 52-week low (percentile computes negative), the strongest form of "knife still falling" -- killed on category without a search. None appeared in this batch.
- **Commodity-vol exception:** Per this session's funnel instructions, commodity-adjacent names (miners, shippers, energy-linked) get feasibility slack up to ~30% required move instead of the standard 20% cutoff, because those stocks historically print larger earnings-day moves. Applied to AEM, WPM (both precious-metals streamers/miners) and ERII (energy-linked); MP's 32.6% required move exceeded even the exception's ~30% ceiling and was deprioritized rather than kept alive.
- **DTE:** Days to expiration. This batch's target expiry is Aug 21, 2026, roughly 36 DTE from today (Jul 16).
- **BORDERLINE:** A Stage 3 verdict where the confirmed lines (R2, R3) pass or are incomplete but not failed, and the one missing piece -- an earnings date, a decline-category read -- is specifically named rather than guessed at. Three this batch (BXSL, BTG, PEG), all queued for a single resolving search next session.


