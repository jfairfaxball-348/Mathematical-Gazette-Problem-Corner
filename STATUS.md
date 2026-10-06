# Status

**As of:** 2026-10-06  
**Mode:** active mathematical research

## Established

For a finite sequence of pairwise distinct real values:

- only order type matters, so the sequence may be replaced by a permutation;
- a term is deletable exactly when it is the middle of a currently monotone triple;
- the endpoints and original local extrema are permanent;
- every original non-extremum remains deletable until removed;
- the unique terminal subsequence is the endpoints plus the original local extrema;
- reachable states are exactly the subsequences containing that core;
- if (d) original terms are outside the core, there are (2^d) reachable states and (d!) complete deletion histories;
- if the original comparison word has (c) sign changes, the terminal sequence has (c+2) terms for (nge2);
- all terms survive exactly for alternating permutations;
- for a uniformly random permutation of length (nge2), the expected number of survivors is
  [
  2+rac{2(n-2)}3=rac{2n+2}{3}.
  ]

## Immediate programme

The next priority is the enumeration of permutations by survivor count, equivalently by the number of changes in the up/down comparison word. This should be connected carefully to the classical distribution of alternating runs.

Secondary priorities are:

- exact formulas or recurrences for the survivor-count distribution;
- variance, limiting laws and asymptotics for random permutations;
- the circular version;
- repeated values under several natural weak/strict rules;
- structural variants in which deletability is not permanent;
- literature mapping for alternating runs, local extrema and rewrite systems.

See `questions/RESEARCH_QUESTIONS.md`.
