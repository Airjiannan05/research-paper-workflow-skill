#!/usr/bin/env python3
"""Strip metadata blocks from all rpw-*/SKILL.md frontmatter, keeping only name + description."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

for skill_dir in sorted(ROOT.glob("rpw-*/")):
    skill_file = skill_dir / "SKILL.md"
    if not skill_file.exists():
        continue
    content = skill_file.read_text(encoding="utf-8")
    # Remove metadata block: "metadata:" through the next non-indented line (before "---")
    new_content = re.sub(r'\nmetadata:.*?(?=\n---)', '', content, flags=re.DOTALL)
    # Also remove any trailing blank line left by the removal
    new_content = re.sub(r'\n\n---', '\n---', new_content)
    if new_content != content:
        skill_file.write_text(new_content, encoding="utf-8")
        print(f"  stripped: {skill_dir.name}/SKILL.md")
    else:
        print(f"  no change: {skill_dir.name}/SKILL.md")

print("Done.")
