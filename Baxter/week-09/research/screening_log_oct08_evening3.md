# Screening log, Thu Oct 8, 10:00pm ET (EVENING 3 of 3, DO + refill)

**Session job:** refill the queue and leave PREMARKET a loaded plan. First finished EVENING 2's leftovers (CTMX/PHAR Jan15, the 10-name Dec18 list, SLSR), then re-ran the Dec18-window scan (8pm's preview wasn't saved) across three price bands.
**Rule 5 line:** reserve = spendable = $676.28 -> 3.5/5 line **$0.676**. All quotes are the 4:00pm close (market closed).
**Names moved: 25** (cap 25). Plus a free ratings screen on 183 new scan names.

## 1. EVENING 2 leftovers
| Ticker | Stock | Ratings / low | Print (tool) | R6 median / cap | Chain | Verdict |
|---|---|---|---|---|---|---|
| CTMX | $2.47 | 8/0/0, $6 | Nov 5 PM (f), LY Nov 6 | 12.8 / 19.1 (8pm), max BE $2.94 | Jan15 $2C **0.55 / 1.00** (OI 260), mid BE $2.775 (+12.3%); $3C 0.40 / 0.60, BE $3.60 (+45.7%) | **PARK, R5:** $2C passes R6 at mid, ask $1.00 > $0.676. Price watch: needs ask <= $0.676. |
| PHAR | $9.47 | 7/0/0, $20.46 | Nov 5 AM verified | 10.8 / 16.3 | **No option chain at all** (`get_option_chains` empty; same as Oct 6) | **KILL, R5 (no listed options)** |
| DNN | $2.36 | 16/0/0, $3.73 | Nov 3 PM verified, LY Nov 6 | -1.3, -5.36, -0.39, -0.99, -2.97, -0.91: **1.15 / 1.72**, max BE $2.40 | Jan15 $2C 0.50 / 0.60 (OI 8,384), BE $2.60 (+10.2%) | **KILL, R6** |
| NUVB | $4.95 | 12/1/0, $7 | Nov 2 PM (f), LY Nov 3 | +2.94, -0.43, -6.58, -25.34, +9.52, -4.08: **5.33 / 8.0**, max BE $5.35 | Dec18 $5C 0.20 / 0.95 (OI 123), mid BE $5.575 (+12.6%) | **KILL, R6 + R5** |
| SLSR | $6.73 | 5/1/0, $13.35 | **tool still shows no upcoming quarter** (LY Nov 12 PM) | not run | Dec18 listed | **PARK:** R2 needs a tool date |
| WRN, IE, GRAB, TKC, INDI, VYX | | | | Oct 5-6 logs: caps 3.77, 3.32, 2.70, 2.22, 7.10, 12.42% | | **KILL, R6 (carried over).** R6 depends on the stock's print history, not the expiry; a later expiry only raises the premium, so the Nov20 kills hold for Dec18. |
| HLMN | $7.01 | 6/2/0, $10 | Nov 3 AM | 7.63 / 11.45 (Oct 6), max BE $7.81 | Nov20 $7.5C was 0.10 / 0.85, OI 0 | **KILL, R5 + liquidity (carried over):** the Dec18 $7.5C can't be cheaper than the Nov20 that already failed. |
| TBLA | $3.51 | 5/4/0, $5 | Nov 5 AM | 18.04 / 27.06, max BE $4.46 | strikes $2.5 / $5 / $7.5 only | **KILL, R5 (carried over):** $2.5C carries $1.01 intrinsic > $0.676; $5C BE > $4.46. |

## 2. Refill: Dec18 window re-scan (prints Nov 2 - Nov 25, $300M+, 52w pct < 0.25)
Three previews (not saved): **$2-5: 89 rows, $5-12: 158 rows, $12-25: 125 rows.** Names already killed or blocked in a week-09 log were dropped (regex over every log line carrying KILL/R3-R6/BLOCKED). That left 31 / 89 / 67 names; free ratings screen on all of them (4 calls).

**$2-5 band:** only **GROY** passed R3 (8/0/0, $4.00). Most others came back with no coverage.
**$5-12 band:** R3 passes: **OTF** 5/4/0, **EXK** 6/1/0, **RGNX** 10/2/0, **BIOA** 7/2/0. **RUN** 13/7/1 fails the R4 proxy (low $4.63 < stock $7.60). STNE, MLTX, XPEV (2 Sells), CCOI, TRIP, TU, GOOS, FLNC, SMR, JOBY, JKS, CSIQ and others fail R3.
**$12-25 band:** R3 + R4-proxy passes (low / stock): STOK 14/0/0 ($35 / $23.95), NAMS 16/1/0 ($38 / $21.26), AVTX 13/0/0 ($30 / $13.43), MUX 6/0/0 ($28 / $17.32), ENOV 12/1/0 ($24 / $17.44, ratings `updated_at` 2022: stale data flag), VRDN 17/0/0 ($22 / $18.34), PRVA 17/1/0 ($24 / $20.19), BILI 34/1/0 ($18.04 / $15.02), ADNT 9/3/1 ($21 / $17.60), EYE 9/3/0 ($20 / $16.74), TNDM 14/11/0 ($18 / $15.60), ATS 6/1/1 ($20 / $17.67), SRAD 18/7/0 ($13.69 / $12.20), MDU 6/3/0 ($21 / $18.81), KT 20/2/0 ($20.64 / $18.55), CPRI 10/8/0 ($16 / $14.68), KVYO 23/2/0 ($19 / $17.56), BEAM 14/2/0 ($26 / $24.53), RARE 11/10/0 ($16 / $15.15). **R4-proxy kills:** DKNG (low $20 vs $19.93), ACAD ($17 vs $19.39), TSLX ($17.50 vs $17.57).

