# SCREENING LOG: MACXTER, JULY 10 2026

Slice: 50 unique names split across two pools.

Pool A (approximately 20 names): companies with live policy, tariff, or regulatory exposure in either direction, sourced from documented 2026 filings, executive orders, tariff lists, congressional trade disclosures, or regulatory actions. Policy tailwind on a beaten-down name is a calls candidate. Policy threat on a name at highs is a puts candidate. Sources cited for every policy claim.

Pool B (approximately 30 names): stocks in the top 20 to 25 percent of their 52-week range carrying visible analyst skepticism (2 or more Sell ratings, or a documented Buy-to-Sell downgrade in the last 30 days). This is the puts-hunting pool.

Method: WebSearch and WebFetch only, no Robinhood scripts. Screen implements lines 1 through 4 of the 13-line funnel (screen tier, not full DD): (1) range percentile, with the puts-specific no-new-52-week-high-in-5-days check, (2) confirmed earnings before expiry, 21 or more DTE for puts, (3) ratings direction filter (calls: max 1 Sell and no downgrades or target cuts in 30 days; puts: minimum 2 Sell/Underperform or documented Buy-to-Sell within 30 days, Buy-to-Hold does not count), (4) feasibility glance on Rule 5 (ask at or below $1.00 calls, $1.50 puts) and Rule 6 (required move at or below 1.5x median earnings-reaction move) joint. Targeting Aug/Sep 2026 expiries. On any puts ADVANCE, the puts protocol flags are recorded: short interest greater than 10 percent of float (squeeze warning), M&A rumor or strategic review or activist campaign (auto-disqualify), 4 or more consecutive beat-and-raise quarters (earnings history cap), and direction of consensus EPS revisions in the last 30 days.

Exclusions already applied (held, screened, or watched elsewhere): ABT, TRMB, UBER, LYFT, LVS, ZG, DIS, TSLA, DASH, ABNB, RCL, TTD, DKNG, MDT, NKE, CCL, BSX, HITI, DSGX, CHWY, CMG, MCD, WEN, SBUX, KVUE, MDLZ, YUM, EL, ISRG, PFE, BMY, CI, ELV, MRK, HUM, MEDP, VEEV, CELH, PLTR, COIN, SNOW, MDB, LULU, HOOD, DUOL, STZ, KBH, WGO, CALM, ZTS, FLUT, STE, GEHC, EQT, EXE, FIS, AVY, SNDK, AAPL, SOFI, KO.

All data below is sourced via live search on July 10, 2026. Any unverifiable figure is marked UNVERIFIED. Thin-data names are marked DATA-INSUFFICIENT.

---

## SCREENING TABLE

