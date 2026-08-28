# Chemistry IA Conventions — Data, Uncertainties, and Safety

Author's own-words digest of the conventions that examiners expect in IB DP Chemistry scientific investigations (use alongside `data-and-analysis-guide.md` for the shared rules).

## Uncertainty handling (chemistry)

- **Instrument uncertainties matter quantitatively**: burette ±0.05 cm³ per reading (two readings → ±0.10 cm³ for a titre), pipette ±0.06 cm³, volumetric flask ±0.1–0.2 cm³, balance ±0.001 g (analytical) or ±0.01 g, thermometer ±0.5 °C (or better with a probe), pH meter ±0.01–0.05.
- **Report with the right precision**: a titre of 24.35 cm³, never 24.3; the number of decimal places follows the instrument, not the calculator.
- **Percentage error is expected** for concentrations and derived quantities: % error = (uncertainty / value) × 100. When several quantities combine, add percentage errors for multiplication/division (conservative, student-level approach); the TSM expects propagation to be attempted, not perfect — but ignoring it entirely caps the uncertainties strand.
- **Titration protocol**: concordant titres within 0.10–0.20 cm³; repeat until concordant; use the mean of concordant titres; identify the rough titre as separate.
- **Calibration**: quote calibration of the balance (two-point), thermometer/probe against a standard, and any colorimeter/spectrophotometer blank. A calibration statement is cheap marks in Research design.

## Data processing conventions

- **Stoichiometric reasoning** must be shown: mol → mol conversions with balanced equations, molar ratios, and limiting-reagent checks where relevant.
- **Rates**: initial-rate methods (gradient of the tangent at t=0) need the method stated; concentration–time graphs for continuous monitoring.
- **Trends and models**: linearization (e.g. 1/[A], ln[A]) and R² for fits; Arrhenius plots for temperature dependence — with the slope interpreted, not just quoted.
- **Graphs**: scatter with best-fit line (not connect-the-dots); error bars where uncertainties are known; axes with units; gradient ± uncertainty (max/min slope method) for rate and calibration data.
- **Averages**: mean ± SD for ≥3 replicates; identify outliers via 1.5×IQR or a stated, justified rule — never silent removal.

## Typical investigation types

- Titration (acid–base, redox, back-titration), enthalpy change (calorimetry), rates (iodine clock, gas collection, mass loss), equilibrium (colourimetric or titration shift), electrochemistry (cell potentials, electrolysis), organic synthesis (yield %, purity via melting point/TLC), and database/correlation studies (e.g. periodic trends) — the last must still be analysed with statistics (correlation coefficient + significance), not just graphed.

## Safety specifics (chemistry)

- Hazard classes: flammables (ethanol, cyclohexane), corrosives (strong acids/bases, hydrogen peroxide), toxics (lead salts, heavy metals, benzene derivatives), oxidizers, compressed gases.
- Controls: eye protection always; fume cupboard for volatile toxics; small-scale quantities; never mouth-pipette; waste segregation (heavy-metal waste, organic waste); MSDS awareness for each reagent; water-reactive or incompatible pairings flagged (e.g. oxidizer + flammable).
- Ethics/environment: micro-scale where possible; disposal rules stated — the "state so explicitly if none" rule applies to every risk category.

## Sources for lesson practicals (chemistry)

- RSC Learn Chemistry (classic experiments library), CLEAPSS (UK school-lab safety + practicals — teacher login), Nuffield Practical Chemistry, SSERC (Scotland), Vernier/PHET simulations for database-style IAs.

## Official TSM conventions (mined from the Chemistry teacher support material)

**Uncertainty mechanics:**
- **Propagation scope**: addition/subtraction (absolute), multiplication/division (fractional/percentage), and **exponents at HL only** — a SL student propagating through a power is doing more than required, and HL students missing exponents are under-requirement.
- Express measurement and processed uncertainties in absolute, fractional and percentage forms to a sensible number of significant figures; quantities and uncertainties to sensible decimal places.
- Percentage error and percentage difference vs literature/theoretical values are the expected currency (see the sample-patterns file — %difference earned credit even where full propagation was skipped).

**The research question checklist (chemistry):** the examiner guidance expects the RQ to identify the independent variable and its range, identify the dependent variable (which may be a *derived* value, e.g. rate from measured data), describe the chemical system/reaction being studied, and include a methodology. In simulations, a derived value (such as a rate) may be the raw data. The answer must not be known to the student in advance; SL and HL may both explore beyond the syllabus.

**Data sufficiency:** no single standard — the design must justify the quantity of data and repeats; rough processing while collecting is recommended; awareness that limited data limit the conclusion is credited; data that are insufficient without good reason impact Data analysis.

**Database IAs:** the choice of data source must be explained and its reliability commented on; sampling/extraction/filtering explained.

**Report mechanics** (shared with physics — see `data-and-analysis-guide.md`): no cover page or table of contents; prose or recipe-style methods both fine; language errors ignored unless they create ambiguity; word count excludes tables, graphs, headings and references; only a sample of large datasets appears in the report — **the full dataset no longer needs an appendix**; the teacher has reviewed the full dataset and records that on the work; appendices are not read (consent forms only); citations needed for specific facts, not broad theory (e.g. a quoted activation energy needs a source; "rate increases with temperature" does not).
