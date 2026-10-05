# Agent Instructions

This repository is a staged publication project, not an open-ended mathematics research programme.

## Mandatory entry sequence

At the beginning of every session, inspect the live committed repository. Then read, in order:

1. `authoritative/START_HERE.md`
2. `authoritative/STATE.json`
3. `PROJECT_CHARTER.md`
4. `ROADMAP.md`
5. `authoritative/STAGE_GATE_LEDGER.md`
6. `STATUS.md`
7. `docs/PUBLICATION_TARGET.md`

Read the stage-specific README/schema files before adding stage-specific work.

## Authority

Current explicit human instructions override repository documents. Otherwise, committed repository state is authoritative.

The following are frozen project-level constraints and may not be silently redefined by an agent:

- the publication target;
- the central design principle;
- the five-stage order;
- the requirement that Stage 2 precede serious candidate invention;
- the ten candidate-quality rubric dimensions;
- the Stage-2 minimum corpus target;
- the requirement to audit all serious Stage-3 candidates in Stage 4;
- the meaning of novelty classifications and the rule that failed searches do not prove novelty.

Any human-authorised change to these must be recorded in `authoritative/DECISION_LOG.md` and reflected consistently in the authority files.

## Stage discipline

Do only work allowed by the current stage. Do not anticipate later stages merely because it is convenient.

In particular:

- Stage 2: research the actual Problem Corner corpus; do not seriously invent candidates.
- Stage 3: invent and validate candidates, but do not declare novelty from casual searching.
- Stage 4: perform documented prior-art work on every serious candidate.
- Stage 5: formalise only candidates that passed the Stage-4 selection gate.

A useful incidental idea encountered before Stage 3 may be noted only as an unworked observation if losing it would be harmful; it must not be developed, scored, or promoted as a candidate.

## Evidence discipline

For time-sensitive publication facts, prefer current official sources. Record source URL, access/verification date, and whether the source is current official guidance or historical evidence.

For Stage 2, store structured catalogue records according to `research/problem-catalogue.schema.json`. Prefer faithful summaries over unnecessary long quotation.

For Stage 4, “no result found” means only that a particular search found no result. Never equate it with proved originality.

## Repository hygiene

Keep the system proportionate. Add documents only when they reduce ambiguity, preserve evidence, or support later synthesis. Avoid duplicated status statements: update the authority files together when a gate is crossed.

Do not put speculative candidate mathematics in `final/`.
