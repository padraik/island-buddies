# POST-MORTEM: THE 202-NAME SCREEN
*Baxter's desk, Saturday July 12, 2026. The question on the table: 202 names went in, zero positions came out. Is that the funnel working, or the funnel welded shut? The data answers both ways, and the difference matters.*

---

## 1. WHAT HAPPENED, IN ONE TABLE

Aggregate mortality across all four July 10 screening logs (Bullxter 50, Bearxter 50, Macxter 52, Calxter 50) plus the evening triage and the SOUN DD:

| Stage | Kills | % of 202 | Cumulative survivors |
|---|---|---|---|
| R1 range percentile (MID-OUT + wrong-direction) | 78 | 38.6% | 124 |
| R3 ratings direction (hardened) | 55 | 27.2% | 69 |
| Decline category, screen tier (Bearxter's door-kills) | 19 | 9.4% | 50 |
| R5/R6 feasibility glance | 18 | 8.9% | 32 |
| R2 earnings window | 10 | 5.0% | 22 |
| DATA-INSUFFICIENT + out-of-lane | 11 | 5.4% | 11 |
| **ADVANCE to triage** | | | **11** |
| Triage line 5 (decline category, full check) | 6 | | 5 |
| Triage lines 7-8 (live chains) | 4 | | 1 |
| DD line 11 (estimate revisions), SOUN | 1 | | **0** |

Zero entries. The reserve stayed at $527.

## 2. WAS 0/202 ON MODEL, OR OFF MODEL?

Multiply the observed per-line pass rates through the funnel: R1 passes ~61%, R3 passes ~44% of those, category ~72% of those (screen tier), R5/6 glance ~64%, everything else ~50% joint, triage survival 1-in-11, line 11 roughly a coin flip. The compound survival probability is in the neighborhood of **0.2-0.5%, which predicts 0.5 to 1 survivor per 200 names.**

We got exactly 1 survivor to full DD (SOUN, 0.5%), and it died on a fair, pre-committed gate. **The funnel produced precisely the yield its own math predicts.** Nothing is broken. But the corollary is uncomfortable and has to be said out loud: **at this yield, one entry costs roughly 200-400 screened names.** If we want one to two entries per month, we either screen 400+ names a month inside the token budget, or we raise the yield per name screened. The budget rule (10-20 names per session, inline) means brute force is not available. The yield has to come up. Sections 4-6 are how.

## 3. WHERE THE FUNNEL IS TELLING THE TRUTH

Three lines did exactly the job they were written to do, and the post-mortem's first duty is to say so before touching anything:

- **R1 killed 38.6% for one search each.** Cheapest kill in the funnel. No change.
- **The decline-category test (line 5) killed 25 names total (19 at Bearxter's screen, 6 at triage), and every one of them reads correctly in hindsight.** MVIS/BLNK/BBAI are dilution treadmills; QUBT/RGTI are bubble deflation; the SaaS names are sector beta. Not one of those 25 has since produced news that makes us wrong. No change.
- **The chain checks (lines 7-8) went 4-for-4 against the screen-tier feasibility glance.** UPST, HAS, ORLY, AMCX all passed the web glance and all died on live chains. Chains are truth. Already codified.

And the retroactive control: Rule 6 would have blocked TRMB, UBER, LVS, and ABT as structured — four positions currently worth less than we paid for them, carrying $371 of the $551 deployed. The hardened funnel refusing 202 names is the same instrument that would have refused the four positions currently bleeding. **The tightness is not a bug. The tightness is the lesson of June, priced in.**

## 4. FINDING ONE: THE GEOMETRY BOTTLENECK IS THE REAL FILTER — SO SCREEN ON GEOMETRY FIRST

Look at what actually killed the 11 advancers: 6 died on decline category, 4 died on chain geometry, and the survivor (SOUN) was a cheap stock with a violent earnings distribution. Look at what killed AMGN, ASML, SNY, TROW, FTNT, NET, TRV, NTRS, FICO, MAR, HLT at the glance: high price, modest move. The pattern across all 202:

**Rules 5+6 jointly define a narrow admissible geometry: stock price roughly $3-40, median earnings-day move ≥6%, liquid chain.** Outside that box, no thesis matters — there is no instrument. Inside that box, most residents are structurally broken (which line 5 catches), but *every* possible entry lives there.

The July 10 run selected slices by STORY (short interest, quality dislocation, policy) and then let geometry kill 90%+ of survivors at the expensive end of the funnel. That is backwards. **The fix: build future screening batches from the geometry box first — price and range via `fetch_price.py` (free), chain affordability via the chain scripts (free) — and only then spend searches on the names that already own a viable instrument.** The July 10 run couldn't do this (parallel agents couldn't share Robinhood auth, so chains came last). Inline screening has no such constraint. Geometry costs zero tokens now. Story costs searches. Cheap truth before expensive narrative.

## 5. FINDING TWO: R1 AND R3 FIGHT EACH OTHER ON A CLOCK, AND FRESH-LOW LISTS LOSE THAT FIGHT

Calxter's control group is the cleanest evidence in the record: **73% of R1 survivors died at R3** — nearly every bottom-quartile name carried fresh downgrades/target cuts (capitulation in progress), and nearly every top-quartile name carried fresh upgrades (wrong direction for puts). Ratings momentum points WITH price at the extremes, not against it.

The funnel therefore only admits a name inside a specific time window: **the decline must be old enough that the last analyst cut is >30 days stale, but recent enough that the price hasn't bounced out of the bottom quartile.** Call it the stabilization window. It probably lasts two to six weeks per name. A screen built from "stocks at 52-week lows this week" systematically catches names BEFORE the window opens (knife still falling, R3 kills them — MAT, OLLI, OLN, OPCH, ORA, MORN, all of Calxter's casualties). A screen built from "stocks that hit their 52-week low 4-10 weeks ago and are still within a few percent of it" catches names INSIDE the window.

