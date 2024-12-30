---
title: Migrating pyproject.toml from Poetry to uv
date: 2024-12-30
lastmod: 2024-12-30
---

## TL;DR
```shell
uvx pdm import pyproject.toml
uvx tomlq 'del(.tool.poetry)' -i -t pyproject.toml
uvx tomlq 'del(."build-system")' -i -t pyproject.toml
uvx tomlq 'del(.tool.pdm)' -i -t pyproject.toml
```

## Migration
I managed to migrate my project from Poetry to uv using [PDM import command](https://pdm-project.org/latest/reference/cli/#import).

0. You will need uv installed
1. Run PDM import
    ```shell
    uvx pdm import pyproject.toml
    ```
1. Remove all `[tool.poetry.*]` sections from your `pyproject.toml`
    ```shell
    uvx tomlq 'del(.tool.poetry)' -i -t pyproject.toml
    ```
1. Remove `build-system` section from your `pyproject.toml`
    ```shell
    uvx tomlq 'del(."build-system")' -i -t pyproject.toml
    ```
1. Remove `tool.pdm` sections from your `pyproject.toml`
    ```shell
    uvx tomlq 'del(.tool.pdm)' -i -t pyproject.toml
    ```

## Another tools
### poetry-to-uv
[PyPI](https://pypi.org/project/poetry-to-uv/) | [GitHub](https://github.com/PacificGilly/poetry_to_uv)

The code looks fine. I tried, but it failed with this error:

```shell
$ uvx poetry_to_uv pyproject.toml
...
  File "~/.cache/uv/archive-v0/6p7woB22YMNNr2cWH9v7v/lib/python3.13/site-packages/poetry_to_uv/poetry.py", line 57, in _process_poetry_export_command
    dependency, version = dependency_version.split("@")
    ^^^^^^^^^^^^^^^^^^^
ValueError: too many values to unpack (expected 2)
```

I guess it was because my `pyproject.toml` had some dependencies installed
using git, but I didn't investigated further.

### uv-migrator
[crates.io](https://crates.io/crates/uv-migrator) | [GitHub](https://github.com/stvnksslr/uv-migrator)

I didn't try this one.

### migrate-to-uv
[PyPI](https://pypi.org/project/migrate-to-uv/) | [GitHub](https://github.com/mkniewallner/migrate-to-uv)

I didn't try this one.


## References
- [Loopwerk: How to migrate your Poetry project to uv](https://www.loopwerk.io/articles/2024/migrate-poetry-to-uv)
- [python - How to migrate from Poetry to UV package manager? - Stack Overflow](https://stackoverflow.com/questions/79118841/how-to-migrate-from-poetry-to-uv-package-manager)
