# Screening log, Wed Oct 21, EVENING 1 (6:00pm ET): RESEARCHED

*Market closed; quotes are the 4:00pm close (after-hours stock prints noted). Free tools for everything except 3 searches (NRG floor, GLXY floor x2). Two new saved scans: `Baxter Oct21 E1 25-100 Oct28-Nov27 prints` (`1ddba801-0e53-4177-b260-97d0abfc804a`, 211 rows) and `Baxter Oct21 E1 2-100 Nov28-Jan15 prints` (`8335ad1d-cd82-4a09-bb9a-467a46a4cd94`, 70 rows). Also re-ran `Baxter Oct13 10-25 Dec12-Jan31 prints` (9 rows) and `Baxter Oct16 E2 sub-$25 Oct30-Dec4 prints` (160 rows).*

## Held

| Check | COUR $5C Nov20 | QUBT $7C Dec18 |
|---|---|---|
| Quote (close) | 0.40 / 0.55 (mark 0.475, OI 3,234) | 0.60 / 0.89 (mark 0.745, OI 1,117) |
| Stock | $4.975 close, AH $5.03 | $6.83 close, AH $6.84 |
| Earnings | Thu Oct 29 PM, `verified: true`, `actual: null` | Fri Nov 13 PM, `verified: false`, `actual: null` (LY Nov 14 PM) |
| Rule 4 | 8/4/0, low **$6.00** vs BE $5.65: holds | 5/2/0, tool low **$10** vs BE $7.54: holds |
| SEC since Oct 15 | none | none |
| GTC | `6ac7d537` 1 @ $1.65, `gtc`, `confirmed` | `6ad8ced0` 1 @ $1.35, `gtc`, `confirmed` |

Tab 4 checks 0 through f: none fire on either.

## Queue names

| # | Name | Dir | Stock (close) | R1 | R3 (B/H/S, low) | R2 | Contract | OI | Quote | Needed move vs R6 cap | Result |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **NRG** Dec18 | CALLS | $99.80 (AH $100.50) | 0.05-0.07 (52w $93.36-$189.96) | 16/4/0, $131 (stamp Oct 3) | Thu Nov 5 AM unverified, LY Nov 6 AM; Dec18 is 42 days past Nov 6; 10-Q deadline Mon Nov 9 | $95C `afb0b611` / **$100C `db21ddf5`** / **$105C `6fa30201`** / $110C `698f4080` | 27 / 306 / 511 / 1,335 | 10.70/11.60; 8.10/9.90 (20.0% of mid); 6.20/7.10 (13.5%); 4.70/5.20 | Six AM prints (same-day close vs prior close): +26.21, -13.61, -1.78, +4.25, -4.31, -15.48; **median 8.96%, cap 13.44%** (BE line $113.21). $100C BE $109.90 = **+10.1%**, $105C BE $112.10 = **+12.3%** pass; $110C +15.4% fails; $95C R7 | **ADVANCE to paper doc** (EVENING 2). Floor gate cleared: one search found **Siebert Williams Shank initiating at Buy, $184** (MarketBeat Oct 19 article, "4 days ago", so ~Oct 15, after the slide). Morgan Stanley's $165 is Equal Weight, not a Buy. Whoever owns the tool's $131 low, every reading is far over BE $112.10. Confirm the Siebert date in the doc. Paper-size ($665+ per contract vs the $62 line) |
| 2 | NG Mar19 2027 | CALLS | $6.51 | 0.15 | 6/0/0, $12.02 | Thu Jan 21 2027 AM unverified, LY Jan 22; no Feb expiry listed, so Mar19 (Jan 22 + 21 = Feb 12) | $5C `a07ce4bc` / $6C `78cc27dc` / $7C `b6211278` | 375 / 2,404 / 2,004 | 1.65/2.20; 1.30/1.45; 0.90/1.00 | Six AM prints: -5.13, +15.00, +5.01, +4.23, -14.13, -1.26; **median 5.07%, cap 7.60%** (BE line $7.005). $5C BE $7.20 (+10.6%), $6C $7.45 (+14.4%), $7C $8.00 (+22.9%) | **KILL R6** (structural: no strike gets inside 7.6%) |
| 3 | GLXY Nov20 $16.5C (paper-size) | CALLS | $16.94 (+7.5%) | ~0.04 | 15/1/0, $24 | Tue Oct 27 AM verified | `ce4f3f69` | 924 | 1.91 / 2.27 (17.2%) | line = 16.94 x 1.1214 - 16.50 = $2.50; ask 2.27 passes | **KILL R4 (Tab 6 dating)**. Two searches: the newest Buys found are BTIG $45 and Rosenblatt $35, both **Aug 5 2026** (77 days, past the 60-day limit); the $24 low is Goldman (Feb, likely Neutral). No dated Buy exists and the paper window closes Fri Oct 23 with no evening search left that would change it |
| 4 | APH Nov20 $80C (paper-size) | CALLS | $79.19 (AH $79.50) | -- | 22/2/0, $90 (stamp Oct 3) | unchanged | `d254aa6a` | 5,771 | 3.90 / 4.40 (12.0%) | line = 79.19 x 1.0607 - 80 = **$4.00**; ask 4.40 **fails by $0.40** (at the $79.50 AH print the line is $4.33, still fails) | **PARKED, fails R6 at the close.** Paper doc only if a live quote passes; kill Fri Oct 23 |
| 5 | TTWO | CALLS | $206.18 | ~0.22 | 29/1/1, $270 (stamp **Aug 7**, 75 days) | -- | -- | -- | -- | -- | **HOLD**, floor past 60 days |
| 6-8 | ONDS / BTBT / CLSK (watch) | CALLS | $6.26 / $0.944 / $8.77 | -- | 11/0/0 $13 / 6/0/0 $3.50 / 15/0/0 $19 | -- | -- | -- | -- | need ~$6.90 / ~$1.10 / > ~$9.20 | no change |

