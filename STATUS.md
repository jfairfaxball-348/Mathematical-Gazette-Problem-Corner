# Status

**As of:** 2026-10-05

## Overall

- Stage 1 — Scaffold / Bootstrap: **PASSED / COMPLETE**
- Stage 2 — Research: **CLOSED BY HUMAN OVERRIDE; ORDINARY GATE NOT PASSED**
- Stage 3 — Discovery: **PASSED / COMPLETE**
- Stage 4 — Prior-art / Novelty Audit: **UNLOCKED / READY, NOT STARTED**
- Stage 5 — Formalisation and Submission Package: **LOCKED**

Decision **D010** records the Stage-3 pass. No Stage-4 prior-art audit was performed in the Stage-3 session.

## Stage-2 limitation carried forward

The research catalogue remains at **23 structured, solution-reviewed Problem Corner records**, with known era imbalance and incomplete synthesis. D009 remains an exception to the Stage-2 gate, not evidence that the missing research was completed.

## Stage-3 outcome

The discovery programme substantially explored **31** candidate seeds.

Final disposition:
- **10** frozen serious candidates;
- **17** rejected;
- **4** merged as variants / same-family formulations.

The serious set is stored in `candidates/serious-candidates.jsonl`; every record is marked `FROZEN_FOR_STAGE_4`.

The final set is:

1. CAND-001 — Crossing ribbons at a round table
2. CAND-002 — How many nearest-neighbour pairs?
3. CAND-003 — Equalising by pairwise sharing
4. CAND-004 — The doubling transfer game
5. CAND-005 — Which scenic villages survive?
6. CAND-006 — When must a choice be reciprocated?
7. CAND-007 — Returns to the city diagonal
8. CAND-008 — Round separately or round once?
9. CAND-009 — Rock-paper-scissors triples
10. CAND-010 — How far is everyone’s nearest neighbour?

The strongest provisional mathematical/editorial candidates before novelty auditing are CAND-004, CAND-003, CAND-010, CAND-002 and CAND-001. This is **not** a final selection.

Important failures caught during discovery include the stuck merge state (1,2,1), choice-dependent balancing times from ((0,0,4)), and an initially incorrect small grid-route count that was corrected before promotion.

## Stage-4 boundary

Stage 4 is now unlocked because the Stage-3 gate genuinely passed.

The next session must audit **all ten** frozen candidates using:
- `prior-art/README.md`;
- `prior-art/prior-art-audit.schema.json`;
- both visible/story searches and story-stripped mathematical-equivalence searches.

No candidate may be called original merely because a quick search is empty, and no primary publication candidate should be selected until all ten audits are complete and classified.

Stage 5 remains locked.
