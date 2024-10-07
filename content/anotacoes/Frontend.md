---
title: Frontend
date: 2023-08-29
lastmod: 2024-10-07
aliases:
  - /anotacoes/html-over-the-wire/
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

## HTML over the wire
- [Hotwire](https://hotwired.dev/)
	- [for](https://github.com/hotwire-django) [Python#Django]({{< ref "Python#django" >}})
	- [Stimulus](https://stimulus.hotwired.dev/) - modest [JavaScript]({{< ref "JavaScript" >}}) framework
	- [Strada](https://strada.hotwired.dev/) - fully native controls, driven by your web app.
		- [Android](https://strada.hotwired.dev/handbook/android) - [GitHub](https://github.com/hotwired/strada-android)
		- [iOS](https://strada.hotwired.dev/handbook/ios) - [GitHub](https://github.com/hotwired/strada-ios)
		- [Web](https://strada.hotwired.dev/handbook/web) - [GitHub](https://github.com/hotwired/strada-web)
- [htmx](https://htmx.org/)
	- [for](https://github.com/adamchainz/django-htmx) [Python#Django]({{< ref "Python#django" >}})
- [Hyperview](https://hyperview.org/) - [GitHub](https://github.com/instawork/hyperview) - Native mobile apps, as easy as creating a website.
- [NativeScript](https://nativescript.org/)

## Math Notation
### Formats
- ASCIImath
- LaTeX
- MathML
### Libs
- [Builtin MathML] - [Can I use?](https://caniuse.com/?search=mathml) - [W3C](https://www.w3.org/TR/MathML/)
- [CKEditor + MathType](https://ckeditor.com/mathtype/)
- [KaTeX](https://github.com/KaTeX/KaTeX) - [for React](https://cortexjs.io/mathlive/guides/react/)
- [MathJax](https://www.mathjax.org/)
- [MathLive](https://github.com/arnog/mathlive/)
- [QuickLaTeX](https://www.quicklatex.com/)

## Storages
| Type            | Capacity | Supported Types                                           | Lifetime                                                    | Access                                              |     |
| --------------- | -------- | --------------------------------------------------------- | ----------------------------------------------------------- | --------------------------------------------------- | --- |
| Cookies         | 4KB      | Strings                                                   | until expiration date or manually deleted by user or webapp | Shared between tabs and windows and with the server |     |
| Session Storage | 5MB      | Strings                                                   | until tab is closed                                         | Not shared between tabs or windows                  |     |
| Local Storage   | 5MB      | Strings                                                   | until manually deleted by the user or webapp                | Shared between tabs and windows                     |     |
| IndexedDB       | >50MB    | Keys (Strings) and Values (objects, arrays, binary, etc.) | until manually deleted by the user or webapp                | Shared between tabs and windows                     |     |
- [Please Stop Using Local Storage](https://www.rdegges.com/2018/please-stop-using-local-storage/) - string only; synchronous; can’t be used by web workers; Any JavaScript code on your page can access;
- [OWASP - HTML5 Security Cheat Sheet # Local Storage](https://cheatsheetseries.owasp.org/cheatsheets/HTML5_Security_Cheat_Sheet.html#local-storage)
- [HTML Standard - Web Storage](https://html.spec.whatwg.org/multipage/webstorage.html)
- References: GPT-4; [MDN - IndexedDB API](https://developer.mozilla.org/en-US/docs/Web/API/IndexedDB_API); [MDN - Shared Storage API](https://developer.mozilla.org/en-US/docs/Web/API/Shared_Storage_API); [MDN - Web Storage API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Storage_API); [Stack Overflow - What is the difference between localStorage, sessionStorage, session and cookies?](https://stackoverflow.com/questions/19867599/what-is-the-difference-between-localstorage-sessionstorage-session-and-cookies)


## Toolbox
### Drag and Drop
- [Draggable JS](https://shopify.github.io/draggable/)
- [Pragmatic drag and drop](https://atlassian.design/components/pragmatic-drag-and-drop/about) - [GitHub](https://github.com/atlassian/pragmatic-drag-and-drop)
