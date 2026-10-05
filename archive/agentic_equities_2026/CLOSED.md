# Agentic Equities: closed

Retired Oct 5, 2026. Patrick shut it down: underperforming and no time for the continuous-improvement loop it needed. Last firing Fri Oct 2, 3:35pm ET: total value $363.14 against $400.00 deposited (-9.22%). Its 5 remaining stock positions were sold at the Oct 5 open, and the account became the Island Fund, run by Baxter.

What it taught, for whoever builds the next one:
- The scanner's instrument-type filter needs the literal wire values `STOCK`/`ETF`; every other spelling silently matches nothing (two weeks of zero trades).
- The scanner's relative-volume metric compares partial-day to full-day volume, so it structurally penalizes morning runs. Never make it a hard filter.
- A deposit looks exactly like a gain unless a human-kept capital ledger says otherwise.
- Headless claude-code on the VM broke three separate ways (workspace trust, a failed native install, expired auth). Broker-side stops kept positions safe each time; everything else silently stopped. Heartbeats aren't optional.
- At $300-400, whole-share sizing dominates everything: most candidates were unaffordable at one share.
