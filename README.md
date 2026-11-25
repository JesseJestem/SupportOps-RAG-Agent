# SupportOps RAG Agent

**AI-Powered Support Assistant with RAG, Tool Calling & FastAPI**

An AI-powered support assistant built with Python and FastAPI, designed to answer questions using a knowledge base, retrieve relevant documentation, and automate support workflows through LLM tool calling.

The project focuses on building a reliable, testable, and maintainable AI agent using modern backend engineering practices.

> **Status:** Work in progress — MVP development.

## Overview

Support teams often spend significant time searching documentation, investigating recurring issues, and manually creating support tickets.

SupportOps RAG Agent explores how Retrieval-Augmented Generation (RAG) and AI agents can improve these workflows.

The system is designed to:

- Retrieve relevant information from a document knowledge base.
- Generate answers grounded in retrieved documents.
- Provide references to the information used.
- Execute predefined tools through LLM function calling.
- Create support tickets after explicit user confirmation.
- Handle missing information and tool failures safely.
- Measure retrieval and answer quality through automated evaluation.

The project uses fictional support scenarios and synthetic documentation.

## Tech Stack

| Category | Technologies |
|---|---|
| Language | Python 3.12+ |
| Backend | FastAPI, Pydantic |
| LLM Integration | OpenAI API |
| Retrieval | Embeddings, similarity search |
| Vector Database | Chroma |
| Testing | pytest, httpx |
| Code Quality | Ruff, mypy |
| Containerization | Docker |
| CI/CD | GitHub Actions |

The initial implementation uses a lightweight Python architecture without LangChain or LangGraph to make the core RAG and agent mechanisms easier to understand and maintain.

## System Architecture

The planned system follows this workflow:

1. **Document Ingestion** — Load and process support documentation.
2. **Indexing** — Split documents into chunks, generate embeddings, and store them in a vector database.
3. **Retrieval** — Search for relevant information based on a user's question.
4. **Agent Orchestration** — Decide whether to retrieve knowledge, generate an answer, or call a tool.
5. **Tool Execution** — Perform predefined operations with validated inputs.
6. **Response Generation** — Return a structured response with supporting sources.
7. **Evaluation** — Measure quality, reliability, and performance.

### Simplified Architecture

```text
                  User
                    |
                    v
               FastAPI API
                    |
                    v
             Agent Orchestrator
                    |
          +---------+---------+
          |                   |
          v                   v
    Knowledge Search     Support Tools
          |                   |
          v                   v
    Vector Database      Ticket Service
          |                   |
          v                   v
    Relevant Context    Confirmation
          |                   |
          +---------+---------+
                    |
                    v
               LLM Response
                    |
                    v
             Answer + Sources
```

## Planned API

| Method | Endpoint | Description |
|---|---|---|
| GET | `/health` | Service health check |
| POST | `/documents/ingest` | Index knowledge-base documents |
| POST | `/chat` | Process user questions through the agent |
| POST | `/tickets/confirm` | Confirm a proposed support ticket |
| GET | `/tickets/{id}` | Retrieve a mock ticket |

The final API contract will be documented as each feature is implemented.

## Development Roadmap

### Stage 0 — Project Setup
- [ ] Initialize Python project and dependencies.
- [ ] Configure FastAPI application.
- [ ] Add Pydantic schemas and basic configuration.
- [ ] Implement a health-check endpoint.
- [ ] Set up initial unit tests.

### Stage 1 — Document Ingestion
- [ ] Load Markdown and TXT documents.
- [ ] Implement text chunking.
- [ ] Generate embeddings.
- [ ] Store and retrieve chunks using Chroma.

### Stage 2 — Basic RAG
- [ ] Implement vector similarity search.
- [ ] Build prompts from retrieved context.
- [ ] Integrate an LLM.
- [ ] Return answers with source references.
- [ ] Handle insufficient-context scenarios.

### Stage 3 — AI Agent
- [ ] Implement function/tool calling.
- [ ] Add a knowledge-base search tool.
- [ ] Add a mock ticket creation tool.
- [ ] Implement explicit confirmation for ticket creation.
- [ ] Handle tool errors, timeouts, and invalid responses.

### Stage 4 — Evaluation & Testing
- [ ] Create a reproducible evaluation dataset.
- [ ] Measure retrieval quality (Recall@K, MRR).
- [ ] Evaluate answer correctness and groundedness.
- [ ] Add regression tests for agent workflows.
- [ ] Test failure scenarios with mocked dependencies.

### Stage 5 — Deployment & Documentation
- [ ] Add structured logging and configuration.
- [ ] Containerize the application with Docker.
- [ ] Configure GitHub Actions.
- [ ] Document installation and local execution.
- [ ] Publish architecture documentation and evaluation results.

## Engineering Principles

The project follows several key principles:

- **Modularity:** Separate API, agent logic, retrieval, and storage.
- **Testability:** Support mocked LLM and external service dependencies.
- **Reliability:** Handle errors, retries, and invalid tool responses.
- **Transparency:** Provide evidence for generated answers.
- **Safety:** Require confirmation before actions with side effects.
- **Maintainability:** Use type hints, clear interfaces, and automated checks.

## Evaluation Strategy

The evaluation process will include:

- Retrieval Recall@K.
- Mean Reciprocal Rank (MRR).
- Answer correctness.
- Groundedness and source accuracy.
- Correct abstention when information is unavailable.
- Tool execution success rate.
- Response latency.

Evaluation results will be published after implementation and testing.

## Project Goals

This project is being developed as a practical AI engineering portfolio project.

The main learning objectives are:

1. Understand and implement RAG architecture.
2. Build LLM-powered agents with tool calling.
3. Develop production-oriented Python APIs.
4. Apply software testing and evaluation techniques to AI systems.
5. Explore reliability, observability, and failure handling.
6. Demonstrate end-to-end system design and engineering decisions.

## Security & Data

All sample documents and tickets are fictional.

The project does not use real customer information or proprietary employer data.

API keys and other secrets must be supplied through environment variables and must never be committed to Git.

## License

License to be determined before the first public release.
