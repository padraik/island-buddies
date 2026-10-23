# PROPOSAL: should the paper book apply Tab 3's correlated-position cap?

*Thu Oct 22, 2026, VM EVENING 2. Written for a local session to decide. Nothing changes until then; the paper book keeps running as it is.*

## Why it came up

Thursday's WRAP marked the paper book **-$2,350 on the day**, its worst yet. Four of the five worst lines were AVGO (-$1,180), MSTR (-$610), APP (-$370) and NRG (-$220): names that sold off together on one AI/power/crypto risk-off day. The real fund has a rule for exactly this (binder Tab 3: total reserve in plays sharing one primary macro driver may not exceed **35%**). The paper book doesn't apply it, because it has no reserve. If the paper book is the lab for the real rules (Oct 9 order), it's testing them without one of them.

## The numbers tonight (open paper, at entry cost)

| Driver bucket | Positions | Cost | Share of $17,385 open |
|---|---|---|---|
| AI capex / power demand | AVGO $6,090, FSLR $1,650, NRG $710 | $8,450 | **48.6%** |
| ... plus AI-adjacent adtech | + APP $2,740 | $11,190 | 64.4% |
| Bitcoin | MSTR $2,205 | $2,205 | 12.7% |
| Consumer | CAVA $755, BURL $1,860 | $2,615 | 15.0% |
| China internet | BABA $855 | $855 | 4.9% |
| Telecom | TMUS $520 | $520 | 3.0% |

On any reading, the biggest bucket is already over 35%. APH (blocked on R1 tonight anyway) would have pushed it higher.

## Options

**A. Leave it.** The paper book tests R1-R7 on liquid names, one contract each, and nothing else. Simple, and the sample grows fastest. The cost is that a correlated day like Thursday reads as "the rules lost $2,350" when it's really one theme losing.

**B. Apply 35% of open paper deployed, at entry only.** Tag each paper entry with one primary driver when it's logged. A new entry whose bucket would go over 35% of open paper (after adding it) doesn't get logged; the doc still gets written and the name goes in the log as "blocked by correlated cap." No forced exits on what's already open. Easy to run from the tables that already exist.

**C. Give the paper book a notional reserve** (say $20,000) and apply Tab 3 sizing and the 35% cap to it. This is the closest copy of the real rules. But at one contract per entry, AVGO alone ($6,090) is 30% of that, so sizing would push the book away from big-ticket names. That's a bigger change than the question needs.

## Recommendation

**B.** It's the smallest change that makes the paper book obey the same diversification rule real money does, it uses data already on the page, and it leaves the existing positions alone so their results still count. WRAP would also print the bucket table once a day so the concentration is visible.

What the sweep could later learn from it: whether blocked entries would have helped or hurt (keep logging them with "would have" P&L, the same way passes.md works).

## Open questions for Michael

1. Is "primary driver" Baxter's call at entry (written in the doc), or should there be a fixed list of buckets?
2. Does APP count as AI capex? (It moved with the group Thursday; its business is ad-tech.)
3. Should the same 35% apply to the real fund's two-to-five positions? It already does on paper (Tab 3); in practice the real book has never had two names on one driver.

## GLOSSARY
- **Tab 3 correlated position cap:** total reserve deployed to plays sharing one primary macro driver may not exceed 35%.
- **Paper book:** tracked-only positions, one contract each, entered at the ask and exited at the bid, no money.
- **Open paper deployed:** sum of entry costs of open paper positions ($17,385 tonight).
- **Driver bucket:** the shared macro force that would move several positions together (AI capex, bitcoin, rates, consumer spending).
