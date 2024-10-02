---
title: Bash
date: 2024-09-30
lastmod: 2024-10-02
---


- command or error
    ```bash
    <command> || {
        echo "Please install <package>"
        exit 1
    }
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
#### Files/dirs
- `[[ -e <file> ]]` file exists
- `[[ -d <dir> ]]` dir exists

#### Strings
- `[[ -z <string> ]]` string is empty
- `[[ -n <string> ]]` string is not empty



## sed
- insert a line at the beginning of a file
    ```bash
    sed -i '1i\<lines>' "<file>"
    ```
- find and sed multiple files
    ```bash
    find "<dir>" -type f -exec sed -i "s|<search>|<replace>|" {} +
    ```
