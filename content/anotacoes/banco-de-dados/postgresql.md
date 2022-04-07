+++
title = 'PostgreSQL'
date = 2020-11-02T18:25:21+00:00
aliases = [
    "/anotacoes/banco-de-dados/postgresql/",
    "/dicas-rapidas-postgresql/",
]
+++


Como apagar todas as tabelas do banco ⚠
```sql
DROP SCHEMA public CASCADE;
CREATE SCHEMA public;
```
