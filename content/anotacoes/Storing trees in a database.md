---
title: Storing trees in a database
date: 2024-10-08
lastmod: 2024-10-08
---

## Q&A
### ltree - What happens if I query `.*foo.*` but there are 2 "foo"s in two diferent trees in my databases?

## References
### Modeling Hierarchical Tree Data in PostgreSQL
- [Modeling Hierarchical Tree Data in PostgreSQL](https://leonardqmarcq.com/posts/modeling-hierarchical-tree-data)
- example: hierarchy of countries, states and cities
- Approach #1: Static tree schema
    * example: 3 tables: country, state, city
    * constraints: fixed tree-depth; ancestors/descendants queries become
      more complex proportionally to the depth of the trees;
    * pros: simple; easy to enforce integrity constraints;
    * cons: lack of flexibility;
    * better to model as a actual tree if you want to use tree operations
      and traversal queries
- Approach #2: Dynamic tree with Recursive Common Table Expression (CTE)
    * example: 1 table with a parent column
    * pros: flexibility; arbitrary tree-depth; easy to do traversal queries
    * cons: medium complexity queries; may not work in another RDBMS
- Approach #3: Label tree (ltree) materialized path
    * example: 1 table with a path column type
      [`ltree`](https://www.postgresql.org/docs/9.1/ltree.html)
    * constraints: assumes that there is only one path from the root to any
      given node; the application must build the path.
    * pros: flexible; arbitrary tree-depth; the simplest queries (may not
      make diference when using ORMs)
    * cons: may not work in another RDBMS; needs to every node in the
      subtree whenever one ancestor changes

### Do's and Don'ts of Storing Large Trees in PostgreSQL
- [Do's and Don'ts of Storing Large Trees in PostgreSQL](https://leonardqmarcq.com/posts/dos-and-donts-of-modeling-hierarchical-trees-in-postgres)
1. The parent_id column
    * (Almost) always use; even when using ltree
    * pros: enforce the tree structure; can be used to rebuild the materialized
      path if becomes inconsistent; simple to move subtrees; easy concurrent
      updates
    * cons: the tree needs to be written in a specific order respecting
      the relationships; inserting by path is harder
    * You must have a unique constraint on the column representing the path name
        * example: if you have two nodes with a name set to be `"backup"`, then you
          cannot have a path based on the name, like `/system/backup` because it
          would map to two different nodes.
        * Option 1: store the full path
            * example: `path` column with a unique constraint containing the full
              path from the root to the node
            * cons: need to update the `path` column on every move operation;
        * Option 2: store the path component
            * example: `name` column with a unique constraint together with the
              parent_id
2. Materialized paths
    * best use cases: tree rarely changes and you need to do traversal queries;
      the source of truth for the tree is external, and you are only reading
      and replicating.
    * avoid: when you have a lot of writes/levels/nodes in the tree; when the
      nodes chage position frequently.
    * pros: simple query;
    * cons: hard to maintain consistency, you need to update the ltree in the
      whole tree everytime you move/rename a node in a transaction; write
      performance
