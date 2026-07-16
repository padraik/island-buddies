# PUTS BACK-TEST — OUTCOME DATA (as of Jul 16, 2026)

*Mechanical data pull only. No verdict on whether the puts system "works" is rendered here — that judgment happens elsewhere. Every number below comes from a script output (`fetch_price.py`, `fetch_option_history.py`) or a research document read directly. Nothing is invented.*

---

## PURPOSE

On Jun 22, 2026 a screening session documented six hypothetical PUTS entries (never actually traded) across `passes.md` and five `research_TICKER.md` files. This log answers: what actually happened to each documented instrument between the screen and today (Jul 16, 2026)?

## CONVENTIONS

- **Hypothetical fill:** Jun 23, 2026 (first trading day after the Jun 22 screen) CLOSE price. This is the realistic entry point, not the Jun 22 estimate.
- **Mark:** Jul 15, 2026 close (last full trading day before today, Jul 16).
- **Peak:** highest HIGH recorded on or after Jun 23, 2026.
- **Trough:** lowest LOW recorded on or after Jun 23, 2026.
- **Flag threshold:** if the Jun 23 close differs from the documented estimate by more than 30%, it is flagged below.
- All expiries are Aug 21, 2026 (2026-08-21) as documented in the research files — none were ASSUMED, all were explicitly stated.

## EXCLUSIONS

- **TDOC** — no documented instrument in passes.md or any research doc. EXCLUDED, not constructed.
- **SBUX** — passes.md explicitly lists this as "DIRECTION UNCERTAIN" with no proposed strike/premium (recategorization pending price check, never resolved into an instrument). EXCLUDED, not constructed.

## DATA QUALITY NOTE (applies across all six instruments)

The option-history script frequently returns isolated `$0.01` low/close prints on individual days that are inconsistent with the highs and closes on adjacent days (e.g., a contract shows a real close of $1.95 the day before and $1.60 the day after, with a $0.01 print sandwiched between). These read as stale-quote/no-bid artifacts in the data feed rather than real fills. They are reported mechanically where they are the literal min, and separately flagged as likely anomalies. RCL's substituted contract ($190P) is degraded further — $0.01 prints appear on a majority of days, not just isolated ones — see the RCL section.

---

## TSLA (Tesla) — $250P Aug21 2026

**Documented estimate (research_TSLA.md, confirmed against passes.md):** $250P Aug21 at est. $0.97. Stock at screen: $405.04.

**Script results:**
- `fetch_price.py TSLA --range`: **$393.82** | 52wk range $297.82–$498.83 | 48th percentile.
- `fetch_option_history.py TSLA 2026-08-21 250 put 0.97`: contract found directly, no substitution needed.

**Hypothetical fill (Jun 23, 2026 close):** $1.29 (low $0.90 / high $1.33).
**vs. documented estimate ($0.97):** +33.0% — **FLAGGED** (exceeds 30% threshold).

**Peak since Jun 23:** $1.48 high on 2026-06-25 (+14.7% vs. entry fill $1.29).
**Trough since Jun 23:** $0.39 low, first hit 2026-07-10, repeated 2026-07-15 (-69.8% vs. entry fill).
**Latest close (Jul 15, 2026):** $0.41 (-68.2% vs. entry fill).

**Catalyst status:** RESOLVED. Q2 delivery report (the pre-earnings catalyst flagged in the research doc as the first trigger) fired Jul 2, 2026: Tesla delivered 480,126 vehicles, +25% YoY, beating the ~406K consensus by ~74K — the opposite of the delivery-miss bear thesis required for the put to work. Q2 earnings (~Jul 22-23) still pending, but the pre-earnings decay described in the research doc ("the put goes from $1.00 to $0.30 before we even hear Elon talk about robots") happened in the bear-killing direction: stock barely moved (-2.8% since screen) and the put decayed to near-worthless well before earnings.

**Notable candles:**

| Date | Event | Low | High | Close | % vs. entry fill |
|------|-------|-----|------|-------|-------------------|
| 2026-06-23 | Entry day | 0.90 | 1.33 | 1.29 | — |
| 2026-06-25 | Peak high | 1.28 | 1.48 | 1.28 | — |
| 2026-07-02 | Delivery beat announced | 0.60 | 0.87 | 0.77 | -40.3% |
| 2026-07-10 | Trough (tied) | 0.39 | 0.52 | 0.50 | -61.2% |
| 2026-07-15 | Latest mark | 0.39 | 0.44 | 0.41 | -68.2% |

---

## DASH (DoorDash) — $130P Aug21 2026

