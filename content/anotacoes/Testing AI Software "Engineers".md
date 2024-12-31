---
title: Testing AI Software "Engineers"
date: 2024-12-26
lastmod: 2024-12-31
---


I used my project [django-template](https://github.com/lucasrcezimbra/django-template) as a test.
It has a straightforward issue that any AI/developer should be able to solve: [Makefile #488](https://github.com/lucasrcezimbra/django-template/issues/488)



## All-Hands-AI/OpenHands
[Homepage](https://www.all-hands.dev/) | [GitHub](https://github.com/All-Hands-AI/OpenHands/) | [Docs](https://docs.all-hands.dev/modules/usage/installation)

OpenHands was the first AI SWE I tested.


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

I created a (free tier) EC2 instance on AWS:

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
I gave up on this issue and tried others. After some back and forth, I gave up on OpenHands and solved all the issues myself.

You can follow the back and forth in the PRs: [feat(#488): Makefile · #500](https://github.com/lucasrcezimbra/django-template/pull/500), [Fix issue #501: style: add ruff rules "N804", "N805" · #503](https://github.com/lucasrcezimbra/django-template/pull/503), and [Fix issue #504: Run lint and tests for generated projects · #505](https://github.com/lucasrcezimbra/django-template/pull/505)



## References
- [OpenHands/README.md](https://github.com/All-Hands-AI/OpenHands/blob/172183f1af9ae39118823e8eeaa86cf0b34e4a1e/README.md)
- [OpenHands docs](https://docs.all-hands.dev/modules/usage/installation)
