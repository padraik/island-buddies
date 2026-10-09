# Screening log: Fri Oct 9, EVENING 1 (6:00pm ET)

**Source:** the research queue's parked names (FSLR, APP, TMUS, SE, RKT), then the second tier of the paper scan `Baxter Oct9 PAPER large-cap Oct19-Nov20 prints` (`20e32def-9451-43e5-92b3-c8b4231d376e`), re-run tonight: 185 rows, **90 never named in any Oct 5-9 log**.
**Quotes:** market closed. Option and stock quotes are the regular-session close (option quotes stamped 3:59:4x-3:59:59pm ET Oct 9). Ratings via `get_equity_analyst_ratings` this run. Floors dated via MarketBeat forecast pages (WebFetch: FSLR, APP, NRG). 2 web searches (TMUS cause).
**Rule 5 line (real money):** reserve = spendable = $676.28 -> 3.5/5 line **$0.676**. Nothing below is anywhere near it; this log feeds the paper book.

R6 = six most recent prints, close-to-close reaction (PM: print day -> next day; AM: day before -> print day), daily bars pulled this run. Max BE = stock x (1 + 1.5 x median). Expiry = first listed one >= 21 days past the later of tool date and LY date. **R7 = OI >= 250 and spread <= 25% of mid.**

## 1. Queue names

| Ticker | Stock | Ratings / floor | Print | Contract / quote | BE at ask / max BE | R7 | Verdict |
|---|---|---|---|---|---|---|---|
| FSLR | $177.82 | 29/10/1. The tool's $197 low is **Bernstein Underperform** (Jul 31), i.e. the one Sell, not a floor. MarketBeat Buy-side actions inside 60 days: Evercore Positive $218 (Aug 17), GLJ Buy $250 (Sep 22), Baird Outperform $290 (Sep 22), Piper OW $251 (Sep 30), Goldman Buy $272 (Oct 8). BMO went to Market Perform Aug 27, so its old $187 doesn't count. Last leg down was the week of Sep 21 ($198 -> $177); lowest Buy target published after it: **Piper $251**. Even Evercore's $218 clears. | Oct 29 PM (f), LY Oct 30 -> Nov 20 exactly; 10-Q Nov 9 | Nov20 $175C `99f5f557` 13.60 / 16.50 (close), OI 282, vol 11, spread 19.3% | **$191.50 / $195.98** (cap 10.21%) | pass | **PAPER ENTRY** @ $16.50. R4 resolved. |
| APP | $277.02 | 32/7/0, tool low $325 (Sep 11) predates the Sep 28 week (-17%, $322 -> $268). MarketBeat: **Jefferies Buy $375, Oct 8** (lowered, post-drop), Needham Buy $475 Oct 6. Floor $375. R1 0.02 ($266.84-$738). | Nov 4 PM **verified**, LY Nov 5 -> Dec18 | Dec18 **$290C** `07e4b5a0` 26.10 / 27.40, OI 350, spread 4.9%. ($280C 30.30 / 34.50 OI 269 spread 13%; $300C 22.30 / 23.60 OI 531; $270C OI 334 spread 14%) | **$317.40 / $326.58** (cap 17.89%) | pass | **PAPER ENTRY** @ $27.40. |
| TMUS | $148.59 (-13.3%) | 27/5/0, low $169 stamped Oct 8 23:11 UTC (pre-drop). **Cause found:** SpaceX confirmed an ~$8B spectrum purchase from Grain Management, positioning Starlink against the carriers; T and VZ fell too; worst TMUS day in ~13 years (Seeking Alpha, Benzinga, TipRanks, Oct 9). No SEC filing since Oct 5. | Oct 28 PM verified | not chained | n/a | n/a | **PARKED, R4 + decline category.** A new competitor is a Category-2 shape (TME, Aug 8) unless the Street calls it overdone with fresh Buy targets. Needs a post-Oct 9 Buy target. |
| SE | $95.24 | 27/4/0, $105 stamped Aug 12 (stale after Sun Oct 11) | Nov 10 AM (f), 6-K | Dec18 $95C `4fe7f5f7` 8.85 / 9.55, **OI 157** | $104.55 / $114.74 | fail | **PARKED, R7 + floor aging.** Unchanged. |
| RKT | $11.47 | 10/8/0, $13 | | Nov20 $12C | | | **PARKED.** Under the $11.75 cutoff; off the queue if it opens there Monday. |