**Documented estimate (research_DASH.md, confirmed against passes.md):** $130P Aug21 at est. $1.00. Stock at screen: ~$172 (last trade; ask stale at $205).

**Script results:**
- `fetch_price.py DASH --range`: **$188.25** | 52wk range $143.30–$285.50 | 32nd percentile.
- `fetch_option_history.py DASH 2026-08-21 130 put 1.00`: contract found directly, no substitution needed.

**Hypothetical fill (Jun 23, 2026 close):** $2.46 (low $2.41 / high $2.85).
**vs. documented estimate ($1.00):** +146.0% — **FLAGGED, large divergence.** DASH was already trading well above the ~$172 screen reference by the time of fill; the $130P was far more expensive than modeled.

**Peak since Jun 23:** $2.85 high, same day as entry (2026-06-23) — no later high exceeded it (+15.9% vs. entry fill, but effectively the entry-day range itself).
**Trough since Jun 23:** $0.01 low (data-anomaly pattern — isolated single-day prints on 2026-06-25, 06-29, 07-01, 07-07, 07-14, 07-15, each surrounded by normal-range days). Excluding those anomaly prints, the practical trough is $0.49 low on 2026-07-13.
**Latest close (Jul 15, 2026):** $0.59 (-76.0% vs. entry fill).

**Catalyst status:** OPEN — catalyst pending. Q2 earnings estimated Aug 6-7, 2026, not yet fired. No search spent (per instructions, only fired catalysts get searched). Stock is up ~9.4% from the ~$172 screen reference to $188.25, moving away from the bear thesis so far, consistent with the put's decay to date.

**Notable candles:**

| Date | Event | Low | High | Close | % vs. entry fill |
|------|-------|-----|------|-------|-------------------|
| 2026-06-23 | Entry day / peak high | 2.41 | 2.85 | 2.46 | — |
| 2026-06-25 | First $0.01 anomaly print | 0.01 | 2.12 | 1.95 | -20.7% |
| 2026-07-13 | Practical trough (non-anomaly low) | 0.49 | 1.48 | 0.71 | -71.1% (low) |
| 2026-07-15 | Latest mark | 0.01 | 0.64 | 0.59 | -76.0% (close) |

---

## ABNB (Airbnb) — $117P Aug21 2026 (SUBSTITUTED $115P)

**Documented estimate (research_ABNB.md, confirmed against passes.md):** $117P Aug21 at est. $1.28. Stock at screen: ~$139.

**Script results:**
- `fetch_price.py ABNB --range`: **$147.99** | 52wk range $110.81–$150.82 | 93rd percentile.
- `fetch_option_history.py ABNB 2026-08-21 117 put 1.28`: **errored — "NO HISTORICAL DATA."** $117P does not exist as a listed contract in the historical feed.
- Retried nearest listed strike: `fetch_option_history.py ABNB 2026-08-21 115 put 1.28` — **SUCCEEDED. SUBSTITUTED $115P for the documented $117P.**

**Hypothetical fill (Jun 23, 2026 close, $115P):** $1.61 (low $1.04 / high $2.55).
**vs. documented estimate ($1.28, for the un-tradeable $117P):** +25.8% — within the 30% threshold, not flagged (note strike substitution makes this an imperfect comparison).

**Peak since Jun 23:** $2.55 high, same day as entry (2026-06-23) — no later high exceeded it. A secondary near-peak of $2.08 occurred 2026-07-08.
**Trough since Jun 23:** $0.01 low (anomaly prints on 2026-07-10 and 2026-07-13). Excluding those, practical trough is $0.38 low on 2026-07-15.
**Latest close (Jul 15, 2026):** $0.43 (-73.3% vs. entry fill).

**Catalyst status:** OPEN — catalyst pending. Q2 earnings confirmed Aug 4, 2026, not yet fired. No search spent. Stock is UP ~6.5% from the ~$139 screen reference to $147.99, and now sits at the 93rd percentile of its 52-week range — moving further from the bear thesis (which required nights-booked deceleration + ADR compression), consistent with the put's decay.

**Notable candles:**

| Date | Event | Low | High | Close | % vs. entry fill |
|------|-------|-----|------|-------|-------------------|
| 2026-06-23 | Entry day / peak high | 1.04 | 2.55 | 1.61 | — |
| 2026-07-08 | Secondary high spike | 0.58 | 2.08 | 1.01 | -37.3% |
| 2026-07-10 | $0.01 anomaly print | 0.01 | 0.66 | 0.53 | -67.1% (close) |
| 2026-07-15 | Latest mark / practical trough | 0.38 | 0.51 | 0.43 | -73.3% |