### R6 from daily closes (6 prints each)
| Ticker | Stock | Print (tool) | Moves (%) | Median / cap | Max BE | Verdict |
|---|---|---|---|---|---|---|
| GROY | $2.88 | Nov 4 PM verified | 0.0, +1.65, -6.49, -9.47, +2.27, -0.69 | 1.96 / 2.94 | $2.96 | **KILL, R6** |
| OTF | $9.43 | Nov 4 PM verified | not run | | | **KILL, R5: no listed options** |
| EXK | $8.32 | Nov 6 AM (f) | +0.3, -4.52, -1.64, -0.93, +9.02, +2.78 | 2.21 / 3.31 | $8.59 | **KILL, R6** (no Dec18 either; Jan15 ATM time value is far above $0.27) |
| RGNX | $8.09 | Nov 5 AM (f) | +2.63, -4.01, -3.79, -4.6, -37.8, +7.43 | 4.30 / 6.46 | $8.61 | **KILL, R6 + R5** (no Dec18; Jan15 $7.5C carries $0.59 intrinsic plus time value) |
| BIOA | $6.26 | Nov 5 PM (f) | -4.82, -0.23, -2.81, -13.53, +0.95, +2.64 | 2.73 / 4.09 | $6.52 | **KILL, R6 + R5** (Dec18 $5C intrinsic $1.26 > $0.676; $7.5C BE > max) |
| AVTX | $13.58 | Nov 5 AM (f) | -1.48, +0.48, -6.26, +0.6, -0.45, -0.74 | 0.67 / 1.00 | $13.72 | **KILL, R6** |
| NAMS | $22.13 | Nov 4 AM (f) | +1.85, +8.7, +4.37, +1.48, +12.46, -0.47 | 3.11 / 4.67 | $23.16 | **KILL, R6 (free math)** |
| MUX | $17.32 | Nov 5 PM (f) | -5.62, -0.37, +2.55, -1.73, +2.45, -7.36 | 2.50 / 3.75 | $17.97 | **KILL, R6 (free math)** |
| STOK | $23.95 | Nov 3 PM (f), LY Nov 4 | -7.56, +24.98, -9.94, +2.32, +0.3, +7.14 | 7.35 / 11.02 | $26.59 | **ADVANCE to Dec18 chain:** $25C ask must be <= $0.676 (R5 binds) |
| VRDN | $18.28 | Nov 4 AM (f), LY Nov 5 | -8.31, -1.38, +8.29, +1.9, +33.36, +6.83 | 7.56 / 11.34 | $20.35 | **ADVANCE to Dec18 chain:** $20C ask <= $0.35 for R6 |
| ENOV | $17.61 | Nov 5 AM **verified**, LY Nov 6 | -3.39, +10.71, -9.75, +13.89, +9.66, -12.82 | 10.23 / 15.35 | $20.31 | **ADVANCE to Dec18 chain:** $17.5C ask <= $0.676 (R5 binds), $20C <= $0.31. Ratings data stale (2022): date the floor first. |

## 3. Tally
25 names moved: **2 parked** (CTMX R5 price watch, SLSR no date), **20 killed** (PHAR, OTF no options; DNN, NUVB, GROY, EXK, RGNX, BIOA, AVTX, NAMS, MUX on R6; WRN, IE, GRAB, TKC, INDI, VYX, HLMN, TBLA carried-over R5/R6; RUN R4 proxy), **3 advanced to the Dec18 chain** (STOK, VRDN, ENOV). Plus 13 more R3 + R4-proxy passes from the $12-25 band queued for R6 (PRVA, BILI, ADNT, EYE, TNDM, ATS, SRAD, MDU, KT, CPRI, KVYO, BEAM, RARE) and DKNG/ACAD/TSLX killed free on the R4 proxy.

**What this pass showed:** the November reporters that still have a real floor are mostly names whose prints barely move the stock. Of 11 names R6'd tonight, 8 have a median print under 5%. The $12-25 band has the only three survivors, and on a $676 reserve its strike grids are where Rule 5 usually kills. That's the next fight.

## GLOSSARY
- **R1 / Rule 1:** stock in the bottom 20-25% of its 52-week range.
- **R2 / Rule 2 (Oct 8):** (a) expiry at least 21 days after the later of the tool's date and last year's date (LY); (b) the 10-Q deadline at least 5 trading days before expiry. "(f)" = `verified: false`.
- **R3 / Rule 3:** at most 1 Sell, at least 3 Buys, Buys at least equal to Holds.
- **R4 proxy:** free screen check that the lowest analyst target sits meaningfully above the stock; the real Rule 4 (lowest dated Buy target above breakeven) comes in the doc.
- **R5 / Rule 5:** one contract's ask must fit the tier budget ($0.676/share at 3.5/5 on $676.28).
- **R6 / Rule 6:** the move to breakeven must be no more than 1.5x the median earnings-day move. Max BE = stock x (1 + cap).
- **Carried over:** a kill from an earlier log that holds for the new expiry because the binding rule doesn't depend on expiry.
- **Free math:** at-the-money time value estimated as 0.4 x IV x sqrt(T) x stock; an estimate, not a quote.
- **Intrinsic value:** stock minus strike for an in-the-money call.
- **Dec18 / Jan15:** the Dec 18, 2026 and Jan 15, 2027 monthly expirations.
- **AM / PM print:** before the open / after the close. AM moves are measured prior close -> print-day close; PM moves print-day close -> next close.
