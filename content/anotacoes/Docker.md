---
title: "Docker"
date: 2023-08-15
lastmod: 2025-03-06
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
- Docker build --ssh not working #troubleshooting
    - Pass the private key filepath explicitly: `docker build --ssh default=~/.ssh/id_rsa .`
- Pull private image from AWS ECR
    ```shell
    aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin <aws-account>.dkr.ecr.us-east-1.amazonaws.com && docker pull <aws-account>.dkr.ecr.us-east-1.amazonaws.com/<image>:<tag>
    ```