| Ticker | Price | Range % | Direction | Earnings date | Ratings check | Feasibility | Verdict | Note |
|---|---|---|---|---|---|---|---|---|
| LLY | $1188.58 | 90% | PUTS (threat, at highs) | Aug 6 2026 | 1 Sell / 23 Buy; fails puts min-2 | n/a | R3-FAIL | Pool A. Section 232 pharma tariff, Annex III company, 120-day clock from Apr 2 2026 EO, effective Jul 31 2026 (Foley Hoag / Crowell & Moring summaries). Only 1 Sell despite being at 90th pctile. |
| JNJ | $257.17 | 89% | PUTS (threat, at highs) | Jul 15 2026 | 0 Sell / 20 Buy | n/a | R3-FAIL | Pool A. Annex III pharma tariff name (same EO). Zero Sells, no documented downgrade. |
| ABBV | $248.00 | 82% | PUTS (threat, at highs) | Jul 31 2026 | 0 Sell / 17 Buy + 2 SB | n/a | R3-FAIL | Pool A. Annex III pharma tariff name. JPM raised PT 7/10, no bearish momentum. |
| AMGN | $363.39 | 77% | PUTS (threat, at highs) | Aug 4 2026 | 2 Sell / 11 Buy; passes | Last earnings move -4.8%; required OTM strike for $1.50 ask ≈14%+ vs 1.5x-cap ≈7% | R5-R6-FAIL | Pool A. Annex III pharma tariff name. Ratings pass but $363 price structurally can't clear Rule 6 at a $1.50 ask. |
| GILD | $129.83 | 45% | OUT (mid) | Aug 6 2026 | 0 Sell | n/a | MID-OUT | Pool A. Annex III pharma tariff name; range sits in the dead middle. |
| REGN | $664.52 | 44% | OUT (mid) | Jul 30 2026 | 0 Sell | n/a | MID-OUT | Pool A. Annex III pharma tariff name; mid-range despite Morgan Stanley PT cut to $730 (7/2026). |
| NVS | $154.06 | 72% | OUT (below 75% cutoff) | Jul 21 2026 | 2 Sell / 7 Buy | n/a | MID-OUT | Pool A. Annex III pharma tariff name (ADR); just short of top-quartile line. |
| NVO | $49.49 | 39% | OUT (mid) | Aug 5 2026 | 1 Sell | n/a | MID-OUT | Pool A. Annex III pharma tariff name (ADR); well off both extremes despite prior collapse from $71.79 high. |
| AZN | $171.86 | 46% | OUT (mid) | Jul 27 2026 | 1 Sell | n/a | MID-OUT | Pool A. Annex III pharma tariff name (ADR); Wainua trial miss news already digested into mid-range. |
| GSK | $52.77 | 66% | OUT (below 75% cutoff) | Jul 28 2026 | 2 Sell / 3 Buy | n/a | MID-OUT | Pool A. Annex III pharma tariff name (ADR). |
| SNY | $43.50 | 22% | CALLS (bottom quartile) | Jul 30 2026 | 0 Sell; passes | Low-vol multinational ADR (~2% typical earnings move); required move for $1.00 ask call exceeds 1.5x cap | R5-R6-FAIL | Pool A. Annex III pharma tariff name (ADR), beaten down into bottom quartile, ratings clean, but structurally too low-beta to clear Rule 6. |
| NVDA | $210.96 | 66% | OUT (below 75% cutoff) | Aug 26 2026 | 0 Sell | n/a | MID-OUT | Pool A. US-China chip export-control threat/relief whiplash (CNBC 4/7/26 ASML curbs story; CSIS); NVDA China share down from ~90% to ~50%. Range not extreme enough. |
| ASML | $1797.32 | 85% | PUTS (threat, at highs) | Jul 15 2026 | 3 Sell / 23 Buy; passes | Mega-cap, last move only -2.4%; $1797 price makes any $1.50-ask strike require an unreachable move | R4-FAIL (feasibility glance) | Pool A. Proposed further US export curbs targeting ASML's DUV lithography sales to China (CNBC 4/7/26). Ratings genuinely pass but stopped at the mega-cap glance per audit Finding 1. |
| AMD | $557.89 | 94% | PUTS (threat, at highs) | Aug 4 2026 | 1 Sell / 30 Buy; fails | n/a | R3-FAIL | Pool A. Same chip export-control policy backdrop as NVDA; congressional buying in AI infra names also documented (Quiver/InsiderFinance summaries). Only 1 Sell. |
| MP | $52.27 | 14% | CALLS (bottom quartile) | Aug 6 2026 | 1 Sell, but Deutsche Bank cut PT to $61 TODAY (7/10/26); fresh cut | n/a | R3-FAIL | Pool A. China MOFCOM added MP Materials to its dual-use export control list 6/22/26 (Washington Post, Al Jazeera). Beaten down but disqualified by same-day target cut. |
| AA | $48.69 | 37% | OUT (mid) | Jul 16 2026 | 2 Sell / 5 Buy | n/a | MID-OUT | Pool A. Section 232 steel/aluminum/copper tariff overhaul (WH fact sheet 6/2026); stock has pulled back from its post-tariff highs into mid-range. BofA cut PT to $51 today. |
| CLF | $9.38 | 18% | CALLS (bottom quartile) | Jul 23 2026 | 2 Sell / 0 Buy; fails max-1 | n/a | R3-FAIL | Pool A. Steel tariff beneficiary (same WH proclamation) but capitulation already in progress: BofA/Citi cuts inside 30 days, consensus "Reduce." Exact trap Finding 2 describes. |
| NUE | $227.28 | 69% | OUT (below 75% cutoff) | Jul 27 2026 | 0 Sell | n/a | MID-OUT | Pool A. Steel tariff beneficiary; range not extreme. |
| CENX | $44.67 | 50% | OUT (mid) | Aug 6 2026 | 1 Sell | n/a | MID-OUT | Pool A. Aluminum tariff beneficiary; B. Riley cut PT to $74 on 7/7/26. Mid-range. |
| FSLR | $227.83 | 42% | OUT (mid) | Jul 30 2026 | 2 Sell / 19 Buy | n/a | MID-OUT | Pool A. Solar AD/CVD tariff beneficiary (DOC/USITC orders on SE Asian solar, PV Tech). Mid-range. |
| DHI | $151.53 | 40% | OUT (mid) | Jul 21 2026 | 2 Sell / 5 Buy | n/a | MID-OUT | Pool A. Softwood lumber tariff cost pressure on homebuilders (NAHB: ~$10k added per home); rate cut relief also pending (Commerce 7th review). Mid-range. |
| PHM | $124.83 | 47% | OUT (mid) | Jul 22 2026 | 0 Sell | n/a | MID-OUT | Pool A. Same lumber tariff angle as DHI. Mid-range. |
| TROW | $118.55 | 93% | PUTS (at highs) | Jul 31 2026 | 4 Sell / 0 Buy; passes strongly | Asset manager, moderate earnings mover, $118 price; required OTM strike likely exceeds 1.5x-cap | R5-R6-FAIL (pattern) | Pool B. Consensus "Reduce," 1.73/5 score; strongest ratings signal in either pool, but high dollar price kills feasibility at a glance. |
| AMCX | $9.92 | 86% | PUTS (at highs) | Aug 14 2026 | 2 Sell / 2 Hold; passes | Cheap stock, 6.35% avg earnings move vs ~9.5% cap (1.5x); plausibly reachable at $1.50 ask | **ADVANCE** | Pool B. See protocol flags below. |
| DBX | $29.19 | 70% | OUT (below 75% cutoff) | Aug 6 2026 | 2 Sell / 1 Buy | n/a | MID-OUT | Pool B. Just under the top-quartile line. |
| FHB | $30.13 | 94% | PUTS (at highs) | Jul 24 2026 | 3 Sell / 1 Buy; passes | Regional bank, low-vol earnings mover; required OTM strike unlikely to clear cap | R5-R6-FAIL (pattern) | Pool B. |
| INNV | $11.52 | 88% | PUTS (at highs) | Sep 8 2026 | 2 Sell / 1 Hold; passes | Microcap, options liquidity/chain data not resolvable via search | DATA-INSUFFICIENT | Pool B. |
| MMI | $30.74 | 69% | OUT (below 75% cutoff) | Aug 6 2026 | 2 Sell / 1 Hold | n/a | MID-OUT | Pool B. Just under the top-quartile line. |
| UNH | $425.05 | 95% | PUTS (at highs) | Jul 16 2026 | 1 Sell / 22 Buy; fails | n/a | R3-FAIL | Pool B. |
| ANET | $187.46 | 97% | PUTS (at highs) | Aug 4 2026 | 0 Sell | n/a | R3-FAIL | Pool B. |
| UNP | $287.27 | 98% | PUTS (at highs) | Jul 23 2026 | 0 Sell | n/a | R3-FAIL | Pool B. |
| FTNT | $157.51 | 92% | PUTS (at highs) | Jul 29 2026 | 5 Sell / 7 Buy; passes | Avg move 3.28%/8qtrs vs ~4.9% cap; $157 price + 66% 30-day run makes reachable-strike math tight | R5-R6-FAIL | Pool B. Best ratings signal of the large-cap batch but fails Rule 6 math at a glance. |
| NET | $268.46 | 90% | PUTS (at highs) | Jul 30 2026 | 4 Sell / 22 Buy; passes | $268 price, moderate-vol growth name; required OTM strike likely exceeds cap | R5-R6-FAIL (pattern) | Pool B. |
| CSX | $49.41 | 99% | PUTS (at highs) | Jul 22 2026 | 1 Sell / 16 Buy; fails | n/a | R3-FAIL | Pool B. |
| MPC | $283.60 | 97% | PUTS (at highs) | Aug 4 2026 | 0 Sell | n/a | R3-FAIL | Pool B. |
| PSX | $188.59 | 94% | PUTS (at highs) | Jul 24 2026 | 0 Sell | n/a | R3-FAIL | Pool B. |
| CNI | $124.46 | 98% | PUTS (at highs) | Jul 24 2026 | 0 Sell | n/a | R3-FAIL | Pool B. |
| JPM | $336.03 | 89% | PUTS (at highs) | Jul 14 2026 | 0 Sell | n/a | R3-FAIL | Pool B. |
| WELL | $231.32 | 91% | PUTS (at highs) | Jul 27 2026 | 0 Sell | n/a | R3-FAIL | Pool B. |
| PNC | $251.98 | 95% | PUTS (at highs) | Jul 15 2026 | 0 Sell | n/a | R3-FAIL | Pool B. |
| USB | $62.49 | 96% | PUTS (at highs) | Jul 16 2026 | 1 Sell / 16 Buy; fails | n/a | R3-FAIL | Pool B. |
| TRV | $338.80 | 89% | PUTS (at highs) | Jul 17 2026 | 3 Sell / 8 Buy; passes | Insurer, low-vol earnings mover, $338 price; beat estimates 4 straight qtrs (conviction-cap flag, moot) | R5-R6-FAIL | Pool B. |
| SMCI | $28.31 | 21% | OUT (bottom quartile; wrong pool) | Aug 4 2026 | 2 Sell | n/a | MID-OUT | Pool B intended; landed in bottom quartile, out of lane for this pool. |
| MIDD | $135.67 | 36% | OUT (mid) | Aug 5 2026 | 1 Sell | n/a | MID-OUT | Pool B intended; mid-range. |
| BRBR | $12.49 | 9% | OUT (bottom decile; wrong pool) | Aug 3 2026 | 1 Sell | n/a | MID-OUT | Pool B intended; landed in bottom decile after major decline, out of lane. |
| NTLA | $14.22 | 31% | OUT (mid) | Aug 6 2026 | 3 Sell | n/a | MID-OUT | Pool B intended; mid-range. |
| IONS | $58.25 | 39% | OUT (mid) | Aug 5 2026 | 1 Sell | n/a | MID-OUT | Pool B intended; mid-range. |
| ACGL | $101.06 | 82% | PUTS (at highs) | Jul 28 2026 | 1 Sell / 8 Buy; fails | n/a | R3-FAIL | Pool B. |
| NTRS | $183.55 | 97% | PUTS (at highs) | Jul 22 2026 | 2 Sell / 5 Buy; passes | Asset manager, moderate mover, $183 price; likely exceeds cap | R5-R6-FAIL (pattern) | Pool B. |
| EIX | $75.20 | 95% | PUTS (at highs) | Jul 30 2026 | 3 Sell / 4 Buy; passes | Utility, low-vol earnings mover (guidance reaffirmed, ~2% typical); Eaton Fire settlements >$500M are a liability tail-risk but not earnings-linked | R5-R6-FAIL | Pool B. |
| EQR | $68.72 | 80% | PUTS (at highs) | Jul 22 2026 | 0 Sell | n/a | R3-FAIL | Pool B. |
| ROIV | $35.97 | 96% | PUTS (at highs) | Aug 10 2026 | 1 Sell / 10 Buy; fails | n/a | R3-FAIL | Pool B. |

