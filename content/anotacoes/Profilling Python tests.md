---
title: Profilling pytest tests and fixtures
date: 2024-10-02
lastmod: 2024-11-04
---

## pytest --durations
`--durations=<n>` outputs the top <n> slowest tests/fixtures

```shell
pytest --durations=<n>
```


## pyinstrument
[pyinstrument · PyPI](https://pypi.org/project/pyinstrument)

```shell
pip install pyinstrument
pyinstrument -m pytest
```


## pytest-profiling
[pytest-profiling · PyPI](https://pypi.org/project/pytest-profiling)

```shell
pip install pytest-profiling
```
### + SnakeViz
[snakeviz · PyPI](https://pypi.org/project/snakeviz)
```shell
pytest --profile
pip install snakeviz
snakeviz prof/combined.prof
```

### + SVG
```shell
pytest --profile-svg
# open prof/combined.svg
```


## Workaround to time fixtures teardown
1. Edit file `<venv>/lib/python<version>/site-packages/_pytest/fixtures.py`
2. Search for `def _teardown_yield_fixture`
3. Replace `next(it)` with
    ```python
    from time import time
    t = time()
    next(it)
    print(f"#################################### fixture {fixturefunc} teardown took {d} seconds")
    ```
