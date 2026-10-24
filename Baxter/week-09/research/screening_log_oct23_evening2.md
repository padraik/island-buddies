# SCREENING LOG: Fri Oct 23, 2026, EVENING 2 (8:00pm ET)

*Market closed; quotes are the 4:00pm close. Session 2's job is docs for names past the chain stage. None were owed from EVENING 1, so this session did EVENING 3's refill per the queue: the paper large-cap scan and the sub-$25 real-money band, prints moved to **Nov 2 - Dec 18**. 68 never-screened names hit the free screen (ratings), 15 went to R1 / R2 / chains, 1 advanced (CDE, paper) and got its doc. 2 web searches (both CDE floor). No Discord messages.*

New saved scans:
- `Baxter Oct23 E2 PAPER large-cap Nov2-Dec18 prints` (`6310cc71-719c-493f-8cdb-e2d61336844c`): >$10B cap, R1 < 0.25, prints Nov 2 - Dec 18. 93 rows; 55 never in an Oct 2x log.
- `Baxter Oct23 E2 1-25 Nov2-Dec18 prints` (`0fd4f88e-17cf-48ca-a90c-60c5df40fc6e`): $0.3-10B, $1-25. 395 total, 200 rows ($9.18-25); 8 never screened.
- `Baxter Oct23 E2 1-9.18 Nov2-Dec18 prints` (`c82bcecd-9837-461e-892c-6059d32ba3f7`): 243 total, 200 rows ($2.215-9.18); 5 never screened.
- `Baxter Oct23 E2 1-2.21 Nov2-Dec18 prints` (`b83193a4-e1ad-4d1a-bd00-f7746a63e45b`): 42 rows; all 42 already screened this month.

## Held (fact check)

| Contract | Close quote | Stock | Earnings | Ratings / low vs BE | SEC since Oct 20 | Verdict |
|---|---|---|---|---|---|---|
| COUR $5C Nov20 | 0.45 / 0.60 (OI 3,257, IV 86%) | $5.085 (AH $5.08) | Thu Oct 29 PM `verified: true`, `actual: null` | 8/4/0, low $6.00 vs BE $5.65 | none | Nothing changed. Ramp sell Thu Oct 29 3:35pm. GTC $1.65 `confirmed`. |
| QUBT $7C Dec18 | 0.36 / 0.61 (OI 1,125) | $6.555 (AH $6.52) | Fri Nov 13 PM `verified: false` (LY Nov 14 PM), `actual: null` | 5/2/0, low $10 vs BE $7.54 | none | Nothing changed. Ramp sell Thu Nov 12 3:35pm. GTC $1.35 `confirmed`. |

Paper: PAAS 6/2/0 low $51 vs BE $43.90 (stock $40.125): holds. TMUS 27/4/0 low $169 vs BE $165.20 (stock $146.61, AH $146.96): holds; paper ramp sell Tue Oct 27 3:35pm.

## Free screen: R3 + R4 proxy (68 never-screened names)

**Large-cap scan (55).** Pass: IDXX, CW, FN, VST, ALB, RBA, CCJ, ULS, FNF, IREN, CDE, JBS, EQX.
Killed:
- **R3** (Sells > 1 or Buys < Holds or < 3 Buys): FICO (4 Sells), INTU (2), TPR (2), CLX (2/15/5), ZTS (5/13), PDD (2 Sells), CRWV (3), FISV (8/27/4), ENB (2), ASTS (7/8/1), NVO (1/3/2), FIG (7/10), LI (13/14/2), TU (5/12/4), SKYD (5/12/9).
- **R4 proxy** (tool low at or under ~+10% of the stock): TDG (low $1,100 vs $1,104.84), MLM ($530 vs $507), FERG ($235 vs $226.63), ORCL ($110 vs $126), AKAM ($93 vs $93.40), KKR ($97 vs $91.43), BNTX ($84.07 vs $88.42), BIDU ($69.96 vs $77.20), UBER ($70 vs $66.99), RYAAY ($53.73 vs $52.53), TCOM ($42.09 vs $39.90), CG ($41 vs $38.61), BN ($31 vs $37.97), FIS ($37 vs $37.50), MDLN ($34 vs $34.08), ONON ($19.97 vs $32.46), CPRT ($25 vs $29.04), AS ($31 vs $28.24, +9.8%), JD ($25.03 vs $25.42), DKNG ($20 vs $20.84), BCE ($22.42 vs $20.45, +9.6%), ZTO ($21.68 vs $19.85, +9.2%), CPNG ($12 vs $13.91), KEP ($9.57 vs $10.62), TME ($9.07 vs $8.40, +7.9%; has an Oct 6 doc).
- **No coverage:** UI, BMNR.

