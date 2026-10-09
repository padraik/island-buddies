# Screening log, Fri Oct 9, 1:35pm ET (MIDDAY, DO)

**Session job:** Michael wants a paper book started, so this run's research seeds it: liquid large caps, every Iron Rule except Rule 5. Live candidates (ARDX, ACHR) requoted first.
**Rule 5 line (real money):** reserve = spendable = $676.28 -> 3.5/5 line **$0.676**. Quotes pulled live 1:35-1:38pm ET. Ratings via `get_equity_analyst_ratings` this run. 0 web searches.
**Names moved: 10** (plus 2 requotes).

## 1. Live candidates (real money)
| Ticker | Contract | Live quote | Stock | Verdict |
|---|---|---|---|---|
| ARDX | $3C Nov20 `e500baad` | 0.30 / 0.65, mark 0.475, OI 49, vol 0 | $3.295 | **NO ORDER.** Mid $0.475 > the doc's $0.45 ceiling, and on hold until the call (liquidity question). 11/0/0, low $8.00 unchanged. |
| ACHR | Nov27 $5C `309e52d9` | 0.46 / 0.53, mark 0.495, OI 8, vol 33 | $4.93 (+4.4%) | **Now passes R6 by 3.9 cents** (max BE $4.93 x 1.1226 = $5.534; BE at mid $5.495, at ask $5.53). R4 7/2/0 low $8.00, still undated. OI 8 = the same thin-strike problem Michael raised. No doc. Held for the call. |

## 2. Source: new paper scan
Saved scan **"Baxter Oct9 PAPER large-cap Oct19-Nov20 prints"** (`20e32def-9451-43e5-92b3-c8b4231d376e`): market cap > $10B, earnings Oct 19 - Nov 20, STOCK, 52-week range pct < 0.25, call-volume column. **187 matches.** Liquidity cut: 2,000+ calls traded today -> **62**.

**Free ratings screen (62, 1 call), R3 + R4 proxy (low target above the stock):**
- Fail R3 (Sells > 1 or Holds > Buys): ASTS, SOFI, VZ, PCG, RIVN, IBM, NVO, FIG, F, CMCSA, HL, CHKP, CHTR, KHC, EIX, AGNC, INTU, TSCO, LOW, SO, KMB, STLA, FISV, O, COIN, CRWV, PDD.
- Fail R4 proxy (low target at or under the stock): NFLX ($57 vs $70.36), T, UBER ($70 vs $71.06), MCD, CVNA, JD, CPNG, BIDU, NEE, CPRT, EQT, BX (+3.7%), BSX (+3.9%), AXP (+4%).
- No coverage: BMNR. Already killed this week: GRAB.
- Stale ratings: CCJ (stamp 2021).
- **Advance (17):** IREN, BA, AS, TMUS, CMG, RKT, IONQ, APP, LVS, KGC, QXO, ALB, TCOM, SE, BKNG, FSLR, HD. Took the top 10 by liquidity and R4 margin.

## 3. Chain checks (10)
R6 = six most recent prints, close-to-close reaction (PM: print day -> next day; AM: day before -> print day), from daily bars pulled this run. Max BE = stock x (1 + 1.5 x median). Expiry = first listed one >= 21 days past the later of tool date and LY date.

