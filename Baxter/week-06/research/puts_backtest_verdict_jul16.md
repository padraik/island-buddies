# PUTS BACK-TEST — INTERIM CALIBRATION VERDICT
*Jul 16, 2026. Data: `puts_backtest_data_jul16.md` (real contract candles, pulled same day). Verdict rendered on the main thread (Fable 5) per the Model Cost Awareness rule — this is the rule-changing call the gate exists for. Calxter's Jul 31 deadline: met by this interim, with the completion pass scheduled below.*

---

## VERDICT: PUTS STAY BLOCKED. FINAL PASS AFTER THE AUG 4-7 PRINTS.

Nothing in the outcome data justifies unblocking live puts entries, and two of the six documented calibration entries turn out to have never existed at all. The details matter more than the headline, because three of them change how the final back-test must be run.

---

## THE SCOREBOARD (marks as of Jul 15, all catalysts still pending except TSLA's deliveries)

| Instrument | Jun 23 fill | Mark | Status |
|---|---|---|---|
| TSLA $250P Aug21 | $1.29 | **-68%** | Q2 deliveries (Jul 2) beat by ~74K units — the specific bear mechanism died mid-hold. Earnings Jul 22-23 pending. |
| DASH $130P Aug21 | $2.46 | **-76%** | Catalyst Aug 6-7 pending. |
| ABNB $115P Aug21 (sub.) | $1.61 | **-73%** | Catalyst Aug 4 pending. |
| RCL $190P Aug21 (sub., illiquid) | $0.88 | **~-90%+** | Stock rallied +26.5% INTO its own print (Jul 25 pending). $0.01 bids most days — the contract has no real market. |
| TTD $65P Aug21 | — | **EXCLUDED — corrupted entry** | See Finding 3. |
| CMG $47P Aug21 | — | **EXCLUDED — corrupted entry** | See Finding 3. |

Zero winners. Four clean hypotheticals, all down 68-90% **before any catalyst fired**.

---

## FINDINGS

**1. The theta funeral is now proven on real candles, in both directions.** Every clean entry was placed 6+ weeks before its catalyst and bled 68-90% of premium during the wait — the exact pattern the calls-side audit found (ABT's $1.95 → $0.08 into its own print). An option entered far ahead of its mechanism pays rent the whole way, long or short. **Any future puts system needs an entry-timing line: no entry more than ~21 days before the dated catalyst.** This goes to the final back-test as a proposed Iron Rule amendment, not adopted here.

**2. Screen-estimated premiums are fiction; only live chains price entries.** Realistic fills diverged from the documented estimates by +33% (TSLA) and +146% (DASH). Every screen-tier EV calculation on the Jun 22 watch list was wrong at the moment it was written. Already canon for calls since Jul 10 ("chains are truth"); now demonstrated for puts with real fills.

**3. Two of six calibration entries were built on corrupted prices — the since-fixed fetch_price label-desync bug.** TTD was documented as an $82 stock (real: ~$21-25 — it had already lost half its value in H1 2026 before the screen ever saw it). CMG was documented near $55 (real: ~$31; its put was already ~$13 deep-ITM on screen day). The bug (batch quotes silently shifting prices onto wrong tickers) was caught and fixed Jul 12 — the Jun 22 screens predate the fix, same era as the known TRMB $66.91 failure. Both entries are excluded: not because they're inconvenient, but because the documented instruments could never have been purchased at the documented prices. **Consequence for the final pass: the Jun 22 screen output cannot serve as the calibration baseline as-is. Any name the final back-test counts must first have its screen-day stock price re-verified against real candle data.**

**4. The momentum finding extends to puts.** The two positions whose stories resolved early both resolved against the bear: TSLA's delivery beat and RCL's +26.5% pre-earnings rally. Fading a stock near its highs without a specific, dated disappointment mechanism is fighting momentum with theta on your back — the double disadvantage Calxter's control group predicted from the ratings side (improving ratings starve puts Rule 3 for the same underlying reason).

**5. The only genuine crash in the sample was un-catchable by the rules as designed — and that's worth knowing, not fixing yet.** TTD really did keep collapsing ($25 → $19, another ~-24%, while we watched). But on *clean* data, puts Rule 1 (top 20-25% of range) would have disqualified it on Jun 22 — it was already at its lows. The inverted system, by design, cannot short a knife that's already fallen; it only fades strength. One observation, no rule change proposed. Logged for the final pass to weigh with complete data.

---

## STANDING ITEMS

- **Puts remain blocked for live entry.** The 2-of-6 corruption plus 0-of-4 clean performance to date settles the interim question.
- **Final calibration pass: Aug 8-10, 2026**, after ABNB (Aug 4), DASH (Aug 6-7), and TTD (Aug 7) print and RCL (Jul 25) and TSLA (Jul 22-23) resolve. It re-verifies screen-day prices per Finding 3, scores the four clean names through their catalysts, and renders the permanent verdict — including whether the ≤21-day entry-timing line becomes an Iron Rule.
- **The 3-closed-puts requirement for 5/5 sizing:** still zero; untouched by any of this.
- **TDOC** stays on the gated watch list.

---

## GLOSSARY

- **Back-test:** Evaluating documented hypothetical entries against what the market subsequently did — calibration, not cherry-picking. The standing precondition (Jun 18, 2026) for any live puts entry.
- **Hypothetical fill:** The realistic entry price for a never-placed trade, set by convention at the close of the first trading day after the screen (Jun 23), from real contract candles.
- **Theta:** The daily decay of an option's time value. The "rent" both findings 1 and 4 refer to.
- **Label-desync bug:** The fetch_price.py defect (fixed Jul 12, 2026) where batch quotes dropped invalid tickers and shifted every subsequent price onto the wrong name — the source of the TTD/CMG corruption.
- **Deep ITM (in-the-money):** An option whose strike is far past the current stock price, priced mostly as intrinsic value. A $65 put on a $22 stock is ~$43 deep ITM.
- **Puts Rule 1:** Entry only on stocks in the top 20-25% of their 52-week range with no fresh high in 5 sessions — fading stalled strength, never chasing an existing collapse.
- **Momentum:** The tendency of recent winners to keep winning over multi-week horizons; the force a top-of-range put entry fights.
- **Calibration baseline:** The set of documented entries a back-test scores. Per Finding 3, the Jun 22 baseline requires price re-verification before final use.
- **Substituted (sub.):** The documented strike didn't exist in the historical feed; the nearest listed strike was used (ABNB $117→$115, RCL $185→$190).
