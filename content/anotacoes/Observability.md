---
title: "Observability"
date: 2023-08-15T07:30:00-03:00
---
- [Sentry]({{< ref "Sentry" >}})
- Transactions vs Spans
	- ![diagram-transaction-trace.png](../assets/diagram-transaction-trace_1678298375545_0.png)
	  from https://docs.sentry.io/product/sentry-basics/tracing/distributed-tracing/
	- Span
		- [Spans in OpenTelemetry](https://opentelemetry.io/docs/concepts/signals/traces/#spans-in-opentelemetry)
		- A Span represents a unit of work or operation. Spans are the building blocks of Traces.
		- A Span is best used to when the operation has a start and an end.
		- A Span Event is a information of the Span. It's best used to track operations with singular point in time.

## [LLM]({{< ref "LLM" >}})
- [arize](https://arize.com/)
- [baserun](https://baserun.ai/welcome) - From identifying an issue to evaluating the solution
- [Datadog](https://www.datadoghq.com/solutions/openai/) - OpenAI Monitoring
- [fiddler](https://www.fiddler.ai/llmops) - 
- [Gantry](https://www.gantry.io/) - observability, analytics, and evaluation for your AI-powered products.
- [Helicone](https://www.helicone.ai/) - monitoring, logging, and tracing for your LLM applications out of the box #OpenSource 
- [OpenInference](https://github.com/Arize-ai/openinference) - set of conventions and plugins that is complimentary to OpenTelemetry #OpenSource 
- [OpenLLMetry](https://github.com/traceloop/openllmetry) - set of extensions built on top of OpenTelemetry #OpenSource 
- [Phoenix](https://phoenix.arize.com/) - Evaluate, troubleshoot, and fine tune your LLM, CV, and NLP models in a notebook #OpenSource 
- [Vellum](https://www.vellum.ai/) - prompt engineering, semantic search, version control, quantitative testing, and performance monitoring.

## OpenTelemetry
- [Python]({{< ref "Python" >}}) [SDK](https://opentelemetry-python.readthedocs.io/en/latest/index.html)
- [Python]({{< ref "Python" >}}) instrumentation - [API doc](https://opentelemetry-python-contrib.readthedocs.io/en/latest/index.html) - [GitHub - opentelemetry-python-contrib](https://github.com/open-telemetry/opentelemetry-python-contrib)
- How to set the trace ID manually? - [Discussion](https://github.com/open-telemetry/opentelemetry-python/discussions/1919) - [Docs](https://opentelemetry.io/docs/instrumentation/python/cookbook/#manually-setting-span-context)
	```python
	  tracer = get_tracer()
	  propagator = get_global_textmap()
	  headers = request.headers
	  context = propagator.extract(headers)
	  
	  with tracer.start_as_current_span("span_name", context=context):
	      ...
	  ```
- How to rename `RequestsInstrumentor` events? passing a function for the `name_callback` argument
- How to manually add `trace_id` to a transaction
	```python
	  context = context=get_global_textmap().extract(app.current_request.headers)
	  with tracer.start_as_current_span("span_name", content=content):
	    ...
	  ```
	- [Example](https://github.com/getsentry/sentry-python/blob/1e3e1097e104abb39799b59654bf4f8725448909/sentry_sdk/integrations/opentelemetry/propagator.py#L45) of a propagator (textmap) extract