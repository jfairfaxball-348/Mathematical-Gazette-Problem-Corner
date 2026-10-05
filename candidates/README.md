# Stage 3 Candidate Workspace

**Stage 3 is active.**

Stage 2 was closed on 2026-10-05 by explicit human override (decision D009) at 23 solution-reviewed catalogue records. The ordinary Stage-2 gate did not pass, so the editorial evidence carried into this workspace is useful but incomplete and sampling-biased. Do not overstate it.

## Serious candidate records

Use `candidate.schema.json` for every serious candidate. A story alone is not a serious candidate: the record must contain a credible mathematical kernel, expected result, and plausible solution mechanism.

Current structured serious records are stored one JSON object per line in `serious-candidates.jsonl`. The exploration/rejection ledger and mathematical validation notes are in `STAGE3_DISCOVERY_NOTES.md`.

Do not pad the pool to reach a numerical target. “Up to roughly 50” is a diversity ceiling/ambition, not a quota.

## Discovery discipline

Generate broadly across surface families, mathematical mechanisms and question forms before converging. Do not choose a preferred mathematical field in advance.

The frozen design principle remains:

> **simple situation → natural question → unexpected answer → elegant mathematics**

Basic mathematical validation belongs in Stage 3. Formal prior-art / novelty auditing does not: similarity risks may be noted, but Stage-4 novelty claims must wait until the serious set is frozen.

## Diversity control

Maintain `DIVERSITY_TRACKER.md` as the pool grows.

Two candidates that differ only by renamed objects, superficial story, notation, or inessential constants count as one idea family until a genuinely different mathematical question or mechanism is shown.

Before promoting a new item to serious-candidate status, compare it against the existing pool on both **surface family** and **mechanism family**. Near-duplicates should be merged, marked as variants, or rejected rather than counted separately.

## Rubric

Use all ten dimensions in `docs/CANDIDATE_QUALITY_RUBRIC.md`. Stage-3 scoring must be accompanied by brief written reasoning; do not reduce selection to arithmetic.

A candidate with fatal mathematical weakness, no credible solution route, severe accessibility problems or obvious derivative risk should not survive merely because its total score is high.
