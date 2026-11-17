# Screening log, Tue Nov 17 EVENING 1 (6:00pm ET)

*Session 1 of 3. Job (from the Nov 16 EVENING 3 and Nov 17 PREMARKET handoffs): (a) NIO after its Dec18 doc died on R2: write a new doc only if a listed expiry clears R2 AND the floor gate has a dated source, otherwise move it to passes.md Keep Watching, and quote the Nov 17 6-K from EDGAR; (b) date-stage band A's last six parks (NUVB, SOUN, WVE, DNN, CTMX, SANA); (c) start band B's unstaged parks, real-money size (cheapest) first. Nothing held. Spendable $715.96, so the 3.5/5 R5 line is $0.716/share. Prices: Tuesday Nov 17 close. 0 web searches. 25 names moved.*

## 1. NIO: to passes.md Keep Watching

- **6-K read from EDGAR** (acc. 0001104659-26-128778). Ex. 99.1: "The Company will publish its Q3 2026 Results on Tuesday, December 1, 2026," with the call at "7:00 a.m. U.S. Eastern Time on December 1, 2026." Write-up: `nio_6k_nov17.md`.
- Tool: Q3 **Dec 1 AM `verified: true`**, LY Nov 25 AM. Later + 21 = **Dec 22**.
- Chain lists Nov20, Nov27, Dec4, Dec11, Dec18, **Dec24, Dec31, Jan15**, Feb19... So Dec24, Dec31 and Jan15 all clear R2 (6-K filer: both dates present, no 10-Q test).
- Ratings 16/7/1, low **$3.6996**, high $8.8549, `updated_at` 2026-11-17 01:00Z. That's the same low as Saturday, so it's a record refresh, not a new target. **Floor gate shut.**
- Close $2.81 (+3.3%), AH $2.83.
- **Verdict: no doc.** A doc behind a shut gate is the thing the queue rule says not to write. NIO goes into passes.md as Keep Watching. Create New Pitch only if a Buy target dated after Nov 5 becomes the low. Stop Watching after the Mon Nov 30 3:35pm ramp line.

## 2. Band A's last six + 18 band B parks: R3, R4 proxy, dates, listed expiries

R3 = at least 3 Buys, Buys >= Holds, at most 1 Sell. R4 proxy = low target above Tuesday's close. Contract = the earliest *listed* expiry at least 21 days after the later of (tool date, LY date). Mar19 also needs a large-accelerated filer (10-K due Mar 1). Foreign filers need both dates and no deadline test.

