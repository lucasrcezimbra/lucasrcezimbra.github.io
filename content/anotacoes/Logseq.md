---
title: "Logseq"
date: 2023-08-15T07:30:00-03:00
lastmod: 2023-08-15
---
- Namespaces
	- Create: use `/` on the page name. Example: `Root Page/Child Page`
	- Query: `{{namespace [[Root Page] ]}}`
- Create aliases: add property `alias:: First alias, Second Alias`
- Default templates: `:default-templates {:journals "Template Name"}`
- How to Login on Logseq? #troubleshooting 
	- 1. Create a `.desktop` file
	  ```
	  [Desktop Entry]
	  Exec=/bin/logseq %u
	  MimeType=x-scheme-handler/logseq
	  Name=Logseq
	  Type=Application
	  .local/share/applications
	  ```
	- from https://thinkstack.club/how-to-set-up-an-automated-daily-template-in-logseq/
- Arweave support [Web3]({{< ref "Web3" >}})
	- https://github.com/logseq/logseq/pull/3220
	- https://twitter.com/djwhitt/status/1462790586977689600
	- https://twitter.com/logseq/status/1462590014722764802

## Cheat sheet
- `Ctrl+Up Arrow` - Collapse
- `Ctrl+Down Arrow` - Expand
- Editing mode
	- `alt+Right Arrow` - Zoom in editing block
	- `alt+Left Arrow` - Zoom out editing block
- Normal mode
	- `g s` - Go to Keyboard shortcuts page
	- `g j` - Go to journals
	- `g t` - Go to journals
	- `alt+Right Arrow` - Forwards otherwise
	- `alt+Left Arror` - Backwards otherwise

## Publishing
- https://docs.logseq.com/#/page/publishing
- Publish on Github https://github.com/pengx17/logseq-publish
- Export to Hugo - https://github.com/sawhney17/logseq-schrodinger