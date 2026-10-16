# Screening log, Thu Oct 15, EVENING 2 (8:00pm ET)

EVENING 2's job: research docs for every name past the chain stage. The two candidates (LBRT, RIOT) were both gated on a dated floor, so the first half of the session re-scored them against binder Tab 6 ("A bear floor is only as good as its publication date": targets dated within 60 days and published after the decline). Neither clears it, so no doc got written. With that job done early, the session started EVENING 3's: a fresh scan of December prints.

Names moved: 2 re-scored + 27 new. Killed: 1 re-scored (LBRT) + 26 new. Advanced: 1 (PL, paper, gated on a dated floor). Two web searches (LBRT floor, PL floor), plus one on the COUR date (held position, not counted here).

## Held position: COUR date change

`get_earnings_results` now says COUR Q3 **Thu Oct 29 PM, `verified: true`** (6pm: Oct 26 PM, unverified). Ramp sell moves to Thu Oct 29 3:35pm ET (window Wed Oct 28); Wed Oct 21 stays the fallback until PREMARKET finds a second source. Rule 2 passes with 22 days (needs 21). Details: positions.md, research_COUR.md EXIT PLAN addendum.

## Re-scores (dated-floor gate)

| Ticker | Contract | Close quote | Stock | BE (ask) | Needs | R6 cap | R7 | Floor | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| LBRT | Nov20 $17C | 1.15 / 1.45 | $16.70 (-7.4%) | $18.45 | +10.5% | 19.57% | 20,026 / 23.1% | Tool low $19, record stamped 2024-11. Search: $21-40 range, the latest dated actions are Piper $34 -> $30 (Aug 2026) and Stifel $37 -> $36 (Jul 2026); the low's owner and date unknown | **KILL, R4 (Tab 6: no dated, post-decline floor).** Also the clock: print Oct 21 PM verified, ramp sell Tue Oct 20, so even a Friday paper entry is a 3-session hold. No 8-K since Oct 1 explains Thursday's -7.4% (two Form 4s, Oct 5 and Oct 7) |
| RIOT | Nov20 $13C | 2.77 / 4.05 | $15.51 | $17.05 | +9.93% | 10.69% | 568 / 37.5% (closing width) | JPM $22, Aug 17: 59 days old today, 60 tomorrow, and published with RIOT ~$19-20, before the slide | **PARK.** Fails Tab 6 as of today (pre-decline). Earnings Oct 29 PM (unverified, LY Oct 30). Miners often get preview notes the week before the print; a Buy target dated after Sep 15 with a low above BE clears it. Re-check ratings every run through Tue Oct 27; if nothing by then the ramp window is gone: kill |

## New scan: December prints

