# Changelog

Формат: Keep a Changelog, версии — SemVer.

## [0.1.0] — 2026-10-25

Первый публичный релиз.

- `design-vocabulary` — словарь команд-глаголов (`direction`, `tokens`, `restyle`, `audit`, `polish`, `critique`), порядок работы и 10 правил вкуса.
- `design-slop-detector` — 60 проверок на шаблонный AI-дизайн: цвет, типографика, layout, копирайт, компоненты, изображения; режим аудита по diff.
- `design-style-library` — каталог 12 стилей с полными токенами, флоу выбора 6→3→1, три HTML-образца (swiss, editorial, neo-brutalist).
- `design-memory` — память вкуса проекта: шаблоны `DESIGN.md` и appearance-ledger.
- `design-loop` — визуальная петля скриншот→вердикт→фикс→повторный скрин.
- Установка: `npx skills add xronocode/design-pack`; Claude Code plugin marketplace через `.claude-plugin/marketplace.json`.
- CI: валидация frontmatter, HTML-образцов, ссылок и манифеста.
