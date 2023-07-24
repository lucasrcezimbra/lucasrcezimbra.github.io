---
title: "Python"
date: 2022-04-10T18:45:24-03:00
---


Parcialmente movido para https://publish.obsidian.md/cezimbra/Public/Python

## f-string

### debugging
```python
user = "eric_idle"
f"{user=}"
# "user='eric_idle'"
f"{user = }"
# "user = 'eric_idle'"
```

### padding

```python
val = "test"
f"{val:>10}"
# '      test'
f"{val:<10}"
# 'test      '
f"{val:_<10}"
# 'test______'
f"{val:^10}"
# '   test   '
```

Fonte: https://fstring.help/


## pandas

- axios: 0=linha e 1=coluna
- pandas-profilling - [PyPI](https://pypi.org/project/pandas-profiling/), [docs](https://pandas-profiling.ydata.ai/docs/master/index.html)

### Geral

```python
df.shape  # (linhas, colunas)
df.info()
df.High.mean()  # média da coluna High
df.Date = pd.to_datetime(df.Date)  # convert column to datetime
```


### Informações Estatísticas

```python
df.describe()  # informações estatísticas
df.ride_duration.std()  # desvio padrão da coluna ride_duration
```


### Visualização

```python
df.High.plot()  # gráfico da coluna High
df.Volume.hist()  # histograma da coluna Volume
df.plot.scatter('c1', 'c2')  # gráfico de dispersão
df.Low.plot(kind='box')  # gráfico boxplot
```

### Valores ausentes

```python
df.isnull().sum()  # conta o número de linhas com NaN
df.isnull().sum() / df.shape[0] # % de valores ausentes
df.dropna(subset=['user_gender'], axios=0)  # apaga as linhas com valor NaNs da coluna user_gender
```

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


## String Parsing
- [parse](https://github.com/r1chardj0n3s/parse) - Parse strings using a specification based on the Python format() syntax.
- [ttp](https://github.com/dmulyalin/ttp) - Template Text Parser
