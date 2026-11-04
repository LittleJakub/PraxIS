# Calibration corpus and method

Provenance, counts and limits behind every number in `references/calibration-*.md` and `data/*.csv`. Read this before quoting a calibration figure in feedback, marking or moderation.

## What the corpus is

849 real IB DP Sciences IA reports, in two provenances, plus 21 official assessed samples used qualitatively:

| Subject | Four-criteria reports (`corpus-a`) | Session-tagged reports | Session-tagged with A/B scores |
|---|---|---|---|
| Biology | 220 | 91 | 41 |
| Chemistry | 199 | 95 | 72 |
| Physics | 177 | 67 | 35 |
| **Total** | **596** | **253** | **148** |

- **`corpus-a`** — 596 reports scored on all four criteria, with per-criterion evaluator commentary (6,560 strength statements and 6,462 weakness statements). These are the reports behind the distributions, the criterion means and the merged A/B tables.
- **`session-tagged`** — 253 exemplars from current-syllabus sessions (M25, N25, M26) with human-verified grades. 148 of them carry A/B scores and are merged into the A/B tables; the remainder carry grade and examiner text only.
- **Official samples** — the 21 assessed samples (7 per subject) and the session subject reports inform the qualitative patterns in `sample-patterns-*.md` and `session-subject-reports.md`, not the counts.

## What is generated, and what is not

Generated, deterministic, and checked:

| Output | Script |
|---|---|
| `calibration-distributions.md` | `calibration_tables.py` |
| `calibration-subject-patterns.md` | `calibration_tables.py` |
| `calibration-cross-criterion.md` | `calibration_tables.py` |
| the merged A/B tables in `marking-calibration.md` | `calibration_tables.py` |
| `calibration-feedback-library.md` | `distill_feedback.py` |

Not generated from a committed script, and therefore not covered by the numeric checks: `calibration-band-transitions.md`, `calibration-commentary-intelligence.md` (band sizes are checked; the theme percentages are not), `calibration-investigation-types.md` and `calibration-topic-intelligence.md` (both use title-keyword rules that are not in the repository). Treat those four as descriptive, not audited.

## Data files

`data/` carries the same numbers in machine-readable form:

- `calibration-distributions.csv` — subject × criterion × mark counts (includes a `0` row where a mark exists);
- `calibration-summary.csv` — n, mean total, SD, criterion means, grade-7 and sub-11 shares, A/B subset size;
- `calibration-merged-ab.csv` — per-grade n and A/B means for the merged tables;
- `calibration-cross-criterion.csv` — Pearson r for the six criterion pairs per subject.

## Verification

The private corpus repository carries `scripts/calibration_tables.py` with a `--check` mode that recomputes 199 assertions and fails on any drift: every mark count and total bucket, every subject mean and SD, every merged A/B value, every correlation, every commentary band size, and the grade-label deviation sentence. It exits non-zero on the first mismatch and prints the published and computed values side by side.

Every number in this repository's calibration files reproduced exactly when last checked. If you edit a table by hand, the check fails — regenerate instead.

## Limits you should state when you use these numbers

- **`corpus-a` grades are not IB-moderated.** They are recorded component scores from a teacher-accessible corpus; the distributions describe that corpus, not the population of all candidates.
- **`session-tagged` grades are human-verified** but come from a teaching platform; they are not official IB statistics.
- **Grade labels deviate from the summed criteria** for about 9% of `corpus-a` reports (20 of 220 in Biology). The criterion marks are the reliable unit; treat reported grade labels as noisy.
- **Small cells exist.** Component grade 2 holds one report per subject in Chemistry and Physics. Per-grade means for those rows are single values, not averages.
- **Topic and investigation-type tables are title-based.** Titles under-describe methods, so treat those classifications as indicative.
- **Correlations are within-corpus** and describe how these reports were scored; they are not a claim about the criteria themselves.
- **The feedback library matches commentary lexically**, by keyword, not semantically. Frequencies are lower bounds.

## Privacy

The corpus is private and is never linked from this repository. Only aggregates are published: counts, means, correlations and paraphrased commentary templates. No report text, title, student identifier, school or candidate code appears in this repository. The raw files carry no names, e-mail addresses or school fields.

## Regenerating

From the private corpus checkout (sibling layout):

```bash
python scripts/calibration_tables.py --csv ../PraxIS/data
python scripts/calibration_tables.py --check ../PraxIS
python scripts/distill_feedback.py --out ../PraxIS/skills/ib-sciences-praxis-coach/references/calibration-feedback-library.md
```

`--check` is the gate: run it after any corpus change and before publishing updated tables.