| Ticker | Band | Close | B/H/S | Low (margin) | Q4 tool date | LY | Later | Listed (2027) | Contract | Ramp line* | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|---|
| NUVB | A | 3.915 | 12/1/0 | 7 (79%) | Mar 1 PM (f) | Mar 2 | Mar 2 | Jan15, Mar19, Jun17 | **Jun17** | Mon Mar 1 | STAGED. Mar19 fails on date (needs Mar 23) |
| SOUN | A | 3.055 | 7/1/0 | 5 (64%) | Feb 25 PM (f) | Feb 26 | Feb 26 | Jan15, Apr16 + weeklies | **Apr16** | Thu Feb 25 | STAGED |
| WVE | A | 2.84 | 20/1/0 | 8.37 (195%) | Feb 25 AM (f) | Feb 26 | Feb 26 | Jan15, Apr16, Jun17 | **Apr16** | Wed Feb 24 | STAGED |
| DNN | A | 1.90 | 15/0/0 | 3.50 (84%) | Mar 9 PM (f) | Mar 10 | Mar 10 | Jan15, Apr16 + weeklies | **Apr16** | Tue Mar 9 | STAGED. Canadian filer, both dates present |
| CTMX | A | 1.945 | 8/0/0 | 5 (157%) | Mar 15 AM (f) | Mar 16 | Mar 16 | Jan15, Feb19, May21 | **May21** | Fri Mar 12 | STAGED |
| SANA | A | 1.885 | 9/1/0 | 6 (218%) | Mar 2 PM (f) | Mar 3 | Mar 3 | Jan15, Apr16 | **Apr16** | Tue Mar 2 | STAGED |
| SBSW | B | 8.455 | 6/4/1 | 9.5959 (13%) | malformed rows (2027-02-25 `verified: true` labeled "2021 Q3"; no usable LY) | -- | -- | not pulled | -- | -- | **DATES UNUSABLE.** Foreign filer, both dates required. Re-pull Saturday; still unusable = R2 kill (MESO precedent) |
| VINP | B | 8.415 | 6/0/0 | 10.483 (25%) | Mar 3 PM (f) | Mar 4 | Mar 4 | Feb19, May21 | **May21** | Wed Mar 3 | STAGED. Foreign filer, both dates present |
| BKD | B | 8.805 | 6/0/0 | 12 (36%) | Feb 17 PM (f) | Feb 18 | Feb 18 | Jan15, Feb19, Apr16, Jun17 | **Apr16** | Wed Feb 17 | STAGED. No Mar19 listed |
| BSRT | B | 9.165 | 5/4/0 | 10.25 (12%) | **empty** | -- | -- | not pulled | -- | -- | **DATES UNUSABLE** (tool returned nothing). Re-pull Saturday |
| CAPR | B | 8.405 | 5/4/0 | 10.5 (25%) | Mar 11 PM (f) | Mar 12 | Mar 12 | Jan15, Mar19, Jun17 + weeklies | **Jun17** | Thu Mar 11 | STAGED. Mar19 fails on date (needs Apr 2) |
| OTF | B | 9.26 | 6/4/0 | 11 (19%) | Feb 17 PM (f) | Feb 18 | Feb 18 | **no option chain** | -- | -- | **KILLED: no listed options** |
| OFRM | B | 11.67 | 5/4/1 | 10 (-14%) | not pulled | | | | | | **KILLED R4 proxy** ($10 low under the $11.67 close; was $9.65 Saturday) |
| BRSL | B | 8.96 | 6/3/0 | 10.9 (22%) | Feb 23 AM (f) | Feb 24 | Feb 24 | Jan15, Apr16 | **Apr16** | Mon Feb 22 | STAGED. No Mar19 listed. Filer type to confirm at doc stage |
| EQX | B | 9.865 | 11/0/0 | 13.3329 (35%) | Mar 10 PM (f) | Feb 18 | Mar 10 | Jan15, Apr16 | **Apr16** | Thu Feb 18 | STAGED. Tool date is 3 weeks later than LY, so the ramp line sits on the earlier LY date until announced. Canadian filer |
| AFYA | B | 10.30 | 6/2/0 | 10.0289 (-3%) | not pulled | | | | | | **KILLED R4 proxy** (low under the close) |
| AEVA | B | 9.97 | 3/3/0 | 11 (10%) | Feb 25 PM (f) | Feb 26 | Feb 26 | Jan15, Apr16, Jun17 | **Apr16** | Thu Feb 25 | STAGED. Thin (3/3/0, 10%) |
| VCRE | B | 10.25 | 10/0/0 | 15 (46%) | **empty** | -- | -- | not pulled | -- | -- | **DATES UNUSABLE** (tool returned nothing). Re-pull Saturday |
| NMRK | B | 10.185 | 6/2/0 | 13 (28%) | Feb 24 AM (f) | Feb 25 | Feb 25 | Mar19, Jun17 | **Mar19 if LA, else Jun17** | Tue Feb 23 | STAGED. 1 day spare on Mar19 |
| EFC | B | 10.685 | 6/2/0 | 13 (22%) | Feb 24 PM (f) | Feb 25 | Feb 25 | Jan15, Apr16 | **Apr16** | Wed Feb 24 | STAGED. No Mar19 listed |
| STWD | B | 11.32 | 6/2/0 | 13 (15%) | Feb 24 AM (f) | Feb 25 | Feb 25 | Jan15, Mar19, May21, Jun17 ... | **Mar19** | Tue Feb 23 | STAGED. 1 day spare. Large-accelerated (multi-billion REIT); confirm on the 10-K cover at doc stage |
| JANX | B | 10.72 | 15/3/1 | 14 (31%) | Feb 25 PM (f) | Feb 26 | Feb 26 | Jan15, Feb19, May21 | **May21** | Thu Feb 25 | STAGED. No Mar19 listed |
| SLRC | B | 11.06 | 5/2/0 | 12.5 (13%) | Feb 23 PM (f) | Feb 24 | Feb 24 | Mar19, Jun17 | **Mar19 if LA, else Jun17** | Tue Feb 23 | STAGED. 2 days spare on Mar19 |
| RSI | B | 11.57 | 12/3/0 | 15 (30%) | Feb 16 PM (f) | Feb 17 | Feb 17 | Jan15, Apr16 | **Apr16** | Tue Feb 16 | STAGED. No Mar19 listed |

