---
title: "Smart Home"
date: 2022-12-27
lastmod: 2024-10-07
---
## Communication
- [Matrix](https://matrix.org/) - An open network for secure, decentralized communication

## DNS
- What Top-Level Domain can I use for my internal domains?
	- `.local` conflicts with Multicast DNS.
	- Unregistered TLD are not recommenced, but these can be used without conflicts (for now): `.intranet.`, `.internal.`, `.private.`, `.corp.`, `.home.`, `.lan.`
	- Reference: [RFC 6762 - Appendix G.  Private DNS Namespaces](https://datatracker.ietf.org/doc/html/rfc6762#appendix-G)

## Hardware
- [Umbrel](https://umbrel.com)
- [ZimaBoard](https://www.zimaspace.com/)

## Hubs
- [Home Assistant]({{< ref "Home Assistant" >}})
- [HomeSeer](https://homeseer.com/)
- [Hubitat](https://hubitat.com/)

## Matter
- [GitHub](https://github.com/project-chip/connectedhomeip/)
- [List of compatible devices](https://www.matterdatabase.com/)
- Developed by [Connectivity Standards Alliance](https://csa-iot.org/)
- Can be used over [Smart Home#Thread]({{< ref "Smart Home#thread" >}}) or Wi-Fi
- What do I need to setup a Matter network?
	- Border Routers (only for Over Thread networks) - bridges devices (running Thread) to your LAN - Alexa or Thread radio + Raspberry PI with [ot-br](https://github.com/openthread/ot-br-posix) can be used.
	- What is Matter controllers? Do I need a controller if I'm using over wi-fi?
- Developer tools
	- [mattertool (chip-tool)](https://github.com/project-chip/connectedhomeip/tree/master/examples/chip-tool) - An example application that uses Matter to send messages to a Matter server.
	- [Google Home Developers - Matter](https://developers.home.google.com/matter)
		- [Matter 101](https://developers.home.google.com/matter/overview)
- References: [The Engineer’s Guide To Matter](https://www.ovyl.io/blog-posts/matter-smart-home), [Wikipedia - Matter (standard)](https://en.wikipedia.org/wiki/Matter_(standard)),  [Silicon Labs Matter User’s Guide](https://siliconlabs.github.io/matter/latest/OVERVIEW.html), [Ars Technica - IoT harmony? What Matter and Thread really mean for your smart home](https://arstechnica.com/gadgets/2022/10/matter-and-thread-could-fix-smart-home-compatibility-but-dont-get-excited-yet/), [Matter SDK documentation page](https://project-chip.github.io/connectedhomeip-doc/index.html)


## OS
- [CasaOS](https://github.com/IceWhaleTech/CasaOS)
- [UmbrelOS](https://umbrel.com/#umbrelos)

## Storage
- [PhotoPrism](https://www.photoprism.app/) - AI-Powered Photos App for the Decentralized Web

## Thread
- Developed by [Thread Group](https://threadgroup.org/)
- [OpenThread](https://openthread.io/) - #OpenSource implementation by Google - [GitHub](https://github.com/openthread/openthread)
- References: [Wikipedia - Thread (network protocol)](https://en.wikipedia.org/wiki/Thread_(network_protocol)), [Connectivity Standards Alliance](https://csa-iot.org/)

## Zigbee
- A low-power, low-data-rate, and close proximity (i.e., personal area) wireless ad hoc network. It's decentralized type of wireless network that doesn't rely on a pre-existing infrastructure, such as routers or wireless access points. Each node participates in routing by forwarding data for other nodes.
- Developed by [Connectivity Standards Alliance](https://csa-iot.org/)
- [Database of compatible devices](https://zigbee.blakadder.com/)
- vs Wi-fi: consume less battery; mesh network (some (check w/ manufacturer) devices are repeaters).
- References: [Wikipedia - Zigbee](https://en.wikipedia.org/wiki/Zigbee), [Wikipedia - Wireless ad hoc network](https://en.wikipedia.org/wiki/Wireless_ad_hoc_network)
