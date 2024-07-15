---
title: 'PostgreSQL'
date: 2020-11-02
lastmod: 2024-06-05
aliases: [
    "/anotacoes/banco-de-dados/postgresql/",
    "/dicas-rapidas-postgresql/",
    "/psql/",
]
---
- [Serverless Postgres](https://neon.tech/)
- [Postgres: a Better Message Queue than Kafka?](https://dagster.io/blog/skip-kafka-use-postgres-message-queue)

`\` commands
```
\d - list tables, views, and sequences
\dn - list schemas
```

Como listar todas as tabelas do banco
```sql
SELECT 
    *
FROM
    pg_catalog.pg_tables
WHERE
    schemaname != 'pg_catalog'
    AND schemaname != 'information_schema'
;
```

Como apagar todas as tabelas do banco :warning:
```sql
DROP SCHEMA public CASCADE;
CREATE SCHEMA public;
```

Remover todos caracteres que não são letras
```sql
regexp_replace(value, '[^A-z ]+', '', 'g')
```


Criar uma função PL/pgSQL
```sql
CREATE OR REPLACE FUNCTION even_odds(max int)
 RETURNS int[][]
 LANGUAGE plpgsql
AS $function$
DECLARE
    evens int[] := Array[]::int[];
    odds int[] := Array[]::int[];
BEGIN
    FOR n IN 1..max loop
        IF n % 2 = 0 then
            evens := ARRAY_APPEND(evens, n);
        ELSE
            odds := ARRAY_APPEND(odds, n);
        END IF;
    END LOOP;

    RETURN Array[evens, odds];
END;
$function$
;

SELECT even_odds(100);
```

## Row-level permission
- https://www.postgresql.org/docs/current/ddl-rowsecurity.html
- https://www.enterprisedb.com/postgres-tutorials/how-implement-column-and-row-level-security-postgresql