*Ramp line = the last trading run before the earliest of (tool date, LY date): same day for a PM print, the trading day before for an AM print, 3:35pm ET. It moves when the company announces.

**Band A is now fully staged.** Band B unstaged after tonight: FIGR, BVN, FLY, VCYT, BEAM, LINC, FPS, TECX, TYRA, BKV, RVLV, IMNM, EYE, BNL, LEGN, RCUS, EQPT, MLYS, HMY, CORZ, CDE, DEC, AG, LUNR, QXO, WULF, ARLO (27, the $11.9-25 end; see the Nov 14 log), plus bands C-D (paper size).

## 3. Watch line

- **AVGO (paper):** close $341.705 (+2.5%), **AH $350.49** (bid 349.50 / ask 350.75), above the $338.85-341.08 window on the after-hours print. R1 is out at that price. Floor stamp still Oct 27 (53/3/0, low $398.47). Nothing to do.
- **DY (paper watch):** close $220.84, AH $222.00. Still under the ~$225.50 line. 12/1/0, low $375.
- **Paper BABA:** ramp sell Wed Nov 18 3:35pm LASTCALL at the bid. Not re-quoted tonight.

## Tally

25 names moved: NIO to passes.md Keep Watching (6-K quoted). 24 December parks: **18 staged**, **3 killed** (OFRM and AFYA on the R4 proxy, OTF with no listed options), **3 dates unusable** (SBSW, BSRT, VCRE; Saturday re-pull). 0 advanced to a doc, 0 buyable. Web searches 0. EDGAR fetches 3 (index, 6-K, Ex. 99.1).

## Handed on

1. EVENING 2: no doc to write (nothing cleared the chain), so start EVENING 3's job early: stage the next 25 band B parks from the $11.9-25 end (FIGR through ARLO), list-checked.
2. Saturday: re-pull SBSW, BSRT, VCRE and MESO (unusable twice = R2 kill).
3. Filer status for the Mar19-conditional names at the doc stage: PHAT, PUMP, PCT, METC, NMRK, SLRC, STWD.
4. December chain pass (~Dec 12-15, once spring OI builds).

## GLOSSARY

- **Date-staging:** working out which option expiry a name's next earnings date allows under Rule 2, before spending a chain check.
- **Listed expiry:** an expiration that actually appears on the stock's option chain.
- **R2 / Rule 2:** the expiry must be at least 21 days after the later of the tool date and last year's date. US filers also need the filing deadline at least 5 trading days before expiry.
- **Large accelerated filer (LA):** $700M+ public float on the last day of Q2. Files its 10-K within 60 days (Mar 1).
- **R3:** at least 3 Buys, Buys at least equal to Holds, at most 1 Sell.
- **R4 proxy:** at screening, is the lowest analyst target above the stock price?
- **Floor gate:** the lowest Buy target has to be dated after the stock's slide to count as a floor.
- **6-K:** the form a foreign company uses to file its home-market announcements with the SEC.
- **(f):** `verified: false`, an estimated date.
- **Ramp sell / ramp line:** selling before the print into the pre-earnings premium; the line is the last run to do it.
- **Park:** passes the free screens and waits on a later check.
- **AH:** after-hours. **OI:** open interest.
- **Weeklies:** weekly expirations, a sign the options trade actively.
