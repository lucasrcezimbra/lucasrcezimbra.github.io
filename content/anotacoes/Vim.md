---
title: "Vim"
date: 2023-08-15
lastmod: 2025-04-07
---
- Profilling startup time
	- https://github.com/dstein64/vim-startuptime
	- `vim` then `:StartupTime`
- mapping keys
	- map = recursive map
	- noremap = non-recursive
	- nnoremap = normal mode non-recursive map
	- https://vim.fandom.com/wiki/Mapping_keys_in_Vim_-_Tutorial_(Part_1)
	- https://stackoverflow.com/questions/3776117/what-is-the-difference-between-the-remap-noremap-nnoremap-and-vnoremap-mapping
- Search and add new line (with indentation)
	```vim
	:g/<pattern>/norm otext of the new line
	```
- Search and delete all lines
	```vim
	:g/<pattern>/d
	```
- Search and delete all lines that do NOT match
	```vim
	:g!/<pattern>/d
	```
 - Search and replace
	```vim
	:s/remove(.*)/\1/
	```

## Neovim
- config .vimrc `~/.config/nvim/init.vim`
- Error: `No "python3" provider found.` #troubleshooting
	- `let g:python3_host_prog = "~/.pyenv/shims/python"`
- Error: `Vim(lua):E5105: Error while calling lua chunk: ..are/nvim/plugged/telescope.nvim/lua/telescope/health.lua:1: module 'health' not found:` #troubleshooting
	- Update neovim from 0.4.4 to 0.8.2 by uninstalling apt version and installing snap version.
- vim-illuminate not highlighting #troubleshooting
	- https://github.com/RRethy/vim-illuminate/issues/154
	- `set termguicolors`
- `:LspInfo` to show the active LSP clients and servers
- `:Mason` to show installed LSPs, DAPs, Linters, and Formatters

### Creating a new plugin
- Tutorials
    - [Neovim Plugin Development](https://lyz-code.github.io/blue-book/vim_plugin_development)
- Templates
    - [ellisonleao/nvim-plugin-template](https://github.com/ellisonleao/nvim-plugin-template)
    - [nvimdev/nvim-plugin-template](https://github.com/nvimdev/nvim-plugin-template)
    - [nvim-lua/nvim-lua-plugin-template](https://github.com/nvim-lua/nvim-lua-plugin-template)
    - [jacobsimpson/nvim-example-python-plugin](https://github.com/jacobsimpson/nvim-example-python-plugin) -
      template for plugins written in Python
    - [FGtatsuro/cookiecutter-neovim-plugin](https://github.com/FGtatsuro/cookiecutter-neovim-plugin) -
      last commit 6 years ago
    - [gennaro-tedesco/boilit](https://github.com/gennaro-tedesco/boilit) -
      didn't like; it's a CLI written in Go, not a template

### Lunarvim
- Error while lunarvim installation `unknown flag 'u'`
	- Uninstall nvim installed using snap
	- https://github.com/LunarVim/LunarVim/issues/3612
#### Plugins
✅ = using
🧪 = testing
❔ = to test
❌ = discarded
🧊 = unmaintained
- ❔[codi.vim](https://github.com/metakirby5/codi.vim)
- ❔[git-blame.nvim](https://github.com/f-person/git-blame.nvim)
- 🧊 [hop](https://github.com/hadronized/hop.nvim) - Neovim motions on speed! - "unmaintained for probably forever"
- 🧪 [leap](https://github.com/ggandor/leap.nvim) - Neovim's answer to the mouse
- 🧊 [lightspeed](https://github.com/ggandor/lightspeed.nvim) - deprecated in favor of leap.nvim
- ❌ [minimap](https://github.com/wfxr/minimap.vim) - blazing fast minimap/scrollbar - I didn't like because it doesn't show the code, only dots
- ❌ [numb](https://github.com/nacro90/numb.nvim) - Peek lines just when you intend - It didn't interest me.
- ✅ [nvim-bqf](https://github.com/kevinhwang91/nvim-bqf) - Better quickfix window in Neovim
- ❔[nvim-spectre](https://github.com/nvim-pack/nvim-spectre)
- 🧪[nvim-treesitter-context](https://github.com/nvim-treesitter/nvim-treesitter-context)
