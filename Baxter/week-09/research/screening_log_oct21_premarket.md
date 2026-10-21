# Screening log, Wed Oct 21, PREMARKET (8:30am ET): PREPARED

*Market closed. Free tools only: pre-market quotes, ratings, earnings, SEC index. 3 searches (QUBT dated Buy, GLXY floor, COUR news). One EDGAR fetch covered three filings (MLYS 8-K, HSAI 6-K, BTDR 6-K), because `get_sec_filing` returned 404 on all three. No chains pulled live, so the option quotes below are Tuesday's close.*

## Held: COUR $5C Nov20

| Check | Result |
|---|---|
| Quote (Tue close) | 0.50 / 0.55, OI 3,234, IV 83.6%, delta 0.58 |
| Stock | $5.07 official close. Pre-market 4.94 / 5.65 (no real market), last overnight print $5.07 |
| Q3 | Thu Oct 29 PM, `verified: true`, `actual: null` (LY Oct 23 PM) |
| Rule 4 | 8/4/0, low **$6.00** vs BE $5.65: holds |
| SEC | index since Oct 15 empty |
| News search | nothing new (latest company item: CLO appointment Sep 21) |

Tab 4 checks 0 through f: none fire. Ramp sell Thu Oct 29 3:35pm ET.

## Queue: pre-market + ratings re-pull + SEC check (top 10)

| # | Name | Close | Pre-mkt | Ratings (B/H/S, low) | Moved overnight | SEC since Oct 19 | Note for OPEN |
|---|---|---|---|---|---|---|---|
| 1 | **QUBT** Dec18 $7C | $6.50 | **$6.63** (+2.0%), 6.62 / 6.65 | 5/2/0, $10 (Cantor Hold) | -- | none | **R6 line at $6.63 = $0.550** (at $6.62: $0.538). Tue close 0.47 / 0.52, OI 1,117. At the 0.52 ask, BE $7.52 = +13.4% from $6.63 vs the 13.875% cap: passes **if the regular session holds ~$6.62+ and the ask stays <= ~$0.54**. Search: no Buy newer than Ascendiant $32 (Aug 26). The others are older: Lake Street Buy $16 (Jul 6) and Rosenblatt Buy $22 (Jun 29). Both are still far above any BE, but both are past the 60-day limit. **Window closes Fri Oct 23 3:35pm** (Ascendiant ages out Sun Oct 25) |
| 2 | APH Nov20 $80C (paper-size) | $79.32 | $81.00 last, 79.99 / 83.43 (wide) | 22/2/0, $90 | -- | none | At $81.00 the R6 line is $5.92 vs the 4.30 close ask: would pass. Pre-market book is too wide to trust, re-check after 9:45. **Kill Fri Oct 23** |
| 3 | GLXY | $15.76 | **$16.39** (+4.0%) | 15/1/0, $24 | -- | none | Floor search: the $24 matches **Goldman Sachs, Feb 4 2026**, and a Nasdaq headline has Goldman at **Neutral**. Stale and probably not a Buy. Another aggregator shows a $26 low. **The floor is still undated.** Chain Nov20 at OPEN anyway (prints Tue Oct 27 AM, verified) |
| 4 | MIR | $15.24 | 13.94 / 15.50 (no market) | 10/1/0, $20 | -- | none | Nov20 chain at OPEN (prints Oct 27 PM, verified) |
| 5 | HSAI | $13.99 | **$13.55** (-3.1%) | 24/1/0, $19.42 | -- | **6-K Oct 20** | **Date company-confirmed:** board meeting Nov 10, earnings call **7:00am ET Tue Nov 10** (pre-market print). 6-K filer: both dates needed for R2 (tool Nov 10 AM + this release). Dec18 chain next |
| 6 | MLYS | $21.58 | 21.27 / 23.63 | 8/2/0, $29 | -- | **8-K Oct 19** (Item 5.02) + 2 Form 3s / 2 Form 4s Oct 20 | Two independent directors added (Peterson, Coats), board 7 -> 9. Standard grants. No financing, no clinical news. Dec18 chain next |
| 7 | LEGN | $19.01 | 17.51 / 19.68 | 12/5/0, $24 | -- | none | Dec18 chain |
| 8 | SARO | $21.43 | 21.44 / 23.77 | 13/3/0, $25 (stamp Oct 1) | -- | none | Dec18 chain; thin R4 room |
| 9 | BTDR Dec18 $9C (paper-size) | $7.84 | **$8.08** (+3.1%) | 13/1/0, $10 | -- | **6-K Oct 19** | September update: 1,355 BTC mined (+200% Y/Y). **AI-cloud backlog $0.9B -> ~$2.9B** (>70% of the 21.7MW A201 site committed, >$1.7B over 5 years). 200-acre land buy near Rockdale. No financing, no earnings date. BTC held fell to 47 (2,029 a year ago, unexplained). At the 0.95 close ask, BE $9.95 = +23.1% from $8.08. Print table still needed |
| 10 | TTWO | $206.70 | $206.70 | 29/1/1, $270 (stamp Aug 7) | -- | none | stamp still stale |

