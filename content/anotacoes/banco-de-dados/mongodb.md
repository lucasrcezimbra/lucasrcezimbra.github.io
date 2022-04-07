+++
title = "MongoDB"
date = 2018-11-21T21:28:05+00:00
aliases = [
    "/anotacoes/banco-de-dados/mongodb/",
    "/dicas-mongodb/",
]
+++


Como filtrar e atualizar elementos de um array
```javascript
// Atualiza para 'Python' todas as tags que o atributo 'nome' seja igual 'Phyton'
db.collection.updateMany(
    {},
    {'$set': {'tags.$[tag].nome': 'Python'}},
    {arrayFilters: [{'tag.nome': 'Phyton'}]}
)
```


Como atualizar nomes de campos de todos documentos de uma collection
```javascript
db.collection.updateMany(
    {},
    {$rename: {
        'campo_antigo': 'campo_novo',
        'segundo_campo_antigo': 'segundo_campo_novo'
    }}
)
```


Como filtrar pelo tamanho de uma string
```javascript
db.collection.find({"$expr": {"$lte": [{"$strLenCP": "$FIELD"}, 4]}})
```


Como atualizar um campo de todos documentos com a data atual
```javascript
 db.collection.updateMany({}, {$set: {FIELD: new Date()}})
```
