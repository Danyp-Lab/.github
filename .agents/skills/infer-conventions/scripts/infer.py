#!/usr/bin/env python3
import os
import sys
import json
from pathlib import Path

def inspect():
    repo_root = Path(__file__).resolve().parents[4]
    files = [f for f in os.listdir(repo_root) if not f.startswith(".")]
    has_agents_md = (repo_root / "AGENTS.md").is_file()
    has_lessons = (repo_root / ".ai" / "lessons.md").is_file()
    has_license = any(f.lower().startswith("license") for f in files)
    has_readme = any(f.lower().startswith("readme") for f in files)

    report = {
        "repository": repo_root.name,
        "status": "HEALTHY",
        "has_agents_md": has_agents_md,
        "has_lessons_md": has_lessons,
        "has_license": has_license,
        "has_readme": has_readme,
        "total_root_files": len(files)
    }
    print(json.dumps(report, indent=2))

if __name__ == "__main__":
    inspect()
