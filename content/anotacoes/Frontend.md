---
title: "Frontend"
date: 2023-08-29T10:09:49-0300
---
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

## Frameworks
- [Alpine.js](https://alpinejs.dev/) - Your new, lightweight, JavaScript framework.
- [htmx](https://htmx.org/) - high power tools for HTML
- [htmz](http://leanrada.com/htmz/) 
- [hyperscript](https://hyperscript.org/) - An easy & approachable language for modern web front-ends

## Math Notation
- [KaTeX](https://github.com/KaTeX/KaTeX) - [for React](https://cortexjs.io/mathlive/guides/react/)
- [MathJax](https://www.mathjax.org/)
- [MathLive](https://github.com/arnog/mathlive/)
- [QuickLaTeX](https://www.quicklatex.com/)