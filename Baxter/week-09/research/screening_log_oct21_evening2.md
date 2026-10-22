# SCREENING LOG: Wed Oct 21, 2026, EVENING 2 (8:00pm ET, VM)

*Market closed; quotes are the 4:00pm close (after-hours prints noted). Session 2's job: docs for every name past the chain stage. One name qualified (NRG). 4 searches, all on NRG. No scans run.*

## Held

| Check | COUR $5C Nov20 | QUBT $7C Dec18 |
|---|---|---|
| Quote (close) | 0.40 / 0.55 (mark 0.475, OI 3,234) | 0.60 / 0.89 (mark 0.745, OI 1,117) |
| Stock | $4.97 official close, AH $5.02 | $6.82 official close, AH $6.76 |
| Earnings | Thu Oct 29 PM, `verified: true`, `actual: null` | Fri Nov 13 PM, `verified: false`, `actual: null` (LY Nov 14 PM) |
| Rule 4 | 8/4/0, low **$6.00** vs BE $5.65: holds | 5/2/0, tool low **$10** vs BE $7.54: holds |
| SEC since Oct 15 | none | none |
| GTC | `6ac7d537` 1 @ $1.65, `gtc`, `confirmed` | `6ad8ced0` 1 @ $1.35, `gtc`, `confirmed` |

Tab 4 checks 0 through f: none fire on either.

## Queue names

| # | Name | Dir | Stock | R1 | R3 (B/H/S, low) | R2 | Contract | OI | Quote | R6 | Result |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **NRG** Dec18 $105C | CALLS | $99.80 (AH $100.50) | **0.067** (weekly $93.355 - $189.96) | 16/4/0, $131 (stamp Oct 3) | Nov 5 AM (f), LY Nov 6; Dec18 42 days past; 10-Q Nov 9 | `6fa30201` | 511 | 6.20 / 7.10 (13.5%) | BE $112.10 = +12.32% vs cap 13.44% | **PAPER ENTRY at $7.10.** Floor re-sourced: EVENING 1's Siebert Williams Shank $184 is a **Jul 6** initiation (stale, pre-slide), so it's dropped. One search found **Jefferies Buy, cut $160 -> $131** and Seaport Buy $190 -> $160, dated Sep 28 - Oct 19, post-slide. Floor $131, $18.90 over BE. Doc `research_NRG_paper.md`, vote 3-2 |
| 2 | APH Nov20 $80C | CALLS | $79.19 (AH $78.65) | -- | 22/2/0, $90 | -- | `d254aa6a` | 5,771 | close unchanged 3.90 / 4.40 | line $4.00; ask 4.40 fails (AH line $3.42, worse) | **PARKED, R6.** Kill Fri Oct 23 |
| 3 | TTWO | CALLS | $206.18 | ~0.22 | 29/1/1, $270 (stamp **Aug 7**, 75 days) | -- | -- | -- | -- | -- | **HOLD**, floor past 60 days |
| 4-6 | ONDS / BTBT / CLSK (watch) | CALLS | $6.26 / $0.944 / $8.77 | -- | 11/0/0 $13 / 6/0/0 $3.50 / 15/0/0 $19 | -- | -- | -- | -- | need ~$6.90 / ~$1.10 / > ~$9.20 | no change |

**Moved:** NRG (doc + paper entry), APH, TTWO, ONDS, BTBT, CLSK re-checked (6). **Killed:** none. **Real money:** nothing buyable under the $0.622 line.

**Correction logged:** EVENING 1 dated the Siebert Williams Shank $184 Buy "~Oct 15" from a MarketBeat "4 days ago." It's Jul 6 2026. NRG's advance survived only because a second, real post-slide Buy exists. Aggregator "N days ago" lines aren't dates.

## GLOSSARY

- **R1-R7:** the Iron Rules (binder Tab 1): range percentile, earnings before expiry, ratings, bear floor, chain filter, reachability, liquidity.
- **R6 line / cap:** the largest stock move to breakeven we accept, 1.5x the median earnings-day move over the last six prints.
- **Tab 6 dating:** a floor counts only if the Buy target is dated within 60 days and after the stock's slide.
- **Stamp:** the `updated_at` date on the tool's analyst-target data.
- **(f):** tool date not verified by the company.
- **AH:** after-hours trading.
- **Paper entry:** tracked-only position at the closing ask, no money.
