# SCREENING LOG: JULY 13, 2026 (THE 200-NAME BATCH)
*Michael explicitly approved a batch far above the normal 10-20/session cap, with one new condition: figure out how to gate Fable 5 to a single capstone review instead of running the whole thing on premium reasoning. Protocol note at the end covers that. Everything through this log runs on the standing model, not Fable 5 -- none of it is rule-changing or decision-critical on its own.*

**Sourcing:** geometry-first, per the Jul 12 post-mortem. No dedicated puts pools (Finding 3 -- puts stay blocked until the back-test runs). Sectors deliberately NOT yet touched by any prior batch: regional banks, REITs, industrials/transports, biotech/pharma mid-caps, apparel/retail, autos, energy E&P, chemicals, semis, media, software mid-caps, healthcare services, gaming, airlines, cruise, restaurants, homebuilders, insurance, staffing, industrial machinery. Checked against the full exclusion list accumulated across every prior batch (Jun 22, Jul 10 four-screener run, Jul 12, Jul 13 re-checks).

**Method:** `fetch_price.py --range` (free) on all 198 candidates first, in five batched calls. R1 MID-OUTs and PUTS-zone names killed/logged for zero cost. `fetch_puts_chain.py --calls` (free) on every CALLS-zone survivor. Searches spent only on names that survived the free chain-feasibility glance.

---

## STAGE 1: RANGE PERCENTILE (198 attempted, 15 invalid/delisted, 183 valid)

| Outcome | Count | % of valid |
|---|---|---|
| MID-OUT (25-75th pctile) | 87 | 47.5% |
| PUTS zone (>=75th pctile) | 76 | 41.5% |
| CALLS zone (<=25th pctile) | 20 | 10.9% |

**PUTS-zone names logged to watch list only, zero searches spent, per the no-dedicated-puts-pools rule** (banks: ZION, KEY, FITB, CFG, WTFC, GBCI, UMBF; REITs: SPG, KIM, REG, FRT, HIW, DOC, ESS, CPT, UDR, EGP, STAG; transports: UPS, FDX, JBHT, CHRW, XPO, ODFL, KNX, WERN, LSTR, RXO, ARCB; biotech: EXEL, INCY, JAZZ, HALO, ARWR; apparel: LEVI, COLM, GIII, CROX, SHOO; retail: TGT, BURL, ROST, BBY; auto/energy: MGA, OVV; chemicals: ASH; semis: LSCC, SLAB; media/software: LYV, TWLO, FROG; healthcare: CNC, MOH, CVS, DVA, ACHC; gaming: PENN, CZR, MGM; airlines: DAL, ALGT; restaurants: CAKE, DIN, TXRH, EAT; insurance: MET, PRU, HIG, UNM, GL, VOYA, PFG; staffing: KFY; machinery: PH, IEX, CR). This sector mix skewed unusually PUTS-heavy (41.5% vs the historical ~15-20% in prior batches) -- banks, REITs, and transports have broadly rallied this cycle.

**Notably invalid/delisted (15):** CMA, SNV, FOLD, SKX, JWN, GPS, CTRA, CIVI, CFLT, SMAR, GDEN, DENN, TPH, BLD, ASGN.

## STAGE 2: LIVE CHAIN FEASIBILITY (20 CALLS-zone survivors)