## Refill scans

**Scan A, $25-100, prints Oct 28 - Nov 27 (211 rows, 200 returned).** 195 of the 200 already appear in week-09 logs. The five new ones:

| Name | Stock | R3 | Print | Result |
|---|---|---|---|---|
| IBOC | $66.02 | no coverage | -- | **KILL R3** |
| LGIH | $40.01 | no coverage | -- | **KILL R3** |
| TBN | $29.02 | 7/0/0, $47 | Thu Nov 12 PM unverified | **KILL, no listed options** |
| CTRE | $35.65 (R1 0.28 on daily bars) | 12/3/0, $41 | Wed Nov 4 PM unverified, LY Nov 5 | **KILL R6** (structural: six PM prints -1.82, -0.31, -1.22, -0.32, +5.32, +0.22, median 0.77%, cap 1.16%) |
| GHM | $68.35 | 5/1/0, $115 | Fri Nov 6 AM unverified, LY Nov 7 | Six AM prints +6.33, -18.21, +0.35, +12.87, -10.98, +0.47: median 8.66%, cap 12.99%. Dec18 $65C OI 7 (7.60/9.80), $70C OI 0 (4.50/9.00), $75C OI 3. **KILL R7** |

**Scan B, sub-$25, prints Oct 30 - Dec 4 (160 rows):** 159 already in week-09 logs; **VALE** new: 13/15/1, **KILL R3** (Holds over Buys, one Sell).

**Scan C, $10-25, prints Dec 12 - Jan 31 (9 rows):** all seen before. Re-checked the ones without a final verdict:

