# Dependencies & Upstream Sync

This repo is a **curriculum layer** for IB DP Sciences (Biology, Chemistry, Physics): lesson-practical design, IA design/review/marking, and submission-file production. It deliberately depends on a general scientific-computing layer so the coach can execute real data processing instead of describing it.

## Upstream: K-Dense Scientific Agent Skills

- **Repository**: [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills)
- **License**: MIT (their `LICENSE.md`)
- **What it provides**: 163 validated skills + 78+ scientific databases (statistics, plotting, data analysis, literature retrieval, Python-package guidance for scikit-learn/pandas/Scanpy/etc.), distributed as a portable Agent Plugins package (`plugin.json` + `skills/`) on the open Agent Skills standard.
- **Why we depend on it**: our coach is subject-domain expertise (IB criteria, conventions, calibration); K-Dense is the scientific-computing engine. When both are installed, the coach can run real analyses (t-tests, ANOVA, chi-squared, Spearman, linearization, propagation) and pull scientific context for database IAs instead of only advising on them.

## Installing both

```bash
# 1) This suite (curriculum layer)
hermes skills tap add LittleJakub/ib-sciences-praxis   # or: npx skills add LittleJakub/ib-sciences-praxis

# 2) The scientific-computing layer (upstream)
npx skills add K-Dense-AI/scientific-agent-skills
# or, with provenance + version pinning via GitHub CLI:
gh skill install K-Dense-AI/scientific-agent-skills --pin v2.64.0
```

The coach works without the upstream layer (it will say so and fall back to guidance); installing both unlocks execution.

## Sync policy (keeping our integration current)

Upstream is maintained continuously, so our integration is pinned and reviewed on a schedule:

| Item | Policy |
|---|---|
| **Pin** | Reference the upstream release tag / commit SHA used for our last review (below). Installers should pin the same SHA for reproducibility. |
| **Review trigger** | On every upstream release, or at least once per term (4×/year), re-run our verification: the skill names/paths we reference in `SKILL.md` (Mode A data-plan tooling, Mode D processing instructions) still exist; calibration-independent data conventions unchanged. |
| **Process** | 1. `gh skill install K-Dense-AI/scientific-agent-skills --pin <new-tag>` · 2. Update the table below · 3. Commit as "Sync upstream K-Dense vX.Y.Z" · 4. Spot-check one Mode A data plan and one Mode D practical pack end-to-end. |
| **Attribution** | MIT requires preserving the copyright notice when redistributing; we do not redistribute upstream code — we depend on it and cite it here and in the README. Any skill text adapted from upstream carries its own attribution header. |

## Last synced

| Date | Upstream ref | Notes |
|---|---|---|
| 2026-08-27 | v2.64.0 (initial dependency) | Initial integration: documented dependency + sync policy; no code from upstream is vendored. |
