# Local-Extrema Deletion Dynamics

This repository is an open mathematical research project about a local deletion process on finite ordered sequences.

## Basic process

Let
[
x=(x_1,x_2,ldots,x_n)
]
be a sequence of pairwise distinct real numbers.

At any stage, an interior term may be deleted when it lies strictly between its two **current** neighbours. Thus, for a current triple (a,b,c), the middle term (b) is deletable exactly when
[
a<b<c quad	ext{or}quad a>b>c.
]

After deletion, the two former neighbours become adjacent and the rule is applied again.

Because only relative order matters, every instance can be rank-normalised to a permutation of (1,ldots,n).

## Baseline theorem

For the original sequence, mark:

- the two endpoints; and
- every interior local maximum and local minimum.

These marked terms form the **core**.

Every marked term survives every legal deletion sequence. More strongly, every unmarked term remains legally deletable until it is deleted. Therefore:

- the terminal subsequence is independent of deletion order;
- the terminal subsequence is exactly the core;
- if (d) terms lie outside the core, every subset of those (d) terms may be deleted;
- the reachable-state graph is a Boolean lattice with (2^d) states;
- every ordering of the (d) deletable terms is a valid complete deletion history, so there are (d!) complete histories.

See [theory/FOUNDATIONS.md](theory/FOUNDATIONS.md) for proofs.

## Main research directions

The project now studies the process as mathematics in its own right, especially:

- permutation enumeration by number of survivors;
- alternating permutations and Euler zigzag numbers;
- distributions and asymptotics for random permutations;
- the rewrite-system interpretation of the comparison-sign word;
- enumeration of states, histories and constrained variants;
- circular, repeated-value and graph variants;
- connections with local extrema, alternating subsequences and related combinatorics.

## Repository map

- `authoritative/START_HERE.md` — entry point for a new session.
- `authoritative/STATE.json` — compact current research state.
- `PROJECT.md` — scope and mathematical object.
- `STATUS.md` — established results and immediate priorities.
- `theory/FOUNDATIONS.md` — proved baseline structure.
- `theory/ENUMERATION.md` — counting results and reductions.
- `literature/KNOWN_CONNECTIONS.md` — mathematical connections to investigate.
- `questions/RESEARCH_QUESTIONS.md` — open programme.
- `experiments/deletion_dynamics.py` — exhaustive computational exploration.

The project distinguishes proved results, computational evidence and conjectures. A failed literature search is never treated as proof of novelty.