---

## RCL (Royal Caribbean) — $185P Aug21 2026 (SUBSTITUTED $190P) — DATA-DEGRADED

**Documented estimate (research_RCL.md, confirmed against passes.md):** $185P Aug21 at est. $0.75 (4/5 conviction variant) OR $180P at est. $0.38 (3.5/5 conviction variant). Stock at screen: ~$230.

**Script results:**
- `fetch_price.py RCL --range`: **$290.94** | 52wk range $232.10–$366.50 | 44th percentile.
- `fetch_option_history.py RCL 2026-08-21 185 put 0.75`: **errored — "NO HISTORICAL DATA."**
- Retried documented variant strike: `fetch_option_history.py RCL 2026-08-21 180 put 0.38`: **also errored — "NO HISTORICAL DATA."**
- Retried next-nearest strike: `fetch_option_history.py RCL 2026-08-21 190 put 1.07`: **SUCCEEDED. SUBSTITUTED $190P** (neither documented strike — $185P or $180P — exists in the historical feed; $190P is the nearest listed strike that returned data).

**DATA QUALITY FLAG — this contract is unusually illiquid.** Unlike the isolated single-day $0.01 anomalies seen on other tickers, the $190P LOW and CLOSE print $0.01 on a majority of days across the entire window (roughly 10 of 16 trading days since entry), while the HIGH column shows real, volatile values. This reads as a contract with effectively no real bid for much of the period — wide spreads, sporadic single-print asks. Treat the figures below as directionally indicative, not precise fills.

**Hypothetical fill (Jun 23, 2026 close, $190P):** $0.88 (low $0.01 / high $1.88).
**vs. substituted-strike estimate ($1.07):** -17.8% — within 30% threshold, not flagged on a like-for-like basis. (Cannot be meaningfully compared to the original $185P/$180P estimates given the strike substitution.)

**Peak since Jun 23:** $2.63 high on 2026-07-13 (+198.9% vs. entry fill) — a one-day spike; the corresponding close that day was $0.01, reinforcing the illiquidity flag (no real fill likely available at the high print).
**Trough since Jun 23:** $0.01 low/close, recurring on most days (2026-06-24, 06-26, 06-29, 06-30, 07-06, 07-07, 07-08, 07-09, 07-10, 07-13, 07-15) — this is the DEGRADED pattern described above, not an isolated anomaly.
**Latest close (Jul 15, 2026):** $0.01 (-98.9% vs. entry fill) — essentially worthless / no bid.

**Catalyst status:** OPEN — catalyst pending. Q2 earnings estimated ~Jul 25, 2026, not yet fired. No search spent. Stock is UP sharply — from ~$230 at screen to $290.94, a +26.5% rally — the opposite direction of the bear thesis (net yield exhaustion), fully consistent with the put decaying to near-zero well before its catalyst.

**Notable candles:**

| Date | Event | Low | High | Close | % vs. entry fill |
|------|-------|-----|------|-------|-------------------|
| 2026-06-23 | Entry day | 0.01 | 1.88 | 0.88 | — |
| 2026-07-13 | Peak high (one-day spike, no real close) | 0.01 | 2.63 | 0.01 | -98.9% (close) |
| 2026-07-14 | Rare non-anomaly close | 0.01 | 1.45 | 0.78 | -11.4% |
| 2026-07-15 | Latest mark | 0.01 | 0.73 | 0.01 | -98.9% |

---

## TTD (The Trade Desk) — $65P Aug21 2026 — DATA-UNAVAILABLE

**Documented estimate (research_TTD.md, confirmed against passes.md):** $65P Aug21 at est. $0.77 (4/5 conviction variant) OR $60P at est. $0.32 (3.5/5 conviction variant). Stock at screen: ~$82.

**Script results:**
- `fetch_price.py TTD --range`: **$19.22** | 52wk range $16.98–$91.45 | **3rd percentile.** Stock has collapsed -76.6% since the ~$82 screen reference.
- `fetch_option_history.py TTD 2026-08-21 65 put 0.77`: errored — "NO HISTORICAL DATA."
- Retried documented variant: `... 60 put 0.32`: errored — "NO HISTORICAL DATA."
- Retried nearest chain strikes from research doc: `... 68 put 1.35`: errored. `... 72 put 2.10`: errored. `... 45 put 0.30`: errored.
- Checked the LIVE puts chain (`fetch_puts_chain.py TTD`) for context: as of today, the nearest available expiries (Jul 17 / Jul 24 / Jul 31) list **no strikes above $20** — consistent with a chain that has been entirely restruck around the new, much lower stock price. The $65P/$60P/$68P/$72P/$45P Aug21 contracts are not retrievable through this data path.

