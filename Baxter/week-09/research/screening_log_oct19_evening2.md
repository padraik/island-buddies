# SCREENING LOG: Mon Oct 19, 2026, 8:00pm ET (VM EVENING 2 of 3)

*Session job: write the docs for names that cleared the chain stage (MSTR), then start EVENING 3's refill early. Market closed; every quote is Monday's 3:59pm close. Reserve $676.28 (3.5/5 real-money line $0.676). Nothing real-money passes R6 under that line, so everything here is paper-track.*

## Part 1: the doc

| Ticker | Contract | Result | Verdict |
|---|---|---|---|
| **MSTR** | **Nov20 $120C** `da3b54fb` (alt Dec18 $120C `bd3cc447`) | Q3 now **Oct 29 PM `verified: true`** (was unverified Saturday). R1 0.242 at $136.02 (high $306.16 Oct 20 2025 rolls off: line $137.86 Tue, $136.31 Wed, $130.44 by Oct 29). R2 exactly (LY Oct 30 + 21 = Nov 20; 10-Q Nov 9). R3 20/2/0. R4 tool low $165 / Barclays OW $175 (Oct 9) vs BE $142.05. R6 six prints re-pulled: median 5.22%, cap 7.82%, needs +4.43%. R7 OI 1,764, spread 8.0%. Dec18: BE $146.00, +7.34% (0.48 pt of R6 room), spread 12.9% | **DOC WRITTEN + PAPER ENTRY** at the $22.05 closing ask. `research_MSTR_paper.md`, vote 3-2 |

## Part 2: sweep re-run (EVENING 3's job, started early)

Preview (not saved): market cap >= $300M, `FILTER_TYPE_EARNINGS_DATE` **20261022-20261223**, `FILTER_TYPE_TOTAL_CALL_VOLUME` > 300 (Monday), 52w range pct expression < 0.25, split by `FILTER_TYPE_LAST`: $2-15: **193**, $15-50: **116**, $50+: **107**. **416 rows.** Diffed against every week-08/09 file, passes.md, paper_book.md, the queue and the October journals: **4 names never seen** (TRVI, XIFR, LAND, CLS). Same finding as Saturday: the bottom quartile is fished out; new names come from stocks falling into it, one or two a day.

| Ticker | Last | R1 (scan) | R3 B/H/S, low target | R2 (tool, LY) | R6 base median / cap | Contract | Quote (close) | BE / needs | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| XIFR | $9.76 | 0.237 | 2/8/3, $7 | -- | -- | -- | -- | -- | **KILL R3** (3 Sells, 2 Buys < 8 Holds) |
| LAND | $8.84 | 0.193 | no coverage | -- | -- | -- | -- | -- | **KILL R3** (no coverage) |
| TRVI | $11.90 | 0.200 | 12/0/0, $23 | Nov 12 PM (f), LY Nov 13 -> Dec18 | -0.79 / -4.47 / -2.73 / +0.05: **1.76% / 2.64%** | Dec18 $10C-$12C | $10C 1.00 / 4.00, **OI 0**; $11C, $12C no bid, OI 0 | -- | **KILL R7** (OI 0 on every near strike; R6 cap 2.64% kills it anyway) |
| **CLS** | $300.35 | **0.246** | **25/0/0, $375** (undated) | **Oct 26 PM (v)**, LY Oct 27 -> Nov20 passes (Oct 27 + 21 = Nov 17) | +8.16 / -13.10 / -14.37 / +10.04: **11.57% / 17.36%** | **Nov20 $310C** `1d6db773-8ba0-40db-b037-34c89685b50a` | 24.00 / 27.20, **OI 1,970**, spread 12.5% | $337.20 / **+12.27%** | **ADVANCE (paper), floor-dating gate.** One search: only 2025 cuts (Barclays $157 -> $126, Argus $150 -> $120, when CLS was ~$100). The $375 has no owner or date. Alternates: $300C 26.50 / 30.90, OI 113, spread 15.3%, BE $330.90 (+10.17%); $320C 17.90 / 23.50, OI 445, spread 27% (R7 fail); $290C OI 38 (R7 fail) |

**CLS detail.** Celestica fell from ~$422 (Apr 27 close, before a -14.4% print) to $300. Two of the last four prints went down 13-14%, so this one's reachability is wide, but in both directions. Same AI-hardware bucket as the paper AVGO position. R2 note: Celestica may file 6-Ks as a Canadian issuer; both the tool date and last year's date exist, so it passes either reading. **Time limit:** the print is Mon Oct 26 PM, so the paper ramp sell would be Mon Oct 26 3:35pm. An entry after Thu Oct 22 has two days of ramp left and isn't worth logging. **Kill date Thu Oct 22** if the floor isn't dated by then.

## Moved this run

7 names: **MSTR** to a doc and a paper entry; **CLS** advanced (paper, floor gate); **XIFR, LAND** killed R3; **TRVI** killed R7. Plus a 416-row sweep diff. 2 searches (MSTR Friday drop: nothing dated; CLS floor: only 2025 cuts).

## GLOSSARY
- **R1-R7:** binder Tab 1 Iron Rules. R1 52-week range percentile (< 0.25 for calls), R2 earnings proven before expiry, R3 consensus (<= 1 Sell, >= 3 Buys, Buys >= Holds), R4 lowest Buy target above breakeven, R5 affordability, R6 breakeven move <= 1.5x median print move, R7 OI >= 250 and spread <= 25% of mid.
- **(v) / (f):** `get_earnings_results` verified true / false. **LY:** last year's same-quarter report date.
- **Preview scan:** the Robinhood scanner run without saving it.
- **Fished out:** nearly every bottom-quartile name with a print in the window has already been through the funnel this month.
- **Floor-dating gate:** R4 passes on the number, but the target's owner and date are unknown, so it may be a stale pre-decline target (binder Tab 6).
- **Paper:** tracked-only entries in `paper_book.md`, at the ask in, the bid out.
