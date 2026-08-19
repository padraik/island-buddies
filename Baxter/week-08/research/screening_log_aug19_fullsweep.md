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

## Stage 5 (same night, continued): the remaining 62 CALLS-zone names

Michael: "lets check the remaining 62." Ran all 62 through Rule 2.

**9 more killed on calendar/data integrity:** BKT, VZLA (no forward-looking report left in the data), SAC, VCRE, DXYZ, BGB (no data), SBSW (report dates don't correspond to any sane fiscal quarter — 2019-2021 labels with 2026 dates), MPLT (real next report is Dec 3, scanner's Aug 31 was stale), LAES (same problem, self-contradicting quarters).

**3 more killed the same way WB died: reporting today, catalyst already spent.** LOW, YMM, KC all show `verified: true` reports dated 2026-08-19 (today).

**26 real, verified/tentative survivors remained.** Chain-checked the strongest 7: PICS had no option chain at all (Rule 5 kill, no instrument). Of the rest:

| Ticker | Needed | Liquidity (OI) | Rule 3 |
|---|---|---|---|
| BZ | +13.0% | 26 | not checked, math too weak |
| GAP | +8.0% | 102 | **KILL** — Barclays cut to Equal Weight, target below spot; Zacks Strong Sell present |
| CSIQ | +8.3% | 5 | not checked — chronic EPS misses, solar-sector structural headwind, Category 2 not overreaction |
| VIPS | +5.8% | 61 | Buy consensus, fresh upward revisions (BofA $20.20→$23.60, JPM $21→$22) but one stale low-end target ($14.21) sits under breakeven — real candidate, not as clean as BILI |
| PDD | +5.1% | 143 | Buy consensus but **1 real Sell rating present** + target just cut ($119.85→$115.81) on "earnings disappointments, regulatory uncertainty" — soft kill, not clean |
| FUTU | +4.2% | 1,874 (best liquidity of the whole session) | not checked — moot: earnings is *tomorrow* AM, meaning there's no trading session left to sell the pre-earnings ramp into. This would be a hold-through-earnings bet by default, which the fund's own audit already proved is a losing regime. Passed on structural/timing grounds, not the math. |

**No second trade tonight.** GAP resolves a two-session-old open question (queued Aug 8, Aug 16) — dead, and now closed out for good. VIPS is the best of what's left: logged as backlog, worth a fresh look with a cleaner Rule 3 read (or after its own next ratings update) rather than forced into tonight's book on a borderline read.

## Backlog for next session(s)

- GME, WDH, XPEV, NIO, PLAY, ABAT, BRAI, CHA, LEN, FIZZ — real Rule-2 survivors from the first 30, never reached the chain check.
- TIGR, DKS — chain-clean from the first 30, Rule 3 not yet run.
- MNSO, EH, FLO — chain-borderline from the first 30, need one more look.
- VIPS — chain-clean, decent liquidity, mixed-but-leaning-positive Rule 3. Best queued name from the second 62.
- LUCK, AI, TCOM, OLLI, PAHC, CPRT, CHWY, LE, OXM — unverified-date survivors from the second 62, never chain-checked.
- 184-name PUTS-zone pool (92 + 92 across both sweeps) — logged only, per standing rule (blocked on the puts back-test).

**Full universe now covered: all 371 real operating companies with earnings inside 35 days have been through at least Rule 1. Nothing was missed for lack of looking.**

## Stage 6 (same night, continued): the puts pool, actually screened

Michael asked directly: did we check puts? Honest answer at the time: no — logged only, per the standing "no dedicated puts pools" habit. But that habit outlived its reason. **The puts back-test gate was formally satisfied Aug 7** (`puts_backtest_final_verdict_aug07.md`): four hypothetical far-dated puts all lost 86-99.6% to pure theta before their catalysts mattered, and the fix adopted was a **21-day entry-timing rule** (no puts entry more than 21 days before the dated catalyst), not a blanket ban. Nobody had re-run the puts pool against that rule since. Ran it tonight.

**Sourcing:** top quartile of both sweeps' range-percentile computation = 184 raw PUTS-zone names (92 + 92). Filtered to scanner-date earnings inside 21 days (Aug 19-Sep 9): **83 names.**

**Rule 2 on the top 30 by extension (most overbought):** 10 killed on calendar/data integrity or same-day catalysts — **TGT and ZIM both report today**, same WB pattern from the calls side; PINC turned out to be a fund (PGIM Securitized Income ETF) misclassified by the scanner as having an earnings date; AEG and NEWP had self-contradicting or missing forward dates. 20 real survivors.

**Checked the three strongest candidates for real Rule 6 (historical down-move) data, not just extension:**

| Ticker | Real median move (6 qtrs) | 1.5x cap | Verdict |
|---|---|---|---|
| SNOW | 2.06% | 3.70% | Mega-cap, mature, well-covered software -- earnings surprises are small and well-anticipated. Any put cheap enough to be worth buying needs a strike too close to be affordable within the cap. |
| PANW | 1.10% | 1.74% | Same problem, worse. This name barely moves on its own prints. |
| FRO | 3.64% | 5.33% | Bigger real moves (shipping/tanker cyclical) -- but **5 of the last 6 prints were UP moves**, only 1 down. This is a stock whose own earnings history argues against the puts thesis, not for it. Betting against a name that keeps beating is the exact RCL trap the Aug 7 back-test's Finding 4 already documented.

**No puts trade tonight.** Not because the pool is empty or the gate is still closed -- because the three strongest real candidates each fail on a different, real reason (move too small twice, wrong direction once), and the remaining 17 survivors plus the other 53 names in the 21-day pool haven't been individually checked yet. This is genuine backlog, not a dead end -- shipping/cyclical names as a class showed the most real historical volatility of anything checked tonight (calls or puts); the miss on FRO specifically was direction, not magnitude, which means BWLP, NMM, SFL, NAT (same sector, not yet checked) are worth a look before writing off the whole cyclical bucket.

## Backlog for next session(s)

- Calls side: GME, WDH, XPEV, NIO, PLAY, ABAT, BRAI, CHA, LEN, FIZZ (Rule-2 survivors, no chain check); TIGR, DKS (chain-clean, no Rule 3); MNSO, EH, FLO (chain-borderline); VIPS (best queued name, mixed Rule 3); LUCK, AI, TCOM, OLLI, PAHC, CPRT, CHWY, LE, OXM (unverified-date, unchecked).
- Puts side: WLYB, NAT, BWLP, NMM, TWIN, CMBT, P, BNS, CM, SAIC, NTAP, BMO, TD, KFY, RY, HEI, SFL (17 real survivors from the top-30 extension pass, not yet chain-checked) -- **BWLP, NMM, SFL, NAT flagged as priority** (same cyclical-shipping profile as FRO, where the miss was directional not magnitude).
- 53 more PUTS-zone names (of the 83 inside the 21-day window) never reached Rule 2 at all.
- Both sides: full universe sourced and range-percentile'd; nothing skipped at the sourcing stage.

## The one trade

**BILI $17.50C Aug 28 2026.** Full writeup: `research_BILI.md`.
