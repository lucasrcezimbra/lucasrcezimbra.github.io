---
title: Profilling Python tests
date: 2024-10-02
lastmod: 2024-10-02
---

## Using pytest-profiling + snakeviz

[pytest-profiling · PyPI](https://pypi.org/project/pytest-profiling)

1. `pip install pytest-profiling snakeviz`
1. `pytest --profile`
1. `snakeviz prof/combined.prof`
