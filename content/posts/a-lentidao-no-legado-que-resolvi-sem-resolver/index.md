---
title: "A lentidão no legado que resolvi sem resolver"
description: "Como utilizei observabilidade para resolver um problema de performance em um projeto que eu nunca tinha mexido antes"
date: 2025-09-02
lastmod: 2025-09-02
---

Esse post foi originalmente publicado como uma newsletter no Substack. Inscreva-se para receber novos posts diretamente no seu e-mail.

<iframe src="https://lucasrcezimbra.substack.com/embed" width="100%" height="320" style="border:1px solid #EEE; background:white;" frameborder="0" scrolling="no"></iframe>

Adoro investigar e resolver problemas de performance. Na edição de hoje, vou contar como resolvi um N+1 que deixava um sistema praticamente inutilizável.

Detalhe: era um projeto desconhecido, sem ambiente local, nem testes. Com direito a _deploy_ direto em produção via FTP.

Se você lida com código legado ou já precisou decidir entre o ideal e o possível, esse texto pode te trazer bons insights.

* * *

Eu tinha um cliente que atendia há alguns anos. Os serviços só envolviam pequenas alterações de _layout_ no site da empresa. Porém, dessa vez ele me procurou com um problema diferente.

Eles estavam com uma lentidão no sistema que chamavam de Gerenciador. Acessei para verificar e realmente estava bem lento. Levava cerca de 1 minuto para carregar qualquer página.

## Conhecendo o terreno

O sistema era um misto de CMS com CRM. Servia para fazer algumas alterações no site da empresa e também para gerenciar contatos e clientes.

O problema era que eu não conhecia nada do sistema. Não tinha sido desenvolvido por mim, eu nunca tinha nem visto o código. Era escrito em PHP, linguagem que eu não mexia há anos. Usava o framework Zend, que eu só conhecia de nome. E tinha zero versionamento, documentação e testes, pelo menos que eu soubesse.

