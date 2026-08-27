# Statistics Decision Tree — Which Test, When, Per Subject

Use this in Mode A (scaffolding the data plan), Mode B (reviewing whether the student used the right test), and Mode C (marking — verifying the statistical treatment is appropriate). The single most reliable mark-mover across all three sciences is a correctly chosen and executed significance test; the single most common cap is having no test at all.

**The n-rules are non-negotiable**: SD needs ≥5 replicates; t-test ≥10 per group; SEM ≥30. Below those thresholds, express variation as a range (max − min). A student who calculates SD on n=3 gets penalised, not rewarded.

## Quick decision tree

```
START: What is your research question asking?
│
├─ COMPARING two groups/conditions?
│   ├─ DV is continuous (e.g. height, rate, absorbance)?
│   │   ├─ n ≥ 10 per group → Independent-samples t-test (unpaired)
│   │   │   └─ OR Mann–Whitney U if n < 10 or data clearly non-normal
│   │   ├─ Same subjects measured twice → Paired t-test
│   │   │   └─ OR Wilcoxon signed-rank if n < 10
│   │   └─ n < 5 per group → No formal test; report means + range
│   │
│   └─ DV is categorical/count data (e.g. alive/dead, colour categories)?
│       └─ Chi-squared test (χ²)
│           ├─ Expected frequencies ≥ 5 in each cell
│           └─ If any expected < 5 → Fisher's exact test (2×2 only)
│
├─ COMPARING more than two groups?
│   ├─ DV is continuous, one factor?
│   │   └─ One-way ANOVA
│   │       └─ Follow with post-hoc (Tukey HSD) to find which groups differ
│   │       └─ If assumptions violated → Kruskal–Wallis (non-parametric)
│   └─ DV is categorical?
│       └─ Chi-squared test (larger contingency table)
│
├─ LOOKING FOR a relationship/correlation between two continuous variables?
│   ├─ Both variables continuous and approximately linear?
│   │   ├─ Pearson's r (product-moment correlation)
│   │   │   └─ Test against critical values at p = 0.05 (table or software)
│   │   │   └─ Report r, n, and p-value
│   │   └─ Data is ordinal OR relationship is non-linear?
│   │       └─ Spearman's rank correlation (ρ)
│   │           └─ Better for non-linear, ranked, or small-n data
│   └─ One variable categorical, one continuous?
│       └─ This is a comparison, not a correlation → use t-test or ANOVA above
│
├─ TESTING a model fit (e.g. linear regression)?
│   ├─ Report R² (coefficient of determination)
│   ├─ Report the equation of the line (y = mx + c)
│   ├─ For significance of the slope: t-test on the regression coefficient
│   └─ Physics-specific: max/min gradient method for uncertainty in slope
│
└─ JUST describing data (no comparison, no relationship)?
    ├─ Mean ± SD (n ≥ 5)
    ├─ Mean + range (n < 5)
    ├─ Median + IQR for skewed data
    └─ No significance test needed — but this is weak processing
```

## Subject-specific rules

### Biology — the statistics subject

Biology expects and rewards statistical testing. The TSM is explicit.

| Situation | Recommended test | Minimum n | Notes |
|---|---|---|---|
| Compare two conditions | Independent t-test | ≥ 10 per group | The most common biology IA test |
| Compare > 2 conditions | One-way ANOVA + Tukey | ≥ 5 per group (ideally ≥ 10) | Check: is the RQ about comparison? ANOVA on a correlation RQ is a classic error |
| Association (2 categorical) | Chi-squared | Expected ≥ 5 per cell | E.g. phenotype ratios, habitat preference |
| Correlation (2 continuous) | Pearson r (linear) or Spearman ρ (non-linear) | ≥ 10 (ideally ≥ 15) | Test r against critical values at p = 0.05 |
| Very small samples | Mann–Whitney U or Wilcoxon | ≥ 5 | Non-parametric alternatives |

**Biology-specific notes**:
- A significance test is the single most reliable band-mover. Reports with a justified, correctly executed test consistently out-mark otherwise-identical reports without one.
- No test at all caps the processing strand at 2–3 — even a small-n test (e.g. Pearson on n=5) earns credit for attempting significance properly.
- Always state: the test used, the test statistic, the degrees of freedom (where relevant), the p-value (or "p < 0.05" / "p > 0.05"), and whether the result is significant.
- Outliers: never remove systematically; use 1.5×IQR or a stated rule; present data with and without; justify any removal.
- R² for linear fits; do not fit regression lines just to maximise R².

### Chemistry — tolerates statistics, expects propagation

Chemistry does NOT demand significance tests the way biology does. The chemistry currency is percentage difference vs theoretical values, uncertainty propagation, and concordant titres.

