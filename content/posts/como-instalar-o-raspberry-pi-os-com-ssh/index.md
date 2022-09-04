+++ 
date = 2022-09-04T17:54:17-03:00
title = "Como instalar o Raspberry Pi OS com SSH"
+++

Resposta curta:

```bash
wget https://downloads.raspberrypi.org/imager/imager_latest_amd64.deb
sudo dpkg -i imager_latest_amd64.deb
rpi-imager
```

```bash
# no Raspberry, após criar o usuário
sudo su -
apt update
apt upgrade
systemctl enable ssh
systemctl restart ssh
raspi-config  # 1 > S5 > B1
```

## Montando Cartão SD bootável

1. Baixe o Raspberry Pi Imager: https://www.raspberrypi.com/software/
1. Instale o Imager
    ```bash
    sudo dpkg -i imager_latest_amd64.deb
    ```

    - se tiver algum problema na instalação rode
        ```bash
        sudo apt --fix-broken install 
        sudo dpkg -i imager_latest_amd64.deb
        ```
1. Insira o cartão SD na máquina;
    - esse cartão SD será formatado, se necessário faça backup;
1. Abra o Imager
    ```bash
    rpi-imager
    ```
1. Escolha o sistema operacional que deseja instalar;
    - No meu caso, foi o `Raspberry Pi OS Lite (64-bit)`;
    - Para verificar qual SO sua Raspberry suporta, acesse: https://www.raspberrypi.com/software/operating-systems/
1. Escolha o cartão SD;
1. "Write"
    {{< figure src="rpi-imager.png" alt="Raspberry Pi Imager" caption="Raspberry Pi Imager" >}}
1. Após finalizar, remova o cartão SD da máquina.


## Setup inicial do Raspberry Pi OS
1. Insira o cartão SD no Raspberry;
1. Conecte teclado, monitor, internet e energia;
1. Após ligar, será necessário criar um usuário e senha;
1. Atualize os pacotes
    ```bash
    sudo apt update
    sudo apt upgrade
    ```

### Desabilitando o Auto Login (segurança)
1. Abra a ferramenta de configuração do Raspberry
    ```bash
    sudo raspi-config
    ```
1. Abra a opção 1 `System Options`
1. Abra a opção S5 `Boot / Autologin`
1. Seleciona a opção B1 `Console` `Text console, requiring user to login`
    {{< figure src="raspi-config-autologin.png" alt="Desabilitando o Auto Login no Raspberry" caption="Desabilitando o Auto Login no Raspberry" >}}



### Habilitando acesso SSH
1. Inicie o servidor SSH
    ```bash
    sudo su -
    systemctl enable ssh
    systemctl restart ssh
    ```
