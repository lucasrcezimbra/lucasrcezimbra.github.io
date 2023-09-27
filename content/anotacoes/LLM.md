---
title: "LLM"
date: 2023-08-15T07:30:00-03:00
---
- [Vector Database]({{< ref "Vector Database" >}})
- OWASP Top 10 - [Doc](https://owasp.org/www-project-top-10-for-large-language-model-applications/assets/PDF/OWASP-Top-10-for-LLMs-2023-v1_0.pdf) - [Slides](https://owasp.org/www-project-top-10-for-large-language-model-applications/assets/PDF/OWASP-Top-10-for-LLMs-2023-slides-v1_0.pdf)
- [Unstructured](https://unstructured.io/) - ETL for LLMs
- LoRA = low rank adaptation - vastly cheaper mechanism for fine tuning
- [Emerging Architectures for LLM Applications](https://a16z.com/2023/06/20/emerging-architectures-for-llm-applications/)
- https://github.com/imartinez/privateGPT
- https://github.com/Stability-AI/StableLM - Stability AI #OpenSource
- https://github.com/Torantulino/Auto-GPT
- https://github.com/hpcaitech/ColossalAI
	- https://www.hpc-ai.tech/blog/one-half-day-of-training-using-a-few-hundred-dollars-yields-similar-results-to-mainstream-large-models-open-source-and-commercial-free-domain-specific-llm-solution
- Transformer for Actions - GPT - https://www.adept.ai/blog/act-1
- Toolformer
	- Meta desenvolve modelo de linguagem que aprende sozinho a usar ferramentas externas, como mecanismos de busca, calculadoras e calendários
	- Decide por conta própria quais APIs usar para contornar as limitações presentes em outros sistemas, como a falta de conhecimento em aritmética, por exemplo. Seu desempenho é superior ao GPT-3, mesmo sendo baseado no GPT-J, um modelo com apenas 4% dos parâmetros.
	- https://arstechnica.com/information-technology/2023/02/meta-develops-an-ai-language-bot-that-can-use-external-software-tools/
	- https://arxiv.org/abs/2302.04761
- [You probably don't know how to do Prompt Engineering](https://gist.github.com/Hellisotherpeople/45c619ee22aac6865ca4bb328eb58faf)
- https://github.com/Lightning-AI/lit-llama #OpenSource 
> Good speech-to-text models have this trait, along with language translation programs and on-screen swipe keyboards. In each of these cases we want to be understood, not surprised. AI, therefore, makes the most sense as a translation layer between humans, who are incurably chaotic, and traditional software, which is deterministic.
> 
> an adaptive interface between chaotic real-world problems and secure, well-architected technical solutions. AI may not truly understand us, but it can deliver our intentions to an API with reasonable accuracy and describe the results in a way we understand.
> 
> from https://stackoverflow.blog/2023/05/01/ai-isnt-the-app-its-the-ui/

## ChatGPT
- Plugins
	-  https://medium.com/geekculture/6-chatgpt-mind-blowing-extensions-to-use-it-anywhere-db6638640ec7
		- https://github.com/wong2/chat-gpt-google-extension
		- https://github.com/gragland/chatgpt-chrome-extension
	- https://platform.openai.com/docs/plugins/introduction - Docs
	- http://openai.com/waitlist/plugins - Waitlist
	- https://openai.com/blog/chatgpt-plugins#OpenAI - Landing Page
	- https://github.com/openai/chatgpt-retrieval-plugin - The open-source retrieval plugin enables ChatGPT to access personal or organizational information sources

## Code generation
- https://github.com/replit/ReplitLM
- https://huggingface.co/blog/starcoder
	- https://huggingface.co/bigcode/starcoder
	- https://marketplace.visualstudio.com/items?itemName=HuggingFace.huggingface-vscode
### Copilot
- https://marketplace.visualstudio.com/items?itemName=gencay.vscode-chatgpt - ChatGPT no VSCode
- [Copilot Internals](https://thakkarparth007.github.io/copilot-explorer/posts/copilot-internals.html) - Reverse engineering

## Datasets
- https://pile.eleuther.ai/ - An 800GB Dataset of Diverse Text for Language Modeling
- https://laion.ai/ - Large-scale Artificial Intelligence Open Network - TRULY OPEN AI. 100% NON-PROFIT. 100% FREE.

## Hosting 
### Cloud
- https://www.cerebrium.ai/ - makes it easier to train, deploy and monitor machine learning models with just a few lines of code - Serverless GPU Model Deployment
- https://cohere.ai/ - build high performance, secure LLM for the enterprise - powerful capabilities, like content generation, summarization, and search
- https://replicate.com/ - Run models in the cloud at scale.
### Decentralized
- [Petals](https://petals.dev/) - Run large language models at home, BitTorrent‑style - [Repo](https://github.com/bigscience-workshop/petals)
### Local
- [MLC LLM](https://mlc.ai/mlc-llm/) - LLM on iPhone - [App Store](https://apps.apple.com/us/app/mlc-chat/id6448482937?platform=iphone) - [Repository](https://github.com/mlc-ai/mlc-llm)
- [LocalAI](https://github.com/go-skynet/LocalAI) - Self-hosted, community-driven, local OpenAI-compatible API. (...) No GPU required...
- [llama.cpp](https://github.com/ggerganov/llama.cpp)
	- [Python]({{< ref "Python" >}}) bindings - [Repo](https://github.com/abetlen/llama-cpp-python)
	- [A comprehensive guide to running Llama 2 locally](https://replicate.com/blog/run-llama-locally)
	
## Image Generation
- [DALL-E 2](https://openai.com/dall-e-2/)
	- [Prompt book](https://pitch.com/v/DALL-E-prompt-book-v1-tmd33y)
	- [DALL·E 2 Prompt Engineering Guide](https://docs.google.com/document/d/11WlzjBT0xRpQhP9tFMtxzd0q6ANIdHPUBkMV-YB043U/edit#)
	- [Use DALL-E to create infinite zoom movies](https://dosinga.medium.com/use-dall-e-to-create-infinite-zoom-movies-234fb72c85ab)
- [DreamStudio](https://beta.dreamstudio.ai/)
- [Midjourney]({{< ref "Midjourney" >}})
- [Stable Diffusion](https://github.com/CompVis/stable-diffusion)
	- [Demo Hugging Face](https://huggingface.co/spaces/stabilityai/stable-diffusion)
	- [Online](https://stablediffusionweb.com/)
	- Outpainting on an infinite canvas - [Tweet](https://twitter.com/lkwq007/status/1576078349503373312) and [Sourcecode](https://github.com/lkwq007/stablediffusion-infinity)
- https://www.tryleap.ai/

## MPT
- [Introducing MPT-7B: A New Standard for Open-Source, Commercially Usable LLMs](https://www.mosaicml.com/blog/mpt-7b)
- https://github.com/mosaicml/composer - PyTorch library that enables you to train neural networks faster, at lower cost, and to higher accuracy - [Python]({{< ref "Python" >}}) 
- https://github.com/mosaicml/streaming - make training on large datasets from cloud storage as fast, cheap, and scalable as possible. [Python]({{< ref "Python" >}})
- https://github.com/mosaicml/llm-foundry

## SDKs
- [Guidance](https://github.com/microsoft/guidance/) - [Python]({{< ref "Python" >}}) lib that allows you to interleave generation, prompting, and logical control into a single continuous flow matching #OpenSource 
- [Kor](https://eyurtsev.github.io/kor/index.html) - [Python]({{< ref "Python" >}}) lib that “helps” you extract structured data from text using LLMs #OpenSource 
- [LangChain](https://langchain.readthedocs.io/en/latest/ ) -  [Python]({{< ref "Python" >}}) lib to develop AI applications - PromptTemplate, LLMs interface, etc. #OpenSource
	- **Agents** use an LLM to determine which actions to take and in what order.
	- Pros
		- [Builtin Chain serialization](https://python.langchain.com/en/latest/modules/chains/generic/serialization.htm)
	- [BabyAGI](https://github.com/yoheinakajima/babyagi) #Pinecone
- [LlamaIndex](https://gpt-index.readthedocs.io/en/latest/index.html) - #OpenSource 
- [LLM](https://llm.datasette.io/en/stable/) - A CLI utility and [Python]({{< ref "Python" >}}) lib for interacting with OpenAI, PaLM and local models installed on your own machine #OpenSource 
- [Prompt Engine](https://github.com/microsoft/prompt-engine) - [Javascript]({{< ref "Javascript" >}}) lib for creating and maintaining prompts #OpenSource 
- [Semantic Kernel](https://github.com/microsoft/semantic-kernel) -  [Python]({{< ref "Python" >}}) and C# libs that allow to define plugins that can be chained together #OpenSource

## Speech Recognition 
- https://github.com/openai/whisper - general-purpose speech recognition model
	- https://github.com/ggerganov/whisper.cpp - runs on the CPU
		- https://huggingface.co/ggerganov/whisper.cpp/tree/main - models