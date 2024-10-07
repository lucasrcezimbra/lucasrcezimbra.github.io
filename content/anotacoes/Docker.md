---
title: "Docker"
date: 2023-08-15
lastmod: 2024-10-07
---
- Error: `Bind for 0.0.0.0:8080 failed: port is already allocated` #troubleshooting
	- `sudo netstat -tulpn | grep LISTEN`
	- `sudo service docker restart`
- Prune - [Linux]({{< ref "Linux" >}})
	- `docker system prune && docker image prune`
- Remove all images - [Linux]({{< ref "Linux" >}})
	- `docker images -q | xargs docker rmi`
- Error: `failed to start daemon: Error initializing network controller: error obtaining controller instance: failed to create NAT` #troubleshooting
	- `sudo shutdown -r now`
	- If reboot doesn't work: `sudo update-alternatives --set iptables /usr/sbin/iptables-legacy && sudo update-alternatives --set ip6tables /usr/sbin/ip6tables-legacy`
- [export command](https://docs.docker.com/engine/reference/commandline/export/) - export the contents of the _underlying_ directory, not the contents of the volume.
