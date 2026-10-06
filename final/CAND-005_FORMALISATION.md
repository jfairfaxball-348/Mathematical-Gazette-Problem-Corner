# CAND-005 — Formalisation and Validation

**Final title:** Which villages survive?  
**Status:** canonical submitted statement frozen  
**Final novelty classification:** `CLEAR_WITH_RELATED_PRIOR_ART`  
**Submission status:** submitted by the human author on 2026-10-06

## Canonical reader-facing statement

> A road runs through more than two villages, all at different altitudes.
>
> The villages are perpetually at war. At any stage, a surviving village may be invaded and razed by the surviving villages immediately before and after it along the road, provided that its altitude lies strictly between theirs.
>
> Once a village has been razed, it disappears, so its two attackers become neighbours. The wars continue, with any eligible village being razed at each stage, until no further attack is possible.
>
> Does the final collection of surviving villages depend on the order in which the attacks take place? Which villages ultimately survive?

The phrase **“surviving villages immediately before and after it along the road”** is intentional: after a village has been razed, eligibility is judged using the current surviving neighbours.

The road need not be straight. Only the order of the villages along the road and their relative altitudes matter.

## Theorem

Every legal sequence of attacks terminates with the same villages.

The survivors are exactly:

- the first village on the road;
- the last village on the road; and
- every village that was originally a local peak or a local valley.

Equivalently, an interior village survives precisely when it was originally higher than both of its neighbours or lower than both of them.

## Primary solution — UP and DOWN

As we travel along the road, describe each step from one surviving village to the next as either **UP** or **DOWN**, according to whether the altitude increases or decreases.

A village can be razed precisely when the road is going in the same direction on both sides of it. Thus either the road goes UP to the village and then UP again, or it goes DOWN to the village and then DOWN again.

When such a village is removed, two consecutive UP steps become a single UP step, or two consecutive DOWN steps become a single DOWN step.

Therefore every attack merely shortens a stretch in which the road is continually rising or continually falling. It can never remove a village at which the direction changes from rising to falling or from falling to rising.

Eventually, every continually rising or continually falling stretch has been reduced as far as possible. The villages that remain are therefore exactly the first and last villages, together with every village that was originally a local peak or a local valley.

Hence the same villages survive regardless of the order in which the attacks take place.

## Alternative solution — maximal monotone runs

Mark the two endpoint villages and every original local peak and local valley.

Between two consecutive marked villages, the original altitude sequence is strictly increasing throughout or strictly decreasing throughout. A marked peak can never be razed because its surviving neighbours on both sides remain below it; similarly, a marked valley always has surviving neighbours above it.

Within one of the continually rising or falling stretches, razing an eligible village leaves the remaining stretch still continually rising or falling. If any unmarked interior village remained when the wars stopped, it would still lie strictly between its two surviving neighbours and would therefore still be eligible to be razed.

So each such stretch is eventually reduced to its two marked endpoints. The final survivors are therefore exactly the endpoints and original peaks and valleys, independently of attack order.

## Adversarial checks

### Termination

Every attack razes exactly one village, so the process must stop.

### Small cases

The submitted wording assumes more than two villages.

- With three villages in monotone altitude order, the middle village is razed.
- With three villages where the middle is a peak or a valley, all three survive.
- With four or more villages, the same UP/DOWN reduction applies without change.

The theorem also extends harmlessly to the two-village case, although that case is deliberately excluded from the reader-facing wording.

### Distinct altitudes

All altitudes are required to be different. This avoids equality cases and makes “strictly between” unambiguous.

### Current versus original neighbours

Attack eligibility always uses the villages currently surviving immediately before and after the target. The theorem nevertheless identifies the final survivors in terms of peaks and valleys in the **original** configuration.

### No hidden geometric assumptions

The road may curve or wind. Horizontal distances, gradients, and the physical shape of the road are irrelevant; only village order and altitude comparisons are used.

## Computational validation

As supporting evidence, not as a substitute for proof, every permutation of lengths 2 through 8 was checked before submission.

For each permutation, every legal deletion branch was explored. In all 46,232 order types, there was exactly one terminal collection, and it matched the endpoints plus the original local peaks and valleys.

## Reader-review note

No independent human reader test was available during Stage 5. Subsequent human review of the wording led to the final qualitative war-and-razing formulation above and to the plain-language UP/DOWN solution used in the submitted package.

The mathematical rule did not change: a village is eligible exactly when its altitude lies strictly between those of its two current surviving neighbours.
