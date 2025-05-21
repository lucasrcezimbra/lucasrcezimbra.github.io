---
title: Testing Autonomous Coders (or AI SWE)
date: 2024-12-26
lastmod: 2025-05-21
---


I created this [list of AI Software "Engineers"](https://toolbox.cezimbra.me/lists/ai-software-engineers/).

I used my project [django-template](https://github.com/lucasrcezimbra/django-template) as a test.
It has a straightforward issue that any AI/developer should be able to solve: [Makefile #488](https://github.com/lucasrcezimbra/django-template/issues/488)


## GitHub Copilot coding agent
Pricing: $39/month or $390/year

Testing on May/2025

### Setup
1. Signing up: https://github.com/features/copilot/plans
1. Allowing to access my repos: https://github.com/settings/copilot/coding_agent

### Testing
Issue: [Update psycopg from 2 to 3 · Issue #509 · lucasrcezimbra/django-template · GitHub](https://github.com/lucasrcezimbra/django-template/issues/509)

1. It created this WIP PR:
   [[WIP] Update psycopg from 2 to 3 · Pull Request #524 · lucasrcezimbra/django-template · GitHub](https://github.com/lucasrcezimbra/django-template/pull/524)
1. It started this agent session:
   [Update psycopg from version 2 to 3](https://github.com/lucasrcezimbra/django-template/pull/524/agent-sessions/0ee0e793-75c1-4ab0-889f-3a50efbb07da)
1. ✅ It checked and understood the repo structure
1. ❌ It tried to run the tests and failed because pytest was not installed;
   it tried to install and failed due a PyPI read timeout; then it gave up.
1. ✅ It "thought" and came up with a plan:
   ```
   - [ ] Update `{{cookiecutter.project_slug}}/pyproject.toml` to use psycopg 3.x instead of psycopg2-binary
   - [ ] Update test assertions in `tests/test_database.py` to check for psycopg instead of psycopg2-binary
   - [ ] Check for any other files that might need updates for psycopg3 compatibility
   - [ ] Verify changes work with the existing database connection configuration
   ```
1. ⚠ It updated psycopg by editing `{{cookiecutter.project_slug}}/pyproject.toml`
   instead of running poetry. Given that, it installed `psycopg==3.2.0` instead
   of the latest `3.2.9`.
1. ✅ It updated `tests/test_database.py` correctly.
1. ✅ It searched for another occurrences of `psycopg2` and didn't find.
1. ✅ It checked the `settings.py` file and understood it's using
   `dj-database-url`, so no need to change.
1. ⚠ It "thought" that `dj-database-url` supports psycopg3 which is true, but
   it referenced a release note that doesn't exist.
   > version 2.0.0 (released in August 2023) added support for psycopg3
   > ...
   > Reference: https://github.com/jazzband/dj-database-url/blob/master/CHANGELOG.md

   Version 2.0.0 was released April 2023 and there is no mention of psycopg3.
1. ✅ It pushed everything; the tests passed on CI.
1. 🧑 I asked it to update psycopg to the latest version. I purposely didn't
   say what is the latest, because I wanted to see if it would find out
   ([PR Comment](https://github.com/lucasrcezimbra/django-template/pull/524#discussion_r2099079481))
1. ✅ It tried to install and use `pip-search` twice and didn't work, then it
   ran `pip index versions psycopg`, found out the latest version, update the
   `pyproject.toml` and pushed the change.



## OpenHands
[Homepage](https://www.all-hands.dev/) | [GitHub](https://github.com/All-Hands-AI/OpenHands/) | [Docs](https://docs.all-hands.dev/modules/usage/installation)

OpenHands was the first AI SWE I tested on Dec/2024.


### Attempt 1. Using Docker
First I tried the Quick Start approach from the [README](https://github.com/All-Hands-AI/OpenHands/blob/172183f1af9ae39118823e8eeaa86cf0b34e4a1e/README.md) that uses Docker:

```shell
docker run -it --rm --pull=always \
    -e SANDBOX_RUNTIME_CONTAINER_IMAGE=docker.all-hands.dev/all-hands-ai/runtime:0.16-nikolaik \
    -e LOG_ALL_EVENTS=true \
    -v /var/run/docker.sock:/var/run/docker.sock \
    -v ~/.openhands:/home/openhands/.openhands \
    -p 3000:3000 \
    --add-host host.docker.internal:host-gateway \
    --name openhands-app \
    docker.all-hands.dev/all-hands-ai/openhands:0.16
```

Because I didn't review the code, and the Docker command needed some untrusted permissions, I created a (free tier) EC2 instance on AWS to run it:

- OS: Amazon Linux 2023 AMI
- Instance type: t2.micro
- Storage: 16GB (I started with 8GB, but it wasn't enough because I pulled
  multiple versions of the Docker image).
- Tailscale to expose the service to my local network

It didn't work. The logs were not helpful. I tried with different versions (0.16, 0.15, and 0.14). One of the errors was: `AttributeError: 'NoneType' object has no attribute 'logs'`. I found similar issues on GitHub, but none solved my issue. So, I gave up.


### Attempt 2. GitHub Actions
My second attempt was to run it on GitHub Actions.

I followed the instructions from [Docs - Using the OpenHands GitHub Action](https://docs.all-hands.dev/modules/usage/how-to/github-action) and [README - OpenHands Github Issue Resolver](https://github.com/All-Hands-AI/OpenHands/blob/725e71ad221c3eaa1aafebf3b32363afd044f57a/openhands/resolver/README.md).

#### Setting up and fixing Anthropic API Key
My first commit was [this](https://github.com/lucasrcezimbra/django-template/commit/2390b8fd073d3bb8b00326a16dd8e61ea4596a69) that adds the GitHub Actions workflow. The [run](https://github.com/lucasrcezimbra/django-template/actions/runs/12505374596/job/34888643271) failed with the following error:

```shell
ERROR:root:<class 'litellm.exceptions.AuthenticationError'>: litellm.AuthenticationError: AnthropicException - {"type":"error","error":{"type":"authentication_error","message":"invalid x-api-key"}}
```

I had two guesses:
1. Anthropic API keys were wrong or not working. So, I tested it locally and updated it on GitHub.
2. The OpenHands action was broken. So, I
   [tried to pin the version to 0.16.1](https://github.com/lucasrcezimbra/django-template/commit/2bec6e02b69c4021ca59959e273b60f18b1c99c8)
   (it was using from the `main` branch before).


I [ran the workflow again](https://github.com/lucasrcezimbra/django-template/actions/runs/12505750188/job/34889588239) and it partially worked:
- ✅ created the `Makefile`, committed, and pushed it into a new
  [branch](https://github.com/lucasrcezimbra/django-template/tree/openhands-fix-issue-488)
- ❌ didn't open the PR
- ❌ didn't run `make` commands to test the `Makefile`
- ❌ didn't understand that the `Makefile` was supposed to be for the template
  and not for the root project.


#### Opening PR
My next steps were opening the PR:
1. Manually opened the
   [PR](https://github.com/lucasrcezimbra/django-template/pull/500/) using the description written by OpenHands.
2. Waited for the CodeRabbit to run (idea: could configure CodeRabbit to mention
  `@openhands-agent` in the PR comments and let the AIs talk).
3. Deleted all CodeRabbit comments because I didn't want them to interfere with my comments.


#### Asking for fixes
After the PR was open, I [asked](https://github.com/lucasrcezimbra/django-template/pull/500#issuecomment-2562925426) OpenHands to fix it by moving the `Makefile`:
> @openhands-agent, the Makefile is supposed to belong to the project
> created by this template. So, it should be inside the
> `{{cookiecutter.project_slug}}/` folder.

Then I found some bugs:

`Error: Unhandled error: SyntaxError: Unexpected token '{'`.
and
 `Error: Unhandled error: SyntaxError: Unexpected identifier 'cookiecutter'`

I guessed it was because my comment had `, so I removed them and it worked. OpenHands added a new [commit](https://github.com/lucasrcezimbra/django-template/pull/500/commits/c69a9775b1af9db9a27b3017efc13d3a4d750829) to the PR.


#### Back and forth
After some back and forth, I gave up on this issue and tried with others. After more back and forth, I gave up on OpenHands at all and solved all the issues myself.

You can follow the back and forth in the PRs: [feat(#488): Makefile · #500](https://github.com/lucasrcezimbra/django-template/pull/500), [Fix issue #501: style: add ruff rules "N804", "N805" · #503](https://github.com/lucasrcezimbra/django-template/pull/503), and [Fix issue #504: Run lint and tests for generated projects · #505](https://github.com/lucasrcezimbra/django-template/pull/505)



## References
- [OpenHands/README.md](https://github.com/All-Hands-AI/OpenHands/blob/172183f1af9ae39118823e8eeaa86cf0b34e4a1e/README.md)
- [OpenHands docs](https://docs.all-hands.dev/modules/usage/installation)
