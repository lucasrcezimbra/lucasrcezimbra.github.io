---
title: Logging
date: 2024-08-21
lastmod: 2024-10-31
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
Moved to My Toolbox - [Logging](https://toolbox.cezimbra.me/lists/logging/),
[Python - Logging](https://toolbox.cezimbra.me/lists/python-logging/), and
[Django - Logging](https://toolbox.cezimbra.me/lists/django-logging/)



## References
- [12factor - XI. Logs](https://12factor.net/logs)
- [Canonical Log Lines 2.0](https://brandur.org/nanoglyphs/025-logs#canonical-log-lines-2)
- [Fast and flexible observability with canonical log lines](https://stripe.com/blog/canonical-log-lines)
- [logfmt](https://brandur.org/logfmt)
- [structlog - Why ...](https://www.structlog.org/en/stable/why.html)
- [Python - logging - LogRecord attributes](https://docs.python.org/3/library/logging.html#logrecord-attributes)
