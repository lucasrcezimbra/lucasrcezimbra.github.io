+++
title = "Git"
date = 2018-11-30T18:36:15+00:00
aliases = [
    "/anotacoes/git/",
    "/dicas-rapidas-git/",
    "/git/",
]
+++


* Reverter somente um arquivo
```bash
git checkout <commit_hash>~1 -- <path/to/file>
git commit
```

* Encontrar um commit de uma branch deletada
```bash
git reflog --no-abbrev
```


* Usar o blame a partir de um determinado commit
```bash
git blame <commit_hash>^ -- <path/to/file>
```


* Pesquisar um código que já foi removido
```bash
git log -c -S'removed_code' <path/to/file>
```


* Editar um commit específico
```bash
git rebase -i '50defb6^'
# Alterar pick para edit no commit a ser alterado
# Fazer as alterações desejadas
git commit --all --amend --no-edit
git rebase --continue
```
{{< figure src="git-rebase-i.png" alt="git rebase -i" caption="git rebase -i" >}}


* Desfazer o commit mais recente (uncommit)
```bash
git reset --soft HEAD^
```


* Adicionar alterações ao commit mais recente
```bash
git commit --amend
```


* Melhorar o git log
```bash
git config --global alias.lg "log --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset'"
git lg
```
{{< figure src="git-lg.png" alt="git lg, um log melhorado" caption="git lg, um log melhorado" >}}


* Adicionar ao stage apenas pedaços de um arquivo
```bash
git add -p
```
{{< figure src="git-add-p.png" alt="git add -p" caption="git add -p" >}}


* Puxar uma branch juntando todos os comitts num só
```bash
git pull --squash origin <branch>
```


* Reescrever o nome e e-mail do autor no histórico de commits 
```bash
git filter-branch --env-filter '
	OLD_EMAIL="<the old e-mail>"
	CORRECT_NAME="<the new name>"
	CORRECT_EMAIL="<the new e-mail>"

	if [ "$GIT_COMMITTER_EMAIL" = "$OLD_EMAIL" ]
	then
		export GIT_COMMITTER_NAME="$CORRECT_NAME"
		export GIT_COMMITTER_EMAIL="$CORRECT_EMAIL"
	fi
	if [ "$GIT_AUTHOR_EMAIL" = "$OLD_EMAIL" ]
	then
		export GIT_AUTHOR_NAME="$CORRECT_NAME"
		export GIT_AUTHOR_EMAIL="$CORRECT_EMAIL"
	fi' -- origin/HEAD..HEAD
```
