---
title: "PostgreSQL"
date: 2023-08-15T07:30:00-03:00
---
+++
title = 'PostgreSQL'
date = 2020-11-02T18:25:21+00:00
aliases = [
    "/anotacoes/banco-de-dados/postgresql/",
    "/dicas-rapidas-postgresql/",
    "/psql/",
]
+++


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


Row-Level permission
- https://www.postgresql.org/docs/current/ddl-rowsecurity.html
- https://www.enterprisedb.com/postgres-tutorials/how-implement-column-and-row-level-security-postgresql


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
