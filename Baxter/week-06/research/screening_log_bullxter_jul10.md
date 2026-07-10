# SCREENING LOG: BULLXTER, JULY 10, 2026

**Slice:** 50 unique names from the high-short-interest / retail-sentiment hunting ground (short interest greater than 10% of float, or heavy r/wallstreetbets and r/stocks mention volume).

**Method note:** This is the screen tier only (lines 1 to 4 of the 13-line funnel in selection_criteria_audit_jul10.md), not full DD. Four steps per name: (1) 52-week range percentile to set direction (bottom quartile: calls, top quartile: puts, middle: MID-OUT), (2) confirmed earnings date inside the Aug/Sep 2026 expiry window (puts need 21+ DTE at entry), (3) ratings direction filter (calls: max 1 Sell/Underperform and no downgrades or target cuts in 30 days; puts: minimum 2 Sell/Underperform or a documented Buy-to-Sell downgrade within 30 days), (4) feasibility glance (Rule 5 plus Rule 6 joint check: an option ask at or below $1.00 for calls, $1.50 for puts, at a strike whose required move to breakeven is no more than 1.5x the stock's typical earnings-day move). All data sourced live via WebSearch/WebFetch. No Robinhood scripts used (auth conflicts with parallel agents). Any unverifiable figure is marked UNVERIFIED, not guessed. Thin-data names are marked DATA-INSUFFICIENT and passed over.

Excluded universe (already held, screened, or watched, skipped entirely): ABT, TRMB, UBER, LYFT, LVS, ZG, DIS, TSLA, DASH, ABNB, RCL, TTD, DKNG, MDT, NKE, CCL, BSX, HITI, DSGX, CHWY, CMG, MCD, WEN, SBUX, KVUE, MDLZ, YUM, EL, ISRG, PFE, BMY, CI, ELV, MRK, HUM, MEDP, VEEV, CELH, PLTR, COIN, SNOW, MDB, LULU, HOOD, DUOL, STZ, KBH, WGO, CALM, ZTS, FLUT, STE, GEHC, EQT, EXE, FIS, AVY, SNDK, AAPL, SOFI, KO.

---

## SCREENING TABLE

| Ticker | Price | Range % | Direction | Earnings date | Ratings check | Feasibility | Verdict | Note |
|---|---|---|---|---|---|---|---|---|
| GME | $21.77 | 22.5% | bottom quartile (calls) | ~Sep 8-9 2026, UNVERIFIED (not yet company-confirmed) | 1 analyst, Sell, target $13.50 | not reached | R2 | SI 12.7-14.2% of shares outstanding fits slice; earnings date is forecast-only, not company-confirmed, so fails the "confirmed" requirement |
| AMC | $1.90 | 36.3% | MID-OUT | - | - | - | MID-OUT | - |
| CVNA | $65.02 | 24.6% | bottom quartile (calls) | Jul 29, 2026 (confirmed) | Strong Buy: 14 Buy/3 Mod Buy/5 Hold/0 Sell; last downgrade Apr 6 (>30d) | not reached | R2 | Earnings falls Jul 29, outside the Aug/Sep 2026 window; would otherwise have cleared R3 easily |
| UPST | $33.23 | 14.6% | bottom quartile (calls) | Aug 4, 2026 (confirmed) | 6 Buy/6 Hold/0 Sell, no downgrades found in last 30d | Plausible: high-IV small cap, ~20%+ OTM strike likely ≤$1 ask (UNVERIFIED, no live chain access); last print moved -7.9% (UNVERIFIED full 4-8 print history, paywalled) | ADVANCE | SI 28.03% of shares outstanding, strong squeeze fuel; Rule 6 reachability needs full DD earnings-move table |
| RIVN | $18.24 | 60.0% | MID-OUT | - | - | - | MID-OUT | - |
| LCID | $5.60 | 3.9% | bottom quartile (calls) | Aug 4-10, 2026 (window, exact date UNVERIFIED) | 1 Buy/8 Hold/3 Sell | not reached | R3 | SI 42.2% of float is huge but 3 Sell ratings exceeds the max-1 calls filter |
| NIO | $4.78 | 28.5% | MID-OUT | - | - | - | MID-OUT | - |
| PLUG | $2.27 | 27.6% | MID-OUT (borderline) | - | - | - | MID-OUT | - |
| FUBO | $9.52 | 3.2%* | bottom quartile* | Aug 7, 2026 (confirmed) | Strong Buy, 0 Sell | not reached | DATA-INSUFFICIENT | *52-wk high $56.64 looks like a pre-merger (Hulu+Live TV combination) capital-structure artifact, range % likely not comparable; SI only 6.58% of shares outstanding, below the 10% slice threshold either way |
| BYND | $0.68 | 2.5% | bottom quartile (calls) | Aug 12, 2026 (confirmed) | Moderate/Strong Sell: 0 Buy/3 Hold/3 Sell | not reached | R3 | SI 31-33% of float is enormous but Sell consensus kills calls; sub-$1 share price also raises delisting-risk flag for later |
| WOLF | $38.00 | 41.2% | MID-OUT | - | - | - | MID-OUT | - |
| OPEN | $5.28 | 44.9% | MID-OUT | - | - | - | MID-OUT | - |
| IONQ | $44.77 | 32.1% | MID-OUT | - | - | - | MID-OUT | - |
| RGTI | $16.83 | 10.3% | bottom quartile (calls) | Aug 6-10, 2026 (window, exact date UNVERIFIED) | Buy consensus, target $29.24 (+73%); no downgrades found | Plausible: small-cap high-IV name, wide 52wk range ($12-58) implies large historical swings, OTM call ≤$1 UNVERIFIED pending live chain | ADVANCE | SI 15.16% of shares outstanding |
| QUBT | $9.16 | 15.2% | bottom quartile (calls) | Aug 19, 2026 (confirmed) | Buy consensus (Northland Outperform), target $17.83 (+58%); no downgrades found | Plausible: sub-$10 high-IV quantum name, OTM call ≤$1 UNVERIFIED pending live chain | ADVANCE | SI 26.07% of shares outstanding |
| SMCI | $28.24 | 20.4% | bottom quartile (calls) | Aug 11, 2026 (confirmed) | Hold consensus: 10 Buy/24 Hold/5 Sell | not reached | R3 | 5 Sell ratings (12.8%) exceeds max-1 calls filter despite SI 19.71% of float |
| MARA | $13.89 | 43.1% | MID-OUT | - | - | - | MID-OUT | - |
| RIOT | $21.60 | 55.8% | MID-OUT | - | - | - | MID-OUT | - |
| MSTR | $93.89 | 3.2% | bottom quartile (calls) | Jul 30, 2026 (confirmed) | Buy-leaning (B.Riley, HC Wainwright, Cantor, TD Cowen all Buy/Overweight) | not reached | R2 | Earnings Jul 30 falls outside the Aug/Sep 2026 window; SI 11.63% of shares outstanding would have fit |
| CLSK | $12.89 | 31.3% | MID-OUT | - | - | - | MID-OUT | - |
| HUT | $108.25 | 73.3% | MID-OUT (borderline top) | - | - | - | MID-OUT | - |
| SIRI | $29.24 | 81.3% | top quartile (puts) | Jul 30, 2026 (confirmed) | Mixed: Seaport downgrade Buy→Neutral Feb 6; JPM upgrade Feb 10 | not reached | R2 | Earnings Jul 30 falls outside Aug/Sep window; SI 13.93% of shares outstanding |
| GPRO | $0.78 | 7.7% | bottom quartile (calls) | Aug 10, 2026 (UNVERIFIED, one source says Jul 30) | No Sell flagged, target $1.41 (7 analysts); breakdown UNVERIFIED | Only ~7 call strikes/contracts found for nearest expiry - chain too thin to locate a reliable OTM strike | DATA-INSUFFICIENT | Sub-$1 stock; SI 12-15% fits slice but options chain liquidity looks too thin to screen reliably |
| CLOV | $4.49 | 72.6% | MID-OUT (borderline top) | - | - | - | MID-OUT | - |
| SPCE | $2.56 | 6.4% | bottom quartile (calls) | Jul 30, 2026 (confirmed) | Mixed: 2 Buy/4 Hold/1 Sell | not reached | R2 | Confirmed earnings Jul 30 falls outside Aug/Sep window |
| CHPT | $5.75 | 13.8% | bottom quartile (calls) | Sep 2, 2026 (confirmed) | Hold consensus: 13% Strong Buy/0% Buy/63% Hold/13% Sell/13% Strong Sell (~26% Sell combined, 24 analysts) | not reached | R3 | Sell/Strong Sell ~26% of coverage far exceeds max-1 calls filter |
| BLNK | $0.60 | 6.8% | bottom quartile (calls) | Aug 17, 2026 (confirmed) | Moderate Buy: 2 Buy/1 Hold/0 Sell (small sample, 3 analysts) | Sub-$1 stock, cheap strikes plausible ≤$1 ask (UNVERIFIED live chain); flagged risk below | ADVANCE (caution) | SI 25.5% of float; company is under a Nasdaq minimum-bid-price compliance extension to Jan 2027 - real delisting risk, DD should weigh this hard under decline-category test before pitching |
| AFRM | $82.54 | 69.8% | MID-OUT | - | - | - | MID-OUT | - |
| PTON | $5.93 | 41.1% | MID-OUT | - | - | - | MID-OUT | - |
| DNUT | $3.52 | 22.5% | bottom quartile (calls, borderline) | Aug 6, 2026 (confirmed) | Hold consensus, Sell count 2-3 depending on source (of 7-14 analysts) | not reached | R3 | Sell count exceeds max-1 calls filter regardless of which source is used |
| KSS | $16.25 | 44.0% | MID-OUT | - | - | - | MID-OUT | - |
| GT | $6.64 | 19.5% | bottom quartile (calls) | not found in window (last report May 6; next UNVERIFIED) | "Reduce" consensus: 3 Sell/4 Hold/2 Buy | not reached | R3 | Sell count of 3 kills calls filter regardless of earnings-date question; SI 11.5% of shares outstanding would have fit |
| XRX | $2.74 | 27.6% | MID-OUT (borderline) | - | - | - | MID-OUT | - |
| BBAI | $3.34 | 5.2% | bottom quartile (calls) | Aug 10, 2026 (confirmed) | Buy consensus, 78% buy (3 analysts), no downgrades found | Plausible: sub-$4 high-IV name, OTM call ≤$1 UNVERIFIED pending live chain | ADVANCE | SI 21-29% of float (source-dependent), defense-AI retail favorite |
| SOUN | $6.68 | 5.2% | bottom quartile (calls) | Aug 6, 2026 (confirmed) | Outperform maintained (Northland, May 8); last rating action was an upgrade (Cantor, Dec 2025), no downgrades found | Plausible: sub-$10 high-IV name, OTM call ≤$1 UNVERIFIED pending live chain | ADVANCE | SI 38-40% of float - one of the most-shorted >$2B names on the tape |
| ACHR | $4.88 | 2.7% | bottom quartile (calls) | Aug 6, 2026 (confirmed) | Buy consensus (6-9 analysts), target $10.61 (+119%), no downgrades found | Plausible: sub-$5 high-IV name, OTM call ≤$1 UNVERIFIED pending live chain | ADVANCE | SI 11-14% of float, right at the slice threshold |
| JOBY | $7.87 | 1.5% | bottom quartile (calls) | Aug 12, 2026 (confirmed) | Hold consensus; Sell count 1-3 depending on source; multiple target cuts inside 30d (Canaccord $15.50→$11.50, Deutsche Bank $7→$6, JPMorgan $8→$7) | not reached | R3 | Fresh target cuts in the last 30 days disqualify regardless of Sell-count ambiguity |
| LAZR | $2.28 | N/A | N/A | - | - | - | DATA-INSUFFICIENT | Ticker shows as LAZRQ on retail platforms and search results reference Chapter 11 proceedings; 52-wk high dated May 2025 is stale/outside window - screened out as likely bankrupt/reorganized |
| MVIS | $0.38 | 8.3% | bottom quartile (calls) | Aug 6, 2026 (confirmed) | Buy consensus, 83% buy, target $5.00 | Sub-$1 stock but options chain confirmed active across multiple platforms (Yahoo/Fidelity/Market Chameleon); cheap strikes plausible ≤$1 ask UNVERIFIED live price | ADVANCE | SI 22.2% of float, 14.7 days-to-cover, explicitly flagged as a squeeze candidate by outside sources |
| TLRY | $4.37 | N/A | N/A | - | - | - | DATA-INSUFFICIENT | 52-wk high of $23.20 is inconsistent with TLRY's known post-reverse-split trading range and looks like a stale/bad data point; range percentile not reliable enough to sort direction |
| CGC | ~$1.31 | 30.3% | MID-OUT | - | - | - | MID-OUT | Sources conflict ($0.95 "current price" vs $1.16-1.47 day range after a reported 28% cannabis-rally surge); used the post-surge figure |
| SNDL | $1.37 | 12.6% | bottom quartile (calls) | not found within Aug/Sep window | Strong Buy, target $5.00 | not reached | R2 | SI only 0.67% of shares outstanding - well below the slice's 10% short-interest bar, and no confirmed earnings date in window either |
| ACB | $2.69 | 1.4% | bottom quartile (calls) | not found within window (next report window appears to have already passed, ~Jun 16-22) | Effectively no active analyst coverage (1 stale Neutral) | not reached | R2 | No confirmed Aug/Sep earnings date; thin analyst coverage would also make R3 unreliable |
| BB | $10.91 | 74.4% | MID-OUT (borderline top) | - | - | - | MID-OUT | Stock hit fresh 52-wk highs Jul 1 - close to the puts threshold but stayed under 75% |
| KOSS | $3.90 | 7.9% | bottom quartile (calls) | Aug 6, 2026 (window, one conflicting May source) | 0 Buy/10 Hold/0 Sell - clears calls filter | Could not confirm any live options quotes/strikes despite chain existing on major platforms | DATA-INSUFFICIENT | SI only 4.58% of available shares - qualifies for the slice on retail-meme reputation only, not short interest; option liquidity unverifiable |
| ATER | $1.19 | 49.6% | MID-OUT | - | - | - | MID-OUT | - |
| IEP | $7.31 | 8.6% | bottom quartile (calls) | Aug 3, 2026 (window) | 84% buy consensus (5 analysts) | not reached | DATA-INSUFFICIENT | SI only 2.40% of shares outstanding and no evidence of heavy WSB/retail chatter - doesn't clear either slice qualifier; corrected out here rather than advanced |
| BTBT | $1.71 | 13.9% | bottom quartile (calls) | Aug 10-13, 2026 (window) | Strong Buy (5 analysts), but B. Riley cut target to $4 from $5 while keeping Buy | not reached | R3 | Fresh target cut inside the lookback window disqualifies under the calls ratings-momentum filter |
| CIFR | $23.37 | 73.5% | MID-OUT (borderline top) | - | - | - | MID-OUT | - |
| WULF | $23.62 | 75.3% | top quartile (puts) | Aug 17, 2026 (window, 21+ DTE OK) | Buy consensus (14 analysts), no downgrades found - targets being raised (e.g. MS to $72) | not reached | R3 | Puts need min-2-Sell or a fresh Buy-to-Sell; this is the opposite, a name getting upgraded on an Anthropic data-center lease. SI 22-32% of float also flags squeeze risk against a short thesis |

---

## ADVANCERS

Ranked by conviction on the data available. All eight are calls candidates (the screen produced zero surviving puts names this run - the only two top-quartile names found, SIRI and WULF, both died at R2/R3). None of these have been through Rule 5/6 chain math or the 13-line DD funnel; they are screen passes only.

1. **SOUN (SoundHound AI)** - $6.68, 5.2 percentile (deep bottom quartile). SI 38-40% of float, reported as one of the most-shorted >$2B names on the tape. Outperform maintained in May with no downgrades since; last rating action was an upgrade. Earnings confirmed Aug 6, 2026. Best combination of squeeze fuel and clean ratings in the batch.
2. **MVIS (MicroVision)** - $0.38, 8.3 percentile. SI 22.2% of float with a 14.7-day cover ratio; independently flagged elsewhere as a squeeze setup. Buy consensus 83%. Earnings confirmed Aug 6, 2026. Sub-$1 price is a real feasibility wildcard but options chain is confirmed active on multiple major platforms, unlike the penny names that got screened out.
3. **QUBT (Quantum Computing Inc)** - $9.16, 15.2 percentile. SI 26.07% of shares outstanding. Buy consensus (Northland Outperform), earnings confirmed Aug 19, 2026.
4. **BBAI (BigBear.ai)** - $3.34, 5.2 percentile. SI 21-29% of float depending on source. Buy consensus (78%), earnings confirmed Aug 10, 2026. Known defense-AI retail name.
5. **UPST (Upstart)** - $33.23, 14.6 percentile. SI 28.03% of shares outstanding, 0 Sell/6 Buy/6 Hold. Earnings confirmed Aug 4, 2026.
6. **ACHR (Archer Aviation)** - $4.88, 2.7 percentile (essentially at the 52-week low). SI 11-14% of float, right at the slice's threshold rather than deep in it. Buy consensus, earnings confirmed Aug 6, 2026.
7. **RGTI (Rigetti Computing)** - $16.83, 10.3 percentile. SI 15.16% of shares outstanding. Buy consensus, earnings window confirmed but exact day (Aug 6 vs Aug 10) unverified.
8. **BLNK (Blink Charging)** - $0.60, 6.8 percentile. SI 25.5% of float, ratings sample is thin (3 analysts). Weakest advancer: the company is under a Nasdaq minimum-bid-price compliance extension through Jan 2027, a real delisting risk that DD should test hard under the Finding-4 decline-category framework before this gets anywhere near a pitch.

## BASE RATES

Of the 50 names screened:

| Outcome | Count | Names |
|---|---|---|
| MID-OUT (range percentile, line 1) | 20 | AMC, RIVN, NIO, PLUG, WOLF, OPEN, IONQ, MARA, RIOT, CLSK, HUT, CLOV, AFRM, PTON, KSS, XRX, CGC, BB, ATER, CIFR |
| R2 (earnings date, line 2) | 7 | GME, CVNA, MSTR, SIRI, SPCE, SNDL, ACB |
| R3 (ratings direction, line 3) | 9 | LCID, BYND, SMCI, CHPT, DNUT, GT, JOBY, BTBT, WULF |
| R5-R6 (feasibility, line 4) | 0 | none died here - everything that cleared R1-R3 either advanced or was already thin enough to call DATA-INSUFFICIENT |
| DATA-INSUFFICIENT | 6 | FUBO, GPRO, LAZR, TLRY, KOSS, IEP |
| ADVANCE | 8 | UPST, RGTI, QUBT, BLNK, BBAI, SOUN, ACHR, MVIS |

Notes on the shape of this run: MID-OUT was the single biggest killer at 40% of the slice, consistent with the fact that a name being heavily shorted or retail-chattered doesn't automatically mean it sits at a 52-week extreme - plenty of these names (RIOT, MARA, AFRM, HUT, CIFR) were mid-range momentum names, not dislocations. R3 (ratings) was the second-biggest killer and it was almost always a Sell-count problem rather than a fresh-downgrade problem - several high-SI names (LCID, SMCI, GT, DNUT, BYND) had genuine 3+ Sell rating counts, meaning the ratings-direction filter is doing real work on this slice rather than the "barely filters anything" pattern the audit found on the calls-at-lows universe generally. Zero puts names survived to ADVANCE; the two top-quartile names found (SIRI, WULF) both had earnings outside the window or bullish-leaning ratings that fail the puts filter outright - momentum names near highs tend to have improving, not deteriorating, ratings, which is exactly why puts are harder to source from this slice. DATA-INSUFFICIENT clustered around sub-$1 penny names with unverifiable or clearly thin options liquidity (FUBO, GPRO, KOSS) plus two names with corrupted-looking 52-week range data (LAZR - likely Chapter 11/ticker-Q, TLRY - implausible high) and one name (IEP) that technically cleared the funnel steps but never actually met the slice's short-interest-or-retail-sentiment qualifier on closer look.

## GLOSSARY

- **52-week range percentile:** Where a stock's current price sits between its 1-year low (0%) and high (100%). Bottom quartile (0-25%) sets up calls; top quartile (75-100%) sets up puts; the 25-75% middle is MID-OUT.
- **MID-OUT:** Screen shorthand for a name that lands in the middle of its 52-week range and is dropped immediately, before any further research, per the token-discipline rule.
- **Bottom quartile / top quartile:** The bottom or top 25% of a stock's 52-week trading range, used to set calls-vs-puts direction under Rule 1.
- **DTE:** Days to expiration. Puts need at least 21 days between entry and earnings under Rule 2.
- **Short interest:** The number of shares currently sold short, expressed as a percent of either shares outstanding or of float (see below) depending on the data source - this screen notes which basis was used wherever the two diverge.
- **Float:** The subset of a company's shares actually available for public trading (excludes insider/locked-up shares). Short interest as a percent of float is usually a larger, more meaningful number than short interest as a percent of total shares outstanding.
- **Days-to-cover:** How many days of average trading volume it would take short sellers to buy back their entire position. A high days-to-cover with high short interest is the classic squeeze setup.
- **Squeeze:** Forced short-covering that accelerates a rising price, cited here (MVIS, SOUN) as the mechanism that would actually pay a far-OTM call inside a short option window.
- **Consensus rating / Buy-Hold-Sell breakdown:** The aggregate of individual analyst ratings on a stock. This screen requires the full Buy/Hold/Sell count, not just the headline consensus label, because a "Hold" or "Buy" consensus can still hide enough Sell ratings to fail the calls filter (e.g. DNUT, SMCI).
- **Price target / target cut:** An analyst's 12-month expected share price. A "target cut" (lowering the number without necessarily changing the rating) still counts against the calls ratings-momentum filter if it happened in the last 30 days (e.g. BTBT/B. Riley).
- **Downgrade:** A change in an analyst's rating in a more bearish direction (e.g. Buy to Neutral). Distinct from a target cut, which can happen without a rating change.
- **Buy-to-Sell downgrade:** The specific, sharper version of a downgrade the puts filter looks for - an analyst moving straight from Buy to Sell/Underperform, treated as a stronger bearish signal than a routine one-notch downgrade.
- **OTM (out-of-the-money):** An option strike beyond the current stock price (above for calls, below for puts) that has no intrinsic value, only time/volatility value.
- **Ask price:** The price a buyer would currently pay to open an option position. Rule 5 caps this at $1.00 for calls and $1.50 for puts at the researched strike.
- **Implied volatility (IV):** The options market's forward-looking estimate of how much a stock will move, baked into the option's price. Higher IV generally means cheaper OTM strikes are available further from the current price for the same dollar cost.
- **Required move / breakeven:** How far the stock needs to move for the purchased option to be worth what was paid for it. Rule 6 caps this at 1.5x the stock's typical earnings-day move.
- **Feasibility glance:** The screen-tier, non-precise version of the Rule 5/Rule 6 check - a plausibility judgment rather than a live-chain-verified number, used to decide whether a name is even worth a full DD pass.
- **DATA-INSUFFICIENT:** Verdict used when the data needed to make a screening call is too thin, contradictory, or unverifiable to trust (thin options chains, conflicting 52-week ranges, apparent bankruptcy/ticker changes) - the name is dropped, not guessed at.
- **UNVERIFIED:** A figure that could not be confirmed against a reliable live source but is included anyway with this flag, rather than omitted or fabricated.
- **R2 / R3 / R5-R6:** Shorthand in the base-rate table for which funnel line killed a name - line 2 (confirmed earnings date), line 3 (ratings direction filter), or lines 5-6 (Rule 5/Rule 6 feasibility, from the DD tier, referenced here as the outer bound the screen's feasibility glance approximates).
- **Minimum bid price compliance / delisting risk:** A Nasdaq (or NYSE) requirement that a stock trade above $1.00; falling below it for an extended period triggers a compliance period and, eventually, delisting risk if the price doesn't recover (flagged for BLNK).
- **M&A / activist auto-disqualify:** A standing rule (referenced for puts specifically) that a name under an active M&A process or activist campaign is dropped regardless of other screen results, because deal mechanics can override normal price action.
- **Beat-and-raise:** A pattern of a company beating earnings estimates and raising forward guidance in the same report; four or more consecutive beat-and-raise quarters caps a puts thesis regardless of other factors, since the trend argues against a downside surprise.
- **EPS revision (30-day direction):** Whether Wall Street's consensus earnings-per-share estimate for a stock has been moving up or down over the trailing 30 days; falling estimates into a print raise miss risk for puts, rising estimates raise miss risk for a short-the-beat calls thesis.
