# Biology IA Conventions — Data, Uncertainty, and Safety

Author's own-words digest of the conventions that examiners expect in IB DP Biology scientific investigations (use alongside `data-and-analysis-guide.md` for the shared rules, and `safety-and-ethics.md` for the core principles).

## Uncertainty handling (biology)

- **Biology is the judgment subject, not the propagation subject**: the TSM is explicit that full error propagation is not expected — appropriate treatment is qualitative judgment backed by instrument uncertainties. State the instrument resolution (±0.5 °C thermometer, ±0.01 g balance, ±0.1 cm³ measuring cylinder), and handle derived quantities sensibly (e.g. rates as ranges rather than propagated errors).
- **Express variation with the n-rules**: SD needs ≥5 independent repeats; t-test ≥10 per group; SEM ≥30 — below those numbers, express variation as a range (min–max), not as SD/SEM. A student who calculates SD on n=3 gets penalized, not rewarded.
- **Error bars**: use ±SD (or ±SEM when n ≥ 30) and **say which one it is** — unlabelled error bars get the benefit of the doubt, but identification is the cheap mark.
- **Percentage uncertainties are not required in biology** (unlike chemistry) — do not push students to over-engineer.
- **Significant figures and decimal places**: consistent decimal places across a table is the accepted biology standard; inconsistent sf/dp is a recurring precision criticism. Units in every column heading.

## Data processing conventions

- **Statistics menu by question type**: comparison of two conditions → t-test (n ≥ 10/group); more than two conditions or categories → ANOVA (with the RQ checked first — ANOVA on a correlation RQ is a classic error); association between two categorical variables → chi-squared; correlation → Pearson (linear) or Spearman (non-linear) with the coefficient tested against critical values at p = 0.05.
- **A significance test is the single most reliable band-mover**: reports with a justified, correctly executed test consistently out-mark otherwise-identical reports without one. No test at all caps the processing strand at 2–3 — even a small-n test (e.g. Pearson on n=5) earns credit for attempting significance properly.
- **Trends and fits**: best-fit line + R² for continuous data; do not fit regression lines just to maximize R² (that is explicitly the wrong approach).
- **Outliers**: never remove systematically; use 1.5×IQR or a stated rule; present data with and without; justify any removal in the analysis, not only in the evaluation.
- **Database and simulation IAs**: screenshots of the database/simulation in the body (not the appendix); explain the selection and sampling of data; use biological variables — broad socio-economic metrics (e.g. HDI) yield data that is hard to analyse well.

## Fieldwork and organism conventions

- Scientific names: italicized, correct format, genus species; a species misidentification caps Research design.
- Sampling: describe method (quadrats, transects, random vs systematic) and justify it; note that non-random sampling introduces bias.
- Metric units only; retrieval dates for online sources; species counts with abundance indices where relevant.

## Safety & ethics specifics (biology)

- **Microbiology**: non-pathogenic strains only, stated source, correct incubation temperature, no open cultures, disinfection protocol.
- **Human participants**: consent forms (the only permitted appendix), no invasive or harmful procedures, anonymity; body fluids (saliva, blood) require special approval and handling rules.
- **Animals**: 3Rs (replacement, reduction, refinement); no vertebrates beyond observational/behavioural studies without approval; invertebrates treated humanely.
- **Plants/fieldwork**: permissions for field sites; no protected species; minimal environmental impact.
- **Chemicals**: even "household" substances (bleach, hydrogen peroxide, plant extracts) get a risk assessment — hazards → exposure → controls → emergencies.

## Sources for lesson practicals (biology)

- Royal Society of Biology (practical resources), CLEAPSS/SSERC (school-lab safety + practicals), SAPS (plants), Nuffield Practical Biology, Vernier/PhET for sensor-based and simulation work. The vetted list lives in `lesson-practical-sources.md`.
