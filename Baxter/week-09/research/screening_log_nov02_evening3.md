# Screening log: Mon Nov 2, EVENING 3 (10:00pm ET)

**Source:** two unsaved scan previews (same filters as `e6411b30`, nothing saved). (a) The under-$8.45 band ($1-8.45) with the call-volume floor dropped 300 -> **50** and the print window widened to **Nov 3 - Mar 5**: 179 rows, **2 never logged** in week-09 (ADAM, AUTL). (b) The $8.45+ bands, prints **Feb 13 - Mar 5** only (the slice no scan had covered), call volume >= 300: 25 rows, all logged somewhere in week-09 before, so all 25 were re-rated free on tonight's counts.
**Reserve / lines:** spendable $592.15 -> R5 line at 3.5/5 = **$0.592**.
**Data:** Monday closing option quotes (stamped 20:59 UTC), official closes, AUTL daily closes Oct 2024 - Nov 2026, analyst counts and earnings dates, all pulled live this run. 0 web searches.

## Chain stage

| Ticker | Dir | Stock | Next print | R3 / tool low | Contract | Bid / Ask | OI | Spread | BE / needs | R6 cap | Result |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AUTL | CALLS | 1.42 close (scan 1.44), R1 0.188 | Tue Nov 10 AM `verified: true`, LY Wed Nov 12 2025 AM | 10/0/0, $5.00 | Dec18 $1C / $1.5C / $2C; Mar19 $1.5C | 0.10 / 1.10; 0.00 / 0.50; 0.05 / 0.25; 0.20 / 0.55 | 601 / 1,959 / 830 / 413 | 167% / no bid / 133% / 93% | $2.10 +48%; $2.00 +41%; $2.25 +58%; $2.05 +44% | 14.3% (6 verified prints: +9.8, -12.8, -9.3, -6.2, -7.0, +12.6; median 9.55%) | **KILLED, R6 + R7.** R2 passes (Dec18 is 36 days after Nov 12). The $1.5C Dec18 would need an ask of $0.12 or less to clear R6, and it has no bid. Every contract fails R7 on spread. |
| SBSW | CALLS | 8.75, R1 0.066 | H2 results ~Feb 25 (tool data garbled: 2021 rows stamped 2026/2027); 6-K filer | 6/4/1, $9.60 | Apr16 $8C / $9C | 1.40 / 2.15; 1.05 / 1.55 | 3 / 82 | 42% / 38% | $10.15; $10.55 | not computed | **KILLED, R4 + R5 + R7.** Both BEs are over the $9.60 low; asks are 2.6-3.6x the $0.592 line; OI 3 / 82. |

## Free stage (re-rated on tonight's counts)

- **ADAM** ($5.98, R1 under its 52-week low, prints Feb 18): 2/4/0. **R3** (2 Buys). Out.
- **R3 fails (10):** BLDR 9/16/2, SFM 9/8/3, FND 5/15/5, AMRZ 14/12/2, MIAX 3/4/0, KGC 17/2/2 (2 Sells), RKT 8/9/0, ALKT 2/6/1, ARR 2/4/0, FVRR 0/10/0.
- **No coverage (2):** HYMC, MRAM.
- **R4 proxy, low at or under the stock (5):** FSLR (29/10/1, $161 vs $183.98), OLED ($71 vs $89.70), CSGP ($26 vs $31.82), LKQ ($18 vs $19.64; stamp May 2025 anyway), EXE ($92 vs $89.00, 3.4% room, nothing reachable after premium).
- **Pass R3 + R4 proxy, to the chain (paper-size, Feb prints):**
  - **STRL** $338.00, 11/0/0, low $565, prints Thu Feb 25 (f). Next: LY date, Mar19 / Apr16 chain.
  - **MTZ** $194.25, 24/1/0, low $232 (stamp Nov 1), prints Fri Feb 26 (f). Next: same.
  - **INSM** $109.69, 24/1/0, low $158, prints Fri Feb 19 (f). Was floor-gated on a stale low Oct 19-20; re-date the $158 first.
  - **UCTT** $47.72, 6/0/0, low $80, prints Tue Feb 23 (f). Killed on R6 Oct 20 at the Dec print (+14.1% vs 9.87%); re-test on Apr16.
  - **RSI** $11.63 (under its 52-week low), 12/3/0, low $15, prints Tue Feb 16 (f). Killed R6 Oct 2026 on the Oct print; re-test on Apr16 (no Mar19 listed).
  - **IONS** $41.04, 24/4/0, low $58 (stamp Oct 3), prints Thu Feb 25 (f). Killed R7 on Dec18 tonight (EVENING 1); the Feb print needs Apr16; re-test R7 there.
  - **AGI** $27.76, 12/1/0, low $34.37. Killed R7 on Mar19 tonight (EVENING 1); Apr16 not checked. Stays dead this week.
- **Gates (unchanged):** CRDO 21/1/0 low $235 (no stamp); NIO 16/7/1 low $3.7053 (stamp Sep 1); PL 8/5/0 low $17.

## Totals

29 names moved: AUTL and SBSW killed at the chain; ADAM, BLDR, SFM, FND, AMRZ, MIAX, KGC, RKT, ALKT, ARR, FVRR (R3), HYMC, MRAM (no coverage), FSLR, OLED, CSGP, LKQ, EXE (R4 proxy) out free; AGI stays dead; STRL, MTZ, INSM, UCTT, RSI, IONS to the chain queue (paper-size); CRDO, NIO, PL gates re-read. **0 real-money advances.** Dropping the call-volume floor to 50 on the cheap band found only 2 new names, and both died. The cheap band is fished out through early March.

## GLOSSARY
- **R1-R7**: binder Tab 1 Iron Rules (calls). R1 range percentile, R2 earnings before expiry, R3 analyst consensus, R4 bear floor (lowest target above breakeven), R5 price cap on reserve, R6 reachability (needed move <= 1.5x median earnings move), R7 liquidity (OI >= 250, spread <= 25% of mid).
- **BE**: breakeven at expiry = strike + ask.
- **OI**: open interest, contracts outstanding.
- **(f)**: earnings date estimated from cadence, not announced.
- **LY**: last year's same-quarter report date.
- **6-K filer**: foreign private issuer; no 10-Q deadline, so R2 needs both the tool date and last year's date.
- **R4 proxy**: at the free stage, a tool low target at or under the stock price means no strike can pass R4.
- **Floor gate**: R4 passes on the numbers, but no Buy target is dated after the stock's decline (binder Tab 6), so no entry until one is found.
- **Paper-size**: one contract costs more than the R5 line, so it can only go in the paper book.
- **Call-volume floor**: the scan's minimum day's call volume; lower floors find thinner names that usually die on R7.
