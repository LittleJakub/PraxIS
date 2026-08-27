---
name: equipment-inventory
description: Maintain a YAML lab inventory file for the IB DP Sciences (Biology, Chemistry, Physics).
allowed-tools: Read Write Edit Bash
compatibility: Requires Python >=3.10. No external services.
license: MIT
metadata:
  version: "0.1.0"
  skill-author: Jakub Grzeszczuk (via Hermes Agent)
---

# Equipment Inventory

Optional helper for the `ib-sciences-praxis-coach` skill. Maintains the machine-readable list of laboratory equipment, sensors, chemicals, consumables, and software so the coach can design activities and IAs against what actually exists in the lab. The inventory is a **private** YAML file that lives outside the skills repository — it is never committed, never shared, and contains no student data.

**The coach does not require this file.** The teacher can simply describe what they have ("we have 8 colorimeters, 4 water baths, Vernier dataloggers…") and the coach works from that description. This file is for teachers who want a maintained, versioned inventory the coach can read automatically.

## When to Use

- Creating the inventory for the first time from a teacher's description of the lab
- Adding, updating, or removing items after purchases, losses, or donations
- Before running `ib-sciences-praxis-coach` when a maintained inventory exists
- Answering "what investigations are feasible with what we have?" queries

Don't use for: designing activities (use `ib-sciences-praxis-coach`), ordering consumables (teacher/administrator task), or recording student data.

## Prerequisites

- The inventory file lives at `~/lab-inventory.yaml` by default, or at the path given by the environment variable `IB_LAB_INVENTORY` if set. The skill never writes anywhere else.

## File Format

YAML with fixed top-level categories. Every item is a mapping with `count` (number, or `"stock"` for bulk chemicals) and optional `notes` (capacity, concentration, condition, supplier quirks).

```yaml
lab: School Biology Lab          # free text — the skill reads it back to the teacher
updated: 2026-08-27            # ISO date of last edit — checked on every load
apparatus:                     # instruments, glassware, hardware
  colorimeter: {count: 8, notes: "10 mm cuvettes included"}
  water_bath:  {count: 4, notes: "30–80 °C, ±0.5 °C"}
sensors:                       # data loggers and probes
  light_sensor: {count: 6, notes: "Vernier, for datalogger"}
chemicals:                     # stock reagents; give concentration where it matters
  hydrogen_peroxide: {count: "stock 2 L", notes: "3% v/v, refrigerated"}
consumables:                   # disposable items
  disposable_pipettes: {count: 200}
glassware:                     # keep separate from apparatus if it helps clarity
software:                      # what students actually use for data processing
  excel: {notes: "classroom standard"}
safety:                        # PPE and safety infrastructure
  goggles: {count: 30}
```

Rules:

- Item keys are `snake_case`, descriptive, and stable — renaming breaks nothing but churn the diff.
- `count` is always a number or `"stock"` — never free text like "a few".
- Every entry the teacher mentions goes in; nothing is invented. If a quantity is unknown, write `{count: "?"}` and mark it as a follow-up rather than guessing.
- The file ends with a `## items: N` comment the skill keeps updated, so a stale file is visible at a glance.

## Procedure

1. **Resolve the path.** Use `$IB_LAB_INVENTORY` if set, else `~/lab-inventory.yaml`. If the file exists, read it and skip to step 3.
2. **Elicit (first creation only).** Walk the teacher through the categories in order — apparatus, sensors, chemicals, consumables, glassware, software, safety — one at a time, in plain language ("What thermometers do you have, and roughly how many?"). Record every item with a count. Confirm the lab name and today's date. Do not move to the next category until the previous one's items are written down.
3. **Update.** Apply the requested change (`write_file` or `patch`), bump `updated` to today, refresh the trailing item count, and report the diff to the teacher in one line per changed item.
4. **Validate.** Confirm the file parses as YAML (`python -c "import yaml,sys; yaml.safe_load(open(sys.argv[1]))"`), all counts are numbers or `"stock"`, and no category is missing.

Completion criterion: the file parses, `updated` is today's date, and every item the teacher named appears with a count.

## Pitfalls

- **Inventing items.** Never add equipment the teacher didn't mention — a design built on a phantom centrifuge fails in the classroom. Mark unknowns as `?` and list them as follow-ups.
- **Quantities are load-bearing.** "8 colorimeters" enables class sizes of 24 (3 per group); "2" does not. Ask for counts, not just names.
- **Confusing the private inventory with the repo.** The inventory never goes in the skills repository — the repo ships only the template (`templates/lab-inventory.example.yaml`).
- **Stale dates.** A file whose `updated` is months old will mislead the designer; bump it on every edit.

## Verification

- `python -c "import yaml; d=yaml.safe_load(open('<path>')); assert set(d) >= {'lab','updated','apparatus','chemicals'}"` passes.
- Every category the teacher was asked about is present (empty categories can appear with `{}`).
- The teacher confirms the file matches their lab when shown a compact summary (one line per category: name + count).
