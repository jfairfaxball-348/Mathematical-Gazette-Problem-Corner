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
