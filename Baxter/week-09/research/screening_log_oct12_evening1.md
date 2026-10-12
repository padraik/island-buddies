# Screening log: Mon Oct 12, 2026, 6:00pm ET EVENING 1 (VM, LIVE, no order tools)

**Session job:** DO, up to 25 names through the funnel (EVENING 1). Plan from LASTCALL/WRAP: the **$50+ bands** (not yet covered this week), prefer names with a listed Dec expiry. Quotes are Monday's closing prints (~19:59 UTC). Reserve (spendable) $676.28: Rule 5 3.5/5 line $0.676, so every name in these bands is **paper-only** (R5 not applied in the paper book). Ratings via `get_equity_analyst_ratings`; R6 from `get_equity_historicals` daily closes around each tool-dated print (pm print: print-day close -> next close; am print: prior close -> print-day close). No web searches, no WebFetch.

Scanner (preview, not saved): market cap >= $300M, `FILTER_TYPE_EARNINGS_DATE` **20261028-20261211**, 52w range pct expression < 0.25, split by `FILTER_TYPE_LAST`: **$50-100: 103 names** (54 already in this week's week-09 files, 49 new); **>$100: 93 names** (58 seen, 2 share-class/illiquid skipped (BIO.B, FORTY), 33 new). **82 new names moved; 0 advance.**

## Band 1: $50-100 (49 new)

**No coverage (11), KILLED R3:** NFG, WLDN, MGEE, AGO, TNC, PIPR, DBD, GRBK, MMS, PHIN, LMB.

**R3 fails (13):**

| Name | B/H/S | Result |
|---|---|---|
| INGR | 3/7/0 | KILLED, R3 (Buys < Holds) |
| LULU | 4/27/6 | KILLED, R3 |
| DCI | 2/7/1 | KILLED, R3 |
| GOLF | 1/8/0 | KILLED, R3 |
| UFPI | 3/4/0 | KILLED, R3 |
| PEG | 10/14/0 | KILLED, R3 |
| THO | 5/10/1 | KILLED, R3 |
| BC | 10/11/0 | KILLED, R3 |
| WLK | 9/11/1 | KILLED, R3 |
| MTH | 5/7/1 | KILLED, R3 |
| MC | 4/6/1 | KILLED, R3 |
| AOS | 6/8/2 | KILLED, R3 |
| CSR | 3/6/0 | KILLED, R3 |

**R4-proxy kills (8):** tool low target at/under the price, or within ~3% of it (no call breakeven can clear it).

| Name | Stock | B/H/S, low | Result |
|---|---|---|---|
| LMAT | $82.91 | 4/4/0, $81 | KILLED, R4 (low < price) |
| SR | $79.56 | 7/4/0, $79 | KILLED, R4 |
| MRCY | $78.00 | 10/2/1, $78 | KILLED, R4 |
| BFAM | $69.90 | 6/4/1, $66 | KILLED, R4 |
| CRSP | $51.54 | 13/9/0, $44 | KILLED, R4 |
| PRIM | $82.79 | 11/5/0, $85 | KILLED, R4 (+2.7%) |
| POST | $76.83 | 7/2/0, $79 (stamp 2023) | KILLED, R4 (+2.8%, stale) |
| IPGP | $76.05 | 8/3/1, $78 | KILLED, R4 (+2.6%) |

**R3 survivors to earnings + chain (17):**

| Name | Stock | B/H/S, low | Earnings (tool) / LY | Expiry needed (R2) | Contract checked | Quote / OI | Result |
|---|---|---|---|---|---|---|---|
| BGSI | $78.18 | 14/1/0, $120 | Nov 11 AM v / Nov 12 | Dec 3+ | none | no listed options | **KILLED, no options** |
| CHDN | $80.50 | 13/0/0, $117 | Oct 28 PM **v** / Oct 22 | Nov 18+ -> Nov20 | Nov20 $80C / $85C | 3.90/5.10 OI 5; 2.05/3.90 OI 48 (spread 62%) | **KILLED, R7** |
| WGS | $63.82 | 8/0/0, $83 | Oct 27 AM (f) / Oct 28 | Nov 18+ -> Nov20 | Nov20 $65C / $67.5C / $70C | OI 0 / 2 / 1, spreads 34-41% | **KILLED, R7** |
| RKLB | $65.60 | 21/4/0, $75 | Nov 9 PM (f) / Nov 10 | Dec 1+ -> Dec18 | Dec18 **$65C** / $70C | **8.00/8.30 OI 2,570 (3.7%)**; 5.95/6.20 OI 5,523 | **KILLED, R6.** Median of last 6 print moves **3.08%** (-11.2, +1.1, -1.3, -4.9, +34.2, -0.0) -> cap 4.62%, max BE $68.63. $65C BE at ask $73.30 needs +11.7%. ($70C also fails R4: BE $76.20 > low $75.) |
| EMN | $62.10 | 10/10/0, $73 | Oct 29 PM v / Nov 3 | Nov 24+ -> Dec18 | Dec18 $65C / $60C | 1.90/3.00 OI 100 (45%); 4.80/5.60 OI 64 | **KILLED, R7** |
| ACM | $59.01 | 12/3/0, $65 | Nov 16 PM (f) / Nov 18 | Dec 9+ -> Dec18 | Dec18 $60C | 2.15/4.60 OI 121 (73%) | **KILLED, R7** |
| ROAD | $86.18 | 4/2/0, $115 | Nov 19 AM (f) / Nov 20 | Dec 11+ -> Dec18 | Dec18 $90C | 6.20/6.50 OI **0** | **KILLED, R7** |
| AAON | $84.77 | 8/1/0, $110 | Nov 5 AM (f) / Nov 6 | Nov 27+ -> Dec18 | Dec18 $90C | 6.40/8.70 OI 28 | **KILLED, R7** |
| ANIP | $73.59 | 7/2/0, $85 | Nov 6 AM (f) / Nov 7 | Nov 28+ -> Dec18 | Dec18 $75C | 2.15/6.50 OI 1 | **KILLED, R7** |
| ESAB | $66.40 | 12/1/0, $95 | Nov 4 AM v / Oct 29 | Nov 25+ -> Dec18 | Dec18 $70C | 3.20/5.90 OI 4 | **KILLED, R7** |
| CELC | $66.05 | 12/0/0, $130 | Nov 11 PM (f) / Nov 12 | Dec 3+ -> Dec18 | Dec18 $70C | 4.30/8.30 OI 115 (63%) | **KILLED, R7** |
| LCII | $79.00 | 7/6/0, $105 | Nov 5 AM (f) / Oct 30 | Nov 26+, no Dec -> Jan15 | Jan15 $80C | 3.70/6.30 OI 2 | **KILLED, R7** |
| OGS | $73.61 | 7/4/0, $79 | Nov 2 PM v / Nov 3 | Nov 24+, no Dec -> Jan15 | Jan15 $75C | 1.70/3.90 OI 14 | **KILLED, R7** |
| CYTK | $62.79 | 21/2/0, $85 | Nov 4 PM v / Nov 5 | Nov 26+, no Dec -> Jan15 | Jan15 **$65C** / $60C | **5.70/6.80 OI 1,253 (17.6%)**; 8.10/10.60 OI 640 (26.7%) | **KILLED, R6.** Median of last 6 print moves **3.08%** (-2.7, -3.2, +1.9, -10.3, -2.9, -5.7) -> cap 4.61%, max BE $65.68. $65C BE at ask $71.80 needs +14.3%. |
| CIGI | $86.40 | 9/4/0, $110 | Nov 4 AM v / Nov 4 | Nov 25+, no Dec/Jan -> Feb19 | Feb19 $90C | 2.95/7.00 OI 4 | **KILLED, R7** |
| STN | $66.79 | 12/1/0, $79.42 | Nov 12 PM (f) / Nov 13 | Dec 4+, no Dec/Jan -> Feb19 | Feb19 $70C | 0.10/10.10 OI 102 | **KILLED, R7** |
| DOO | $52.40 | 11/10/0, $60.45 | Dec 3 AM (f) / Dec 4 | Dec 25+ -> Feb19 | Feb19 $55C | 3.20/5.90 OI 2 | **KILLED, R7** |

## Band 2: >$100 (33 new)

**No coverage (7), KILLED R3:** UI, KAI, ALG, HWKN, GVA, USLM, HOV.

**R3 fails (7):** IBP 2/12/1, GPOR 7/8/1, EXP 0/12/1, PJT 2/4/1, RH 7/12/2, OC 11/7/2, AGCO 8/9/2. All KILLED, R3.

**R4-proxy kills (5):** AZO ($2,898.85, low $3,000, +3.5%), PODD ($139.81, low $143, +2.3%), ORCL ($137.40, low $110), TOL ($132.15, low $118), WING ($126.02, low $120). All KILLED, R4.

**R3 survivors taken to R6 + chain (7, the likeliest big movers):**

| Name | Stock | B/H/S, low | Earnings / LY | Expiry | Last 6 print moves (%) -> median, cap, max BE | Contracts checked (bid/ask, OI) | Result |
|---|---|---|---|---|---|---|---|
| **FN** | $456.50 | 10/2/0, $598 | Nov 2 PM (f) / Nov 3 | Dec18 | -7.3, -12.8, +3.8, -10.2, -8.0, -19.4 -> 9.12%, 13.67%, $518.92 | $450C 50.30/58.20 OI 22; **$460C 46.50/53.30 OI 67** (BE $513.30, passes R6 by $5.62); $500C 30.90/39.10 OI 36 | **KILLED, R7** (max OI 67). R1-R6 pass on the $460C. |
| **AVAV** | $131.98 | 20/5/0, $165 | Dec 8 PM (f) / Dec 9 | Jan15 | +21.6, +7.0, -12.9, -6.3, +18.8, +4.5 -> 9.90%, 14.85%, $151.58 | $130C 13.60/21.50 OI 15; **$135C 15.20/15.80 OI 91** (BE $150.80, passes R6 by $0.78); $140C 12.00/17.40 OI 98 | **KILLED, R7** (max OI 98). |
| **LEU** | $135.67 | 10/7/0, $167 | Nov 4 PM (f) / Nov 5 | Dec18 | +22.0, +8.7, -14.7, -20.7, +12.3, -5.1 -> 13.50%, 20.24%, $163.13 | $135C 16.60/19.10 OI 12; **$140C 14.40/16.90 OI 136** (BE $156.90); $150C 10.80/13.30 OI 28 (BE $163.30, fails R6 by $0.17) | **KILLED, R7** (max OI 136). |
| **DY** | $266.99 | 12/0/0, $375 | Nov 18 AM (f) / Nov 19 | Dec18 (10-Q Dec 10, 6 trading days before) | +15.8, -4.6, +9.8, -4.1, +25.8, -11.6 -> 10.72%, 16.08%, $309.92 | $260C OI 1; $270C 23.40/28.70 OI 10; $280C 19.20/24.80 OI 13 | **KILLED, R7** (max OI 13). |
| BOOT | $119.97 | 16/1/0, $160 | Oct 28 PM (f) / Oct 29 | Nov20 | +16.7, -0.6, -4.5, +2.9, -1.7, +2.3 -> 2.59%, 3.89%, $124.64 | Nov20 $120C 8.50/9.80 OI 8 | **KILLED, R6** (BE $129.80) and R7. |
| IRTC | $106.68 | 16/0/0, $150 | Nov 5 PM v / Oct 30 | Dec18 | +20.8, +17.7, +1.7, -5.0, -6.5, -0.2 -> 5.72%, 8.59%, $115.84 | Dec18 $110C 5.50/9.70 OI 1 | **KILLED, R6** (BE $119.70) and R7. |
| CRUS | $106.33 | 5/2/0, $130 | Nov 3 PM (f) / Nov 4 | Dec18 | -2.1, -7.4, -7.9, +8.3, +2.4, -4.6 -> 5.96%, 8.94%, $115.84 | Dec18 $110C 4.40/8.30 OI 33 | **KILLED, R6** (BE $118.30) and R7. |

**R3 survivors not yet chain-checked (queued, 7):** OSIS ($195.32, 7/1/0, low $250), SPXC ($168.45, 14/2/0, $215), NXST ($160.55, 9/1/0, $215), HLI ($130.38, 6/5/0, $147), WMS ($125.93, 13/0/0, $145), JBTM ($107.10, 9/0/1, $118, stamp 2023), MZTI ($101.22, 3/3/0, $118).

## Totals

82 new names moved: 18 no coverage, 20 R3, 13 R4 proxy, 1 no options, 18 R7, 5 R6, 7 queued at R3-passed. 0 advances, 0 paper entries.

**What the session says:** above $50, Rule 7 is the wall, not Rules 3-6. Of the 24 names that reached the chain stage, 18 had no strike within reach with OI >= 250, and four of those (FN, AVAV, LEU, DY) passed Rules 1-6 cleanly. The only two contracts with real liquidity (RKLB, CYTK) belong to stocks whose earnings prints barely move them (both medians 3.08%). The paper book's large-cap candidates sit in the $100-300 megacap band, where options are deep; the mid-cap $50-150 band is mostly a liquidity desert in December.

**Real-money entry:** none possible from these bands (every contract is 10-80x the $0.676 line). No order tools this run.

## GLOSSARY

- **Range pct (Rule 1):** where the price sits in its 52-week range, 0 = at the low, 1 = at the high. Bottom quarter (< 0.25) is the calls pool.
- **R2 expiry needed:** the option must expire at least 21 days after the later of the tool's earnings date and last year's same-quarter date; the 10-Q deadline must fall at least 5 trading days before expiry.
- **(f) / v:** the tool's earnings date is estimated (`verified: false`) or company-announced (`verified: true`).
- **R3:** at most 1 Sell, at least 3 Buys, Buys at least equal to Holds.
- **R4 proxy:** the tool's lowest target of any rating; if it's under or barely over the price, no call breakeven can clear it.
- **R6 cap:** 1.5 x the median absolute earnings-day move over the last 6 prints. Max BE = stock x (1 + cap).
- **R7:** open interest >= 250 and bid/ask spread <= 25% of mid on the exact contract.
- **BE at ask:** strike + ask, the price the stock has to reach at expiry for the call to break even.
- **OI:** open interest, the number of contracts outstanding. Low OI means a thin market and a wide spread going in and out.
