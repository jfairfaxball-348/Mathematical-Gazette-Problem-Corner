# Problem Corner Submission Package

## Proposed title

**Which villages survive?**

## Problem

A road passes through villages (V_1,V_2,ldots,V_n), in that order, where (nge2) and no two villages have the same altitude. At any stage, you may cross out an interior village if its altitude lies strictly between those of its two neighbouring villages still on the list. Continue until no more villages can be crossed out.

**Does the final list depend on the choices made? Which villages survive?**

## Solution

Let the altitude of (V_i) be (h_i). Put a (+) sign between (V_i) and (V_{i+1}) when (h_{i+1}>h_i), and a (-) sign when (h_{i+1}<h_i).

A current middle village is eligible for deletion exactly when its two adjacent signs are equal: its three current altitudes are then strictly increasing or strictly decreasing.

Deleting it replaces
[
++quad	ext{by}quad +,
qquad	ext{or}qquad
--quad	ext{by}quad -.
]

Thus every move merely shortens one run of identical signs. Whatever choices are made, each original run is eventually reduced to one sign, and boundaries between (+)-runs and (-)-runs can never disappear.

Consequently the terminal sign word is unique. Its vertices are the two endpoints together with the vertices at which the original sign changes. Those are exactly the original local maxima and local minima.

So the final list is independent of all choices: **the survivors are (V_1,V_n) and precisely the original strict local maxima and local minima.**

## Alternative view

Mark the endpoints and every original local extremum. Consecutive marked villages bound a maximal strictly monotone run.

A marked local maximum can never become deletable, because its current neighbours on both sides remain below it; similarly a marked local minimum always has both current neighbours above it. Within any monotone run, deleting an interior village preserves monotonicity. A terminal list cannot leave an unmarked interior village in such a run, because it would still lie between its current neighbours.

Hence every maximal monotone run reduces to its two marked endpoints, giving the same survivor set.

## Background for the editor

The terminal set is related to established work on alternating subsequences. In particular, Dan Romik showed that local extrema form a canonical longest alternating subsequence:

Dan Romik, “Local extrema in random permutations and the structure of longest alternating subsequences”, *DMTCS Proceedings* AO (2011), 825–834, DOI:
https://doi.org/10.46298/dmtcs.2956

Standard wiggle-subsequence algorithms likewise retain peaks and valleys while discarding interior points of monotone slopes.

The proposed problem is more specific in a different direction: it gives an asynchronous local deletion rule and asks whether **every** sequence of legal choices reaches the same actual subsequence. Targeted Stage-5 searches did not locate that exact deletion/confluence formulation.

Accordingly the project classifies the novelty position as **CLEAR_WITH_RELATED_PRIOR_ART**, not unqualified clear/original. The detailed audit is in `final/CAND-005_FINAL_PRIOR_ART_AUDIT.md`.

## Validation

The sign-word proof is exact for all (nge2).

As a supporting check, all 46,232 permutations of lengths 2 through 8 were exhaustively reduced through every legal deletion branch; every case had a unique terminal list equal to the endpoints plus original local extrema.

No independent human reader test was available during preparation. The wording was adversarially reviewed internally; “the two neighbouring villages still on the list” was added to remove the main interpretation ambiguity.

## Current Problem Corner proposal instructions

Rechecked 2026-10-05 against the current Taylor & Francis Problem Corner page published online 20 August 2026:
https://www.tandfonline.com/doi/full/10.1080/00255572.2026.2714697

The page says that proposals for problems are welcome, should be sent to **Chris Starr** at **czqstarr@gmail.com** (or the listed postal address), and should be accompanied by **solutions and any relevant background information**.

The solution deadline printed for the currently posed problems is not treated here as a proposal deadline.

**This package has not been sent.**
