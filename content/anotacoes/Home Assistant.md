---
title: Home Assistant
date: 2024-06-03T15:27:01-03:00
---
- [Home Assistant](https://www.home-assistant.io/)
- [Awesome HA Blueprints](https://epmatt.github.io/awesome-ha-blueprints/)
- [best-of-hassio](https://github.com/legovaer/best-of-hassio)
- https://github.com/rospogrigio/localtuya
- Dashboards: [Madelena/hass-config-public](https://github.com/Madelena/hass-config-public), [russellventura/HomeAssistant](https://github.com/russellventura/HomeAssistant), [EvisHome/Home-Assistant](https://github.com/EvisHome/Home-Assistant)
- [Community Add-ons](https://community.home-assistant.io/tag/hassio-repository)
- How to hide `Energy` sidebar? Click and hold `Home Assistant` to edit the sidebar
- FireTV events
	- Amazon Prime: `sendevent /dev/input/event4 1 745 1 && sendevent /dev/input/event4 0 0 0 && sendevent /dev/input/event4 1 745 0 && sendevent /dev/input/event4 0 0 0`
	- Disney+: `sendevent /dev/input/event4 1 746 1 && sendevent /dev/input/event4 0 0 0 && sendevent /dev/input/event4 1 746 0 && sendevent /dev/input/event4 0 0 0`
	- Netflix: `sendevent /dev/input/event4 1 744 1 && sendevent /dev/input/event4 0 0 0 && sendevent /dev/input/event4 1 744 0 && sendevent /dev/input/event4 0 0 0`

#### My Add-ons
- [File editor](https://github.com/home-assistant/addons/tree/master/configurator) (Official)
- [Log viewer](https://github.com/hassio-addons/addon-log-viewer) (Community)
- [Terminal & SSH](https://github.com/home-assistant/addons/tree/master/ssh) (Official)
- [Spotify Connect](https://github.com/hassio-addons/addon-spotify-connect) (Community)
#### My Integrations
- [Internet Printing Protocol (IPP)](https://www.home-assistant.io/integrations/ipp)
- (TODO) [Iperf3](https://www.home-assistant.io/integrations/iperf3)
- [Meteorologisk institutt (Met.no)](https://www.home-assistant.io/integrations/met)
- [Mobile App](https://www.home-assistant.io/integrations/mobile_app)
- [Moon](https://www.home-assistant.io/integrations/moon)
- [Nmap Tracker](https://www.home-assistant.io/integrations/nmap_tracker)
- [Open Exchange Rates](https://www.home-assistant.io/integrations/openexchangerates)
- [Raspberry Pi Power Supply Checker](https://www.home-assistant.io/integrations/rpi_power)
- [Speedtest.net](https://www.home-assistant.io/integrations/speedtestdotnet)
- [Sun](https://www.home-assistant.io/integrations/sun)
- [System Monitor](https://www.home-assistant.io/integrations/systemmonitor)
- [UPnP/IGD](https://www.home-assistant.io/integrations/upnp)


https://www.youtube.com/watch?v=FVusYP4fHFM
- Configure general settings: This includes language, time zone, and currency. [1:02]
- Create zones: Zones are used to create automations based on location. For example, you can turn off lights when you leave home. [1:20]
- Enable advanced mode: This will show you all of the options in the UI. [1:38]
- Set a static IP address: This will make sure that your Home Assistant server always has the same IP address. [1:45]
- Enable SSH: This will allow you to access your Home Assistant server in the event of an emergency. [2:12]
- Enable two-factor authentication: This will add an extra layer of security to your server. [2:38]
- Install apps: There are apps available for iOS, Android, Windows, and Mac. [2:55]
- Back up your system: This is important in case you make a mistake or something goes wrong. [3:10]
- Install a file editor: This will allow you to edit configuration files. [3:25]
- Create areas: Areas are used to group your smart home devices and sensors together. [3:40]
- Add media storage from a NAS: This will allow you to playback media and store recordings. [4:00]
- Install HACS: HACS is a community store where you can find hundreds of extra integrations for Home Assistant. [4:18]
- Install Watchman: Watchman is an integration that will check for issues within your Home Assistant environment. [4:35]
- Set up remote access: There are a few different ways to set up remote access, including using Nabucasa, a VPN, or a Cloudflare tunnel. [4:50]
- Enable analytics: This will allow the Home Assistant team to see how many people are using certain integrations, which Hardware configurations are most popular, and which versions people are using. [5:10]