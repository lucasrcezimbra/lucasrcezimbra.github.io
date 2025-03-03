---
title: Deploying Django with Kamal
date: 2025-02-24
lastmod: 2025-03-03
---

## Steps
1. Install Ruby. I didn't have Ruby installed and I use
   [mise-en-place](https://mise.jdx.dev/) as my tool version manager. So, I
   installed Ruby:

```shell
mise use ruby 3.4.2
```

2. Spin up a VPS. It could be any VPS. I used AWS EC2 because of the free tier.
   I did it through the AWS console.

3. Install kamal
```shell
gem install kamal
```
