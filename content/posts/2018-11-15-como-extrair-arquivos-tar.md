---
title: Como extrair arquivos tar
author: Lucas Cezimbra
type: post
date: 2018-11-15T20:02:24+00:00
url: /como-extrair-arquivos-tar/
categories:
  - Linux
tags:
  - linux

---
## Como extrair

### **.tar.gz ou .tgz**

<pre class="wp-block-code"><code>tar -zxvf arquivo.(tar.gz|tgz)</code></pre>

### .tar.bz2

<pre class="wp-block-code"><code>tar -jxvf arquivo.tar.bz2</code></pre>

### .tar.xz

<pre class="wp-block-code"><code>tar -Jxvf arquivo.tar.xz</code></pre>

## O que é cada opção

<pre class="wp-block-code"><code>-x, --extract, --get
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
    para arquivos bzip2 .bz2</code></pre>