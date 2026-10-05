# Stage 3 Discovery Notes

**As of:** 2026-10-05  
**Status:** **COMPLETE / PASSED**. The serious set is frozen for Stage 4; no Stage-4 novelty audit has yet been performed.

Stage 2 was closed early by D009. The 23-record corpus was therefore used only as provisional editorial evidence. Discovery borrowed design clues actually observed there — compact statements supporting longer solutions, representation changes, elementary decisive ideas, alternative routes, and solver-driven generalisation — without treating that incomplete corpus as a reliable frequency survey.

## Discovery summary

- Candidate seeds substantially explored: **31**
- Frozen serious candidates: **10**
- Rejected: **17**
- Merged as variants / same-family formulations: **4**
- Structured serious records: `candidates/serious-candidates.jsonl`
- Formal Stage-4 novelty audit performed: **no**
- Serious set frozen for Stage 4: **yes**

All ten frozen candidates have a reader-facing statement, mathematical kernel, expected answer, credible solution mechanism, basic mathematical validation, similarity-risk notes, a ten-dimension rubric assessment with written reasons, and a diversity classification.

Originality scores remain provisional risk assessments only. They are not novelty claims.

## Seed ledger

| Seed | Idea | Decision | Mathematical check / reason |
|---|---|---|---|
| S01 | Random round-table pairing; expected crossing ribbon pairs | **FROZEN → CAND-001** | Exact expectation (n(n-1)/6); perfect-matching enumeration checked n=2,3,4. |
| S02 | Random points on a circle; expected mutual nearest-neighbour pairs | **FROZEN → CAND-002** | Mutual pairs are local-minimum gaps; exchangeability gives (n/3); cyclic-rank enumeration checked n=3…7. |
| S03 | Uniform random points on a line; same nearest-neighbour question | **MERGED VARIANT of CAND-002** | Also gives (n/3), with endpoint gaps contributing 1/2 and interior gaps 1/3. Same reader question and local-gap kernel. |
| S04 | Pairwise pool-and-split averaging; when can every initial distribution be equalised? | **FROZEN → CAND-003** | Exact iff n is a power of two: dyadic obstruction plus recursive construction. |
| S05 | Two-person “richer gives poorer what poorer has” process | **FROZEN → CAND-004** | Exact iff ((a+b)/\gcd(a,b)) is a power of two; process is doubling modulo total. Exhaustive check for (1≤a,b≤24). |
| S06 | Delete a village whose altitude lies between its current neighbours | **FROZEN → CAND-005** | Sign-word compression proves unique final turning-point list; exhaustive all-choice reduction checked through n=7. |
| S07 | Two independent rankings; expected Pareto-undominated contestants | **REJECTED** | Exact expectation (H_n) via record indicators, but this is classical record statistics and looked too standard to spend a serious-candidate slot. |
| S08 | Everyone chooses k card recipients; threshold forcing reciprocity | **FROZEN → CAND-006** | Sharp threshold (lceil n/2ceil) by edge counting plus cyclic construction. |
| S09 | Random shortest grid route; expected number of turns | **REJECTED** | Exact (2mn/(m+n)), but the indicator proof is essentially a standard textbook expectation exercise. |
| S10 | Random shortest square-grid route; expected interior returns to diagonal | **FROZEN → CAND-007** | Exact (4^n/\binom{2n}{n}-2); enumerated n=1…5. |
| S11 | Random interleaving of two queues; expected queue switches | **MERGED VARIANT of S09** | Same binary-word / adjacent-switch kernel as grid-route turns under a changed story. |
| S12 | Misassigned coats; swaps needed when holders swap with coat owners | **REJECTED** | Correct value (n-#\text{cycles}), but this is a familiar permutation-cycle exercise. |
| S13 | Repeatedly remove any local height maximum around a table | **REJECTED** | Correct but too shallow and structurally overlaps CAND-005’s local-deletion family. |
| S14 | Each point links to its nearest neighbour; components end in mutual pairs | **MERGED / NOT PROMOTED** | Strictly decreasing edge lengths rule out cycles longer than 2, but it duplicates CAND-002’s nearest-neighbour surface. |
| S15 | Random perfect matching on a line; expected total span | **MERGED VARIANT of CAND-001** | Gives (n(2n+1)/3), but the same random-perfect-matching symmetry is doing the work. |
| S16 | Secret-Santa-style random choices; expected mutual pairs | **REJECTED** | Linear expectation gives (n/(n-1)), but the result is too slight for the target. |
| S17 | Adjacent equal-value merging; conjectured power-of-two criterion | **REJECTED — COUNTEREXAMPLE** | (1,2,1) has total 4 but no legal merge. |
| S18 | Balance piles by moving one item from richer to poorer; conjectured move-count independence | **REJECTED — COUNTEREXAMPLE** | From ((0,0,4)), legal routes can take 2 or 3 moves. |
| S19 | Two-player pile-splitting game; last move wins | **REJECTED** | Every play has exactly n-1 splits; too close to a generic fixed-move-count trick. |
| S20 | Recursively split a set; score product of child sizes | **REJECTED** | Total is always (inom n2) because each pair is separated exactly once; elegant but too light. |
| S21 | Broken-stick / polygon probability | **REJECTED** | Overtly classical recreational family. |
| S22 | Circular lamps; toggle three consecutive lamps | **REJECTED** | Neat mod-3 structure, but recognisably a Lights-Out-family problem. |
| S23 | Round converted purchases separately or round only the exact total | **FROZEN → CAND-008** | Sharp discrepancy (lfloor n/2floor) pence by rounding-error bounds; exhaustive tenth-penny tests for n=2…5. |
| S24 | Maximise rock-paper-scissors triples in a round robin | **FROZEN → CAND-009** | Formula verified by complete tournament enumeration for n=3…6; proof uses triple counting, balanced win totals and cyclic constructions. |
| S25 | Houses on a one-mile road; maximise total nearest-house distance | **FROZEN → CAND-010** | Exact maximum (n/(n-1)), equality at equal spacing; LP checks n=2…10 and a total-variation proof. |
| S26 | Everyone sees all binary labels except their own and guesses simultaneously | **REJECTED** | Maximum guaranteed correct is (lfloor n/2floor) by split parity targets, with an averaging upper bound. Mathematically clean but equivalent to a standard hat-guessing family explicitly disfavoured by the brief. |
| S27 | Adjacent overtaking in a queue with toll equal to the pair’s value difference | **REJECTED** | Every inverted pair crosses exactly once, so total toll is the weighted inversion sum independent of swap order. Too close to standard sorting/inversion bookkeeping. |
| S28 | Two cafés inside a convex park; guarantee a corner closer to each café | **REJECTED** | Perpendicular-bisector halfplanes and convexity give a one-line proof. Too slight, and uncomfortably close in spirit to the Stage-2 interior-point generalisation around 101.L. |
| S29 | Circular fuel-station route; existence of a starting point that completes the circuit | **REJECTED** | Correct partial-sum/cycle argument, but this is the classical gas-station / cycle-lemma family. |
| S30 | Order jobs to minimise total queue waiting time | **REJECTED** | Shortest-processing-time-first follows by an adjacent exchange argument; standard scheduling textbook material. |
| S31 | Even row of coin values; take from either end and guarantee at least half | **REJECTED** | The parity-position strategy is classical and too recognisable as a standard coin-row game. |

## Important mathematical failures caught

The discovery process deliberately tested attractive conjectures before promotion.

1. **Adjacent merging:** a power-of-two total is not sufficient. The row (1,2,1) is a minimal obstruction.
2. **Balancing piles:** the number of balancing moves is not choice-independent. From ((0,0,4)), different legal choices take 2 or 3 moves.
3. **Grid-return hand count:** an early scratch calculation for n=2 undercounted diagonal visits. Exact enumeration gives (4/6=2/3), and the serious record was corrected before promotion.
4. **Surface duplication:** line nearest-neighbours, queue switches, deterministic nearest-neighbour components and random-matching span were merged/demoted rather than allowed to inflate the pool.

## Frozen serious set

The ten candidates frozen for exhaustive Stage-4 audit are:

- **CAND-001 — Crossing ribbons at a round table**
- **CAND-002 — How many nearest-neighbour pairs?**
- **CAND-003 — Equalising by pairwise sharing**
- **CAND-004 — The doubling transfer game**
- **CAND-005 — Which scenic villages survive?**
- **CAND-006 — When must a choice be reciprocated?**
- **CAND-007 — Returns to the city diagonal**
- **CAND-008 — Round separately or round once?**
- **CAND-009 — Rock-paper-scissors triples**
- **CAND-010 — How far is everyone’s nearest neighbour?**

This is intentionally a ten-candidate set rather than a padded march toward fifty.

## Provisional strongest candidates before novelty audit

The present mathematical/editorial leaders are:

- **CAND-004 — The doubling transfer game.** Excellent experimentation, a highly non-obvious gcd/power-of-two theorem, and a decisive representation change (x\mapsto 2x\pmod S).
- **CAND-003 — Equalising by pairwise sharing.** Extremely natural operation with complementary construction and impossibility proofs; finite-time consensus prior art is the main risk.
- **CAND-010 — How far is everyone’s nearest neighbour?** Strong deterministic geometry/extremal candidate with an elementary but non-obvious total-variation mechanism.
- **CAND-002 — How many nearest-neighbour pairs?** Striking (n/3) answer and no integration, but nearest-neighbour literature may be dangerous.
- **CAND-001 — Crossing ribbons at a round table.** Exceptionally visual one-sentence problem with a clean four-endpoint symmetry; random chord-diagram prior art is the obvious risk.

CAND-009 is mathematically strong but likely to face classical tournament-theory prior art. CAND-005 is elegant but may be too light. CAND-006, CAND-007 and CAND-008 remain serious because their mathematics is complete enough to justify audit, despite higher “standard exercise” risk.

## Diversity profile at freeze

Surface/context families represented:
- round-table ribbons;
- random spatial nearest neighbours;
- many-person sharing;
- two-person money transfer;
- route elevations and deletion;
- social reciprocal choices;
- city-grid routes;
- currency conversion / billing;
- round-robin competition;
- deterministic house spacing on a road.

Mechanism families represented:
- perfect-matchings and four-point symmetry;
- exchangeable circular spacings and local minima;
- dyadic averaging and recursive construction;
- modular dynamics and gcd;
- rewrite-system confluence via sign compression;
- extremal directed-edge counting;
- lattice paths and central-binomial convolution;
- rounding-error extremals;
- double counting plus convex balancing of score sequences;
- gap sequences and total variation.

Visible concentrations remain but are controlled rather than accidental:
- CAND-001, CAND-002 and CAND-007 are expectation/probability problems, with different mathematical structures.
- CAND-003 and CAND-004 both produce power-of-two phenomena but are not variants.
- CAND-002 and CAND-010 both use nearest-neighbour language but one is random/local and the other deterministic/extremal.
- CAND-006 and CAND-009 both use directed choices/results, but their statistics and proof mechanisms differ materially.

Information/guessing and impartial-game seeds were explicitly explored; the promising examples collapsed into standard hat, gas-station, sorting, scheduling or coin-game families, so no weak representative was retained merely to fill those categories.

## Stage-3 gate assessment

**PASS.**

- Candidate generation explicitly used the provisional Stage-2 observations without overstating them.
- The pool is broad and diverse and was not padded.
- Every frozen serious candidate has a complete structured record.
- Every frozen candidate has an expected answer and credible solution route.
- Basic mathematical checks were performed, including exhaustive enumeration or computational spot-checking where useful.
- The diversity tracker records overlaps and merged variants.
- Every frozen candidate was assessed on all ten frozen rubric dimensions with written reasons.
- Weak, unsound, textbook-like, derivative-looking and repetitive candidates were rejected or merged with reasons.
- The ten-candidate set is clearly frozen for exhaustive Stage-4 audit.

Stage 4 is therefore unlocked but **not started** in this session.
