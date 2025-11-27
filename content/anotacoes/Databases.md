---
title: Databases
date: 2023-08-15
lastmod: 2025-11-27
aliases:
  - /anotacoes/vector-database/
---

- ## PostgreSQL
  - [PostgreSQL]({{< ref "PostgreSQL" >}})

- ## SQLite
  - [Quirks, Caveats, and Gotchas In SQLite](https://sqlite.org/quirks.html)
  - [Appropriate Uses For SQLite](https://sqlite.org/whentouse.html)
  - [libSQL](https://github.com/tursodatabase/libsql)- fork of SQLite that is both Open Source, and Open Contributions.

- ## Learnings from migrating from PostgreSQL to SQLite.
  - ### Ordering nulls
    - On PostgreSQL, date columns ordered DESC returns nulls first and ASC returns
      nulls last;
    - On SQLite, it's the opposite: ASC returns nulls first and DESC returns nulls
      last. This can be changed using the "NULLS LAST" or "NULLS FIRST" syntax.
      ["SQLite considers NULL values to be smaller than any other values for sorting purposes."](https://www.sqlite.org/lang_select.html#orderby).
  - ### Ordering unicode chars
    - SQLite doesn't support ordering unicode chars by default (documented
      [here](https://sqlite.org/quirks.html#sqlite_does_not_do_full_unicode_case_folding_by_default)).

- ## Vector
  - [What is a Vector Database?](https://www.pinecone.io/learn/vector-database/) by Pinecone
  - Why Use a Vector Database?
    1. Semantic search;
    2. Similarity search for images, audio, video, JSON, and other forms of unstructured data;
    3. Ranking and recommendation engines;
    4. Deduplication and record matching;
    5. Anomaly detection
  - ### Options
    - [Amazon OpenSearch](https://aws.amazon.com/opensearch-service/serverless-vector-engine/)
    - [Chroma](https://www.trychroma.com/) - SQLite of vector databases
    - [Elasticsearch Vector Search](https://www.elastic.co/what-is/vector-search)
    - [GraphDB](https://graphdb.ontotext.com/)
    - [Kùzu](https://kuzudb.com/)
    - [LanceDB](https://lancedb.com/) - [Repo](https://github.com/lancedb/lancedb)
    - [milvus](https://milvus.io/)
    - [pgvector](https://github.com/pgvector/pgvector) - [Python]({{< ref "Python" >}}) [support](https://github.com/pgvector/pgvector-python)
    - [Pinecone](https://www.pinecone.io/)
    - [Qdrant](https://qdrant.tech/) - vector similarity search engine and
      database - [Python]({{< ref "Python" >}})
      [client](https://github.com/qdrant/qdrant-client) - used by
      [OpenAI](https://twitter.com/altryne/status/1721989500291989585) and
      [xAI](https://twitter.com/qdrant_engine/status/1721097971830260030)
      #OpenSource
    - [typesense](https://typesense.org/) - #OpenSource
    - [VectorDB](https://github.com/vectordb-io/vectordb)
    - [Weaviate](https://weaviate.io/)
