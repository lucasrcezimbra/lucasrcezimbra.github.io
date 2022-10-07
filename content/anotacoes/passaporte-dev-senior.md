---
title: "Passaporte Dev Senior"
date: 2022-10-07T16:38:24-03:00
---


[Curso](https://henriquebastos.net/produtos/passaporte-dev-senior/)

## Opensource
- pitch das ideas
    - cativar/sensibilizar os colegas a participar junto no projeto
    - é um processo de venda

**Coisas erradas**
- não idealizar os mantenedores
    - essas pessoas são sucessos possíveis
    - todos esses caras começaram com um código simples
- Overengineering
    - escopo grande sem ter tempo para executar
    - senão não coloca na rua
- O valor de um projeto Opensource não é o problema q ele resolve e sim a **quantidade de pessoas** que usam o projeto Opensource




## Estratégias para aplicações Multi-Tenent
- https://github.com/henriquebastos/pds-multi-tenant/
- Formas de isolamento
    1. Diferentes instâncias
        1. “single-tentant na nuvem”
        2. economicamente é muito díficil fazer sentido
        3. um codebase pra aplicar em várias instâncias
        4. faz sentido se tiver uma discrepancia muito grande entre consumo de diferentes clientes
    2. Mesma instância e diferentes databases
        1. mais comum
        2. pq em geral o programador não tem um grande conhecimento de banco de dados
    3. Mesmo database e diferentes esquemas
        1. muito especifico para bancos q suportam schemas: Postgres, Oracle, SQL Server...
        2. quais bancos suportam?
    4. Mesmo esquema mas com id de referência
        1. segundo mais comum
        2. simples, mas é muito fácil fazer merda e vazar os dados
        3. com Django é fácil garantir que toda request pro ORM terá tenant_id
- “Tem q ficar fácil. Você não pode fazer uma estratégia de multi-tenant e exigir que o estagiário lembre de colocar o tenant_id na query”
- Sempre começo com a estratégia 4. É muito fácil fazer uma migração de tenant_id (estratégia 4) pra cada um ter um banco de dados
- importante focar na estratégia de otimização do custo de infraestrutura
- [https://www.viget.com/articles/multi-tenancy-in-django/](https://www.viget.com/articles/multi-tenancy-in-django/)
- ao invés de middleware do Django, também pode-se fazer outra aplicação WSGI para pegar o tenant, injetar na thread e depois chamar o Django
    - `application = tenant_wsgi(get_wsgi_application())`
- o tenant tem q ser especifíco por thread, pode-se usar o `[threading.Local()](https://docs.python.org/3/library/threading.html#thread-local-data)`
- fazer um experimento com [threading.Local](https://docs.python.org/3/library/threading.html#thread-local-data)
- fazer experimento em usar o DATABASE_ROUTERS do Django
    - [https://docs.djangoproject.com/en/4.0/ref/settings/#std:setting-DATABASE_ROUTERS](https://docs.djangoproject.com/en/4.0/ref/settings/#std:setting-DATABASE_ROUTERS)
    - [https://docs.djangoproject.com/en/4.0/topics/db/multi-db/](https://docs.djangoproject.com/en/4.0/topics/db/multi-db/)
    - [https://www.amvtek.com/blog/posts/2014/Jun/13/accessing-multiple-postgres-schemas-from-django/](https://www.amvtek.com/blog/posts/2014/Jun/13/accessing-multiple-postgres-schemas-from-django/)
    - [https://stackoverflow.com/questions/65519069/django-routers-with-multiples-schema-in-database](https://stackoverflow.com/questions/65519069/django-routers-with-multiples-schema-in-database)
- Postgres row-level permission
    - [https://www.postgresql.org/docs/current/ddl-rowsecurity.html](https://www.postgresql.org/docs/current/ddl-rowsecurity.html)
    - [https://www.enterprisedb.com/postgres-tutorials/how-implement-column-and-row-level-security-postgresql](https://www.enterprisedb.com/postgres-tutorials/how-implement-column-and-row-level-security-postgresql)
