from pathlib import Path

ROOT_DIR = Path(__file__).parent.parent
notes_dir = ROOT_DIR / 'content' / 'anotacoes'

header = f"""\
---
title: "Anotações"
date: 2023-08-15T07:30:00-03:00
---"""


def main():
    lines = []

    for filepath in notes_dir.iterdir():
        if filepath.is_dir() or filepath.name == 'indice.md':
            continue
        title = filepath.name.replace('.md', '')
        lines.append(f'- [{title}]({{{{< ref "{title}" >}}}})')

    lines.sort(key=lambda l: l.lower())

    with open(notes_dir / 'indice.md', 'w') as f:
        f.write('\n'.join([header, *lines]))


if __name__ == '__main__':
    main()