| Ticker | Price | Pctile | Chain result | Verdict |
|---|---|---|---|---|
| CABO | $38.10 | 3rd | No options chain listed (404) | **R5 KILL -- no instrument** |
| ALNY | $286.00 | 6th | Only Jul17 (4d) at +36.5%; no viable Aug21 strike | **R5 KILL -- no instrument** |
| SWKS | $59.25 | 19th | Cheapest Aug21 needs +49.2%, STRETCH-tagged | **R6 KILL -- feasibility glance** |
| UHS | $152.77 | 12th | Only Jul17 (4d) at +8.6%; no viable Aug21 strike | **R5 KILL -- no instrument** |
| DPZ | $309.85 | 13th | Only Jul17 (4d) at +6.8%; no viable Aug21 strike | **R5 KILL -- no instrument** |
| WING | $154.00 | 14th | Only one Aug21 strike, +63.0%, STRETCH-tagged | **R5 KILL -- no real instrument** |
| TDS | $32.08 | -8th (below stated 52wk low) | Aug21 $40C $0.45, +26.1% | **KILLED ON CATEGORY -- fresh new low, knife still falling, no search spent** |
| REXR | $34.75 | 21st | Aug21 $40C $0.20, +15.7% | Deprioritized (industrial REIT, low historical vol; queued) |
| ADNT | $19.20 | 16th | Aug21 $22C $0.85, +21.6% | Deprioritized (queued) |
| LEN | $82.96 | 3rd | Aug21 $100C $0.55, +21.2% | Deprioritized (queued) |
| PZZA | $33.00 | 13th | Aug21 $40C $0.70, +23.3% | Deprioritized (queued) |
| ASAN | $7.60 | 22nd | Aug21 $10C $0.20, +34.2% | Deprioritized (queued) |
| DOMO | $3.30 | 9th | Aug21 $4C $0.65, +40.9% | Deprioritized (queued) |
| SHAK | $62.06 | 12th | Aug21 needs +38.5-46.2%; Jul24 needs only +12.1% but 11 days is tight | Deprioritized (queued, check earnings date vs Jul24 first) |
| AOS | $59.53 | 19th | Aug21 $70C $0.50, +18.4% | Deprioritized (queued) |
| CRSP | $50.65 | 19th | Aug21 cheapest reasonable $70C $0.60, +39.4% | **See Stage 3** |
| RRC | $36.24 | 23rd | Aug21 $41C $0.70, +15.1% | **See Stage 3** |
| FMC | $11.23 | 2nd | Aug21 $12C $0.65, +17.1% | **See Stage 3** |
| MOS | $22.36 | 14th | Aug21 $25C $0.65, +14.7% | **See Stage 3** |
| BNTX | $90.07 | 24th | Aug21 $115C $0.90, +28.7%, STRETCH-tagged | **See Stage 3** |

## STAGE 3: SEARCHES ON THE FIVE MOST PLAUSIBLE (biotech + commodity, categories that can plausibly deliver 15-30% moves)

| Ticker | Earnings | Ratings | Decline story | Verdict |
|---|---|---|---|---|
| **FMC** | Jul 29, 2026 (inside window) | 5 Buy/11 Hold/1 Sell -- passes raw count | 75% YoY decline, GAAP net loss, net debt $4.15B at 5-6x EBITDA, RBC cut target $17->$14 (FRESH, inside 30 days) | **KILL -- R3 fails on the fresh cut regardless of Sell count. Balance-sheet distress (secular/structural), not an overreaction.** |
| **RRC** | Jul 21, 2026 (inside window) | Mixed/conflicting sources, real Sell count present, consensus reads Hold | "Continued commodity headwinds and oversupply concerns" -- explicit cycle language | **KILL -- Category 4 (commodity/cycle unwind), and ratings don't clear R3 cleanly either.** |
| **MOS** | Aug 3, 2026 (inside window) | Buy consensus, 21 analysts, target $27-$28 vs $22.36 spot (~20-25% gap) | Potash segment revenue UP YoY ($667M vs $570M); "geopolitical disruption" and phosphate cost pressure cited as near-term drag, not company failure | **ADVANCE to full DD.** Genuine dislocation shape: segment growing while stock sits at 14th pctile. Best candidate of the batch. |
| **CRSP** | Aug 3, 2026 (inside window) | 17 Buy/9 Hold/1 Sell of 39 -- clean R3 pass | 2026 pipeline is data/milestone-heavy (CTX310, Lp(a), CTX611 readouts) but nothing single dated and market-moving lines up exactly with Aug 3 | **BORDERLINE -- R2/R3 clear, but cheapest viable Aug21 strike needs +39.4%. Needs CRSP's own historical earnings-day move before Rule 6 can be scored either way. Queued.** |
| **BNTX** | Aug 3-4, 2026 (inside window) | No Sell found; UBS just upgraded to Buy ($117->$135) on ASCO oncology data; Bernstein initiated Hold-equivalent ($96) | Positive momentum already fired (ASCO readout, UBS upgrade) -- some of the good news may already be priced in | **BORDERLINE -- clean R3, but +28.7% required move on a name that just got its bullish catalyst. Needs historical earnings-day move data. Queued.** |

---

