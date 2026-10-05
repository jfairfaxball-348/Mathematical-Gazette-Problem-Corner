# Stage 3 Candidate Workspace

**Stage 3 passed on 2026-10-05. The serious set is frozen for Stage 4.**

Stage 2 was closed by explicit human override (D009) at 23 solution-reviewed catalogue records. Its ordinary gate did not pass, so the editorial evidence used during discovery was useful but incomplete and sampling-biased.

## Frozen serious records

The complete Stage-3 set is stored one JSON object per line in `serious-candidates.jsonl`.

There are **10** frozen candidates, each with status `FROZEN_FOR_STAGE_4`.

The exploration, rejection, merge and validation ledger is in `STAGE3_DISCOVERY_NOTES.md`. The final diversity profile is in `DIVERSITY_TRACKER.md`.

Do not add cosmetic variants or casually append new candidates after freeze. If Stage 3 genuinely needs reopening, record the reason and reconcile the authority files.

## What Stage 3 established — and did not establish

Stage 3 established that every frozen candidate has:
- a clear reader-facing formulation;
- a mathematical kernel and expected answer;
- a credible solution mechanism;
- basic soundness checks;
- a ten-dimension rubric assessment with written reasons;
- explicit surface/mechanism diversity metadata;
- stated similarity and failure risks.

Stage 3 did **not** establish originality.

The originality scores in candidate records are provisional risk judgements only. Formal visible-form and mathematical-equivalence prior-art work belongs to Stage 4 and must use `prior-art/prior-art-audit.schema.json`.

The frozen design principle remains:

> **simple situation → natural question → unexpected answer → elegant mathematics**
