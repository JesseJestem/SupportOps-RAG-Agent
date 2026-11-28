# Development Progress

## 2026-11-24 to 2026-11-26 — Technical Assessment and Project Bootstrap

### Completed
- Initial technical assessment: 7/14; follow-up knowledge check: 4.5/5.
- Task 0.1: initialized Git repository, src layout, pyproject.toml, virtual environment, FastAPI and GET /health.
- Added API integration test and development tooling.
- Corrected package imports and migrated the TestClient dependency to httpx2.
- Local pytest, Ruff, mypy and pip check passed for Task 0.1.

### Learned
- Python packaging, editable installation, runtime/development dependencies, ASGI and basic API testing.

### Issues / Gaps
- Clean-environment installation verification remains pending.

## 2026-11-26 — Testing Fundamentals

### Completed
- Task 0.2: reusable TestClient fixture with setup and teardown, parametrized API tests, positive and negative cases.
- Reviewed 8 test cases; code review: 9.5/10; knowledge check: 4/5.
- Final test naming and response assertions corrected; PR #2 merged into dev.

### Learned
- Arrange, Act, Assert; fixtures and scopes; test isolation; resource lifecycle; mock, stub and fake fundamentals.

### Issues / Gaps
- Practical mocking experience remains pending.

## 2026-11-27 — Chat API Contract & Validation

### Completed
- Task 0.3: declared Pydantic v2 as a direct dependency and implemented ChatRequest and ChatResponse.
- Implemented POST /chat stub, whitespace normalization, length constraints and strict top_k validation.
- Added 15 parametrized validation cases, a response contract test and two schema unit tests.
- 26 tests reported passing; local quality checks reported passing.
- PR #3 merged into dev; code review: 9.5/10; knowledge check: 4.5/5.

### Learned
- Pydantic runtime validation, static typing, constraints, serialization, HTTP errors and boundary value analysis.

## 2026-11-27 — API & Service Layer Refactoring

### Completed
- Task 0.4: extracted health and chat routers and introduced ChatService.
- Separated application assembly, HTTP routing and application logic.
- Preserved existing API contracts and added an isolated ChatService unit test.
- PR #4 merged into dev (469f500e63b49cc130d27553087e2a6ffc9ed55a).
- Code review: 9.5/10; knowledge check: 3.5/5.
- 27 tests reported passing locally and independently reproduced in the review environment (27 passed in 0.13s).
- Verified application title and Health/Chat tags in the generated OpenAPI schema.

### Learned
- Separation of Concerns, APIRouter, Service Layer, thin controllers and composition root.
- Direction of dependencies, coupling, cohesion and regression testing.

### Issues / Gaps
- ChatService is still instantiated directly inside the endpoint; dependency overrides are not implemented.
- Refine the distinction between APIRouter and FastAPI, coupling strength vs dependency count, and circular imports vs architectural violations.
- Final local Ruff, mypy, pip check and browser Swagger UI verification remain to be confirmed for Task 0.4.
- Review tests used Linux, Python 3.13.5, FastAPI 0.128.2, Pydantic 2.13.5, httpx 0.28.1 and pytest 9.0.2; not the exact local dependency environment.
- Clean-environment installation verification remains pending.

### Next Task
- Confirm final local checks for Task 0.4.
- Task 0.5 — Dependency Injection: providers, FastAPI Depends, dependency overrides and isolated service substitution.

### Current Stage
- Stage 0 — Setup & Architecture (In Progress).

## 2026-11-28 — Dependency Injection

### Completed
- Task 0.5: introduced get_chat_service provider and injected ChatService using Annotated and FastAPI Depends.
- Added StubChatService and a dependency override integration test with try/finally cleanup.
- Verified existing API behavior and normalized message delivery to the substituted service.
- Reviewed dev commit 4c20033d926d7b1a4d68828a8c6a4719c71a41b4; changes were committed directly to dev.
- Reproduced all 28 tests successfully in the review environment (28 passed in 0.14s).
- Code review: 9.7/10 (rounded); knowledge check: 4.5/5.

### Learned
- Dependency injection, providers, dependency resolution and request-scoped caching.
- Dependency overrides, stub implementations and test isolation.

### Issues / Gaps
- Clarify provider responsibility vs FastAPI dependency resolution.
- The override test verifies message propagation but not top_k propagation; cleanup removes rather than restores a pre-existing override. Both are optional improvements for now.
- Local Ruff, formatting, mypy and pip check results remain unconfirmed for the current commit.
- Review used Linux, Python 3.13.5, FastAPI 0.128.2, Pydantic 2.13.5, httpx 0.28.1 and pytest 9.0.2 with PYTHONPATH=src; httpx2 and clean installation were not independently checked.

### Next Task
- Confirm local quality checks.
- Task 0.6 — Asynchronous Python: coroutines, event loop, blocking vs non-blocking I/O and concurrency.
- Resume feature-branch workflow.

### Current Stage
- Stage 0 — Setup & Architecture (In Progress).
