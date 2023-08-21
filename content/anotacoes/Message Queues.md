---
title: "Message Queues"
date: 2023-08-15T07:30:00-03:00
---
## AWS SQS

## Database-Backed
- [Postgres: a Better Message Queue than Kafka?](https://dagster.io/blog/skip-kafka-use-postgres-message-queue)
- [The Database As Queue Anti-Pattern](http://mikehadlow.blogspot.com/2012/04/database-as-queue-anti-pattern.html)

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

