# Submitted Problem Corner Email

**Status:** submitted by the human author on 2026-10-06  
**To:** Chris Starr <czqstarr@gmail.com>  
**Subject:** Problem Corner proposal - Which villages survive?

The repository records the following plain-text editor-facing version. The human author's personal signature is not reproduced here.

---

Dear Chris,

I would like to propose the following problem for the Problem Corner of The Mathematical Gazette.

It is an elementary order-independence problem with a deliberately qualitative formulation. I have included the problem, a solution, and a brief note on related background below.

WHICH VILLAGES SURVIVE?

Problem

A road runs through more than two villages, all at different altitudes.

The villages are perpetually at war. At any stage, a surviving village may be invaded and razed by the surviving villages immediately before and after it along the road, provided that its altitude lies strictly between theirs.

Once a village has been razed, it disappears, so its two attackers become neighbours. The wars continue, with any eligible village being razed at each stage, until no further attack is possible.

Does the final collection of surviving villages depend on the order in which the attacks take place? Which villages ultimately survive?


Solution

The final collection does not depend on the order of the attacks.

As we travel along the road, describe each step from one surviving village to the next as either UP or DOWN, according to whether the altitude increases or decreases.

A village can be razed precisely when the road is going in the same direction on both sides of it. Thus either the road goes UP to the village and then UP again, or it goes DOWN to the village and then DOWN again.

When such a village is removed, two consecutive UP steps become a single UP step, or two consecutive DOWN steps become a single DOWN step.

Therefore every attack merely shortens a stretch in which the road is continually rising or continually falling. It can never remove a village at which the direction changes from rising to falling or from falling to rising.

Eventually, every continually rising or continually falling stretch has been reduced as far as possible. The villages that remain are therefore exactly the first and last villages, together with every village that was originally a local peak or a local valley.

Hence the same villages survive regardless of the order in which the attacks take place.


Background

There is a known connection between local extrema and alternating subsequences. In particular, Dan Romik discusses how the local extrema of a sequence give a canonical longest alternating subsequence in:

D. Romik, "Local extrema in random permutations and the structure of longest alternating subsequences", Discrete Mathematics & Theoretical Computer Science Proceedings, AO (2011), 825-834.

The formulation above is instead an arbitrary sequential elimination process: at each stage any currently eligible village may be razed, and the question is whether different choices can lead to different terminal collections.

I have not found this particular dynamic formulation or the associated order-independence question in the literature, although the underlying appearance of local maxima and minima is clearly related to the alternating-subsequence observation above.

I hope the problem may be suitable for the Problem Corner.

Best wishes,

[human author's signature]
