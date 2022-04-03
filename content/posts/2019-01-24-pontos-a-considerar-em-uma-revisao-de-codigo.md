---
title: Pontos a considerar em uma revisão de código
author: Lucas Cezimbra
type: post
date: 2019-01-25T00:50:28+00:00
excerpt: 'A revisão de código é um processo importante do desenvolvimento de software. Outras pessoas olhando para o código ajudam a identificar falhas que passaram desapercebidas ou melhorias que poderiam ser implementadas. '
url: /pontos-a-considerar-em-uma-revisao-de-codigo/
categories:
  - Sem categoria
tags:
  - software

---
<div class="wp-block-image">
  <figure class="aligncenter"><img loading="lazy" width="370" height="195" src="https://lrcezimbra.com.br/wp-content/uploads/2018/12/code-review.png" alt="" class="wp-image-264" srcset="https://lucas.tec.br/wp-content/uploads/2018/12/code-review.png 370w, https://lucas.tec.br/wp-content/uploads/2018/12/code-review-300x158.png 300w" sizes="(max-width: 370px) 100vw, 370px" /><figcaption>Code review do GitHub</figcaption></figure>
</div>

A revisão de código é um processo importante do desenvolvimento de software. Outras pessoas olhando para o código ajudam a identificar falhas que passaram desapercebidas ou melhorias que poderiam ser implementadas. 

Segue uma lista de itens que considero importantes e me guio ao fazer uma revisão de código:

<!--more-->

## Testes

  *<input type="checkbox" /> Todos os testes estão passando? (O ideal é que os testes rodem automaticamente via alguma ferramenta de automação)
  *<input type="checkbox" /> Foram adicionados testes referente ao código modificado?
  *<input type="checkbox" /> A cobertura de testes está satisfatória?

## Simplicidade e Legibilidade

  *<input type="checkbox" /> O código está simples e fácil de entender?
  *<input type="checkbox" /> O código está organizado?

## Alteração nos modelos

Se o projeto possui modelos que se comunicam com um banco de dados:

  *<input type="checkbox" /> Esses modelos foram alterados?
  *<input type="checkbox" /> As modificações não irão quebrar a aplicação quando subir para outros ambientes?
  *<input type="checkbox" /> Foram criadas as migrações necessárias?

## Documentação

  *<input type="checkbox" /> O código alterado modifica algum comportamento que deveria ser documentado?
  *<input type="checkbox" /> Alguma docstring deveria ser alterada?

## Conflitos

  *<input type="checkbox" /> Tem algum conflito do git a ser resolvido?

## Ambientes

  *<input type="checkbox" /> O ambiente que o código está indo necessita alguma modificação?
  *<input type="checkbox" /> Alguma variável deve ser adicionada ao ambiente?

<hr class="wp-block-separator" />

Concorda? Discorda? Tem algo a acrescentar ou remover? Deixe nos comentários.