Preview (not saved): market cap >= $300M, `FILTER_TYPE_EARNINGS_DATE` **20261205-20261224**, 52w range pct expression < 0.25, all prices. **28 rows** (LEN.B skipped as a share class). All 27 went through `get_equity_analyst_ratings`. Contract for these prints: Jan15 (Dec18 fails Rule 2's 21 days for any print after Nov 27).

| Ticker | Direction | Last | Range pct | Ratings (B/H/S), low | Verdict |
|---|---|---|---|---|---|
| AZO | CALLS | $3,046 | 0.223 | 27/5/0, low $3,000 | KILL R4 proxy (low under price) |
| TOL | CALLS | $134.33 | 0.247 | 17/5/1, low $118 | KILL R4 proxy |
| ORCL | CALLS | $133.41 | 0.091 | 36/8/1, low $110 | KILL R4 proxy |
| AVAV | CALLS | $123.24 | -0.040 | 20/5/0, low $165 | Chain: Jan15 $125C 14.70 / 17.80 OI 24; $130C 13.40 / 15.40 OI 27. **KILL R7** (OI) |
| RH | CALLS | $119.68 | 0.101 | 7/13/2 | KILL R3 |
| LULU | CALLS | $99.15 | 0.065 | 4/27/6 | KILL R3 |
| LEN | CALLS | $78.00 | 0.071 | 3/10/11 | KILL R3 |
| KBH | CALLS | $43.54 | 0.027 | 3/10/6 | KILL R3 |
| CNM | CALLS | $41.79 | 0.117 | 10/6/1, low $40 | KILL R4 proxy |
| NKE | CALLS | $37.19 | 0.136 | 11/25/7 | KILL R3 |
| GIS | CALLS | $32.91 | 0.094 | 4/15/4 | KILL R3 |
| PLAB | CALLS | $28.54 | 0.236 | none | KILL no coverage |
| OXM | CALLS | $27.54 | 0.132 | 0/6/0 | KILL R3 |
| CHWY | CALLS | $21.30 | 0.175 | 22/9/0, low $21 | KILL R4 proxy |
| CPB | CALLS | $19.86 | 0.093 | 1/14/8 | KILL R3 |
| DAKT | CALLS | $18.27 | 0.130 | none | KILL no coverage |
| XZO | CALLS | $14.89 | 0.207 | none | KILL no coverage |
| **PL** | CALLS | $14.57 | 0.098 | 8/4/0, low $17 | **ADVANCE (paper), dated-floor gate.** See below |
| CAG | CALLS | $14.11 | 0.203 | 1/12/6 | KILL R3 |
| NNE | CALLS | $13.57 | -0.025 | 7/1/0, low $22 | Dec 17 PM (f), LY Dec 18. Jan15 $14C OI 27; $15C 1.40 / 1.60 OI 791, BE $16.60, needs +22.3%. 6-print median 3.25% (cap 4.9%). **KILL R6** |
| PHR | CALLS | $11.55 | 0.232 | 10/8/0, low $10 | KILL R4 proxy |
| SPIR | CALLS | $9.30 | 0.140 | none | KILL no coverage |
| UEC | CALLS | $8.04 | -0.076 | 8/3/0, low $10 | Dec 9 AM (f), LY Dec 10. Jan15 $8C 1.12 / 1.20 OI 791 (6.9%), BE $9.20, needs +14.4%; $9C needs +23.3%. 6-print median 5.4% (cap 8.1%). **KILL R6** |
| FWDI | CALLS | $7.05 | 0.162 | none | KILL no coverage |
| MOMO | CALLS | $4.77 | 0.061 | 6/0/0, low $6.72 | Jan15 strikes are adjusted (x.74, non-standard deliverable); $4.74C 0.20 / 0.45 (77% spread). **KILL R7** |
| GLOO | CALLS | $3.32 | 0.059 | 6/0/0, low $7 | Tool date moved to **Jan 13, 2027** (f), LY Dec 17: needs a Feb+ expiry. **KILL R2** for this window |
| VZLA | CALLS | $3.31 | 0.100 | none | KILL no coverage |

### R6 bases (daily closes; AM print = prior close to print-day close, PM = print-day close to next close)

- **UEC** (AM): Jun 2 '25 -4.0%, Sep 24 '25 -1.2%, Dec 10 '25 -7.4%, Mar 10 '26 +6.8%, Jun 9 '26 -15.5%, Sep 29 '26 +0.9%. Median **5.4%**, cap 8.1%.
- **NNE**: May 16 '25 AM +4.5%, Aug 14 '25 PM +2.0%, Dec 18 '25 AM +0.8%, Feb 17 '26 PM -0.6%, May 14 '26 PM -9.5%, Aug 12 '26 PM +7.9%. Median **3.25%**, cap 4.9%.
- **PL**: Jun 4 '25 PM +49.4%, Sep 8 '25 AM +47.9%, Dec 10 '25 PM +35.0%, Mar 19 '26 PM +25.5%, Jun 4 '26 PM -26.0%, Sep 3 '26 PM -1.3%. Median **30.5%**, cap 45.75%.

### PL Jan15 calls (chain `f81baef2-21f8-4da6-aa94-a0bf03124a95`)

Jan15 strikes near the money: $10, $15 (no $12.5 / $13 / $14 / $16). Dec18 fails R2 (Dec 10 + 21 = Dec 31).

| Strike | Bid / ask | OI | Spread | BE (ask) | Needs | R4 (low $17) | Verdict |
|---|---|---|---|---|---|---|---|
| $15C `0d73590a-85cf-49a9-9384-580ad50217b3` | 2.05 / 2.30 | 1,453 | 11.5% | $17.30 | +18.7% | **fails by $0.30** | out |
| **$10C** `bb9b3f83-1e43-4a35-aa61-1fd838d3d82f` | 4.60 / 5.30 | 4,174 | 14.1% | **$15.30** | **+5.0%** | passes by $1.70 | **ADVANCE (paper)** |

- R1 0.098 pass. R2: Q3 (FY27) Dec 9 PM `verified: false`, LY Dec 10 PM; Jan 15 is 36 days after the later date; 10-Q deadline (Oct 31 quarter) ~Dec 10, 24 trading days before expiry: pass. R3 8/4/0 pass. R4 $17 vs $15.30 passes on number. R5: $5.30 ask, far over the $0.676 line: **paper only**. R6 +5.0% vs 45.75% cap: pass with a lot of room. R7 4,174 / 14.1%: pass.
- The $10C is deep in the money (delta 0.90), so it behaves like stock with a defined loss, not like a cheap lottery ticket. Worth saying in the doc: most of the premium is intrinsic, so the ramp gives less here than on an at-the-money strike.
- **Gate (binder Tab 6):** the $17 low has no date. PL fell from ~$43 (June) to $14.57; the one search found only older actions (Northland $17 -> $28, Jan 13; Goldman $12.30 -> $16.40, Jan 20) and a TheStreet $17 from Dec 2025, nothing after the slide. Same shape as RIOT. Next: a Buy target dated after the Sep 3 print with a low above $15.30, then the paper doc (Five-Baxter, exit plan: ramp sell Tue Dec 8 3:35pm, print Dec 9 PM).

## GLOSSARY

- **R1-R7:** the Iron Rules in binder Tab 1. R1 range position, R2 earnings before expiry, R3 analyst consensus, R4 lowest Buy target above breakeven, R5 price cap on reserve, R6 required move vs. typical earnings move, R7 liquidity (OI >= 250, spread <= 25% of mid).
- **R4 proxy:** a free screen: if the lowest analyst target is already under the stock price, no call can have its breakeven under that target, so the name dies before a chain check.
- **Dated-floor gate (Tab 6):** a Rule 4 target only counts if it was published within 60 days and after the stock's decline. An old target from before the drop is a downgrade waiting to happen.
- **BE (breakeven):** strike plus the premium paid, here at the ask.
- **OI (open interest):** contracts currently open at that strike. A thin number means a wide, expensive exit.
- **Adjusted strike:** a contract changed by a corporate action (MOMO's special dividend), with an odd strike and a non-standard deliverable. They trade thinly.
- **Delta:** how much the option moves per $1 in the stock. 0.90 means it moves almost like the stock.
- **(f) / verified:** the earnings tool's flag. `verified: true` means the company announced the date; false is an estimate from its cadence.
- **Ramp sell:** selling before the print, into the rising pre-earnings premium, instead of holding through the IV crush.
- **Paper:** tracked in `paper_book.md` with no money; real-money entries also need Rule 5.
