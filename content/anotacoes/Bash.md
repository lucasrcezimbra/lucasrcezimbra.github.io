---
title: Bash
date: 2024-09-30
lastmod: 2025-02-10
---

- command or error
    ```bash
    <command> || {
        echo "Please install <package>"
        exit 1
    }
    ```

## arrays
- defining: `fruits=("apple" "banana" "cherry")`
- accessing by index: `echo "${fruits[0]}"`
- accessing all: `echo "${fruits[@]}"`
- length: `echo "${#fruits[@]}"`
- concatenating: `echo "${fruits[*]}"`
- appending: `fruits+=("durian")`
- appending multiple: `fruits+=("durian" "elderberry")`

```bash
fruits=("apple" "banana" "cherry")
echo "${fruits[0]}"
# apple

for f in "${fruits[*]}"; do
    echo "$f"
done
# apple banana cherry

more_fruits=("durian" "elderberry")
fruits+=("${more_fruits[@]}")

for f in "${fruits[@]}"; do
    echo "$f"
done
# apple
# banana
# cherry
# durian
# elderberry
```


## if
```bash
if [[ <condition> ]]; then
    <command>
elif [[ <condition> ]]; then
    <command>
else
    <command>
fi
```

### Conditions
- `[[ ! <condition> ]]` not

#### Files/dirs
- `[[ -e <file> ]]` file exists
- `[[ -d <dir> ]]` dir exists

#### Strings
- `[[ -z <string> ]]` string is empty
- `[[ -n <string> ]]` string is not empty


## Loops
### for
```bash
fruits=("apple" "banana" "cherry")
for f in "${fruits[@]}"; do
    echo "$f"
done
```

## sed
- insert a line at the beginning of a file
    ```bash
    sed -i '1i\<lines>' "<file>"
    ```
- find and sed multiple files
    ```bash
    find "<dir>" -type f -exec sed -i "s|<search>|<replace>|" {} +
    ```


## Substitution
- `${<variable>}` = variable substitution
    * same as `$variable`, but useful when doing string manipulation
    * ```bash
      text="hello"
      echo "${text:1:3}"
      # ell
      ```
- `$(<command>)` = command substitution
    * ```bash
      echo "Today is $(date +%Y-%m-%d)"
      ``
