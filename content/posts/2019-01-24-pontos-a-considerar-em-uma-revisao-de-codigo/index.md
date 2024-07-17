+++
title = "Pontos a considerar em uma revisão de código"
date = 2019-01-25T00:50:28+00:00
url = "/pontos-a-considerar-em-uma-revisao-de-codigo/"
categories = ["Sem categoria"]
tags = ["software"]
+++



A revisão de código é um processo importante do desenvolvimento de software. Outras pessoas olhando para o código ajudam a identificar falhas que passaram desapercebidas ou melhorias que poderiam ser implementadas.

{{< figure src="code-review.png" alt="Code review do GitHub" caption="Code review do GitHub" >}}

Segue uma lista de itens que considero importantes e me guio ao fazer uma revisão de código:


## Testes

- Todos os testes estão passando? (O ideal é que os testes rodem automaticamente via alguma ferramenta de automação)
- Foram adicionados testes referente ao código modificado?
- A cobertura de testes está satisfatória?


## Simplicidade e Legibilidade

- O código está simples e fácil de entender?
- O código está organizado?


## Alteração nos modelos

Se o projeto possui modelos que se comunicam com um banco de dados:

- Esses modelos foram alterados?
- As modificações não irão quebrar a aplicação quando subir para outros ambientes?
- Foram criadas as migrações necessárias?


## Documentação

- O código alterado modifica algum comportamento que deveria ser documentado?
- Alguma docstring deveria ser alterada?


## Conflitos

- Tem algum conflito do git a ser resolvido?


## Ambientes

- O ambiente que o código está indo necessita alguma modificação?
- Alguma variável deve ser adicionada ao ambiente?


-------------------------------------------------------------------------------

Concorda? Discorda? Tem algo a acrescentar ou remover? Deixe nos comentários.