| Ticker | Stock | Ratings / low | Print (tool, LY) | Six reactions / median / cap | Contract | Quote | BE at ask / max BE | Verdict |
|---|---|---|---|---|---|---|---|---|
| **BA** | $190.60 | 28/5/0, $240 | Oct 27 AM **verified**, LY Oct 29 | +6.06 / -4.37 / -4.37 / -1.56 / +5.53 / +4.76; 4.56%; 6.85% | Nov20 $195C `a30375aa` | 7.30 / 7.70, OI 1,695 | $202.70 / $203.65 | **PAPER ENTRY @ 7.70** |
| **CMG** | $31.385 | 27/12/0, $35 | Oct 28 PM **verified**, LY Oct 29 | +1.60 / -13.34 / -18.18 / +1.94 / +3.03 / +12.50; 7.76%; 11.65% | Nov20 $32.5C `d09c051f` | 1.42 / 1.48, OI 5,109 | $33.98 / $35.04 | **PAPER ENTRY @ 1.48** |
| **LVS** | $36.00 | 17/7/0, $47 | Oct 21 PM (f), LY Oct 22 | +6.49 / +4.31 / +12.39 / -13.96 / -8.62 / +1.72; 7.55%; 11.33% | Nov20 $37.5C `5e7ad1e5` | 1.12 / 1.35, OI 1,417 | $38.85 / $40.08 | **PAPER ENTRY @ 1.35** |
| RKT | $11.42 | 10/8/0, $13 | Oct 29 PM (f), LY Oct 30 | -4.64 / +11.98 / +4.52 / +2.36 / +10.88 / +3.78; 4.58%; 6.87% | Nov20 $12C `0219d087` | 0.78 / 0.81, OI 8,587 | $12.81 / $12.20 | **KILL, R6** (and the real-money R5: 0.81 > 0.676) |
| IONQ | $39.30 | 13/3/0, $49 | Nov 4 PM (f), LY Nov 5 | +9.27 / -1.79 / +3.65 / +21.70 / -9.30 / -0.53; 6.46%; 9.69% | Nov27 $40C `c284bb03` | 3.35 / 3.95, OI 2 | $43.95 / $43.11 | **KILL, R6** (also fails liquidity, OI 2) |
| IREN | $34.905 | 17/5/0, $40 (stamp Aug 28) | Nov 5 PM (f), LY Nov 6 | -2.76 / +14.93 / -6.84 / +5.13 / +7.65 / -12.53; 7.25%; 10.87% | Nov27 $35C `68b0de5a` | 3.90 / 4.05, OI 56 | $39.05 / $38.70 | **KILL, R6** (and floor stamp > 60 days, liquidity OI 56) |
| QXO | $10.857 | 19/0/0, $15 | Nov 5 PM (f), LY Nov 6 | -0.14 / -0.19 / +6.51 / -3.74 / -4.06 / -2.55; 3.15%; 4.72% | Dec18 $11C `5c438e2d` | 1.15 / 1.25, OI 0 | $12.25 / $11.37 | **KILL, R6** |
| AS | $27.92 | 26/1/0, $31 | Nov 17 AM (f), LY Nov 18 (6-K filer, both dates present) | +19.05 / -4.69 / +8.45 / -5.56 / +2.05 / +3.22; 5.12%; 7.69% | Dec18 $30C `a39eb368` | 1.50 / 1.60, OI 7,096 | $31.60 / $30.07 | **KILL, R6** |
| APP | $276.98 | 32/7/0, $325 | Nov 4 PM **verified**, LY Nov 5 | +11.88 / +11.97 / +0.70 / -19.68 / +6.41 / -19.66; 11.93%; 17.89% | Nov27 $280C `84fcbf75` | 25.20 / 30.00, OI 1, vol 0 | $310.00 / $326.53 | **PARKED, liquidity** (passes R6; OI 1, spread 17%). EVENING: check Dec18 $280C/$290C. |
| TMUS | $149.08 (**-13.0% today**, close $171.31) | 27/5/0, $169 (stamp Oct 8) | Oct 28 PM verified | -11.22 / +5.80 / -3.26 / +5.07 / +6.13 / -10.75; 5.96%; 8.95% | not pulled | | | **PARKED, R4 floor predates today's drop** (Tab 6: floor must be published after the decline). Find out why it fell 13% before anything else. |

## 4. Result
10 moved: **3 paper entries** (BA, CMG, LVS -> `Baxter/paper_book.md`), **5 killed** (RKT, IONQ, IREN, QXO, AS: all R6), **2 parked** (APP liquidity at Nov27, TMUS floor stale after a -13% day). Not chained yet (EVENING): KGC, ALB, TCOM, SE, BKNG, FSLR, HD.

What it says: on liquid names, Rule 6 still does most of the killing (5 of 9), the same as on the cheap names. The difference is that liquid chains let the survivors through cleanly: BA, CMG, LVS all have OI over 1,000 and spreads of 4-19%, against ARDX's 49 OI and 74% spread. None of the three fits the real fund: the cheapest, LVS, costs $135, double the $67.60 line.

## GLOSSARY
- **R1 / range pct:** where the stock sits in its 52-week range; < 0.25 = bottom quartile (calls side).
- **R2:** earnings print proven to land before expiry (21 days past the later of tool date and last year's date; 10-Q deadline 5+ trading days before expiry).
- **R3:** at most 1 Sell, at least 3 Buys, Buys >= Holds.
- **R4 / floor / low:** the lowest Buy-rated price target must be above breakeven, and published after the decline.
- **R5:** one contract's ask <= tier % x reserve / 100 ($0.676 at 3.5/5 today). Dropped for paper.
- **R6 / cap / max BE:** the move to breakeven must be <= 1.5x the median earnings reaction; max BE = stock x (1 + cap).
- **BE:** strike + premium. **OI:** open interest. **(f):** date not company-verified.
- **Paper entry:** logged as if bought at the ask, no money.
- **Parked:** alive, waiting on one specific check.
