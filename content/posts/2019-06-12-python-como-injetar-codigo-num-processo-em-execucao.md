---
title: 'Python: Como injetar código num processo em execução'
author: Lucas Cezimbra
type: post
date: 2019-06-13T01:59:02+00:00
excerpt: Como podemos usar o pyrasite e o pyrasite-shell para debugar, injetar código e modificar processos Python que já estão em execução.
url: /python-como-injetar-codigo-num-processo-em-execucao/
categories:
  - Python
tags:
  - debug
  - linux
  - python

---
Resposta curta: [pyrasite][1]

<pre class="wp-block-code"><code>pip install pyrasite
echo 0 | sudo tee /proc/sys/kernel/yama/ptrace_scope
pyrasite &lt;pid> dump_stacks.py
pyrasite-shell &lt;pid></code></pre><figure class="wp-block-image">

<img loading="lazy" width="1024" height="340" src="https://lrcezimbra.com.br/wp-content/uploads/2019/06/pyrasite-1-1024x340.png" alt="Utilizando pyrasite para injetar código num console Python" class="wp-image-622" srcset="https://lucas.tec.br/wp-content/uploads/2019/06/pyrasite-1-1024x340.png 1024w, https://lucas.tec.br/wp-content/uploads/2019/06/pyrasite-1-300x100.png 300w, https://lucas.tec.br/wp-content/uploads/2019/06/pyrasite-1-768x255.png 768w, https://lucas.tec.br/wp-content/uploads/2019/06/pyrasite-1.png 1421w" sizes="(max-width: 1024px) 100vw, 1024px" /> <figcaption>Utilizando pyrasite para injetar código num console Python</figcaption></figure> <!--more-->

## Contexto

Esses dias estava com um bug intermitente que só ocorria no servidor de desenvolvimento, então não estava conseguindo reproduzir localmente.

Tentando descobrir o problema, dei SSH para o servidor e vi que num processo estava justamente acontecendo o que eu queria corrigir.

Então comecei a tentar debugar o código que já estava em execução, sem ter que recomeçar o processo, pois se fizesse isso provavelmente o bug não iria ocorrer.

Foi assim que descobri o <a href="https://pyrasite.readthedocs.io/en/latest/" target="_blank" rel="noreferrer noopener" aria-label=" (abre numa nova aba)">pyrasite</a> e como debugar um processo Python que já está em execução.

## Pyrasite

Com o pyrasite conseguimos injetar código em um processo Python e debugar em tempo de execução.

<p style="text-align:right">
  Fonte: <a href="http://pyrasite.com/" target="_blank" rel="noreferrer noopener" aria-label=" (abre numa nova aba)">http://pyrasite.com/</a>
</p>

#### Instalação

<pre class="wp-block-code"><code>pip install pyrasite</code></pre>

#### Habilitar o trace

No Linux, por uma questão de segurança, o trace é desabilitado por padrão. Então temos que habilitar para conseguir debugar com o pyrasite. 

<pre class="wp-block-code"><code>echo 0 | sudo tee /proc/sys/kernel/yama/ptrace_scope</code></pre>

Recomendo voltar o _ptrace_scope_ para o valor padrão (1) após o debug.

Mais informações sobre o <a href="https://www.kernel.org/doc/Documentation/security/Yama.txt" target="_blank" rel="noreferrer noopener">ptrace_scope na documentação do Kernel</a>.

#### Utilização

Para utilizar o pyrasite chamamos com o ID do Processo (PID) e o script que queremos executar:

<pre class="wp-block-code"><code>pyrasite &lt;pid> my_script.py</code></pre>

A ferramenta já vem com alguns scripts prontos para injetar no processo, são eles:

  * <a rel="noreferrer noopener" aria-label=" (abre numa nova aba)" href="https://github.com/lmacken/pyrasite/blob/master/pyrasite/payloads/dump_stacks.py" target="_blank">dump_stacks.py</a>: _printa_ o stacktrace do código executado
  * <a rel="noreferrer noopener" aria-label=" (abre numa nova aba)" href="https://github.com/lmacken/pyrasite/blob/master/pyrasite/payloads/dump_modules.py" target="_blank">dump_modules.py</a>: _printa_ os módulos carregados (<a rel="noreferrer noopener" aria-label=" (abre numa nova aba)" href="https://docs.python.org/3/library/sys.html?highlight=sys#sys.modules" target="_blank">sys.modules</a>)
  * <a rel="noreferrer noopener" aria-label=" (abre numa nova aba)" href="https://github.com/lmacken/pyrasite/blob/master/pyrasite/payloads/force_garbage_collection.py" target="_blank">force_garbage_collection.py</a>: força a execução do garbage collector
  * <a rel="noreferrer noopener" aria-label=" (abre numa nova aba)" href="https://github.com/lmacken/pyrasite/blob/master/pyrasite/payloads/helloworld.py" target="_blank">helloworld.py</a>: _printa_ Hello World
  * <s><a rel="noreferrer noopener" aria-label=" (abre numa nova aba)" href="https://github.com/lmacken/pyrasite/blob/master/pyrasite/payloads/dump_memory.py" target="_blank">dump_memory.py</a></s>: depende de uma lib que não suporta Python 3

Além desses, também temos <a rel="noreferrer noopener" aria-label=" (abre numa nova aba)" href="https://github.com/lmacken/pyrasite/blob/master/pyrasite/payloads/reverse_python_shell.py" target="_blank">reverse_python_shell.py</a>, <a rel="noreferrer noopener" aria-label=" (abre numa nova aba)" href="https://github.com/lmacken/pyrasite/blob/master/pyrasite/payloads/reverse_shell.py" target="_blank">reverse_shell.py</a>, <a rel="noreferrer noopener" aria-label=" (abre numa nova aba)" href="https://github.com/lmacken/pyrasite/blob/master/pyrasite/payloads/start_callgraph.py" target="_blank">start_callgraph.py</a>, <a href="https://github.com/lmacken/pyrasite/blob/master/pyrasite/payloads/stop_callgraph.py" target="_blank" rel="noreferrer noopener" aria-label=" (abre numa nova aba)">stop_callgraph.py</a>, mas esses eu não consegui usar e não fui muito a fundo.

Para, por exemplo, utilizar o _dump_stacks.py_, rodamos:

<pre class="wp-block-code"><code>pyrasite &lt;pid> dump_stacks.py</code></pre>

#### Shell

Além de executar scripts, também podemos habilitar um shell Python para depurar o que está acontecendo na aplicação. Com o shell conseguimos rodar comandos, acessar variáveis e tudo mais que fazemos num console Python

<pre class="wp-block-code"><code>pyrasite-shell &lt;pid></code></pre>

## Troubleshooting

  1. Rodei o pyrasite e não apareceu nenhum resultado
      * O _output_ do código injetado aparecerá no _stdout_ do processo principal que está recebendo a injeção. Se o seu processo redireciona o _stdout_ para um arquivo, a saída do código injetado também irá para o mesmo arquivo.

 [1]: https://pyrasite.readthedocs.io/en/latest/