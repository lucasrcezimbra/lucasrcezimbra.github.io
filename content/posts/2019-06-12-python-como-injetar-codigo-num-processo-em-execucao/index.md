+++
title = 'Python: Como injetar código num processo em execução'
date = 2019-06-13T01:59:02+00:00
excerp = 'Como podemos usar o pyrasite e o pyrasite-shell para debugar, injetar código e modificar processos Python que já estão em execução.'
url = '/python-como-injetar-codigo-num-processo-em-execucao/'
categories = ['Python']
tags = ['debug', 'linux', 'python']
+++


Resposta curta: [pyrasite][1]

```bash
pip install pyrasite
echo 0 | sudo tee /proc/sys/kernel/yama/ptrace_scope
pyrasite $PID dump_stacks.py
pyrasite-shell &lt;pid>
```

{{< figure src="pyrasite.png" alt="Utilizando pyrasite para injetar código num console Python" caption="Utilizando pyrasite para injetar código num console Python" >}}


## Contexto
Esses dias estava com um bug intermitente que só ocorria no servidor de desenvolvimento, então não estava conseguindo reproduzir localmente.

Tentando descobrir o problema, dei SSH para o servidor e vi que num processo estava justamente acontecendo o que eu queria corrigir.

Então comecei a tentar debugar o código que já estava em execução, sem ter que recomeçar o processo, pois se fizesse isso provavelmente o bug não iria ocorrer.

Foi assim que descobri o [pyrasite](https://pyrasite.readthedocs.io/en/latest/) e como debugar um processo Python que já está em execução.


## Pyrasite
Com o pyrasite conseguimos injetar código em um processo Python e debugar em tempo de execução.

{{< asciinema 1148 >}}

Fonte: [http://pyrasite.com/](http://pyrasite.com/)


#### Instalação
```bash
pip install pyrasite
```


#### Habilitar o trace
No Linux, por uma questão de segurança, o trace é desabilitado por padrão. Então temos que habilitar para conseguir debugar com o pyrasite.

```bash
echo 0 | sudo tee /proc/sys/kernel/yama/ptrace_scope
```

Recomendo voltar o _ptrace_scope_ para o valor padrão (1) após o debug.

Mais informações sobre o [ptrace_scope na documentação do Kernel](https://www.kernel.org/doc/Documentation/security/Yama.txt).


#### Utilização
Para utilizar o pyrasite chamamos com o ID do Processo (PID) e o script que queremos executar:

```bash
pyrasite $PID my_script.py
```

A ferramenta já vem com alguns scripts prontos para injetar no processo, são eles:

  * [dump_stacks.py](https://github.com/lmacken/pyrasite/blob/master/pyrasite/payloads/dump_stacks.py): _printa_ o stacktrace do código executado
  * [dump_modules.py](https://github.com/lmacken/pyrasite/blob/master/pyrasite/payloads/dump_modules.py): _printa_ os módulos carregados ([sys.modules](https://docs.python.org/3/library/sys.html?highlight=sys#sys.modules))
  * [force_garbage_collection.py](https://github.com/lmacken/pyrasite/blob/master/pyrasite/payloads/force_garbage_collection.py): força a execução do garbage collector
  * [helloworld.py](https://github.com/lmacken/pyrasite/blob/master/pyrasite/payloads/helloworld.py): _printa_ Hello World
  * [~~dump_memory.py~~](https://github.com/lmacken/pyrasite/blob/master/pyrasite/payloads/dump_memory.py): depende de uma lib que não suporta Python 3

Além desses, também temos [reverse_python_shell.py](https://github.com/lmacken/pyrasite/blob/master/pyrasite/payloads/reverse_python_shell.py), [reverse_shell.py](https://github.com/lmacken/pyrasite/blob/master/pyrasite/payloads/reverse_shell.py), [start_callgraph.py](https://github.com/lmacken/pyrasite/blob/master/pyrasite/payloads/start_callgraph.py), [stop_callgraph.py](https://github.com/lmacken/pyrasite/blob/master/pyrasite/payloads/stop_callgraph.py), mas esses eu não consegui usar e não fui muito a fundo.

Para, por exemplo, utilizar o _dump_stacks.py_, rodamos:

```bash
pyrasite $PID dump_stacks.py
```

#### Shell
Além de executar scripts, também podemos habilitar um shell Python para depurar o que está acontecendo na aplicação. Com o shell conseguimos rodar comandos, acessar variáveis e tudo mais que fazemos num console Python

```bash
pyrasite-shell $PID
```


## Troubleshooting
1. Rodei o pyrasite e não apareceu nenhum resultado
    - O _output_ do código injetado aparecerá no _stdout_ do processo principal que está recebendo a injeção. Se o seu processo redireciona o _stdout_ para um arquivo, a saída do código injetado também irá para o mesmo arquivo.


[1]: https://pyrasite.readthedocs.io/en/latest/
