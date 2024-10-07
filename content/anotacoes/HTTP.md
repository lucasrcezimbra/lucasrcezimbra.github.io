---
title: "HTTP"
date: 2024-01-24
lastmod: 2024-10-07
---
## Methods

### POST
#### Responses
- 201 (Created) containing a Location header - If one or more resources has been created. Source: [RFC 7231 - Section 4.3.3](https://datatracker.ietf.org/doc/html/rfc7231#section-4.3.3)


## Headers
- Location: URI `https://example.com/path` or relative `/path`. When relative the final value is computed by resolving it against the effective request URI. Source: [RFC 7231 - Section 7.1.2](https://datatracker.ietf.org/doc/html/rfc7231#section-7.1.2)
