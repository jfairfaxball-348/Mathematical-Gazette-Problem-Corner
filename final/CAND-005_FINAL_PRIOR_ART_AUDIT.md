# CAND-005 — Final Exact-Form Prior-Art Audit

**Audit date:** 2026-10-05  
**Final mathematical formulation audited:** the current-neighbour strictly-between deletion rule frozen in `final/CAND-005_FORMALISATION.md`  
**Classification:** **CLEAR_WITH_RELATED_PRIOR_ART**

This is a qualified evidence assessment, not proof of originality.

## Exact mathematical kernel

For a sequence of pairwise distinct real numbers, repeatedly delete any interior term that lies strictly between its two **current** neighbours.

Equivalently, encode consecutive comparisons by a word in \(+\) and \(-\). A legal deletion is exactly
\[
++\to+,\qquad --\to-.
\]

The claim is not merely that an alternating subsequence exists. It is that **every legal asynchronous deletion order reaches the same actual subsequence**, namely the original endpoints plus original local extrema.

## Final searches

The Stage-5 audit searched the final visible wording and variants involving:

- crossing out / erasing / deleting an interior village;
- a value lying strictly between its two current neighbours;
- monotone triples and deleting their middle term;
- order independence / confluence of the deletion process;
- endpoints plus local maxima and minima;
- sign words and contractions \(++\to+\), \(--\to-\);
- run compression / run-length encoding;
- alternating or wiggle subsequences;
- consecutive monotone triples.

Source classes included the Mathematical Gazette / Problem Corner current and legacy indexing, problem/Q&A sources, Mathematics Stack Exchange, MathOverflow, AoPS-style searches, OEIS, general/algorithmic web sources, academic literature on local extrema and alternating subsequences, and generic rewriting/confluence terminology.

No empty search was treated as proof of originality.

## Closest located prior art

### 1. Dan Romik — canonical local-extrema subsequence

Dan Romik, “Local extrema in random permutations and the structure of longest alternating subsequences”, *Discrete Mathematics & Theoretical Computer Science Proceedings* AO (2011), 825–834:
https://doi.org/10.46298/dmtcs.2956

Romik shows that local extrema provide a canonical longest alternating subsequence of a sequence of distinct values. This is close to the **terminal object** of CAND-005.

Material difference: the paper studies longest alternating subsequences. It does not pose the process “delete any currently monotone middle term” or prove choice-independence of every deletion order.

### 2. Wiggle / alternating-subsequence algorithms

Standard greedy explanations for the wiggle-subsequence problem retain peaks and valleys and discard points along monotone slopes. One representative exposition is:
https://leetsolve.readthedocs.io/Greedy/376_Wiggle_Subsequence.html

This reinforces that peak/valley compression is familiar.

Material difference: the algorithmic objective is to construct or count a longest wiggle subsequence. The frozen puzzle asks whether an apparently choice-dependent **asynchronous deletion rule** is confluent and which original vertices survive under every legal order.

### 3. Consecutive monotone triples / wiggly sequences

OEIS A344654 and related entries use the condition of having no consecutive monotone triple and identify the complementary “wiggly”/alternating condition:
https://oeis.org/A344654

This is closely related to the terminal condition.

Material difference: these entries count or classify sequences/partitions with the property. They do not give the same deletion dynamics or normal-form theorem.

### 4. Generic run compression / rewriting

After the sign encoding, the rules \(++\to+\) and \(--\to-\) are a simple terminating rewrite system: every run of identical symbols reduces to one symbol.

This mechanism is elementary and not itself claimed to be new. The proposed Problem Corner contribution is the accessible village process and the observation that its arbitrary choices become this unique run compression.

## Target-journal check

Targeted searches of current Taylor & Francis indexing and legacy Mathematical Gazette indexing did not locate the exact village/sequence deletion problem or an equivalent arbitrary-order confluence statement.

That negative result is only a coverage statement. It does not establish that the problem has never appeared in the Gazette or elsewhere.

## Materiality assessment

The relationship to established local-extrema / longest-alternating-subsequence material is real and should be disclosed to the editor.

However, the final audit did **not** locate a source containing all of the following together:

1. an arbitrary current-neighbour deletion rule;
2. permission to choose any eligible term at each step;
3. the question whether the terminal actual subsequence depends on those choices; and
4. the theorem that every order leaves exactly the original endpoints and local extrema.

The distinction is mathematical rather than cosmetic: confluence of an asynchronous local rewrite is stronger than merely identifying one longest alternating subsequence.

## Limitations

- Elementary sequence-reduction puzzles are often poorly indexed and may exist in old problem books, classroom material or contest archives.
- The Gazette backfile was searched through available indexing rather than manually page-by-page.
- The relation to local-extrema/wiggle material means the idea may be folklore even if the exact problem was not located.
- Stage 2 remains an incomplete 23-record, era-biased corpus under D009.

## Final assessment

**CLEAR_WITH_RELATED_PRIOR_ART.**

CAND-005 is suitable to present to the editor with an explicit background note, but it should not be described as proved original. If the editor recognises the exact deletion/confluence problem from prior publication, the submission should yield to that evidence.


## Post-audit submitted-wording check

**Date:** 2026-10-06

After human review, the reader-facing story was changed from “cross out an interior village” to a war-and-razing formulation. The mathematical rule is unchanged: a village is eligible exactly when its altitude lies strictly between those of its two current surviving neighbours.

A targeted visible-wording check was run for combinations of villages, invasion/razing, altitude, strict betweenness, neighbours and survival. No materially equivalent formulation was located in that check. This is only a coverage note, not proof of originality.

Because the mathematical kernel is unchanged and the new visible wording produced no new material prior art in the targeted check, the classification remains **CLEAR_WITH_RELATED_PRIOR_ART**.

The submitted wording is the version now frozen in `final/CAND-005_FORMALISATION.md`.
