---
title: Architecture
date: 2023-08-15
lastmod: 2024-07-12
aliases:
  - /anotacoes/microservices
  - /anotacoes/manifest-architecture
---
- References
	- [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected/)
	- [Azure Well-Architected Framework](https://learn.microsoft.com/en-us/azure/well-architected/)
	- [The Twelve-Factor App](https://12factor.net/)
- [How to drive your architecture decisions with a simple framework](https://twitter.com/milan_milanovic/status/1721442290760057223)
- Getting the Basics - Software Architecture Introduction
	- https://www.youtube.com/watch?v=8UlLgOf20Ho
	- Functional requirements: What should the system do?
	- Non-functional requirements: How should the system behave? (Functionality, Usability, Reliability, Efficiency, Maintainability, Scalability, Portability)
	- Restrictions (Legal Compliance, Cost, Standards, Talent Hiring, Time to Market)
	- Book - Software Architecture Patterns (O'Reilly)
- [The Architect’s Blueprint - Understanding Software Styles and Patterns with Cheatsheet](https://medium.com/bytebytego-system-design-alliance/the-architects-blueprint-understanding-software-styles-and-patterns-with-cheatsheet-5c1f5fd55bbd)
	- ![](/anotacoes/Assets/Software_Architecture_Styles.png)


## API
- https://jsonapi.org/

### REST
- [How Did REST Come To Mean The Opposite of REST?](https://htmx.org/essays/how-did-rest-come-to-mean-the-opposite-of-rest/)
- [REST APIs must be hypertext-driven](https://roy.gbiv.com/untangled/2008/rest-apis-must-be-hypertext-driven)


## Clean Architectures in [Python]({{< ref "Python" >}})
- https://www.youtube.com/watch?v=C7MRkqP5NRI
- by Leonardo Giordani - https://thedigitalcatonline.com
- Archicture is about
  > Firmitas, Utilitas, Venustas (Durability, Utility, Beauty)
  >
  > Vitruvius, De architecture, 15 BC
- Books suggestions
	- Object Oriented Software Engineering: A Use-Case Driven Approach - Ivar Jacobson
	- **Design Patterns** - E. Gamma, R. Helm, R. Johnson, J. Vlissides
	- Design Principles and Design Patterns - Robert Martin
	- Domain-Driven Design: Tackling Complexity in the Heart of Software - Eric Evans
	- **Enterprise Integration Patterns: Designing, Building, and Deploying Messaging Solutions** - H. Hohpe, B. Woolf
	- Clean Architecture in Python - Leonardo Giordani - bit.ly/getpycabook

### The Clean Architecture
- A **layered** approach for a more civilized age
  ![](/anotacoes/Assets/Pasted_image_20230720162108.png)
- "Your component can see only what is being defined in the inner layer"
- "The problem of unclean systems is dependent components"
- The golden rule: Talk inward with **simple structures**, talk outwards through **interfaces**.
  ![](/anotacoes/Assets/Pasted_image_20230720162524.png)
- Pros
	- Testability - be able to test only the business logic

### Django Architecture
- Mentioned unclean patterns
	- ORM that couples with Relational Databases - that's true
	- Models are aware/connected to the database (can be saved/retrieved natively) - partially true
		> When you test your Django application, you need the database. It's possible to test without the database, but you are sort of fighting against the framework.

	- "You usually implement your business logic in views" - That's not true. You can do it in every frameworks. But you should avoid in all, including Django.


## Event-driven
- https://serverlessland.com/event-driven-architecture/visuals - Diagrams about event-driven architectures

## Monoliths
- [How to recover from microservices](https://world.hey.com/dhh/how-to-recover-from-microservices-ce3803cc)
- [The Majestic Monolith](https://m.signalvnoise.com/the-majestic-monolith/)
- [Scaling up the Prime Video audio/video monitoring service and reducing costs by 90%](https://www.primevideotech.com/video-streaming/scaling-up-the-prime-video-audio-video-monitoring-service-and-reducing-costs-by-90)
	- [Amazon Prime Video’s Microservices Move Doesn’t Lead to a Monolith after All](https://thenewstack.io/amazon-prime-videos-microservices-move-doesnt-lead-to-a-monolith-after-all/)
- [Stack Overflow Architecture](https://stackexchange.com/performance)
- [What Powers Instagram: Hundreds of Instances, Dozens of Technologies](https://instagram-engineering.com/what-powers-instagram-hundreds-of-instances-dozens-of-technologies-adf2e22da2ad)

## RPC
> (in most cases) is a dangerous illusion.
>
> Local call: 1. Single process; 2. Negligible latency; 3. Call-stack built-in; 4. Same language and data types; 5. No partial failure;
>
> Fallacies of distributed computing: 1. The network is reliable; 2. Latency is zero; 3. Bandwidth is infinite; 4. The network is secure; 5. Topology doesn't change; 6. There is one administrator; 7. Transport cost is zero; 8. The network is homogeneous;
>
> from https://d1.awsstatic.com/events/Summits/reinvent2022/API308_Are-you-integrating-or-building-distributed-applications.pdf page 38

## Security
### Basic Auth
#### API Key
- [On API Keys Best Practices](https://blog.mergify.com/api-keys-best-practice/)
- Pros
	- Generated by the API - avoids poor passwords.
	- Only the API can know the user a key belongs to.
	- Doesn't leak the user password.
	- Can have different privileges.
- Best practices
	- Need to be rotated regularly - commonly required by operation control frameworks, such as SOC 2, HIPAA, or ISO 27001.
	- Allow multiple API keys, if the user wants to rotate its API Key without downtime.
	- Key expiration - enable the user to set an expiration.
	- Encrypt when storing in the database in a way that is not decryptable (hash).

### Cryptography
- Timing Attacks
	- Given a system that checks an encrypted value. The attacker measures the time to respond to a request. The longer it takes, the closer to breaking the encryption the attacker is.
	- [Python]({{< ref "Python" >}}) - use [secrets.compare_digest](https://docs.python.org/3/library/secrets.html#secrets.compare_digest), which uses a constant-time compare to reduce the risk.
	- [A Lesson In Timing Attacks (or, Don’t use MessageDigest.isEquals)](https://codahale.com/a-lesson-in-timing-attacks/)
		> A value which shares no bytes in common with the secret digest will return immediately; a value which shares the first 15 bytes will return 15 compares later.

### OAuth2
### OIDC
### Transport Security
- mTLS
- [Stunnel](https://www.stunnel.org/)
- [Toolbox#VPN]({{< ref "Toolbox#vpn" >}})


## Software Development Hour: From Developer to Architect with Nathaniel Schutta
- O'Reilly
- Hosted by Sam Newman
- Differences between Engineer and Architect
	- Need to know more about company politics
	- Have to be more proactive - you need to go to the work
	- More autonomy and accountability
	- Architect needs to deal more with people
	- It's more common to work on PoCs than day-to-day coding
- Tips
	- Try to remove obstacles before it happens
	- Make sure people understand your job/value
	- Focus on skills that last (example: communication, influence)
	- You will need to influence - get people to do what you want by making them think it's his idea
	- You will not know all answers, but you need to know how research and who ask
	- You have a limited social capital (influence currency) - You need to choose your battles.
- How to bring global context to your local team? Help the team to see the big picture.
	- Translate the message (security, performance, etc) for the particular audience. Business will not care about tech.
	- Maintenance - "Did you go to an airplane that didn't have maintenance for months/years?
- Book - How to win friend and influence people - It will help in your architecture role.

## References
![architecture_boat.jpeg](/anotacoes/Assets/architecture_boat.jpeg)
Source: https://x.com/vlad_mihalcea/status/1735564011666633001?s=46
