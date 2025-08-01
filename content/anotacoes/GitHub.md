---
title: "GitHub"
date: 2023-08-15
lastmod: 2025-08-01
---

## Actions
- Default environment variables: https://docs.github.com/en/actions/learn-github-actions/variables#default-environment-variables

- Error `refusing to allow a GitHub App to create or update workflow .github/workflows/<workflow.yml> without workflows permission`
  - https://github.com/orgs/community/discussions/35410#discussioncomment-7645702
  - `GITHUB_TOKEN` can't be given permissions to modify workflow files.
  - Use [PAT](https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token) or [GitHub App](https://github.com/peter-evans/create-pull-request/blob/main/docs/concepts-guidelines.md#authenticating-with-github-app-generated-tokens) instead.
