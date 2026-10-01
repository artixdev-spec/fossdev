# Sales report

Учебная практика по документированию: предметная область, спецификация,
docstring-и в коде и сборка документации Sphinx (reStructuredText + Markdown).

## Структура

```
docs_domain/
├── docs/
│   ├── DOMAIN.md           # предметная область
│   ├── SPECIFICATION.md    # требования к модулю
│   ├── Makefile            # сборка Sphinx
│   └── source/             # исходники документации (conf.py, *.rst, *.md)
├── src/sales/              # код
├── tests/                  # тесты
├── .readthedocs.yaml       # конфигурация Read the Docs
└── Makefile                # install / test / docs / clean
```

## Команды

Окружение `.venv` создаётся в корне репозитория (`make venv` из корня).

```bash
make install   # зависимости, включая sphinx и myst-parser
make test      # тесты
make docs      # HTML-документация в docs/build/html
make clean     # удалить собранную документацию
```

## Read the Docs

Конфиг лежит не в корне репозитория, поэтому в настройках проекта на
readthedocs.org (Admin → Settings → Path for .readthedocs.yaml) нужно указать
`docs_domain/.readthedocs.yaml`. Пути внутри конфига — от корня репозитория.
