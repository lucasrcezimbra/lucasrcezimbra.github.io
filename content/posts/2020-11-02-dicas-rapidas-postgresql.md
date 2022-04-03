---
title: Dicas rápidas PostgreSQL
author: Lucas Cezimbra
type: post
date: 2020-11-02T18:25:21+00:00
url: /dicas-rapidas-postgresql/
categories:
  - Dicas Rápidas
tags:
  - database
  - dicas
  - postgres

---
  * Como apagar todas as tabelas do banco ⚠

<pre class="wp-block-code"><code>DROP SCHEMA public CASCADE;
CREATE SCHEMA public;</code></pre>