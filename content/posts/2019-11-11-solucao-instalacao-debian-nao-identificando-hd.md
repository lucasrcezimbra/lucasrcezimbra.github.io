---
title: 'Solução: Instalação Debian não identificando HD'
author: Lucas Cezimbra
type: post
date: 2019-11-12T00:35:07+00:00
excerpt: Como resolver quando a instalação do Debian não está encontrando o HD de um notebook Dell Latitude 5400.
url: /solucao-instalacao-debian-nao-identificando-hd/
categories:
  - Linux
tags:
  - debian
  - linux
  - troubleshooting

---
 

Resposta curta:

<pre class="wp-block-preformatted">BIOS -> System Configuration -> SATA Operation -> mudar "RAID On" para "AHCI".</pre><figure class="wp-block-image">

<img loading="lazy" width="800" height="600" src="https://lrcezimbra.com.br/wp-content/uploads/2019/11/Debian_graphical_installer.png" alt="Debian 9 instalação completa" class="wp-image-658" srcset="https://lucas.tec.br/wp-content/uploads/2019/11/Debian_graphical_installer.png 800w, https://lucas.tec.br/wp-content/uploads/2019/11/Debian_graphical_installer-300x225.png 300w, https://lucas.tec.br/wp-content/uploads/2019/11/Debian_graphical_installer-768x576.png 768w" sizes="(max-width: 800px) 100vw, 800px" /> <figcaption>Debian 9 instalação completa. Fonte: [https://commons.wikimedia.org/wiki/File:Debian\_Graphical\_Installer\_Finish-install\_reboot\_in\_progress_0.png][1]</figcaption></figure> <!--more-->

Estava eu tentando formatar e instalar o Debian ❤ num notebook novo Dell Latitude 5400 que estava com Windows. 

Porém estava tendo um problema que a instalação do Debian não reconhecia o HD da máquina. Primeiramente pensei que fosse devido ao BitLocker que estava instalado, então desativei-o pelo Windows, mas continuou não funcionando.

Depois de muito quebrar a cabeça e pesquisar na internet, encontrei essa [página da Wiki para hardware Dell][2]. E descobri que era necessário alterar a configuração na BIOS para desativar o Intel RAID, assim:

<pre class="wp-block-preformatted">BIOS -> System Configuration -> SATA Operation -> mudar "RAID On" para "AHCI"</pre>

Depois de alterar essa configuração na BIOS o HD foi encontrado normalmente e eu finalmente pude instalar o Debian no notebook.

Fonte: <https://wiki.debian.org/InstallingDebianOn/Dell/Latitude7490>

 [1]: https://commons.wikimedia.org/wiki/File:Debian_Graphical_Installer_Finish-install_reboot_in_progress_0.png
 [2]: https://wiki.debian.org/InstallingDebianOn/Dell