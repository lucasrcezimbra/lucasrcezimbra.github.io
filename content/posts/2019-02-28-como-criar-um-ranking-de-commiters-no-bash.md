---
title: Como criar um ranking de commiters no bash
author: Lucas Cezimbra
type: post
date: 2019-03-01T01:55:23+00:00
excerpt: g log dev | grep Author | sort | uniq -c | sort -n -r | head -n 20
url: /como-criar-um-ranking-de-commiters-no-bash/
categories:
  - Linux
tags:
  - bash
  - git

---
Resposta curta:

<pre class="wp-block-code"><code>git log | grep Author | sort | uniq -c | sort -n -r | head -n 20</code></pre>

<div class="wp-block-image">
  <figure class="aligncenter"><img loading="lazy" width="630" height="299" src="https://lrcezimbra.com.br/wp-content/uploads/2019/02/git-log-grep-author-sort-uniq-sort-head-1.png" alt="" class="wp-image-557" srcset="https://lucas.tec.br/wp-content/uploads/2019/02/git-log-grep-author-sort-uniq-sort-head-1.png 630w, https://lucas.tec.br/wp-content/uploads/2019/02/git-log-grep-author-sort-uniq-sort-head-1-300x142.png 300w" sizes="(max-width: 630px) 100vw, 630px" /><figcaption>20 maiores commiters do projeto git</figcaption></figure>
</div>

## O que fazem esses comandos?

<!--more-->

### git log 

Mostra o log da branch atual do git

<div class="wp-block-image">
  <figure class="aligncenter"><img loading="lazy" width="390" height="276" src="https://lrcezimbra.com.br/wp-content/uploads/2019/02/git-log-git.png" alt="" class="wp-image-551" srcset="https://lucas.tec.br/wp-content/uploads/2019/02/git-log-git.png 390w, https://lucas.tec.br/wp-content/uploads/2019/02/git-log-git-300x212.png 300w" sizes="(max-width: 390px) 100vw, 390px" /><figcaption>Resultado do git log na branch master do projeto git</figcaption></figure>
</div>

## | (pipe)

Pega o output do comando e joga como entrada do próximo comando. Nesse caso pega a saída do _git log_ e coloca como entrada do _grep_

### grep Author

Procura por &#8220;Author&#8221; no texto que foi dado como entrada. Nesse caso a entrada foi a saída do _git log_

<div class="wp-block-image">
  <figure class="aligncenter"><img loading="lazy" width="399" height="300" src="https://lrcezimbra.com.br/wp-content/uploads/2019/02/git-log-grep-author.png" alt="" class="wp-image-552" srcset="https://lucas.tec.br/wp-content/uploads/2019/02/git-log-grep-author.png 399w, https://lucas.tec.br/wp-content/uploads/2019/02/git-log-grep-author-300x226.png 300w" sizes="(max-width: 399px) 100vw, 399px" /><figcaption>git log | grep Author</figcaption></figure>
</div>

### sort

Ordena as linhas

<div class="wp-block-image">
  <figure class="aligncenter"><img loading="lazy" width="377" height="261" src="https://lrcezimbra.com.br/wp-content/uploads/2019/02/git-log-grep-author-sort.png" alt="" class="wp-image-553" srcset="https://lucas.tec.br/wp-content/uploads/2019/02/git-log-grep-author-sort.png 377w, https://lucas.tec.br/wp-content/uploads/2019/02/git-log-grep-author-sort-300x208.png 300w" sizes="(max-width: 377px) 100vw, 377px" /><figcaption>git log | grep Author | sort</figcaption></figure>
</div>

### uniq -c

<ul style="list-style: None;">
  <li>
    <em>uniq</em> retorna somente as linhas não duplicadas.
  </li>
  <li>
    <em>-c</em> retorna o número de ocorrências de cada linha.
  </li>
</ul>

<div class="wp-block-image">
  <figure class="aligncenter"><img loading="lazy" width="448" height="257" src="https://lrcezimbra.com.br/wp-content/uploads/2019/02/git-log-grep-author-sort-uniq.png" alt="" class="wp-image-554" srcset="https://lucas.tec.br/wp-content/uploads/2019/02/git-log-grep-author-sort-uniq.png 448w, https://lucas.tec.br/wp-content/uploads/2019/02/git-log-grep-author-sort-uniq-300x172.png 300w" sizes="(max-width: 448px) 100vw, 448px" /><figcaption>git log | grep Author | sort | uniq -c</figcaption></figure>
</div>

### sort -n -r

<ul style="list-style: none;">
  <li>
    <em>-n</em> considera a ordenação como numérica.
  </li>
  <li>
    <em>-r</em> reverte a ordenação, de crescente para decrescente.
  </li>
</ul>

## head -n 20

Retorna as primeiras linhas. O _-n_ é o número de linhas que vai ser retornado, nesse caso serão as primeiras 20 linhas.