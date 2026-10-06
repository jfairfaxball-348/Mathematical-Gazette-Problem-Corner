# Start Here

This repository is an active mathematics research project on a deletion process for sequences and permutations.

## Current mathematical object

Start with a finite sequence of pairwise distinct real numbers. Repeatedly delete any interior current term that lies strictly between its two current neighbours.

The geometric story is no longer part of the mathematical model. Only the ordered sequence and comparisons matter.

## Baseline structure

The current proved foundation is:

1. rank-normalisation reduces the problem to permutations;
2. original endpoints and local extrema form a permanent core;
3. every term outside that core remains legal to delete until removed;
4. every deletion order terminates at the same core;
5. with (d) non-core terms, the state space is a Boolean lattice of size (2^d), and all (d!) orders of deleting those terms are legal;
6. the comparison-sign word reduces by (++\to+) and (--\to-), leaving an alternating word.

## Read next

1. `authoritative/STATE.json`
2. `PROJECT.md`
3. `STATUS.md`
4. `theory/FOUNDATIONS.md`
5. `theory/ENUMERATION.md`
6. `questions/RESEARCH_QUESTIONS.md`

## Current priority

Develop the exact enumeration and probability theory of the number of surviving terms, then explore variants where the Boolean-lattice property may fail.

Repository state is authoritative unless superseded by an explicit human instruction.
