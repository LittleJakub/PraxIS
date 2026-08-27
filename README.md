# PraxIS — IB Sciences Practical & IA Suite

Curriculum-layer [Agent Skills](https://agentskills.io/) for the IB DP Group 4 sciences — **Biology, Chemistry, and Physics** — built from the official IB sciences guides, teacher support material, sciences experimentation guidelines, the official assessed samples, and a large corpus of real graded IAs used for calibration.

> **Status: in development** (v0.3.0). Skills are drafted and being tested live. Not yet published.

## What this is

[`ib-sciences-praxis-coach`](skills/ib-sciences-praxis-coach/SKILL.md) powers the whole practical-science workflow for a DP sciences teacher. The four-criteria IA model (Research design / Data analysis / Conclusion / Evaluation, 24 marks) is shared across the sciences; the coach applies subject-specific conventions (chemistry uncertainties and titration protocol, physics error propagation and linearization, biology's qualitative judgment) once the subject is named:

- **Design guidance** — co-shape a student's IA idea into a unique, quantifiable research question and a feasible, criteria-ready methodology (scaffolding, never ghost-writing)
- **Review** — criterion-referenced critique and comments on a student's plan or draft
- **Marking support** — support the teacher in marking a final report against the official criteria with evidence-based justification, calibrated against 800+ real graded IAs (596 with full four-criteria scores: 220 Biology, 199 Chemistry, 177 Physics)
- **Lesson practical design** — plan practicals and activities for lessons from a topic and the equipment the school actually has
- **Submission pack** — the completeness checks and files needed for IB submission (word count, appendices rule, cover-sheet fields, teacher's per-criterion comments, moderation-sample advice)

You provide what you have or what you want to accomplish — **no database required**, and nothing is invented: equipment, reagents, and quantities always come from you or are flagged "determine in trial run". Optional companion skill: [`equipment-inventory`](skills/equipment-inventory/SKILL.md) maintains a private YAML lab inventory the coach can read automatically.

## Install

### Hermes Agent

```bash
hermes skills tap add LittleJakub/PraxIS
```

Manual (same effect, no tap index): clone into the profile skills directory —

```bash
git clone https://github.com/LittleJakub/PraxIS.git "$LOCALAPPDATA/hermes/skills/ib-sciences-praxis"
```

(The repo is also a portable [Agent Plugins](https://agent-plugins.org/) package — `plugin.json` + `skills/` — so plugin-capable hosts can load the whole thing as one plugin.)

### OpenClaw (and other Agent Skills hosts)

The suite is a standard Agent Skills repo (`SKILL.md` with frontmatter per [agentskills.io](https://agentskills.io/)), so any host that supports the open standard can load it:

```bash
# OpenClaw / other standard hosts: clone into the skills directory
git clone https://github.com/LittleJakub/PraxIS.git <your-skills-dir>/ib-sciences-praxis

# Or via the common standards-based installer
npx skills add LittleJakub/PraxIS

# Or via GitHub CLI (v2.90+), with provenance
gh skill install LittleJakub/PraxIS --agent <host>
```

If your host is not listed, check its current docs for where skills live (Claude Code, Codex, Gemini CLI, Cursor, OpenClaw, and others all read the standard `SKILL.md` format).

### Optional companion: scientific-computing layer

PraxIS is the subject-domain layer; for heavy data analysis (statistics, plotting, literature retrieval) install the MIT-licensed [K-Dense scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) collection alongside it — see [`DEPENDENCIES.md`](DEPENDENCIES.md) for the dependency and sync policy.

## How it works

Ask your agent, for example:

- *"My student wants to investigate enzymes for their Biology IA. Help me guide their design — SL, 10 hours, we have colorimeters and water baths."* → Mode A
- *"Here is my chemistry student's draft — review it against the criteria."* → Mode B
- *"Help me with the marking of this physics report — moderation comments please."* → Mode C
- *"Design a 50-minute practical for 'gas exchange in plants' with what we have."* → Mode D
- *"What do I need to submit for the moderation sample this session?"* → Mode E

The skill encodes the criteria, assessment methodology, data rules, safety/ethics, subject conventions, and examiner patterns from the official samples plus real-IAs calibration — all distilled into `references/` in the author's own words.

## What's deliberately NOT here

- **Generic scientific tooling** — install the K-Dense scientific-agent-skills collection separately (see above).
- **IB-copyrighted content** — criteria and guidance are paraphrased in the author's own words; the official IB publications remain the authority. The skill can consult the teacher's own copies (e.g. `IB_DOCS_DIR`) for exact descriptor wording.
- **School-specific data** — real inventories, school policies, and student work stay in private files outside this repo.
- **Anything a student could submit as their own IA** — the coach scaffolds and evaluates; it never writes student work.

## License & disclaimer

MIT. Teacher-authored; not affiliated with or endorsed by the International Baccalaureate Organization. Marking and feedback are starting points for qualified teacher judgment — verify against the official guide, school policy, and your own professional standards. All practicals require the teacher's own risk assessment and school approval.
