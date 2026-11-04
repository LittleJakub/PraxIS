# Changelog

All notable changes to this project are documented here. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and the project uses
[Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Fixed

- `plugin.json` no longer declares a `skills` array. Agent Plugins 1.0.0 has a closed
  manifest schema and discovers skills from the fixed `skills/` location, so the field
  was non-conformant and ignored by clients.
- Chemistry conventions no longer permit a standard deviation at n = 3; the shared
  n-rule (SD from ≥5 replicates, range below that) now applies, as it already did in
  `data-and-analysis-guide.md` and `statistics-decision-tree.md`.
- Chemistry uncertainty terminology corrected: the `(uncertainty / value) × 100` formula
  is percentage *uncertainty*, not percentage *error*; percentage error and percentage
  difference are now defined separately, matching `session-subject-reports.md`.
- Digital-instrument uncertainty corrected to ±1 in the last digit (least count) in both
  `physics-conventions.md` and `equipment-uncertainties.md`; the previous "± half the last
  digit" rule contradicted its own worked example.
- Dot-to-dot guidance reconciled: joining points is acceptable for showing raw data, but a
  trend claim requires a best-fit line. `data-and-analysis-guide.md` previously said
  dot-to-dot was acceptable while `anti-patterns.md` capped it at 3–4.
- The missing-trial anti-pattern now points at strand 3 (methodology description), matching
  `calibration-feedback-library.md` and the teacher-check notes in `ia-criteria.md`.
- `lab-inventory.example.yaml` now complies with its own rule that `count` is a number or a
  `stock` string; `"made fresh"` and `"on demand"` moved into `notes`.
- Grade-boundary arithmetic in `grade-boundaries.md` corrected: 18/24 plus 60–65% on the
  papers reaches an overall grade 6, not a grade 7 (which needs roughly 75–80%).
- README no longer advertises an `IB_DOCS_DIR` variable that no skill implements.
- The assessed-sample count in `marking-calibration.md` now matches `anti-patterns.md` and
  the two sample-pattern files (7 + 7 chemistry/physics commentaries, not 6 + 5).

### Added

- This changelog.

## [0.3.0] — 2026-08-28

Initial public version: `ib-sciences-praxis-coach` (five modes, four-criteria IA model,
subject conventions, calibration tables, assessment samples) and the optional
`equipment-inventory` skill.
