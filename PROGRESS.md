# Development Progress

## 2026-11-26 — Testing Fundamentals

### Completed
- Implemented reusable TestClient fixture.
- Implemented fixture setup and teardown.
- Added parametrized API integration tests.
- Added positive and negative test cases.
- Completed code review: 9.5/10.
- Knowledge check: 4/5.
- All 8 tests passed in the review environment.

### Learned
- Arrange, Act, Assert pattern.
- Pytest fixtures and fixture scopes.
- Generator-based fixtures.
- Resource lifecycle management.
- Test parametrization.
- Positive and negative testing.
- Mock, Stub and Fake fundamentals.

### Issues / Gaps
- Mock vs Fake requires further practical experience.
- Local quality checks and PR merge pending.
- Clean environment verification pending.

### Next Task
- Finalize Task 0.2 and merge into dev.
- Task 0.3: REST & Pydantic.

### Current Stage
- Stage 0 — Setup & Architecture (In Progress).

## 2026-11-27 — Chat API Contract & Validation

### Completed
- Task 0.3: Chat API Contract & Validation.
- Declared Pydantic as a direct runtime dependency.
- Implemented ChatRequest and ChatResponse schemas.
- Implemented message length constraints and whitespace normalization.
- Implemented strict integer validation for top_k.
- Configured default values and numeric boundaries.
- Implemented POST /chat with a predefined stub response.
- Added 15 parametrized chat API validation scenarios.
- Added response contract integration test.
- Added unit tests for default values and whitespace normalization.
- Passed all 26 automated test cases.
- Passed local code quality checks.

### Learned
- Pydantic BaseModel.
- Runtime validation and static type checking.
- Field constraints and StringConstraints.
- Annotated metadata.
- Strict Mode and Type Coercion.
- Required and nullable fields.
- Request and response models.
- API contracts.
- Serialization, deserialization, and normalization.
- HTTP request and response validation.
- Boundary Value Analysis.
- Stub implementations.
- Pytest collection, setup, execution, and teardown.

### Issues / Gaps
- Dependency Injection requires further practice.
- API and business logic are not separated yet.
- External dependency mocking requires further practice.
- Clean environment installation verification pending.

### Next Task
- Task 0.4: Application Architecture & Dependency Injection.
- FastAPI APIRouter.
- Separation of Concerns.
- Service Layer.
- FastAPI Depends.
- Dependency overrides for testing.

### Current Stage
- Stage 0 — Setup & Architecture (In Progress).

## 2026-11-27 — API & Service Layer Refactoring

### Completed
- Created API and Service packages.
- Extracted health and chat endpoints into dedicated APIRouter modules.
- Implemented ChatService with a typed public interface.
- Delegated chat processing to the Service Layer.
- Separated application configuration from HTTP handling and business logic.
- Configured application metadata and Swagger tags.
- Implemented an isolated ChatService unit test.
- Preserved existing API behavior covered by regression tests.
- Passed all 27 automated tests.

### Learned
- Separation of Concerns.
- API Layer and Service Layer.
- APIRouter and router registration.
- Absolute and relative imports.
- Circular imports.
- Coupling and Cohesion.
- Delegation.
- Thin Controller.
- Composition Root.
- Python instance methods and object lifecycle.
- Arrange, Act, Assert pattern.
- Unit testing vs integration testing.
- Runtime type checking with isinstance().

### Issues / Gaps
- ChatService is instantiated directly inside the endpoint.
- Dependencies are not easily replaceable in API integration tests.
- Dependency lifecycle management is not implemented.
- Final static analysis checks, Swagger UI verification, and Pull Request are pending.

### Next Task
- Task 0.5: Dependency Injection.
- Dependency providers.
- FastAPI Depends().
- Dependency overrides.
- Testing with replaceable service implementations.

### Current Stage
- Stage 0 — Setup & Architecture (In Progress).
