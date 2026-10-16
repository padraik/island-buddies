# Screening log, Fri Oct 16, 2026, 6:00pm ET (EVENING 1, VM)

DO slot: up to 25 names through the funnel. Market closed; all quotes are Friday's 3:59-4:00pm closing book (stock after-hours prints noted only where they matter). Three parts: (1) the floor searches the WRAP queued for tonight, (2) a fresh scanner pass (EVENING 3's refill job, started early since part 1 finished fast), (3) ten names from that pass taken to the chain.

## Part 1: queue floor searches (one web search each) + re-quotes

| Ticker | Contract | Stock (close) | Bid / ask | BE / needs | R6 cap | Search result | Verdict |
|---|---|---|---|---|---|---|---|
| COUR (held) | Nov20 $5C (real) | $4.945 | 0.40 / 0.65 | $5.65 BE (entry) | | "Coursera to announce Q3 2026 results Oct 29": no Coursera release or IR page in results; the one aggregator answer says Oct 26 PM (the stale date the tool dropped Oct 15) | Oct 29 still single-source (tool `verified: true`); **Wed Oct 21 3:35pm fallback stays** |
| RIOT | Nov20 $13C (paper) | $13.735 | 1.92 / 2.13 | $15.13 / +10.2% | 10.69% | Newest dated actions: MS $43 (Aug 13), JPM $22 (Aug 17), KBW $35 (Jul 28). Nothing after Sep 15. JPM $22 is 60 days old today, ages out Monday | PARK, floor gate holds |
| NRG | Dec18 $105C (paper) | $103.745 | 8.60 / 9.20 | $114.20 / +10.1% | 13.42% | Newest dated: MS $162 (Aug 21), BMO $212 (Jul 28), BNP $221 (undated). Nothing in Sep/Oct; tool low $159 (record Oct 3) still unowned | PARK, floor gate holds |
| NXT | Nov20 $80C (paper) | $80.00 | 7.60 / 8.10 | $88.10 / +10.1% | 13.14% | Results are the 2025 raise cycle ($88-114 targets, Barclays/JPM/Wells/Citi) and a "$101.20 average target" story dated against a Sep 2025 prior. Nothing tied to the tool's Oct 13, 2026 record | PARK, floor gate holds |
| INSM | Nov20 $105C (paper) | $96.30 | 3.90 / 5.80 | $110.80 / +15.1% | 17.1% | Mizuho $165 found, but it's the Aug 13, **2025** action (pre-slide, >1 year old). Nothing dated after mid-Sep 2026 | PARK, floor gate holds; R7 re-test mid-day Monday (closing spread 39%) |
| PL | Jan15 $10C (paper) | $13.56 | 4.00 / 4.30 | $14.30 / +5.5% | | Only old actions (Citizens JMP $8->$11, DB $16->$17, Clear Street $14->$16, Citi init $19, MS $35), none dated in the results | PARK, floor gate; ratings 8/5/0 low $17 unchanged |
| TTWO | Dec18 $190C (paper) | $205.21 | 25.30 / 27.60 | $217.60 / +6.04% | 7.35% | Newest dated: JPM $310 (Aug 11), Roth $300 (Aug 10). Nothing after Aug 17; tool record still Aug 7 | PARK on R4 dating |
| PAAS | Jan15 $40C (paper) | $44.215 | 6.00 / 6.70 | | | no search (R1 only) | R1 ($44.215 vs $42.31 line) |
| ONDS | Dec18 $8C (real) | $6.045 | 0.27 / 0.32 | $8.32 / +37.6% | 20.89% | | watch line, R6 |
| BTBT | Jan15 $1C (real) | $0.96 | 0.15 / 0.18 | $1.18 / +22.9% | 8.23% | | watch line, R6 |

Ratings (free, all unchanged from WRAP): COUR 8/4/0 low $6; RIOT 24/1/0 $22; NRG 16/4/0 $159 (Oct 3); NXT 27/4/0 $101 (Oct 13); INSM 24/1/0 $165; PL 8/5/0 $17; TTWO 29/1/1 $270 (Aug 7); PAAS 6/2/0 $51; ONDS 11/0/0 $13; BTBT 6/0/0 $3.50.