| Name | Stock | R3 | Result |
|---|---|---|---|
| HDB | $22.81 | 41/3/0, $26.23 | Q2 printed Sat Oct 17 (stock -3.19% Mon Oct 19; tool `actual` still null). Next print Jan 19 2027 (LY Jan 17); first passing expiry is **Apr16 2027**. Seven prints: +1.91, +4.22, -0.30, -0.95, -3.38, -10.54, -3.19, median 3.19%, cap 4.78%. A 6-month at-the-money call costs well over 4.78% of spot on its own. **KILL R6** (structural) |
| FCEL | $13.26 | 7/3/2 | **KILL R3** (two Sells) |
| IPX | $13.34 | 6/0/0, $26 | `get_earnings_results` returns nothing. **KILL R2** (no provable print) |
| APLD | $21.02 (+8.7%) | 18/2/0, **$22** | **KILL R4 proxy** (low $22 sits about at the stock; no call's BE fits under it) |
| DX | $11.09 | 4/2/0, **$11.50** | **KILL R4 proxy** |
| CAG / NNE / ADUR | -- | -- | prior kills stand (R3; R6 + R7; no coverage) |

**Scan D, $2-100, prints Nov 28 - Jan 15 (70 rows).** Ratings pulled on all 53 operating companies (closed-end funds and SPACs skipped): every name was already chained or killed in week-09 except **IQMX**, which now has coverage (5/1/0, low $10.42 vs $9.49; Q3 Nov 5 `verified: true`). **KILL: no listed options.** The rest re-confirmed dead at the ratings screen: LULU, LEN, THO, KBH, NKE, GIS, CPB, HRL, AEO, YSS, GEMI, SFIX (R3); CHWY ($21 low vs $21.33), EQPT ($16 vs $16.52), CNM ($40 vs $41.43), BIRK ($27 vs $32.32), EIKN ($4) on the R4 proxy; HOV, CALM, PLAB, WAFD, OXM, ELVR, BBW, DAKT, APC, YB, FWDI, XXI, OWLS, VZLA, NUAI, BTQ no coverage. The R3 passers (RPM, FUL, LGN, FPS, SHAZ, MWH, BETA, AKTS, OFRM, GENB, INFQ, AGMB, MPLT, UEC, BTGO, MOMO, TIGR, PL, DOO) all have a chain-stage kill on file this month (R7, R6, R2 on print history, or R4 dating) and nothing in tonight's ratings changes those reasons.

**Moved to a verdict:** 20 (NRG, NG, GLXY, APH, TTWO, ONDS, BTBT, CLSK, IBOC, LGIH, TBN, CTRE, GHM, VALE, HDB, FCEL, IPX, APLD, DX, IQMX), plus 53 free re-ratings. **Killed:** 14 (NG, GLXY, IBOC, LGIH, TBN, CTRE, GHM, VALE, HDB, FCEL, IPX, APLD, DX, IQMX). **Advanced:** NRG to paper doc. **Parked:** APH (R6), TTWO (R4 dating).

**What it says:** the bottom-quartile universe with prints between Oct 28 and Jan 15, $2-$100, is fished out: 470+ scanner rows tonight and only about 15 names that hadn't already been through the funnel this month. The next new names come from the calendar (January prints on Feb/Mar contracts), not from re-running these bands.

## GLOSSARY

- **R1-R7:** the Iron Rules (binder Tab 1): range percentile, earnings before expiry, ratings, bear floor, chain filter, reachability, liquidity.
- **R6 line / cap:** the largest stock move to breakeven we accept, 1.5x the median earnings-day move over the last six prints.
- **R4 proxy:** at the ratings screen, a lowest target at or under the stock price means no call's breakeven can sit under the floor.
- **Tab 6 dating:** a floor counts only if the Buy target is dated within 60 days and after the stock's slide.
- **Structural R6 kill:** the stock's median print move is so small that no liquid strike is reachable.
- **Paper-size:** passes everything but Rule 5's dollar line; goes to the paper book, not real money.
- **Stamp:** the `updated_at` date on the tool's analyst-target data.
- **AH:** after-hours trading.
