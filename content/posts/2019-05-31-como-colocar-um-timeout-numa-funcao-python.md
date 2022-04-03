---
title: Como colocar um timeout numa função Python
author: Lucas Cezimbra
type: post
date: 2019-05-31T03:03:11+00:00
excerpt: Utilizando biblioteca que facilita a definição de um timeout para uma função Python
url: /como-colocar-um-timeout-numa-funcao-python/
categories:
  - Python
tags:
  - python

---
Resposta curta: [timeout-decorator][1]

<pre class="wp-block-code"><code>pip install timeout-decorator</code></pre>

<pre class="wp-block-code"><code>from timeout_decorator import timeout

@timeout(5)  # tempo em segundos
def my_slow_function():
    ...</code></pre>

<!--more-->

## Contexto

Esses dias estava dando manutenção num serviço que lê mensagens de uma fila SQS, processa e apaga a mensagem da fila. Só que estava tendo um problema que às vezes o processamento demorava mais do que o tempo máximo definido no SQS. A mensagem acabava voltando para fila, era lida por outro processo e gerava duplicação desnecessária.

Para resolver esse problema, comecei a pesquisar alguma forma de colocar um timeout numa função Python, então encontrei a lib [timeout-decorator][1] que faz exatamente o que eu precisava.

## Como funciona

A lib usa, por padrão, o signals do Unix para gerar uma exceção e parar de executar a função que foi envolvida pelo decorator.

Também é possível passar um parâmetro use_signals=False, daí será usado multithreading ao invés de signals, mas eu não cheguei a testar dessa forma.

## Exemplo

Instalando:

<pre class="wp-block-code"><code>pip install timeout-decorator</code></pre>

arquivo.py

<pre class="wp-block-code"><code>from time import sleep

from timeout_decorator import timeout


@timeout(5)  # tempo em segundos
def my_slow_function():
    for i in range(1, 10):
        print(i)
        sleep(1)

if __name__ == '__main__':
    my_slow_function()</code></pre>

Resultado:

<pre class="wp-block-code"><code>1
2
3
4
5
Traceback (most recent call last):
...
timeout_decorator.timeout_decorator.TimeoutError: 'Timed Out'
</code></pre>

## Limitações

Por usar o signal do Unix para gerar a exceção, a lib não funciona em ambiente Windows. No projeto que eu a usei, rodamos em ambientes Linux, então não tivemos problemas em produção. Porém, um dos membros da equipe usa Windows para desenvolvimento, então fizemos um wrapper para o decorator que verifica se é Unix, se não for será retornada a função original sem o timeout-decorator.

 [1]: https://github.com/pnpnpn/timeout-decorator
