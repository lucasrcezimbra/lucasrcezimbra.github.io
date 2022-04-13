---
title: "Python"
date: 2022-04-10T18:45:24-03:00
---


## Background tasks

- [Dramatiq](https://dramatiq.io/)
- [Celery](https://github.com/celery/celery)
- [python-rq](https://python-rq.org/)
- [huey](https://github.com/coleifer/huey)


## Dataclasses

- attrs vs pydantic: [Why I use attrs instead of pydantic](https://threeofwands.com/why-i-use-attrs-instead-of-pydantic/)


## Profiling

- [pyperf](https://github.com/psf/pyperf)

| Profiler | What | Granularity | How |
| --- | --- | --- | --- |
| [timeit](https://docs.python.org/3/library/timeit.html) | run time | snippet-level |  |
| [cProfile](https://docs.python.org/3/library/profile.html#module-cProfile) | run time | method-level | deterministic |
| statprof.py | run time | method-level | statictical |
| [line_profiler](https://github.com/pyutils/line_profiler) | run time | line-level | deterministic |
| [memory_profiler](https://github.com/pythonprofilers/memory_profiler) | memory | line-level | +- deterministic |
| [pympler](https://github.com/pympler/pympler) | memory | method-level | deterministic |

Fonte: https://www.youtube.com/watch?v=DUCMjsrYSrQ
