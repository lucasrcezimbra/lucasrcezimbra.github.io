+++
title = 'Dicas rápidas PostgreSQL'
date = 2020-11-02T18:25:21+00:00
url = '/dicas-rapidas-postgresql/'
categories = ['Dicas Rápidas']
tags = ['database', 'dicas', 'postgres']
+++


Como apagar todas as tabelas do banco ⚠
```sql
DROP SCHEMA public CASCADE;
CREATE SCHEMA public;
```
