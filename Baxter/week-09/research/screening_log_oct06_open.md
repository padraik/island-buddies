# Screening Log: Tue Oct 6, 2026, 9:37am ET run (VM, OPEN slot)

**Source:** the research queue as the Oct 5 WRAP left it ("Tuesday OPEN, first ten minutes" block). DO run: 3 new chains (REZI, FWRG, TREE), 2 requotes (COUR, ADTN), 2 web searches + 1 extended search on COUR, and the COUR research doc (`research_COUR.md`).

**Rule 5 line:** the $290.54 settled overnight. Spendable = cash $741.32 - unsettled $0.00 = **$741.32**. 3.5/5 line **$0.741**; 4/5 line $1.00 (transitional lock); screen line $1.00.

**Quotes are 9:38-9:41am ET, inside the first ten minutes.** Opening option spreads were wide everywhere, so prior closes are listed next to every live quote and no kill rests on the opening ask alone.

## Funnel

| Stage | Names | Tool |
|---|---|---|
| Queue in | 7 worked (COUR, PCT, CWH, ADTN, REZI, FWRG, TREE) | research_queue.md |
| Ratings refresh | 7. **COUR low target $6.50 -> $6.00.** All others unchanged. | get_equity_analyst_ratings |
| Earnings date | COUR still Oct 22 PM, `verified: false` | get_earnings_results |
| Chains (new) | 3: REZI, FWRG, TREE | get_option_instruments + get_option_quotes |
| Requotes | 2: COUR $5C, ADTN $7C | get_option_quotes |
| Killed | 2: FWRG, TREE | |
| Alive | COUR (doc written, entry blocked), REZI ($22.5C unpriced), ADTN, PCT, CWH | |

## Chains

| Ticker | Stock | Strike Nov20 | Live bid/ask | Prior close | BE at ask | Max BE (R6) | Verdict |
|---|---|---|---|---|---|---|---|
| FWRG | $10.53 | $10C | 0.85 / 1.60 | 1.23 | $11.60 | $11.61 | **KILLED, R5 + R6.** Strikes are 2.5-wide: no $11C. The $10C's prior close ($1.23) and live mid ($1.225) are both well over $0.74. The $12.5C has a BE above $12.50 > $11.61 at any price. |
| TREE | $24.59 | $30C | 0.35 / 1.35 | 1.23 | $31.35 | $31.86 | **KILLED, R5 (+R6 above $30).** No $27.5C (strikes 25/30/35). The $30C passes R6 but its prior close $1.23 and live mid $0.85 are over $0.74. The $35C fails R6 (BE > $35). The $25C is 2.00 / 3.20. Oct 16 expiry is before the Oct 29 print. |
| REZI | $18.60 | $20C | 0.60 / 1.75 | 1.03 | $21.75 | $23.17 | $20C fails R5 (prior close $1.03, mid $1.175). |
| REZI | | $22.5C | no bid / 2.55 | **0.01 (phantom)** | | $23.17 | **UNPRICED, alive.** A $0.01 close next to a $1.03 $20C is impossible (TRMB-style phantom); not acted on. To pass R6 the $22.5C needs an ask <= **$0.67** (BE $23.17); R5 needs <= $0.74. Requote at MIDDAY once makers post a bid. OI 76. |
| COUR | $5.105 | $5C | 0.40 / 0.75 | 0.65 | $5.75 | $6.24 | **ALIVE, R5 one cent over at the ask** ($0.75 vs $0.741). Doc written. |
| ADTN | $7.19 | $7C | 0.60 / 1.20 | 0.85 | $8.20 | $8.26 | Alive, R5 fails (prior close $0.85 > $0.74). |

## COUR research (this run)

- **Range:** 0.090 (52w $4.5305 Sep 29 2026 to $11.1104 Oct 6 2025). The high rolls off tomorrow.
- **Rule 4 change:** low target $6.50 -> **$6.00**. BE at $0.74 is $5.74: margin $0.26 (4.5%). Who cut it: not identified.
- **Date:** no Q3 announcement found. Q2's date was announced Jul 15 for Jul 29; expect Q3's around Oct 8.
- **Decline category:** fundamental (demand, retention, Udemy integration costs: Q2 net loss $80.4M, FCF -$32.6M). Synergies ahead of schedule, FY outlook raised at Q2, six straight EPS beats; last four prints fell anyway.
- **Doc:** `research_COUR.md`, 3.5/5, 1 contract, Five-Baxter + EXIT PLAN written. Entry blocked on ask <= $0.74 and a company-confirmed date.

## GLOSSARY

- **R1-R6:** the six Iron Rules for calls (binder Tab 1): range, earnings, ratings, bear floor, chain affordability, reachability.
- **Max BE (R6):** the highest breakeven a contract can have and still pass Rule 6 (stock price x (1 + 1.5 x median earnings move)).
- **Phantom quote:** a price that can't be real against its neighbors (here a $0.01 close on a strike next to a $1.03 one). Never acted on.
- **Prior close:** the option's official closing price yesterday, used to sanity-check wide opening quotes.
- **Bid/ask:** what buyers will pay / sellers will take right now.
- **OI:** open interest, contracts outstanding.
- **Verified:** the company itself announced the earnings date.
