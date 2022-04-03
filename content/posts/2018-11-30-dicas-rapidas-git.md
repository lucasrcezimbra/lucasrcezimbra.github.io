---
title: Dicas rápidas Git
author: Lucas Cezimbra
type: post
date: 2018-11-30T18:36:15+00:00
excerpt: Resumo para teste
url: /dicas-rapidas-git/
categories:
  - Dicas Rápidas
tags:
  - dicas
  - git

---
  * Encontrar um commit de uma branch deletada

<pre class="wp-block-code"><code>git reflog --no-abbrev</code></pre>

  * Usar o blame a partir de um determinado commit

<pre class="wp-block-code"><code>git blame COMMIT_HASH^ -- /path/to/file</code></pre>

  * Pesquisar um código que já foi removido

<pre class="wp-block-code"><code>git log -c -S'removed_code' /path/to/file</code></pre>

  * Editar um commit específico&nbsp;

<pre class="wp-block-code"><code>git rebase -i '50defb6^'
# Alterar pick para edit no commit a ser alterado
# Fazer as alterações desejadas
git commit --all --amend --no-edit
git rebase --continue</code></pre><figure class="wp-block-image">

<img loading="lazy" width="657" height="390" src="https://lrcezimbra.com.br/wp-content/uploads/2018/11/git-rebase-i.png" alt="git rebase -i" class="wp-image-197" srcset="https://lucas.tec.br/wp-content/uploads/2018/11/git-rebase-i.png 657w, https://lucas.tec.br/wp-content/uploads/2018/11/git-rebase-i-300x178.png 300w" sizes="(max-width: 657px) 100vw, 657px" /> <figcaption>git rebase -i</figcaption></figure> 

  * Desfazer o commit mais recente (uncommit)

<pre class="wp-block-code"><code>git reset --soft HEAD^</code></pre>

  * Adicionar alterações ao commit mais recente

<pre class="wp-block-code"><code> git commit --amend</code></pre>

  * Melhorar o git log

<pre class="wp-block-code"><code>$ git config --global alias.lg "log --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)&lt;%an&gt;%Creset'"
$ git lg</code></pre><figure class="wp-block-image">

<img loading="lazy" width="779" height="285" src="https://lrcezimbra.com.br/wp-content/uploads/2018/12/git-lg.png" alt="" class="wp-image-208" srcset="https://lucas.tec.br/wp-content/uploads/2018/12/git-lg.png 779w, https://lucas.tec.br/wp-content/uploads/2018/12/git-lg-300x110.png 300w, https://lucas.tec.br/wp-content/uploads/2018/12/git-lg-768x281.png 768w" sizes="(max-width: 779px) 100vw, 779px" /> <figcaption>git lg, um log melhorado</figcaption></figure> 

  * Adicionar ao stage apenas pedaços de um arquivo

<pre class="wp-block-code"><code>git add -p</code></pre><figure class="wp-block-image">

<img loading="lazy" width="800" height="421" src="https://lrcezimbra.com.br/wp-content/uploads/2018/12/git-add-p.png" alt="" class="wp-image-242" srcset="https://lucas.tec.br/wp-content/uploads/2018/12/git-add-p.png 800w, https://lucas.tec.br/wp-content/uploads/2018/12/git-add-p-300x158.png 300w, https://lucas.tec.br/wp-content/uploads/2018/12/git-add-p-768x404.png 768w" sizes="(max-width: 800px) 100vw, 800px" /> <figcaption>git add -p</figcaption></figure> 

  * Puxar uma branch juntando todos os comitts num só

<pre class="wp-block-code"><code>git pull --squash origin &lt;branch&gt;</code></pre>

  * Reescrever o nome e e-mail do autor no histórico de commits 

<pre class="wp-block-code"><code>git filter-branch --env-filter '
	OLD_EMAIL="MY OLD E-MAIL"
	CORRECT_NAME="MY CORRECT NAME"
	CORRECT_EMAIL="MY CORRECT E-MAIL"

	if &#91; "$GIT_COMMITTER_EMAIL" = "$OLD_EMAIL" ]
	then
		export GIT_COMMITTER_NAME="$CORRECT_NAME"
		export GIT_COMMITTER_EMAIL="$CORRECT_EMAIL"
	fi
	if &#91; "$GIT_AUTHOR_EMAIL" = "$OLD_EMAIL" ]
	then
		export GIT_AUTHOR_NAME="$CORRECT_NAME"
		export GIT_AUTHOR_EMAIL="$CORRECT_EMAIL"
	fi' -- origin/HEAD..HEAD</code></pre>