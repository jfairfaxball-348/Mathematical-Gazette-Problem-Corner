# Stage 3 Discovery Notes

**As of:** 2026-10-05  
**Status:** first substantial discovery pass complete; Stage 3 remains **IN PROGRESS**.

Stage 2 was closed early by D009. The 23-record corpus is therefore used only as provisional editorial evidence. This pass deliberately borrowed design clues that were actually observed — compact statements supporting longer solutions, representation changes, elementary decisive ideas, alternative routes and solver-driven generalisation — without treating the corpus as a reliable frequency survey.

## Discovery-pass summary

- Candidate seeds substantially explored: **22**
- Promoted to current serious-candidate status: **7**
- Rejected: **11**
- Merged as variants / same-family formulations: **4**
- Current structured serious records: `candidates/serious-candidates.jsonl`
- Formal Stage-4 novelty audit performed: **no**
- Serious set frozen for Stage 4: **no**

The seven serious candidates are mathematically checked enough to have a credible theorem/answer and solution route, but their originality scores remain provisional risk assessments. A score is not a novelty claim.

## Seed ledger

| Seed | Idea | Decision | Mathematical check / reason |
|---|---|---|---|
| S01 | Random round-table pairing; expected crossing ribbon pairs | **SERIOUS → CAND-001** | Exact expectation (n(n-1)/6); perfect-matching enumeration checked n=2,3,4. |
| S02 | Random points on a circle; expected mutual nearest-neighbour pairs | **SERIOUS → CAND-002** | Mutual pairs are local-minimum gaps; exchangeability gives (n/3); cyclic-rank enumeration checked n=3…7. |
| S03 | Uniform random points on a line; same nearest-neighbour question | **MERGED VARIANT of CAND-002** | Also gives (n/3), with endpoint gaps contributing 1/2 and interior gaps 1/3. Same reader question and local-gap kernel, so not counted separately. |
| S04 | Pairwise pool-and-split averaging; when can every initial distribution be equalised? | **SERIOUS → CAND-003** | Exact iff (n) is a power of two: dyadic obstruction plus recursive construction. |
| S05 | Two-person “richer gives poorer what poorer has” process | **SERIOUS → CAND-004** | Exact iff ((a+b)/\gcd(a,b)) is a power of two; process is doubling modulo total. Exhaustive check for (1≤a,b≤24). |
| S06 | Delete a village whose altitude lies between its current neighbours | **SERIOUS → CAND-005** | Sign-word compression proves unique final turning-point list; exhaustive all-choice reduction checked through n=7. |
| S07 | Two independent rankings; expected number of Pareto-undominated contestants | **REJECTED** | Exact expectation (H_n) via record indicators, but this is a classical record-statistics result and looked too standard to spend a serious-candidate slot before Stage 4. |
| S08 | Everyone chooses k card recipients; threshold forcing reciprocity | **SERIOUS → CAND-006** | Sharp threshold (lceil n/2ceil) by edge counting plus cyclic construction. Retained as a lower-tier extremal candidate with high prior-art risk. |
| S09 | Random shortest grid route; expected number of turns | **REJECTED** | Exact (2mn/(m+n)), verified on small grids, but the indicator proof is essentially a standard textbook expectation exercise. |
| S10 | Random shortest square-grid route; expected interior returns to diagonal | **SERIOUS → CAND-007** | Exact (4^n/\binom{2n}{n}-2); enumerated n=1…5. Requires central-binomial convolution. |
| S11 | Random interleaving of two queues; expected colour/queue switches | **MERGED VARIANT of S09** | Same binary-word / adjacent-switch kernel as grid-route turns under a changed story. |
| S12 | Misassigned coats; swaps needed when holders swap with coat owners | **REJECTED** | Correct value (n-#	ext{cycles}), but this is a familiar permutation-cycle exercise. |
| S13 | Around a table, repeatedly remove any local height maximum; ask final survivors | **REJECTED** | The two shortest people necessarily survive and some maximum is always removable. Correct but too shallow, and structurally overlaps CAND-005’s local deletion family. |
| S14 | Each point links to its nearest neighbour; prove every directed component ends in a mutual pair | **MERGED / NOT PROMOTED** | Strictly decreasing edge lengths rule out directed cycles longer than 2, but it duplicates CAND-002’s nearest-neighbour surface and a known graph property is likely. |
| S15 | Random perfect matching on a line; expected total span of matched pairs | **MERGED VARIANT of CAND-001** | Indicator calculation gives (n(2n+1)/3), but the same random-perfect-matching symmetry is doing the work. |
| S16 | Secret-Santa-style random choices; expected number of people in mutual pairs | **REJECTED** | Linear expectation gives (n/(n-1)), mathematically correct but too slight for the target. |
| S17 | Adjacent equal-value merge process; conjecture that power-of-two total is sufficient to merge to one pile | **REJECTED — COUNTEREXAMPLE** | (1,2,1) has total 4 but no adjacent equal pair, so it is immediately stuck. Surface remained appealing but proposed theorem failed. |
| S18 | Repeatedly move one item from a richer pile to a poorer pile until counts differ by at most one; conjecture move-count independence | **REJECTED — COUNTEREXAMPLE** | From ((0,0,4)), one legal route takes 2 moves and another takes 3, so the attractive order-independence claim is false. |
| S19 | Two-player pile-splitting game; last move wins | **REJECTED** | Every complete play has exactly (n-1) splits. Surprise exists, but mathematical content is too thin and reads like a generic invariant trick. |
| S20 | Recursively split a set; score product of child sizes at each split | **REJECTED** | Total is always (inom n2) because each unordered pair is separated exactly once. Elegant but not enough depth for this project. |
| S21 | Broken-stick / polygon formation probability | **REJECTED** | Attractive probability surface, but this is an overtly classical recreational family and not a useful Stage-3 originality bet. |
| S22 | Circular lamps; pressing toggles three consecutive lamps | **REJECTED** | Leads to a neat mod-3 / linear-algebra condition, but is recognisably a Lights-Out-family problem rather than a fresh surface. |

## Important mathematical failures caught

The pass deliberately tested attractive conjectures before promotion.

1. **Adjacent merging:** a power-of-two total is not sufficient. The row (1,2,1) is a minimal obstruction.
2. **Balancing piles:** the number of balancing moves is not choice-independent. From ((0,0,4)), different legal choices take 2 or 3 moves.
3. **Grid-return hand count:** an early scratch calculation for n=2 undercounted diagonal visits. Exact enumeration gives (4/6=2/3), and the serious record was corrected before commit.
4. **Surface duplication:** the line nearest-neighbour version, queue-switch formulation, deterministic nearest-neighbour graph and random-matching span statistic were mathematically sound but merged/demoted because they did not add enough mechanism diversity.

## Current serious-candidate comparison

Provisional strongest group:

- **CAND-004 — The doubling transfer game.** Strongest combination so far of immediate experimentation, non-obvious theorem, a representation change (xmapsto 2xmod S), and an exact gcd/power-of-two classification.
- **CAND-003 — Equalising by pairwise sharing.** Extremely clean natural question with complementary construction and impossibility proofs; biggest concern is equivalent finite-time-consensus prior art.
- **CAND-002 — How many nearest-neighbour pairs?** Very strong qualitative/geometric surface and a striking (n/3) answer with no integration; nearest-neighbour literature is the obvious risk.
- **CAND-001 — Crossing ribbons at a round table.** Exceptionally visual and concise with a one-third four-endpoint symmetry; random chord-diagram prior art risk is substantial but the reader experience is strong.

CAND-005 is elegant but may be too light. CAND-006 is deliberately retained as a lower-tier extremal/threshold representative despite likely graph-theory prior art. CAND-007 has enough depth but is exposed to classical lattice-path prior art and textbook resemblance.

## Diversity profile after first pass

Current serious surfaces:
- round-table pairing / ribbons;
- random spatial nearest neighbours;
- many-person sharing / equalisation;
- two-person transfer dynamics;
- route elevations / deletion;
- social reciprocal choice;
- city-grid routes.

Current serious mechanisms:
- perfect matching symmetry and indicator expectation;
- exchangeable spacings and local minima;
- dyadic averaging / recursive construction;
- modular doubling and gcd;
- rewrite-system confluence via sign compression;
- extremal directed-edge counting;
- lattice-path indicators and binomial convolution.

This is materially diverse, but it is **not yet broad enough to freeze**. Three of seven serious candidates are expectation/probability-led, and CAND-003/CAND-004 share a power-of-two/dyadic flavour even though they are not variants.

## Deliberate gaps for the next discovery pass

Underexplored areas now worth targeting:
- information and guessing without falling into standard hat/prisoner puzzles;
- non-generic games with a genuinely explanatory solution rather than a one-line parity trick;
- recurrence or finite-state processes not driven by modular doubling;
- natural deterministic geometry not based on nearest neighbours;
- non-monotonic or threshold phenomena outside extremal directed graphs;
- allocation/sharing mechanisms that are not another dyadic equalisation problem;
- parity and averaging mechanisms with a qualitatively different surface;
- symmetry or unexpected equivalence problems with no expectation calculation.

## Gate view

Stage 3 should **not** pass yet. Every current serious candidate has a structured record, expected answer, credible solution mechanism, basic soundness checks, rubric assessment and diversity entry. Weak and duplicate seeds have been explicitly rejected/merged. However:

- this is only the first serious discovery pass;
- diversity still has identifiable gaps and some probability/dyadic concentration;
- the serious set has **not** been frozen for exhaustive Stage-4 audit.

Stage 4 therefore remains locked.
