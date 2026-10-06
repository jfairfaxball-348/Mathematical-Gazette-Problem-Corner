# Research Questions

The base process is structurally simple once the permanent core is identified. The research programme therefore has two branches: extract its full combinatorics, and then study nearby rules where richer dynamics may appear.

## A. Enumeration and probability

1. Determine the exact standard recurrence for
   [
   a(n,k)=#{piin S_n:	ext{exactly }k	ext{ terms survive}}.
   ]
2. Express the survivor-count generating polynomial in the standard language of alternating/up-down runs.
3. Derive the variance of the number of survivors in a uniform random permutation.
4. Establish the limiting distribution after centring and scaling.
5. Study large deviations: how rare are nearly monotone or nearly fully alternating permutations?
6. Enumerate permutations by both survivor count and another statistic such as descents.

## B. Reachable states and histories

The base state graph is (B_d), where (d) is the number of non-core terms.

Questions that remain useful include:

1. Count histories subject to positional restrictions or time constraints.
2. Study a random deletion order as a random maximal chain of (B_d).
3. For a random permutation, study the induced distribution of (d), hence of (2^d) reachable states and (d!) complete histories.
4. Determine asymptotics for expectations such as (mathbb E[2^d]) or (mathbb E[d!]).

## C. Circular variant

Place the entries on a cycle and allow deletion when a value lies strictly between its two current cyclic neighbours.

Investigate:

- the correct analogue of the permanent core;
- whether every non-core point remains permanently deletable;
- whether the state space is again Boolean;
- enumeration of terminal cores for cyclic permutations.

The likely behaviour should be proved rather than inferred from the path case.

## D. Repeated values

Allow equal values and compare several rules:

- strict betweenness only;
- weak betweenness;
- deletion only when one inequality is strict;
- deterministic tie-breaking by original index.

Determine which variants remain confluent and which admit genuinely order-dependent terminal states.

## E. Modified local rules

Examples:

- delete a middle term only when it lies in a prescribed percentile interval between neighbours;
- delete local extrema rather than monotone middle points;
- use windows of four or more current neighbours;
- attach weights or costs to deletions;
- permit both deletion and insertion operations.

Seek the smallest natural rule change for which deletion order genuinely matters.

## F. Graph variants

Replace the path by a tree or graph and define a local deletion rule using neighbouring values.

Questions:

- what is the right analogue of “between” with degree greater than two?
- when does a permanent core exist?
- when is the state graph distributive, Boolean, or non-confluent?

## G. Pattern theory

Characterise survivor statistics through consecutive patterns and vincular patterns. Determine whether the survivor-count distribution has useful pattern-avoidance interpretations.

## H. Computational programme

Use exhaustive search to:

- verify formulas for small (n);
- find smallest counterexamples to proposed variants;
- tabulate (a(n,k));
- test cyclic and repeated-value rules;
- export reproducible tables rather than relying on hand examples.
