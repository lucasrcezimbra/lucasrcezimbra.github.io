---
title: "Frontend"
date: 2023-08-29T10:09:49-0300
---
- [Alpine.js](https://alpinejs.dev/) - Your new, lightweight, JavaScript framework.
- [HTMX](https://htmx.org/) - high power tools for HTML
- [hyperscript](https://hyperscript.org/) - An easy & approachable language for modern web front-ends


- [Islands Architecture](https://www.patterns.dev/posts/islands-architecture) - encourages small, focused chunks of interactivity within server-rendered web pages


## async vs defer
- [Tweet](https://twitter.com/lucasrcezimbra/status/1717870039565533530)
- Both
	- Doesn't block page loading and rendering.
- async
	- Runs immediately after download.
	- No guaranteed execution order (might differ from the order in the HTML)
	- Beneficial for stand-alone scripts, not affecting initial DOM.
- defer
	- Waits for HTML parsing to finish.
	- Maintains script order in the document (beneficial for scripts that rely on each other)
	- Beneficial for scripts that are not necessary until the page content has been loaded.