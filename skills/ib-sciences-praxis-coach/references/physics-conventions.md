# Physics IA Conventions — Uncertainties, Error Propagation, and Safety

Author's own-words digest of the conventions that examiners expect in IB DP Physics scientific investigations (use alongside `data-and-analysis-guide.md` for the shared rules).

## Uncertainty handling (physics)

- **Physics is the propagation subject**: uncertainties must be tracked through every calculation. Absolute (Δx), relative (Δx/x), and percentage forms; multiplication/division → add fractional/percentage errors; addition/subtraction → add absolute errors; powers → multiply the fractional error by the power. Quadrature (√(a²+b²)) is the rigorous treatment; the TSM accepts linear addition at student level — but a claim like "uncertainty negligible" without justification caps the uncertainties strand.
- **Reading errors**: digital instruments → ± half the last digit (or the stated resolution); analogue scales → ± half the smallest division; stopwatch reaction time ±0.2–0.3 s (often dominates — students should justify the value); ruler parallax and end-error.
- **Repeated measurements**: mean ± SD for ≥5 repeats; the SD of repeated readings can be smaller than instrument resolution for well-behaved systems — say which you use and why.
- **Graphical uncertainties**: error bars from the measurement uncertainty; best-fit line with max/min slope lines to quote gradient ± uncertainty; intercept uncertainty similarly.

## Data processing conventions

- **Linearization is the core skill**: choose axes so the relationship is linear (e.g. T² vs L for a pendulum, 1/d for inverse-square), plot the transformed data, and interpret the gradient/intercept in terms of physical quantities (e.g. gradient = 4π²/g). A curved graph with no transformation is weak processing at HL.
- **Fit quality**: R² for linear fits; residuals discussed only if relevant; never force a line through the origin without justification.
- **Significant figures**: final answers to the precision of the least precise input; calculations carried with more digits, rounded at the end; units on every quantity.
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
