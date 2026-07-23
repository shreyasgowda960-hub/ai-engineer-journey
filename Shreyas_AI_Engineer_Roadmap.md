# Shreyas's Roadmap to Becoming an AI Engineer

*Built July 2026 · Target: AI engineer role · Commitment: a few focused hours daily · Realistic runway: ~6–10 months given your existing base*

---

## Read this first

You are not starting from zero. You already have Python, pandas/numpy, an ML project (the malware detector with scikit-learn), a data pipeline, and real software experience. That's a genuine head start for AI engineering — many people begin this path with none of it.

**What "AI engineer" actually means in 2026:** it's mostly about *building and deploying production AI systems* — connecting large language models to real products through RAG pipelines, agents, and APIs — rather than doing academic research or training huge models from scratch. Think: a chatbot that resolves support tickets, an internal search tool over company documents, an AI agent that automates a workflow.

**The single most important fact for you as a fresher:** deployed projects on GitHub are the #1 hiring signal. A degree matters less than a portfolio of 3–5 real, deployed AI projects. Everything in this roadmap builds toward that.

Two timelines:
- **Job-ready** — roughly 6–10 months of consistent daily work from where you are now.
- **Great AI engineer** — a multi-year path that continues into your career.

---

## How to use this

- Consistency beats intensity. A few focused hours every single day wins.
- Build and ship, don't just watch tutorials. "Tutorial hell" is the #1 way people stall on this path.
- Depth over breadth: one well-built, deployed RAG project is worth more than ten half-finished notebooks.
- Don't skip the foundations to rush to the shiny LLM stuff — the fundamentals are what make you employable versus just "someone who can call an API."
- Track progress daily (see the end).

---

## Daily time template (~3–4 hours)

- **~50%** — the current phase's main focus
- **~25%** — hands-on building / project work
- **~15%** — DSA practice (right-sized — see note below)
- **~10%** — reading, notes, applications, communication

Take one lighter review day per week.

**A note on DSA:** it's still worth doing because many AI/tech companies screen candidates with coding rounds. But for AI engineering it is *not* the main event — your project portfolio is. Keep DSA as a steady side-habit (1 problem most days), not your primary focus.

---

## Phase 0 — Python reset (Weeks 1–2)

Everything in AI runs on Python, so getting fluent again is the highest-leverage thing you can do first. You said you want to re-practice basics — do it here, fast.

- Core Python: variables, loops, functions, comprehensions, string/file handling, exceptions, OOP (classes, inheritance).
- Then push into what AI engineering actually uses: type hints, modular code design, and **async programming (asyncio)** — these come up constantly in production AI code.
- Set up: VS Code, Git, a clean GitHub profile, daily commit habit.
- Resources: Python official tutorial, "Automate the Boring Stuff" (free), freeCodeCamp Python.

**Checkpoint:** you can write clean Python functions and classes without googling basic syntax.

---

## Phase 1 — Foundations: math, data, and Python depth (Weeks 3–8)

Goal: build the mathematical and data groundwork that makes ML click, while keeping Python sharp.

