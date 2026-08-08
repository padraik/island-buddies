# Research: HIVE (HIVE Digital Technologies Ltd.), Aug 7 to 8, 2026

**Verdict: KILL. Rule 6 decisive fail, compounded by unresolved earnings-date risk. Not queued.**

## Setup

- Price: $2.85 (Aug 7, 2026 close, live re-verified)
- 52-week range: $1.73 to $7.84
- Percentile: 18.2nd, bottom quartile

## The earnings-date problem (checked first, per the Aug 7 standing rule)

`get_earnings_results` returns HIVE's upcoming print at **2026-08-21, PM, verified: false** (estimated from cadence, not company-announced). HIVE's own fiscal cadence is irregular (Q4 FY2025 came Jun 26, 2025; Q1 FY2026 followed only 7 weeks later on Aug 14, 2025; the gaps between quarters run 7 to 15 weeks with no clean pattern), so a cadence-based estimate here is less trustworthy than usual.

A confirming WebSearch, run because the tool flagged this date unverified, did not confirm Aug 21. It surfaced **Aug 18, 2026, after close**, sourced to MarketBeat and labeled "Confirmed" there. Neither date could be traced to an actual HIVE press release or 6-K filing: the only fiscal-2027 Q1 filings found were the company's Q4/full-year FY2026 release from June 1 to 2, 2026, nothing for the upcoming quarter. **The real report date is genuinely unresolved, somewhere between Aug 18 and Aug 21, 2026, with no company confirmation either way.**

This matters specifically because the pre-screen's Aug 21 candidate expiry is the same date the tool's own (unverified) estimate uses for the earnings release, PM. If that combination were correct, the Aug 21 contract would already be dead, expired and settled at the close, before HIVE's own after-hours release ever printed. That is a worse version of the exact structural trap that put KR into the ledger on a wrong date: not a mistaken date corrected in time, but an option that structurally cannot see its own catalyst. If the real date is Aug 18 instead, three trading days of room exist before Aug 21 expiry, which would be fine. Both are live possibilities right now, and neither is confirmed.

**Later-expiry check (explicitly requested):** a later, tradable expiry chain does exist. HIVE's live option chain lists Aug 21, Aug 28, Sep 4, Sep 11, Sep 18, Sep 25 (and further months out) as active. Real markets exist near the money at both later dates: Aug 28 $3.00C bid $0.15 / ask $0.25 (open interest 65); Sep 4 $3.00C bid $0.25 / ask $0.35 (open interest 116). So the earnings-timing problem, if it is real, has a structural fix available. It does not need to be used here, because the play dies independently below.

## Rule 6 (Reachability), the actual kill

Candidate instrument: $3.00C, breakeven $3.20 (matches the pre-screen). Needed move from $2.85: **+12.28%.**

Four real, verified earnings-day reactions pulled from actual daily bars:
- Aug 14, 2025 (PM release, reaction next session): close $2.25 to $2.22, -1.33%
- Nov 17, 2025 (AM release, same-session reaction): close $3.31 to $3.56, +7.55%
- Feb 17, 2026 (AM): close $2.21 to $2.12, -4.07%
- Jun 2, 2026 (AM): close $4.76 to $4.54, -4.62%

Median absolute move: **4.35%.** 1.5x cap: **6.52%.**

**Rule 6: decisive fail.** The required move (12.28%) is roughly **1.9 times** the cap, independent of which earnings date turns out to be correct and independent of which expiry gets used. HIVE simply has not moved enough on its last four prints to plausibly deliver this. Moving to the Aug 28 or Sep 4 expiry, which would fix the timing structure, does not fix this: the stock's own history is the constraint, not the calendar.

## Decline category, Rule 3, Rule 4, Rule 5, straddle

Not scored. Rule 6 kills this decisively on its own, and the earnings-date uncertainty is disqualifying on a second, independent axis. Per binder precedent, spending further research budget on ratings, bear floor, or a straddle cross-check would not change the verdict.

## What would reopen this

Company confirmation of the real Q1 FY2027 date would resolve the structural half of this kill, but Rule 6 is the harder wall: HIVE would need either a strike needing under 6.5% (not available near the money at any live expiry checked tonight) or a meaningfully more volatile earnings history than its last four prints show. Not worth requeuing on the current chain.

## GLOSSARY

- **52-week range / percentile:** where the current price sits between the stock's low and high over the trailing year; 0% equals the low, 100% equals the high.
- **Rule 2 (confirmed catalyst):** the Iron Rule requiring a dated earnings event before the option's expiration.
- **Rule 6 (reachability):** the move required to reach breakeven must not exceed 1.5x the stock's median historical earnings-day reaction, checked against real price bars.
- **verified flag:** `get_earnings_results`' indicator of whether an earnings date is company-announced (true) or estimated from reporting cadence (false).
- **Breakeven:** strike price plus premium paid per share, the price at which the option holder neither gains nor loses at expiration.
- **Same-day expiry-catalyst trap:** the structural failure mode where a PM earnings release lands on the same day an option expires, so the contract settles before the market can react to its own catalyst. First identified on this fund's real KR position (wrong date, discovered after entry, Aug 7 2026).
- **Open interest:** the number of outstanding contracts for a given strike and expiry, a rough proxy for how real a market is beyond the quoted bid/ask.
