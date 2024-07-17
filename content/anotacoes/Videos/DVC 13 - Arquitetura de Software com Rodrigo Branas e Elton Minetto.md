---
title: "DVC 13 - Arquitetura de Software com Rodrigo Branas e Elton Minetto"
date: 2024-07-14
lastmod: 2024-07-17
---

https://www.youtube.com/watch?v=t4o1tOV3q78

## Notas
- Livro [Building Evolutionary Architectures - Neil Ford](https://evolutionaryarchitecture.com/) - Lean Startup aplicado a arquitetura
- (12:08) o objetivo da arquitetura de software é minimizar a quantidade de
recursos que você precisa construir e manter **required** systems - Uncle Bob
- (16:05) as decisões de arquitetura (por exemplo, a linguagem escolhida)
restringem o design que você pode aplicar no código
- (17:23) "na maior parte das empresas não faria diferença usar a linguagem A, B
ou C"
- (17:38) é importante mapear as decisões caras de mudar (por exemplo, OO ou
funcional)
- (19:20) tomada de decisão: gastar tempo em experimentação (PoC, método
cientifico) para as decisões caras;
- documentar: porque foi feito; o que foi testado; o caminho até a decisão, não
somente a decisão final; contexto do momento da decisão (como no ADR)
- (24:40) automatizar tudo o que puder dos "checks" das decisões. por exemplo,
automatizar o check de determinado padrão do nome das PKs nos bancos;
automatizar load tests
- a decisão tem que vir do time porque é quem tem o contexto
- Cuidado com o Career Driven Development - o que é bom para carreira nem sempre
é bom para o produto/empresa. O foco tem que ser resolver o problema e não usar
tech pra colocar no curriculo.
- (28:28) Nunca resolver ou fazer o primeiro draft para o time. Sempre deixar a
ideia partir do time e a judar a polir por meio de perguntas.
- (30:20) Exemplo de baby steps: não precisa resolver tudo de uma vez. Por ser
incremental. Exemplo: começar usando SQS que já estava disponível na stack ao
invés de adicionar um Kafka.
- Livro Enterprise Integration Patterns
- Bounded Contexts?
- Buy vs Build
- (48:40) Transaction Script?
- (51:35) Frameworks tem seu próprio design.
- (53:25) Melhor um framework de comunidade do que interno - possibilidade de
trazer pessoas que já conhecem.
- (55:00) Balanço entre comportamento (negócio) e estrutura (tech/sustenta o
comportamento).
    * Focar só no comportantamento tende a perder produtividade com o tempo,
      dificultar escala, contratação, retenção.
    * Focar só estrutura não entrega o negócio que sustenta a empresa.
- Outside testing (comunidade Rails)?
- (56:45) Testabilidade: olhar para hexagonal. A borda é expor para diferentes
drivers (fila, HTTP, CLI, etc.).
- (59:33) CRUD: esqueça o banco ao modelar API REST.
