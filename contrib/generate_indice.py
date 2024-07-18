import subprocess
from datetime import date
from pathlib import Path

ROOT_DIR = Path(__file__).parent.parent
notes_dir = ROOT_DIR / "content" / "anotacoes"

header = f"""\
---
title: "Anotações"
date: 2023-08-15
lastmod: {date.today().strftime("%Y-%m-%d")}
---

Anotações sobre tópicos diversos. Algumas em Português outras em Inglês.

Ordenadas de acordo com a data de atualização. Últimas atualizações no topo.
"""


def get_lastmod_date(filepath):
    with open(filepath) as f:
        for line in f:
            if line.startswith("lastmod:"):
                return line.split(":")[1].strip()


def get_date(filepath):
    with open(filepath) as f:
        for line in f:
            if line.startswith("date:"):
                return line.split(":")[1].strip()


def get_pages(directory):
    for filepath in directory.iterdir():
        if filepath.is_dir():
            yield from get_pages(filepath)

        is_index = filepath.name in ("index.md", "indice.md")
        is_markdown = filepath.name.endswith(".md")
        if is_index or not is_markdown:
            continue

        title = str(filepath.relative_to(notes_dir)).replace(".md", "")

        yield (
            f'- [{title}]({{{{< ref "{title}" >}}}})',
            (get_lastmod_date(filepath), get_date(filepath)),
        )


def main():
    pages_generator = get_pages(notes_dir)
    sorted_pages = sorted(pages_generator, key=lambda p: p[1], reverse=True)
    lines = [p[0] for p in sorted_pages]

    with open(notes_dir / "indice.md", "w") as f:
        f.write("\n".join([header, *lines]))
        f.write("\n")


if __name__ == "__main__":
    main()
