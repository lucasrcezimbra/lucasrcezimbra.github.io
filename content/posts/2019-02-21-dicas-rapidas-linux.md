---
title: Dicas rápidas Linux
author: Lucas Cezimbra
type: post
date: 2019-02-21T22:21:20+00:00
excerpt: Tópicos e dicas rápicas para utilizar no Linux
url: /dicas-rapidas-linux/
categories:
  - Linux
tags:
  - bash
  - dicas
  - linux

---
  * Gerar Lorem Ipsum pelo terminal

<pre class="wp-block-code"><code>sudo apt update && sudo apt install libtext-lorem-perl
lorem -w 96  # 96 words
lorem -s 8   # 8 sentences
lorem -p 12  # 12 paragraphs</code></pre>

  * Formatar pendrive

<pre class="wp-block-code"><code>df -h 
# encontre o pendrive a ser formatado
sudo umount /dev/sdXX
sudo mkfs.vfat /dev/sdXX</code></pre>

  * Pendrive bootavel

<pre class="wp-block-code"><code>df -h
# encontre o pendrive
sudo umount /dev/sdXX
cp image.iso /dev/sdXX
sync</code></pre>

  * Acessar WiFi que precisa de autenticação pelo browser (Captive Portals)

<pre class="wp-block-code"><code>ip --oneline route get 1.1.1.1 | awk '{print $3}' | xargs google-chrome</code></pre>

  * Ler o output de um processo

<pre class="wp-block-code"><code>less /proc/&lt;pid&gt;/fd/1  #stdout
less /proc/&lt;pid&gt;/fd/2  #stderr</code></pre>

  * Inverter o teclado para os símbolos serem primários e os números secundários (créditos ao <a href="https://elmord.org/" target="_blank" rel="noreferrer noopener">Vítor</a>)

<pre class="wp-block-code"><code>xmodmap -pke | sed -nre 's/keycode  (1&#91;0-9]) = (&#91;^ ]*) (&#91;^ ]*)/keycode \1 = \3 \2/p' | xmodmap - </code></pre>