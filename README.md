# IB DP Sciences Agent Skills

Curriculum-layer [Agent Skills](https://agentskills.io/) for the IB DP Group 4 sciences — **Biology, Chemistry, and Physics** — built from the official IB sciences guides (first assessment 2028), teacher support material, sciences experimentation guidelines, the official assessed samples, and a large corpus of real graded IAs used for marking calibration.

> **Status: in development** (v0.2.0). Skills are drafted and being tested live. Not yet published.

## What this is

[`ib-sciences-ia-coach`](skills/ib-sciences-ia-coach/SKILL.md) powers the whole scientific-investigation process for a DP sciences teacher. The four-criteria IA model (Research design / Data analysis / Conclusion / Evaluation, 24 marks) is shared across all Group 4 sciences; the coach applies subject-specific conventions (chemistry uncertainties and titration protocol, physics error propagation and linearization, biology's qualitative judgment) once the subject is named:

- **Design guidance** — help a student shape a unique, quantifiable research question and a feasible, criteria-ready methodology (scaffolding, never ghost-writing)
- **Review** — criterion-referenced constructive feedback on a student's plan or draft
- **Mark** — mark a final report against the official 2028 criteria with evidence-based justification, calibrated against 596 real graded IAs (220 Biology, 199 Chemistry, 177 Physics with full four-criteria scores)
- **Lesson practical design** — design practicals and activities for lessons from a topic and the equipment you have

You provide what you have or what you want to accomplish — **no database required**. Optional companion skill: [`equipment-inventory`](skills/equipment-inventory/SKILL.md) maintains a private YAML lab inventory the coach can read automatically.

## Install (Hermes)

Once published:

```bash
hermes skills tap add <owner>/ib-dp-sciences-ia-skills
```

Manual install for any Agent Skills host:

```bash
git clone https://github.com/<owner>/ib-dp-sciences-ia-skills.git ~/.agents/skills/ib-dp-sciences-ia-skills
```

## How it works

Ask your agent, for example:

- *"My student wants to investigate enzymes for their Biology IA. Help me guide their design — SL, 10 hours, we have colorimeters and water baths."* → Mode A
- *"Here is my chemistry student's draft — review it against the criteria."* → Mode B
- *"Mark this physics report and give me moderation comments."* → Mode C
- *"Design a 50-minute practical for 'gas exchange in plants' with what we have."* → Mode D

The skill encodes the criteria, marking methodology, data rules, safety/ethics, subject conventions, and examiner patterns from the official samples plus real-IAs calibration — all distilled into `references/` in the author's own words.

## What's deliberately NOT here

- **Generic scientific tooling** — install the K-Dense scientific-agent-skills collection separately for heavy statistics/cheminformatics/bioinformatics.
- **IB-copyrighted content** — criteria and guidance are paraphrased in the author's own words; the official IB publications remain the authority. The skill can consult the teacher's own copies (e.g. `IB_DOCS_DIR`) for exact descriptor wording.
- **School-specific data** — real inventories, school policies, and student work stay in private files outside this repo.
- **Anything a student could submit as their own IA** — the coach scaffolds and evaluates; it never writes student work.

## License & disclaimer

MIT. Teacher-authored; not affiliated with or endorsed by the International Baccalaureate Organization. Marking and feedback are starting points for qualified teacher judgment — verify against the official guide, school policy, and your own professional standards. All practicals require the teacher's own risk assessment and school approval.