**Verdict: DATA-UNAVAILABLE.** No candle history could be pulled for any tried strike near the documented instrument. Marking per instructions rather than substituting further or estimating a fill.

**What we know without the option data:** the underlying stock fell from ~$82 to $19.22 (52-week 3rd percentile) since the Jun 22 screen — a decline far beyond the -21.7% breakeven move the $65P needed. If a contract near $65P Aug21 still exists and was tradeable, it would be deep in the money. This is inferred from the stock-price script only; no option-level number is asserted.

**Catalyst status:** OPEN — catalyst pending. Q2 earnings estimated ~Aug 7, 2026, has not fired. Per the search-budget rule, no search was spent investigating the cause of the pre-earnings collapse, since the documented catalyst (earnings) has not yet fired. The stock-price move is real (per `fetch_price.py`) but its cause is unexplained in this log — flagged for follow-up, not searched.

**Notable candles:** none available (DATA-UNAVAILABLE).

---

## CMG (Chipotle) — $47P Aug21 2026 (SUBSTITUTED $45P)

**Documented instrument:** sourced from passes.md only — no research_CMG.md exists in the repo (Glob/find confirmed absent under `Baxter/**`). Documented: $47P Aug21 at est. $0.65. Stock at screen: ~$55 (post-split).

**Script results:**
- `fetch_price.py CMG --range`: **$34.57** | 52wk range $28.04–$54.29 | 25th percentile. Stock down -37.2% from the ~$55 screen reference.
- `fetch_option_history.py CMG 2026-08-21 47 put 0.65`: errored — "NO HISTORICAL DATA."
- Retried nearest listed strike: `fetch_option_history.py CMG 2026-08-21 45 put 0.50`: **SUCCEEDED. SUBSTITUTED $45P for the documented $47P.**

**Hypothetical fill (Jun 23, 2026 close, $45P):** $13.80 (low $13.55 / high $14.35).
**vs. documented estimate ($0.65):** +2,023% — **FLAGGED, extreme divergence, far beyond the 30% threshold.** This gap cannot be explained by the $2 strike substitution alone. The contract was already priced at $12.75-$14.13 on Jun 22 (screen day itself, per the raw candle data), meaning CMG's actual tradeable option was already deep in the money at the time of the Jun 22 screening session — inconsistent with the ~$55 stock price and $0.65 premium documented in passes.md. Either the passes.md stock price/premium estimate was stale or wrong at the time it was written, or CMG underwent a large decline between whatever reference point produced "~$55" and the Jun 22-23 trading window that is not otherwise documented in this repo. Flagged as an open data-conflict, not resolved here.

**Peak since Jun 23:** $14.35 high, same day as entry (2026-06-23) — matches the script's own reported all-time peak for this series (+4.0% vs. entry fill).
**Trough since Jun 23:** $8.35 low on 2026-07-14 (-39.5% vs. entry fill). No $0.01 anomaly prints in this series' post-entry window.
**Latest close (Jul 15, 2026):** $9.98 (-27.7% vs. entry fill).

**Catalyst status:** OPEN — catalyst pending. Earnings estimated ~Jul 23, 2026, not yet fired. No search spent (per instructions). As with TTD, the stock has already moved substantially (-37.2%) well ahead of its documented catalyst, and the option was already deep ITM before the Jun 23 hypothetical fill — the cause is unexplained in this log and flagged for follow-up rather than searched.

**Notable candles:**

| Date | Event | Low | High | Close | % vs. entry fill |
|------|-------|-----|------|-------|-------------------|
| 2026-06-22 | Screen day (already deep ITM) | 12.75 | 14.13 | 14.13 | +2.4% |
| 2026-06-23 | Entry day / peak high | 13.55 | 14.35 | 13.80 | — |
| 2026-07-14 | Trough | 8.35 | 8.98 | 8.98 | -34.9% |
| 2026-07-15 | Latest mark | 8.70 | 9.98 | 9.98 | -27.7% |

---

## ALL-INSTRUMENTS SUMMARY

