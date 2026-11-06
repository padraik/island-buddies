# FRMI Form 4 and two Form 144s, Nov 4-5, 2026: the co-founder sold 5 million shares on Thursday

*Pulled from SEC EDGAR by the VM EVENING 3 run on Thu Nov 5 at ~10:05pm ET. Robinhood's `get_sec_filing_index` listed the Form 4 (filing_id cd0d7c61-d8cf-492b-8828-fe46edea1bdd, filed Nov 5), but `get_sec_filing` returned 404 ("No readable text for this filing"). The tool index did not list the two 144s at all, the same miss as Nov 3. Source: EDGAR submissions for CIK 2071778. Form 4 accession 0000905148-26-004667; Form 144s 0001958244-26-000694 (Nov 4) and 0001958244-26-000701 (Nov 5).*

## What they are

- **Form 4 (filed Nov 5):** reporting persons Toby R. Neugebauer and the Melissa A. Neugebauer 2020 Trust. Both are marked 10% owners and neither is marked a director. Four open-market sales (code S) of common stock.
- **Form 144 (filed Nov 4):** notice to sell **94,000 shares** (aggregate market value **$171,080**) through Goldman Sachs, approx. sale date 11/04/2026. The seller is the Trust.
- **Form 144 (filed Nov 5):** notice to sell **5,000,000 shares** (aggregate market value **$7,650,000**) through Goldman Sachs, approx. sale date 11/05/2026. Shares outstanding are listed as 641,259,703.

## The transactions (Form 4, verbatim values)

| Date | Shares | Weighted avg price | Price range (footnote) | Shares held after |
|---|---|---|---|---|
| Nov 3 | 1,281,900 | $2.0391 | n/a | 89,907,010 |
| Nov 3 | 1,281,900 | $2.0391 | n/a | 42,077,276 (Vicksburg Investments Management LLC) |
| Nov 4 | 94,000 | $1.9948 | "$1.99 to $2.005, inclusive" | 89,813,010 |
| **Nov 5** | **5,000,000** | **$1.5206** | **"$1.44 to $1.59, inclusive"** | **84,813,010** |

> "These securities are directly held by the Trust. Toby R. Neugebauer ... is the investment trustee of the Trust and may be deemed to beneficially own the securities held by the Trust."

Not sure how the two Nov 3 rows split between the Trust and Vicksburg, since the parser pulled both at the same count and price. The Nov 3 144 (read Nov 4) covered 2,563,800 shares, which is 2 x 1,281,900, so the Nov 3 rows are that notice being executed.

## Why it matters for the position (FRMI $2.5C Dec18, BE $3.15)

Facts for Baxter to weigh, not a verdict:
- **This is not an exit trigger under the doc's EXIT PLAN.** Rule 4 holds (tool low $6 vs BE $3.15, 6/2/0). The forced exits are Rule 4, a lease termination, the ramp date, or Michael. Insider selling isn't one of them, and nothing here touches the lease or Project Matador.
- **It corrects the record on Thursday.** WRAP and EVENING 1 called FRMI's -16.5% "market-wide, no FRMI news." The market fell (SPY -4.4%), but the co-founder also sold 5.0M shares into it at $1.44-1.59, roughly the whole day's range. That's a named seller, not just beta.
- **The overhang is still big.** He still holds ~84.8M shares through the Trust plus ~42M through Vicksburg. Each 144 has been filed and executed on the same day, so a new one can show up any morning with no warning.
- **Worth at the bid:** $5 (0.05 / 0.10). Selling now would recover about $5 of the $65 paid. Holding costs nothing extra; the case for holding is the Thu Nov 12 AM print and the ramp into it.
- Next things to watch on EDGAR (the tool index misses 144s): more 144s and Form 4s, a Schedule 13D/A, and a lawsuit 8-K on the nomination-agreement dispute.

## GLOSSARY

- **Form 4:** an insider's report of a completed trade, filed within 2 business days.
- **Form 144:** notice an affiliate files before selling restricted or control stock. It's a plan to sell. The Form 4 shows the sale actually happened.
- **10% owner:** a holder of 10% or more of a class of shares; they must file Forms 3, 4, 5.
- **Code S:** an open-market or private sale.
- **Weighted average price:** the average fill price across many trades, weighted by size.
- **Overhang:** a large block of stock a known holder may sell, which tends to weigh on the price.
- **BE:** breakeven, strike plus premium paid.
