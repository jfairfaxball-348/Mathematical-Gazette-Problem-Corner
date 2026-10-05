# CAND-005 — Formalisation and Validation

**Final title:** Which villages survive?  
**Status:** canonical statement frozen  
**Final novelty classification:** `CLEAR_WITH_RELATED_PRIOR_ART`

## Canonical reader-facing statement

> A road passes through villages (V_1,V_2,ldots,V_n), in that order, where (nge2) and no two villages have the same altitude. At any stage, you may cross out an interior village if its altitude lies strictly between those of its two neighbouring villages still on the list. Continue until no more villages can be crossed out. Does the final list depend on the choices made? Which villages survive?

The phrase **“still on the list”** is intentional: after deletions, eligibility is judged using the current neighbours.

## Theorem

Let the altitudes be pairwise distinct real numbers (h_1,ldots,h_n).

Every legal sequence of deletions terminates in the same list. The survivors are exactly (V_1,V_n) together with every original strict local maximum or strict local minimum (V_i), (2le ile n-1).

Thus an interior (V_i) survives precisely when
[
h_{i-1}<h_i>h_{i+1}
quad	ext{or}quad
h_{i-1}>h_i<h_{i+1}.
]

## Primary solution — signs and run compression

Write a sign between each pair of consecutive villages:
[
s_i=
egin{cases}
+,&h_{i+1}>h_i,\
-,&h_{i+1}<h_i.
end{cases}
]
Because all altitudes are distinct, every sign is (+) or (-).

Consider three consecutive villages currently remaining, with altitudes (a,b,c). The middle one is eligible exactly when (b) lies strictly between (a) and (c). This happens exactly when (a<b<c) or (a>b>c), so the two adjacent signs are equal.

If the middle village is deleted, those two signs are replaced by the single sign from (a) to (c). Hence a legal move is exactly
[
++longrightarrow +,
qquad
--longrightarrow -.
]

Each move merely shortens one maximal run of equal signs. It can neither cross nor remove a boundary between a (+)-run and a (-)-run.

The process terminates because every move removes one village. It stops exactly when no two adjacent signs are equal, so every original maximal sign-run has been shortened to one sign.

That reduced sign word is independent of the order of contractions. Its vertices are the two original endpoints together with the original vertices where the sign changes. A sign change is exactly an original strict local maximum or local minimum.

Therefore every legal deletion order leaves the same actual villages: the endpoints and the original local extrema.

## Alternative solution — maximal monotone runs

Mark the two endpoints and every original local maximum and local minimum.

Between two consecutive marked villages, the original altitude sequence is strictly monotone. These intervals are the maximal monotone runs.

A marked interior village can never be deleted. If it is a local maximum, every surviving village immediately to its left and right lies below it; if it is a local minimum, both lie above it. So it never lies between its current neighbours.

Within a maximal monotone run, deleting an interior village preserves strict monotonicity of the remaining villages in that run. If a terminal list retained any unmarked interior village of such a run, that village would still lie strictly between its two current neighbours and would still be deletable, a contradiction.

Hence each maximal monotone run is reduced to its two marked endpoints. Joining the runs shows that the final list is exactly the endpoints plus original local extrema, independently of deletion order.

This proof is retained because it gives a direct geometric interpretation of the sign-word proof.

## Adversarial checks

### Termination

Every move removes exactly one village, so no infinite deletion sequence is possible.

### Small cases

- (n=2): there is no interior village; both villages remain.
- (n=3): if the three altitudes are monotone, the middle village is deleted. If the middle is a local maximum or minimum, all three remain.
- (n=4): the sign words (+++), (++-), (+--), (+-+) (and reversals) reduce exactly as predicted by their sign-runs.

### Distinct altitudes

The pairwise-distinct hypothesis is deliberate. It avoids zero signs and makes “strictly between” equivalent to two equal adjacent signs. Allowing ties creates a different problem requiring an additional rule and is not part of the submission.

### Current versus original neighbours

Eligibility always uses the two neighbours **still on the list**. The theorem nevertheless identifies the terminal villages using local extrema in the **original** list.

### Actual vertices, not just a sign pattern

The proof does more than show that the final signs alternate. Boundaries between original sign-runs cannot be deleted, while every internal vertex of a sign-run must disappear before termination. Hence the same original villages survive.

### No hidden geometric assumptions

Only the order of the villages along the road and comparisons of their altitudes matter. Horizontal distances, gradients and units of altitude play no role.

## Computational validation

As supporting evidence, not as a substitute for proof, every permutation of lengths (2) through (8) was checked.

For each permutation, the computation recursively explored **every legal deletion choice** and collected all terminal lists. In all cases there was exactly one terminal list, and it matched the endpoints plus the original local maxima and minima.

The test covered
[
2!+3!+4!+5!+6!+7!+8!=46{,}232
]
distinct order types.

Since only relative altitude order matters, permutations are the natural finite test cases for sequences of distinct real altitudes.

## Reader-testing note

No independent human reader was available in this session, so no external reader-testing result is claimed.

An internal adversarial wording review identified the main possible ambiguity—whether “neighbours” meant original or current neighbours. The canonical statement now explicitly says **“the two neighbouring villages still on the list.”**

Other points checked internally:

- the stopping condition is explicit;
- (nge2) avoids an unnecessary one-village convention;
- equal altitudes are excluded explicitly;
- “which villages survive?” makes clear that the actual original villages, not merely the final number, are sought.

This limitation should remain visible if the package is reviewed later.
