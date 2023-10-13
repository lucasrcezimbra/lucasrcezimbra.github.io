---
title: Git
date: 2023-08-15T07:30:00-03:00
aliases:
  - /git
---
- Revert only one file ([Tweet](https://twitter.com/lucasrcezimbra/status/1712070769793253811))
	```bash
	git checkout <commit_hash>~1 -- <path/to/file>
	git commit
	```

- Search for a commit in a deleted branch ([Tweet](https://twitter.com/lucasrcezimbra/status/1712071799280726433))
	```bash
	git reflog --no-abbrev
	```

- Blame history before a commit ([Tweet](https://twitter.com/lucasrcezimbra/status/1712070775069614240))
	```bash
	git blame <commit_hash>^ -- <path/to/file>
	```

- Search for a deleted code ([Tweet](https://twitter.com/lucasrcezimbra/status/1712070777783390608))
	```bash
	git log -c -S'removed_code' <path/to/file> # search for string
	git log -c -G'removed.*code' <path/to/file> # search for regex
	```

- Edit a commit ([Tweet](https://twitter.com/lucasrcezimbra/status/1712070772418912359))
	```bash
	git rebase -i '<commit_hash>^'
	# Change 'pick' to 'edit' in the commit to be edit.
	# Update the files.
	git commit --all --amend --no-edit
	git rebase --continue
	```

- Undo a commit (uncommit) ([Tweet](https://twitter.com/lucasrcezimbra/status/1712070764525195670))
	```bash
	git reset --soft HEAD^
	```

- Add changes to the last commit ([Tweet](https://twitter.com/lucasrcezimbra/status/1712070767100543349))
	```bash
	git commit --amend
	```

- How to find a file that I don't know on which branch is ([Tweet](https://twitter.com/lucasrcezimbra/status/1712070780404834342))
	```shell
	git log --all -- <file-path>
	```

- Better git log format
	```bash
	git config --global alias.lg "log --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset'"
	git lg
	```
	![git lg, a better log](Assets/git-lg.png)

- Add some parts of a file ([Tweet](https://twitter.com/lucasrcezimbra/status/1712070761928908992))	
	```bash
	git add -p
	```

- Pull a branch squashing all remote commits ([Tweet](https://twitter.com/lucasrcezimbra/status/1712070783034699978))
	```bash
	git pull --squash origin <branch>
	```

- Rewrite history updating commits author name and e-mail
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

- Fixing down merge conflicts
  ```bash
  export FROM=<branch>
  export TO=<branch>
  git checkout $TO
  git pull --ff-only origin $TO
  git branch -D downmerge-$FROM-to-$TO
  git checkout -b downmerge-$FROM-to-$TO
  git pull origin $FROM
  # fix conflicts
  git commit
  git push origin downmerge-$FROM-to-$TO
  ```

## Trunk based
- https://trunkbaseddevelopment.com/#one-line-summary
- [Transitioning to Trunk Based Development](https://devcycle.com/blog/transitioning-to-trunk-based-development)

## Versioning
- Conventional Commits - https://www.conventionalcommits.org
	- [GitHub]({{< ref "GitHub" >}}) action: https://github.com/amannn/action-semantic-pull-request
- Semantic Versioning - https://semver.org/