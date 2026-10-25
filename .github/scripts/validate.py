#!/usr/bin/env python3
"""Валидация design-pack: frontmatter скилов, HTML-специмены, marketplace.json, относительные ссылки.
Запускается в CI (.github/workflows/ci.yml) и локально: python3 .github/scripts/validate.py"""
import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SKILLS = ROOT / "skills"
VOID = {"meta", "link", "br", "img", "input", "hr", "source", "col", "area", "base", "embed", "track", "wbr"}
errors: list[str] = []


def err(msg: str) -> None:
    errors.append(msg)


def check_frontmatter(skill_dir: Path) -> None:
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.is_file():
        err(f"{skill_md}: файла нет")
        return
    text = skill_md.read_text(encoding="utf-8")
    m = re.match(r"^---\r?\n(.*?)\r?\n---", text, re.S)
    if not m:
        err(f"{skill_md}: нет YAML-frontmatter между --- ---")
        return
    fm = m.group(1)
    name = re.search(r"^name:\s*(\S+)\s*$", fm, re.M)
    desc = re.search(r"^description:\s*(.+)$", fm, re.M | re.S)
    if not name:
        err(f"{skill_md}: нет обязательного поля name")
    else:
        n = name.group(1)
        if n != skill_dir.name:
            err(f"{skill_md}: name «{n}» != имени папки «{skill_dir.name}»")
        if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", n):
            err(f"{skill_md}: name «{n}» должен быть lowercase-дефисами")
    if not desc or len(desc.group(1).strip()) < 30:
        err(f"{skill_md}: description короче 30 символов (нужен для триггеринга агентов и skills.sh)")


def check_html(path: Path) -> None:
    stack: list[str] = []

    class P(HTMLParser):
        def handle_starttag(self, tag, attrs):
            if tag not in VOID:
                stack.append(tag)

        def handle_endtag(self, tag):
            if not stack:
                err(f"{path}: закрывающий </{tag}> без открывающего")
            elif stack[-1] != tag:
                err(f"{path}: ожидался </{stack[-1]}>, пришёл </{tag}>")
            else:
                stack.pop()

    p = P()
    p.feed(path.read_text(encoding="utf-8"))
    if stack:
        err(f"{path}: незакрытые теги {stack}")


def check_links(skill_dir: Path, text: str) -> None:
    for target in re.findall(r"\[[^\]]*\]\(([^)#\s]+?)(?:#[^)]*)?\)", text):
        if target.startswith(("http://", "https://", "mailto:")):
            continue
        if not (skill_dir / target).exists() and not (ROOT / target).exists():
            err(f"{skill_dir / 'SKILL.md'}: битая относительная ссылка → {target}")


def check_marketplace() -> None:
    mp = ROOT / ".claude-plugin" / "marketplace.json"
    try:
        data = json.loads(mp.read_text(encoding="utf-8"))
        for plugin in data.get("plugins", []):
            for skill_path in plugin.get("skills", []):
                if not (ROOT / skill_path / "SKILL.md").is_file():
                    err(f"marketplace.json: путь скила {skill_path} не существует")
    except (json.JSONDecodeError, KeyError) as e:
        err(f"marketplace.json: {e}")


def main() -> int:
    skill_dirs = sorted(d for d in SKILLS.iterdir() if d.is_dir())
    if not skill_dirs:
        err("skills/: не найдено ни одного скила")

    for d in skill_dirs:
        check_frontmatter(d)
        check_links(d, (d / "SKILL.md").read_text(encoding="utf-8") if (d / "SKILL.md").is_file() else "")
        for html in (d / "assets").rglob("*.html"):
            check_html(html)

    specimens = list((SKILLS / "design-style-library" / "assets" / "style-specimens").glob("*.html"))
    if len(specimens) < 3:
        err(f"style-specimens: образцов меньше трёх ({len(specimens)})")

    check_marketplace()

    if errors:
        print(f"✗ {len(errors)} проблем(а):")
        for e in errors:
            print(f"  - {e}")
        return 1
    print(f"✓ OK: {len(skill_dirs)} скилов, {len(specimens)} образца, frontmatter/HTML/ссылки/marketplace валидны")
    return 0


if __name__ == "__main__":
    sys.exit(main())