---

## ADVANCERS

1. **AMCX (AMC Networks); PUTS.** Price $9.92, 86th percentile of 52-week range ($5.41–$10.65). Ratings: 2 Sell / 2 Hold / 0 Buy, consensus "Reduce," PT $8.50 (~12.6% below spot). Earnings Aug 14 2026, well inside Aug/Sep window with ample DTE. Feasibility glance: 6.35% average earnings move against a ~9.5% cap (1.5x) on a sub-$10 stock; a reachable OTM strike at ≤$1.50 ask is plausible, not deep-chain-verified. Pool A citation: n/a (Pool B name; policy angle not applicable). **Puts protocol flags:** short interest; UNVERIFIED (marketbeat/nasdaq/fintel short-interest pages referenced in search but figure not resolved); M&A/strategic review/activist; soft, unconfirmed takeover speculation only (Seeking Alpha pieces call AMCX a "potential" target given low valuation/Dolan-family control, no active process or bid disclosed; not an auto-disqualify under the letter of the flag, but noted as a live overhang); consecutive beat-and-raise; none, last quarter (May 8 2026) was a miss ($0.08 vs $0.22 consensus), so no conviction cap; 30-day consensus EPS revision direction; UNVERIFIED (not resolvable via search in glance time).

No Pool A names advanced. No other Pool B names advanced.

