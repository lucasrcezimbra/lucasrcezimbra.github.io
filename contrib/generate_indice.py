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
    cmd = ["git", "log", "-1", "--format=%aI", "--date=iso", "--", filepath]
    output = subprocess.check_output(cmd).decode('utf-8').strip()
    return output


def get_first_commit_date(filepath):
    cmd = ["git", "log", "--diff-filter=A", "--follow", "--format=%aI", "-1", "--", filepath]
    output = subprocess.check_output(cmd).decode('utf-8').strip()
    return output


def get_pages(directory):
    for filepath in directory.iterdir():
        if filepath.is_dir():
            yield from get_pages(filepath)

        if filepath.name in ('index.md', 'indice.md') or not filepath.name.endswith('.md'):
            continue

        title = str(filepath.relative_to(notes_dir)).replace('.md', '')

        yield (
            f'- [{title}]({{{{< ref "{title}" >}}}})',
            (get_last_commit_date(filepath), get_first_commit_date(filepath))
        )


def main():
    pages_generator = get_pages(notes_dir)
    sorted_pages = sorted(pages_generator, key=lambda p: p[1], reverse=True)
    lines = [p[0] for p in sorted_pages]

    with open(notes_dir / 'indice.md', 'w') as f:
        f.write('\n'.join([header, *lines]))


if __name__ == '__main__':
    main()
