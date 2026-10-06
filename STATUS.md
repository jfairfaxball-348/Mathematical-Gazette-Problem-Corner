# Status

**As of:** 2026-10-06

## Overall

- Stage 1 — Scaffold / Bootstrap: **PASSED / COMPLETE**
- Stage 2 — Research: **CLOSED BY HUMAN OVERRIDE; ORDINARY GATE NOT PASSED**
- Stage 3 — Discovery: **PASSED / COMPLETE**
- Stage 4 — Prior-art / Novelty Audit: **PASSED / COMPLETE**
- Stage 5 — Formalisation and Submission Package: **PASSED / COMPLETE**
- Submission: **SENT BY HUMAN AUTHOR ON 2026-10-06**

Decisions **D012** and **D013** record the Stage-5 candidate switch and gate pass. Decision **D014** records the final wording revision and human submission.

## Stage-2 limitation carried forward

The research catalogue remains at **23 structured, solution-reviewed Problem Corner records**, with known era imbalance and incomplete synthesis. D009 remains an exception to the Stage-2 gate, not evidence that the missing research was completed.

## Stage-5 candidate outcome

Stage 5 began with **CAND-010 — How far is everyone’s nearest neighbour?** Its mathematics survived independent re-derivation, but the final novelty audit located materially equivalent older linear nearest-neighbour analysis. CAND-010 was therefore retired as **REDISCOVERY**.

The reserve **CAND-005 — Which villages survive?** was promoted and passed Stage 5.

## Final submitted problem

**Selected and submitted:** **CAND-005 — Which villages survive?**

**Reserve:** none.

The final reader-facing wording is deliberately qualitative. A road runs through more than two villages at different altitudes. The villages are perpetually at war. A surviving village may be invaded and razed by the surviving villages immediately before and after it whenever its altitude lies strictly between theirs. When it disappears, its attackers become neighbours.

The question asks whether the eventual survivors depend on the order of attacks and which villages ultimately survive.

The theorem is unchanged: every legal attack order produces the same survivors — the first and last villages together with exactly the original local peaks and local valleys.

The editor-facing solution now uses plain-text **UP/DOWN** language rather than mathematical sign notation, so it survives ordinary email copying cleanly.

## Mathematical validation

The UP/DOWN argument is the same run-compression proof previously expressed with plus and minus signs. Every legal attack shortens a continually rising or continually falling stretch; a change from rising to falling or falling to rising cannot disappear.

A maximal-monotone-run proof remains as an alternative validation.

Exhaustive computation over all **46,232 permutations of lengths 2 through 8**, exploring every legal branch, agreed with the theorem. The proof, not the computation, establishes the general result.

## Final novelty position

CAND-005 remains **CLEAR_WITH_RELATED_PRIOR_ART**.

Materially related prior art includes Dan Romik's work showing that local extrema form a canonical longest alternating subsequence and standard wiggle-subsequence material retaining peaks and valleys.

The original Stage-5 audit did not locate the exact arbitrary-order current-neighbour deletion/confluence problem. After the story was revised, a targeted visible-wording check for the war-and-razing formulation likewise found no material match. Neither negative search is treated as proof of originality.

## Submission

The user confirmed that the proposal was submitted on **2026-10-06** to **Chris Starr**, the Problem Corner editor.

The repository records this as a **human submission**. ChatGPT did not send the email.

The final submitted wording, solution and background are recorded in `final/SUBMISSION_PACKAGE.md` and the plain-text email version in `final/SUBMISSION_EMAIL.md`.

## Next action

Await the editor's response. Record any reply, prior-art identification, request for revision, acceptance, rejection, or other disposition before changing the final package again.