Tudo o que eu tinha era o acesso à hospedagem, que utilizava o cPanel[¹](#notas-de-rodapé), e ao servidor FTP[²](#notas-de-rodapé).

Outro “problema”, agora pessoal, é que adoro investigar esse tipo de gargalo nas aplicações. Então, lá fui eu, na cara, coragem e vontade de me incomodar e aceitei o projeto.

## Metendo a mão na massa

A primeira coisa que fiz foi baixar todo o código via FTP e colocar em um repositório Git[³](#notas-de-rodapé).

O próximo passo foi tentar rodar o projeto localmente. Não me recordo exatamente como foi essa etapa, mas lembro que eu não consegui rodar localmente. Na época não existiam o _ChatGPT_ e o _Claude Code_ para ajudar.

Então minha próxima tentativa foi adicionar alguma forma de observabilidade ao sistema diretamente em produção. Felizmente, o cPanel tinha uma integração com o New Relic e o plano gratuito desse era o suficiente para o volume de transações do sistema.

Consegui adicionar a ferramenta sem mexer no código, ou seja, menos risco de quebrar algo.

Deixei o New Relic rodando uns dias e voltei para conferir.

## Diagnóstico

O New Relic me mostrou exatamente onde estava o problema. Era um clássico N+1[⁴](#notas-de-rodapé).

Investiguei o código e descobri que havia uma consulta no banco de dados para buscar todas as mensagens não lidas. Logo depois havia um _loop_ : para cada mensagem fazia outra consulta para buscar mais dados.

Esses dados eram utilizados para popular um ícone no cabeçalho do sistema, presente em todas as páginas, com o número de mensagens não lidas.

Enquanto o sistema tinha 10 ou 100 mensagens não lidas, o impacto era pequeno, porém, quando esse número cresceu para milhares, o impacto ficou significativo e o que levava milissegundos passou a levar segundos ou até minutos.

Após entender o problema, eu precisava de uma solução simples que não precisasse de muitas mudanças no código, dada a sua fragilidade.

## Solução

Optei por adicionar um limite ( _LIMIT_ do SQL) na _query_ que buscava as mensagens não lidas no banco de dados. Agora, ao invés de retornar todas, retornava somente 100. O ícone que antes mostrava o número total de mensagens passou a mostrar “99+”.

Você pode estar se perguntando “mas isso não resolve o N+1, resolve?” e a resposta é “não, não resolve”, — até onde sei, pode ser que o N+1 esteja até hoje em produção — mas resolve a lentidão e por consequência o problema do usuário.

Eu poderia ter alterado a _query_ para buscar todos os dados de uma só vez e resolver o N+1? Com certeza, mas o risco de eu quebrar algo no meio do caminho seria muito maior.

O usuário final não está interessado se o código faz 1 ou 100 consultas ao banco de dados. O que importa é a usabilidade e, nesse caso, as 100 consultas não comprometiam o sistema.

Não me entenda mal. Não estou advogando entregar código com problemas de performance, mas cada situação tem seu contexto. Esta foi a melhor solução possível? Não, porém, considerando as limitações, foi boa o suficiente. Lembre-se de que eu estava mexendo em um projeto desconhecido, sem ambiente de desenvolvimento e sem possibilidade de testes.

Solução pronta. Mas e agora? Como faz para validar e implantar?

## Implantação

Eu só tinha uma forma de validar minha solução: testar em produção (evitem fazer isso em casa!).

Escolhi uma hora fora do horário comercial; abri ambas as versões (antes e depois das minhas modificações), caso houvesse algum problema, eu poderia reverter rapidamente; abri o sistema no navegador; e finalmente abri o FTP e enviei os arquivos modificados.

E não é que funcionou?

O sistema estava abrindo em um tempo aceitável. O ícone mostrava “99+” mensagens não lidas.

![](./99.webp)

Comuniquei ao cliente e continuei monitorando com o New Relic por mais alguns dias para garantir que o problema estava resolvido e nenhum outro havia aparecido.

Sucesso!

## O que eu faria diferente?

Olhando para trás, eu faria algumas coisas diferentes.

Código sem testes; desenvolvimento sem conseguir rodar localmente; validação em produção; implantação via FTP. Essas foram práticas, no mínimo, questionáveis.

Não vou dizer que não repetiria algumas das mesmas práticas, se necessário. Em empresas onde software não é a atividade-fim, às vezes, o código rodando em produção é tudo o que se tem.

O que eu com certeza faria diferente é que, atualmente, com mais maturidade, eu me preocuparia muito mais em gerenciar os riscos e principalmente comunicá-los ao cliente. Deixaria clara a situação do projeto e os riscos envolvidos. Ofereceria diferentes opções para lidar com o problema e seus respectivos prós e contras.

Outra coisa que faria diferente é a precificação. Cobrei um valor fixo para resolver o problema, assumindo todo o risco do projeto. Atualmente, eu cobraria um valor por hora, dividindo o risco.

## Aprendizados

Podemos tirar algumas lições dessa história. A primeira é que não existe software que não precise de manutenção. Esse sistema específico rodou tranquilamente por anos até que, de repente, um problema que sempre esteve ali o tornou praticamente inutilizável.

A segunda lição é o valor de uma boa observabilidade. Adicionar o New Relic ao projeto me possibilitou encontrar facilmente o problema em meio a milhares de linhas de um código desconhecido, em uma linguagem e framework com os quais tenho pouca experiência.

A terceira lição é que a melhor solução depende do contexto. Em um mundo ideal, eu teria refatorado a query para eliminar o N+1. No mundo real, com código legado, sem testes e sem ambiente local, adicionar um simples LIMIT foi a decisão mais inteligente.

## Conclusão

No fim, deu tudo certo. Consegui resolver o problema do cliente e o desafio foi bem legal. Gosto bastante de investigar e resolver esse tipo de problema de performance.

E aí, o que achou da solução? Você teria arriscado resolver completamente o N+1 ou também teria ido pelo caminho mais conservador? Já passou por alguma situação similar? [Deixe um comentário no Substack](https://lucasrcezimbra.substack.com/p/a-lentidao-no-legado-que-resolvi/comments) e vamos conversar.

Você está com algum problema desse tipo no seu projeto? Às vezes, alguém vendo o problema de fora pode ajudar. Me mande uma mensagem contando um problema técnico que você está enfrentando e quem sabe a próxima newsletter é contando como eu te ajudei.


* * *

## Notas de Rodapé
¹ **cPanel** é um painel de controle baseado na web usado para gerenciar servidores e hospedagem de sites.

² **FTP** é um protocolo usado para transferir arquivos entre um computador local e um servidor. Ele é bastante usado em hospedagens de sites para enviar ou atualizar arquivos no servidor. Hoje em dia é bem menos do que no passado.

³ **Git** é um sistema de controle de versão que permite rastrear mudanças em arquivos (principalmente de código).

⁴ **N+1** é um problema comum em consultas a banco de dados. Acontece quando o sistema faz 1 consulta principal para buscar uma lista de registros e, depois, para cada item dessa lista, faz mais 1 consulta para buscar dados relacionados. Isso gera muitas queries desnecessárias e pode deixar o sistema lento.
