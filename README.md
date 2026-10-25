# design-pack

> **EN TL;DR:** an open, Russian-language design skills pack for AI coding agents (Claude Code, Codex, Cursor, Gemini CLI, OpenCode…). Five composable skills: a design verb vocabulary, a ~60-check AI-slop detector, a catalog of 12 styles with tokens and HTML specimens, project design memory (DESIGN.md + taste ledger), and a screenshot→verdict→fix visual loop. Install: `npx skills add xronocode/design-pack`. MIT.

Русскоязычный набор скилов, который учит агента проектировать, а не расставлять карточки. Превращает «сделай красиво» в контролируемый процесс: направление → сборка → аудит на клише → шлифовка → визуальное подтверждение.

## Установка

```bash
npx skills add xronocode/design-pack
# интерактивно: выбрать скилы × агентов (claude-code, codex, cursor, …)

# точечно:
npx skills add xronocode/design-pack --skill design-vocabulary -a claude-code

# глобально для всех проектов:
npx skills add xronocode/design-pack -g
```

Для Claude Code репо можно добавить и как plugin-маркетплейс:

```
/plugin marketplace add xronocode/design-pack
```

## Состав

| Скил | Что делает |
|---|---|
| `design-vocabulary` | Словарь команд-глаголов (`polish`, `critique`, `direction`, `audit`, `tokens`, `restyle`) и порядок работы. Точка входа, маршрутизирует на остальные скилы. |
| `design-slop-detector` | ~60 проверок на шаблонный AI-дизайн: цвет, типографика, layout, копирайт, компоненты, изображения. Каждый хит — с направлением исправления. |
| `design-style-library` | 12 стилей с полными токенами (палитра, шрифтовые пары, сетка, радиусы, тени, моушен), сценариями применения и HTML-образцами. Подбор: 6 кандидатов → 3 → 1. |
| `design-memory` | Память вкуса проекта: `DESIGN.md` (токены, компоненты, голос) + appearance-ledger (журнал принятых решений). Чем дольше работаешь, тем точнее результат. |
| `design-loop` | Петля «скриншот → вердикт → фикс → повторный скрин». Дизайн не считается готовым, пока не подтверждён глазами агента. Работает с chrome-devtools-mcp или браузерными инструментами агента. |

## Быстрый старт

```
Возьми за основу этот лендинг и прогони audit — мне кажется, он выглядит как AI-слоуп
Сделай direction для B2B-дашборда аналитики — покажи 3 направления на выбор
Прогони polish по главному экрану, контраст и вертикальный ритм так себе
Собери лендинг в стиле editorial из библиотеки, потом restyle карточек под swiss
```

## Философия

1. **Стиль — это решение, а не украшение.** Направление выбирается до первой строчки CSS и фиксируется в токенах.
2. **Клише — измеримы.** «AI-выглядящий» дизайн — это конкретный список паттернов; каждый можно найти и заменить.
3. **Глаза обязательны.** Ни один дизайн-вердикт не выдаётся без свежего скриншота.
4. **Вкус накапливается.** Решения проекта живут в `DESIGN.md` и ledger, а не в памяти сессии.
5. **Правило причины.** У каждого элемента — тень, радиус, градиент, анимация — должна быть причина. «Красиво» не причина.

## Вдохновение

Пакет собран с оглядкой на лучшие открытые коллекции: [impeccable](https://github.com/pbakaus/impeccable), [taste-skill](https://github.com/Leonxlnx/taste-skill), [gstack](https://github.com/garrytan/gstack), [huashu-design](https://github.com/alchaincyf/huashu-design), [diagram-design](https://github.com/cathrynlavery/diagram-design). Контент написан с нуля.

## Лицензия

MIT — см. [LICENSE](LICENSE).
