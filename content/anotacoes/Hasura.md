---
title: "Hasura"
date: 2023-08-15T07:30:00-03:00
---
- Changelog - https://hasura.io/changelog/community-edition
- cli-migrations [Docker]({{< ref "Docker" >}}) image
	- > automatically apply Migrations/Metadata when the server starts
	- https://hasura.io/docs/latest/migrations-metadata-seeds/legacy-configs/config-v2/advanced/auto-apply-migrations/#cli-migrations-image
- API Limits
	- It's not available on self-hosted open source
	- Docs: https://hasura.io/docs/latest/security/api-limits/
	- Metadata API Reference: https://hasura.io/docs/latest/api-reference/metadata-api/api-limits/
- config.yaml reference: https://hasura.io/docs/latest/hasura-cli/config-reference/
	- CLI environment variables: https://hasura.io/docs/latest/hasura-cli/config-reference/#environment-variables
- Hasura and AWS Aurora: https://hasura.io/blog/aws-aurora-is-it-for-you/
- Audit logs w/ Postgres: https://hasura.io/docs/latest/schema/postgres/postgres-guides/auditing-tables/