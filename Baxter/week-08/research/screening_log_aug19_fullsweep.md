# SCREENING LOG — Aug 19 (Wednesday night) — FULL-UNIVERSE SWEEP

Michael's instruction: "screen fresh names tonight. we are sitting idle. lets go until we're sure its not because we didnt look." Full-universe scanner run, not a standard 10-20 batch — Michael explicitly asked for exhaustive coverage this session.

## Stage 1: Sourcing (scanner, 7 market-cap bands, $300M–$150B+)

Ran the live scanner across 7 bands (300M-1B, 1B-5B, 5B-10B, 10B-50B, 50B-150B, 150B+), each joined with an earnings-date filter for the next 35 days (Aug 19 – Sep 23, 2026).

**Raw yield: 398 names** with earnings inside the window, market cap $300M+.

Excluded 26 closed-end funds/trusts/leveraged ETPs (CLM, RVT, GAB, BST, BSTZ, ETV, ETW, BDJ, RQI, CII, UTF, TY, USA, QQQX, GDV, BBN, AWF, BHK, IFN, CRF, GOGL, BMEZ, ECAT, BTX, EOS, FSCO) — these carry a distribution/NAV "earnings date," not a real EPS catalyst, and would fail the fund's whole premise. One name (DCX) excluded for broken 52-week-high data (high=$25,776 vs last=$0.95, clearly corrupted).

**Real operating-company universe: 371 names.**

## Stage 2: Rule 1 (range percentile, computed by hand from high/low/last)

Bottom quartile (CALLS-zone): **92 names**, percentile range -7.5% to 25.0%.
(Top quartile / PUTS-zone: 92 names, logged, untouched, per standing no-puts-pools rule pending the back-test.)

## Stage 3: Rule 2 (earnings date verification via get_earnings_results, free structured calls)

Ran the deepest 30 CALLS-zone names by percentile through `get_earnings_results`.

**10 killed on calendar/data integrity, not story:**
- AHG, CRAQ, BIT, NEGG, OIO, DSU — no earnings data returned at all (fails closed, missing data = kill).
- **KDK** — scanner said Aug 31; real data shows KDK already reported Aug 6, next print isn't until Nov 11. Stale scanner date, exactly the KR-style calendar trap the Aug 7 rule exists to catch.
- **AAPG** — irregular/inconsistent fiscal calendar across quarters (a report dated "today," another for the same fiscal period 5 days later). Unreliable, killed on data quality.
- **RZLV** — earnings-date entries out of chronological order across quarters, unreliable calendar.
- **WB** — reports today (Aug 19) AM, verified=true. By tonight's session that catalyst has already happened; no longer a forward-looking trade. (Also: this is the same WB killed on Rule 3 in the Aug 16 batch — BofA Underperform.)

**20 real survivors**, 10 with `verified: true` dates: GME, MNSO, WDH, FINV, XPEV, NIO, PLAY, LI, ABAT, BRAI, EH, ODD, FLO, BILI, NOAH, CHA, TIGR, LEN, DKS, FIZZ.

## Stage 4: Rule 5/6 (chain feasibility, live option chains) — the 10 verified-date names

- **FINV** — killed. Ask $0.20 on zero bid, no real market to exit into.
- **NOAH** — killed. Same problem: ask $0.15, bid $0.00.
- **ODD** — weak. Needs +16.7% to breakeven ($14.35 vs $12.30), expensive ask relative to stock. Not pursued further tonight.
- **MNSO** — borderline. Needs +18.7% ($12.65 vs $10.66). Queued, not chased tonight — coarse $2.50 strikes leave no cheaper alternative.
- **EH** — borderline. Needs +11.2% ($6.33 vs $5.69). Queued.
- **LI** — clean chain (needs +5.6%) but **killed on Rule 3**: zero Buy ratings this month (0 Buy / 6 Hold / 1 Sell), consensus Hold, and a stack of recent cuts (Morgan Stanley, Goldman downgrade to Neutral, HSBC, BofA, Barclays all trimmed targets). Same capitulation shape that killed WB and CCL/NKE/BSX historically — Rule 3 exists exactly for this.
- **TIGR** — clean chain (needs +7.1%), good liquidity (OI 7,421). Consensus Buy (10 Buy/1 Sell), average target $7.69 vs $5.12 breakeven — real cushion. One dissenting Sell not yet isolated from the low-end target. Queued as backup.
- **DKS** — clean chain (needs +6.7%), decent liquidity (OI 20, tight $9.00/$9.70 spread). Not yet Rule-3-checked tonight. Queued as backup.
- **FLO** — clean chain math (needs +5.0%) but Flowers Foods is a bakery/staples name — historically low earnings-day volatility. Flagged for a real Rule 6 historical-move check before trusting the cheap-looking math; staples rarely clear even 5%. Queued, not chased.
- **BILI — full pass, pitch-ready.** See `research_BILI.md`.

## Backlog for next session(s)

- 62 of the original 92 CALLS-zone names never reached Rule 2 (only the deepest 30 by percentile were checked tonight).
- GME, WDH, XPEV, NIO, PLAY, ABAT, BRAI, CHA, LEN, FIZZ — real Rule-2 survivors, never reached the chain check.
- TIGR, DKS — chain-clean, Rule 3 not yet run.
- MNSO, EH, FLO — chain-borderline, need one more look.
- 92-name PUTS-zone pool — logged only, per standing rule (blocked on the puts back-test).

## The one trade

**BILI $17.50C Aug 28 2026.** Full writeup: `research_BILI.md`.
