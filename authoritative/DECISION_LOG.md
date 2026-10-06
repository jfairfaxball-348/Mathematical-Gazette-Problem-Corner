# Decision Log

Record only project-level decisions that affect objectives, stage order, evidence standards, schemas, or selection criteria. Do not log routine edits.

## D001 — Single publication target

**Date:** 2026-10-05  
**Decision:** The sole target is *The Mathematical Gazette — Problem Corner*.  
**Reason:** The project should optimise for one real editorial context rather than generic puzzle quality.

## D002 — Central design principle

**Date:** 2026-10-05  
**Decision:** Freeze **simple situation → natural question → unexpected answer → elegant mathematics** as the central design principle.  
**Consequence:** Surface accessibility and mathematical elegance are both required; neither alone is sufficient.

## D003 — Five-stage order is mandatory

**Date:** 2026-10-05  
**Decision:** Freeze the five-stage order in `ROADMAP.md`. Stage 2 must precede serious candidate invention.  
**Reason:** Candidate design should be informed by the actual Problem Corner corpus rather than preconceptions.

## D004 — No mathematical field chosen in advance

**Date:** 2026-10-05  
**Decision:** Stage 1 does not privilege number theory, probability, combinatorics, geometry, or any other field.  
**Reason:** Mathematical mechanism should follow editorial evidence and candidate quality.

## D005 — Candidate-quality rubric frozen at ten dimensions

**Date:** 2026-10-05  
**Decision:** Later candidates must be assessed on the ten dimensions in `docs/CANDIDATE_QUALITY_RUBRIC.md`.  
**Note:** Stage 2 may calibrate interpretation and thresholds from corpus evidence, but may not silently delete or replace dimensions.

## D006 — Novelty is an evidence claim, not a search impression

**Date:** 2026-10-05  
**Decision:** A failed search never proves novelty. Stage 4 must document visible-form and mathematical-equivalence searches for every serious candidate and use the frozen classification vocabulary.

## D007 — Proportionate governance

**Date:** 2026-10-05  
**Decision:** Use a small authority core and explicit gates, but avoid research-programme bureaucracy that does not help this publication project.

## D008 — Stage 1 closed

**Date:** 2026-10-05  
**Decision:** Stage 1 passed its gate. Stage 2 is ready but not started.  
**Evidence:** Charter, roadmap, publication-target note, rubric, three stage schemas, authority files, and gate ledger are all committed. No substantive candidate discovery was performed.

## D009 — Stage 2 closed early by explicit human instruction

**Date:** 2026-10-05  
**Decision:** Close Stage 2 at the existing 23 structured, solution-reviewed catalogue records and move the project to Stage 3.  
**Authority:** Explicit human instruction that the progress made is sufficient and the project should move on rather than continue being blocked by historical full-text access.  
**Consequence:** This is a stage-gate exception, not an evidentiary finding. The ordinary Stage-2 gate did not pass: the roughly-60 corpus target, balanced older sampling, final synthesis, genre comparison and evidence-based Stage-3 design specification remain incomplete. Their limitations must remain visible. Stage 3 is unlocked; Stages 4–5 remain locked.  
**Unchanged constraints:** The publication target, central design principle, five-stage order, ten candidate-quality dimensions, novelty standards and later-stage gates remain unchanged.

## D010 — Stage 3 passed and serious candidate set frozen

**Date:** 2026-10-05  
**Decision:** Pass the Stage-3 discovery gate and freeze a ten-candidate serious set for exhaustive Stage-4 audit.  
**Evidence:** 31 candidate seeds were substantially explored; 10 were promoted and mathematically checked, 17 rejected, and 4 merged as variants. Every frozen record contains the candidate-schema fields, a credible expected answer and solution mechanism, basic validation, diversity metadata, similarity risks, and a written ten-dimension rubric assessment.  
**Frozen set:** CAND-001 through CAND-010 in `candidates/serious-candidates.jsonl`.  
**Consequence:** Stage 4 is unlocked but was not begun in the Stage-3 session. Stage 4 must audit all ten candidates before any primary candidate is selected. Stage 5 remains locked.  
**Novelty caution:** Stage-3 originality scores are risk estimates only; no candidate has yet received a Stage-4 novelty classification.

## D011 — Stage 4 passed; CAND-010 selected primary, CAND-005 reserve

