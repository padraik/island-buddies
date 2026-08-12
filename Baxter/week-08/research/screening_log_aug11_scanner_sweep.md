# Screening Log — Aug 11, 2026 (Tuesday evening) — First full run of the ratified scanner method

First live use of the scanner-based sourcing method since it was ratified Aug 10 (binder Tab 6) and cross-checked Aug 7 (`Correspondence/2026-08-07_from_Baxter_screening_upgrade.md`). Fund is fully in reserve ($1,056.96) after closing UAMY and JMIA earlier today, so this is a fresh sourcing pass, not a follow-up to an open position. Full funnel (Rule 2 re-verify, Rule 5/6 chain check, Rule 3/4 for the strongest survivors) run the same night at Michael's request, prioritizing an honest read of all 18 shortlisted names over speed.

**Method:** `create_scan` / `update_scan_filters` per band, `FILTER_TYPE_MARKET_CAP` BETWEEN the band, `FILTER_TYPE_EARNINGS_DATE` BETWEEN today and +35 days, plus `FILTER_TYPE_HIGH` and `FILTER_TYPE_LOW` (length 52, interval 1w) added as visible columns to compute 52-week range percentile by hand: `(Last - Low) / (High - Low)`.

**New finding:** the scanner's earnings-date filter, which failed three value formats on Aug 7, now works. The field is `fundamental.earningsYmd` and wants a plain `YYYYMMDD` integer. Collapses range-check and earnings-window into one scan per band.

**Second finding, more important:** the scanner's earnings-date field is not a substitute for `get_earnings_results` per name, even now that it's filterable. Re-verifying all 18 shortlisted names live turned up a company that had *already reported* the night before (SOC, real print Aug 10 PM, scanner still showed 8/12) and two multi-week drifts (KEP: scanner said 8/12, real date 8/25 unverified; QFIN: scanner said 8/14, real date 8/25 unverified). The scanner is good for casting the net across the whole market for free. It is not good enough to trust a single name's date without the same per-name check the binder already requires.

## Sourcing pass (3 bands)

| Band | Total items | Returned | CALLS candidates | PUTS candidates |
|---|---|---|---|---|
| $300M–$1B | 353 | 200 (cap) | 60 | 50 |
| $1B–$5B | 248 | 200 (cap) | 47 | 50 |
| $10B–$50B | 96 | 93 | 12 | 30 |

Sanity check: UAMY and JMIA both surfaced correctly on the day they closed; CPRT, QXO, TME, HIVE, DQ, PFLT (all previously killed) reappeared in their expected low-percentile slots.

## Full funnel results, all 18 shortlisted names

**Rule 2 kills / concerns (4):**
- **SOC** — already reported (Aug 10 PM, verified true, missed -0.42 vs +0.32 est). Next real catalyst Nov 12, unverified, outside any usable window. Dead.
- **KEP** — real date 8/25, unverified (scanner said 8/12, 13-day drift). Deprioritized, not killed outright — worth a clean re-check if it resurfaces with a verified date.
- **QFIN** — real date 8/25, unverified (scanner said 8/14, 11-day drift). Same treatment as KEP.
- **CSAN** — no options chain exists at all (404 from the instruments endpoint). Rule 5 kill by default, no live name to research.

**Rule 6 kills (2) — decisive, real 4-quarter history, the stock just doesn't move enough on its own prints:**
- **LI** — median absolute earnings move 2.02%, 1.5x cap 3.03%. Every real strike checked needed more than that.
- **NNE** — median absolute earnings move 1.38%, 1.5x cap 2.07%. Same story, even the tightest visible strike needed 4.6%+.

**Rule 3 kills (2) — good Rule 6 math, killed on ratings, the exact "Buy consensus headline hides real Sell count" trap the rule exists for:**
- **XPEV** — 25 analysts, Buy consensus, but 2-3 Sell-rated among them depending on the source cut. Exceeds max-1. Rule 6 was fine (needed 6.8% vs a 9.43% cap, 72% used) — doesn't matter once Rule 3 fails.
- **GEMI** — best Rule 6 margin of the whole batch (needed 3.8% vs a 9.13% cap, 42% used) and still dies: 9 analysts, 3 Buy / 2 Sell / 4 Hold. 2 Sell exceeds max-1.

**Soft-kill / caution (2):**
- **STNE** — Rule 6 solid (needed 5.4% vs a 13.33% cap, 41% used) but real analyst downgrades in the last month cite structural take-rate and volume pressure in the Brazilian payments market, not a one-off miss. Lowest visible target ($9.33) sits below the current stock price. Leans Category 2 (real deterioration), not the overreaction the fund buys.
- **WB** — Rule 6 solid (needed 4.6-8.4% depending on expiry vs a 10.22% cap) but Rule 4 is unresolved: the lowest visible analyst target ($6.60) sits below our breakeven, and it isn't confirmed whether that's a Buy-rated number or a Sell/Hold outlier. Same gap Bearxter flagged on JMIA Saturday — needs the specific firm and date pinned down before this could advance.

