# Stage 2 Research Workspace

Stage 2 learns the editorial reality of **The Mathematical Gazette — Problem Corner** before serious candidate invention.

## Corpus target

Review at least roughly **60 problems**, preferably **80–100**, spanning multiple years, issues, mathematical types, presentation styles, and where possible more than one editorial period.

Published solutions matter as much as statements. A title-only bibliography does not satisfy the gate.

## Record format

Create one structured record per reviewed problem using `problem-catalogue.schema.json`. JSON Lines (`.jsonl`) is recommended for the working catalogue because it is append-friendly, searchable, scriptable, and easy for later AI sessions to synthesise.

Use stable catalogue IDs such as `MG-PC-YYYY-ISSUE-LOCAL` when metadata permits. The exact ID convention may be refined once real archive patterns are inspected, but IDs must remain unique and stable.

## Research practice

For each record:

- preserve source URL/citation and access date;
- distinguish exact statement text from a faithful summary;
- record both surface presentation and underlying mathematical mechanism;
- capture solution style, not only the final answer;
- note multiple solutions and editorial comments where relevant;
- record unknown fields as `null` or `unknown`, not guesses.

Prefer faithful summaries when full quotation is unnecessary.

## Sampling discipline

Actively check for accidental skew by:

- year/issue;
- editor era;
- abstract versus contextual presentation;
- mathematical area/mechanism;
- apparent prerequisite level;
- problem/solution length.

Do not let a convenient searchable subset stand in for the section as a whole.

## Required Stage-2 synthesis

After the corpus is large enough, produce an evidence-based synthesis covering the Stage-2 gate questions, including contrasts with olympiad, textbook, and generic internet-puzzle styles. The synthesis must cite or reference catalogue evidence and explicitly state limitations.

## Prohibition

Do not run a serious candidate-invention programme during Stage 2.