## WHAT'S QUEUED FOR NEXT SESSION

1. **MOS full 13-line DD** -- decline category confirmation, floor freshness (target dates), implied-move cross-check, short interest, insider activity, sizing. This is the lead candidate.
2. **CRSP and BNTX Rule 6 resolution** -- one historical-earnings-move data point each settles whether these advance or die. Cheap to finish (2 searches).
3. **The eight deprioritized CALLS-zone names** (REXR, ADNT, LEN, PZZA, ASAN, DOMO, SHAK, AOS) -- none killed outright, none advanced. Feasibility glance put all of them in a 18-40% required-move band that's plausible but not clean; they get the remaining search budget next session if MOS/CRSP/BNTX don't fill the pipeline.

## THE FABLE 5 GATE (per Michael's ask this session)

Everything above ran on the standing model. None of it needed to be otherwise -- range percentile is arithmetic, chain feasibility is arithmetic, and the searches were narrow lookups (earnings date, ratings, one-line decline story), not judgment calls. The Model Cost Awareness rule (`/stonks` skill, added Jul 13) says Fable 5 gets spent on work that could change a standing rule or resolve a decision-critical uncertainty -- not on running 200 names through a funnel.

**The actual Fable 5 moment comes at the end, once MOS (and CRSP/BNTX, if they clear) finish full DD.** At that point the funnel triage package -- decline category, Rule 6 reachability math, implied-move cross-check, short interest, insider activity, sizing -- is exactly the kind of real-money judgment call the July 10 `funnel_triage_jul10.md` was, and exactly what the SOUN gate was. That's the capstone: one focused Fable 5 pass on whatever small survivor set exists, not a Fable 5 pass on every name in a 200-name haystack. Same structure as the four-screener run (cheaper reasoning does the screen tier, the expensive tier does triage), just with the model-cost line drawn explicitly this time instead of implicitly.

## GLOSSARY

- **Geometry-first:** Screening order adopted Jul 12 -- free local scripts (price/range, then live chain) run before any search, so paid searches are spent only on names that already own a viable instrument.
- **MID-OUT:** Killed at range percentile for sitting in the 25-75th percentile of the 52-week range -- no directional edge either way.
- **PUTS zone:** Top-quartile (>=75th percentile) names. Not screened further this batch per the standing decision that puts stay blocked until the passes.md back-test runs (Calxter deadline Jul 31); logged to the watch list only.
- **R1/R2/R3/R5/R6:** Funnel lines from the Jul 10 audit. R1 = range percentile. R2 = confirmed earnings inside the expiry window. R3 = hardened ratings direction filter (calls: max 1 Sell AND no downgrades/target cuts in 30 days). R5 = chain affordability (ask <=$1.00 calls). R6 = reachability (required move <=1.5x median earnings-day move).
- **Fresh new low / negative percentile:** A stock trading below its own recorded 52-week low (percentile computed as negative), meaning the range data itself is stale relative to price action -- treated as the strongest form of "knife still falling" and killed on category without a search (TDS this batch).
- **Feasibility glance:** The free, chain-verified (not web-estimated) check of whether a name's cheapest reasonable near-the-money strike requires a plausible move for its category. Advisory but chain-sourced, unlike the Jul 10 run's web-estimated glance.
- **Fresh downgrade/target cut:** An analyst action inside the trailing 30 days. Disqualifies a calls candidate under hardened R3 even if the raw Sell count is low (FMC this batch: 1 Sell but a fresh RBC cut).
- **Decline category:** Every CALLS candidate's decline gets named before advancing: (1) event overreaction -- tradeable, (2) secular decline, (3) macro beta, (4) commodity/cycle unwind. FMC reads as (2)/distress; RRC reads as (4); MOS reads as a genuine (1) candidate given segment growth against a beaten-down price.
- **Model Cost Awareness:** Standing rule (added Jul 13, `/stonks` skill) -- Fable 5 gets flagged and used only for analysis that could change a standing rule or resolve a decision-critical uncertainty. Mechanical screening and narrow lookups don't qualify; final funnel triage on real survivors does.
- **Funnel triage:** The DD-tier synthesis step (lines 5-13) that turns screen-tier survivors into a pitch-ready or killed verdict. Precedent: `funnel_triage_jul10.md`.
