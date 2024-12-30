---
title: Comparing Python package managers
date: 2024-10-02
lastmod: 2024-12-30
---

{{< datatables >}}

## Comparison
| Tool   | Lock file | Manage Python versions | Global cache | PEP compliant | Packaging/PyPI distribution         |
| ------ | --------- | ---------------------- | ------------ | ------------- | ----------------------------------- |
| Hatch  | ❌        | ✅                     |              | ✅            | ✔️ only using Hatch build backend    |
| pip    | ❌        | ❌                     |              | ✅            |                                     |
| Pipenv | ✅        | ❌                     |              |               | ❌                                  |
| PDM    | ✅        | ✅                     | ✅           | ✅            | ✅                                  |
| Poetry | ✅        | ❌                     |              | ❌            | ✔️ only using Poetry build backend   |
| uv     | ✅        | ✅                     | ✅           | ✅            | ✅                                  |


### uv
[GitHub](https://github.com/astral-sh/uv) | [Docs](https://docs.astral.sh/uv/)

#### Pros
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

#### How to use
##### Installing
- `pipx install uv` to install uv

##### Managing Python versions
- `uv python install <version>` to install a [Python]({{< ref "Python" >}})
  version
- `uv run --python <version> -- <command>` to run a command with a specific
  [Python]({{< ref "Python" >}}) version

##### Tools
- `uvx` (alias for `uv tool run`) same as `pipx`

##### Runnig scripts
- `uv add --script <my-script> <package>` to install a package to one script.


### PDM
[GitHub](https://github.com/pdm-project/pdm) | [Docs](https://pdm-project.org/en/latest/)


### Poetry
[GitHub](https://github.com/python-poetry/poetry) | [Docs](https://python-poetry.org/docs/)

#### Pros
- lock file

#### Cons
- "does not follow the standard specifying how metadata should be represented
  in a pyproject.toml file (PEP 621), instead using a custom `[tool.poetry]`
  table. This is partly because Poetry came out before PEP 621."


## References
- [Codebeez | uv as a poetry/pyenv/pipx replacement](https://codebeez.nl/blogs/uv-as-a-poetrypyenvpipx-replacement)
- [Hatch | docs](https://hatch.pypa.io/1.12)
- [Loopwerk: Poetry versus uv](https://www.loopwerk.io/articles/2024/python-poetry-vs-uv)
- [Loopwerk: Revisiting uv](https://www.loopwerk.io/articles/2024/python-uv-revisited)
- [PEP 517 – A build-system independent format for source trees](https://peps.python.org/pep-0517)
- [PEP 518 – Specifying Minimum Build System Requirements for Python Projects](https://peps.python.org/pep-0518)
- [PEP 621 – Storing project metadata in pyproject.toml](https://peps.python.org/pep-0621)
- [PDM | README - Comparisons to other alternatives](https://github.com/pdm-project/pdm/blob/e29740f4022cb0bc29140a05f6f2cfb900b8b581/README.md#comparisons-to-other-alternatives)
- [pyproject.toml specification](https://packaging.python.org/en/latest/specifications/pyproject-toml/#pyproject-toml-spec)
- [uv | docs](https://docs.astral.sh/uv)
- [uv | Publishing packages](https://docs.astral.sh/uv/guides/publish)
- [uv | Unified Python packaging](https://astral.sh/blog/uv-unified-python-packaging)
