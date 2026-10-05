# CWH 8-K, Oct 5, 2026: the filing the VM couldn't read

*Pulled from SEC EDGAR by a local session on Oct 5 at ~12:30pm ET, because Robinhood's `get_sec_filing` kept returning 404 ("Filing content is not available") for filing_id d9d05b80-dee8-4b5c-9da8-8d3a4a9a4996. Same filing on EDGAR: accession 0001104659-26-113490, https://www.sec.gov/Archives/edgar/data/1669779/000110465926113490/tm2627004d1_8k.htm*

## What it is

Item 7.01 (Regulation FD disclosure). No exhibits. Not preliminary results, not a management change.

## The key sentence, verbatim

> "On October 5, 2026, Camping World Holdings, Inc. (the "Company") announced that, reflecting the operating trends and other factors described below, the Company now expects full-year 2026 Adjusted EBITDA to be below the low end of its previously communicated guidance range of $230 million to $270 million."

## The rest (summarized from the filing)

- **Guidance cut:** FY2026 Adjusted EBITDA now expected **below $230M** (prior range $230-270M). No new range given.
- **Why:** new and used unit sales softened sequentially from July through the quarter. "New vehicle front-end margins have remained under greater pressure than previously expected." Energy prices and interest rates cited as macro headwinds.
- **Cost actions:** accelerating the $100M SG&A savings program; $50M+ more in annualized headcount cuts; closing four dealerships (two planned to reopen later).
- **Financing:** exploring a refinancing of the existing term loan facility, possibly new term loans and senior secured debt, subject to market conditions and definitive documentation.

## Why it matters for the queue entry

This is the reason for Monday's ~13% drop. Facts for Baxter to weigh, not a verdict:
- A negative pre-announcement before the Oct 27 print. Some of the print's bad news is now out early.
- Analysts tend to cut targets after a guidance cut. The $6.00 low target behind the Rule 4 check was already undated (the newest dated targets found were $9 from Jul 31 and Aug 3). Expect Rule 3 and Rule 4 inputs to move this week. Re-pull `get_equity_analyst_ratings` before trusting either.
- Guidance cut + refinancing search reads like the decline-category question (a cyclical dip, or the business actually getting worse?). That's the call Baxter makes in the research doc.

## GLOSSARY

- **8-K:** a filing companies must make within a few days of a material event.
- **Item 7.01 / Regulation FD:** a disclosure made publicly so no investor hears it first.
- **Adjusted EBITDA:** earnings before interest, taxes, depreciation and amortization, with one-time items stripped out. Camping World's headline profit measure.
- **Pre-announcement:** a company telling the market its results will miss before the actual earnings date.
- **Term loan refinancing:** replacing existing debt with new debt, usually to push out maturities or change terms. Doing it while cutting guidance can mean tighter terms.
