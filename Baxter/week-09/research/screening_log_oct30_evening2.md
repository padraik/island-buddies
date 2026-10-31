# Screening log: Fri Oct 30, EVENING 2 (8:00pm ET)

**Source:** EVENING 1's queue: PL for the doc, then EVENING 3's chain job started early (HBAN, GLXY, MIR, NLY, DX, FLG).
**Reserve / lines:** spendable $592.15 -> R5 line at 3.5/5 = **$0.59**. Nothing below clears it.
**Data:** Friday closing option quotes (stamped 19:59 UTC, so closing spreads), stock closes, analyst counts, earnings dates and daily closes pulled live this run.

## Chain stage

| Ticker | Dir | Stock | Next print | R3 / tool low | Expiries that pass R2 | Contract | Bid / Ask | OI | Spread | BE / needs | Result |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PL | CALLS | 13.465 (R1 0.071) | Wed Dec 9 PM (f), LY Dec 10 PM | 8/5/0, $17 | Jan15 | **$12C** | 2.70 / 2.90 | 2,329 | 7.1% | $14.90 +10.66% | **Doc written, `research_PL_paper.md`. No entry: floor gate.** DB Buy $28 is dated Sep 8 but predates the last ~25%. Enter on a Buy dated after Oct 16 above BE. |
| HBAN | CALLS | 15.79 | Thu Jan 21 AM (f) | 16/7/0, $17 | Feb19 (29 days past) | $16C | 0.50 / 1.20 | 177 | 82% | $17.20 +8.9% | **KILLED, R7 and R6** (cap 3.9%: reactions -0.4, -4.8, +0.1, -6.0; median 2.6%). |
| FLG | CALLS | 10.52 | Fri Jan 29 AM (f) | 12/7/0, $11 | Mar19 | $11C | 0.50 / 0.80 | 153 | 46% | $11.80 +12.2% | **KILLED, R4, R6, R7.** BE over the $11 low; cap 6.2% (reactions -9.3, -5.8, -2.2, -2.4; median 4.1%). Last print was an EPS miss, 0.01 vs 0.07. |
| MIR | CALLS | 18.35 | Tue Feb 9 PM (f) | 10/1/0, $20 | May21 (Feb19 is 10 days past) | $20C | 2.30 / 3.10 | 87 | 30% | $23.10 +25.9% | **KILLED, R4 and R7.** BE over the $20 low. |
| NLY | CALLS | 18.25 | Wed Jan 27 PM (f) | 9/4/0, $19.50 | Apr16 | $19C | 0.61 / 0.81 | 3,140 | 28% | $19.81 +8.5% | **$19C fails R4 and R7.** $18C not pulled; stays for EVENING 3, with R6 measured. |
| GLXY | CALLS | 16.00 | Tue Feb 2 AM (f) | 15/1/0, $20.50 | Apr16 (no Feb or Mar expiry) | $15C / $17.5C | not quoted | | | | Chain lists $2.50 strikes. EVENING 3 quotes `220e1b54` ($15C) and `a0fa8ab5` ($17.5C). |
| DX | CALLS | 10.64 | Mon Jan 25 AM (f) | 4/2/0, $11.50 | Mar19 | $10C | not quoted | | | | Chain lists $2.50 strikes only, no $11C. EVENING 3 quotes `a6b7b83d` ($10C). |

## PL floor work

Three floor searches, two cause searches, plus the MarketBeat and Trefis articles. Dated: Deutsche Bank reaffirmed Buy $28, Sep 8; Northland $40 and Craig-Hallum $35, Sep 4 (ratings not stated). Search summaries calling old notes "October 2026" were thrown out (Goldman $3.50, Deutsche $6 and $17, Wedbush $20, Needham $22): 2025-era targets. Cause of Oct 12-16: not found.

## Real-money read

Nothing under the $0.59 line passes R6. ONDS $6.32, RCAT $4.62, BTBT $0.811, CLSK $7.655: no move toward their lines, same closes as EVENING 1.

## Tally

7 names moved: PL doc written, HBAN, FLG, MIR killed, NLY, GLXY, DX to EVENING 3 with instrument IDs. 0 real-money candidates. Live queue 9, under 10, so EVENING 3's refill is on.

## GLOSSARY
- **R1-R7**: binder Tab 1 Iron Rules (calls). R1 range percentile, R2 earnings before expiry, R3 analyst consensus, R4 bear floor (lowest target above breakeven), R5 price cap on reserve, R6 reachability (needed move <= 1.5x median earnings move), R7 liquidity (OI >= 250, spread <= 25% of mid).
- **BE**: breakeven at expiry = strike + ask.
- **OI**: open interest, contracts outstanding.
- **(f)**: earnings date estimated from cadence, not announced.
- **Tab 6 dating**: a floor only counts if it's dated inside 60 days and published after the stock's decline.
- **Closing spread**: the wider book quoted in the last minute of the session.
- **Paper**: tracked in the paper book, no money moves.
