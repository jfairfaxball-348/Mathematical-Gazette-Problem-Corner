# Foundations

## 1. Definitions

Let
[
x=(x_1,ldots,x_n)
]
be pairwise distinct real numbers.

In any current surviving subsequence
[
y=(y_1,ldots,y_m),
]
an interior term (y_i) is **deletable** if
[
y_{i-1}<y_i<y_{i+1}
quad	ext{or}quad
y_{i-1}>y_i>y_{i+1}.
]

Equivalently, (y_i) lies strictly between its current neighbours.

For the original sequence, an interior index (i) is a **local extremum** when
[
x_{i-1}<x_i>x_{i+1}
quad	ext{or}quad
x_{i-1}>x_i<x_{i+1}.
]

Define the **core**
[
C={1,n}cup{i: i	ext{ is an original local extremum}}
]
for (nge2). For (n=1), the sole index is the core.

## 2. Order type is sufficient

A strictly increasing transformation preserves all comparisons and therefore every legal move. Replacing the values by their ranks gives a permutation with exactly the same deletion dynamics.

Thus the base problem is fundamentally a problem about permutations.

## 3. Comparison-word formulation

For (nge2), define
[
s_i=
egin{cases}
+,&x_i<x_{i+1},\\
-,&x_i>x_{i+1}.
end{cases}
]

An original local extremum occurs exactly where (s_{i-1}
e s_i).

A legal deletion occurs exactly when the two adjacent current signs agree. Deleting the middle term contracts
[
++	o+,
qquad
--	o-.
]

So the sign dynamics are run compression: every maximal run of equal signs eventually contracts to one sign.

## 4. Permanent-core theorem

**Theorem.** Every original endpoint and every original local extremum survives every legal deletion history.

**Proof.** Endpoints can never be selected.

Consider an original local maximum (x_i). The original sequence increases into (x_i) along its maximal increasing run on the left and decreases away from (x_i) along its maximal decreasing run on the right. Any surviving term to its left within the adjacent run is below (x_i), and any surviving term to its right within the adjacent run is also below (x_i). Hence whenever (x_i) has current neighbours on both sides, both are below it, so (x_i) never lies between them. The local-minimum case is symmetric. ∎

## 5. Strong deletability theorem

**Theorem.** Every original term outside the core remains legally deletable at every state in which it is still present.

**Proof.** A non-core term lies strictly inside one maximal monotone run whose endpoints belong to the core. Suppose the run is increasing; the decreasing case is symmetric.

At any later state, the nearest surviving term to the left of the chosen term within that run is smaller, and the nearest surviving term to the right is larger. Core endpoints of the run never disappear, so both neighbours exist. Therefore the chosen term still lies strictly between its current neighbours and remains deletable. ∎

This strengthens ordinary confluence: legality does not merely survive in some order; every not-yet-deleted non-core term is legal at all times.

## 6. Complete description of the state space

Let (d=n-|C|) be the number of non-core terms.

**Corollary.** A subsequence is reachable if and only if it contains every core term.

Indeed, choose any subset (D) of the non-core terms and delete exactly the elements of (D), in any order. Strong deletability guarantees that every step is legal.

Therefore the reachability poset is the Boolean lattice (B_d):

- number of reachable states: (2^d);
- number of states after exactly (r) deletions: (inom dr);
- number of ordered legal histories of length (r):
  [
  d(d-1)cdots(d-r+1)=rac{d!}{(d-r)!};
  ]
- number of complete deletion histories: (d!).

## 7. Unique terminal subsequence

The process stops exactly when no non-core terms remain. Hence every complete history ends at the same subsequence: the core.

If the original sign word has (c) sign changes, then it has (c+1) constant-sign runs, and for (nge2)
[
|C|=c+2.
]

Equivalently, the terminal sign word is obtained by replacing every maximal block of (+)'s or (-)'s by a single sign.

## 8. Extremal cases

For (nge2):

- **All terms survive** iff the signs alternate, equivalently every interior term is a local extremum.
- **Only the two endpoints survive** iff the original sequence is strictly monotone.

The first condition is the classical alternating-permutation condition after rank normalisation.

## 9. A useful probabilistic consequence

Let a permutation of length (n) be uniformly random. Each interior position is a local extremum with probability (2/3): among the six possible relative orders of a consecutive triple, the middle entry is largest or smallest in four.

By linearity of expectation, for (nge2),
[
mathbb E[|C|]
=2+(n-2)rac23
=rac{2n+2}{3}.
]

No independence assumption is needed for this expectation.