## 2. Second-tier free screen (90 names)
R3 (<= 1 Sell, >= 3 Buys, Buys >= Holds) plus R4 proxy (low target >= ~1.08x stock, so a near-the-money breakeven can sit under it).

- **No coverage (3):** IESC, ERIE, FMS.
- **R3 fail (31):** NVR (3 Sells), MKL (0 Buys), FICO (4 Sells), AON (3), VMC (2), HUBS (14/22), HON (2), PAC (7/8), HSY, ATO, DHI, LDOS, MAA, PHM (2 Sells), WEC, CPT, CLX, DECK (3), GGG, ZTS (8/11), TXT (9/10), SF, ES, WPC, BRO, COO, TSN, ENB (2), EMA, EXC, PHG, WSO.B, LII.
- **R4 proxy fail, low within ~8% of the stock (30):** TDG, NOC, TYL, CSL, SYK (1.075), EVR, TM, EFX, BWXT, DTE, DUK, SUI, KKR, EXE, APH, SRE, FLUT, NGG, LNT, TRU, GEHC, ALC, ELS, GSK, BAM, NI, ALLY, MDLN, plus MLM / CMS / FE (passed the proxy, not worked tonight, see queue).
- **Advance (26):** IDXX, CW, MLM, AXON, NVMI, HII, LHX, ALNY, MTZ, VRSK, FTAI, TXRH, AZN, WCN, CBRE, NRG, XYL, RBA, ORLY, ULS, OTIS, CMS, SGI, FE, BCE, CARR. 20 worked below; MLM, NVMI, AZN, CMS, FE, BCE queued.

## 3. Second tier, chained

