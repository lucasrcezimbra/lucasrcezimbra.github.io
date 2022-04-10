+++
title = 'PostgreSQL'
date = 2020-11-02T18:25:21+00:00
aliases = [
    "/anotacoes/banco-de-dados/postgresql/",
    "/dicas-rapidas-postgresql/",
]
+++


Como apagar todas as tabelas do banco :warning:
```sql
DROP SCHEMA public CASCADE;
CREATE SCHEMA public;
```


Remover todos caracteres que não são letras
```sql
regexp_replace(value, '[^A-z ]+', '', 'g')
```
