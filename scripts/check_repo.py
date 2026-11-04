#!/usr/bin/env python3
"""Repository hygiene checks: manifest shape, skill frontmatter, relative links.

Run in CI and locally before publishing. Exit 1 on any failure.
"""
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ALLOWED_MANIFEST_KEYS = {
    "$schema", "name", "version", "description", "author", "homepage",
    "repository", "license", "keywords", "extensions",
}
NAME_RE = re.compile(r"^(?!.*(?:--|\.\.))[a-z0-9](?:[a-z0-9.-]*[a-z0-9])?$")

fail = 0
passed = 0


def ok(label, condition):
    global fail, passed
    if condition:
        passed += 1
    else:
        fail += 1
        print("FAIL:", label)


def check_manifest():
    with open(os.path.join(ROOT, "plugin.json"), encoding="utf-8") as f:
        m = json.load(f)
    extra = set(m) - ALLOWED_MANIFEST_KEYS
    ok(f"plugin.json has only permitted top-level keys (found extra: {sorted(extra)})", not extra)
    ok("plugin.json declares the canonical $schema",
       m.get("$schema") == "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json")
    ok(f"plugin.json name '{m.get('name')}' matches the spec pattern",
       bool(NAME_RE.match(m.get("name", ""))) and len(m.get("name", "")) <= 64)
    ok("plugin.json declares a version", bool(m.get("version")))


def check_skills():
    skills_dir = os.path.join(ROOT, "skills")
    found = 0
    for name in sorted(os.listdir(skills_dir)):
        skill = os.path.join(skills_dir, name, "SKILL.md")
        if not os.path.isfile(skill):
            continue
        found += 1
        with open(skill, encoding="utf-8") as f:
            text = f.read()
        ok(f"{name}: has YAML frontmatter", text.startswith("---\n"))
        fm = text.split("---\n", 2)[1] if text.startswith("---\n") else ""
        m_name = re.search(r"^name:\s*(.+)$", fm, re.M)
        m_desc = re.search(r"^description:\s*(.+)$", fm, re.M)
        ok(f"{name}: frontmatter name present", bool(m_name))
        if m_name:
            val = m_name.group(1).strip().strip('"')
            ok(f"{name}: name is lowercase-hyphen and <=64 chars", bool(NAME_RE.match(val)) and len(val) <= 64)
            ok(f"{name}: directory name matches frontmatter name", val == name)
        ok(f"{name}: description <=1024 chars", bool(m_desc) and len(m_desc.group(1)) <= 1024)
    ok(f"at least one skill discovered (found {found})", found > 0)


def check_links():
    broken = 0
    scanned = 0
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in {".git", "node_modules"}]
        for fn in filenames:
            if not fn.endswith(".md"):
                continue
            scanned += 1
            path = os.path.join(dirpath, fn)
            with open(path, encoding="utf-8") as f:
                text = f.read()
            for m in re.finditer(r"\]\(([^)#]+?)(?:#[^)]*)?\)", text):
                target = m.group(1).strip()
                if target.startswith(("http://", "https://", "mailto:", "#")):
                    continue
                resolved = os.path.normpath(os.path.join(dirpath, target))
                if not os.path.exists(resolved):
                    broken += 1
                    print(f"  broken link: {os.path.relpath(path, ROOT)} -> {target}")
    ok(f"all relative Markdown links resolve ({scanned} files scanned)", broken == 0)


def check_yaml():
    path = os.path.join(ROOT, "skills", "equipment-inventory", "templates", "lab-inventory.example.yaml")
    try:
        import yaml
    except ImportError:
        print("  (pyyaml not installed; skipping the YAML parse)")
        return
    with open(path, encoding="utf-8") as f:
        data = yaml.safe_load(f)
    ok("inventory example parses as YAML", isinstance(data, dict))
    bad = []
    for cat, items in data.items():
        if not isinstance(items, dict):
            continue
        for key, val in items.items():
            if not isinstance(val, dict):
                bad.append(f"{cat}.{key}")
                continue
            c = val.get("count")
            if not (isinstance(c, (int, float)) or (isinstance(c, str) and c.startswith("stock"))):
                bad.append(f"{cat}.{key}={c!r}")
    ok(f"inventory counts are numbers or stock strings (bad: {bad})", not bad)


def main():
    check_manifest()
    check_skills()
    check_links()
    check_yaml()
    print(f"\n{passed} checks passed, {fail} failed")
    return 0 if fail == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
