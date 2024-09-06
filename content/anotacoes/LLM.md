---
title: "LLM"
date: 2023-08-15
lastmod: 2024-09-06
---
- [Observability]({{< ref "Observability" >}})
- Vector [Databases]({{< ref "Databases" >}})
- OWASP Top 10 - [Doc](https://owasp.org/www-project-top-10-for-large-language-model-applications/assets/PDF/OWASP-Top-10-for-LLMs-2023-v1_0.pdf) - [Slides](https://owasp.org/www-project-top-10-for-large-language-model-applications/assets/PDF/OWASP-Top-10-for-LLMs-2023-slides-v1_0.pdf)
- [Unstructured](https://unstructured.io/) - ETL for LLMs
- LoRA = low rank adaptation - vastly cheaper mechanism for fine tuning
- [Emerging Architectures for LLM Applications](https://a16z.com/2023/06/20/emerging-architectures-for-llm-applications/)
- https://github.com/imartinez/privateGPT
- [Lit-GPT](https://github.com/Lightning-AI/lit-gpt)
- [Jina AI](https://jina.ai/)
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

## Web UIs for LLMs
| Name                                                           | Web Browse | Web Search | Voice | Image Generation | Mobile UI | Static site | Depends on | Language |
| -------------------------------------------------------------- | ---------- | ---------- | ----- | ---------------- | --------- | ----------- | ---------- | -------- |
| [Lobe Chat](https://github.com/lobehub/lobe-chat)              | Plugins    | Plugins    | ✅    | ✅               | ✅        | ❌          |            | English  |
| [big-AGI](https://github.com/enricoros/big-agi)                | ✅         | ✅         | ✅    | ✅               | ✅        |             |            | English  |
| [NextChat](https://github.com/ChatGPTNextWeb/ChatGPT-Next-Web) |            |            |       |                  |           | ❌          |            | Chinese  |
| [Anse](https://github.com/anse-app/anse)                       |            |            |       |                  |           |             |            | English  |
| [Chatbot UI](https://github.com/mckaywrigley/chatbot-ui)       |            |            |       |                  |           | ❌          | Supabase   | English  |
| [Better ChatGPT](https://github.com/ztjhz/BetterChatGPT)       |            |            |       |                  |           | ✅          |            | English  |
| [SlickGPT](https://github.com/ShipBit/slickgpt)                |            |            |       |                  |           | ❌          | Firebase   | English  |

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

## Comparison
- [Artificial Analysis](https://artificialanalysis.ai/) - independent analysis of AI models and hosting providers
- [Chatbot Arena](https://chat.lmsys.org/) - Benchmarking LLMs in the Wild


## Datasets
- https://pile.eleuther.ai/ - An 800GB Dataset of Diverse Text for Language Modeling
- https://laion.ai/ - Large-scale Artificial Intelligence Open Network - TRULY OPEN AI. 100% NON-PROFIT. 100% FREE.

## Hosting
### Cloud
- https://www.cerebrium.ai/ - makes it easier to train, deploy and monitor machine learning models with just a few lines of code - Serverless GPU Model Deployment
- https://cohere.ai/ - build high performance, secure LLM for the enterprise - powerful capabilities, like content generation, summarization, and search
- [CoreWeave](https://www.coreweave.com/) - cloud provider, delivering a massive scale of GPUs.
- [Foundry](https://mlfoundry.com/) - Instant Compute ML infra.
- [Lambda](https://lambdalabs.com/) - access to GPUs for deep learning.
- [Modal](https://modal.com/) - Run generative AI models, large-scale batch jobs, job queues, and much more.
- [Monster API](https://monsterapi.ai/) - access powerful generative AI models with our auto-scaling APIs, zero management required.
- [Replicate](https://replicate.com/) - Run models in the cloud at scale.
### Decentralized
- [GPUtopia](https://gputopia.ai/) - GPU Marketplace
- [Petals](https://petals.dev/) - Run large language models at home, BitTorrent‑style - [Repo](https://github.com/bigscience-workshop/petals)
### Local
- [LocalAI](https://github.com/go-skynet/LocalAI) - Self-hosted, community-driven, local OpenAI-compatible API. (...) No GPU required...
- [llama.cpp](https://github.com/ggerganov/llama.cpp)
	- [Python]({{< ref "Python" >}}) bindings - [Repo](https://github.com/abetlen/llama-cpp-python)
	- [A comprehensive guide to running Llama 2 locally](https://replicate.com/blog/run-llama-locally)
- [MLC LLM](https://mlc.ai/mlc-llm/) - LLM on iPhone - [App Store](https://apps.apple.com/us/app/mlc-chat/id6448482937?platform=iphone) - [Repository](https://github.com/mlc-ai/mlc-llm)
- [MLX](https://github.com/ml-explore/mlx) - An array framework for Apple silicon

## Image Generation
- DALL-E
	- [Prompt book](https://pitch.com/v/DALL-E-prompt-book-v1-tmd33y)
	- [DALL·E 2 Prompt Engineering Guide](https://docs.google.com/document/d/11WlzjBT0xRpQhP9tFMtxzd0q6ANIdHPUBkMV-YB043U/edit#)
	- [Use DALL-E to create infinite zoom movies](https://dosinga.medium.com/use-dall-e-to-create-infinite-zoom-movies-234fb72c85ab)
- [DreamStudio](https://beta.dreamstudio.ai/)
- [Hidden in Plain Sight](https://www.factsmachine.ai/p/hidden-in-plain-sight) - Hide text into images
- [Midjourney]({{< ref "Midjourney" >}})
- [Stable Diffusion](https://github.com/CompVis/stable-diffusion)
	- [Demo Hugging Face](https://huggingface.co/spaces/stabilityai/stable-diffusion)
	- [Online](https://stablediffusionweb.com/)
	- Outpainting on an infinite canvas - [Tweet](https://twitter.com/lkwq007/status/1576078349503373312) and [Sourcecode](https://github.com/lkwq007/stablediffusion-infinity)
- [Runway](https://runwayml.com/)
- https://stockimg.ai/
- https://www.tryleap.ai/

## Models
- [OpenHermes 2.5 - Mistral 7B](https://huggingface.co/teknium/OpenHermes-2.5-Mistral-7B) - can do function calling #OpenSource
### MPT
- [Introducing MPT-7B: A New Standard for Open-Source, Commercially Usable LLMs](https://www.mosaicml.com/blog/mpt-7b)
- https://github.com/mosaicml/composer - PyTorch library that enables you to train neural networks faster, at lower cost, and to higher accuracy - [Python]({{< ref "Python" >}})
- https://github.com/mosaicml/streaming - make training on large datasets from cloud storage as fast, cheap, and scalable as possible. [Python]({{< ref "Python" >}})
- https://github.com/mosaicml/llm-foundry

## Low-code platforms
- [Rivet](https://rivet.ironcladapp.com/) - The Open-Source Visual AI Programming Environment #OpenSource
- [Stack AI](https://www.stack-ai.com/) - The No-Code AI Automation Platform
- [Vellum](https://www.vellum.ai/) - The dev platform for production LLM apps

## RAG
- [ColBERT](https://github.com/stanford-futuredata/ColBERT) - fast and accurate retrieval model, enabling scalable BERT-based search over large text collections in tens of milliseconds.
	- [Exploring ColBERT with RAGatouille](https://til.simonwillison.net/llms/colbert-ragatouille)
	- [RAGatouille](https://github.com/bclavie/RAGatouille) - bridging the gap between state-of-the-art research and alchemical RAG pipeline practices

## SDKs
- [Guardrails](https://github.com/guardrails-ai/guardrails) - lets a user add structure, type and quality guarantees to the outputs of LLMs.
- [Guidance](https://github.com/microsoft/guidance/) - [Python]({{< ref "Python" >}}) lib that allows you to interleave generation, prompting, and logical control into a single continuous flow matching #OpenSource
- [Kor](https://eyurtsev.github.io/kor/index.html) - [Python]({{< ref "Python" >}}) lib that “helps” you extract structured data from text using LLMs #OpenSource
- [LangChain](https://langchain.readthedocs.io/en/latest/ ) -  [Python]({{< ref "Python" >}}) lib to develop AI applications - PromptTemplate, LLMs interface, etc. #OpenSource
	- **Agents** use an LLM to determine which actions to take and in what order.
	- Pros
		- [Builtin Chain serialization](https://python.langchain.com/en/latest/modules/chains/generic/serialization.htm)
	- [BabyAGI](https://github.com/yoheinakajima/babyagi) #Pinecone
	- [Langflow](https://github.com/logspace-ai/langflow) - UI designed with react-flow to provide an effortless way to experiment and prototype flows.
- [LiteLLM](https://docs.litellm.ai/docs/) - Call 100+ LLMs using the same Input/Output format #OpenSource
- [LlamaIndex](https://docs.llamaindex.ai/en/stable/) - framework for RAG #OpenSource
- [LLM](https://llm.datasette.io/en/stable/) - A CLI utility and [Python]({{< ref "Python" >}}) lib for interacting with OpenAI, PaLM and local models installed on your own machine #OpenSource
- [MonkeyPatch](https://github.com/monkeypatch/monkeypatch.py) - easily call an LLM in place of the function body in Python. The more you use MonkeyPatch functions, the cheaper and faster they gets (up to 9-10x!) through automatic model distillation. #OpenSource
- [Prompt Engine](https://github.com/microsoft/prompt-engine) - [Javascript]({{< ref "Javascript" >}}) lib for creating and maintaining prompts #OpenSource
- [Semantic Kernel](https://github.com/microsoft/semantic-kernel) -  [Python]({{< ref "Python" >}}) and C# libs that allow to define plugins that can be chained together #OpenSource

## Speech Recognition
- https://github.com/openai/whisper - general-purpose speech recognition model
	- https://github.com/ggerganov/whisper.cpp - runs on the CPU
		- https://huggingface.co/ggerganov/whisper.cpp/tree/main - models