| Ticker | Stock | R1 | Ratings / low | Print (tool, LY) | Six reactions / median / cap | Contract | Quote | BE at ask / max BE | R7 | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| AXON | $417.31 | 0.18 | 21/3/0, $600 | Nov 3 PM (f), LY Nov 4 | +14.13 / +16.41 / -9.43 / +17.55 / +10.63 / -14.28; 14.21%; 21.31% | Dec18 $400C / $420C / $440C | 54.90 / 62.00 OI 44; 44.80 / 51.70 OI 58; 36.10 / 43.30 OI 44 | $462 / $506.23 | fail | **KILL, R7** (three strikes, OI 44-58). Passes everything else with room. |
| FTAI | $171.06 | 0.12 | 12/0/0, $275 | Oct 29 AM **verified**, LY Oct 27 | -18.87 / +26.56 / -3.08 / +2.65 / +17.16 / +0.07; 10.12%; 15.18% | Nov20 $175C / $180C | 10.70 / 16.60 OI 34; 8.80 / 14.10 OI 117 | $191.60 / $197.03 | fail | **KILL, R7** (spreads 43-46%) |
| NRG | $106.32 | 0.13 | 15/4/0, tool low $159 = **Morgan Stanley Equal Weight** (Sep 18), not a Buy. Newest Buy-side targets: Evercore OP $195 / Scotiabank SO $211, both **Aug 5** (65 days, and before the slide) | Nov 5 AM (f), LY Nov 6 | +26.21 / -13.61 / -1.78 / +4.25 / -4.31 / -15.48; 8.96%; 13.44% | Dec18 **$105C** `6fa30201` | 10.80 / 11.80, OI 523, spread 8.8% | $116.80 / $120.61 | pass | **PARKED, R4 dating.** Clears R1/R2/R3/R6/R7; no Buy target inside 60 days. ($110C 8.40 / 9.50 OI 1,355 also passes R6 by $1.11.) |
| MTZ | $216.66 | 0.13 | 23/2/0, $280 | Oct 29 PM (f), LY Oct 30 | +5.12 / -8.01 / -4.58 / +2.78 / +5.93 / -18.91; 5.53%; 8.29% | Nov20 $220C / $210C | 15.40 / 16.30 OI 1,609; 18.30 / 20.80 OI 36 | $236.30 / $234.62; $230.80 | $220 pass, $210 fail | **PARKED.** Liquid strike misses R6 by $1.68; the strike that fits is thin. Alive at stock ~$218.2+ on the $220C. |
| SGI | $62.34 | 0.06 | 11/1/0, $80 | Nov 5 AM (f), LY Nov 6 | -0.97 / +0.43 / +11.78 / -8.60 / -10.11 / -6.77; 7.68%; 11.53% | Dec18 $65C / $60C | 3.70 / 5.10 OI 84; 6.00 / 6.90 OI 0 | $70.10 / $69.53 | fail | **KILL, R7** (and R6 at $65C) |
| RBA | $84.03 | 0.15 | 13/1/0, $110 | Nov 9 AM verified | median 2.87%; cap 4.30% | | | max $87.65 | | **KILL, R6** (a 4.3% cap can't pay for 10 weeks of premium) |
| IDXX | $513.14 | 0.05 | 9/6/1, $665 | Nov 2 AM verified | median 6.77%; cap 10.16% | Dec18 $520C | 28.30 / 37.20, OI 3 | $557.20 / $565.29 | fail | **KILL, R7** |
| CBRE | $131.08 | 0.18 | 13/2/0, $164 | Oct 22 AM verified | median 1.71%; cap 2.57% | | | max $134.44 | | **KILL, R6** |
| CW | $507.29 | 0.02 | 8/4/0, $622 | Nov 4 PM verified | median 4.50%; cap 6.75% | Dec18 $500C | 39.40 / 47.80, OI 1 | $547.80 / $541.53 | fail | **KILL, R7 + R6** |
| HII | $265.02 | 0.04 | 9/6/0, $304 (Sep 24) | Oct 29 AM verified, LY Oct 30 | -1.24 / +7.87 / +6.92 / -10.59 / -10.25 / +14.09; 9.06%; 13.59% | Nov20 **$270C** `ad19b167` | 12.30 / 14.00, **OI 235**, spread 12.9% | $284.00 / $301.04 | fail by 15 OI | **PARKED, R7.** $260C OI 13. Requote OI Monday. |
| LHX | $236.92 | 0.03 | 14/9/0, $260 | Oct 29 AM verified | median 1.27%; cap 1.90% | | | | | **KILL, R6** |
| WCN | $154.69 | 0.24 | 25/4/0, $180 (Jul 23) | Oct 21 PM verified | median 2.38%; cap 3.57% | | | | | **KILL, R6** |
| OTIS | $66.11 | 0.08 | 9/8/1, $73 | Oct 28 AM verified | median 2.21%; cap 3.32% | | | | | **KILL, R6** |
| ORLY | $86.01 | 0.16 | 26/6/0, $94 | Oct 28 PM verified | median 3.25%; cap 4.88% | | | | | **KILL, R6** |
| VRSK | $175.49 | 0.21 | 14/9/0, $195 | Nov 5 AM verified | median 5.47%; cap 8.21% | Dec18 $175C | 11.90 / 13.80, OI 10 | $188.80 / $189.90 | fail | **KILL, R7** |
| XYL | $101.99 | 0.06 | 17/7/0, $112 | Oct 27 AM verified | median 4.27%; cap 6.40% | Nov20 $100C | 5.40 / 6.80, OI 11 | $106.80 / $108.51 | fail | **KILL, R7** |
| TXRH | $162.76 | 0.14 | 17/12/1, $186 | Nov 5 PM verified | median 3.74%; cap 5.60% | Dec18 $160C | 9.50 / 12.40, OI 16 | $172.40 / $171.88 | fail | **KILL, R7 + R6** |
| CARR | $55.83 | 0.21 | 17/12/0, $60 | Oct 29 AM verified, LY Oct 28 | +11.61 / -10.61 / +0.77 / -0.71 / +8.79 / -8.90; 8.84%; 13.27% | Nov20 $55C `51e40c98` | 3.00 / 3.30, **OI 99**, spread 9.5% | $58.30 / $63.24 (floor $60) | fail | **PARKED, R7.** R4 passes by $1.70. Check $52.5C / $57.5C OI next. |
| ULS | $70.65 | 0.17 | 9/6/0, $82.80 | Nov 3 AM (f), LY Nov 4 | +12.29 / -11.51 / +10.62 / +15.99 / +16.25 / -13.96; 13.12%; 19.69% | no Dec18 listed; Nov20 fails R2 | | max $84.56 | | **PARKED.** Chain Jan15 $70C / $75C next. |
| ALNY | $224.53 | 0.09 | 23/9/0, $256 | Oct 29 AM (f), LY Oct 30 | -3.08 / +15.43 / -6.65 / -4.28 / +2.76 / -28.31; 5.46%; 8.20% | Nov20 (no $225 strike) | | max $242.94 | | **PARKED.** Chain Nov20 $220C / $230C next. |

## 4. Result
**25 names moved** (5 queue + 20 second tier), plus 70 cut free at the ratings screen.
- **2 paper entries:** FSLR $175C Nov20 @ $16.50, APP $290C Dec18 @ $27.40.
- **14 killed:** AXON, FTAI, SGI, IDXX, VRSK, XYL (R7); CW, TXRH (R7 + R6); RBA, CBRE, LHX, WCN, OTIS, ORLY (R6).
- **9 parked:** TMUS (R4 + decline category), SE (R7 + floor), RKT (price), NRG (R4 dating), MTZ (R6/R7 split across strikes), HII (OI 235), CARR (OI 99), ULS (Jan15 chain), ALNY (strike grid).

What it says: Rule 7 is now the main killer on the mid-cap names (six outright, two more parked within a few hundred contracts). The liquid large caps die on R6 instead, because they don't move on earnings. The names that survive both are the volatile, heavily traded ones that fell hard: FSLR, APP. Two floors that looked dead turned out fine once dated (FSLR's $197 was a Sell's target; APP got a post-drop Jefferies $375), and one that looked fine (NRG $159) turned out to be a Hold's target. **The tool's "low target" is not the lowest Buy target; it's the lowest target of any rating.** Worth checking that on every name, real or paper.

## GLOSSARY
- **R1 / range pct:** where the stock sits in its 52-week range; < 0.25 = bottom quartile (calls side).
- **R2:** earnings print proven to land before expiry (21 days past the later of tool date and last year's date; 10-Q deadline 5+ trading days before expiry; 6-K filers need both dates).
- **R3:** at most 1 Sell, at least 3 Buys, Buys >= Holds.
- **R4 / floor / low:** the lowest Buy-rated price target must be above breakeven, dated within 60 days and published after the decline.
- **R5:** one contract's ask <= tier % x reserve / 100 ($0.676 at 3.5/5 today). Dropped for paper.
- **R6 / cap / max BE:** the move to breakeven must be <= 1.5x the median earnings reaction; max BE = stock x (1 + cap).
- **R7:** liquidity floor, OI >= 250 and spread <= 25% of mid on the exact contract.
- **BE:** strike + premium. **OI:** open interest. **(f):** date not company-verified. **6-K:** foreign filer, no 10-Q deadline.
- **Category 2 decline:** the business itself got worse (a new competitor, a broken product), as opposed to an overreaction.
- **Parked:** alive, waiting on one specific check.
