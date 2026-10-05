# Status

**As of:** 2026-10-05

## Overall

- Stage 1 — Scaffold / Bootstrap: **PASSED / COMPLETE**
- Stage 2 — Research: **CLOSED BY HUMAN OVERRIDE; ORDINARY GATE NOT PASSED**
- Stage 3 — Discovery: **PASSED / COMPLETE**
- Stage 4 — Prior-art / Novelty Audit: **PASSED / COMPLETE**
- Stage 5 — Formalisation and Submission Package: **PASSED / COMPLETE**

Decisions **D012** and **D013** record the Stage-5 candidate switch and final gate pass.

## Stage-2 limitation carried forward

The research catalogue remains at **23 structured, solution-reviewed Problem Corner records**, with known era imbalance and incomplete synthesis. D009 remains an exception to the Stage-2 gate, not evidence that the missing research was completed.

## Stage-5 candidate outcome

Stage 5 began with the Stage-4 primary **CAND-010 — How far is everyone’s nearest neighbour?**

Its mathematics survived independent re-derivation. For ordered positions with positive consecutive gaps summing to the fixed span, the nearest-neighbour total is bounded by the span plus the smallest gap, giving the sharp value \(nL/(n-1)\). Equality forces every gap to be equal, so equal spacing is the unique maximiser.

However, the required final novelty audit located materially equivalent older **linear nearest-neighbour analysis**. That literature uses the same sum of pointwise nearest-neighbour distances on a line and normalises it so that perfectly regular spacing has the extremal score. CAND-010 is therefore retired in Stage 5 as **REDISCOVERY**. The Stage-4 audit remains preserved as the record of what was known at that gate.

Per the reserve rule, **CAND-005 — Which villages survive?** was then promoted.

## Final selected problem

**Selected:** **CAND-005 — Which villages survive?**

**Reserve:** none.

The canonical statement asks about repeatedly crossing out an interior village whose altitude lies strictly between those of its two neighbours still on the list.

The final theorem is that every legal deletion order has the same terminal list: the two endpoint villages together with exactly the original strict local maxima and local minima.

The primary proof encodes successive altitude changes by signs. A legal deletion is exactly the contraction \(++\to+\) or \(--\to-\), so every maximal sign-run contracts to one sign and the normal form is unique. A direct maximal-monotone-run proof is retained as a useful alternative.

Exhaustive computation over all **46,232 permutations of lengths 2 through 8**, exploring every legal deletion branch, agreed with the theorem. The proof, not the computation, establishes the general result.

## Final novelty position

CAND-005 is **CLEAR_WITH_RELATED_PRIOR_ART**.

Materially related prior art includes Dan Romik's work showing that local extrema form a canonical longest alternating subsequence, standard wiggle-subsequence algorithms that retain peaks and valleys, and the familiar notion of an alternating/wiggly sequence with no consecutive monotone triple.

The Stage-5 audit did not locate the exact dynamic problem in which **any currently eligible** middle term may be deleted and every deletion order is proved to reach the same actual subsequence. This supports a qualified submission position only; it does not prove originality.

## Reader testing

No independent human reader was available during the session. This limitation is explicit. An internal adversarial wording review led to the phrase **“the two neighbouring villages still on the list”**, which removes the main ambiguity after earlier deletions.

## Submission package

Prepared in \`final/\`:
- canonical statement and rigorous primary solution;
- useful alternative solution;
- edge-case/adversarial checks;
- computational validation note;
- exact-form final prior-art audit;
- editor background/prior-art disclosure;
- submission-ready package;
- concise email draft.

Current official Problem Corner proposal guidance was rechecked on 2026-10-05. It asks that proposals be sent to Chris Starr with solutions and relevant background information.

**Nothing has been sent.**

## Recommended next action

Human review of the CAND-005 package, especially the qualified novelty disclosure. If satisfied, send the problem, solution and background note to the Problem Corner editor.