## Part 2: fresh scan (prints Oct 30 - Dec 4, $25+, all caps >= $300M, 52w range pct < 0.25)

Saved scan `4bc59b84-cc60-4619-870c-359c2daae902`, retitled "Baxter Oct16 E1 refill Oct30-Dec4 prints" (new config version; the Oct 14 E3 config is preserved). Two price bands to stay under the 200-row cap: $32.77+ (200 rows) and $25-32.76 (42 rows) = **242 bottom-quartile names**.

- Liquidity pre-cut (Friday call volume >= 300): **107** left. The rest have almost no options trading and would die on R7 regardless.
- Rule 3 (<= 1 Sell, >= 3 Buys, Buys >= Holds), 93 rated: **60 pass**. Dead on R3 or no coverage include CRWV (3 Sells), NVO, CHTR, SEDG, CLX, FISV, LMND, AAP, DUOL, HUBS, CAR, TAP, SYM, FICO, DKS, LOW, INTU, PDD (2+ Sells), ASTS, MNDY, O, ZTS, BLSH, Z, PEG (Holds > Buys), INOD, BHF, AMSC, TDS (no coverage).
- R4 proxy (low target / price): 28 names at >= 1.15. Of those, 18 were already chained and killed earlier this week or last on R7 / R6 / R2 (CELC, RAPP, HROW, DY, ESAB, LASR R7; STRL, ECHO, CRUS, FUTU, ALB, KTOS, BROS R6/R5; LEU, MTZ, FN R7/R6; FPS R2) or are stale (CCJ, ratings stamp 2021). Ten were never chained or have re-priced hard since their kill; they go to Part 3.

## Part 3: ten names to the chain

Rule 2: all ten print Nov 2-10, so Nov27 clears the 21-day test from the later of (tool, LY) dates, with the Nov 9 / Nov 14 10-Q deadlines >= 5 trading days before expiry. Where Nov27 strikes were thin or missing, Dec18. R6 base = median absolute one-day reaction over the last 4 prints (daily closes; pm prints close-to-next-close, am prints prior-close-to-close).

| Ticker | Stock | Pct | Ratings / low | Print (tool) | Last 4 reactions | Median / cap | Contract | Bid / ask, OI | BE (ask) / needs | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| KRMN | $34.69 | 0.041 | 15/0/0, $63 | Nov 5 PM (f), LY Nov 6 | -5.73 / -13.64 / +7.68 / +5.60 | 6.71% / 10.06% | Dec18 $35C | 4.00 / 5.20, OI 343 | $40.20 / +15.9% | **KILLED, R6** ($40C: OI 96, worse) |
| IMCR | $29.43 | 0.140 | 10/4/0, $34 | Nov 5 AM (f), LY Nov 6 | +2.58 / -4.51 / +6.55 / +3.63 | 4.07% / 6.11% | Dec18 $30C | 2.40 / 4.90, OI 9 | $34.90 / +18.6% | **KILLED, R6** (and R7: OI 9, spread 68%) |
| MP | $40.15 | 0.038 | 17/1/0, $53 | **Nov 5 PM (v)**, LY Nov 6 | +12.80 / -1.88 / -2.46 / +7.62 | 5.04% / 7.56% | Nov27 $41C | 2.98 / 3.35, OI 3 | $44.35 / +10.5% | **KILLED, R6** (and R7, OI 3) |
| IONQ | $31.27 | 0.094 | 13/3/0, $43 | Nov 4 PM (f), LY Nov 5 | +3.65 / +21.70 / -9.30 / -0.53 | 6.48% / 9.71% | Nov27 $32C | 2.82 / 3.20, OI 30 | $35.20 / +12.6% | **KILLED, R6** (and R7) |
| IREN | $27.00 | -0.042 | 18/5/0, $40 | Nov 5 PM (f), LY Nov 6 | -6.84 / +5.13 / +7.65 / -12.53 | 7.25% / 10.87% | Nov27 $27C | 3.55 / 4.05, OI 41 | $31.05 / +15.0% | **KILLED, R6** (and R7) |
| MDGL | $449.53 | 0.243 | 20/1/0, $543 | Nov 3 AM (f), LY Nov 4 | +7.83 / -11.11 / +7.42 / -9.83 | 8.83% / 13.25% | Dec18 $450C | 38.60 / 46.60, OI 12 | $496.60 / +10.5% | **KILLED, R7** (OI 12; passes R6 and R4: low $543 > BE) |
| VERA | $27.91 | 0.146 | 13/2/0, $34 | Nov 4 AM (f), LY Nov 5 | -1.03 / +1.61 / -1.95 / -4.08 | 1.78% / 2.67% | Dec18 $30C | 1.65 / 3.40, OI 568 | $33.40 / +19.7% | **KILLED, R6** |
| XENE | $33.47 | -0.045 | 18/1/0, $46 | Nov 2 PM (f), LY Nov 3 | -4.94 / -3.76 / +0.79 / -1.84 | 2.80% / 4.20% | Dec18 $35C | 1.20 / 3.50, OI 57 | $38.50 / +15.0% | **KILLED, R6** (and R7) |
| NKTR | $35.81 | 0.022 | 11/4/0, $50 | Nov 5 PM (f), LY Nov 6 | +1.54 / +4.11 / -1.78 / -3.82 | 2.80% / 4.20% | Dec18 $35C | 2.75 / 6.80, OI 0 | $41.80 / +16.7% | **KILLED, R6** (and R7) |
| RKLB | $50.84 | 0.118 | 21/4/0, $67 | Nov 9 PM (f), LY Nov 10 | -1.27 / -4.89 / +34.22 / -0.04 | 3.08% / 4.62% | Nov27 $51C | 4.80 / 5.55, OI 3 | $56.55 / +11.2% | **KILLED, R6** (same verdict as Oct 12 at $65.60) |

