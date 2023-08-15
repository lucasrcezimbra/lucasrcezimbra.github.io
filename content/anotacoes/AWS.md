---
title: "AWS"
date: 2023-08-15T07:30:00-03:00
---
## Lambda

### Observability

- [AWS Lambda Powertools (Python)](https://github.com/awslabs/aws-lambda-powertools-python)
- [honeycomb-lambda-extension](https://github.com/honeycombio/honeycomb-lambda-extension)
- [OpenTelemetry Automatic Instrumentation (Python)](https://opentelemetry.io/docs/instrumentation/python/automatic/)
- AWS Service Lens
- AWS X-Ray


## RDS
- [Terraform]({{< ref "Terraform" >}}) modules
	- RDS - https://registry.terraform.io/modules/terraform-aws-modules/rds/aws/latest
	- Aurora - https://registry.terraform.io/modules/terraform-aws-modules/rds-aurora/aws/latest

### Aurora
#### Replicas
- Auto scalling increases replicas when necessary. 
- Aurora has 1 writer and up to 15 read replicas.
> Write operations are managed by the primary instance.
> 
> The Aurora Replicas can be **distributed across the Availability Zones** that a DB cluster spans within an AWS Region.
> 
> If the writer instance in a cluster becomes unavailable, Aurora automatically **promotes one of the reader instances to take its place as the new writer**.
> 
> https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Replication.html#Aurora.Replication.Replicas

#### Vertical scale
> It can take 15 minutes or more to complete the change to a different DB instance class.
> 
> https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.Managing.html#AuroraPostgreSQL.Managing.Performance.InstanceScaling

- How to scale the writer replica vertically with minimal downtime? 
> (1) add an Aurora Replica to your cluster, ... choose the DB instance class size that you want to use for your cluster.
> 
> (2) When the Aurora Replica is synchronized with the cluster, you then failover to the newly added Replica. 
> 
> https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.Managing.html#AuroraPostgreSQL.Managing.Performance.InstanceScaling

#### Tunning
- Managing query execution plans (...) - https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.Optimize.html

#### Serverless
> v2 writers and readers don't scale all the way down to zero ACUs. (minimum is 0.5 ACU)
> 
> (...) v1 (..) can pause after a period of idleness, but then takes some time to resume when you open a new connection. 
> 
> https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-serverless-v2.how-it-works.html#aurora-serverless-v2.how-it-works.scaling 


## S3
### Versioning
- How am I charged for using Versioning?
> 	Normal Amazon S3 rates apply for every version of an object stored or requested.
> 	
>     from https://aws.amazon.com/s3/faqs/