# Data Collection, Processing & Uncertainty Guide

Teacher-authored digest in our own words from the official TSM ("Unpacking the internal assessment" and "General advice"). Use for Mode A (data-plan scaffolding), Mode B (review comments), Mode C (marking Data analysis / Conclusion), and Mode D (student-level data-processing instructions).

**Subject application**: the n-rules and statistics here are the shared sciences frame (drawn from the Biology TSM; the Chemistry and Physics TSMs make the same demands). Subject-specific treatment: see `biology-conventions.md` (judgment-based uncertainty, statistics menu, fieldwork, microbiology/consent ethics), `chemistry-conventions.md` (titration uncertainties, percentage error, stoichiometry) and `physics-conventions.md` (error propagation, linearization, sig figs).

## How much data is enough (the n-rules)

- Repeats are selected **with a rationale**, commensurate with 10 hours of work and the nature of the system (catalase generates data fast; photosynthesis does not).
- **SD from ≥ 5 replicates**; **t-test needs ≥ 10 replicates**; **SEM from ≥ 30**. With fewer replicates, express variation as a **range** (max − min). Mann–Whitney U can handle very small samples; generally aim for ≥ 10 for any significance test.
- Sample-size language: n > 30 large; 15–30 small; 5–14 very small; t-tests with n < 10 are usually too small.
- If insufficient data were collected for reasons outside the student's control, mean + range (+ a significance test if feasible) may still reach the top band **if the processing is commensurate with the data and the research question**.
- Doing rough processing as the data come in is strongly recommended — it lets the student adjust range/interval and catch issues early.
- Trials are not repeats: a student who describes several trials need not log them again as separate repeats.

## Recording and presentation conventions

- SI or metric units only (mL/cm³, L/dm³ fine; °F, cups, inches are not). Units and uncertainties go **in the column headings** of data tables (unless data within a column justifiably differ).
- Consistent decimal places matched to the precision of the measurement. Significant-figure conventions are not expected, but must be correct if used.
- Raw and processed data may share one table. Large datasets: show a representative sample taken at regular intervals across the IV range (the teacher has reviewed the full data and records that).
- Tables and graphs are referenced in the text (Figure 1, Graph 1). Inadequate axis labels, legends, titles, proportions, and scaling all cap the Data analysis mark.
- A mean / SD / range at the foot of the column or row it summarises already counts as processing. For spreadsheets, a screenshot showing the formula is fine; unusual processing needs a worked example.
- Device-derived values (an instrument that directly outputs "rate") are raw data, not processed. Software-generated graphs are raw data; gradients or area-under-curve can extend the processing.
- Graphs: dot-to-dot is acceptable (never penalize it for continuous variables); a trend line adds value especially with uncertainty bars, r, or R². Graphing raw data when processed data would answer the question better is insufficient but not wrong. Choose the graph type to fit the data.
- Qualitative observations (labelled images, drawings, descriptions) accompany raw data where relevant.

## Uncertainties

- Sources: instrument graduations, manufacturer specifications, least-count readout — but judge **realistic use** (a stopwatch that displays 0.001 s does not measure events to 0.001 s given human reaction time). Justify the size of the uncertainty.
- Counts don't need ±1 stated, but derived values do (e.g. % germination of 25 seeds ≈ ±4%; heart rate by palpation over 15 s ≈ ±4 bpm).
- **Propagation of uncertainties is NOT systematically expected in biology** — qualitative judgment is the norm.
- Graphical uncertainty: scatter plots with trend lines, uncertainty (error) bars, R² values, box-and-whisker plots.
- Statistical tests are themselves measures of uncertainty: t-test, chi-squared, ANOVA report a p-value (ANOVA should come with a post-hoc test such as Tukey); for correlation coefficients, significance is an additional step. p < 0.05 is the conventional threshold for significance.
- r (correlation coefficient) ≠ R² (coefficient of determination): r measures correlation; R² gauges how closely a trend line matches the data.

## Outliers

- **Never systematically remove outliers** to make results "fit better" — that is data manipulation. Present outcomes with and without the outlier to reveal its impact.
- Statistical identification: points beyond 1.5 × IQR below Q1 or above Q3. Sample sizes in DP biology are small (n ≤ 30, often n < 15), so removal needs explicit justification.
- Justified removal: an observation can be explained, or a method weakness was identified and corrected.

## Statistical tests — selection rules of thumb

| Question | Test |
|---|---|
| Compare 2 groups' means (independent) | t-test (n ≥ 10 per group; Mann–Whitney U for very small/non-normal) |
| Compare ≥ 3 groups' means | ANOVA + post-hoc (Tukey) |
| Compare frequencies/categories (contingency) | chi-squared |
| Association between two continuous variables | correlation (r) — check significance separately |
| Fit of trend line | R² |
| Species diversity / population estimates | Simpson reciprocal index, Lincoln index (ecology) |

Any statistical test needs a null and alternative hypothesis stated in the report (not necessarily at the start of the experiment), and the software source named (e.g. Microsoft Excel); reasoning must be clear enough to verify. When Excel reports only a p-value, students cannot present t-statistic tables — that's expected.

## What caps marks in Data analysis (patterns from the samples)

- Uncertainties missing except "precision of the ruler" → the uncertainty strand sits at 1–2.
- Non-metric units, missing axis labels, units in table cells instead of column headings → communication strand capped.
- Processing limited to means/indices with no uncertainty treatment → strand 3 capped at 3.
- Inconsistent decimal places across raw and processed data → precision strand capped.
- Conversely: consistent conventions + uncertainties in headings + appropriate processing + justified test choice are what the 5–6 band looks for.

## Assessment mechanics (mined from the Chemistry & Physics TSMs — shared)

**Awarding marks:**
- Zero is rare: an incomplete report with nothing at all addressing a criterion gets zero; partial evidence gets zero only if incomprehensible or totally irrelevant. A single zero-scoring strand should not be over-penalized — award the mark the other strands justify.
- Effective communication is not a separate criterion — it is embedded in all four (methodology/context in Research design; clear-precise-accurate recording in Data analysis; justified answers in Conclusion; expressed evaluation in Evaluation).

**Report structure and style:**
- No cover page or table of contents (distractions); a clear, informative title reflecting the RQ, plus a first paragraph that orients the reader.
- Methods may be prose or recipe style; passive or personal voice both fine; spelling/grammar errors are ignored unless they create ambiguity or incomprehensibility (many students write in a non-preferred language).
- How the report is organised, its scientific focus and its brevity matter more than the language.

**Word count:** maximum 3,000 words; the limit excludes tables, sketches, graphs, headings and the reference list. Where a lot of data was collected, include only a sample (at regular intervals covering the IV range); the teacher has reviewed the full dataset and records that (the full dataset no longer needs an appendix). Markers will not read past the limit.

**Citations:** no citation needed for broadly accepted facts/theory (e.g. Newton's second law; rate increases with temperature) — but a specific fact or value needs one (e.g. a quoted activation energy, a friction coefficient). Style is the student's choice but must be consistent and traceable (URL + retrieval date for online sources).

**Appendices:** not read by examiners. The only permissible appendices are consent forms for human-participant data collection.