**What part 3 says:** the $25+ bottom quartile right now is mostly names that crashed on news (IREN -11%, IONQ -8.5%, RKLB -8% today alone), and their option premiums carry that fear: IVs of 63-103% price a 10-20% move into a month-long call, while their own earnings days have moved 2-9%. Rule 6 is doing exactly what it was ratified for. MDGL is the one name that clears the clock and the floor, and nobody trades its December options.

## Behind the queue (added tonight, not yet chained)

From the 60 R3 passers, the ones with a floor ratio 1.10-1.15 that have never been chained in Era 2, in order of floor freshness: **FLUT** (27/9/1, low $85 vs $75.31, ratings stamped today Oct 16), **KKR** (20/5/0, $97 vs $87.48, stamped Oct 13), **CENX** (6/1/0, $40 vs $35.08), **APTV** (18/4/0, $50 vs $44.21), **FIGR** (9/2/0, $30 vs $27.10), **BWXT** (16/5/0, $150 vs $136.50), **GFS** (14/9/1, $51 vs $46.50, stamped Oct 15), **SMG** (6/3/0, $60 vs $54.55, stamped Aug 6: dating risk), **VST** (22/1/1, $169 vs $151.06, stamped Aug 7: dating risk). Next for each: `get_earnings_results`, the 4-print R6 base, then the Nov27/Dec18 chain.

## GLOSSARY
- **R1-R7**: Iron Rules, binder Tab 1. R1 range percentile, R2 earnings before expiry, R3 analyst consensus, R4 bear floor, R5 affordability, R6 reachability (needed move <= 1.5x median earnings move), R7 liquidity (OI >= 250, spread <= 25% of mid).
- **Pct**: where the stock sits in its 52-week range (0 = at the low, 1 = at the high); negative means under the weekly-bar low.
- **BE**: breakeven = strike + ask.
- **Needs**: the stock move from Friday's close to BE.
- **Median / cap**: median absolute one-day earnings reaction over the last 4 prints, and 1.5x that (the most R6 allows).
- **(v) / (f)**: earnings date company-verified / forecast from cadence, per `get_earnings_results`.
- **LY**: last year's same-quarter report date.
- **Floor ratio / R4 proxy**: lowest Buy target divided by the stock price; a free pre-chain check that the floor sits well above any plausible breakeven.
- **Dated floor**: binder Tab 6: a Rule 4 target counts only if it's within 60 days and published after the stock's decline.
- **Paper / real**: paper-book candidate vs. a contract the real fund could afford.
- **Watch line**: names kept at the bottom of the queue, re-quoted once a day instead of every run.