| Situation | Recommended approach | Minimum n | Notes |
|---|---|---|---|
| Trend establishment | ≥ 5 data points with best-fit line + R² | 5+ IV levels | Three values CANNOT establish a trend (explicitly penalised) |
| Comparison to theoretical | Percentage difference = \|experimental − theoretical\| / theoretical × 100 | — | This is the chemistry equivalent of a significance test |
| Concordant titres | Repeat until within 0.10–0.20 cm³; use mean of concordant values | 3+ titres | The rough titre is separate |
| Uncertainty in derived quantities | Add percentage errors for ×/÷; add absolute errors for +/− | — | Propagation, not SD, is the chemistry norm |
| Correlation (database IA) | Pearson r + critical values | ≥ 10 | Accepted but not expected; use only if justified |

**Chemistry-specific notes**:
- SD is used for ≥ 5 replicates, but it is NOT a requirement — concordant values are a legitimate alternative.
- Statistical tests (ANOVA, t-test) are tolerated when well executed but never demanded. Biology habits do not transfer.
- A conclusion that contradicts accepted science caps hard — the student must notice and explain.
- Rate is not the reciprocal of time; rate ≠ rate constant; do not average logarithmic values.

### Physics — the propagation subject

Physics expects uncertainty propagation, NOT statistical testing (except for database-style IAs). The TSM is explicit: propagation is the expected route.

| Situation | Recommended approach | Minimum n | Notes |
|---|---|---|---|
| Repeated measurements | Half-range rule: uncertainty = larger of (half the range) and (reading uncertainty) | 3+ | NOT SD — physics uses half-range |
| Derived quantities | Propagate: ×/÷ → add fractional errors; +/− → add absolute errors; powers → multiply fractional error by power | — | Quadrature (√(a²+b²)) is rigorous; linear addition accepted at student level |
| Graphical uncertainty | Error bars from measurement uncertainty; max/min gradient lines | — | Quote gradient ± uncertainty |
| Model comparison | % difference from theoretical + check if within propagated uncertainty | — | This is the physics equivalent of significance |
| Database/correlation IA | Pearson r + critical values | ≥ 10 | Only for database-style investigations |
| Comparing two conditions | t-test (if justified) | ≥ 10 per group | Not the physics norm, but accepted |

**Physics-specific notes**:
- Significant figures: an uncertainty is expressed to ONE significant digit at the value's decimal place — two digits when it starts with 1 (e.g. ±0.12 s, not ±0.1 s; ±0.4 m, not ±0.36 m).
- Carry extra digits through processing; round only at the end.
- Linearization is the core skill: choose axes so the relationship is linear, interpret gradient/intercept in terms of physical quantities.
- A curved graph with no transformation is weak processing at HL.

## Reporting conventions (all subjects)

Every significance test report should include:
1. **Name of the test** (e.g. "Independent-samples t-test")
2. **Test statistic** (e.g. t = 3.42)
3. **Degrees of freedom** where relevant (e.g. df = 18)
4. **p-value** (e.g. p = 0.003, or "p < 0.05")
5. **Conclusion** (e.g. "There is a significant difference in enzyme activity between 20 °C and 40 °C (t = 3.42, df = 18, p = 0.003)")

For correlation:
1. **Name** (e.g. "Pearson's product-moment correlation")
2. **r value** (e.g. r = 0.87)
3. **n** (e.g. n = 15)
4. **p-value** or comparison to critical value (e.g. "r(13) = 0.87, p < 0.05")
5. **Conclusion** (e.g. "There is a significant positive correlation between light intensity and photosynthesis rate")

## Common statistical errors (mark-capping)

1. **SD on n < 5**: penalised, not rewarded. Use range instead.
2. **t-test on n < 10**: too small for reliable results. Use Mann–Whitney U or acknowledge the limitation.
3. **No p-value reported**: the test result is meaningless without it.
4. **Wrong test for the RQ**: ANOVA on a correlation RQ; chi-squared on continuous data; t-test on paired data treated as unpaired.
5. **Removing outliers silently**: always justify with a stated rule (1.5×IQR) and show data with/without.
6. **Confusing correlation with causation**: a significant r does not prove cause — state this.
7. **Multiple tests without correction**: if running many comparisons, acknowledge the increased risk of Type I error.

## Sources

- IB Biology TSM: "Unpacking the internal assessment" — n-rules, statistics menu, significance testing expectations
- IB Chemistry TSM: concordance, percentage error, propagation; statistics tolerated not demanded
- IB Physics TSM: half-range rule, propagation conventions, sig fig rules
- IB session subject reports (all sciences): recurring feedback on missing/wrong statistical treatment
- Harris, D.C. *Quantitative Chemical Analysis* — statistical methods for chemistry
- Fowler, J. et al. *Handbook of Biological Statistics* — accessible biology statistics guide
