import os
import subprocess
from pathlib import Path

ROOT_DIR = Path(__file__).parent.parent
notes_dir = ROOT_DIR / 'content' / 'anotacoes'

header = f"""\
---
title: "Anotações"
date: 2023-08-15T07:30:00-03:00
---

Anotações sobre tópicos diversos. Algumas em Português outras em Inglês.

Ordenadas de acordo com a data de atualização. Últimas atualizações no topo.
"""


def get_last_commit_date(filepath):
    try:
        output = subprocess.check_output(
            ["git", "log", "-1", "--format=%cd", "--date=iso", "--", filepath],
            cwd=os.path.dirname(os.path.abspath(filepath))
        ).decode('utf-8').strip()
        return output
    except subprocess.CalledProcessError:
        return None


def main():
    pages = []

    for filepath in notes_dir.iterdir():
        if filepath.is_dir() or filepath.name == 'indice.md' or not filepath.name.endswith('.md'):
            continue

        title = filepath.name.replace('.md', '')
        pages.append((f'- [{title}]({{{{< ref "{title}" >}}}})', get_last_commit_date(filepath)))

    lines = [p[0] for p in sorted(pages, key=lambda p: p[1], reverse=True)]

    with open(notes_dir / 'indice.md', 'w') as f:
        f.write('\n'.join([header, *lines]))


if __name__ == '__main__':
    main()
