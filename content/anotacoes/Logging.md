---
title: Logging
date: 2024-08-21
lastmod: 2024-10-07
aliases:
---

## Output
### Fields
- Timestamp
- Level name (human-readable) and number (to filter by greater or lesser).
- Filepath, line number, and function name to locate the source code.
- Process and thread IDs to debug concurrency issues.


### Plaintext vs Structured
- Plaintext
    * pros: most commom; human-readable;
    * cons: hard to parse;
- Structured
    * pros: easy to parse; easy to search/filter/aggregate;
    * cons: verbose; less human-readable (can be solved by showing only the
      message);

#### Structured formats
- logfmt
    * pros: more human-readable; less verbose;
    * cons:
- JSON
    * pros:
    * cons: less human-readable; more verbose;



## Tools
- [Fluentd](https://github.com/fluent/fluentd) - Unified Logging Layer -
  collects events from various data sources and writes them to different
  destinations
- [loguru](https://github.com/delgan/loguru) - Logging for
  [Python]({{< ref "Python" >}})
    * [Entirely compatible with standard logging](https://loguru.readthedocs.io/en/stable/overview.html#entirely-compatible-with-standard-logging)
    * [Django integration using InterceptHandler](https://github.com/Delgan/loguru/issues/977#issuecomment-1771575984)
    * [Logger.bind](https://loguru.readthedocs.io/en/stable/api/logger.html#loguru._logger.Logger.bind)
- [python-json-logger](https://github.com/madzak/python-json-logger) - JSON
  formatter for [Python]({{< ref "Python" >}})
- [python-logfmter](https://github.com/jteppinette/python-logfmter) - logfmt
  formatter for [Python]({{< ref "Python" >}})
- [structlog](https://github.com/hynek/structlog) - Structured Logging for
  [Python]({{< ref "Python" >}}); supports output as JSON, logfmt, plaintext
    * [django-structlog](https://github.com/jrobichaud/django-structlog)
    * [Standard Library support](https://www.structlog.org/en/stable/standard-library.html)
    * [Building a Context](https://www.structlog.org/en/stable/getting-started.html#building-a-context)



## References
- [12factor - XI. Logs](https://12factor.net/logs)
- [Canonical Log Lines 2.0](https://brandur.org/nanoglyphs/025-logs#canonical-log-lines-2)
- [Fast and flexible observability with canonical log lines](https://stripe.com/blog/canonical-log-lines)
- [logfmt](https://brandur.org/logfmt)
- [structlog - Why ...](https://www.structlog.org/en/stable/why.html)
- [Python - logging - LogRecord attributes](https://docs.python.org/3/library/logging.html#logrecord-attributes)
