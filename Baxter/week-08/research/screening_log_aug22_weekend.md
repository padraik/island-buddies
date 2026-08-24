# SCREENING LOG -- Aug 22, 2026 (Saturday, weekend research session)

Michael's instruction: nothing else to do today, find the next 4/5 play, calls or puts, whichever the data supports. Two passes: cleared the Aug 19 full-sweep backlog first (already through Rule 1/2, never chain-checked), then ran a fresh scanner pass covering both directions in one query.

**Result: 21 names screened, 0 advances.** A clean, ordinary 0-for-night by the funnel's own documented base rate (~0.5-1 survivor per 200) -- worth writing up in full because two of the kills are real, non-obvious findings, not just arithmetic misses.

---

## PASS 1: AUG 19 BACKLOG (11 names, all CALLS-zone, Rule 1+2 already cleared)

DKS, GME, WDH, XPEV, NIO, PLAY, ABAT, BRAI, CHA, LEN, FIZZ.

| Ticker | Kill reason |
|---|---|
| WDH | No options chain at all (404, no instrument). |
| BRAI | No options chain at all (404, no instrument). No earnings history either -- likely too new/thin to screen at all. |
| CHA | No options chain at all (404, no instrument). |
| DKS | Rule 6: cheapest viable strike needs +31.8%. Retailer, not a violent earnings mover. |
| FIZZ | Rule 6: only viable strikes need +47.4% to +62.7%. Dead on arrival. |
| PLAY | Rule 6: cheapest viable strike needs +23.2%. |
| LEN | Rule 6: cheapest strike inside the real post-earnings window (Sep18 expiry, after the Sep17 PM print) needs +15.8%. Homebuilder, historically a single-digit mover on earnings. |
| GME | Rule 3 decisive fail: consensus rating Sell, Wedbush Underperform $13.50 target -- would also fail Rule 4 (target sits below every viable breakeven). |
| XPEV | Rule 3 fail: 3 of 17 analysts rate Sell (max 1 allowed). |
| NIO | Rule 3 fail: 2 of 22 analysts rate Sell (max 1 allowed). |
| **ABAT** | **Rule 2 fail, the real finding of the night.** Chain looked excellent (cheapest strike needed only +3.1%, real historical moves gave a wide 20% Rule 6 cap) and Rule 4 looked survivable on the surface. But a direct search found the Q4 FY2026 print already happened -- **August 20, 2026, two days before this session** -- unaudited results already out. `get_earnings_results`' Sep 17 date was unverified and wrong; the next real catalyst (Q1 FY2027) won't land until ~November, outside any strike currently cheap enough to matter. Caught before any research doc got written, let alone money moved. Same calendar-trap shape as KR and HIVE. The one analyst target on file (Northland, $6.00) is also >2 years stale (Mar 2024) and would have failed Rule 4's 60-day freshness rule on its own. |

---

## PASS 2: FRESH SCAN (10 names, both directions, one query)

Reused the saved "Today's losers with earnings window" scan (scan_id `284795c1-...`), refreshed its earnings-date filter to the live 35-day window (2026-08-22 to 2026-09-26) and market cap $300M-$150B, added High/Low(52,1W) as display columns. **342 raw matches**, 200 with usable range data (excluded ~142 with broken/absurd 52wk ranges -- almost all reverse-split artifacts, e.g. a stock showing a 52wk high of $25,776). Computed range percentile by hand on all 200, took the cleanest names at each extreme.