| Ticker | Instrument (documented) | Doc'd est. premium | Jun 23 fill | Fill vs. est. | Peak +% | Trough -% | Jul 15 mark % | Catalyst date | Status |
|--------|--------------------------|---------------------|-------------|----------------|---------|-----------|----------------|----------------|--------|
| TSLA | $250P Aug21 2026 | $0.97 | $1.29 | +33.0% FLAGGED | +14.7% (Jun 25) | -69.8% (Jul 10/15) | -68.2% | Q2 deliveries fired Jul 2 (beat, bear thesis dead); earnings ~Jul 22-23 pending | OPEN — catalyst partially resolved, put already decayed |
| DASH | $130P Aug21 2026 | $1.00 | $2.46 | +146.0% FLAGGED | +15.9% (Jun 23, entry day) | -99.6% anomaly / -71.1% practical (Jul 13) | -76.0% | Q2 earnings ~Aug 6-7 | OPEN — catalyst pending |
| ABNB | $117P Aug21 2026 (SUBSTITUTED $115P) | $1.28 | $1.61 | +25.8% | +58.4% (Jun 23, entry day) | -99.4% anomaly / -76.4% practical (Jul 15) | -73.3% | Q2 earnings Aug 4 | OPEN — catalyst pending |
| RCL | $185P Aug21 2026 (SUBSTITUTED $190P, DATA-DEGRADED) | $0.75 (or $180P $0.38) | $0.88 | -17.8% vs. substituted-strike est. | +198.9% (Jul 13, one-day spike, no real close) | -98.9% (recurring $0.01, most days) | -98.9% | Q2 earnings ~Jul 25 | OPEN — catalyst pending, illiquid contract |
| TTD | $65P Aug21 2026 | $0.77 (or $60P $0.32) | DATA-UNAVAILABLE | n/a | n/a | n/a | n/a | Q2 earnings ~Aug 7 | OPEN — catalyst pending, no option data; stock down -76.6% independently |
| CMG | $47P Aug21 2026 (SUBSTITUTED $45P) | $0.65 | $13.80 | +2,023% FLAGGED (extreme) | +4.0% (Jun 23, entry day) | -39.5% (Jul 14) | -27.7% | Earnings ~Jul 23 | OPEN — catalyst pending, pre-catalyst data conflict flagged |

**Excluded (no documented instrument):** TDOC, SBUX.

---

## SEARCH BUDGET

1 of 3 web searches spent: "Tesla Q2 2026 delivery numbers July 2026" (used because the TSLA delivery catalyst had already fired between Jun 22 screen and Jul 16 today, and the outcome needed a one-line cause). No other name's documented catalyst had fired as of Jul 16, 2026, so no further searches were spent, per instructions — including for TTD's and CMG's unexplained pre-catalyst stock declines, which are flagged above but not investigated.

---

## GLOSSARY

**Back-test:** Testing a trading system's rules against real historical (or, here, forward-realized) outcomes to see what would have happened, without risking real capital. This log is the data-gathering step of a back-test — it records outcomes, it does not judge whether the system worked.

**Hypothetical fill:** The price at which a documented-but-never-executed trade would have been entered, had it actually been placed. Convention used here: the Jun 23, 2026 closing price (first trading day after the Jun 22 screening session), which is more realistic than the same-day estimate written during the screen.

**Mark:** The value used to represent a position's current worth at a specific point in time, without exiting the position. Convention used here: the Jul 15, 2026 closing price (last full trading day before this log was assembled on Jul 16).

**Peak / trough:** Peak is the highest HIGH price recorded for a contract on or after the hypothetical entry date. Trough is the lowest LOW price recorded over the same window. For a long put, a higher peak generally represents a more favorable exit opportunity (stock fell); a trough near the entry price or below represents the position's worst point (stock did not fall, or fell least).

**Catalyst:** A specific, dated event expected to move the stock enough to make the trade profitable — an earnings report, a delivery/production update, a regulatory ruling, etc. "Fired" means the event has already occurred as of the log date (Jul 16, 2026); "pending" means it has not yet occurred.

**ASSUMED expiry:** Per the task instructions, if a documented instrument had no stated expiry, this log would assume 2026-08-21 and mark it ASSUMED. Not needed here — all six instruments had an explicit Aug 21, 2026 expiry stated in their source document.

**SUBSTITUTED:** The exact documented strike does not exist in the historical options-data feed. A nearby listed strike was pulled instead and is clearly marked, with the original documented strike noted for comparison. Used for ABNB ($117P → $115P), RCL ($185P/$180P → $190P), and CMG ($47P → $45P).

**DATA-UNAVAILABLE:** No candle history could be retrieved for the documented strike or any nearby substitute strike tried. No fill price is asserted; only independently-verifiable data (e.g., current stock price) is reported. Used for TTD.

---

*Data-only log. No calibration verdict on the puts system is rendered in this document.*
