---
title: "Hasura"
date: 2023-08-15
lastmod: 2024-07-30
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

## Watch Outs
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
