+++
date = 2022-09-01T09:42:56-03:00
title = "Como instalar o Zeal no Debian Bullseye"
+++


Resposta curta:

```bash
sudo echo 'deb http://deb.debian.org/debian bullseye-backports main contrib non-free' >> /etc/apt/sources.list
sudo apt update
sudo apt install zeal
```

O [Zeal](https://zealdocs.org/) é um app para Linux, Mac e Windows que serve para acessar diversas documentações offline.

{{< figure src="zeal.png" alt="Zeal is an offline documentation browser for software developers." >}}

Eu estava com problemas para instala-lo no Debian Bullseye, pois não estava disponível no source padrão do Debian. Recebia o seguinte erro:

```bash
$ sudo apt install zeal
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
E: Unable to locate package zeal
```

[Pesquisando nos pacotes do Debian](https://packages.debian.org/search?suite=all&searchon=names&keywords=zeal) vi que o Zeal só estava disponível no source `bullseye-backports`.

Você pode descobrir se esse source no seu sistema com o comando:
```bash
grep bullseye-backports /etc/apt/sources.list
```

Se o seu sistema, assim como o meu, não tiver o `bullseye-backports` nos sources, podemos solucionar seguindo esses passos:

1. Adicione o `bullseye-backports` nos sources

```bash
sudo echo 'deb http://deb.debian.org/debian bullseye-backports main contrib non-free' >> /etc/apt/sources.list
```

2. Atualize a lista de pacotes disponíveis
```bash
sudo apt update
```

3. Instale o Zeal
```bash
sudo apt install zeal
```
