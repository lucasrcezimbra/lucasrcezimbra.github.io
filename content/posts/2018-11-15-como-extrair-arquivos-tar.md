+++
title = "Como extrair arquivos tar"
date = 2018-11-15T20:02:24+00:00
url = "/como-extrair-arquivos-tar/"
categories = ["Linux"]
tags = ["linux"]
+++

## Como extrair

### **.tar.gz ou .tgz**
```bash
tar -zxvf arquivo.(tar.gz|tgz)
```

### .tar.bz2
```bash
tar -jxvf arquivo.tar.bz2
```

### .tar.xz
```bash
tar -Jxvf arquivo.tar.xz
```


## O que é cada opção
```bash
-x, --extract, --get
    extrai arquivos

-v, --verbose
    verboso

-f, --file
    arquivo

-z, --gzip, --gunzip --ungzip
    para arquivos gzip .gz

-J, --xz
    para arquivos .xz

-j, --bzip2
    para arquivos bzip2 .bz2
```