**Sub-$25 scans (13 new; the $1-2.21 band had none).** Pass: AG, SVRA.
- R4 proxy: BETR (low $15 vs $17.38), ARCT ($9 vs $10.03). R3: NAVI (1/4/3). No coverage: OGC, SA, GOGL, NVRI, FSM, MTA, LSAK, GALT.

## R1 (split-adjusted), R2, R6, R7 on the 15 survivors

R1 from 52 weekly bars (`get_equity_historicals`, split-adjusted): no fake readings; all 15 under 0.25. R2: every print below is `verified: true` except SVRA, and every one is Oct 30 - Nov 12, so **Dec18** is the first expiry clearing the 21-day cushion. R6 median from the last 5-6 prints (absolute reaction close-to-close).

| Name | Stock | R1 | Print | R6 median / line | Contract checked | Quote / OI | BE | Verdict |
|---|---|---|---|---|---|---|---|---|
| IDXX | $560.07 | 0.221 | Nov 2 AM v | 6.77% / $617.0 | Dec18 $560C | 31.80 / 39.00, OI 12 | $599 | **R7** |
| CW | $465.30 | -0.078 | Nov 4 PM v | 4.50% / $496.7 | Dec18 $470C | 25.00 / 31.80, OI 3 | $501.8 | **R7** (R6 too) |
| FN | $315.01 | -0.123 | Nov 2 PM v | 9.12% / $358.1 | Dec18 $320C | 31.20 / 41.20, OI 35, spread 28% | $361.2 | **R7** (R6 too) |
| VST | $140.30 | 0.105 | Nov 6 AM v | 2.44% / $145.4 | not pulled | n/a | ATM time value alone > $5 | **R6 structural** |
| ALB | $93.89 | 0.044 | Nov 4 PM v | 2.25% / $97.05 | not pulled | n/a | same | **R6 structural** |
| CCJ | $78.60 | 0.016 | **Oct 30 AM v** (scanner said Nov 5) | 2.55% / $81.6 | not pulled | n/a | same | **R6 structural**; tool ratings stamped 2021, R4 unusable anyway |
| RBA | $84.19 | 0.149 | Nov 9 AM v | 2.87% / $87.8 | Dec18 $85C | 3.50 / 6.10, OI 42 | $91.1 | **R7 + R6** |
| ULS | $73.44 | 0.231 | Nov 3 AM v | 13.12% / $87.9 | Dec18 $75C | 2.40 / 4.80, OI 1 | $79.8 | **R7** |
| FNF | $40.44 | 0.114 | Nov 5 PM v | 3.33% / $42.46 | Dec18 $40C | 1.95 / 3.80, OI 180, spread 64% | $43.8 | **R7 + R6** |
| IREN | $24.90 | -0.033 | Nov 5 PM v | 7.25% / $27.61 | Dec18 $25C | 4.10 / 4.20, OI 2,699 | $29.20 (+17.3%) | **R6** |
| JBS | $12.43 | 0.226 | Nov 9 PM v | 3.80% / $13.14 | Dec18 $12.5C / $15C | 0.75 / 0.90 OI 3; 0.05 / 0.15 OI 41 | $13.40 | **R7** (R6 too) |
| EQX | $10.12 | 0.156 | Nov 9 PM v | 7.99% / $11.33 | Dec18 $10C / $11C / $12.5C | OI 60; 0.30 / 0.60 OI 140; 0.20 / 0.25 OI 453 | $11.10 / $11.60 / $12.75 | **R7** on $10C/$11C; **R6** on $12.5C (+26%) |
| AG | $14.81 | 0.210 | Nov 5 AM v | 5.39% / $16.01 | Dec18 $14C / $15C / $16C | 1.49 / 2.20 OI 91; 1.14 / 1.34 OI 15,110; 0.80 / 0.91 OI 619 | $16.20 / $16.34 / $16.91 | **R6** (nearest liquid strike needs +10.3%) / R7 on $14C |
| SVRA | $4.26 | 0.216 | Nov 11 AM unv (LY Nov 12) | 3.04% / $4.45 | Dec18 $4C / $5C | 0.45 / 1.40 OI 22; 0.60 / 0.85 OI 432 | $5.40 / $5.85 | **R6** |
| **CDE** | **$13.46** | **-0.006** | **Nov 4 PM v** (LY Oct 29) | **8.36% / $15.15** | Dec18 $12.5C / $15C; **Jan15 $12.5C** / $15C | 1.70 / 2.00 OI 156; 0.65 / 0.85 OI 5,137; **2.00 / 2.25 OI 4,597, spread 11.8%**; 0.95 / 1.05 OI 8,991 | Dec18 $14.50 / $15.85; **Jan15 $14.75 (+9.58%)** / $16.05 | **ADVANCED (paper)**, Jan15 $12.5C passes R6 and R7; R4 gated on a dated floor |

