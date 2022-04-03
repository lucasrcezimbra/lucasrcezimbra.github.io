+++
title = 'Dicas rápidas Oracle Database'
date = 2019-03-26T18:27:03+00:00
url = '/dicas-rapidas-oracle-database/'
categories = ['Dicas Rápidas']
tags = ['database', 'dicas', 'oracle']
+++


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
