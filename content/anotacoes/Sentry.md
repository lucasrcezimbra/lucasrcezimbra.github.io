---
title: "Sentry"
date: 2023-08-15
lastmod: 2023-08-15
---
- How to Discover what project and environment is sending too many events?
	- `https://<tenant>.sentry.io/discover/homepage/?field=title&field=event.type&field=project&field=user.display&field=timestamp&field=replayId&name=All+Events&query=event.type%3Atransaction&sort=-timestamp&statsPeriod=30d&yAxis=count%28%29`
- [Python]({{< ref "Python" >}})
	- API documentation: https://getsentry.github.io/sentry-python/
	- [AWS]({{< ref "AWS" >}}) Lambda: https://docs.sentry.io/platforms/python/guides/aws-lambda/
	- [OpenTelemetry]({{< ref "OpenTelemetry" >}}) support: https://docs.sentry.io/platforms/python/performance/instrumentation/opentelemetry/
	- Stdlib trace HTTP propagation code: https://github.com/getsentry/sentry-python/blob/d991be73193d833ea9954d0cd82a3923e64e8d43/sentry_sdk/integrations/stdlib.py#L106
- [Javascript]({{< ref "Javascript" >}})
	- Documentation: https://docs.sentry.io/platforms/javascript/
- https://develop.sentry.dev/
- [GraphQL]({{< ref "GraphQL" >}}) support discussion - https://github.com/getsentry/sentry/discussions/38913
