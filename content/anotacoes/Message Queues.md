---
title: "Message Queues"
date: 2023-08-15
lastmod: 2024-10-07
---

## AWS SQS
- [Alternatives to]({{< ref "Alternatives to" >}}) - [ElasticMQ](https://github.com/softwaremill/elasticmq)

## Database-Backed
- [Postgres: a Better Message Queue than Kafka?](https://dagster.io/blog/skip-kafka-use-postgres-message-queue)
- [The Database As Queue Anti-Pattern](http://mikehadlow.blogspot.com/2012/04/database-as-queue-anti-pattern.html)
	1. Polling: short interval = hit database too much; long internal = delay processing
		1. On Postgres can avoid pooling by using `LISTEN`/`NOTIFY`
	2. Performance: no index=slow queries, indexes=slow inserts
		1. Locks: can be a problem.
	3. Purge: needs to clear the table at intervals
	4. Coupling: need to share database between services
		- not an issue for monoliths

## Kafka


## RabbitMQ


## Redis-Backed
### Pub/Sub
- Consumer `SUBSCRIBE` to a key and producers `PUBLISH` to the same key.
- at-most-once: if the consumer was down that data is lost.
- no data persistence: if Redis goes down, all data is lost.
### List
- List is a Redis data structure that can be used to create a FIFO queue.
- Producers uses `RPUSH` to append to the list and consumers uses `BLPOP` to read from the same list.
- consumer group: each message is consumed by only one consumer if more than one is waiting on the same list.
- disk persistence: can be persisted to disk.
### Stream
- Consumers can choose where to read messages from: `$` for new messages; `<id>` for a specific message; `0-0` for the first message.
- Producer uses `XADD` and consumers `XREAD`
