# Screening Log — Aug 11, 2026 (Tuesday evening) — First full run of the ratified scanner method

First live use of the scanner-based sourcing method since it was ratified Aug 10 (binder Tab 6) and cross-checked Aug 7 (`Correspondence/2026-08-07_from_Baxter_screening_upgrade.md`). Fund is fully in reserve ($1,056.96) after closing UAMY and JMIA earlier today, so this is a fresh sourcing pass, not a follow-up to an open position.

**Method:** `create_scan` / `update_scan_filters` per band, `FILTER_TYPE_MARKET_CAP` BETWEEN the band, `FILTER_TYPE_EARNINGS_DATE` BETWEEN today and +35 days, plus `FILTER_TYPE_HIGH` and `FILTER_TYPE_LOW` (length 52, interval 1w) added as visible columns to compute 52-week range percentile by hand: `(Last - Low) / (High - Low)`.

**New finding, worth its own note:** the scanner's earnings-date filter, which failed three value formats on Aug 7 and was left as a known gap, now works. The field is `fundamental.earningsYmd` and wants a plain `YYYYMMDD` integer (`20260811`, not an ISO date or epoch timestamp). This collapses two separate steps (scan for range, then `get_earnings_results` per name) into one scan per band. Binder updated separately with this.

## Bands run tonight

| Band | Total items | Returned (200 cap) | CALLS candidates (≤25th pctile) | PUTS candidates (≥75th pctile) |
|---|---|---|---|---|
| $300M–$1B | 353 | 200 | 60 | 50 |
| $1B–$5B | 248 | 200 | 47 | 50 |
| $10B–$50B | 96 | 93 | 12 | 30 |

**Note on the 200-item cap:** `run_scan`/`create_scan` return at most 200 rows, sorted by market cap descending, with no pagination cursor exposed to this tool. The $300M–$1B and $1B–$5B bands both exceed that (353 and 248 total matches), so each is missing its smallest ~50-150 names — the largest-cap names within each band are what's actually shown. Not a blocker, but the pool isn't perfectly complete; narrower bands would close the gap if that matters later. Two bands ($5B–$10B, $50B–$150B+) weren't run tonight to keep this session's scope reasonable — the three run already cover small, mid, and large cap and comfortably exceed the 10-20 name research budget.

**Sanity check:** several already-known names surfaced in the right place — UAMY (18.9th pctile) and JMIA (0.8th pctile) both showed up correctly in the $300M-$1B band on the day they were both closed; previously-killed names CPRT, QXO, TME, HIVE, DQ, PFLT all reappeared in their expected low-percentile slots. The method is finding what it should.

## CALLS candidates, all three bands combined, previously-screened names excluded

Excluded from the list below: JMIA and UAMY (closed today), CPRT/QXO/TME/HIVE/DQ/PFLT (killed Aug 8, no new information tonight to reopen any of them), KR (closed today on the ramp rule — technically re-clears the scanner at 8.1st percentile, but re-entering the same name hours after exiting it needs its own explicit conversation, not a default include).

**Deprioritized, not excluded: names reporting today or tomorrow (Aug 11–12).** No real DD window left to do the work properly before the print — ONON, FNV, ALC, IHG, CIB, ARMK, SMCI, APGE, VG, ESLT, NNNN, IMSR, VINP, HUYA, URG, CINT, JBI. Worth a look if any survive as a *later* catalyst on a different report, not tonight's queue.

**Shortlist for next full-funnel pass (chain check + Rule 3 + Rule 2 re-verify), 3+ day buffer, spread across bands:**

| Ticker | Pctile | Price | 52wk range | Mcap | Earnings | Band |
|---|---|---|---|---|---|---|
| REZI | -5.3% | $24.41 | $25.46–$45.29 | $3.67B | 8/12 | 1B-5B |
| XPEV | 1.5% | $11.79 | $11.54–$28.23 | $11.49B | 8/24 | 10B-50B |
| GEMI | 0.7% | $4.05 | $3.74–$45.89 | $0.52B | 8/13 | 300M-1B |
| BTGO | 1.9% | $5.04 | $4.67–$24.50 | $0.58B | 8/12 | 300M-1B |
| CSAN | 2.7% | $2.62 | $2.52–$6.00 | $2.68B | 8/14 | 1B-5B |
| NIO | 5.9% | $4.58 | $4.37–$8.02 | $12.12B | 9/2 | 10B-50B |
| FLO | 3.9% | $7.19 | $6.80–$16.85 | $1.51B | 8/20 | 1B-5B |
| LI | 6.6% | $12.67 | $11.65–$27.10 | $12.54B | 8/28 | 10B-50B |
| SOC | 7.1% | $4.80 | $2.88–$29.86 | $0.98B | 8/12 | 300M-1B |
| MNSO | 6.0% | $12.05 | $11.12–$26.74 | $3.74B | 8/21 | 1B-5B |
| TIGR | 7.8% | $4.75 | $4.00–$13.55 | $0.88B | 8/27 | 300M-1B |
| KEP | 8.9% | $12.34 | $11.25–$23.41 | $16.27B | 8/12 | 10B-50B |
| QFIN | 6.1% | $12.76 | $11.31–$34.95 | $1.6B | 8/14 | 1B-5B |
| STNE | 6.6% | $10.14 | $9.45–$19.95 | $2.52B | 8/13 | 1B-5B |
| WB | 12.9% | $7.85 | $7.09–$12.96 | $1.93B | 8/19 | 1B-5B |
| NNE | 9.4% | $19.04 | $14.71–$60.87 | $1.0B | 8/12 | 300M-1B |
| BTBT | 3.9% | $1.31 | $1.18–$4.55 | $0.45B | 8/13 | 300M-1B |
| LULU | 17.7% | $125.91 | $104.44–$225.98 | $14.51B | 9/4 | 10B-50B |

SOC is worth flagging specifically: it was gated (not killed) back in July per the July 30 session note, and this is the first time since then it's resurfaced on a clean sweep rather than a targeted re-check. Worth revisiting whether the old gate condition is still relevant before it gets full DD again.

Full raw scan output not saved verbatim (regenerable via the scan_ids: $300M-1B and $1B-5B bands were saved to disk automatically by the tool due to size; $10B-50B returned inline). Percentile computation script was scratch, not archived.

## GLOSSARY

- **Range percentile:** where the current price sits between the stock's 52-week low and high: `(price - low) / (high - low)`. Bottom quartile (≤25%) is a CALLS candidate under Rule 1; top quartile (≥75%) is a PUTS candidate.
- **Scanner (Robinhood market scanner / screener):** a live filtering tool over the tradeable market, run here via `create_scan`, `update_scan_filters`, and `run_scan`. Returns real-time data, capped at 200 rows per scan with no pagination exposed to this tool.
- **`get_earnings_results`:** the fund's standing first source for earnings dates (binder Tab 6, Aug 7, 2026), returning a company's real reporting history plus a `verified` flag (true = company-announced, false = estimated from cadence).
- **Rule 1 / Rule 2 / Rule 3:** THE UNIFIED SCREEN's first three steps — range percentile, confirmed catalyst before expiry, and analyst ratings direction (max 1 Sell for CALLS). This scan handles Rule 1 and (via the earnings-date filter) a first pass at Rule 2; Rule 3 still requires a per-name check.
- **CALLS / PUTS candidate:** which direction a name screens for based on Rule 1 — bottom-quartile stocks are bought on weakness (calls), top-quartile stocks are faded on strength (puts).
