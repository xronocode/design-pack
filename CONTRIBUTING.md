# Контрибьютинг

Пакет живёт просто: скилы — это папки в `skills/`, каждая с `SKILL.md` и опциональными `assets/` и `references/`. Дистрибуция — `npx skills add xronocode/design-pack`, реестром служит сам репозиторий.

## Перед посылкой PR

```bash
python3 .github/scripts/validate.py   # тот же прогон, что в CI
```

Скрипт проверяет frontmatter всех скилов, парность тегов HTML-образцов, относительные ссылки и `marketplace.json`.

## Как добавить стиль

1. Открой [references/styles-catalog.md](skills/design-style-library/references/styles-catalog.md) — внизу шаблон описания стиля.
2. Заполни по шаблону: характер в одном предложении, палитра с ролями, шрифтовая пара со scale, шкалы, моушн, сценарии, список «нельзя».
3. Сделай образец `assets/style-specimens/<slug>.html` — самодостаточный HTML с токенами в `:root`. **Стиль без образца не принимается**: образец — это контракт, по которому агент понимает стиль.
4. Обнови таблицу в [skills/design-style-library/SKILL.md](skills/design-style-library/SKILL.md).

## Как добавить проверку в slop-детектор

Новая проверка = строка в таблицу своей категории в [skills/design-slop-detector/SKILL.md](skills/design-slop-detector/SKILL.md): паттерн → чем заменить. Сохрани нумерацию и правило «каждому хиту — замена». Паттерн должен быть узнаваемым без спора (как «AI-бежевый»), а не вопросом вкуса.

## Правила

- Frontmatter: `name` = имя папки, lowercase-дефисы; `description` ≥ 30 символов на английском (по нему агенты и skills.sh решают, когда грузить скил). Тело скила — на русском.
- Один PR — одно изменение (стиль, проверка или фикс).
- Коммиты: короткое `type: суть` (`style: +terminal-mono specimen`, `fix: dropcap selector`).
- Либоязненно: контент пишем с нуля; код из репо без лицензии (anthropics/skills, apple-design-skill и др.) не копируем — см. [README](README.md#вдохновение).
