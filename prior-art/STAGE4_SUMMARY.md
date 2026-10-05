# Stage 4 Prior-art / Novelty Audit Summary

**Completed:** 2026-10-05  
**Status:** **PASSED**  
**Decision:** D011

Stage 4 audited all ten candidates frozen by D010. The audit treated the structured Stage-3 records in `candidates/serious-candidates.jsonl` as fixed definitions and searched both visible formulations and story-stripped mathematical equivalents.

A failed search was never treated as proof of novelty. No candidate received an unqualified `CLEAR` classification.

## Frozen classifications

| Candidate | Classification |
|---|---|
| CAND-001 — Crossing ribbons at a round table | REDISCOVERY |
| CAND-002 — How many nearest-neighbour pairs? | REDISCOVERY |
| CAND-003 — Equalising by pairwise sharing | REDISCOVERY |
| CAND-004 — The doubling transfer game | REDISCOVERY |
| CAND-005 — Which scenic villages survive? | CLEAR_WITH_RELATED_PRIOR_ART |
| CAND-006 — When must a choice be reciprocated? | REDISCOVERY |
| CAND-007 — Returns to the city diagonal | REDISCOVERY |
| CAND-008 — Round separately or round once? | TOO_CLOSE_TO_EXISTING_PROBLEM |
| CAND-009 — Rock-paper-scissors triples | REDISCOVERY |
| CAND-010 — How far is everyone’s nearest neighbour? | CLEAR_WITH_RELATED_PRIOR_ART |

The complete structured records are in `prior-art/audits/CAND-001.json` through `CAND-010.json`.

## Strongest prior-art findings

- **CAND-001:** the random-chord expectation (n(n-1)/6) and the four-endpoint / one-of-three pairings proof are already public, and uniform random chord diagrams are an established literature.
- **CAND-002:** one-dimensional reflexive nearest-neighbour pairs have exact mean (n/3); a wrap-around formulation gives the same circle/local-minimum-gap argument.
- **CAND-003:** finite-time symmetric gossip averaging is possible exactly when the number of nodes is a power of two.
- **CAND-004:** the exact map ((a,b)mapsto(2a,b-a)), up to swapping, and the reduced-sum power-of-two termination criterion were already posed and solved.
- **CAND-006:** after people become vertices, the threshold is the standard arc-count forcing of a directed 2-cycle at outdegree at least (n/2), with tournament orientations supplying sharpness.
- **CAND-007:** a 2017 MathOverflow answer gives the same lattice-path indicator sum, (4^n/\binom{2n}{n}) including endpoints, and explicitly says to subtract 2 when endpoints are excluded.
- **CAND-008:** the target journal itself has substantial work on rounding before versus after summation, including a 2016 Gazette article, its 1987 College Mathematics Journal antecedent, and a 2025 Gazette article referring explicitly to the maximum possible error.
- **CAND-009:** the maximum number of cyclic triples in a tournament is classical; the regular/near-regular extremisers, score-sequence identity and both parity formulas are standard.

## Survivors with related but non-fatal prior art

### CAND-010 — primary

The objective (sum_i min_{j
e i}d(x_i,x_j)) is not new: it is known in diversity/facility-location literature as **remote-pseudoforest**, **sum-min** or **p-defense-sum**. That is real related prior art and is why the candidate is not classified `CLEAR`.

What the audit did **not** locate is the frozen continuous one-dimensional theorem: (n) freely placed points of fixed span 1, maximum total nearest-neighbour distance (n/(n-1)), equality at equal spacing, with the gap/total-variation mechanism. Multiple exact-form searches using the formula, fixed-span language, gap language and the established objective names produced no material equivalent.

Combined with the Stage-3 record, CAND-010 has the stronger primary position: the statement is immediate, the extremal answer is non-obvious, the solution has genuine depth without specialist prerequisites, and the located prior art is at the objective-family level rather than the exact theorem level.

### CAND-005 — reserve

Local extrema as a canonical alternating subsequence are established, and standard wiggle/turning-point algorithms retain peaks and valleys while discarding points on monotone slopes. This is meaningful related prior art.

The audit did **not** locate the exact frozen rewrite question: repeatedly delete **any** currently eligible middle term lying between its neighbours, then prove that every deletion order reaches the same surviving subsequence. The confluence/run-compression theorem therefore retains a defensible novelty position, but its terminal object is closer to known material than CAND-010's exact fixed-span theorem appears to be. Its Stage-3 mathematical depth score is also lower.

## Selection

**Primary candidate:** **CAND-010 — How far is everyone’s nearest neighbour?**

**Reserve candidate:** **CAND-005 — Which scenic villages survive?**

No rediscovery or too-close candidate is selected.

## Coverage and limitations

The audit used target-journal searches, mathematical Q&A, scholarly literature, problem/recreational sources where relevant, OEIS where relevant, and alternative terminology derived from each mathematical kernel.

Important limitations remain:

- historical Gazette searching was primarily through publisher/web indexing, not a manual page-by-page read of every issue;
- old problem books and poorly indexed contest/recreational sources can hide elementary prior art;
- some publisher formulae are image-rendered or paywalled, so the audit avoids claiming more than the accessible evidence supports;
- CAND-010's general objective has a substantial optimization literature that was sampled strategically rather than exhaustively;
- CAND-005's local-extrema output is familiar even though the exact confluence formulation was not found;
- Stage 2 remains an incomplete, era-biased 23-record corpus by D009.

These limitations are compatible with the Stage-4 gate because the gate requires a documented reasonably strong audit, not proof of originality. Stage 5 must still perform the required final prior-art audit on the exact finished formulation.

## Gate assessment

Every frozen candidate now has a structured audit; visible and equivalent forms were searched; source classes, searches, findings, materiality and equivalence reasoning are recorded; every candidate has exactly one classification; rediscoveries/too-close cases are excluded; and a primary plus reserve are selected with written rationale.

**Stage 4 passes. Stage 5 is unlocked but has not started.**
