# Screening log: Thu Oct 8, PREMARKET (8:30am ET)

*PREMARKET is a prepare slot: no chains, no orders. This batch is date checks on the six docs, overnight filings, ratings on all 19 queue names, and pre-market quotes recomputed against each doc's max-price formula. Ratings pulled live this run (`get_equity_analyst_ratings`) are unchanged from Oct 7 on all 19 names (TME still last updated Aug 12).*

| Ticker | Direction | Check | Result | Stage after |
|---|---|---|---|---|
| COUR | CALLS | Q3 date + filings | Tool Oct 22 PM, `verified: false` (last year Oct 23 PM). No SEC filing since Oct 6. One web search: an aggregator line says Oct 26 PM; no Coursera press release found. Aggregators were split Oct 22 / Oct 26 yesterday too, so nothing new. Pre-market bid/ask 4.50 / 5.59 (no real book); last 5.11, flat. | Doc complete, date gate shut |
| ONDS | CALLS | Q3 date + filings | Tool Nov 12 AM, `verified: false` (last year Nov 13 AM). No filing since Oct 6. Pre-market 7.07 (close 7.19, -1.7%). Max price = 7.07 x 1.2089 - 8.00 = **$0.547**: the Nov20 $8C (Oct 7 close 0.45 / 0.49) still passes at the ask; the Dec18 $8C (0.64 / 0.71) **fails R6 at this price**. | Doc complete, date gate shut |
| QUBT | CALLS | Q3 date + filings | Tool Nov 13 PM, `verified: false` (last year Nov 14 PM). No filing since Oct 6. Pre-market 7.56 (close 7.62). Max price = 7.56 x 1.1388 - 8.00 = **$0.609**: Oct 7 close 0.51 / 0.64 passes at mid only. | Doc complete, date gate shut |
| WRD | CALLS | Q3 date + filings | Tool Nov 23 AM, `verified: false` (last year Nov 24 AM). 6-K Oct 7: `get_sec_filing` returned 404; read on EDGAR (accession 0001104659-26-114214, EX-99.1): HKEX "Monthly Return ... on Movements in Securities" for September: "Balance at close of the month 932,053,942" Class A shares; "Total funds raised during the month from exercise of options: USD 262,540.92". Routine, not thesis-moving. **Pre-market 4.75 (close 4.96, -4.2%)**, no dated headline found. Max price = 4.75 x 1.1397 - 5.00 = **$0.414**: the Jan15 $5C (Oct 7 0.55 / 0.75) **fails R6 even at the bid** if this holds at the open. | Doc complete, blocked (date + floor ages out Oct 13 / Oct 18; now R6 at pre-market price) |
| BRSL | CALLS | Q3 date + filings | Tool Nov 3 AM, `verified: false` (last year Nov 4 AM). No filing. Last 9.99 (after-hours Oct 7); max price = 9.99 x 1.1101 - 11.00 = **$0.09**: the $11C (0.10 / 0.20) fails R6 at the bid. | Doc complete, blocked |
| TME | CALLS | Q3 date + floor | Tool Nov 11 AM, `verified: false` (last year Nov 12 AM). No filing since Oct 1. Floor search: newest Buy-side action found is Mizuho Outperform $15 (Aug); the Bernstein $13 Outperform hit is dated Nov 13, 2024 (stale). **Floor cluster ages out Sun Oct 11** with nothing to replace it. Pre-market 7.91. | Doc complete, blocked |
| SERV | CALLS | Floor clock | Dated floor (Oppenheimer Aug 7, Guggenheim Aug 10) **goes stale after Fri Oct 9**. Pre-market 4.56 (close 4.66): fails R6 at the ask already (it was failing at $4.59-4.77). | Chain passed at the ask, floor expiring |

**Pre-market quotes (12:30 UTC):** COUR 5.11, QUBT 7.56, ONDS 7.07, WRD 4.75, BRSL 9.99 (AH), TME 7.91, OBDC 9.96, GAU 1.99, SERV 4.56, FRMI 3.96, ADTN 7.68, FUBO 9.22, FINV 2.94, TDUP 2.20, MLCO 4.17, PCT 3.79, ENVX 2.54, BXMT 11.07, CWH 4.47. Thin pre-market books; OPEN requotes before anything.

**Kills this batch:** none outright. WRD and ONDS-Dec18 fail R6 *at the pre-market price*; OPEN re-checks them on the live tape before marking either.

## GLOSSARY
- **R4 / bear floor:** the lowest Buy-rated analyst target must sit above the call's breakeven (strike + premium).
- **R6 / reachability:** the move to breakeven must be no more than 1.5x the stock's median earnings-day move. Each doc turns that into a max option price: stock x (1 + cap) - strike.
- **Dated floor (Tab 6):** a target counts only if it was published within 60 days and after the stock's decline.
- **verified: false:** the earnings date in the tool is estimated from the company's cadence, not announced by the company.
- **6-K:** a foreign issuer's current report (the 8-K equivalent). **EX-99.1:** the main exhibit attached to it.
- **HKEX monthly return:** a Hong Kong-listing filing reporting the month's share count changes; routine.
