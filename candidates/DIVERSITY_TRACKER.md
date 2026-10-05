# Candidate Diversity Tracker

**Stage 3 passed on 2026-10-05. The ten-candidate serious set is frozen for Stage 4.**

Stage 2 closed early by D009, so the 23-record corpus remains provisional design evidence rather than a reliable frequency survey.

## Frozen serious candidates

| Candidate | Surface family | Mechanism family | Question form | Randomness role | Representation | Expected solution shape | Closest existing candidate | Variant? |
|---|---|---|---|---|---|---|---|---|
| CAND-001 | round-table pairing / ribbons | perfect matching; four-point symmetry; linearity | expected value | uniform perfect matching | whole matching → four endpoints / crossing indicator | each pair crosses with probability 1/3, then sum | none | no |
| CAND-002 | random spatial nearest neighbours | exchangeable spacings; local minima; linearity | expected count | uniform points on a circle | points → cyclic gap sequence | mutual pair iff local-minimum gap | CAND-010 | no; line version merged |
| CAND-003 | many-person sharing / equalisation | pairwise averaging; dyadic coefficients; recursion | reachability classification | none | holdings → coefficients of initial holdings | dyadic obstruction + recursive construction | CAND-004 | no; related dyadic theme |
| CAND-004 | two-person transfer process | modular doubling; gcd; finite-state dynamics | eventual-equality classification | none | holding → residue mod total | doubling orbit + gcd reduction | CAND-003 | no; related power-of-two theme |
| CAND-005 | route elevations / deletion | sign changes; run compression; confluence | order independence / characterisation | none | height list → +/- word | deletion becomes duplicate-sign contraction | none | no |
| CAND-006 | social choices / reciprocal selection | extremal counting; orientation; cyclic construction | sharp threshold | none | choices → directed edges | edge bound + sharp cyclic example | CAND-009 | no |
| CAND-007 | city-grid routes | lattice paths; indicators; binomial convolution | expected returns | uniform shortest route | route → diagonal-visit indicators | sum visit probabilities and collapse convolution | none | no |
| CAND-008 | currency conversion / billing | rounding errors; fractional parts; extremal bound | worst-case discrepancy | none | each rounding → additive error | bound integer error and construct equality examples | none | no |
| CAND-009 | round-robin competition | double counting; convexity; balanced tournament construction | maximum cyclic triples | none | results → win totals + triple types | count transitive triples, balance scores, construct equality | CAND-006 | no |
| CAND-010 | houses on a road / nearest distances | gap sequence; total variation; averaging | sharp maximum | none | locations → consecutive gaps | rewrite nearest-distance sum and bound variation | CAND-002 | no; same broad nearest-neighbour motif, different kernel |

## Merged / near-duplicate families

- **CAND-002:** the line-segment nearest-neighbour expectation also gives (n/3), but uses the same local-gap kernel.
- **CAND-001:** expected total span in a random perfect matching uses the same matching symmetry and was not counted separately.
- **CAND-007:** expected turns of a shortest grid route and switches in a random merge of two queues are the same binary-word adjacency mechanism.
- **CAND-005:** circular local-peak elimination was rejected as a shallower local-deletion relative.

## Concentration review at freeze

The set is broad enough to freeze, with overlaps explicitly visible:

1. **Expectation/probability:** CAND-001, CAND-002 and CAND-007 are expectation questions, but their structures are perfect matchings, exchangeable spacings and lattice paths respectively.
2. **Dyadic/power-of-two:** CAND-003 and CAND-004 both have power-of-two conclusions, but one is many-agent averaging and one is deterministic modular dynamics.
3. **Nearest-neighbour surface:** CAND-002 and CAND-010 share language but differ in randomness, statistic, representation and solution.
4. **Directed choices/competition:** CAND-006 and CAND-009 both admit arrow representations, but one is a reciprocity threshold and the other an extremal triple-count problem.

Information/guessing, impartial games, scheduling, sorting and circular-route seeds were deliberately explored. No representative from those areas survived merely for diversity: the strongest versions encountered were standard hats, coin-row, gas-station, scheduling or inversion problems.

## Freeze rule

The ten rows above are the complete Stage-3 serious set. Their status in `serious-candidates.jsonl` is `FROZEN_FOR_STAGE_4`.

Stage 4 must audit **all ten**. A later candidate should not be silently added to the audit set; reopening Stage 3 would require an explicit reason and consistent authority-file updates.
