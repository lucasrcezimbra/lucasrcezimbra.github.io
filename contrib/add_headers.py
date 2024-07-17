from datetime import datetime, timezone, timedelta
from pathlib import Path
from textwrap import dedent

ROOT = Path(__file__).parent.parent
notes_dir = ROOT / "content" / "anotacoes"


def header(title):
    today = datetime.today().strftime("%Y-%m-%d")
    return dedent(
        f"""\
        ---
        title: "{title}"
        date: {today}
        lastmod: {today}
        ---"""
    )


def read(filepath):
    with open(filepath, "r") as f:
        return f.read()


def prepend(filepath, text, original):
    with open(filepath, "w") as f:
        f.write(text + "\n" + original)
        print(filepath)


def main():
    for filepath in notes_dir.iterdir():
        if filepath.is_dir() or not filepath.name.endswith(".md"):
            continue

        title = filepath.name.replace(".md", "")
        original = read(filepath)

        if original.startswith("---"):
            continue

        prepend(filepath, header(title), original)


if __name__ == "__main__":
    main()
