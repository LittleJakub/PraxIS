#!/usr/bin/env python3
"""Verify that the published Markdown tables match data/calibration-*.csv.

Runs without the private corpus, so CI can enforce it on every push:
the CSVs are the machine-readable copy of the same numbers, and any hand
edit to a Markdown table (or to a CSV) fails the build.

Exit codes: 0 = consistent, 1 = drift.
"""
import csv
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REF = os.path.join(ROOT, "skills", "ib-sciences-praxis-coach", "references")
DATA = os.path.join(ROOT, "data")

SUBJECTS = ["Biology", "Chemistry", "Physics"]
CRITERIA = ["Research Design", "Data Analysis", "Conclusion", "Evaluation"]
SHORT = {"Research Design": "A", "Data Analysis": "B", "Conclusion": "C", "Evaluation": "D"}

fail = 0
passed = 0


def ok(label, condition):
    global fail, passed
    if condition:
        passed += 1
    else:
        fail += 1
        print("FAIL:", label)


def near(label, got, want, tol=0.051):
    ok(f"{label} (md {got}, csv {want})", got is not None and abs(got - want) <= tol)


def read(name):
    with open(os.path.join(REF, name), encoding="utf-8") as f:
        return f.read()


def csv_rows(name):
    with open(os.path.join(DATA, name), encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def parse_distributions(md):
    out = {}
    subject = criterion = None
    for line in md.splitlines():
        m = re.match(r"^## (Biology|Chemistry|Physics)", line)
        if m:
            subject, criterion = m.group(1), None
            out.setdefault(subject, {})
            continue
        m = re.match(r"^### (Research Design|Data Analysis|Conclusion|Evaluation)", line)
        if m:
            criterion = m.group(1)
            out[subject].setdefault(criterion, {})
            continue
        m = re.match(r"^\|\s*(\d)\s*\|\s*(\d+)\s*\|", line)
        if m and subject and criterion:
            out[subject][criterion][int(m.group(1))] = int(m.group(2))
    return out


def main():
    dist_md = parse_distributions(read("calibration-distributions.md"))
    for row in csv_rows("calibration-distributions.csv"):
        s, k, m = row["subject"], row["criterion"], int(row["mark"])
        want = int(row["count"])
        got = dist_md.get(s, {}).get(k, {}).get(m)
        if want == 0 and m == 0:
            continue  # a zero row is only printed when a report scored zero
        ok(f"{s}/{k}/mark {m}: md {got}, csv {want}", got == want)

    pat_md = read("calibration-subject-patterns.md")
    for row in csv_rows("calibration-summary.csv"):
        s = row["subject"]
        block = pat_md.split(f"## {s}", 1)[1].split("## ", 1)[0]
        m = re.search(r"Mean total: \*\*([\d.]+)/24\*\* \(SD ([\d.]+)\)", block)
        ok(f"{s}: mean total line present", bool(m))
        if m:
            near(f"{s} mean total", float(m.group(1)), float(row["mean_total"]))
            near(f"{s} SD", float(m.group(2)), float(row["sd_total"]))
        ranked = {k: float(row[f"mean_{['RD','DA','C','E'][i]}"]) for i, k in enumerate(CRITERIA)}
        low = min(ranked, key=ranked.get)
        m = re.search(r"Lowest-scoring criterion: \*\*([^*]+)\*\* \(mean ([\d.]+)/6\)", block)
        ok(f"{s}: lowest criterion is {low}", bool(m) and m.group(1) == low)

    mark_md = read("marking-calibration.md")
    for row in csv_rows("calibration-merged-ab.csv"):
        s, g = row["subject"], int(row["grade"])
        n, a, b = int(row["n"]), float(row["mean_A"]), float(row["mean_B"])
        if s == "Biology":
            m = re.search(rf"^\|\s*\*\*{g}\*\*\s*\|\s*{n}\s*\|\s*([\d.]+)\s*\|\s*([\d.]+)\s*\|", mark_md, re.M)
            ok(f"Biology merged G{g} row (n={n})", bool(m))
            if m:
                near(f"Biology merged G{g} A", float(m.group(1)), a)
                near(f"Biology merged G{g} B", float(m.group(2)), b)
        else:
            seg = mark_md.split(f"**{s} (", 1)[1].split("Merged A/B", 1)[1]
            m = re.search(rf"G{g} A ([\d.]+) B ([\d.]+)", seg)
            ok(f"{s} merged G{g} present", bool(m))
            if m:
                near(f"{s} merged G{g} A", float(m.group(1)), a)
                near(f"{s} merged G{g} B", float(m.group(2)), b)

    cross_md = read("calibration-cross-criterion.md")
    for row in csv_rows("calibration-cross-criterion.csv"):
        s, pair, r = row["subject"], row["pair"], float(row["r"])
        ca, cb = pair.split("-")
        sec = cross_md.split(f"## {s} (n = ", 1)[1].split("## ", 1)[0]
        idx = {"RD": 0, "DA": 1, "C": 2, "E": 3}
        i, j = idx[ca], idx[cb]
        rows = {}
        for line in sec.splitlines():
            m = re.match(r"^\| \*\*([ABCD]) \(", line)
            if m:
                rows[m.group(1)] = [p.strip() for p in line.split("|")]
        parts = rows.get("ABCD"[i])
        ok(f"{s} cross-criterion {pair} row", parts is not None)
        cell = parts[2 + j] if parts and len(parts) > 2 + j else ""
        m = re.match(r"r=([\d.]+)", cell)
        ok(f"{s} cross-criterion {pair} value present", bool(m))
        if m:
            near(f"{s} cross-criterion {pair}", float(m.group(1)), r)

    print(f"\n{passed} checks passed, {fail} failed")
    return 0 if fail == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
