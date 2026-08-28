# Physics IA Conventions — Uncertainties, Error Propagation, and Safety

Author's own-words digest of the conventions that examiners expect in IB DP Physics scientific investigations (use alongside `data-and-analysis-guide.md` for the shared rules).

## Uncertainty handling (physics)

- **Physics is the propagation subject**: uncertainties must be tracked through every calculation. Absolute (Δx), relative (Δx/x), and percentage forms; multiplication/division → add fractional/percentage errors; addition/subtraction → add absolute errors; powers → multiply the fractional error by the power. Quadrature (√(a²+b²)) is the rigorous treatment; the TSM accepts linear addition at student level — but a claim like "uncertainty negligible" without justification caps the uncertainties strand.
- **Reading errors**: digital instruments → ± half the last digit (or the stated resolution); analogue scales → ± half the smallest division; stopwatch reaction time ±0.2–0.3 s (often dominates — students should justify the value); ruler parallax and end-error.
- **Repeated measurements**: physics follows the half-range rule, not SD — the mean uncertainty is the larger of (one-half the range) and (the individual reading uncertainty); if repeats show no variation at all, use the least count. Statistical analysis (SD, t-tests) is NOT the expected route in physics — propagation is (see the TSM conventions below).
- **Graphical uncertainties**: error bars from the measurement uncertainty; best-fit line with max/min slope lines to quote gradient ± uncertainty; intercept uncertainty similarly.

## Data processing conventions

- **Linearization is the core skill**: choose axes so the relationship is linear (e.g. T² vs L for a pendulum, 1/d for inverse-square), plot the transformed data, and interpret the gradient/intercept in terms of physical quantities (e.g. gradient = 4π²/g). A curved graph with no transformation is weak processing at HL.
- **Fit quality**: R² for linear fits; residuals discussed only if relevant; never force a line through the origin without justification.
- **Significant figures**: an uncertainty is expressed to one significant digit at the value's decimal place — two digits when it starts with 1 (e.g. ±0.12 s, not ±0.1 s; ±0.4 m, not ±0.36 m). Carry extra digits through processing and round only at the end; units on every quantity.
- **Model comparison**: where a theoretical value exists (e.g. g = 9.81 m s⁻²), compare measured vs theoretical with percentage difference AND discuss whether the difference is within propagated uncertainty — this is what the Conclusion's context comparison rewards.
- **Statistics**: correlation/significance tests for database-style IAs (Pearson r with critical values); t-tests for comparing two conditions with ≥10 per group.

## Typical investigation types

- Mechanics (pendulum, projectile, inclined plane, collisions), electricity (Ohm's law, resistivity, capacitor discharge), waves (speed of sound, diffraction, standing waves), thermal (specific heat capacity, cooling curves), optics (refraction, lenses, Malus's law), and database/simulation studies (orbital mechanics, stellar properties) — simulation studies must still show investigator choice and real processing.

## Safety specifics (physics)

- Electricity: low-voltage DC preferred; mains equipment PAT-tested; capacitors discharged before handling; never work with wet hands near mains.
- Lasers: class 2 max for student use, never point at eyes, diffuse reflections only; high-intensity light sources flagged.
- Ionizing radiation: sealed sources only, handled with tongs, exposure minimized, storage rules; radioactive work requires school authorization.
- Mechanical: projectiles (range, momentum) — safety screens, eye protection, cleared zones; heavy masses and hanging weights secured; springs under tension.
- Thermal: hot plates and boiling water — tongs, heat-proof mats, no sealed containers heated (explosion risk).
- Ethics: human subjects (reaction time, hearing, vision) need consent and no harmful exposure; animal work follows the same 3Rs frame as biology.

## Sources for lesson practicals (physics)

- Nuffield Physics (legacy practicals still excellent), Institute of Physics (practical physics resources), PhET and Physics Classroom simulations for database-style IAs, CLEAPSS/SSERC for UK school-lab safety, Vernier/Logger Pro for sensor-based work.

## Official TSM conventions (mined from the Physics teacher support material)

**Uncertainty mechanics:**
- **Propagation is the expected route** — absolute/fractional/percentage forms through addition, subtraction, multiplication, division and powers; SD and statistical tests are not the expected treatment.
- **Mean uncertainty**: the larger of (one-half the range) and (the individual reading uncertainty); least count when repeats show no variation.
- **Rounding discipline**: keep extra decimal places during processing (premature rounding distorts the propagated uncertainty), round at the end; a value and its uncertainty share the same decimal place.
- **Uncertainty bars**: symmetric bars are acceptable for the IA even where the function would give asymmetric extremes (log/exponential cases not examined to that detail); additional decimal places may be retained for plotting to avoid compounding rounding errors.
- **Processed-data tables**: heading with quantity name, symbol, unit and uncertainty (e.g. distance d, cm, Δd = ±0.2 cm); raw and processed data may share a table; explanations in the text.

**Data sufficiency:**
- No single standard for "enough data" — it depends on the investigation and the 10 hours; repeat counts need a stated rationale.
- Doing rough processing as the data come in is strongly recommended — it reveals issues early and justifies adjusting the range/interval.
- Insufficient data when the causes were outside the student's control: mean + range can still reach top marks when commensurate with the question, and the student's awareness that limited data limit the conclusion is credited. No good reason for more data → Data analysis is impacted.
- The report should describe problems met during the trial runs and how they were handled (adaptability is credited).

**Database and simulation IAs:**
- Source identified, reliability established, sufficiency and relevance argued; screenshots with web addresses or program names mandatory; paywalled databases acceptable.
- Published tables are rarely suitable (the authors already made the student's decisions); repetitions returning identical values earn minimal credit — use additional simulations/databases instead.
- With secondary data, more independent variables are feasible; explain sampling control, extraction and filtering.
- Computational-analysis IAs should use tools that calculate properties accurately, not just visualize.
- The IA must stay focused on physics — it is not an interdisciplinary study.

**Report mechanics** (shared with chemistry — see `data-and-analysis-guide.md`): no cover page or table of contents; title + first paragraph orient the reader; prose or recipe-style methods both fine; language errors ignored unless they create ambiguity; word count excludes tables, graphs, headings and references; only a sample of large datasets appears in the report; appendices are not read (consent forms only); citations needed for specific facts, not broad theory.