**The fix: change the sourcing question from "what is at a low now" to "what fell 1-3 months ago and has gone quiet."** OLED is the proof this class exists: bottomed in the spring, all its target cuts aged past 30 days, cleared R1-R2-R3 clean in the control group of all places — and died only on unverifiable chain data, which the local scripts can now verify for free. OLED gets re-checked in this weekend's batch.

## 6. FINDING THREE: THE PUTS SIDE OF THE SCREEN IS BURNING BUDGET AT NEAR-ZERO YIELD

Zero puts advanced from 202 names, and it wasn't close. The two-Sell requirement plus the no-fresh-high check plus the price/vol geometry left nothing: names at highs carry improving ratings (Macxter's Pool B: 14 of 30 died at R3 alone), and the rare names WITH standing Sells at highs are low-vol financials/REITs/utilities that can never clear Rule 6 (TROW, FHB, TRV, NTRS, EIX, NNN). The single puts advancer (AMCX) died three separate ways.

On top of the structural starvation: **live puts entry is blocked anyway until the passes.md back-test runs (Calxter's deadline, Jul 31).** We spent something like a third of the July 10 search budget screening a direction we are not allowed to trade.

**The fix: no dedicated puts pools in any screening batch until the back-test unblocks the system.** Puts candidates that fall out of a calls-oriented batch incidentally (a top-quartile name with a genuine Sell cluster and small-cap-violent geometry) get logged to the watch list and nothing more. This is a budget rule, not a strategy retreat — the back-test is still the gate, and it still runs by Jul 31.

## 7. FINDING FOUR: DATA-INSUFFICIENT IS LEAKING REAL CANDIDATES

Eight names died as DATA-INSUFFICIENT at the screen tier, and at least two of them (OLED, NXST) were the most structurally plausible names in their entire logs — killed not because the data said no, but because web sources couldn't say yes. The discipline (never guess) stays. But the local chain scripts resolve exactly the data that was insufficient: real asks, real strikes, real feasibility. **The fix is the same as Finding One's: names that die DATA-INSUFFICIENT on chain/feasibility data get one free re-check via local scripts before the kill is logged as final.** Costs nothing. OLED and NXST get that re-check this weekend.

## 8. WHAT DOES NOT CHANGE

- No rule is loosened. Every amendment from July 10 stands. The funnel's tightness survived this audit on its merits.
- The screen-tier feasibility glance stays advisory-only (already codified July 10).
- The decline-category test stays exactly as written. 25-for-25 on this run.
- Batch sizes stay 10-20 inline per the budget rule. What changes is per-name yield, not volume.

## 9. ACTIONS (this weekend's batch runs on these)

1. **Geometry-first sourcing:** candidate lists built from the $3-40 / volatile-mover box; `fetch_price.py --range` and chain pulls run BEFORE any search.
2. **Aged-dislocation sourcing:** target names whose 52-week low printed 4-10 weeks ago, not this week.
3. **No dedicated puts pools until the back-test runs.** Incidental puts candidates go to the watch list only.
4. **Free re-check of chain-data DATA-INSUFFICIENT kills:** OLED and NXST first.
5. Per-line kill counts keep getting logged every batch so these base rates accumulate into a real calibration set.

---

## GLOSSARY

- **Funnel lines 1-13:** The selection sequence ratified July 10, 2026 (see selection_criteria_audit_jul10.md). Lines 1-4 are the screen tier (range percentile, earnings window, ratings direction, feasibility glance); lines 5-13 are DD (decline category, floor freshness, chain filter, reachability, implied-move cross-check, short interest, estimate revisions, insider activity, sizing).
- **R1 / R2 / R3 / R5 / R6:** Shorthand for funnel lines: R1 = 52-week range percentile, R2 = confirmed earnings inside the option window, R3 = ratings direction filter, R5 = chain affordability (ask ≤$1.00 calls / ≤$1.50 puts), R6 = reachability (required move ≤1.5x median earnings-day move).
- **MID-OUT:** A name killed at R1 because its price sits in the middle (25-75%) of its 52-week range — no directional edge either way.
- **Range percentile:** Where the current price sits between the 52-week low (0%) and high (100%).
- **Decline category:** Every beaten-down name gets its decline named before it can advance: (1) event overreaction — the only tradeable one, (2) secular decline, (3) macro beta, (4) commodity/cycle unwind.
- **Capitulation (analyst):** Analysts cutting ratings/targets after a decline is underway. Fresh cuts mean the bottom isn't in; the hardened R3 requires the cuts to be >30 days stale.
- **Stabilization window:** This post-mortem's name for the period after analyst capitulation ends but before the price recovers out of the bottom quartile — the only window the funnel can admit a calls name.
- **Geometry / the geometry box:** The joint constraint of Rules 5+6: a stock cheap enough (~$3-40) and volatile enough on earnings (≥~6% median move) that an affordable option strike is actually reachable. Names outside the box have no viable instrument regardless of thesis.
- **Feasibility glance:** The screen-tier, web-sourced approximation of Rules 5+6. Went 0-for-4 against live chains on July 10; advisory only.
- **Chain:** The live options chain — real strikes, real asks, real spreads. The only truth source for Rules 5 and 6.
- **DATA-INSUFFICIENT:** Screen verdict when a required figure can't be verified; the name is dropped rather than guessed at.
- **Back-test gate:** Standing decision that no live puts entry happens until every name in passes.md is run through the inverted Iron Rules and documented. Deadline Jul 31, 2026.
- **BOTZ rule:** Themes without dated data mechanisms are dead money. Named for Sheldon's robotics ETF.
- **Compound survival probability:** The product of each funnel line's individual pass rate — the expected fraction of screened names that survive every line. Used here to test whether 1-of-202 was on model (it was).
- **Kelly criterion / half-Kelly:** Bet-sizing math relating edge to bankroll fraction; the fund's sizing tiers sit at half-Kelly. Not touched by this post-mortem.
