---
title: Design Patterns by Example
date: 2025-11-18
lastmod: 2025-12-01
---

## SOLID

### S — Single Responsibility Principle

**Bad:**

```python
class CsvExporter:
    def render(self):
        ...

    def upload(self):
        ...
```

**Good:**

```python
class StorageUploader:
    def upload(self):
        ...

class CsvRenderer:
    def render(self):
        ...
```
