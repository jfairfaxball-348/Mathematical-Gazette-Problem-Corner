# Draft Submission Email

**Status:** draft only — not sent

**To:** Chris Starr <czqstarr@gmail.com>  
**Subject:** Problem Corner proposal — Which villages survive?

Dear Chris Starr,

I would like to propose the following problem for *The Mathematical Gazette* Problem Corner.

> A road passes through villages \(V_1,V_2,\ldots,V_n\), in that order, where \(n\ge2\) and no two villages have the same altitude. At any stage, you may cross out an interior village if its altitude lies strictly between those of its two neighbouring villages still on the list. Continue until no more villages can be crossed out. Does the final list depend on the choices made? Which villages survive?

I have included a complete solution and a short background note. The key observation is to encode successive altitude changes by \(+\) and \(-\): each legal deletion is exactly \(++\to+\) or \(--\to-\), so the final list is independent of the choices and consists of the endpoints together with the original local maxima and minima.

For background, local extrema as a canonical longest alternating subsequence are established (for example, Dan Romik, *DMTCS Proceedings*, 2011, DOI 10.46298/dmtcs.2956). I have not located the exact arbitrary-order deletion/confluence formulation in targeted searches, but I include that relationship rather than making an unqualified originality claim.

Best wishes,

[Name]
