+++
title = "Como criar um ranking de commiters no bash"
date = 2019-03-01T01:55:23+00:00
url = '/como-criar-um-ranking-de-commiters-no-bash/'
categories = ["Linux"]
tags = ["bash", "git"]
+++


Resposta curta:

```bash
git log | grep Author | sort | uniq -c | sort -n -r | head -n 20
```
{{< figure src="git-log-grep-author-sort-uniq-sort-head.png" alt="20 maiores commiters do projeto git" caption="20 maiores commiters do projeto git" >}}


## O que fazem esses comandos?

### git log 
Mostra o log da branch atual do git
{{< figure src="git-log-git.png" alt="Resultado do git log na branch master do projeto git" caption="Resultado do git log na branch master do projeto git" >}}


### | (pipe)
Pega o output do comando e joga como entrada do próximo comando. Nesse caso pega a saída do _git log_ e coloca como entrada do _grep_


### grep Author
Procura por "Author" no texto que foi dado como entrada. Nesse caso a entrada foi a saída do _git log_
{{< figure src="git-log-grep-author.png" alt="git log | grep Author" caption="git log | grep Author" >}}


### sort
Ordena as linhas
{{< figure src="git-log-grep-author-sort.png" alt="git log | grep Author | sort" caption="git log | grep Author | sort" >}}


### uniq -c
- `uniq` retorna somente as linhas não duplicadas.
- `-c` retorna o número de ocorrências de cada linha.
{{< figure src="git-log-grep-author-sort-uniq.png" alt="git log | grep Author | sort | uniq -c" caption="git log | grep Author | sort | uniq -c" >}}


### sort -n -r
- `-n` considera a ordenação como numérica.
- `-r` reverte a ordenação, de crescente para decrescente.
{{< figure src="git-log-grep-author-sort-uniq-sort.png" alt="git log | grep Author | sort | uniq -c | sort -n -r" caption="git log | grep Author | sort | uniq -c | sort -n -r" >}}


## head -n 20
Retorna as primeiras linhas. O `-n` é o número de linhas que vai ser retornado, nesse caso serão as primeiras 20 linhas.
