---
title: "Design de API"
date: 2024-03-06
lastmod: 2024-10-07
---
https://www.youtube.com/playlist?list=PLeKXYyZCJHxdD1CXDeEymwI1S9wlcsmYo

- API History
	- Text API - Unix
	- Posix - IEEE 1003
	- DLL
	- COM, DCOM, COM+ (RPC)
	- Database API
	- Web services (SOAP, XML-RPC)
	- REST API (Roy Fielding)
- Focar no problema, não na ferramente (HTTP, REST, etc)
- **Se você começou pensando na modelagem, está pensando errado.**
- Focar no HTTP acaba restringindo em função dele. E se precisar trocar precisa refazer tudo.
- BFF - ao invés de uma API orientada ao domínio do problema - gera acoplamento e torna caro a mudança.
- Hyperlinks são transições de uma máquina de estado.
- Problemas comuns nas APIs
	- API como ORM - vaza lógica para o client que acaba controlando tudo
	- Domain logic - quase como um RPC. O cliente ainda controla.
- Solução: API as Workflow - o client tem que saber muito pouco. A API fornece os próximos passos.
	- Trate o client como uma camada de apresentação. Client interpreta o resultado e decide com base na resposta.
	- A API não controla o client. O client tem uma inteligência, mas não da lógica de negócio.
	- **Hypermedia**
- DX - trate sua API como um produto
	- Não esconda a informação
	- Mínimo input possível
	- API intuitiva
	- Ofereça conveniências de alto nível.
	- Consistência nos nomes, campos, URLs, etc.
	- URLs: plural para coleções
	- Cuidado com formatação de erros.
- Modelo de maturidade de uma API
	0. Nada - URI tunneling
	1. .
	2. .
	3. Hypermedia
- TODO: hypermedia by example - pq user? exemplos de clients usando e não usando.
