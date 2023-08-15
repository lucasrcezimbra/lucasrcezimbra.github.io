---
title: "Untitled"
date: 2023-08-15T07:30:00-03:00
---
+++
title = "Linux"
date = 2019-02-21T22:21:20+00:00
aliases = [
    "/anotacoes/linux/",
    "/dicas-rapidas-linux/",
]
+++


- [XFCE4](/anotacoes/linux/xfce4/)


## Listar e ordenar diretórios por tamanho
```bash
du -sh * | sort -hr
```


## Logar como outro usuário no terminal
```bash
su $OTHER_USER
```


## Gerar Lorem Ipsum pelo terminal
```bash
sudo apt update && sudo apt install libtext-lorem-perl
lorem -w 96  # 96 words
lorem -s 8   # 8 sentences
lorem -p 12  # 12 paragraphs
```


## Captive Portals
Acessar WiFi que precisa de autenticação pelo browser
```bash
ip --oneline route get 1.1.1.1 | awk '{print $3}' | xargs google-chrome
```


## Formatar pendrive
```bash
df -h 
# encontre o pendrive a ser formatado
sudo umount /dev/sdXX
sudo mkfs.vfat /dev/sdXX
```


## Pendrive bootavel
```bash
df -h
# encontre o pendrive
sudo umount /dev/sdXX
cp image.iso /dev/sdXX
sync
```

## Comando `time` (POSIX)
- `real` é o tempo total do processo, do início ao fim;
- `user` é o tempo de CPU gasto em user-mode (fora do Kernel);
- `sys` é o tempo de CPU gasto no Kernel (ex.: syscalls, alocação de memória, I/O, etc.);
- `user + sys` é o tempo total de CPU do processo;


## Ler o output de um processo
```bash
less /proc/$PID/fd/1  #stdout
less /proc/$PID/fd/2  #stderr
```


## Inverter o teclado
Símbolos serem primários e os números secundários (créditos ao [Vítor](https://elmord.org/))
```bash
xmodmap -pke | sed -nre 's/keycode  (1[0-9]) = ([^ ]*) ([^ ]*)/keycode \1 = \3 \2/p' | xmodmap -
```
