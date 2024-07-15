---
title: "Raspberry"
date: 2023-08-15T07:30:00-03:00
lastmod: 2023-08-15
---
## Lite OS
- How to connect to a new WiFi network
	```bash
	sudo raspi-config
	# System Options > Wireless LAN
	```

## Docker
### Install
1. Download .deb packages
	```bash
	wget https://download.docker.com/linux/raspbian/dists/bullseye/pool/stable/armhf/containerd.io_1.6.21-1_armhf.deb
	wget https://download.docker.com/linux/raspbian/dists/bullseye/pool/stable/armhf/docker-ce_24.0.2-1~raspbian.11~bullseye_armhf.deb
	wget https://download.docker.com/linux/raspbian/dists/bullseye/pool/stable/armhf/docker-ce-cli_24.0.2-1~raspbian.11~bullseye_armhf.deb
	wget https://download.docker.com/linux/raspbian/dists/bullseye/pool/stable/armhf/docker-buildx-plugin_0.10.5-1~raspbian.11~bullseye_armhf.deb
	wget https://download.docker.com/linux/raspbian/dists/bullseye/pool/stable/armhf/docker-compose-plugin_2.18.1-1~raspbian.11~bullseye_armhf.deb
	```

2. Install
	```bash
	sudo apt update
	sudo apt install iptables-persistent
	sudo dpkg -i containerd.io_1.6.21-1_armhf.deb \
		docker-ce_24.0.2-1~raspbian.11~bullseye_armhf.deb \
		docker-ce-cli_24.0.2-1~raspbian.11~bullseye_armhf.deb \
		docker-buildx-plugin_0.10.5-1~raspbian.11~bullseye_armhf.deb \
		docker-compose-plugin_2.18.1-1~raspbian.11~bullseye_armhf.deb
	```

3. Add user to docker group to use without `sudo`
	```bash
	sudo usermod -aG docker $USER
	```

## Home Assistant
```bash
docker run -d \
	--name <container-name> \
	--privileged \
	--restart=unless-stopped \
	-e TZ=America/Sao_Paulo \
	-v <path-to-config>:/config \
	--network=host \
	ghcr.io/home-assistant/home-assistant:stable
```

## Pi-hole
```bash
docker run -d \
	--name <container-name> \
	--restart=unless-stopped \
	-e TZ=America/Sao_Paulo \
	-v <path>/etc-pihole:/etc/pihole \
	-v <path>/etc-dnsmasq.d:/etc/dnsmasq.d \
	--network=host \
	pihole/pihole:latest
```