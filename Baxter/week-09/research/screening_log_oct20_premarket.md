# Screening log, Tue Oct 20, PREMARKET (8:30am ET): PREPARED

*Market closed. Free tools only (pre-market quotes, ratings, earnings, SEC index) plus 2 searches (ALGM floor, COUR news) and one EDGAR fetch (FLUT 8-K, `flut_8k_oct20.md`). No chains pulled live: option quotes below are Monday's close.*

## Held: COUR $5C Nov20

| Check | Result |
|---|---|
| Quote (Mon close) | 0.40 / 0.50, OI 3,235, IV 76.2% |
| Stock | $5.00 close; pre-market 4.72 / 5.53, last overnight print $5.00 |
| Q3 | Thu Oct 29 PM, `verified: true`, `actual: null` (LY Oct 23 PM) |
| Rule 4 | 8/4/0, low **$6.00** vs BE $5.65: holds |
| SEC | nothing since the two Oct 2 Form 4s |
| News search | nothing new; aggregators still echo a stale Oct 22 date, superseded by Coursera's own release |

## Queue: pre-market + ratings re-pull

| # | Name | Close | Pre-mkt | Ratings (B/H/S, low) | Moved overnight | SEC since Oct 16 | Note for OPEN |
|---|---|---|---|---|---|---|---|
| 1 | CLS | $300.35 | **$293.30** (-2.3%) | 25/0/0, $375 | -- | none | R1 easier (line ~$302). R6 at the close ask 27.20: BE $337.20 = +15.0% from $293.30 vs 17.36% cap: pass. $375 owner still unknown. **Kill Thu Oct 22** |
| 2 | ALGM | $33.17 | **$32.20** (-2.9%) | 14/1/0, $40 | -- | none | Floor search: the $40 has two owners, **UBS (Buy, 38 -> 40)** and **Mizuho (Outperform, 37 -> 40)**, both undated in the results. R6 at the close ask 3.70: BE $36.20 = +12.4% from $32.20 vs 10.5% cap. **Fails unless the ask falls with the stock** (delta 0.59 says ~3.13, BE ~$35.63, +10.6%: still a hair over). **Kill Mon Oct 26** |
| 3 | FLUT | $77.38 | $77.41 | 27/9/1, **$84** | **low $85 -> $84** | **8-K Oct 20** (UK&I restructuring, up to 1,400 jobs, $80-90M charges already in guidance; no earnings date) | Dec ask now has to be **<= $9.00** (was $9.95); last ask 10.50 |
| 4 | NRG | $99.38 | $99.38 | 16/4/0, $131 | -- | none | R6 at the live ask; floor cutter still unknown |
| 5 | NXT | $79.70 | $78.96 | 27/4/0, $101 | -- | none | floor undated. **Kill Oct 26** |
| 6 | RIOT | $13.97 | $13.54 (-3.1%) | 24/1/0, **$19** | **low $22 -> $19** | none | Someone cut. Still well over any Nov20 BE, but a fresh cut is the CCL/NKE/BSX pattern: find who. **Kill Oct 27** |
| 7 | TTWO | $204.92 | $206.09 | 29/1/1, $270 (stamp Aug 7) | -- | Form 4 Oct 16 | stamp still stale |
| 8 | PAAS | $44.43 | $44.11 | 6/2/0, $51 | -- | none | R1 re-check at OPEN |
| 9 | AA | $41.67 | $41.15 | 14/4/1, $48 | -- | 425 Oct 16 (business-combination communication) | **M&A flag:** a Rule 425 filing means a deal is in play. Calls flag (Tab: Unified Screen): deal price may cap upside. Read the 425 at MIDDAY before the Mar19 chain |
| 10 | BAC | $50.39 | $50.33 | 23/5/0, $55 | -- | 424B5 + Form 4s (routine) | Mar19 chain + R6 at MIDDAY |
| 11 | PLD | $124.09 | $123.80 | 13/5/0, $136 | -- | (not checked, outside top 10) | Mar19 chain + R6 at MIDDAY |

**Watch line:** ONDS $5.88 pre-market (-3.0%), BTBT $0.87, CLSK $8.22. None revived.
**Paper:** MSTR $134.00 pre-market (Nov20 $120C paper, BE $142.05; R1 holding). LVS $38.01 close, ramp sell **today 3:35pm**.

## Moved this run

0 killed, 0 advanced. Floor facts moved on 3 names (ALGM owners found, FLUT low -$1, RIOT low -$3). AA picked up an M&A flag. Every name has its next check written into the OPEN plan in `research_queue.md`.

## GLOSSARY

- **R1-R7:** the Iron Rules in binder Tab 1. R1 range position, R2 earnings before expiry, R3 analyst consensus, R4 bear floor (lowest Buy target above breakeven), R5 price cap, R6 reachability (needed move vs 1.5x median print move), R7 liquidity (OI >= 250, spread <= 25% of mid).
- **BE (breakeven):** strike + premium paid.
- **Delta:** how much the option's price moves per $1 in the stock.
- **Floor-dating gate (Tab 6):** a bear floor only counts if it was published within 60 days and after the decline.
- **Rule 425 filing:** communications a company files about a pending merger or acquisition.
- **424B5:** a prospectus supplement for a securities offering (routine for big banks issuing notes).
- **Kill date:** the last day a name can still get a doc and an entry with room for its own ramp sell.
- **Paper:** tracked in `paper_book.md`, no money moves.
