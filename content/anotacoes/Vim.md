---
title: "Vim"
date: 2023-08-15T07:30:00-03:00
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
	:g/search/norm otext of the new line
	```
- Search and delete
	```vim
	:g/pattern/d
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

### Lunarvim
- Error while lunarvim installation `unknown flag 'u'`
	- Uninstall nvim installed using snap
	- https://github.com/LunarVim/LunarVim/issues/3612