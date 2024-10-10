---
title: Profilling Python tests
date: 2024-10-02
lastmod: 2024-10-10
---

## Using pyinstrument
[pyinstrument · PyPI](https://pypi.org/project/pyinstrument)

1. `pip add pyinstrument`
2. `pyinstrument -m pytest`


## Using pytest-profiling + snakeviz
[pytest-profiling · PyPI](https://pypi.org/project/pytest-profiling)

[snakeviz · PyPI](https://pypi.org/project/snakeviz)

1. `pip install pytest-profiling snakeviz`
1. `pytest --profile`
1. `snakeviz prof/combined.prof`


## Using pytest-profiling only
[pytest-profiling · PyPI](https://pypi.org/project/pytest-profiling)

1. `pip install pytest-profiling`
1. `pytest --profile-svg`
1. Open `prof/combined.svg`
