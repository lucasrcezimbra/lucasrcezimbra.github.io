---
title: Profilling Python tests
date: 2024-10-02
lastmod: 2024-10-31
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
pytest --profile
# open prof/* SVG files with or prof with SnakeViz
```
### SnakeViz
[snakeviz · PyPI](https://pypi.org/project/snakeviz)
```shell
pip install snakeviz
snakeviz prof/combined.prof
```

### SVG
1. Open `prof/combined.svg`
