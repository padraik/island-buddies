# SCREENING LOG: Fri Oct 23, 2026, EVENING 3 (10:00pm ET)

*Market closed; quotes are the 4:00pm close. Session 3's job: refill the queue and leave PREMARKET a plan. Worked EVENING 2's list in order: holdings fact check, the CDE floor gate, the $25-100 mid-cap band at prints Nov 2 - Dec 18 (the one band that hadn't run at the new window), and Jan15 re-tests on IDXX / FN. 50 names moved: 1 gate verdict (CDE), 47 never-screened names to the free screen, 7 to chains, 2 Jan15 re-tests. 0 advanced. 2 web searches (both CDE). No Discord messages.*

New saved scan:
- `Baxter Oct23 E3 25-100 midcap Nov2-Dec18 prints` (`9ba31349-392d-43c8-9259-0fe057e2366d`): $0.3-10B cap, stocks only, $25-100, R1 < 0.25, prints Nov 2 - Dec 18. 121 rows (under the 200 cap, so the band is complete); 47 never in a week-09 screening log or passes.md.

## Held (fact check)

| Contract | Close quote | Stock | Earnings | Ratings / low vs BE | SEC since Oct 20 | Verdict |
|---|---|---|---|---|---|---|
| COUR $5C Nov20 | 0.45 / 0.60 (OI 3,257, IV 86%) | $5.085 (AH $5.08) | Thu Oct 29 PM `verified: true`, `actual: null` | 8/4/0, low $6.00 vs BE $5.65 | none | Nothing changed. Ramp sell Thu Oct 29 3:35pm. GTC $1.65 `confirmed`. |
| QUBT $7C Dec18 | 0.36 / 0.61 (OI 1,125) | $6.555 (AH $6.52) | Fri Nov 13 PM `verified: false` (LY Nov 14 PM), `actual: null` | 5/2/0, low $10 vs BE $7.54 | none | Nothing changed. Ramp sell Thu Nov 12 3:35pm. GTC $1.35 `confirmed`. |

Paper: PAAS 6/2/0 low $51 vs BE $43.90 (stock $40.125): holds. TMUS 27/4/0 low $169 vs BE $165.20 (stock $146.61, AH $146.96): holds; paper ramp sell Tue Oct 27 3:35pm.

## CDE gate (paper, `research_CDE_paper.md`)

Needed: a Buy-rated target dated after the Sep 4 slide and above BE $14.75. Two searches.
- Scotiabank Outperform, $28.50 -> $26.50: undated in every result.
- **Roth Capital Buy, $21 -> $19:** the only named Buy move with a reason attached, and the reason is "weaker-than-expected Q2 results" / "weaker gold and silver price outlook". Coeur's Q2 print was in early August, so this is a pre-slide (or at best undated) target, not a post-slide floor.
- Already on file: Cantor Buy -> Hold $16, Cormark Buy -> Market Perform $21 (undated, both the wrong way).

**Verdict: KILLED on R4 (Tab 6 dated-floor rule).** No Buy target was found that is dated after the decline. Every named move points down. The tool's $18 low stays unowned. Stock $13.465 (-3.0% Fri). Don't reopen this quarter unless a dated post-slide Buy target appears on its own.

## Free screen: R3 + R4 proxy (47 never-screened names)

| Result | Names |
|---|---|
| No coverage (25) | NFG, WLDN, AGO, TNC, MMS, VPG, LMB, ATMU, WLFC, ASTE, TGLS, BIPC, TDS, CSV, TR, WD, AD, SLVM, LZB, BFS, BEPC, HY, KELYB, AMSC, OGC |
| **R3** (8) | TAP.A 5/12/5, ZG 14/16/0, SEDG 1/20/6, HESM 1/3/3, PRKS 5/8/0, KMPR 2/2/2, WGO 5/9/0, BLSH 6/7/0 |
| **R4 proxy** (7) | NHI low $65 vs $67.06, SHAK $60 vs $65.16, PLNT $49.20 vs $52.52, FOUR $40 vs $38.44 (+4%), CELH $26 vs $28.49, BBUC $28 vs $27.81, OKLO $14 vs $26.32 |
| To chains (7) | ORA, RRR, GXO, PBH, STEP, CWEN, TFPM |

## Chain stage (Dec18; every print is Nov 3 - 9, so Nov20 fails R2's 21-day cushion)

| Ticker | Stock | R1 | Print | Ratings / low | Contract | Bid / ask, OI | Verdict |
|---|---|---|---|---|---|---|---|
| ORA | $87.09 | 0.001 | Nov 4 | 7/6/0, low $98 (tool stamp 2022, untrustworthy) | Dec18 $90C / $95C | 4.10 / 4.60 OI 30; 2.25 / 3.10 OI 91 | **R7** |
| RRR | $49.61 | 0.098 | Nov 3 | 18/2/0, low $59 | Dec18 $50C / $55C | 2.25 / 3.90 OI 0; 0.40 / 1.80 OI 0 | **R7** |
| GXO | $48.43 | 0.207 | Nov 3 | 18/0/0, low $55 | Dec18 $50C / $52.5C | 1.80 / 3.10 OI 3; 0.95 / 2.10 OI 5 | **R7** |
| PBH | $47.80 | 0.182 | Nov 5 | 5/2/0, low $55 | Dec18 $50C | 0.00 / 4.90 OI 0 | **R7** |
| STEP | $42.04 | 0.082 | Nov 6 | 9/1/0, low $51 | Dec18 $45C / $50C | 1.00 / 3.90 OI 131; 0.60 / 1.25 OI 139 | **R7** (OI and spread) |
| CWEN | $31.00 | 0.185 | Nov 9 | 12/1/0, low $37 | Dec18 $30C / $35C | 2.00 / 2.30 OI 121 (spread 14%); 0.35 / 0.55 OI 1,609 (spread 44%) | **R7** (each fails one leg; no $32.5 strike) |
| TFPM | $28.87 | 0.150 | Nov 3 | 8/3/0, low $36.34 | Dec18 $30C | 0.60 / 1.50 OI 2 | **R7** |

## Jan15 re-tests (EVENING 2's R7 kills)

| Ticker | Stock | Contract | Bid / ask, OI | Verdict |
|---|---|---|---|---|
| IDXX | $560.78 | Jan15 $560C / $580C | 35.60 / 42.90 OI 34; 25.40 / 33.20 OI 12 | **R7** on Jan15 too. Dead this quarter. |
| FN | $314.99 | (no chain call) | Dec18 $320C BE $361.2 already over its $358.1 R6 line; Jan15 costs more | **R6** structural at the near strikes. Dead this quarter. |

## Watch lines (free re-check)

ONDS $6.20 (needs >= ~$6.90), BTBT $0.849 (>= ~$1.10), CLSK $7.87 (> ~$9.20): all under. OUST $29.695, still over its ~$28.25 R1 re-entry. TTWO $203.69, tool low $270 still stamped Aug 7 (stale).

## Summary

50 names moved, 0 advanced. Killed: CDE (R4, no dated floor), 25 no coverage, 8 R3, 7 R4 proxy, 7 R7 at the chain (ORA, RRR, GXO, PBH, STEP, CWEN, TFPM), IDXX (R7, Jan15), FN (R6). 2 web searches.

**Finding:** the $25-100 mid-cap band repeats the large-cap result. Names with a real Buy consensus and floor room (RRR 18/2, GXO 18/0, CWEN 12/1, STEP 9/1) carry Dec18 calls nobody trades, OI 0 to 139 near the money. This week's R7 kills split cleanly. Liquid chains belong to miners, crypto/AI names and mega-caps. A sub-$10B industrial or consumer name almost never clears R7 at this window. Saturday's sweep should push the chain-stage cut on mid-caps to the Jan15 expiry first, or skip mid-cap names whose total call volume is near zero.

## GLOSSARY
- **R1-R7:** the binder's Iron Rules (Tab 1). R1 range percentile, R2 earnings before expiry, R3 analyst consensus, R4 lowest Buy target above breakeven, R5 affordability, R6 reachability, R7 liquidity floor.
- **R4 proxy:** a free pre-chain check: if the tool's lowest target is within ~10% of the stock, no near-the-money call can have a breakeven under it.
- **R6 structural:** the stock's median earnings move is so small that the time value of a near-the-money call already exceeds 1.5x of it; no strike can pass.
- **Line (R6):** stock x (1 + 1.5 x median print move); breakeven must be at or under it.
- **BE:** breakeven = strike + ask.
- **OI / spread:** open interest; (ask - bid) / mid. R7 needs OI >= 250 and spread <= 25%.
- **Dated floor:** a Buy target within 60 days and published after the decline (binder Tab 6).
- **Paper book:** tracked-only positions, entered at the ask and exited at the bid, no money.
