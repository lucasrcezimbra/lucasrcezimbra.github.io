---
title: Oracle
date: 2019-03-26
lastmod: 2023-09-27
aliases:
  - /anotacoes/banco-de-dados/oracle/
  - /dicas-rapidas-oracle-database/
---
Criar um usuário para o banco de dados
```sql
CREATE USER my_user IDENTIFIED BY my_password;
```


Alterar a senha de um usuário já existente
```sql
ALTER USER my_user IDENTIFIED BY my_password;
```


Adicionar _grants_ para um usuário do banco
```sql
GRANT
    insert,
    select,
    update,
    delete
ON
    my_table
TO
    my_user;
```
