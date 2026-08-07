# Screening Log -- Aug 7, 2026, Round 2 (Bearxter's lane)

Second parallel round of the day, four agents again (Bullxter/Macxter/Calxter/Bearxter), fresh ~148-name remainder toward the 500 target. This lane: life insurance/reinsurance, aerospace parts/MRO (distinct from defense primes), diagnostics/lab services (distinct from hospitals/medical devices), payment processors/fintech infrastructure (distinct from banks), semiconductor capital equipment (distinct from fabless semis), forest/paper products. Round 1 today already covered industrials/machinery, healthcare services/managed care, specialty insurance, staffing, packaging, building products (this agent) -- avoided re-screening IP, PKG, SON, GPK, DGX, LH from that batch. Reserve $1,054.96, one open position (KR, do not touch).

## Stage 1 -- Range percentile (free, fetch_price.py --range)

40 attempted (hard cap reached exactly), 3 unavailable via broker API (SPR -- Spirit AeroSystems, delisted/absorbed into the Boeing acquisition that closed 2026; EXAS -- Exact Sciences, rejected as bad symbol, possible ticker change; FI -- Fiserv, rejected, likely a symbol mismatch on this feed). 37 valid.

| Ticker | Price | 52wk Range | Pctile | Direction |
|---|---|---|---|---|
| MET | $97.93 | 67.33-100.93 | 91st | PUTS (logged only) |
| PRU | $121.23 | 91.89-127.72 | 82nd | PUTS (logged only) |
| AFL | $123.87 | 101.49-130.22 | 78th | PUTS (logged only) |
| LNC | $46.46 | 32.18-47.66 | 92nd | PUTS (logged only) |
| UNM | $89.08 | 68.28-93.22 | 83rd | PUTS (logged only) |
| GL | $183.88 | 127.84-191.55 | 88th | PUTS (logged only) |
| CNO | $55.05 | 35.81-57.59 | 88th | PUTS (logged only) |
| PRI | $322.87 | 230.09-327.28 | 95th | PUTS (logged only) |
| RGA | $242.43 | 178.21-246.03 | 95th | PUTS (logged only) |
| VOYA | $100.99 | 64.50-103.85 | 93rd | PUTS (logged only) |
| HEI | $361.69 | 256.11-376.86 | 87th | PUTS (logged only) |
| HXL | $101.03 | 59.79-111.73 | 79th | PUTS (logged only) |
| WWD | $361.55 | 233.31-450.92 | 59th | MID-OUT |
| CW | $688.62 | 464.91-808.16 | 65th | MID-OUT |
| AIR | $143.57 | 71.57-154.00 | 87th | PUTS (logged only) |
| DCO | $196.43 | 84.76-210.39 | 89th | PUTS (logged only) |
| NEOG | $11.36 | 4.78-12.85 | 82nd | PUTS (logged only) |
| QGEN | $42.27 | 32.53-57.81 | 39th | MID-OUT |
| NTRA | $315.19 | 136.21-321.82 | 96th | PUTS (logged only) |
| **MYGN** | **$3.20** | **2.74-8.59** | **8th** | **CALLS -- advances to chain** |
| CRL | $265.66 | 144.26-268.00 | 98th | PUTS (logged only) |
| IQV | $235.28 | 154.50-251.36 | 83rd | PUTS (logged only) |
| PYPL | $59.95 | 38.46-79.22 | 53rd | MID-OUT |
| **FIS** | **$42.84** | **37.42-72.91** | **15th** | **CALLS -- advances to chain** |
| GPN | $87.99 | 61.16-90.85 | 90th | PUTS (logged only) |
| **ACI** | **$12.15** | **10.86-20.02** | **14th** | **CALLS -- advances to chain (see note)** |
| JKHY | $156.99 | 121.04-193.39 | 50th | MID-OUT |
| EEFT | $72.13 | 62.50-98.52 | 27th | MID-OUT |
| AFRM | $78.17 | 42.09-100.00 | 62nd | MID-OUT |
| AMAT | $529.52 | 154.47-739.67 | 64th | MID-OUT |
| LRCX | $304.69 | 94.11-438.50 | 61st | MID-OUT |
| KLAC | $195.47 | 83.22-307.37 | 50th | MID-OUT |
| TER | $373.75 | 104.58-487.91 | 70th | MID-OUT |
| ENTG | $144.46 | 67.97-186.94 | 64th | MID-OUT |
| ONTO | $301.32 | 91.61-386.46 | 71st | MID-OUT |
| WY | $25.84 | 21.16-27.75 | 71st | MID-OUT |
| RYN | $21.78 | 19.49-27.34 | 29th | MID-OUT |

**Tally: 15 MID-OUT (WWD, CW, QGEN, PYPL, JKHY, EEFT, AFRM, AMAT, LRCX, KLAC, TER, ENTG, ONTO, WY, RYN), 19 PUTS-zone (logged, untouched, per no-dedicated-puts-pools rule), 3 CALLS-zone advance to chain: MYGN, FIS, ACI.**

