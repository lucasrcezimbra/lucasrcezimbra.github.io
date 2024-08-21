---
title: Logging
date: 2024-08-21
lastmod: 2024-08-21
aliases:
---

## Output
### Plaintext vs Structured
- Plaintext
    * pros: human-readable;
    * cons: hard to parse;
- Structured
    * pros: easier to parse; easy to search/filter/aggregate;
    * cons: verbose; less human-readable (can be solved by showing only the
      message);

### Structured formats
- JSON
- Logfmt

## Tools
- [Fluentd](https://github.com/fluent/fluentd) - Unified Logging Layer -
  collects events from various data sources and writes them to different
  destinations
- [loguru](https://github.com/delgan/loguru) - Logging for
  [Python]({{< ref "Python" >}})
- [python-json-logger](https://github.com/madzak/python-json-logger) - JSON
  formatter for [Python]({{< ref "Python" >}})
- [python-logfmter](https://github.com/jteppinette/python-logfmter) - logfmt
  formatter for [Python]({{< ref "Python" >}})
- [structlog](https://github.com/hynek/structlog) - Structured Logging for
  [Python]({{< ref "Python" >}}); supports output as JSON, logfmt, plaintext
    * [django-structlog](https://github.com/jrobichaud/django-structlog)

## References
- [Canonical Log Lines 2.0](https://brandur.org/nanoglyphs/025-logs#canonical-log-lines-2)
- [Fast and flexible observability with canonical log lines](https://stripe.com/blog/canonical-log-lines)
- [logfmt](https://brandur.org/logfmt)
