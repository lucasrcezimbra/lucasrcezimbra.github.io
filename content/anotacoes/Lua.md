---
title: Lua
date: 2024-08-30
lastmod: 2024-10-07
aliases:
---

- Homepage: [Lua](https://www.lua.org/)
- Package manager: [LuaRocks](https://luarocks.org/)
- Opinionated code formatter: [StyLua](https://github.com/JohnnyMorganz/StyLua)


## Installing
```sh
sudo apt update
sudo apt install lua5.4 luarocks
```

## Learning
### What is `.busted` file?
Configuration file for Busted framework.


### What is Busted?
[busted](https://lunarmodules.github.io/busted) is a unit testing framework
with a focus on being easy to use


### What is `*.rockspec` file?
[Rockspec format](https://github.com/luarocks/luarocks/wiki/Rockspec-format)
describes a Lua package (or Lua rock) that can be installed using LuaRocks.


### What is a table?
Data structure that represents arrays, dictionaries, and other complex data
structures.

Comparison:

|                   | Lua                                            | Python                                           | JavaScript                      |
| ----------------- | ---------------------------------------------- | ------------------------------------------------ | ------------------------------- |
| Keys              | Any type except `nil` (including other tables) | Immutable types (e.g., strings, numbers, tuples) | Strings or symbols              |
| Values            | Any type                                       | Any type                                         | Any type                        |
| Definition syntax | `local x = {a = 1, b = 2, c = 3}`              | `x = {'a': 1, 'b': 2, 'c': 3}`                   | `const x = {a: 1, b: 2, c: 3};` |
| Set value syntax  | `x.d = 4` or `x['d'] = 4`                      | `x['d'] = 4`                                     | `x.d = 4;` or `x['d'] = 4`      |
| Get value syntax  | `x.d` or `x['d']`                              | `x['d']`                                         | `x.d;` or `x['d']`              |


### What is `local M = {}`?
`local M = {}` is a pattern to create and manage a module in Lua, providing
encapsulation and a clear structure for defining and exporting functionality.

How it works: initializes an empty table `M` that will be used to collect
functions and variables that will be a part of the module's interface. `local`
ensures that `M` is scoped to the module file, preventing it from being
accessed globally. This is good practice to avoid polluting the global
namespace and potential name conflicts.

`M` table is returned at the end of the script.

```lua
-- <moduleName>.lua
local M = {}

function M.sayHello()
 print("Hello, world!")
end

local function privateFunction()
 -- This function is not added to M and remains private to the module
end

return M
```

```lua
-- main.lua
require('<moduleName>').sayHello()
-- Hello, world!
require('<moduleName>').privateFunction()
-- stdin:1: attempt to call a nil value (field 'privateFunction')
-- stack traceback:
--        stdin:1: in main chunk
--        [C]: in ?
```
