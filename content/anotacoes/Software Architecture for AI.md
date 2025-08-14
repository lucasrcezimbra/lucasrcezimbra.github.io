---
title: Software Architecture for AI
date: 2025-08-12
lastmod: 2025-08-14
---

By O'Reilly: [Software Architecture Superstream: Architecture Patterns and Antipatterns for AI - O’Reilly Live Events](https://learning.oreilly.com/live-events/software-architecture-superstream-architecture-patterns-and-antipatterns-for-ai/0642572184209/0642572184193/)

## Emerging Patterns in Agentic AI

by Bharani Subramaniam

### Append only context
- If you change the context after sending to the LLM, it will miss the cache
  and be slow and expensive.

### Constrain tool selection
- Too many tools can be overwhelming for the LLM.
- Constraint tool selection to the specific subset by using a prefix in each
  tool name to help the LLM; e.g. search_*, code_*, etc.


## Mind Your Language Models: An Approach to Architecting Intelligent Systems

by Nischal HP

### Embedding Models
- [MTEB Leaderboard - a Hugging Face Space by mteb](https://huggingface.co/spaces/mteb/leaderboard)

### Text Processing & Chunking
- Why chunk text?
  - Limit on context windows
  - Longer the text, lesser the relevance, vaguer the answer
- How to chunk text?
  - Content and Context are the drivers
    - Semantic
    - Sentence
    - Sliding window
    - Hierarchical
- How to evaluate chunking?
  - Real world queries
  - Evaluation of several models
  - Ranked segments and documents
  - Precision, Recall, nDCG

### Retrieval Strategy
- Improving retrieval
  - Query augmentation
  - Keyword search
  - Vector Search
  - Fusion and Reranking

### Selecting LLM & Grounding
-