**Watch line:** ONDS $6.19 pre-market (+1.5%, line ~$6.90), BTBT $0.94 (+4.4%, line ~$1.10), CLSK $8.70 (+3.2%, line ~$9.20). None revived. Crypto names are bid pre-market across the board (GLXY, BTDR, BTBT, CLSK).

## Filings read (EDGAR fallback)

- **MLYS 8-K** (Oct 19, Items 5.02 / 9.01), https://www.sec.gov/Archives/edgar/data/1933414/000193341426000125/mlys-20261016.htm: "appointed Kristine Peterson and Lonnel Coats to the Board effective as of October 19, 2026, increasing the size of the Board from seven to nine directors". Each got options on 16,600 shares and 12,400 RSUs. Nothing thesis-level.
- **HSAI 6-K** (Oct 20, EX-99.1 board meeting notice), https://www.sec.gov/Archives/edgar/data/1861737/000110465926117122/tm2627914d1_ex99-1.htm: "The Company's management will host an earnings conference call at 7:00 AM (U.S. Eastern Time)/8:00 PM (Beijing/Hong Kong Time) on Tuesday, November 10, 2026."
- **BTDR 6-K** (Oct 19, EX-99.1 September operations update), https://www.sec.gov/Archives/edgar/data/1899123/000121390026110703/ea030767901ex99-1.htm: "Bitdeer AI announced offtake commitments covering more than 70% of our ~21.7MW A201 data center in Johor Bahru, generating >$1.7 billion..." Backlog ~$2.9B (was $0.9B in August). Infrastructure updates move to quarterly.

## Moved this run

0 killed, 0 advanced. One fact moved on each of 4 names: QUBT's R6 line rose to $0.55 pre-market, HSAI's date is company-confirmed, BTDR's AI backlog roughly tripled, and GLXY's $24 low turned out to be Goldman's Feb 4 target (stale, likely Neutral). Every name has its next check in the OPEN plan in `research_queue.md` (private desk).

## GLOSSARY

- **R1-R7:** the Iron Rules in binder Tab 1. R1 range position, R2 earnings before expiry, R3 analyst consensus, R4 bear floor (lowest Buy target above breakeven), R5 price cap, R6 reachability (needed move vs 1.5x median print move), R7 liquidity (OI >= 250, spread <= 25% of mid).
- **BE (breakeven):** strike + premium paid.
- **R6 line:** the highest ask that still passes Rule 6 at a given stock price. For QUBT Dec18 $7C: stock x 1.13875 - 7.00.
- **Floor-dating gate (Tab 6):** a bear floor only counts if it was published within 60 days and after the decline.
- **6-K:** the current report a foreign private issuer files (its version of an 8-K).
- **Item 5.02:** the 8-K item for director or officer changes.
- **Backlog:** contracted future revenue not yet earned.
- **Kill date:** the last day a name can still get a doc and an entry with room for its own ramp sell.
- **Paper:** tracked in `paper_book.md`, no money moves.
