# Project

## Central object

Let (x=(x_1,ldots,x_n)) be a finite sequence of pairwise distinct real numbers.

Given a current surviving subsequence (y=(y_1,ldots,y_m)), an interior term (y_i) is **deletable** when it lies strictly between its two current neighbours:
[
min(y_{i-1},y_{i+1})<y_i<max(y_{i-1},y_{i+1}).
]

A **deletion history** is any sequence of legal deletions continued until no legal deletion remains.

Equivalently, (y_i) is deletable when the two adjacent comparison directions agree:
[
y_{i-1}<y_i<y_{i+1}
quad	ext{or}quad
y_{i-1}>y_i>y_{i+1}.
]

## Order-type reduction

Any strictly increasing transformation of all values preserves every legal move. In particular, replace the values by their ranks. The base theory may therefore be studied on permutations in (S_n).

## Core questions

1. Which original terms can ever be deleted?
2. Is the terminal subsequence independent of choices?
3. What is the full graph of reachable subsequences?
4. How many complete and partial deletion histories are there?
5. For permutations of size (n), how many have exactly (k) survivors?
6. What are the probabilistic laws for a uniformly random permutation?
7. Which variants preserve confluence or the Boolean-lattice state space?
8. What established combinatorial objects encode the same statistics?

## Baseline answer

For the base process, the invariant core consists of the endpoints and original local extrema. All other terms are permanently deletable until removed. Thus the base dynamical system is completely described by the choice of which non-core terms have already been deleted.

The research value therefore lies both in developing the combinatorics of this structure and in identifying variants where the dynamics become genuinely richer.
