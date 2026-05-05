#!/usr/bin/env python3

from __future__ import annotations

import os
import re
from pathlib import Path

# Match markdown links with a .md target. Ignore http(s) URLs.
# We intentionally keep anchors unchanged (e.g. #section) to avoid slug-rule drift.
LINK_RE = re.compile(r"\]\((?!https?://)([^)#]+\.md)(#[^)]+)?\)")

ROOT = Path(__file__).resolve().parents[2]
I18N_ROOT = ROOT / "i18n" / "zh-CN"


def rewrite_links_in_file(md_path: Path) -> bool:
    text = md_path.read_text(encoding="utf-8")

    def repl(m: re.Match[str]) -> str:
        target = m.group(1)
        anchor = m.group(2) or ""

        # Leave absolute paths (e.g. /foo/bar.md) unchanged.
        if target.startswith("/"):
            return m.group(0)

        abs_target = (md_path.parent / target).resolve()

        try:
            rel_to_repo = abs_target.relative_to(ROOT)
        except ValueError:
            return m.group(0)

        zh_target = I18N_ROOT / rel_to_repo
        if not zh_target.exists():
            return m.group(0)

        new_rel = os.path.relpath(zh_target, md_path.parent)
        return f"]({new_rel}{anchor})"

    new_text = LINK_RE.sub(repl, text)
    if new_text == text:
        return False

    md_path.write_text(new_text, encoding="utf-8")
    return True


def main() -> None:
    changed = 0
    for md in I18N_ROOT.rglob("*.md"):
        if rewrite_links_in_file(md):
            changed += 1
    print(f"rewrote links in {changed} files")


if __name__ == "__main__":
    main()
