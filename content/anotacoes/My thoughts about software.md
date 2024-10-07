---
title: My Principles for building software
date: 2024-07-04
lastmod: 2024-10-07
aliases:
---
(Inspiration: [My programming beliefs as of July 2024](https://evanhahn.com/programming-beliefs-as-of-july-2024/) and [My Principles for Building Software](https://kevinmahoney.co.uk/articles/my-principles-for-building-software/))

- "Simplicity is the ultimate sophistication."
- Automated testing - could not be left out, although I believe it is already a consensus in the industry.
- Prefer pure functions and immutable data - improves testability, predictability, etc.
- [Computers are fast](https://computers-are-fast.github.io/) - don't try to optimize to solve a problem you don't have - "premature optimization is the root of all evil" Donald Knuth
- Monolith first and [The Majestic Monolith](https://signalvnoise.com/svn3/the-majestic-monolith/)
- Microservices are about team topologies and scaling systems with different types of bounds
- Do NOT start building your own platform - PaaS will be better built and cheaper than hiring DevOps and building internally.
	- When to build a platform internally?
		- When the cost of building and maintaining is smaller than paying a PaaS
		- Or when you have a specific use case not supported by PaaS (uncommon)
- PostgreSQL is probably the only database you need
- [Choose Boring Technology](https://mcfunley.com/choose-boring-technology)
- All code must serve the business.
- [Cognitive Load is what matters](https://github.com/zakirullin/cognitive-load/blob/main/README.md)
