---
title: "Hugo"
date: 2023-09-11
lastmod: 2023-10-27
---
- How to add icon for external links ([Source](https://www.jayeless.net/2021/08/hugo-mark-external-links.html))
	```html
	<!-- layouts/_default/_markup/render-link.html -->
	<a href="{{ .Destination | safeURL }}"{{ with .Title}} title="{{ . }}"{{ end }}>{{ .Text | safeHTML }}{{ if strings.HasPrefix .Destination "http" }} <i class="fa fa-external-link" aria-hidden="true"></i>{{ end }}</a>
	```
- How to override the theme ([Source](https://gohugobrasil.netlify.app/themes/customizing/#override-template-files)): `layouts/_default/single.html` overwrites `/themes/<THEME>/layouts/_default/single.html`

## Search
- [Toolbox#Search#Client-side]({{< ref "Toolbox#search#client-side" >}})
- [hugo-lunr](https://github.com/dgrigg/hugo-lunr)