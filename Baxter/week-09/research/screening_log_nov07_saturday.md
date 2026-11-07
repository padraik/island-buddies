# Screening log: Saturday Nov 7, 2026, 9:00am ET (SATURDAY sweep)

*Job (from EVENING 3's handoff): full sweep, prints Dec 23 - Feb 12 (Jan15 / Feb19 expiries), diff every row against the week-09 logs before spending a chain. Reserve $539.11: 3.5/5 R5 line $0.539, screen line $1.078. Market closed. Stock prices and option quotes are Friday's closes (option books as of 3:59pm, so spreads carry closing width).*

**Scan (preview, not saved):** market cap $300M - $5T, stock, `FILTER_TYPE_EARNINGS_DATE` **20261223-20270212**, range pct (52W) expression **< 0.25** (same expression as the Oct 5 sweep), total call volume >= 100. **174 rows**, under the 200 cap, so no price-band split was needed. Every row was checked against the last 30 week-09 screening logs (Oct 24 - Nov 6): **113 already worked and stay as logged. 61 fresh** (either never logged or last logged before Oct 24). One ratings call covered all 61.

## Free screen: 61 in, 19 out

**No coverage (10):** MZTI, TBBK, BEPC, ARLP, AOSL, AMSC, QDEL, ADUR, CIM, LSAK.

**KILLED R3 (19):** FICO (12/11/3), ROK (13/18/1), CHTR (5/6/6), ZTS (5/13/0), WPC (7/8/0), NNN (4/12/3), AB (1/6/0), PEGA (4/9/0), ZG (14/16/0), KMT (0/4/4), GNTX (5/6/1), YELP (2/7/3), ACI (4/13/4), SAFE (3/7/1), TU (5/12/4), GOOS (3/4/5), FMC (3/14/2), IVR (1/4/1), DCH (5/7/1).

**KILLED R4 proxy (13)** (the tool's low target is under the stock or within ~5% of it, so no call breakeven can clear it): NVMI ($320 vs $313.18), LHX ($241 vs $259.97), VRT ($187 vs $183.02), BA ($157 vs $173.46), LEU ($100 vs $104.72), ALB ($95 vs $99.25), XYL ($90 vs $97.84), RDDT ($100 vs $95.10), UBER ($70 vs $68.68), CG ($40 vs $39.69), HDB ($26.23 vs $25.15), VALE ($9.50 vs $11.60), OWL ($10 vs $9.90).

## Past the free screen: 19 names

**The Rule 2 finding that shapes this whole window:** these prints are Q4 (December-quarter) reports for calendar-year companies, so the backstop deadline in Rule 2(b) is the **10-K**, not a 10-Q: Mar 1 for large accelerated filers, Mar 16 for accelerated, Mar 31 for everyone else. (Same reading the AVGO paper doc used for its FQ4.) **Feb19 fails 2(b) for every calendar-year filer**, whatever its print date. Those names need Mar19 (large accelerated) or Apr16, and Mar19 still has thin OI on most chains (Nov 5 finding). Feb19 only works for off-calendar fiscal years whose Dec-quarter report is a 10-Q, or whose 10-K came due in January. Earlier logs (NG on Oct 21) treated Feb19 as passing for a January print without the 10-K check; this log applies the check. Flagged for a local session in case the Oct 8 wording meant something else.

| # | Ticker | Close | R1 | B/H/S, low | Print (tool, LY) | First expiry passing R2 | Contract checked | Book (Fri close) | OI | Result |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **MNTN** | $5.33 | -0.254 (new lows after the Nov 4 miss, EPS 0.10 vs 0.25) | 7/5/0, $6 | Tue Feb 9 PM (f), LY Feb 10 | Mar19 on (a); (b) depends on filer status (IPO'd 2025: 90-day 10-K = Mar 31 would push it to Jun17) | Mar19 $5C `f5f46fd8` / $7.5C `b9c1e16b` | 1.00 / 1.20; 0.30 / 0.45 | 391 / 71 | **KILLED, R4.** $5C breakeven at the ask $6.20 is over the $6 low target. Also fails R5 ($1.20 vs $0.539). $7.5C fails R7 (OI 71) and R4 harder. The only real-money-shaped liquid contract in the sweep |
| 2 | **FUL** | $49.86 | 0.144 | 8/1/0, $55 | Wed Jan 13 PM (f), LY Jan 14 | **Feb19** (FY ends ~Nov 30; 10-K due ~late Jan) | Feb19 $50C `15fd6b73` / $55C `e11b6b71` | 2.10 / 4.50; 0.55 / 2.65 | 13 / 1 | **KILLED, R7** (OI 13 / 1; spreads 73% / 131%) |
| 3 | **NRIX** | $15.28 | 0.218 | 13/1/0, $20 | Wed Jan 27 PM (f), LY Jan 28 | Feb19 on (a), but **no Feb19 listed** (Nov20, Dec18, Jan15, Apr16, Dec17) | Apr16 $15C-$18C | 1.80 / 5.50 ... 0.95 / 4.20 | 3-27 | **KILLED, R7** (OI 27 at best, spreads > 100%) |
| 4 | **CRS** | $279.15 | 0.016 | 8/3/0, $315 (ratings stamp 2021, so the floor is undated anyway) | Thu Jan 28 AM (f), LY Thu Jan 29 AM | Feb19 on (a) exactly (Jan 29 + 21) and (b) (FY June, 10-Q due Feb 9), but **no Feb19 listed** (Jan15, Mar19) | none | | | **PARKED to ~Dec 15** (Mar19 OI). Paper size only |
| 5 | **MGY** | $23.67 | 0.223 | 17/6/0, $26 | Thu Feb 4 PM (f), LY Feb 5 | Mar19 | Mar19 $25C `5c117c7f` / $22.5C `e135df45` | 1.10 / 2.30; 1.90 / 4.20 | 502 / 91 | **KILLED, R6.** $25C at mid ($1.70) needs +12.8% to $26.70; 7-print median 2.57% (+2.73, -2.30, -2.57, +2.98, -1.75, +4.34, +0.64), cap 3.85%. R7 fails at the close too (70.6% / 75.4%), and R5 |
| 6 | **SLM** | $16.93 | -0.031 | 5/3/1, $22 | Thu Jan 21 PM (f), LY Jan 22 | Feb19 fails (b) (10-K Mar 1); no Feb19 or Mar19 listed; Apr16 | Apr16 $17C-$20C | 1.80 / 2.15 ... 0.75 / 1.10 | 0-24 | **KILLED, R7** (OI 0 / 24 / 4 / 21). Also R5 |
| 7 | **SKHY** | $127.90 | 0.041 | 12/2/0, $200 | Sat Feb 13 PM (f); **no LY date** (3 quarters on record) | ADR, 6-K filer: both dates required, LY missing | none | | | **KILLED, R2** (no last-year date, so "proven before expiry" can't be shown). Recheck after the Feb print |
| 8 | **CLS** | $208.50 | -0.157 | **25/0/0, $325** | Wed Jan 27 PM (f), LY Jan 28 | Feb19 on (a); fails (b) if it files a 10-K (Mar 1). Mar19 | none | | | **PARKED to ~Dec 15** (Mar19). Paper. Strongest board in the sweep; low target 56% over the stock |
| 9 | **APTV** | $39.55 | -0.064 | 17/5/0, $44 | Mon Feb 1 AM (f), LY Feb 2 | Mar19 | none | | | **PARKED to ~Dec 15** (Mar19) |
| 10 | **MCHP** | $58.34 | 0.171 | 23/6/0, $62 | Thu Feb 4 PM (f), LY Feb 5 | Mar19 | none | | | **PARKED to ~Dec 15** (Mar19). R4 tight (low 6.3% over) |
| 11 | **WYNN** | $83.08 | 0.192 | **25/0/0, $93** | Thu Feb 11 PM (f), LY Feb 12 | Mar19 | none | | | **PARKED to ~Dec 15** (Mar19). Paper |
| 12 | **AORT** | $20.21 | 0.036 | 9/0/0, $30 | Thu Feb 11 PM (f), LY Feb 12 | Mar19 on (a); (b) Mar16 / Mar31 if not large accelerated, so likely Apr16 | none | | | **PARKED to ~Dec 15** (check filer status and Apr16 OI) |
| 13 | **ICHR** | $30.97 | 0.170 | 8/1/0, $55 | Mon Feb 8 PM (f), LY Feb 9 | Mar19 on (a); likely Apr16 on (b) | none | | | **PARKED to ~Dec 15** |
| 14-19 | FN, IDCC, HWM, ALNY, MOD, CIGI | | | FN 10/2/0 $364; IDCC 6/0/0 $425; HWM 23/3/0 $230 (stamp 2021); ALNY 22/11/0 $180; MOD 12/0/0 $160; CIGI 8/4/0 $111 | scan dates Feb 2 - Feb 12 | Mar19 on (a) alone | none | | | **PARKED to ~Dec 15** (Mar19). All paper size |

**Totals:** 174 rows, 113 already worked, 61 fresh. 42 cut free (10 no coverage, 19 R3, 13 R4 proxy). 19 past the free screen: 6 killed (MNTN R4, FUL R7, NRIX R7, MGY R6, SLM R7, SKHY R2), 13 parked to ~Dec 15 for Mar19/Apr16 OI. **0 advanced, 0 buyable.** No Five-Baxter meeting was written because nothing cleared the chain.

**What it means:** the Jan/Feb print window is gated by the calendar, not by the names. A December-quarter print needs Mar19 or later, those chains build OI in December, and until then a real-money contract at a $0.539 line doesn't exist. Next week's evening runs should finish the Nov 16 - Dec 22 window's slide-ins and re-run this scan around Dec 12-15, when Mar19 OI is there.

Calls used: 1 preview scan, 1 ratings call (61 names), 13 earnings calls, 5 chain lists, 5 instrument lists, 3 quote batches, 1 historicals pull. No web searches.

## GLOSSARY
- **R1 (range percentile):** where the stock sits between its 52-week low (0) and high (1). Calls need the bottom quarter. A negative number means Friday's close was under the lowest weekly low, so the stock is making new lows.
- **R2 (earnings proven before expiry):** the expiry must be at least 21 days after the later of the tool's date and last year's date (a), and the SEC filing deadline for that quarter must fall at least 5 trading days before expiry (b).
- **10-K / 10-Q:** the annual and quarterly reports. A December-quarter report from a calendar-year company is the 10-K, due 60, 75 or 90 days after Dec 31 depending on company size.
- **Large accelerated / accelerated filer:** SEC size classes (public float over $700M / $75-700M). They set how fast reports are due.
- **6-K / ADR:** a foreign company's US-listed shares; it files 6-Ks, has no 10-Q deadline, so both dates are required.
- **R3:** at most 1 Sell, at least 3 Buys, and Buys at least equal to Holds.
- **R4 (bear floor) / R4 proxy:** the lowest analyst Buy target has to sit above the call's breakeven. The proxy kills a name when the low target is already under or barely above the stock.
- **R5:** one contract's ask has to fit the conviction tier's share of reserve (3.5/5 = 10% of $539.11 = $0.539 a share).
- **R6 (reachability):** the move to breakeven can't be more than 1.5x the stock's median earnings-day move.
- **R7 (liquidity):** open interest at least 250 and a spread no wider than 25% of mid.
- **OI:** open interest, the number of contracts outstanding.
- **Mar19 / Apr16 / Feb19:** option expiries (Mar 19, Apr 16, Feb 19, 2027).
- **(f):** the tool's date is unverified (estimated from the company's cadence).
- **Parked:** passes the free screen, but no expiry that clears R2 has open interest yet; recheck when it builds.
