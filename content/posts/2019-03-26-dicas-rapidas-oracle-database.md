---
title: Dicas rápidas Oracle Database
author: Lucas Cezimbra
type: post
date: 2019-03-26T18:27:03+00:00
url: /dicas-rapidas-oracle-database/
categories:
  - Dicas Rápidas
tags:
  - database
  - dicas
  - oracle

---
Criar um usuário para o banco de dados

<pre class="wp-block-code"><code>CREATE USER my_user IDENTIFIED BY my_password;</code></pre>

Alterar a senha de um usuário já existente

<pre class="wp-block-code"><code>ALTER USER my_user IDENTIFIED BY my_password;</code></pre>

Adicionar _grants_ para um usuário do banco

<pre class="wp-block-code"><code>GRANT 
    insert,
    select,
    update,
    delete
ON
    my_table
TO
    my_user;</code></pre>