**Note on ACI:** intended target was ACI Worldwide (payment processor, ticker ACIW), but "ACI" on this broker feed resolves to Albertsons Companies (grocery retail) -- confirmed by web search: ACIW trades ~$56, range $38.05-$54.28, nothing like the $12.15/10.86-20.02 pulled here. Caught before any DD time was spent on the wrong thesis. Also worth flagging even setting the ticker mix-up aside: Albertsons is grocery retail, same macro bucket as KR (Kroger), the fund's one open position -- would need a correlated-position-cap check if it had otherwise survived. It didn't, so the check is moot here, noted for whoever screens ACIW properly in a later batch.

**Sector note:** life insurance/reinsurance and aerospace MRO both ran almost entirely into 52-week highs or MID-OUT -- zero CALLS-zone survivors from either of the two full sub-sectors (17 names combined). Semiconductor capital equipment similarly produced zero CALLS-zone names, all MID-OUT in the 50th-71st percentile band -- a sector mid-cycle, not dislocated. Forest/paper (WY, RYN) both MID-OUT.

## Stage 2 -- Chain feasibility (free, fetch_puts_chain.py --calls)

All three CALLS-zone survivors looked workable on cheap-strike geometry (MYGN Aug21 $4C at $0.15, 29.7% needed; FIS Aug14 $44C at $0.65, 4.2% needed; ACI Aug14 $12C at $0.75, 0.7% needed -- ACI's number is startling only because it's an unintended ticker, see above). All three died the same way once earnings dates were checked -- the same post-earnings trough this entire sweep keeps hitting on Aug 7:

- **MYGN: KILLED on calendar (Rule 2).** Reported Q2 2026 on Jul 30, 2026 -- a real miss (EPS -$0.25 vs -$0.06 est., revenue $190.7M vs $210.1M est., guidance cut on payer friction), 8 days before this screen. The 8th-percentile read is the post-earnings crater, not a pre-earnings dislocation -- also worth flagging as likely Category 2 (guidance cut = real deterioration signal, not overreaction) had the calendar not already killed it. Next confirmed print: **Nov 2, 2026** -- past every listed expiry (chain topped out at Oct 16, 70 DTE). No instrument brackets the real catalyst.
- **FIS: KILLED on calendar (Rule 2).** Reported Q2 2026 on Aug 4, 2026 -- a beat (EPS $1.48 vs $1.47 est.) -- 3 days before this screen; the 15th-percentile read reflects a stock that's been sliding from a $72.91 high over the year, not a fresh pre-earnings setup. Q3 2026 guidance was issued same day (EPS $1.58-1.62), but no specific Q3 report date is published yet; last year's cadence (Q3 2025 guidance updated ~Aug 5, 2025) points to an early-November report, consistent with MYGN's confirmed Nov 2 date this same batch. That's past every listed expiry (Oct 16 max, 70 DTE). No instrument brackets the real catalyst.
- **ACI (Albertsons, unintended ticker): KILLED on calendar (Rule 2).** Reported earnings Aug 6, 2026 -- the day before this screen. Same trough pattern as the other two. Not pursued further given the ticker mix-up already disqualifies it as a payments-sector candidate regardless.

**Pattern note, fourth confirmation today:** every CALLS-zone survivor across both of this agent's Aug 7 lanes (round 1: GPK, BLDR, JELD, LII; round 2: MYGN, FIS, ACI) died on the identical root cause -- Aug 7 sits in the trough right after a wave of Q2 prints, so cheap-looking dislocations found this week are almost all post-earnings reactions with the real next catalyst sitting past the available near-dated chain. Seven for seven, zero exceptions, across ten distinct sub-sectors now screened by this agent alone today.

## Stage 3 -- Full DD

None reached DD. All three CALLS-zone survivors died in Stage 2 on calendar/Rule 2. No search budget spent on Rule 3/Rule 4/decline-category beyond what was needed to confirm the calendar kill.

## Batch tally

**40 attempted (hard cap), 3 unavailable (bad/delisted symbol), 37 valid, 3 CALLS-zone advances, 0 reached full DD, 0 survivors at 3.5+, 0 at 4/5.**

19 PUTS-zone names logged, untouched, per the no-dedicated-puts-pools rule: MET (91st), PRU (82nd), AFL (78th), LNC (92nd), UNM (83rd), GL (88th), CNO (88th), PRI (95th), RGA (95th), VOYA (93rd), HEI (87th), HXL (79th), AIR (87th), DCO (89th), NEOG (82nd), NTRA (96th), CRL (98th), IQV (83rd), GPN (90th). Two worth flagging in passing: CRL (Charles River Labs) at 98th percentile and NTRA (Natera) at 96th, both deep into fresh-high territory -- stalled-at-the-top shape if the puts back-test ever unblocks live entries.

No survivors, no research docs written this batch. Confirms Bullxter/Macxter/Calxter's likely finding independently: Aug 7 is a structurally weak day to screen for calls no matter which sector gets picked, because the whole market just finished reporting.
