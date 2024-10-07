---
title: "Hasura"
date: 2023-08-15
lastmod: 2024-10-07
---

- [Hasura CE Changelog](https://hasura.io/changelog/community-edition)
- cli-migrations [Docker]({{< ref "Docker" >}}) image
	- > automatically apply Migrations/Metadata when the server starts
	- [cli-migrations image](https://hasura.io/docs/latest/migrations-metadata-seeds/legacy-configs/config-v2/advanced/auto-apply-migrations/#cli-migrations-image)
- [API Limits](https://hasura.io/docs/latest/security/api-limits/)
	- It's not available on self-hosted open source
	- [Metadata API Reference: API Limits](https://hasura.io/docs/latest/api-reference/metadata-api/api-limits/)
- config.yaml reference: [Hasura CLI Configuration Reference](https://hasura.io/docs/latest/hasura-cli/config-reference/)
	- [Environment variables](https://hasura.io/docs/latest/hasura-cli/config-reference/#environment-variables)
- [AWS Aurora: Is it for you?](https://hasura.io/blog/aws-aurora-is-it-for-you/)
- [Auditing Actions on Tables in Postgres](https://hasura.io/docs/latest/schema/postgres/postgres-guides/auditing-tables/)

## Watch Outs
- Lack of observability (in the self-hosted open source plan)
- [GraphQL]({{< ref "GraphQL" >}}) apps leads to to spread business logic in the
  frontend
- Security concerns of exposing a database directly via
  [GraphQL]({{< ref "GraphQL" >}})
- Hasura migrations does NOT run in a transaction by default. If a migration
  file with multiple SQL statements fails, the applied statements are NOT
  rolled back. For example:
  ```sql
  -- migrations/default/1715938531000_my_custom_migration/up.sql
  CREATE TABLE users (
    id serial PRIMARY KEY,
    name text NOT NULL
  );

  -- For some reason, this migration fails in the posts table creation
  CREATE TABLE posts (
    id serial PRIMARY KEY,
    title text NOT NULL,
    author_id integer NOT NULL REFERENCES users(id)
  );
  ```
  If you retry the migration, it will fail because the users table already
  exists.