**Math (you don't need to be an expert — aim for intuition):**
- Linear algebra: vectors, matrices, matrix multiplication, dot products (this is how models represent and transform data).
- Probability & statistics: distributions, mean/variance, conditional probability, Bayes' basics.
- Calculus: just enough to understand gradients and how models "learn" (gradient descent).
- Resource: 3Blue1Brown's "Essence of Linear Algebra" and "Essence of Calculus" (free, visual, excellent); Khan Academy for stats.

**Data handling (you already have a base here — sharpen it):**
- pandas and numpy in depth: cleaning, transforming, merging, feature scaling, encoding.
- Exploratory Data Analysis: distributions, correlations, visualization (matplotlib/seaborn).
- Working with CSV, JSON, and APIs as data sources.

**DSA (side-habit):** start easy — arrays, strings, hashmaps. ~1 problem most days on LeetCode/NeetCode.

**Checkpoint:** you can take a messy dataset, clean it, explore it, and explain what linear algebra and gradients have to do with learning.

---

## Phase 2 — Machine Learning & Deep Learning foundations (Weeks 9–18)

Goal: understand how models actually work before you build on top of them. This is what separates a real AI engineer from someone who only knows how to call an API.

**Classical ML (build on your scikit-learn experience):**
- Supervised learning: regression, classification, decision trees, random forests.
- Unsupervised learning: clustering, dimensionality reduction.
- Model evaluation: train/test split, cross-validation, precision/recall/F1, overfitting vs underfitting.
- Resource: Andrew Ng's Machine Learning Specialization (Coursera), Google's ML Crash Course (free).

**Deep Learning intro:**
- Neural network basics: layers, activation functions, forward/backprop (conceptually), loss functions.
- Pick **one framework and learn it hands-on: PyTorch** (most common in modern AI work) or TensorFlow.
- Build a couple of small models: an image classifier, a text classifier.

**Milestone project:** take your existing malware-detection project and rebuild/upgrade it properly — clean pipeline, solid evaluation, a documented README. Turning something you already did into a polished portfolio piece is high-value and motivating.

**Checkpoint:** you can train, evaluate, and explain a model, and you've built at least one small neural network yourself.

---

## Phase 3 — The modern AI engineering core (Weeks 19–30)

This is the heart of the job in 2026. Goal: build production AI systems on top of LLMs.

**LLM fundamentals & APIs:**
- How LLMs work at a high level (tokens, context windows, embeddings, temperature).
- Calling LLM APIs (Anthropic, OpenAI, etc.) from Python.
- **Prompt engineering:** giving context, examples, constraints, and output formats; understanding when and why model outputs are wrong (hallucinations).

**RAG (Retrieval-Augmented Generation) — learn this deeply, it's central:**
- Embeddings and semantic search.
- Vector databases (Chroma or Pinecone or Weaviate).
- Building a pipeline: chunk documents → embed → store → retrieve → feed to the LLM.

**Frameworks & agents:**
- LangChain and/or LlamaIndex for orchestrating LLM apps.
- AI agents: multi-step reasoning, tool use, agent frameworks (e.g. LangGraph).
- **Model Context Protocol (MCP)** — Anthropic's open standard for connecting AI models to external tools and data. Engineers who can build MCP servers are still a small minority in 2026, so this is a genuine differentiator worth learning.

**Flagship projects (build 2–3 of these and deploy them publicly):**
- A RAG knowledge assistant over a document set (e.g. answer questions about a textbook or a company's docs).
- A customer-support chatbot with guardrails.
- A multi-agent research assistant.
- An MCP-connected productivity assistant (bonus — stands out).
- Given your data background: an AI system that ingests and answers questions over a real dataset (ties into your transit-analytics experience nicely).

**Checkpoint:** you have at least one working, deployed RAG or agent app with a clear README and a demo.

---

## Phase 4 — Deployment, portfolio & job hunt (Weeks 31+, overlaps with Phase 3)

Goal: make your projects production-grade and get hired. Start applying *before* you feel fully ready.

**Deployment / MLOps basics (the "systems-first" skills employers now expect):**
- **FastAPI** — wrap your AI systems in production APIs (async, auto-docs, Pydantic).
- **Docker** — containerize your services for portable, consistent deployment.
- Deploy to the cloud: AWS Lambda / GCP Cloud Run / Azure Container Apps, or Vercel for web-based AI apps.
- **LangSmith** or similar — trace and monitor LLM calls, debug production failures, evaluate RAG quality (faithfulness, relevancy).

**Portfolio:**
- Aim for **3–5 complete, deployed, end-to-end projects.** This is the primary thing hiring managers look at for freshers.
- Each with a clean README (problem, approach, screenshots, live demo link, what you'd improve).
- Write about your work on LinkedIn or a blog — build in public. It attracts recruiters and proves you can communicate.

**Interview prep:**
- Be able to explain every project deeply — the decisions, the trade-offs, what broke and how you fixed it.
- Brush up DSA for coding screens.
- Basic system design: how you'd architect a RAG system, handle scale, manage cost and latency.
- Prepare STAR-format behavioural stories.

**Apply widely and consistently.** Tailor your resume's keywords to each JD. Track every application.

---

## The specialization fork (decide around Phase 3–4)

"AI engineer" splits into two main flavors. You don't have to choose early — the foundation above serves both — but lean into one as you go:

- **AI / GenAI Application Engineer** — building LLM-powered products: RAG, agents, MCP, deployment. *Best fit for your software + API background, and the most abundant fresher-friendly path.* Emphasize Phase 3 heavily.
- **Machine Learning Engineer** — deeper into model training, deep learning, and MLOps (PyTorch/TensorFlow, distributed training, model serving). Emphasize Phase 2 more, add advanced DL.

Your resume (strong software/API skills, some ML) points most naturally at the **Application Engineer** path. That's where I'd aim first.

---

## Milestones to check yourself against

- **Month 1:** Python fluent and async-capable; environment and GitHub set up.
- **Month 2–3:** Math intuition + data skills solid; classical ML understood.
- **Month 4–5:** Deep learning basics; malware project upgraded and polished; first neural net built.
- **Month 6–7:** First deployed RAG/agent app live; portfolio taking shape.
- **Month 8–10:** 3–5 deployed AI projects; actively interviewing.

Timelines are guides. Adjust the pace, don't abandon the plan.

---

## How to track (do this)

- Daily: *did I hit my hours? y/n* + one line on what you built/learned.
- A project tracker: which portfolio projects are planned / in progress / deployed.
- Weekly 3-line review: what went well, what didn't, what to change.

The one variable that decides whether this works is **showing up daily and shipping real projects.** You have the background and the time. The rest is reps.
