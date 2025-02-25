---
title: My principles for building software
date: 2024-07-04
lastmod: 2025-02-25
aliases:
  - /anotacoes/manifest-front-end/
  - /anotacoes/manifest-platforms/
  - /anotacoes/my-thoughts-about-software/
---

## Context
(Inspirations: [My programming beliefs as of July 2024](https://evanhahn.com/programming-beliefs-as-of-july-2024/) and [My Principles for Building Software](https://kevinmahoney.co.uk/articles/my-principles-for-building-software/))

Here are my personal thoughts about building software. I'm constantly updating
and improving this page.


## Table of Contents
- [Principles](#principles)
    - [Maintainability](#maintainability)
    - [Simplicity](#simplicity)
    - [Automated testing](#automated-testing)
    - [Scalability/Performance](#scalabilityperformance)
    - [Monolith first. Microservices need justification.](#monolith-first-microservices-need-justification)
    - [HTML first. SPAs need justification.](#html-first-spas-need-justification)
    - [SQL first. Others need justification.](#sql-first-others-need-justification)
    - [Business first](#business-first)
    - [PaaS first. Building a platform needs justification.](#paas-first-building-a-platform-needs-justification)
    - [Devs Ownership](#devs-ownership)
- [To think/write about](#to-thinkwrite-about)
- [References](#references)


## Principles
### Maintainability
- People (developers) time are more expensive than machine time (at least until
  the AGI).

### Simplicity
- "Simplicity is the ultimate sophistication."

### Automated testing
- It's a must, although I believe it is already a consensus in the industry.

### Scalability/Performance
- [Computers are fast](https://computers-are-fast.github.io/)
- Don't try to optimize to solve a problem you don't have
- "Premature optimization is the root of all evil" Donald Knuth
- Data-driven optimizations. You need observability to detect bottlenecks and
  optimize based on it.
- Optimize based on the number of users.
- Optimizations Should be driven by the SLAs/SLOs defined by the business.
- People (developers) time are more expensive than machine time (at least until
  the AGI).
- You system is probably IO bound. If so, you don't need a CPU/memory optimized
  languages.

### Monolith first. Microservices need justification.
- Microservices add way too much complexity.
- If your team doesn't know how to separate concerns in a monolith, they won't
  know how to do it in microservices. Unless you are centralizing the
  separation decisions, but in this case you are not solving the problem.
- Microservices are about team topologies and scaling systems with different types of bounds
- References
    - https://x.com/milan_milanovic/status/1722252645438484810?s=46
    - [The Majestic Monolith](https://signalvnoise.com/svn3/the-majestic-monolith/)
    - Meme: [Microservices](https://youtu.be/y8OnoxKotPQ?si=gB0Gpt8Pwey-Mt9Z) orchestration complexity
    - [How to recover from microservices](https://world.hey.com/dhh/how-to-recover-from-microservices-ce3803cc)
    - [MonolithFirst](https://martinfowler.com/bliki/MonolithFirst.html)
    - [Monoliths are good enough for almost everything. Microservices need justification.](https://twitter.com/milan_milanovic/status/1722252645438484810)
    - [Scaling up the Prime Video audio/video monitoring service and reducing costs by 90%](https://www.primevideotech.com/video-streaming/scaling-up-the-prime-video-audio-video-monitoring-service-and-reducing-costs-by-90)
        - [Amazon Prime Video’s Microservices Move Doesn’t Lead to a Monolith after All](https://thenewstack.io/amazon-prime-videos-microservices-move-doesnt-lead-to-a-monolith-after-all/)
    - [Stack Overflow Architecture](https://stackexchange.com/performance)
    - [The Majestic Monolith](https://m.signalvnoise.com/the-majestic-monolith/)
    - [What Powers Instagram: Hundreds of Instances, Dozens of Technologies](https://instagram-engineering.com/what-powers-instagram-hundreds-of-instances-dozens-of-technologies-adf2e22da2ad)
    - [Why you should build a (modular) monolith first?](https://twitter.com/milan_milanovic/status/1722573693795086378)

### HTML first. SPAs need justification.
- Backend should be the only source of application state.
- References
    - [HTML First](https://html-first.com)

### SQL first. Others need justification.
- SQLite or PostgreSQL is probably all you need.

### Business first
- All code must serve the business.
- Technical decisions must be driven by the business.

### PaaS first. Building a platform needs justification.
- Do NOT start building your own platform - PaaS will be better built and
  cheaper than hiring DevOps and building internally.
- People (Ops) time are more expensive than machine time (at least until the
  AGI).
- When to build a platform internally?
    - When the cost of building and maintaining is smaller than paying a PaaS
    - Or when you have a specific use case not supported by PaaS (uncommon)
- References
    > 🗣️ “Platform engineering will ultimately solve the central problem
    > of cooperation between software developers and operators.”
    >
    > No it won't. It will make "DevOps/Infrastructure" teams reinventing the
    > wheel by building their own Heroku version.
    >
    > https://x.com/andrealmar_/status/1721962350754836859
    - Meme "Using Kubernetes to deploy your uncle's bakery website":
      https://x.com/o_gabsferreira/status/1242140290443546625?s=46

### Devs Ownership
- Dev team must own the application from end to end (code, infra, testing,
  deployment, monitoring, etc.)
- Devs should work with stakeholders to gather requirements. Only juniors can
  afford to want well-defined tasks. It's the job of senior devs to talk to
  stakeholders, understand requirements, prioritize, define scope, etc.


## To think/write about
- Containers are for external services. The application should run locally.
- Prefer pure functions and immutable data - improves testability, predictability, etc.
- Security
- Documentation
- No build
- Solve things by building it, not only thinking about. You won't be able to
  solve everything in your mind; Some stuff needs to be be built to show up the
  issues; You should focus on easy changing, not doing it right the at first
  time.
- Typing dynamic languages is a mistake
    * TODO To read - https://techblog.bozho.net/static-typing-is-not-for-type-checking/
    * TODO To read - https://docs.google.com/document/d/1aXs1tpwzPjW9MdsG5dI7clNFyYayFBkcXwRDo-qvbIk/preview?tab=t.0
    * TODO To read - https://danluu.com/empirical-pl/


## References
- [The Twelve-Factor App](https://12factor.net)
- [Computers are fast!](https://computers-are-fast.github.io)
- [Radical Simplicity in Technology](https://www.radicalsimpli.city)
- [ONCE #1 is entirely #nobuild for the front-end](https://world.hey.com/dhh/once-1-is-entirely-nobuild-for-the-front-end-ce56f6d7)
- [htmx ~ Locality of Behaviour (LoB)](https://htmx.org/essays/locality-of-behaviour)
- [Choose Boring Technology](https://mcfunley.com/choose-boring-technology)
- [Cognitive Load is what matters](https://github.com/zakirullin/cognitive-load/blob/main/README.md)
- [The Twelve-Factor App](https://12factor.net)