**Date:** 2026-10-05  
**Decision:** Pass the Stage-4 prior-art / novelty gate after documented audits of all ten frozen Stage-3 candidates. Select **CAND-010 — How far is everyone’s nearest neighbour?** as the primary Stage-5 candidate and **CAND-005 — Which scenic villages survive?** as the sole reserve.  
**Evidence:** Complete schema-conforming records are in `prior-art/audits/` and the cross-candidate comparison is in `prior-art/STAGE4_SUMMARY.md`. Final classifications are: CAND-001, 002, 003, 004, 006, 007 and 009 `REDISCOVERY`; CAND-008 `TOO_CLOSE_TO_EXISTING_PROBLEM`; CAND-005 and CAND-010 `CLEAR_WITH_RELATED_PRIOR_ART`.  
**Selection rationale:** CAND-010 combines a very accessible statement, a non-obvious sharp extremum and a substantive elementary gap/total-variation solution. Its objective has established remote-pseudoforest / sum-min prior art, but the audit did not locate the exact fixed-span one-dimensional theorem. CAND-005 survives as reserve because the specific arbitrary-order deletion/confluence formulation was not found, although its local-extrema normal form has closer established prior art.  
**Consequence:** Stage 5 is unlocked but was not begun in the Stage-4 session. Rediscoveries and the too-close rounding candidate are excluded from selection. Stage-4 clearance is evidence, not proof, of originality; Stage 5 must run the required final prior-art audit on the exact finished formulation.  
**Unchanged constraints:** Publication target, central design principle, five-stage order, ten candidate-quality dimensions and novelty standards remain unchanged.

## D012 — Stage-5 novelty audit retires CAND-010 and promotes CAND-005

**Date:** 2026-10-05  
**Decision:** Retire **CAND-010 — How far is everyone’s nearest neighbour?** as a Stage-5 `REDISCOVERY` and promote the sole frozen reserve, **CAND-005 — Which scenic villages survive?**, to primary.  
**Mathematical finding:** CAND-010's theorem is correct. A fresh proof gives \(S\le L+\min d_i\le nL/(n-1)\), with equality only for equal gaps, so the mathematical failure mode did not occur.  
**Novelty finding:** The final audit located the older linear nearest-neighbour-analysis literature of Pinder & Witherick (1973, 1975), later discussed by Stark & Young (1981). A 1989 application explicitly writes the statistic as a constant multiple of \(L^{-1}\sum_i M_i\) and states that its value \(2\) represents perfectly regular spacing. This is algebraically the same extremal value \(\sum_iM_i=nL/(n-1)\).  
**Consequence:** The Stage-4 audit remains preserved as the record of evidence available at that gate, but its selection is superseded. CAND-010 is not defended by cosmetic rewording. CAND-005 becomes the Stage-5 candidate in accordance with the frozen reserve discipline.  
**Evidence:** `final/CAND-010_STAGE5_FAILURE.md`.

## D013 — Stage 5 passed with CAND-005 submission package

**Date:** 2026-10-05  
**Decision:** Pass the Stage-5 gate with **CAND-005 — Which villages survive?** as the selected submission candidate and no reserve.  
**Evidence:** The final package in `final/` freezes an unambiguous statement, proves confluence and identifies the survivors, records edge cases and assumptions, includes a useful monotone-run alternative proof, preserves exhaustive supporting checks for all permutation order types through \(n=8\), and records the lack of an independent human reader test. The exact final prior-art audit retains the qualified classification `CLEAR_WITH_RELATED_PRIOR_ART`: local-extrema / longest-alternating-subsequence material is established, but the exact arbitrary-current-neighbour deletion/confluence formulation was not located. Current official Problem Corner proposal instructions were rechecked and an email was drafted.  
**Consequence:** The package is ready for human review and possible submission. No submission has been sent, and no unqualified originality claim is authorised.

## D014 — Final wording revised and submission recorded

**Date:** 2026-10-06  
**Decision:** Replace the frozen reader-facing “cross out a village” formulation of CAND-005 with the human-approved qualitative war-and-razing formulation, and record that the proposal has now been submitted.  
**Wording change:** The submitted problem says that a village may be invaded and razed by the surviving villages immediately before and after it along the road when its altitude lies strictly between theirs; after it is razed, its attackers become neighbours. The public statement now says “more than two villages” rather than using symbolic notation.  
**Solution presentation:** The editor-facing solution uses plain-text UP/DOWN language rather than plus/minus symbols, to preserve readability when copied into email.  
**Mathematical effect:** None. The current-neighbour strict-betweenness rule and the theorem are unchanged: the terminal survivors are the two endpoints and the original local peaks and valleys, independently of attack order.  
**Novelty effect:** A targeted check of the revised visible wording located no new materially equivalent source. The mathematical kernel was already audited. The classification therefore remains `CLEAR_WITH_RELATED_PRIOR_ART`; no unqualified originality claim is made.  
**Submission:** The user confirmed that the proposal was submitted by the human author on 2026-10-06 to Chris Starr, Problem Corner editor. This repository records the human action; no autonomous sending is claimed.  
**Consequence:** The final package now records the submitted wording and status. The next action is to await and record the editor's response.

