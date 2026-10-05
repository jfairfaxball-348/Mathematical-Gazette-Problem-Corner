# Stage Gate Ledger

A stage normally may be declared complete only when every required item for that gate is satisfied. “Mostly done” is not a pass. Any explicit human-authorized exception must be recorded in `authoritative/DECISION_LOG.md` and must preserve the unmet requirements rather than silently marking them complete.

## Stage 1 — Scaffold / Bootstrap

**Status: PASSED (2026-10-05).**

Requirements:

- [x] Repository structure is coherent.
- [x] Project objective and sole publication target are unambiguous.
- [x] Central design principle and explicit non-objectives are frozen.
- [x] Five-stage roadmap is frozen.
- [x] Current publication-target facts are documented from authoritative sources.
- [x] Candidate-quality rubric is frozen.
- [x] Stage-2 corpus schema exists.
- [x] Stage-3 candidate schema exists.
- [x] Stage-3 diversity control exists.
- [x] Stage-4 novelty-audit schema exists.
- [x] Authority/navigation files are consistent.
- [x] Later agents are instructed not to silently redefine project success.
- [x] No substantive candidate discovery occurred prematurely.

## Stage 2 — Research

**Status: CLOSED BY HUMAN OVERRIDE (2026-10-05); ordinary gate NOT PASSED.**

Ordinary pass requirements were:

- [ ] A substantial Problem Corner corpus has been reviewed: at least roughly 60 problems, preferably 80–100.
- [x] Published solutions are reviewed as well as problem statements wherever accessible.
- [x] Coverage spans multiple years and issues, with deliberate variety of mathematical type and presentation.
- [x] Each included item has a structured catalogue record with provenance.
- [ ] The corpus is sufficiently balanced that one era, editor, or mathematical area does not dominate by accident.
- [ ] A quantitative/qualitative synthesis reports typical statement length, accessibility, prerequisites, difficulty, solution length/style, multiple-solution practice, contextual versus abstract presentation, and recurring mechanisms.
- [ ] The synthesis identifies common sources of surprise and features worth emulating or avoiding.
- [ ] The synthesis explicitly contrasts Problem Corner with olympiad exercises, textbook exercises, and generic internet puzzles.
- [ ] An evidence-based Stage-3 design specification is written.
- [x] Corpus limitations and access gaps are documented.
- [x] No serious candidate-generation campaign began before these requirements were met.

Current evidence at closure: 23 solution-reviewed records. The principal unresolved sampling issue is that 20 of 23 are Chris Starr-era and only 3 are Nick Lord-era. The requested older-corpus tranche, roughly-60 minimum, balanced sampling, final synthesis, genre comparison and evidence-based Stage-3 design specification were incomplete. Per explicit human instruction recorded as decision D009, Stage 2 was nevertheless closed and Stage 3 unlocked. The unchecked requirements above remain genuinely unmet and are not retroactively treated as satisfied.

## Stage 3 — Discovery

**Status: PASSED (2026-10-05; D010).**

Requirements:

- [x] Candidate generation is based explicitly on Stage-2 findings.
- [x] The pool is broad and diverse, up to roughly 50 serious candidates without padding.
- [x] Every serious candidate has a complete structured record using the candidate schema.
- [x] Each serious candidate has a plausible expected answer and solution mechanism, not merely an appealing story.
- [x] Basic mathematical soundness checks have been performed.
- [x] The diversity tracker shows that cosmetic variants have not been counted as distinct serious candidates.
- [x] Candidates have been assessed against the frozen quality rubric.
- [x] Weak, unsound, derivative-looking, or structurally repetitive candidates are rejected or demoted with reasons.
- [x] A clearly defined set of “serious Stage-3 candidates” is frozen for exhaustive Stage-4 audit.

Gate evidence: 31 substantially explored seeds; 10 frozen serious candidates; 17 rejected; 4 merged variants. The frozen records are in `candidates/serious-candidates.jsonl`, with discovery/validation evidence in `candidates/STAGE3_DISCOVERY_NOTES.md` and diversity control in `candidates/DIVERSITY_TRACKER.md`.

## Stage 4 — Prior-art / Novelty Audit

**Status: PASSED (2026-10-05; D011).**

- [x] Every serious Stage-3 candidate has a documented audit.
- [x] Searches cover both story/visible wording and mathematically equivalent formulations.
- [x] Appropriate source classes are searched, including the Gazette archive and relevant problem/recreational/general mathematical sources.
- [x] Search formulations, dates, sources, and findings are recorded.
- [x] Mathematical-equivalence checks explain what transformations or abstractions were considered.
- [x] “No result found” is never presented as proof of novelty.
- [x] Every candidate receives exactly one frozen novelty classification.
- [x] Candidates classified as rediscoveries or too close are not selected.
- [x] Materially related prior art is analysed, not merely linked.
- [x] A primary candidate and a small number of reserves are selected with written rationale grounded in Gazette fit, mathematics, and novelty evidence.

Gate evidence: ten schema-conforming records in `prior-art/audits/`; cross-candidate synthesis in `prior-art/STAGE4_SUMMARY.md`. Seven candidates are `REDISCOVERY`, CAND-008 is `TOO_CLOSE_TO_EXISTING_PROBLEM`, and CAND-005/CAND-010 are `CLEAR_WITH_RELATED_PRIOR_ART`. CAND-010 is primary and CAND-005 is reserve. No unqualified originality claim is made.

## Stage 5 — Formalisation and Submission Package

**Status: PASSED (2026-10-05; D012, D013).**

- [x] The canonical reader-facing problem statement is frozen.
- [x] A complete rigorous solution is written and independently/adversarially checked.
- [x] Edge cases, hidden assumptions, and interpretation ambiguities are resolved.
- [x] Computation supports rather than substitutes for the proof.
- [x] A materially useful alternative solution is included.
- [x] Reader testing was performed if practical: no independent human reader was available, so no external test is claimed; the limitation and internal adversarial wording review are documented.
- [x] A final prior-art audit was run against the exact finished formulation and mathematical kernel.
- [x] Relevant background information for the editor is prepared.
- [x] The submission package follows current Problem Corner instructions verified on 2026-10-05.
- [x] A concise submission email to the current Problem Corner editor is prepared.
- [x] All final authority/status documents identify the selected problem and reserve status consistently.

Gate evidence: Stage 5 began with CAND-010. Its theorem and equality case were independently verified, but the final novelty audit found older linear nearest-neighbour analysis using the same nearest-neighbour sum and regular-spacing extremum; D012 therefore retires CAND-010 as a Stage-5 rediscovery and promotes the frozen reserve CAND-005. CAND-005 was then formalised, adversarially checked, computationally tested over all permutations of lengths 2 through 8, given a useful second proof, and re-audited in exact final form. Its final classification remains `CLEAR_WITH_RELATED_PRIOR_ART`. The package and unsent email draft are in `final/`.

Passing Stage 5 means the package is ready for human review/submission; it does not authorise autonomous sending. No submission has been sent.
