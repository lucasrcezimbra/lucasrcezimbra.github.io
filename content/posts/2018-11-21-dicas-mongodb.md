---
title: Dicas rápidas MongoDB
author: Lucas Cezimbra
type: post
date: 2018-11-21T21:28:05+00:00
url: /dicas-mongodb/
categories:
  - Dicas Rápidas
tags:
  - database
  - dicas
  - mongodb

---
  * Como filtrar e atualizar elementos de um array

<pre class="wp-block-code"><code>// Atualiza para 'Python' todas as tags que o atributo 'nome' seja igual 'Phyton'
db.collection.updateMany(
    {},
    {'$set': {'tags.$[tag].nome': 'Python'}},
    {arrayFilters: [{'tag.nome': 'Phyton'}]}
)</code></pre>

  * Como atualizar nomes de campos de todos documentos de uma collection

<pre class="wp-block-code"><code>db.collection.updateMany({}, {$rename: {'campo_antigo': 'campo_novo', 'segundo_campo_antigo': 'segundo_campo_novo'}})</code></pre>

  * Como filtrar pelo tamanho de uma string

<pre class="wp-block-code"><code>db.collection.find({"$expr": {"$lte": [{"$strLenCP": "$FIELD"}, 4]}})</code></pre>

  * Como atualizar um campo de todos documentos com a data atual

<pre class="wp-block-code"><code> db.collection.updateMany({}, {$set: {FIELD: new Date()}})</code></pre>