---

## BASE RATES

**Pool A (22 screened):**
- MID-OUT (range percentile, line 1): 13; GILD, REGN, NVS, NVO, AZN, GSK, NVDA, AA, NUE, CENX, FSLR, DHI, PHM
- R2 (earnings-window fail): 0
- R3 (ratings-direction fail): 6; LLY, JNJ, ABBV, AMD, MP, CLF
- R5-R6 (feasibility-fail): 3; AMGN, SNY, ASML
- DATA-INSUFFICIENT: 0
- ADVANCE: 0

**Pool B (30 screened):**
- MID-OUT (range percentile, line 1): 7; DBX, MMI, SMCI, MIDD, BRBR, NTLA, IONS
- R2 (earnings-window fail): 0
- R3 (ratings-direction fail): 14; UNH, ANET, UNP, CSX, MPC, PSX, CNI, JPM, WELL, PNC, USB, ACGL, EQR, ROIV
- R5-R6 (feasibility-fail): 7; TROW, FHB, FTNT, NET, TRV, NTRS, EIX
- DATA-INSUFFICIENT: 1; INNV
- ADVANCE: 1; AMCX

**Combined (52 screened):** MID-OUT 20, R2-fail 0, R3-fail 20, R5-R6-fail 10, DATA-INSUFFICIENT 1, ADVANCE 1.

