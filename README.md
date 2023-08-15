# cezimbra.me

## How to export Obsidian?
```shell
poetry install
poetry run python -m obsidian_to_hugo --obsidian-vault-dir <path_to_obsidian> --hugo-content-dir ./content/anotacoes
poetry run python contrib/add_headers.py
poetry run python contrib/generate_indice.py
```
