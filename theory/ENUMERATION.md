# Enumeration

Throughout, permutations are of ({1,ldots,n}).

## 1. Survivor count and sign changes

For a permutation (pi), let
[
K(pi)=	ext{number of terminal survivors}.
]

For (nge2),
[
K(pi)=2+#{i: s_i
e s_{i+1}},
]
where (s_i) is the up/down sign between consecutive entries.

Thus counting permutations by survivor number is exactly the problem of counting permutations by the number of changes in their up/down word. Equivalently, if the sign word has (r) maximal constant-sign runs, then
[
K=r+1.
]

This connects the project directly to the classical enumeration of permutations by alternating or up-down runs.

## 2. All-survive permutations

Every term survives iff the permutation alternates:
[
pi_1<pi_2>pi_3<pi_4>cdots
]
or
[
pi_1>pi_2<pi_3>pi_4<cdots.
]

Let (E_n) denote the Euler zigzag number counting one of these two orientations. For (nge2), the orientations are disjoint and equally numerous, so
[
A_n=2E_n
]
permutations have all (n) terms survive.

For (n=9),
[
E_9=7936,
qquad
A_9=15872.
]

One example is
[
1,9,2,8,3,7,4,6,5.
]

Another is
[
3,8,1,6,2,9,4,7,5.
]

## 3. Only-endpoints permutations

Only the endpoints survive iff there are no sign changes, so the permutation is monotone.

For every (nge2), there are exactly two:
[
1,2,ldots,n
quad	ext{and}quad
n,n-1,ldots,1.
]

## 4. Mean survivor count

For a uniformly random permutation,
[
mathbb E[K]=rac{2n+2}{3}.
]

Equivalently, the expected number of deleted terms is
[
n-mathbb E[K]=rac{n-2}{3}.
]

## 5. Main enumeration problem

Define
[
a(n,k)=#{piin S_n:K(pi)=k}.
]

The immediate goals are to:

1. identify (a(n,k)) precisely with a standard alternating-run number convention;
2. record a clean recurrence;
3. derive or cite its generating polynomial;
4. obtain moments and asymptotics from the known distribution;
5. verify all formulas computationally against `experiments/deletion_dynamics.py`.

Care is required because the literature uses several conventions for “alternating runs”, especially concerning whether the first direction is counted as a run and how (n=1) is handled.