**Not fully funneled tonight, deprioritized for time (4):** REZI (needs 27-46% at every visible strike, weak Rule 6 read even before checking history), MNSO and TIGR (both unverified next-earnings dates), LULU (unverified date, 9/3). None killed outright — just didn't clear the bar to spend a search on tonight.

**Two clean survivors, ranked by confidence:**

**1. BTGO — highest confidence.** Rule 2 verified true (8/12 PM). Rule 3 clean: 12 analysts, 10 Buy, 0 Sell, 2 Hold. Rule 4 cushion is enormous: lowest analyst target $10-11.5+ against a stock at $5.04 and a breakeven around $5.40-5.85 — the floor sits roughly double the entry price. Rule 6 passes at 32% of a 24.70% cap, though the historical sample is thin (only 2 real quarters of earnings-day moves on record, both large: -15.71%, -17.21%). Real caveat: newest, least-covered name in the batch — worth a decline-category gut check (genuine dislocation vs. a still-settling recent listing) that wasn't done tonight.

**2. BTBT — second highest.** Rule 2 verified true (8/13 AM). Rule 3 clean: 5 analysts, 5 Buy, 0 Sell. Rule 4 cushion is large: analyst range $3-7 against a stock at $1.31 and a breakeven near $1.35-1.49. Rule 6 passes at 38% of an 8.24% cap, full 4-quarter real sample, consistent direction. Caveat: Bitcoin miner, BTC-price-correlated volatility (Category 1 likely — sector-wide, not company-specific — but not explicitly checked tonight the way ENVX's or BTDR's decline category was).

Neither is pitch-ready yet — both still need a decline-category read and, for BTGO, a closer look at why coverage is so thin. Straddle cross-check and the Five Baxters debate haven't run. That's the next session's work if either is worth carrying forward.

## Standing item raised this session (not yet ratified)

Brandt (via correspondence) raised a real structural question: should the binder set a minimum total DTE at entry for calls, separate from the existing puts-only "21 days before catalyst" rule, to guard against buying into the steepest part of an option's theta curve with too little runway before the planned exit? UAMY and JMIA (both 4 total DTE at entry, both sold before their prints per Tab 4, both losses) are the concrete evidence prompting the question. Not ratified tonight — flagged for a proper audit (DTE-at-entry vs. days-of-runway-to-planned-exit across every closed play) before it becomes a rule, same standard Rule 5 and Rule 6 were held to.

## Second batch, same night — the un-shortlisted 91 (15 pulled, prioritizing non-crypto sectors)

With BTBT filled and $916.96 still idle (86.8% of the fund), Michael asked to keep going rather than wait for a fresh session — the un-shortlisted pool from tonight's three bands (91 names beyond the original 18) was still live and needed no new scan calls. Pulled 15 spread across sectors, deliberately avoiding more crypto/BTC-correlated names given BTBT already carries that exposure.

**Rule 2 kills (3) — already reported, scanner dates were stale, same pattern as SOC earlier tonight:** ONON (reported this morning, Aug 11 AM), LEGN (reported this morning, Aug 11 AM, missed estimate), NHI (reported yesterday, Aug 10 PM).

**Deprioritized, unverified next date (5):** TCOM, OLLI, JKS, NOAH, BBW.

**Rule 5 kill (1):** GLOB — no affordable near strike at any expiry; cheapest breakeven needed 30.5% even before checking history.

**Decline-category soft-kill (1):** PHR — three consecutive quarters of double-digit post-earnings declines (-9.9%, -23.3%, -26.6%). That's a trend, not noise. Killed on the same standard as STNE earlier tonight, regardless of the Rule 6 math.

**Rule 6 kills (2), and a real lesson in the process:** FUTU and LUNR both looked like the best margins in the batch on a first read of the chain (needs 5.3% and 8.8% respectively). Both readings were wrong — the nearest expiry shown for FUTU (Aug 14) sits *before* its Aug 20 earnings, so that number reflected a contract with no catalyst inside it at all. The real earnings-inclusive expiry (Aug 21) needs 15.2% against an 8.13% cap — a clean fail. LUNR's near expiry genuinely did include its Aug 13 catalyst and still needs 8.8-11.3% against a 6.53% cap — a real fail, not a trap, but caught by the same "confirm the expiry label, don't trust the first chunk" discipline. **Standing practice going forward: always confirm which expiry a chain reading came from before trusting the needs% against Rule 6 -- the nearest priced expiry is not guaranteed to be the nearest one that actually contains the catalyst.**

**Two real survivors, one with a caution flag:**

**YALA** — Rule 6 passes at 45% of an 11.16% cap (needs 5.0%) on a real 4-quarter sample. Ratings lean Buy (Oppenheimer Outperform among a thin field), average target $8.40-9.59, and even a recent trim to $6.90 still clears breakeven with real cushion. Real caveat: only 2-3 analysts covering, thin bench.