The dominant pattern this run: high-dollar-price large/mega-caps (LLY, ASML, AMGN, TROW, FTNT, NET, TRV, NTRS) routinely clear range-percentile and ratings direction but die at the Rule 5/6 feasibility glance, exactly as Finding 1 of the audit predicted. The zero-Sell filter also did real work on the calls side in Pool A: JNJ, ABBV clear range but sit at 0 Sells despite being at 52-week highs, which is really the puts-side mirror of Finding 2 (capitulation hasn't started).

---

## GLOSSARY

- **Range percentile:** Where a stock's current price sits between its 52-week low (0%) and 52-week high (100%). Pool A calls candidates need bottom quartile (≤25%); Pool A puts and all of Pool B need top quartile (≥75%, "top 20-25% of range"); anything else is MID-OUT.
- **MID-OUT:** Screen verdict for a name whose range percentile falls in the 25-75% band; neither beaten-down enough for calls nor high enough for puts. Killed at line 1 of the funnel.
- **R3-FAIL:** Screen verdict for a name that passes range percentile but fails the ratings-direction filter (calls: more than 1 Sell, or a downgrade/target cut in the trailing 30 days; puts: fewer than 2 Sell/Underperform ratings and no documented Buy-to-Sell downgrade in 30 days).
- **R5-R6-FAIL / feasibility glance:** Screen verdict for a name that passes range and ratings but fails the combined Rule 5 (option ask ≤$1.00 calls / ≤$1.50 puts) and Rule 6 (required move to reach that strike ≤1.5x the stock's typical earnings-day move) test at a glance-level check, without pulling the full chain.
- **DATA-INSUFFICIENT:** Verdict for a name where a required data point (usually options liquidity/chain depth) could not be resolved via search in screen-tier time, so the name is logged and dropped rather than guessed at.
- **DTE:** Days to expiration.
- **Annex III:** The list of 17 named pharmaceutical companies subject to the accelerated (Jul 31 2026, vs. the standard Sep 29 2026) effective date under the April 2 2026 Section 232 pharmaceutical tariff proclamation.
- **Section 232:** Trade Expansion Act of 1962 provision allowing tariffs on imports found to threaten national security; the legal basis for the 2026 pharmaceutical, steel/aluminum/copper, and (pending) copper tariff actions cited in this log.
- **AD/CVD:** Antidumping/countervailing duty; the trade-remedy tariff mechanism used against Southeast Asian solar imports (cited for FSLR).
- **Buy-to-Sell downgrade:** An analyst rating change directly from Buy to Sell in one move. Counts toward the puts ratings threshold; a Buy-to-Hold move does not.
- **Consensus rating / rating score:** MarketBeat's aggregated analyst view (e.g., "Moderate Buy," "Reduce") and its underlying 1-5 numeric average, used here as a quick cross-check alongside the raw Buy/Hold/Sell counts.
- **Squeeze / short interest / days-to-cover (puts protocol flags):** Per the audit's Finding 5 and the puts protocol, every puts ADVANCE must record short interest as a percent of float (squeeze-warning if >10%), and days-to-cover, as fuel-gauge context even though the mechanism mainly matters for calls.
- **M&A/strategic review/activist flag:** Mandatory puts-protocol check for any live acquisition process, strategic review, or activist campaign, which would auto-disqualify a puts thesis (a takeover bid caps downside). Distinguished here from unconfirmed market speculation, which is noted but not auto-disqualifying.
- **Beat-and-raise streak (conviction cap):** Four or more consecutive quarters of EPS beats plus raised guidance caps conviction on a puts thesis, since a name with that pattern is statistically likelier to beat again than miss.
- **EPS revision direction:** Whether sell-side consensus EPS estimates have moved up or down over the trailing 30 days; a required puts-protocol data point on every ADVANCE.
- **UNVERIFIED:** A data point that could not be confirmed via live search within screen-tier time; recorded rather than fabricated, per the log's data rules.