**CALLS zone (bottom of range):** FINV, JKS, MZTI, RR, PLBL.
**PUTS zone (top of range, excluding any name showing a *fresh* high within the lookback -- fails Puts Rule 1's stall requirement):** FIVE, A, HQY, BOX, MANU.

| Ticker | Zone | Kill reason |
|---|---|---|
| PLBL | Calls | `get_earnings_results` returns empty -- not a real earnings-reporting equity via this tool (fund/ETF-shaped ticker). No Rule 2 mechanism. |
| MZTI | Calls | No chain in the $0.10-$1.00 affordable band at either checked expiry. |
| FINV | Calls | Rule 6-shaped fail: cheapest viable strike (Sep18, clears the Aug27 PM print) needs +19.7% on a historically modest, consistently-profitable fintech name. Not pursued further given the size of the ask. |
| JKS | Calls | Same shape: cheapest viable strike needs +15.0%. Company has missed EPS estimates by wide margins 5+ consecutive quarters -- reads as real deterioration (decline Category 2), not a market overreaction to an otherwise-sound business. Not pursued to a ratings check given the reachability gap alone. |
| **RR** | Calls | **Rule 3 marginal (Hold consensus, not clean Buy) PLUS a live disqualifier: RR is under an active securities fraud class action** (fabricated a Microsoft "co-innovation" partnership Jan 27 2026 that Microsoft itself denied two days later, -20% single session, multiple law firms now running the case). This is the BTGO shape exactly -- a real credibility/legal problem, not the kind of dislocation this fund is built to buy. Killed outright regardless of the chain's genuinely good reachability (best strike only needed +7.0%). |
| A | Puts | Rule 6 fail: cheapest viable strike (Sep18, clears the Aug26 PM print) needs -12.9% to -15.8%. Large diversified life-sciences name, not a violent earnings mover historically. |
| HQY, BOX, FIVE | Puts | Not chain-checked -- all three carry the Unified Screen's earnings-history cap (5-6 consecutive beat quarters each), capping conviction at 3.5/5 even before a chain check, and time ran out before reaching them. Queued, not killed -- worth a look next session if the queue's otherwise thin. |
| **MANU** | Puts | **Rule 6 fail on real data, the other genuine finding of the night.** Chain looked plausible (best strike needed -10.5%, well inside what a "Hold-turning-skeptical" small-cap could plausibly deliver). Pulled real earnings-day moves for all 6 of MANU's last prints (AM releases, prior-close-to-print-day-close): -3.8%, +18.8%, -6.3%, +2.5%, -2.1%, +12.7%. Median 5.05%, 1.5x cap 7.6%. The -10.5% needed is 138% of that cap -- a real fail, not a rounding error, even though the raw ask looked cheap on the surface. |

---

## THE NIGHT'S REAL LESSON

Two names (ABAT, MANU) looked like clean pitches on the cheap-and-easy checks -- reachable strike, no obvious red flag -- and both died on the checks that actually take real effort: a direct search past the tool's unverified date, and a real historical-move pull instead of trusting a plausible-looking ask. The funnel did its job. Zero entries tonight is the correct output of a working process, not evidence the process needs fixing.

**Queued, not dead (at the time):** HQY, BOX, FIVE (puts, beat-history-capped but not chain-checked) if a future session wants to finish the pass.

No trades. Fund unchanged: $1,075.96 cost basis, $128 deployed (BILI only), $947.96 reserve.

---

## PASS 3 (Aug 23, next session): FINISHING THE QUEUE -- ALL THREE DIE

Michael asked to finish HQY, BOX, FIVE. All three die, closing the queue at zero.

| Ticker | Kill reason |
|---|---|
| HQY | No options chain at all in the affordable band at any checked expiry. |
| **FIVE** | **Decisive Rule 6 fail, and a directional one.** Pulled real moves on the 5 most recent verifiable prints (PM releases, print-day close to next-day close): +0.7%, +5.6%, +3.9%, +3.2%, +10.7%. Median 3.9%, 1.5x cap 5.85% -- the cheapest viable put strike needed -22.8% to -26.5%, 4-5x the real cap. Worse: **every one of the 5 prints moved the stock up.** Zero down closes in the sample. Betting on a drop here isn't just outside Rule 6's magnitude tolerance, it's betting against a 5-for-5 real record. |
| **BOX** | **Rule 3 fail.** Chain and Rule 6 both looked survivable (real 6-print median 5.45%, cap 8.175%; the $32P Sep18 strike needed -7.3%, clearing the cap with room, ask $1.50 sitting exactly at the Rule 5 ceiling). But ratings search found only 1 confirmed Sell/Underperform against a Buy consensus (8-14 analysts) -- puts Rule 3 requires a minimum of 2. Also worth noting even if Rule 3 had cleared: BOX beat estimates 5 of the last 5 quarters and moved up 4 of the last 6 print reactions, which is the Unified Screen's earnings-history cap (max 3.5/5) -- this name was never going above a capped conviction regardless. |

**Full tally across both sessions: 24 names screened, 0 advances.** A genuinely quiet stretch by the numbers, but a clean one -- every kill traces to a specific rule, not a shrug. Nothing pitch-ready. Next session starts a fresh queue.

## GLOSSARY

- **Rule 1 (Range percentile):** Where the stock sits in its trailing 52-week range. Bottom quartile = calls candidate, top quartile = puts candidate.
- **Rule 2 (Catalyst):** Confirmed earnings date before option expiry.
- **Rule 3 (Ratings):** Calls need near-zero Sell ratings (max 1); puts need at least 2 Sell/Underperform ratings.
- **Rule 4 (Bear floor / Bull ceiling):** For calls, the lowest Buy-rated analyst target must sit above breakeven. For puts, the highest Sell-rated target must sit below breakeven.
- **Rule 5 (Chain filter):** Affordability cap on the option's ask price, scaled to fund reserve and conviction tier.
- **Rule 6 (Reachability):** The move required to reach breakeven can't exceed 1.5x the stock's median real historical earnings-day move (last 4-8 real prints).
- **MID-OUT:** A name whose range percentile falls in the 25-74th percentile -- no directional edge, screened out immediately.
- **Verified (earnings date):** `true` means the company itself announced the date; `false` means it's estimated from reporting cadence and needs independent confirmation before real money.
- **STRETCH / OK / OVER (chain tags):** The local chain script's own affordability read against the $0.10-$1.00 (calls) or $0.10-$2.00 (puts) ask band -- OK is clean, STRETCH is at the edge, OVER exceeds it.
