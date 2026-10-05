# Candidate Diversity Tracker

**Stage 3 is active. First substantial discovery pass recorded 2026-10-05.**

The purpose is to prevent a nominally large pool from being dozens of cosmetic variants. Stage 2 closed early by D009, so the 23-record corpus is provisional design evidence rather than a reliable frequency survey.

## Current serious candidates

| Candidate | Surface family | Mechanism family | Question form | Randomness role | Representation | Expected solution shape | Closest existing candidate | Variant? |
|---|---|---|---|---|---|---|---|---|
| CAND-001 | round-table pairing / ribbons | perfect matching; four-point symmetry; linearity of expectation | expected value | uniform perfect matching | whole matching → four endpoints / crossing indicator | each pair of ribbons crosses with probability 1/3, then sum | none | no |
| CAND-002 | random spatial nearest neighbours | exchangeable spacings; local minima; linearity | expected count | uniform random points on a circle | points → cyclic gap sequence | mutual pair iff local-minimum gap; probability 1/3 | CAND-001 | no; line version merged |
| CAND-003 | many-person sharing / equalisation | pairwise averaging; dyadic coefficients; recursion | reachability classification | none | holdings → coefficients of initial holdings | dyadic obstruction + recursive construction | CAND-004 | no; related dyadic theme |
| CAND-004 | two-person transfer process | modular doubling; gcd; finite-state dynamics | eventual-equality classification | none | holding → residue mod conserved total | x→2x mod S, reduce by gcd, classify half-hit | CAND-003 | no; related dyadic theme |
| CAND-005 | route elevations / deletion | sign changes; run compression; confluence | order independence / characterisation | none | height list → +/- word | deletion is duplicate-sign contraction; unique normal form | none | no; weaker local-deletion seed rejected |
| CAND-006 | social choices / reciprocal selection | extremal counting; orientation; cyclic construction | sharp threshold | none | choices → directed edges | global edge count + cyclic sharpness example | none | no |
| CAND-007 | city-grid routes | lattice paths; indicators; central-binomial convolution | expected returns | uniform shortest route | route → visit indicator at each diagonal point | sum point-visit probabilities and collapse convolution | none | no; turns/queue-switch seeds rejected or merged |

## Merged / near-duplicate families

- **CAND-002:** the line-segment nearest-neighbour formulation also gives (n/3), but uses the same local-gap kernel and is not a separate serious candidate.
- **CAND-001:** expected total span in a random perfect matching is another indicator calculation on the same matching object and is not counted separately.
- **CAND-007:** expected turns of a random shortest grid route and expected switches in a random merge of two queues are the same binary-word adjacency mechanism; neither is counted as a separate serious candidate.
- **CAND-005:** circular local-peak elimination was rejected as a shallower local-deletion relative, not promoted as a variant.

## Concentration check

The seven-candidate pool is genuinely multi-mechanism, but two concentrations remain visible:

1. **Expectation/probability:** CAND-001, CAND-002 and CAND-007 are all expectation questions, although their structures differ substantially.
2. **Dyadic/power-of-two phenomena:** CAND-003 and CAND-004 are not variants, but both produce power-of-two thresholds. Do not add another candidate from this mechanism family without a compelling reason.

## Underrepresented regions to target next

Deliberately explore:
- information / guessing without standard hat or prisoner templates;
- non-generic games with more than a parity or fixed-move-count trick;
- recurrence or finite-state dynamics not based on modular doubling;
- natural deterministic geometry unrelated to nearest-neighbour graphs;
- non-monotonic phenomena;
- allocation/sharing mechanisms unrelated to pairwise averaging;
- parity/invariants with a different surface;
- symmetry / equivalence questions that are not expectations.

## Review rules

- A renamed story is not a new idea.
- Changing constants without changing the phenomenon is not a new idea.
- A new surface with the same kernel should normally be treated as a formulation variant until it creates a materially different reader experience or mathematical question.
- A new kernel under the same surface may count as diverse if the actual mathematical task is materially different.
- Periodically inspect concentration by surface family and mechanism family; deliberately search underrepresented regions rather than producing more of the dominant family.
- The final Stage-3 serious set should have an explainable diversity profile, not merely a large count.
- Because Stage 2 closed early by D009, do not infer that underrepresented categories in the 23-record corpus are editorially unimportant.

Near-duplicate variants may be preserved for wording comparison but must not inflate the serious-candidate count.