Real-money read: nothing tonight has a contract under the **$0.622** line that clears R6 and R7. The two closest were EQX $11C (ask $0.60, BE $11.60 vs line $11.33, spread 67%, OI 140) and JBS $12.5C (ask $0.90, OI 3).

## CDE (paper): doc written, entry gated

`research_CDE_paper.md`. R1 -0.006 (52-week low), R2 Nov 4 PM verified, R3 10/3/0, R4 tool low $18 vs BE $14.75 **undated**, R6 passes by $0.40, R7 OI 4,597 / 11.8%. Two searches: Scotiabank Outperform $28.50 -> $26.50, Cantor Buy -> Hold ($16), Cormark Buy -> Market Perform ($21), all undated. No dated post-slide Buy, so Tab 6 isn't met. Five-Baxter vote 3-2 to hold on the gate (Bearxter and Macxter against entering at all: two named downgrades; second precious-metals name after PAAS). Would-be ramp sell Wed Nov 4 3:35pm.

## Parked / watch (free re-check)

| Name | Close | Line | Status |
|---|---|---|---|
| ONDS | $6.20 | >= ~$6.90 | under |
| BTBT | $0.849 | >= ~$1.10 | under |
| CLSK | $7.87 | > ~$9.20 | under |
| OUST | $29.695 (+6.1% again) | <= ~$28.25 | over; still R1-out |
| TTWO | $203.69 | stamp | 29/1/1, low $270, tool stamp still Aug 7. Parked. |

## Tally

68 names at the free screen, 15 to the chain stage, 14 killed there (R7: IDXX, CW, FN, ULS, JBS, RBA, FNF; R6: VST, ALB, CCJ, IREN, EQX, AG, SVRA), 1 advanced (CDE, paper, doc written, gated). 53 killed at the free screen (large-cap: R3 15, R4 proxy 25, no coverage 2; sub-$25: R4 proxy 2, R3 1, no coverage 8). 2 web searches.

**Finding:** prints in the Nov 2 - 9 cluster push nearly everything to Dec18, and Dec18 OI on mid- and large-cap non-tech names (IDXX, CW, ULS, RBA) is single or double digits. The liquid Dec18 chains tonight were all metals and miners (AG, CDE, EQX) and IREN. Saturday's sweep should check Jan15 first on any name whose Dec18 is thin, and not spend a chain call on names with print medians under ~3% (VST, ALB, CCJ): at-the-money time value alone exceeds their R6 line.

## GLOSSARY
- **R1-R7:** the binder's Iron Rules (Tab 1). R1 range percentile, R2 earnings before expiry, R3 analyst consensus, R4 lowest Buy target above breakeven, R5 affordability, R6 reachability, R7 liquidity floor.
- **R4 proxy:** a free pre-chain check: if the tool's lowest target is within ~10% of the stock, no near-the-money call can have a breakeven under it.
- **R6 structural:** the stock's median earnings move is so small that the time value of an at-the-money call already exceeds 1.5x of it; no strike can pass.
- **Line (R6):** stock x (1 + 1.5 x median print move); breakeven must be at or under it.
- **v / unv:** `get_earnings_results` verified flag (company-announced vs estimated).
- **BE:** breakeven = strike + ask.
- **OI / spread:** open interest; (ask - bid) / mid. R7 needs OI >= 250 and spread <= 25%.
- **Split-adjusted R1:** range percentile from adjusted bars; the scanner's own range uses unadjusted weekly candles (APH, Oct 22).
- **Dated floor:** a Buy target within 60 days and published after the decline (binder Tab 6).
- **Paper book:** tracked-only positions, entered at the ask and exited at the bid, no money.