**SPCE** — the best Rule 6 math of the batch (35% of a 15.30% cap at the $3.00 strike, real OTM structure, earnings tomorrow). But the ratings picture argues against calling this a clean dislocation: consensus is explicitly **Hold** (not Buy), and multiple named firms are actively cutting targets right now — Goldman Sachs cut twice ($47 to $41 to $36), Susquehanna cut ($4 to $3.25). Jefferies is still Buy-rated at $8, a real cushion if it holds, but a Buy rating inside an environment of active multi-firm capitulation is exactly the CCL/NKE/BSX pattern the binder was written to catch. Flagged as caution, not advanced to a pitch tonight.

**MOMO** survives narrowly (needs 2.9% vs a 7.53% cap) but only at a strike that's already slightly in the money, on an expiry 38 days out — the weakest structure of the three survivors. Noted, not pursued further tonight.

None of tonight's second batch reached a Five Baxters debate — YALA is the one worth carrying into a real pitch next session if the thin-coverage caveat holds up; SPCE needs the capitulation question resolved one way or the other before it's more than a maybe.

## Third batch, same night — 12 more names

Michael passed on ALT specifically because it reports tomorrow AM — no real ramp window left, same shape as the UAMY problem earlier tonight, correctly caught before it became a live mistake instead of after.

**Rule 2 kills (3):** VZLA (earnings data internally broken — report dates predate their own labeled fiscal quarters, no trustworthy upcoming date), HUYA and URG already covered in round 2's exclusions.

**Survivors after chain + real Rule 6:** TMC (35% of a 9.34% cap, real margin, Strong Buy consensus but genuine structural risk — pre-revenue deep-sea mining dependent on regulatory approval not yet granted, flagged as a weaker-than-it-looks floor) and ALT (66% of a 9.13% cap, clean 8 Buy/2 Hold/0 Sell, real cushion even after recent target cuts) — but ALT reports tomorrow AM, held rather than pitched, per the ramp-window concern above. PONY passed only marginally (87% of cap) and CRMD failed outright even at its cheapest strike.

## Fourth batch, same night — 10 more names, prioritizing real runway

Same lesson as ALT applied going in: skip anything reporting in the next 1-2 days.

**Killed on timing before chain-checking (3):** MLCO, EQPT, WRD all report inside 1-2 days — same problem as ALT, screened out on sight this time instead of after the work.

**Rule 2 kill (1):** VZLA-style broken data did not recur, but CINT's earnings appears to have already happened or is happening as this was checked (actual EPS populated for today's date) — too late for a fresh entry either way.

**Rule 5 kill (1):** FORTY — no viable options chain in range at all.

**Rule 6 kills (3), all confirmed at the correct earnings-inclusive expiry, not a trap:** EH (needs 13.5% vs a 6.77% cap), ASPI (needs 31.3% vs a 17.49% cap), LUCK (needs 23.3% vs a 2.00% cap — this stock barely moves on its own prints, same shape as LI and NNE from round one).

**One survivor: BULL (Webull).** Real Rule 6 margin (54% of a 9.08% cap, needs 4.9%), Strong Buy consensus, lowest target $10 against a breakeven near $7.95 — real cushion. Caveat: only 3 analysts covering, thin bench, same caution as YALA. Earnings Aug 19 PM, 8 days out — real runway, no ramp-window problem this time.

**Running tally, all four batches tonight:** 45 names funneled beyond the original 18, on top of BTBT's entry. Confirmed real survivors not yet pitched: YALA, BULL (both thin-coverage but clean), SPCE (best math, real ratings caution), TMC (real math, real structural-risk caution), ALT (cleanest of the batch, wrong timing tonight). None have been through a Five Baxters debate.

## GLOSSARY

- **Range percentile:** where the current price sits between the stock's 52-week low and high: `(price - low) / (high - low)`. Bottom quartile (≤25%) is a CALLS candidate under Rule 1; top quartile (≥75%) is a PUTS candidate.
- **Scanner (Robinhood market scanner / screener):** a live filtering tool over the tradeable market, run here via `create_scan`, `update_scan_filters`, and `run_scan`. Returns real-time data, capped at 200 rows per scan with no pagination exposed to this tool.
- **`get_earnings_results`:** the fund's standing first source for earnings dates (binder Tab 6, Aug 7, 2026), returning a company's real reporting history plus a `verified` flag (true = company-announced, false = estimated from cadence).
- **Rule 1-6:** THE UNIFIED SCREEN and Tab 1's Iron Rules — range percentile, confirmed catalyst, analyst ratings (max 1 Sell for calls), bear floor above breakeven, chain affordability, and reachability (required move ≤1.5x the stock's own median historical earnings-day move).
- **Decline category (Category 1 vs 2):** whether a stock's drop reflects a one-off market overreaction (tradeable) or real, ongoing business deterioration (not tradeable).
- **DTE:** days to expiration.
- **Theta:** the rate at which an option's extrinsic (time) value decays as expiration approaches; accelerates non-linearly in an option's final weeks of life.
