---
title: Linux
date: 2023-08-15
lastmod: 2025-03-24
aliases:
  - /anotacoes/linux/
  - /dicas-rapidas-linux/
---
- https://www.youtube.com/watch?v=X8h304Jp9N8 Fedora Silverblue's move to bootable OCI images: Linux will never be the same
- io_uring #async
	- https://en.wikipedia.org/wiki/Io_uring
	- https://unixism.net/loti/what_is_io_uring.html
	- https://kernel.dk/io_uring.pdf
- [Alternatives to]({{< ref "Alternatives to" >}}) Apache Benchmark
- listening for codes sent by the keyboard: `sudo showkey`
- listening for codes sent by the mouse: `sudo apt install evtest && sudo evtest`
- How to transform `curl` to `ab`
	- `<curl>` = `<ab>`
	- `-H` = `-H`: headers
	- `--data-raw <json>` = `-p <file>.json`: request body
	- `--data @file` = `-p <file>.json`: request body
- How to print and redirect the stdout
	```shell
	<command> | tee <filename>
	```
- Converting images from webp (or jpg, png, etc.) to jpg (or webp, png, etc) ([Tweet](https://twitter.com/lucasrcezimbra/status/1718995187878256796))
	```shell
	sudo apt install imagemagick
	convert <file>.webp <file>.jpg
	```
- How to resize images
	```bash
	sudo apt install imagemagick
	```
	```bash
	# Reducing quality
	convert <input> -quality <n>% <output>
	```
	```bash
	# Keeping aspect ratio
	convert <input> -resize <w>x<h> <output>
	```
	```bash
	# Ignoring aspect ratio
	convert <input> -resize <w>x<h>! <output>
	```
- Listar e ordenar diretórios por tamanho
	```bash
	du -sh * | sort -hr
	```
- Logar como outro usuário no terminal
	```bash
	su $OTHER_USER
	```
- Gerar Lorem Ipsum pelo terminal
	```bash
	sudo apt update && sudo apt install libtext-lorem-perl
	lorem -w 96  # 96 words
	lorem -s 8   # 8 sentences
	lorem -p 12  # 12 paragraphs
	```
- Captive Portals - Acessar WiFi que precisa de autenticação pelo browser
	```bash
	ip --oneline route get 1.1.1.1 | awk '{print $3}' | xargs google-chrome
	```
- Formatar pendrive
	```bash
	df -h
	# encontre o pendrive a ser formatado
	sudo umount /dev/sdXX
	sudo mkfs.vfat /dev/sdXX
	```
- Pendrive bootavel
	```bash
	df -h
	# encontre o pendrive
	sudo umount /dev/sdXX
	cp image.iso /dev/sdXX
	sync
	```
- Comando `time` (POSIX)
	- `real` é o tempo total do processo, do início ao fim;
	- `user` é o tempo de CPU gasto em user-mode (fora do Kernel);
	- `sys` é o tempo de CPU gasto no Kernel (ex.: syscalls, alocação de memória, I/O, etc.);
	- `user + sys` é o tempo total de CPU do processo;
- Ler o output de um processo
	```bash
	less /proc/$PID/fd/1  #stdout
	less /proc/$PID/fd/2  #stderr
	```
- Inverter o teclado - Símbolos serem primários e os números secundários (créditos ao [Vítor](https://elmord.org/))
	```bash
	xmodmap -pke | sed -nre 's/keycode  (1[0-9]) = ([^ ]*) ([^ ]*)/keycode \1 = \3 \2/p' | xmodmap -
	```
- How to use SSH as SOCKS5 proxy
	```bash
	ssh -vCND localhost:9999 -i <path_to_id_rsa> <username>@<remote_server>
	```
- How to learn what type (DDR?) memory my computer uses?
	```shell
	sudo dmidecode -t 17
	```
- Profiling zsh startup
	```shell
	# .zshrc
	zmodload zsh/zprof
	...
	zprof
	```
- Run command skipping alias
	```shell
	\<command>
	```
	![](/anotacoes/Assets/linux-shell-skip-alias.png)
## Debian
- How to validate a .desktop file
	```bash
	desktop-file-validate ~/.local/share/applications/<file>.desktop
	```
- How to load .desktop files
	```bash
	update-desktop-database ~/.local/share/applications/
	```
- How to install Apache Benchmark [Package](https://packages.debian.org/sid/apache2-utils)
	```bash
	sudo apt install apache2-utils
	```

## CPU
- How to discover CPU model and version
    ```shell
    lscpu | rg 'Model name'
    ```

## GPU
- How to discover GPU. Options:
	```bash
	lspci | grep VGA
	```
	```bash
	sudo lshw -C display
	```
	```bash
	sudo apt install mesa-utils
	glxinfo | grep "OpenGL vendor\|OpenGL renderer"
	```
	```bash
	sudo apt install inxi
	inxi -G
	```

- How to show Intel GPU usage
	```bash
	sudo apt install intel-gpu-tools
	sudo intel_gpu_top
	```

## Network
- List used ports
	```bash
	sudo netstat -tulpn | grep LISTEN
	```
- How to see the WiFi network name (SSID): `iwgetid`
- How to test speed between two devices in a private network
	1. Install `iperf` on both devices: `sudo apt install iperf3`
	2. Run the server in one device: `iperf -s`
	3. Run the test in the other device: `iperf -c <server-ip>`
- How to discover devices in the same network
	```bash
	sudo apt update && sudo apt install nmap
	sudo nmap -sn 192.168.0.0/24
	```
- How to discover the open ports of a specific device:
	```bash
	sudo nmap -p 1-65535 <ip>
	```

## Terminal Emulators
- [Alacritty](https://github.com/alacritty/alacritty) - #OpenSource
	- No tabs or splits
- [kitty](https://github.com/kovidgoyal/kitty)
- [rio](https://github.com/raphamorim/rio)
- [Warp](https://www.warp.dev/) - closed source
- [WezTerm](https://github.com/wez/wezterm)
	- [vs Alacritty](https://github.com/wez/wezterm/discussions/1769)
## ThinkPad
- Fix keyboard to work `/` (slash) key #troubleshooting - [Source](https://askubuntu.com/questions/184465/slash-in-thinkpad-t420-abnt-keyboard)
	```bash
	sudo dpkg-reconfigure keyboard-configuration
	```

## XFCE4
- Window top part (minimize, maximize, close, etc.) disappeared #troubleshooting : `xfwm4`
- Desktop icons disappeared #troubleshooting: `xfdesktop`
- Dead keys stopped working #troubleshooting: `setxkbmap -option`
- Sending notification
	```shell
	notify-send "<title>" "<message>"
	```
- Customizing Keyboard shortcuts
	```shell
	xfconf-query --channel xfce4-keyboard-shortcuts --property <property> --set <command> --create --type 'string'
	```
	- Examples of `<property>`: `'/commands/custom/<Super>d'`, `'/commands/custom/Print'`, `'/xfwm4/custom/<Primary><Shift><Alt>Left'`
	- Example of `<command>`: `'thunar'`, `'xfce4-screenshooter --fullscreen'`, `'move_window_left_workspace_key'`
	- More examples on https://github.com/lucasrcezimbra/dotfiles/blob/master/install.sh
