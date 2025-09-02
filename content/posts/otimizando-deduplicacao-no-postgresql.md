---
title: "Otimizando deduplicação no PostgreSQL"
description: "Como uma simples mudança pode reduzir o tamanho de uma tabela em quase 90%"
date: 2025-07-29
lastmod: 2025-09-02
---

Esse post foi originalmente publicado como uma newsletter no Substack. Inscreva-se para receber novos posts diretamente no seu e-mail.

<iframe src="https://lucasrcezimbra.substack.com/embed" width="100%" height="320" style="border:1px solid #EEE; background:white;" frameborder="0" scrolling="no"></iframe>

---

Gosto de ler como outras pessoas resolveram problemas porque isso aumenta meu repertório para quando encontrar problemas semelhantes. Espero que esse texto faça o mesmo por você.

Na edição de hoje, vou contar como uma troca simples no modelo de dados pode economizar quase 90% do armazenamento, sem aumentar a complexidade da aplicação.

Se você já precisou deduplicar mensagens, lidou com gargalos de banco de dados ou acha que escalar exige sempre algo complexo, esse texto pode lhe trazer bons insights.

---

Há algum tempo, meu amigo [Moacir Moda](https://moacirmoda.substack.com/) mandou uma mensagem pedindo ajuda para resolver um problema técnico. Ele estava com um problema bom: seu negócio estava crescendo rapidamente e o banco de dados estava sendo um gargalo.

A conversa começou mais ou menos assim:

> Tenho uma tabela no Postgres com 300 milhões de registros e 6 colunas (2 datetime, 2 integer, 1 boolean e 1 char 255). Eu só uso essa tabela para deduplicar mensagens; faço um insert na tabela, se der erro de duplicidade, o processamento é abortado. A tabela já tem índices, mas está prejudicando o banco todo, especialmente em relação a storage. Existe uma solução mais simples/eficiente para resolver isso?

## Contexto
### Entendendo o problema

Eu precisava de um pouco mais de contexto para poder ajudar, então comecei com algumas perguntas para entender o problema.

-   Quanto tempo tem que guardar esses registros? Pode ser que o evento venha duplicado após dias? Como esse evento chega para ser processado? É uma fila?
    -   3 meses. Estamos colocando um processo para limpar depois de 3 meses. Esse evento vem numa fila. Essa verificação ocorre no começo e diz se o processo deve seguir ou não.
-   Qual o risco de processar duplicado? Não pode acontecer de forma nenhuma? A mensagem é duplicada pelo _producer_ (múltiplas mensagens) ou pela fila (múltiplas entregas da mesma mensagem)?
    -   Não pode duplicar. Quem duplica é o _producer_.


### Calculando o tamanho da tabela

Parti para uma conta de padeiro (ou [Napkin Math](https://github.com/sirupsen/napkin-math)) e fui calcular o tamanho atual da tabela que tinha “2 datetime, 2 integer, 1 boolean e 1 char 255”. Fui buscar na documentação do PostgreSQL quanto cada um desses tipos ocupa de armazenamento:

-   _timestamp_ (com ou sem timezone) = 8 _bytes_ ([docs](https://www.postgresql.org/docs/current/datatype-datetime.html))
-   _integer_ = 4 _bytes_ ([docs](https://www.postgresql.org/docs/current/datatype-numeric.html#DATATYPE-INT))
-   _boolean_ = 1 _byte_ ([docs](https://www.postgresql.org/docs/current/datatype-boolean.html))
-   _char_ 255 = 259 _bytes_ ([docs](https://www.postgresql.org/docs/current/datatype-character.html))

```
8 + 8 + 4 + 4 + 1 + 259 =
284 bytes por linha da tabela
```


## Proposta

Então pensei o seguinte: se o problema está sendo _storage_ e a tabela serve só para deduplicar, poderíamos diminuí-la se guardássemos somente um _hash_ de cada mensagem.

Um _SHA-1_ tem 40 caracteres, daria para armazená-lo usando um char 40, que ocupa 41 bytes. Isso economizaria 243 bytes (284 - 41) por linha da tabela ou ~85%.

72.9 GB (243 bytes \* 300 milhões de registros) de economia na tabela inteira.

```
char40 = 41 bytes
284 − 41 = 243 bytes
243 × 300 000 000 = 72,9 GB
```

Essa foi a minha ideia inicial. Pensando agora, daria para otimizar ainda mais.


### Otimizando o espaço do sha1

_SHA-1_ é normalmente representado por um hexadecimal de 40 caracteres, ou seja, 41 bytes. Porém, o _SHA-1_ é um _hash_ de 20 _bytes_. Poderíamos utilizar o tipo [BYTEA](https://www.postgresql.org/docs/current/datatype-binary.html) do PostgreSQL e manter o _hash_ em formato binário. O _bytea_ ocupa 4 bytes mais o tamanho do binário. No caso de um _SHA-1_, seriam 20 + 4 _bytes_ = 24 bytes.

Economizaríamos 260 bytes (284 - 24) por linha da tabela ou ~91%.

260 bytes \* 300 milhões de registros = 78 GB de economia.

```
sha1_as_bytea = 24 bytes
284 − 24 = 260 bytes
260 × 300 000 000 = 78 GB
```

Não cheguei a testar essa abordagem, mas acredito que funcione.


### Limpando os registros antigos

Após 3 meses os registros não são mais necessários e podem ser descartados. Se salvarmos somente o _hash_, como saberemos quais registros podem ser apagados?

Eu consigo pensar em duas soluções:

1.  Criar uma tabela por período (mês ou dia) e apagar a tabela inteira após os 3 meses. Essa solução pode adicionar alguma complexidade na aplicação dependendo de como o banco de dados esteja sendo gerenciado (ORM, por exemplo).
2.  Abrir mão da economia de 8 _bytes_ por linha e manter uma coluna de _datetime_ com a data de criação do registro. Essa seria minha primeira opção. Acredito que seja uma troca interessante, 8 bytes para poder continuar eliminando os registros antigos. O tamanho da tabela ficaria assim:

```
datetime = 8 bytes
sha1_as_bytea = 24 bytes
24 + 8 = 32
284 - 32 = 252 bytes
252 × 300 000 000 = 75,6 GB
```

Ainda assim, temos uma economia de ~88%.

## Receios
### SHA-1 e o risco de colisão
O _SHA-1_ não é seguro para senhas por ser possível colidir dois _hashes_ intencionalmente (veja [SHAttered](https://shattered.io/)). Porém, para uso interno, como deduplicar mensagens, podemos utilizá-lo sem problemas.

O risco de um _SHA-1_ colidir aleatoriamente é muito baixo. O número total de _SHA-1_ únicos é 2^160 ou esse número gigante:

```
1461501637330902918203684832716283019655932542976
```

Precisaríamos de aproximadamente 2^80 itens para uma probabilidade ~50% de colisão. É uma possibilidade muito remota.

### Desempenho da aplicação
Computar um _SHA-1_ é rápido. Rodei esse pequeno script no IPython para ver quanto tempo leva para gerar o _SHA-1_ de um _dict_.

```python
import hashlib
import json
from datetime import datetime

d = {
    'datetime1': datetime.now().isoformat(),
    'datetime2': datetime.now().isoformat(),
    'int1': 42,
    'int2': 42 * 42,
    'cha255': '_' * 255
}

%timeit hashlib.sha1(json.dumps(d, sort_keys=True).encode()).hexdigest()

# 4.82 μs ± 744 ns per loop (mean ± std. dev. of 7 runs, 100,000 loops each)
```

Ou seja, o script levou em média 4.82 μs (microssegundos) para computar o _SHA-1_ do _dict_ de exemplo.

## Alternativas
Por que não extrair essa tabela do PostgreSQL e colocar em um Memcached, Valkey, MongoDB, etc.?

Não conheço a _stack_ do projeto a fundo, então não sei quais ferramentas eles já têm disponíveis. Adicionar outra ferramenta à stack tem um custo; é uma nova infraestrutura para gerenciar (ainda que seja gerenciada por alguma _cloud_, existe um custo de configuração e manutenção); é outro ponto de falha no sistema; é outra ferramenta que o time tem que conhecer e utilizar; etc.

Eu costumo manter o mínimo de infraestrutura possível nos meus projetos. Como as aplicações normalmente já necessitam de um banco de dados, eu o utilizo para outras funções como fila, cache, etc. até que o banco seja um gargalo. Para identificar os gargalos é importante sempre contar com ferramentas de observabilidade.

Além disso, o PostgreSQL é "parrudo". Ele aguenta muita carga. 300 milhões de linhas não são um problema para o banco gerenciar. O que me leva ao próximo ponto.

## 75 GB fazem diferença?
A grande vantagem que eu vejo nessa solução é a simplicidade. Uma simples refatoração para causar essa economia de ~88%. Sem a necessidade de adicionar novas ferramentas à stack nem fazer grandes mudanças na aplicação.

Se exigisse uma grande mudança arquitetural, talvez não valesse a pena e fosse melhor pagar mais por uma infra maior. Temos sempre que levar em conta o _trade-off_ entre custo de máquina vs. custo de desenvolvimento. Pagar por máquinas é mais barato do que o custo com desenvolvedores (pelo menos até a IA fazer todo o trabalho).

Outro ponto é que a economia vai crescendo com o sistema. O produto do Moacir [mais que dobrou o MRR](https://moacirmoda.substack.com/p/o-tintim-chegou-a-r-500k-mrr) desde essa conversa. Vamos supor que o número de eventos a serem deduplicados cresça na mesma proporção que o MRR, então teria crescido cerca de 2.5x. Ou seja, essa tabela teria aumentado de 300 milhões de registros para 750 milhões e a economia saído de 75,6 GB para 189 GB.

## Conclusão
Essa foi a proposta que eu cheguei olhando o projeto de fora, tendo somente o contexto que descrevi no começo do texto. O que o Moacir me falou foi que a minha sugestão os ajudou a resolver o problema. Espero que tenha te dado alguns _insights_ também.

E aí, o que achou da solução? Resolveria de alguma outra forma? [Deixe um comentário no Substack](https://lucasrcezimbra.substack.com/p/otimizando-deduplicacao-no-postgresql/comments) e vamos conversar.

Você está com algum problema desse tipo no seu projeto? Às vezes, alguém vendo o problema de fora pode nos ajudar. Me mande uma mensagem contando um problema técnico que você está enfrentando e quem sabe a próxima newsletter é contando como eu te ajudei.

## Referências
-   [https://www.postgresql.org/docs/current/datatype-boolean.html](https://www.postgresql.org/docs/current/datatype-boolean.html)
-   [https://www.postgresql.org/docs/current/datatype-character.html](https://www.postgresql.org/docs/current/datatype-character.html)
-   [https://www.postgresql.org/docs/current/datatype-datetime.html](https://www.postgresql.org/docs/current/datatype-datetime.html)
-   [https://www.postgresql.org/docs/current/datatype-numeric.html#DATATYPE-INT](https://www.postgresql.org/docs/current/datatype-numeric.html#DATATYPE-INT)
-   [https://stackoverflow.com/questions/62664761/probability-of-hash-collision](https://stackoverflow.com/questions/62664761/probability-of-hash-collision)
-   [https://shattered.io/](https://shattered.io/)
-   [https://pt.wikipedia.org/wiki/Paradoxo\_do\_anivers%C3%A1rio](https://pt.wikipedia.org/wiki/Paradoxo_do_anivers%C3%A1rio)
-   [https://calculator.aws/#/createCalculator/RDSPostgreSQL](https://calculator.aws/#/createCalculator/RDSPostgreSQL)

---

Esse post foi originalmente publicado como uma newsletter no Substack. Inscreva-se para receber novos posts diretamente no seu e-mail.

<iframe src="https://lucasrcezimbra.substack.com/embed" width="100%" height="320" style="border:1px solid #EEE; background:white;" frameborder="0" scrolling="no"></iframe>
