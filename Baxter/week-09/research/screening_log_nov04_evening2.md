# Screening log: Wed Nov 4, 2026, EVENING 2 (8:00pm ET, VM)

*Reserve (spendable) $539.11. R5 3.5/5 line $0.539. Closing quotes (3:59pm) unless noted; stock after hours ~8:00pm. Source: the EVENING 1 queue (NIO, CRDO, CIEN, NOC, RMBS). EVENING 2's job is docs for names past the chain stage: only CRDO qualified (paper). R6 medians come from Robinhood daily closes around each `get_earnings_results` print date (AM reporters: prior close to print-day close; PM reporters: print-day close to next close).*

| # | Ticker | Direction | Price | R1 | Next print (tool); LY | R/H/S | Verdict |
|---|--------|-----------|-------|----|-----------------------|-------|---------|
| 1 | NIO | CALLS (real) | 3.30 close, AH 3.29 | ~0.03 | Tue Nov 24 AM (f); LY Tue Nov 25 AM | 16/7/1 | **GATED (R4 dating).** $3C Dec18 0.38 / 0.45 (OI 617, spread 16.9%). R6 max ask at $3.29 = 1.0536 x 3.29 - 3.00 = $0.466, so 0.45 passes; R5 passes (0.45 vs $0.539). Tool low $3.7131, stamp still Sep 1. Two searches: Citi $8.90 (from $7) and Morgan Stanley $6.50 (from $5.90, Tim Hsiao): **both undated, and the MS note is a 2025 note** (it trims the *2025* delivery forecast to 330k). Not counted. Gate holds. |
| 2 | CRDO | CALLS (paper) | 136.50 close, AH 134.11 | 0.225 (AH 0.215) | Mon Nov 30 PM (f); LY Mon Dec 1 PM | 21/1/0 | **PAPER DOC WRITTEN, GATED (R4 dating).** `research_CRDO_paper.md`. Jan15 $130C 22.70 / 29.00, OI 435, spread 24.4%. R6 six prints 14.8 / 7.4 / 10.1 / 14.8 / 1.3 / 20.0%, median 12.46%, cap 18.68%; BE $159 needs +16.5% at the close, +18.6% at the AH price (on the line). Tool low $235; one search: nothing dated after Oct 12 2026. Meeting 4-1 to wait. |
| 3 | CIEN | CALLS (paper) | 272.24 close, AH 267.67 | 0.213 | Thu Dec 10 AM (f); LY Thu Dec 11 AM | 20/5/0 | **KILLED R6 + R7 (Jan15).** Six prints -12.9 / +23.3 / +9.3 / -12.9 / -13.7 / -10.4%, median 12.90%, cap 19.35%: BE must be <= $324.90. Jan15: $250C 42.30 / 49.50 OI 136 (R7), $260C 38.00 / 42.00 OI 68 (R7), $280C 33.70 / 37.40 OI 124 (R7), $290C 29.70 / 33.30 OI 75 (R7), $300C 27.10 / 29.20 OI 293 (R7 pass, 7.5%) but BE $329.20 needs +20.9% (R6). No Jan15 strike passes both. Feb19 not checked; it would cost more premium per strike, so R6 only gets harder at the liquid strikes. |
| 4 | NOC | CALLS (paper) | 525.35 close | 0.176 | Jan 26 2027 AM (f); LY Jan 27 2026 AM | 18/11/1 | **KILLED R4 proxy.** Tool low $430 is **18% under** the stock (stamp Oct 20). EVENING 1 advanced it; on the proxy's own definition (low more than ~8% *above* the stock) it should have been cut there. For the record: R6 median 4.57% on seven prints (cap 6.86%), and Q4 is a 10-K quarter (deadline ~Mar 1), so R2 would have needed Mar19. |
| 5 | RMBS | CALLS (paper) | 82.90 close | 0.035 | Feb 1 2027 PM (f); LY Feb 2 2026 PM | 8/2/1 | **KILLED R6 + R7.** No Mar19 expiry listed (chain: Nov20, Dec18, Jan15, Feb19, May21, ...). Feb19 fails R2 (Feb 2 + 21 = Feb 23). May21: $75C 19.40 / 22.00 OI 0, $80C 16.90 / 19.60 OI 3, $85C 14.70 / 17.20 OI 1, $90C 12.20 / 16.20 OI 15: R7 fails on every strike. R6: seven prints -5.7 / +13.9 / -8.7 / -13.4 / -21.3 / -9.0 / -1.6%, median 8.99%, cap 13.49%; even the $75C (BE $97.00 at the ask) needs +17.0%. |

**Holdings (fact check, not screening):** QUBT close $6.43 official (AH $6.36), FRMI $1.82 (AH $1.82), ACHR $4.12 (AH $4.15). Dates, ratings and SEC unchanged (FRMI newest filing is the Nov 4 8-K already read; QUBT and ACHR none).

**Tally:** 5 moved. 1 paper doc written and gated (CRDO). 1 real-money doc still gated (NIO). 3 killed (CIEN R6 + R7, NOC R4 proxy, RMBS R6 + R7). 0 advanced to a buyable doc. Not reached tonight: NVT / DOX floor dating (EVENING 3 or Saturday).

## GLOSSARY

- **R1:** (price - 52-week low) / (52-week high - 52-week low). <= 0.25 is the calls band.
- **R2:** expiry at least 21 days after the later of the tool date and last year's date, and the 10-Q/10-K deadline at least 5 trading days before expiry.
- **R/H/S:** Buy / Hold / Sell rating counts from `get_equity_analyst_ratings`.
- **R4 proxy:** screening shortcut: tool low target well above the stock (more than ~8%) before a contract is picked.
- **R6:** move to breakeven <= 1.5x the median absolute earnings reaction (last 4-8 prints).
- **R7:** open interest >= 250 and spread <= 25% of mid on the exact contract.
- **(f):** date estimated from cadence (`verified: false`).
- **AH:** after-hours trade.
- **Paper:** tracked in `paper_book.md`, no money moves.
