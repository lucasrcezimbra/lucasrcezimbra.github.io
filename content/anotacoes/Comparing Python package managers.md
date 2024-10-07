---
title: Comparing Python package managers
date: 2024-10-02
lastmod: 2024-10-07
---

## pyproject.toml spec
- [PEP 517 – A build-system independent format for source trees](https://peps.python.org/pep-0517)
- [PEP 518 – Specifying Minimum Build System Requirements for Python Projects](https://peps.python.org/pep-0518)
- [PEP 621 – Storing project metadata in pyproject.toml](https://peps.python.org/pep-0621)
- [pyproject.toml specification](https://packaging.python.org/en/latest/specifications/pyproject-toml/#pyproject-toml-spec)

## Comparison
| Tool   | Lock file | Manage Python versions | Global cache | PEP compliant | Upload to PyPI |
| ------ | --------- | ---------------------- | ------------ | ------------- | -------------- |
| Hatch  |           |                        |              |               |                |
| pip    |           |                        |              |               |                |
| Pipenv |           |                        |              |               |                |
| PDM    |           |                        |              |               |                |
| Poetry |           |                        |              |               |                |
| uv     |           |                        |              |               |                |


## uv
[GitHub](https://github.com/astral-sh/uv) | [Docs](https://docs.astral.sh/uv/)

### Pros
- uv can install and manage Python version (like pyenv); Poetry can't
- uv manages dependencies and environments for single-file scripts
    * `uv add --script <my-script> <package> && uv run <my-script>`
    * That's cool, I never seen that in other [Python]({{< ref "Python" >}})
      tools
- Disk-space efficient; global cache for dependency deduplication
    * I don't know how other tools manage that. It would be interesting to
      compare with Poetry
- Drop-in replacement for `pip`
    * `alias pip='uv pip'`

### How to use
#### Installing
- `pipx install uv` to install uv

#### Managing Python versions
- `uv python install <version>` to install a [Python]({{< ref "Python" >}})
  version
- `uv run --python <version> -- <command>` to run a command with a specific
  [Python]({{< ref "Python" >}}) version

#### Tools
- `uvx` (alias for `uv tool run`) same as `pipx`

#### Runnig scripts
- `uv add --script <my-script> <package>` to install a package to one script.


## PDM
[GitHub](https://github.com/pdm-project/pdm) | [Docs](https://pdm-project.org/en/latest/)


## Poetry
[GitHub](https://github.com/python-poetry/poetry) | [Docs](https://python-poetry.org/docs/)

### Pros
- lock file

### Cons
- "does not follow the standard specifying how metadata should be represented
  in a pyproject.toml file (PEP 621), instead using a custom `[tool.poetry]`
  table. This is partly because Poetry came out before PEP 621."
