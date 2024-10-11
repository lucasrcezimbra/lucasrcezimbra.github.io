---
title: Python
date: 2023-08-15
lastmod: 2024-10-11
aliases:
  - /anotacoes/manifest-python-data-classes/
---

## Printing a tree
[Tweet](https://twitter.com/lucasrcezimbra/status/1711423408909803716)
```python
def print_tree(tree, indent=2, level=0):
    for name, child in tree.items():
        print(' '*indent*level + name)
        print_tree(child, indent, level+1)
```

## Extracting args names from a function
```python
import inspect
inspect.getfullargspec(<func>).args
```

```python
In [1]: import inspect

In [2]: def f(x,y):
    ...:     pass
    ...:

In [3]: inspect.getfullargspec(f).args
Out[3]: ['x', 'y']
```

## Why avoid initing Decimal from float
[Tweet](https://twitter.com/lucasrcezimbra/status/1696892876116914633)
```python
In [1]: from decimal import Decimal

In [2]: Decimal(0.1)
Out[2]: Decimal('0.1000000000000000055511151231257827021181583404541015625')

In [3]: Decimal('0.1')
Out[3]: Decimal('0.1')
```

## Why avoid using mutable objects as default args
[Tweet](https://twitter.com/lucasrcezimbra/status/1697723506727715020)
```python
In [1]: def f(k, v, d={}):
   ...:    d[k] = v
   ...:    return d

In [2]: f("x", 1)
Out[2]: {'x': 1}

In [3]: f("y", 2)
Out[3]: {'x': 1, 'y': 2}
```

## Merging PDFs
[Tweet](https://twitter.com/lucasrcezimbra/status/1712582240943968477)
```python
from pypdf import PdfWriter
w = PdfWriter()
w.append("first.pdf")
w.append("second.pdf")
w.write("merged.pdf")
w.close()
```

## Updating list in-place
[Tweet](https://twitter.com/lucasrcezimbra/status/1726580798025797887)
```python
l2 = l1 = [1, 2]
l2[:] = ['a', 'b']
print(l1 is l2, l1, l2)
# True ['a', 'b'] ['a', 'b']
```

## Moving from pip to Poetry
[Tweet](https://twitter.com/lucasrcezimbra/status/1696637161993326741)
```bash
poetry init
cat requirements.txt | cut -d '=' -f 1 | xargs poetry add
cat requirements-dev.txt | cut -d '=' -f 1 | xargs poetry add --group=dev
rm requirements.txt requirements-dev.txt
poetry install
poetry run <command>
```

## Installing requirements from git + ssh
```shell
pip install git+ssh://git@github.com/<org>/<repo>
```

## Spliting CLI args as string
[Tweet](https://twitter.com/lucasrcezimbra/status/1790034271727493258)
```python
>>> "--system 'string w/ multiple words'".split()
['--system', "'string", 'w/', 'multiple', "words'"]

>>> import shlex
>>> shlex.split("--system 'string w/ multiple words'")
['--system', 'string w/ multiple words']
```

## Sending arguments into a generator
```python
In [1]: def generator():
    ...:     while True:
    ...:         received = yield 'DATA'
    ...:         print('Received:', received)
    ...:

In [2]: g = generator()

In [3]: next(g)
Out[3]: 'DATA'

In [4]: g.send(1)
Received: 1
Out[4]: 'DATA'

In [5]: g.send(2)
Received: 2
Out[5]: 'DATA'
```

## Printing logs when running pytest
[Tweet](https://twitter.com/lucasrcezimbra/status/1705183510837747905)
```shell
pytest --log-cli-level DEBUG
```

## Why to fixtures instead of namespace variables for mocked data
[Tweet](https://twitter.com/lucasrcezimbra/status/1704810879169024089)
```python
# without fixture

MOCK_DATA = [{"field": "value"}]


def test_one():
    MOCK_DATA[0]['field'] = 'other value'
    assert MOCK_DATA[0]['field'] == 'other value'


def test_two():
    assert MOCK_DATA[0]['field'] == 'value'


# with fixture

@pytest.fixture
def mock_data():
    return [{"field": "value"}]


def test_three(mock_data):
    mock_data[0]['field'] = 'other value'
    assert MOCK_DATA[0]['field'] == 'other value'


def test_four(mock_data):
    assert mock_data[0]['field'] == 'value'
```

```python
    def test_two():
>       assert MOCK_DATA[0]['field'] == 'value'
E       AssertionError: assert 'other value' == 'value'
E         - value
E         + other value

path/to/tests/test_zero.py:15: AssertionError
=====================<mark> 1 failed, 3 passed in 0.18s </mark>=====================
```

## Why to use spec when using mocks?
[Tweet](https://twitter.com/lucasrcezimbra/status/1713876531754201433)
```python
from unittest.mock import Mock

class MyClass:
    pass

# without spec
Mock().wrong_method()
# Out: <Mock name='mock.wrong_method()' id='140607049530000'>

# with spec
Mock(spec=MyClass).wrong_method()
# raises "AttributeError: Mock object has no attribute 'wrong_method'"
```

## Why to use autospec when using mocks?
[Tweet](https://twitter.com/lucasrcezimbra/status/1714230538305692145)
```python
from unittest.mock import create_autospec, Mock

class MyClass:
    myobj = object

# without autospec
Mock(spec=MyClass).myobj.wrong_method()
# Out: <Mock name='mock.myobj.wrong_method()' id='140671042320272'>

# with autospec
create_autospec(MyClass).myobj.wrong_method()
# raises "AttributeError: Mock object has no attribute 'wrong_method'"
```

## Anti-Patterns
- [The Little Book of Python Anti-Patterns](https://docs.quantifiedcode.com/python-anti-patterns/)

## Auth
- [Authlib](https://authlib.org/) - The ultimate library in building OAuth and OpenID Connect servers

## Data
### pandas
- https://www.pola.rs/ - Lightning-fast DataFrame library for Rust and Python
- axios: 0=linha e 1=coluna
- pandas-profilling - [PyPI](https://pypi.org/project/pandas-profiling/), [docs](https://pandas-profiling.ydata.ai/docs/master/index.html)
- Geral
	```python
	df.shape  # (linhas, colunas)
	df.info()
	df.High.mean()  # média da coluna High
	df.Date = pd.to_datetime(df.Date)  # convert column to datetime
	```
- Informações Estatísticas
	```python
	df.describe()  # informações estatísticas
	df.ride_duration.std()  # desvio padrão da coluna ride_duration
	```
- Visualização
	```python
	df.High.plot()  # gráfico da coluna High
	df.Volume.hist()  # histograma da coluna Volume
	df.plot.scatter('c1', 'c2')  # gráfico de dispersão
	df.Low.plot(kind='box')  # gráfico boxplot
	```
- Valores ausentes
	```python
	df.isnull().sum()  # conta o número de linhas com NaN
	df.isnull().sum() / df.shape[0] # % de valores ausentes
	df.dropna(subset=['user_gender'], axios=0)  # apaga as linhas com valor NaNs da coluna user_gender
	```

## Dataclasses
- attrs vs pydantic: [Why I use attrs instead of pydantic](https://threeofwands.com/why-i-use-attrs-instead-of-pydantic/)

## Strings
### Formatting
#### `%` operator ([Tweet](https://twitter.com/lucasrcezimbra/status/1704086552274424259))
- `%s`: String conversion.
- `%d` or `%i`: Integer conversion.
- `%f`: Float conversion.
- `%o`: Octal conversion.
- `%x` or `%X`: Hexadecimal conversion.
- `%e` or `%E`: Exponential notation conversion.
```python
In [1]: "%s %d %f %o %x %e" % ("a", 1, 1.0, 8, 16, 100)
Out[1]: 'a 1 1.000000 10 10 1.000000e+02'
```
### f-string
Fonte: https://fstring.help/
- debugging ([Tweet](https://twitter.com/lucasrcezimbra/status/1704465326321070555))
	```python
	user = "eric_idle"
	f"{user=}"
	# "user='eric_idle'"
	f"{user = }"
	# "user = 'eric_idle'"
	```
- padding ([Tweet](https://twitter.com/lucasrcezimbra/status/1714968107674939755))
	```python
	value = "test"
	f"{value:>10}"
	# '      test'
	f"{value:<10}"
	# 'test      '
	f"{value:_<10}"
	# 'test______'
	f"{value:^10}"
	# '   test   '
	```
- date
  ```python
  >>> from datetime import datetime
  >>> d = datetime.now()
  >>> f'{d:%Y-%m-%d}'
  '2024-09-27'
  ```

## Troubleshooting
- `[extras.pipfile_deprecated_finder.2] 'pip-shims<=0.3.4' does not match '^[a-zA-Z-_.0-9]+$` #troubleshooting
	  - `pre-commit autoupdate`
- How to enable relative line numbers in PyCharm?
	- https://intellij-support.jetbrains.com/hc/en-us/community/posts/360008429240-How-To-Enable-Relative-Line-Numbers-With-IdeaVim
	- `:set relativenumber`



## Toolbox
- Background Tasks: Moved to My Toolbox - [Python - Background Tasks](https://toolbox.cezimbra.me/lists/python-background-tasks/)
- CLI: Moved to My Toolbox - [Python - CLI](https://toolbox.cezimbra.me/lists/python-cli/)
- JSON: Moved to My Toolbox - [Python - JSON](https://toolbox.cezimbra.me/lists/python-json/)
- ORM: Moved to My Toolbox - [Python - ORMs](https://toolbox.cezimbra.me/lists/python-orms/)
- RPC: Moved to My Toolbox - [Python - RPC](https://toolbox.cezimbra.me/lists/python-rpc/)
- Text Parsing: Moved to My Toolbox - [Python - Text Parsing](https://toolbox.cezimbra.me/lists/python-text-parsing)
- GraphQL Server:  Moved to My Toolbox - [Django - GraphQL](https://toolbox.cezimbra.me/lists/django-graphql/)
- WebAssembly: Moved to My Toolbox - [Python - WebAssembly](https://toolbox.cezimbra.me/lists/python-webassembly/)
- https://github.com/haralyzer/haralyzer/ - Lib to read HAR files #tools

### Cache
- https://github.com/grantjenks/python-diskcache
- https://github.com/uqfoundation/klepto - persistent caching to memory, disk, or database

### Keycloak
- [https://www.baeldung.com/postman-keycloak-endpoints](https://www.baeldung.com/postman-keycloak-endpoints)
- [https://github.com/marcospereirampj/python-keycloak/](https://github.com/marcospereirampj/python-keycloak/)
    - unnecessarily complex
    - some strange evals: [https://github.com/marcospereirampj/python-keycloak/blob/8fd315d11a42a8b4afebfe84498e882bc0b736c8/keycloak/authorization/__init__.py#L78-L91](https://github.com/marcospereirampj/python-keycloak/blob/8fd315d11a42a8b4afebfe84498e882bc0b736c8/keycloak/authorization/__init__.py#L78-L91)

### Profiling
- [pyinstrument](https://github.com/joerick/pyinstrument)
- [pyperf](https://github.com/psf/pyperf)
- [scalene](https://github.com/plasma-umass/scalene)

| Profiler | What | Granularity | How |
| --- | --- | --- | --- |
| [timeit](https://docs.python.org/3/library/timeit.html) | run time | snippet-level |  |
| [cProfile](https://docs.python.org/3/library/profile.html#module-cProfile) | run time | method-level | deterministic |
| statprof.py | run time | method-level | statictical |
| [line_profiler](https://github.com/pyutils/line_profiler) | run time | line-level | deterministic |
| [memory_profiler](https://github.com/pythonprofilers/memory_profiler) | memory | line-level | +- deterministic |
| [pympler](https://github.com/pympler/pympler) | memory | method-level | deterministic |
Fonte: https://www.youtube.com/watch?v=DUCMjsrYSrQ

### PyPI mirror
- https://github.com/devpi/devpi
- https://github.com/pypa/bandersnatch

### requests
- https://github.com/requests/toolbelt/ #libs

### Retry
- https://github.com/jd/tenacity

### SSH
- Paramiko - [Homepage](https://www.paramiko.org/); [Docs](https://www.paramiko.org/); [Source](https://github.com/paramiko/paramiko)
	- It doesn't support SOCKS5 proxy (`ssh -D`) - [issue](https://github.com/paramiko/paramiko/pull/1873); [third-party PR](https://github.com/linwownil/paramiko/pull/1/)
	- Port forward [example](https://github.com/paramiko/paramiko/blob/main/demos/forward.py)
	- [sshtunnel](https://github.com/pahaz/sshtunnel) - SSH tunnels to remote server

### Pipelines
- https://github.com/pditommaso/awesome-pipeline
- https://temporal.io/
#### AI/Data
- dagster: https://github.com/dagster-io/dagster ![GitHub Repo stars](https://img.shields.io/github/stars/dagster-io/dagster)
	- cloud-native data pipeline orchestrator ... integrated lineage and observability ..., and best-in-class testability.
	- designed for developing and maintaining data assets, such as tables, data sets, machine learning models, and reports.
	- cloud: https://dagster.io/
	- [vs. Airflow](https://dagster.io/vs/dagster-vs-airflow)
	- [vs. Prefect](https://dagster.io/vs/dagster-vs-prefect)
- Metaflow: https://github.com/Netflix/metaflow ![GitHub Repo stars](https://img.shields.io/github/stars/Netflix/metaflow)
	- https://metaflow.org/
- Prefect: https://github.com/PrefectHQ/prefect ![GitHub Repo stars](https://img.shields.io/github/stars/PrefectHQ/prefect)
	- orchestrator for data-intensive workflows.
	- build and observe resilient data workflows so that you can understand, react to, and recover from unexpected changes.
	- [vs. Dagster](https://dagster.io/vs/dagster-vs-prefect)
- Pydra: https://github.com/nipype/pydra ![GitHub Repo stars](https://img.shields.io/github/stars/nipype/pydra)
	- A simple dataflow engine with scalable semantics.
- Ray: https://github.com/ray-project/ray ![GitHub Repo stars](https://img.shields.io/github/stars/ray-project/ray)
	- unified framework for scaling AI
	- consists of a core distributed runtime and a toolkit of libraries (Ray AIR) for simplifying ML compute

#### General
- [Airflow](https://github.com/apache/airflow) ![GitHub Repo stars](https://img.shields.io/github/stars/apache/airflow)
	- [vs. Dagster](https://dagster.io/vs/dagster-vs-airflow)
- ⭐️ [Joblib](https://github.com/joblib/joblib) ![GitHub Repo stars](https://img.shields.io/github/stars/joblib/joblib)
	- set of tools to provide lightweight pipelining.
	- Main features: disk-caching; parallel helper; fast compressed persistence.
	- How cache works? use [hash](https://github.com/joblib/joblib/blob/8a1faea0dd4aa6915044dd7a038da1f0de57c385/joblib/hashing.py#L244) to compare args
- [Luigi](https://github.com/spotify/luigi) ![GitHub Repo stars](https://img.shields.io/github/stars/spotify/luigi)
	- helps you build complex pipelines of batch jobs. It handles dependency resolution, workflow management, visualization, handling failures, command line integration, and much more.
- [Mara](https://github.com/mara/mara-pipelines) ![GitHub Repo stars](https://img.shields.io/github/stars/mara/mara-pipelines)
	- Principles: Data integration pipelines as code; PostgreSQL as a data processing engine; Extensive web ui; No in-app data processing; multiprocessing - single machine pipeline execution; nodes with higher cost are run first
- [Mistral](https://github.com/openstack/mistral) ![GitHub Repo stars](https://img.shields.io/github/stars/openstack/mistral)
	- integrated with OpenStack
	- define tasks and workflows in a simple YAML and a distributed environment
- [Ploomber](https://github.com/ploomber/ploomber) ![GitHub Repo stars](https://img.shields.io/github/stars/ploomber/ploomber) - [Docs](https://docs.ploomber.io/en/latest/index.html)
	-
- [pygrametl](https://github.com/chrthomsen/pygrametl) ![GitHub Repo stars](https://img.shields.io/github/stars/chrthomsen/pygrametl)
	- provides commonly used functionality for the development of ETL processes.
- [Pypeln](https://github.com/cgarciae/pypeln/) ![GitHub Repo stars](https://img.shields.io/github/stars/cgarciae/pypeln)
	- for creating concurrent data pipelines
	- Main Features: Simple; Easy-to-use; Flexible; Fine-grained Control.
	- Queues: Process; Thread; Task.
- ⭐️ [pypyr](https://github.com/pypyr/pypyr/) ![GitHub Repo stars](https://img.shields.io/github/stars/pypyr/pypyr)
	- task runner for automation pipelines
	- script sequential task workflow steps in yaml
	- conditional execution, loops, error handling & retries
- [SCOOP](https://github.com/soravux/scoop/) ![GitHub Repo stars](https://img.shields.io/github/stars/soravux/scoop)
	- distributed task module allowing concurrent parallel programming on various environments, from heterogeneous grids to supercomputers.
	- designed from the following ideas: the future is parallel; simple is beautiful; parallelism should be simpler.
	- brokers: TCP and ZeroMQ
- [SpiffWorkflow](https://github.com/sartography/SpiffWorkflow) ![GitHub Repo stars](https://img.shields.io/github/stars/sartography/SpiffWorkflow)
	- workflow engine implemented in pure Python.
	- support the development of low-code business applications in Python. Using BPMN will allow non-developers to describe complex workflow processes in a visual diagram
	- Built with: lxml; celery.
