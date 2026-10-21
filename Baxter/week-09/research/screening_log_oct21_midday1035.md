# Screening log, Wed Oct 21, MIDDAY (10:35am ET): RESEARCHED + BOUGHT

*Live session, regular-session quotes 10:35-10:41. Free tools only (quotes, chains, ratings, earnings, daily candles). 0 searches.*

## Held: COUR $5C Nov20

| Check | Result |
|---|---|
| Quote (10:35) | 0.40 / 0.60 (mark 0.50, OI 3,234, vol 8, IV 80.1%); Tue close 0.53 |
| Stock | $5.06 (-0.2% vs $5.07) |
| Q3 | Thu Oct 29 PM, `verified: true`, `actual: null` (LY Oct 23 PM) |
| Rule 4 | 8/4/0, low **$6.00** vs BE $5.65: holds |
| SEC | no filing since Oct 15 |
| GTC | `6ac7d537` 1 @ $1.65, `gtc`, `confirmed` |

Tab 4 checks 0 through f: none fire. Ramp sell Thu Oct 29 3:35pm ET.

## QUBT Dec18 $7C: ENTERED

| Time (ET) | Stock | Option | R6 line (stock x 1.13875 - 7) | Action |
|---|---|---|---|---|
| 10:35 | $6.665 | 0.47 / 0.55 (OI 1,117, spread 15.7%) | $0.590 | all rules pass; addendum committed (shared `b492b88`) |
| 10:36 | $6.665 | same | $0.590 | buy 1 @ 0.51 (mid), `6ad8cded`: unfilled after a minute, cancelled |
| 10:37 | $6.64 | 0.51 / 0.55 | $0.561 | step 1: buy 1 @ 0.53, `6ad8ce3b`: unfilled after a minute, cancelled |
| 10:38 | $6.625 | 0.53 / 0.55 | **$0.544** | step 2 capped at 0.54 (0.55 would be over the line): `6ad8ce8b` **FILLED 1 @ $0.54, 10:39:31** |
| 10:40 | | | | GTC sell 1 @ $1.35 (2.5x fill), `6ad8ced0`, confirmed `gtc` |

R1 0.052 (52w $6.08-$17.40) | R2 Nov 13 PM unverified, LY Nov 14 PM, `actual: null` | R3 5/2/0 | R4 tool low $10 (Cantor Hold) vs BE $7.54; Ascendiant Buy $32 Aug 26 | R5 0.54 <= $0.676 (reserve before the buy $676.28) | R6 BE $7.54 needs +13.81% from $6.625 vs 13.875% cap | R7 OI 1,117, spread 15.7%.

## Batch: 8 more names (queue 2-6 + watch line)

| # | Name | Dir | Stock | R1 | R3 (B/H/S, low) | R2 (print) | Contract checked | OI | Quote | Needed move vs R6 cap | Result |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **QXO** Dec18 | CALLS | $10.29 | 0.01 (52w $10.035-$27.61) | 19/0/0, $14 | Nov 5 PM unverified, LY Nov 6 PM | $10C `4260ff4a` / $11C `5c438e2d` / $12C `1e4f8b37` | 102 / 456 / 791 | 1.20/1.35; 0.80/0.90; 0.50/0.60 | 6 prints: -0.14, -0.19, +6.51, -3.74, -4.06, -2.55; **median 3.15%, cap 4.72%**. $11C needs +15.6% at the ask, $12C +22.4% | **KILL R6** (structural: a roofing distributor doesn't move on prints). $10C also R7 |
| 2 | GLXY Nov20 $16.5C (paper-size) | CALLS | $16.90 (+7.2%) | ~0.04 | 15/1/0, $24 (undated) | Tue Oct 27 AM verified | `ce4f3f69` | 924 | 1.92 / 2.30 (18.0% of mid) | R6 line = 16.90 x 1.1214 - 16.50 = **$2.45**; ask 2.30 **passes** | **HOLD at floor**: R6 + R7 pass live; still no dated Buy. Paper only, window ends Fri Oct 23 |
| 3 | APH Nov20 $80C (paper-size) | CALLS | $79.79 | -- | 22/2/0, $90 (stamp Oct 3) | (unchanged) | `d254aa6a` | 5,771 | 4.30 / 4.60 (6.7%) | R6 line = 79.79 x 1.0607 - 80 = **$4.63**; ask 4.60 **passes by 3 cents** | **ADVANCE (paper)**: paper doc due EVENING 2, kill Fri Oct 23 |
| 4 | RIOT Nov20 | CALLS | $13.885 | ~0.05 | 24/1/0, $19 | **Tue Nov 3 PM verified**, LY Oct 30 PM | $14C / $15C / $16C | 1,331 / 8,261 / 5,463 | 1.50/1.56; 1.10/1.17; 0.79/0.87 | -- | **Nov20 FAILS R2**: Nov 20 is 17 days after Nov 3 (needs 21). Move to **Dec18** chain. Paper-size either way (asks over $0.622) |
| 5 | TTWO | CALLS | $205.01 | -- | 29/1/1, $270 (stamp **Aug 7**, 75 days) | -- | -- | -- | -- | -- | **HOLD**, floor past 60 days |
| 6 | ONDS (watch) | CALLS | $6.175 | -- | -- | -- | -- | -- | -- | needs ~$6.90 | no change |
| 7 | BTBT (watch) | CALLS | $0.917 | -- | -- | -- | -- | -- | -- | needs ~$1.10 | no change |
| 8 | CLSK (watch) | CALLS | $8.515 | -- | -- | -- | -- | -- | -- | needs > ~$9.20 | no change |

**Totals:** 9 names moved (QUBT bought, QXO killed, RIOT moved to Dec18, GLXY/APH re-measured, TTWO + 3 watch re-checked). The real-money line after the buy: reserve $622.24, 3.5/5 line **$0.622**.

## GLOSSARY

- **R1-R7:** the Iron Rules (binder Tab 1): range percentile, earnings before expiry, ratings, bear floor, chain filter, reachability, liquidity.
- **R6 line:** the highest ask that keeps the needed move to breakeven inside 1.5x the median earnings-day move.
- **Mid / step:** limit at the midpoint first, then at most two steps toward the ask, never over the line.
- **GTC:** good-til-cancelled resting order.
- **Paper-size:** passes everything but Rule 5; goes to the paper book, not real money.
- **Structural R6 kill:** the stock's median print move is too small for any affordable strike to be reachable.
