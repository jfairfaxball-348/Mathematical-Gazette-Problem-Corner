# Stage 4 Prior-Art / Novelty Audits

This directory remains locked until Stage 3 freezes the serious candidate set.

## Core principle

There is a decisive difference between:

> “I could not immediately find it.”

and:

> “We conducted a documented, reasonably strong prior-art investigation.”

Only the second is useful evidence. Even then, novelty is not mathematically “proved” merely because searches returned nothing.

## Audit scope

Every serious Stage-3 candidate receives an audit using `prior-art-audit.schema.json`.

Search both:

1. the visible/story formulation; and
2. mathematically equivalent formulations after stripping away names, objects, and narrative.

Source classes should include, as relevant:

- the Mathematical Gazette archive;
- other problem journals and problem archives;
- olympiad/problem collections;
- books and recreational-mathematics sources;
- OEIS where sequence data is material;
- Mathematics Stack Exchange;
- MathOverflow where appropriate;
- general mathematical literature/search.

Not every source class will be relevant to every candidate, but omissions should be reasoned rather than accidental.

## Classification

Use exactly one final classification:

- `CLEAR`
- `CLEAR_WITH_RELATED_PRIOR_ART`
- `MATERIAL_PRIOR_ART_POSSIBLY_SALVAGEABLE`
- `REDISCOVERY`
- `TOO_CLOSE_TO_EXISTING_PROBLEM`
- `NOVELTY_UNCERTAIN`

A `CLEAR` classification means no material prior art was found after a documented, reasonably strong investigation; it is not a proof that no prior art exists.
