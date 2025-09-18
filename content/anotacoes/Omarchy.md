---
title: "Omarchy"
date: 2025-09-13
lastmod: 2025-09-18
---

🔽 = lower priority


## Installation
- [x] Install Omarchy - used 2.11 Offline


## ThinkPad
- Monitor
  - [x] Internal monitor
  - [x] External monitor
  - [ ] 🔽 disable the internal monitor somehow (I just use the external one when I'm in my workstation)
  - 🔽 [ ] auto-enable the internal monitor when external is disconnected
  - https://wiki.archlinux.org/title/Kanshi
  - https://github.com/erans/hyprmon
  - https://github.com/basecamp/omarchy/discussions/994
- [x] Keyboard
  - [x] Brazillian layout - https://github.com/lucasrcezimbra/dotfiles/commit/86784468c22382f63f848014f1fe2e587c2e50da
  - [x] Fix Slash, question mark key (keycode 97) - https://github.com/lucasrcezimbra/dotfiles/commit/94276b4a8496bb756bd3a2deda12eccd392d1c08
- [x] Trackpad
  - [ ] 🔽 Fix upper right button
- [x] Webcam
- [x] Mic
- [ ] 🔽 Fingerprint - In my current setup (Debian + XFCE), I have two
  passwords: one for the disk encryption (longer/harder one, only need to type
  once), another for the user (easier one, type after every screen lock). Given
  Omarchy uses the same password (the longer/harder one) for both, I want to
  configure the fingerprint, so I will have to type the password only once.


## Software
- [x] gitconfig - https://github.com/lucasrcezimbra/dotfiles/commit/2a6b3ac1ab14ed47e28ef8b96499077e88b48cfc
- [x] mise tools - https://github.com/lucasrcezimbra/dotfiles/commit/62912985a59d698cfb7f67faf4cadf264f691237
  - I removed the Omarchy default mise.toml config which was installing Ruby. I hope it doesn't break anything
- [x] Remove non-used webapps (Basecamp, Hey, etc.) - https://github.com/lucasrcezimbra/dotfiles/commit/8e485c9c324d0faf255da5fa4a75c7e2c16d9ff5
- [x] Remove non-used packages (1password, signal, localsend, typora, etc.) - https://github.com/lucasrcezimbra/dotfiles/commit/abd6135b38d547398410cb576cf88da0e4be9f1c
- [x] Install Bitwarden - https://github.com/lucasrcezimbra/dotfiles/commit/4e5a45982888d3434db34fdc57d823a6cc821bb1
- [x] Install tailscale - https://github.com/lucasrcezimbra/dotfiles/commit/4e5a45982888d3434db34fdc57d823a6cc821bb1
- [x] Set Bitwarden as default password - https://github.com/lucasrcezimbra/dotfiles/commit/a4eff39405076fe7502836a43e1f4d8c855770db
- [ ] Zsh + Oh-my-zsh
- [ ] Custom NeoVim configs
- [ ] Wezterm - I can't live without [Quick Select Mode](https://wezterm.org/quickselect.html) anymore
- [ ] Is there a way to hide and unhide a window instead of closing it?
- [x] WhatsApp as default messenger - https://github.com/lucasrcezimbra/dotfiles/commit/e088a6159e91bcc00980d566cc84207c12aae391


## Devices
- [ ] Webcam
- [ ] Mic Blue Yeti
- [ ] Headset bluetooth Edifier
- [ ] Mouse Logitech


## Work
- [x] Google Meet
  - [ ] Share screen
- [ ] Zoom
  - [ ] Share screen


## dotfiles
- [ ] Clean up mise.toml. Most tools are there because Debian didn't have the latest version. Now, with Arch, they can be removed and installed using Arch packages.


## Other
- [ ] In my current setup (Debian + XFCE), I use two users, one for my personal
   stuff and another for work stuff. I used it to separate environment
   variables (API Keys, etc.) and other configs. I need to figure out how to do the same in
