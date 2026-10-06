# Known Mathematical Connections

This file is a map of nearby mathematics, not a claim that the deletion formulation is new.

## Alternating permutations

Terminal states have alternating comparison signs. Permutations in which no deletion is possible from the start are exactly alternating permutations. Their enumeration is governed by the Euler zigzag numbers.

## Alternating / up-down runs

The number of survivors is one plus the number of maximal constant-sign runs in the original up/down word. Therefore the full survivor-count distribution is a standard permutation statistic in the neighbourhood of alternating-run enumeration.

A priority is to match notation and conventions to authoritative combinatorics references before importing formulas.

## Longest alternating subsequences and local extrema

Local extrema give a canonical alternating subsequence and are closely connected with longest alternating subsequences.

A relevant reference is:

Dan Romik, “Local extrema in random permutations and the structure of longest alternating subsequences”, *Discrete Mathematics & Theoretical Computer Science Proceedings* AO (2011), 825–834. DOI: 10.46298/dmtcs.2956.

The present process adds an asynchronous deletion viewpoint: monotone interior points are removed while local extrema are permanent.

## Wiggle subsequences

Algorithmic “wiggle subsequence” treatments also retain peaks and valleys while discarding points from monotone stretches. These are useful for comparison, but algorithmic optimisation questions should be kept distinct from the full state-space description of the deletion dynamics.

## String rewriting

The comparison-sign word obeys
[
++	o+,
qquad
--	o-.
]

This is a terminating local rewrite system whose irreducible words are alternating. In the base problem, this rewrite picture is even simpler than a generic confluence problem because each original non-core term is permanently deletable.

## Literature tasks

- locate standard references for permutations by alternating runs;
- map the exact survivor-count polynomial to established notation;
- check known mean, variance and limiting laws;
- investigate whether the Boolean-lattice state-space observation appears explicitly in related sequence-reduction literature;
- keep literature equivalence separate from originality claims.
