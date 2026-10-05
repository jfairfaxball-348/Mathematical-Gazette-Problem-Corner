# CAND-010 — Stage-5 Failure Record

**Candidate:** How far is everyone’s nearest neighbour?  
**Stage-4 status:** primary; `CLEAR_WITH_RELATED_PRIOR_ART`  
**Stage-5 outcome:** **RETIRED — REDISCOVERY**  
**Reason:** final prior-art audit, not mathematical failure

## Frozen Stage-3 problem

> There are (n\ge2) houses at distinct positions along a straight road, with the two outermost houses exactly one mile apart. Each household records the distance to its nearest other house. What is the largest possible value of the sum of the (n) recorded distances?

The proposed answer was (n/(n-1)) miles.

## Independent mathematical recheck

Let
[
x_1<x_2<\cdots<x_n,\qquad x_n-x_1=L,
]
and put (m=n-1) and (d_i=x_{i+1}-x_i>0). Then (sum d_i=L).

The nearest-neighbour total is
[
S=d_1+d_m+sum_{i=1}^{m-1}min(d_i,d_{i+1}).
]

For (n=2), the minimum-sum is empty and the two houses each record (L), so (S=2L).

## Cleaner sharp proof

Choose (k) with (d_k=\delta=min_i d_i). For (i<k),
[
min(d_i,d_{i+1})\le d_{i+1},
]
while for (i\ge k),
[
min(d_i,d_{i+1})\le d_i.
]
Therefore
[
S\le d_1+d_m+sum_{i=1}^{k-1}d_{i+1}+sum_{i=k}^{m-1}d_i
=sum_{i=1}^{m}d_i+d_k=L+\delta.
]
Since (delta\le L/m),
[
S\le L+rac{L}{m}=rac{nL}{n-1}.
]

Equality in the last inequality requires (delta=L/m). Since every gap is at least (delta) and their sum is (mdelta), every gap must equal (L/m).

Thus **equal spacing is the unique maximising configuration up to translation**. The maximum is attained, not merely approached.

## Total-variation route also verified

With
[
\operatorname{TV}(d)=sum_{i=1}^{m-1}|d_{i+1}-d_i|,
]
the identity (2min(a,b)=a+b-|a-b|) gives
[
S=L+rac{d_1+d_m-\operatorname{TV}(d)}2.
]
If (d_k=delta), then
[
\operatorname{TV}(d)\ge(d_1-delta)+(d_m-delta),
]
again yielding (S\le L+delta\le nL/(n-1)).

The direct minimum-gap proof is cleaner.

## Edge cases and ambiguities

- (n=2): (S=2L), matching the formula.
- (n=3): with gaps (a,L-a), (S=L+min(a,L-a)\le3L/2), uniquely at (a=L/2).
- (n=4): (S\le4L/3), uniquely at three equal gaps.
- Distinct houses mean every gap is strictly positive.
- Nearest-neighbour ties need no convention because only the nearest **distance** is recorded.
- No assumption about the road beyond the two outer houses is needed.
- Gaps tending to zero do not create a larger supremum.

The candidate failed for novelty, not correctness.

## Fatal Stage-5 prior art

The final audit broadened beyond modern remote-pseudoforest / sum-min terminology and found an older literature on **linear nearest-neighbour analysis**.

D. A. Pinder and M. E. Witherick published “Nearest-neighbour analysis of linear point patterns”, *Tijdschrift voor Economische en Sociale Geografie* 64(3) (1973), 160–163:
https://doi.org/10.1111/j.1467-9663.1973.tb00077.x

They followed it with “A modification of nearest-neighbor analysis for use in linear situations”, *Geography* 60 (1975), 16–23. The literature was later reconsidered by B. L. Stark and D. L. Young, “Linear Nearest Neighbor Analysis”, *American Antiquity* 46(2) (1981), 284–300:
https://doi.org/10.2307/280209

A later application by Samuel M. Wilson, “The Prehistoric Settlement Pattern of Nevis, West Indies”, *Journal of Field Archaeology* 16 (1989), explicitly gives the Pinder–Witherick statistic as
[
rac{2(n-1)}n,rac1L,(M_1+M_2+\cdots+M_n),
]
where (M_i) is the nearest-neighbour distance for point (i), and states that value (2) represents perfectly regular spacing:
https://latinamericanstudies.org/ancient/JFA-1989.pdf

Algebraically, score (2) is exactly
[
M_1+\cdots+M_n=rac{nL}{n-1},
]
the frozen CAND-010 answer, with regular spacing as the extremal arrangement.

This is materially equivalent prior art for the same one-dimensional nearest-neighbour total and extremal endpoint. An independently found short proof does not rescue the proposed problem.

## Decision

CAND-010 is retired as **REDISCOVERY** in Stage 5. No cosmetic change of the house/road story is used to evade the prior art.

Per the frozen reserve discipline, CAND-005 was promoted for full Stage-5 formalisation.
