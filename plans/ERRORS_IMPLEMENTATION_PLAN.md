# Final, Detailed Plan for Errors API Implementation

## Introduction

This document provides a comprehensive, step-by-step blueprint for integrating the "Errors" calculation module into the PhsiPy-API project. The core objective is to create a robust, well-documented, and maintainable API layer that consumes the pre-existing `libs/phsipy` scientific library without modifying its source code.

The implementation will strictly adhere to the project's established architectural pattern, ensuring the new module is consistent with the existing codebase.

## Architectural Overview

The project follows a modular structure with a clear separation of concerns:

- **`main.py`**: The central entry point of the FastAPI application.
- **`routes/`**: Defines the HTTP API endpoints (e.g., `/errors/error_muldiv`).
- **`controllers/`**: Acts as the business logic layer, connecting routes to the scientific library.
- **`schemas/`**: Contains Pydantic models for robust data validation and clear API contracts.
- **`dictionaries/`**: Stores human-readable definitions for the scientific concepts.
- **`constants/`**: Holds static configuration and metadata for OpenAPI/Swagger documentation.

---

## Phase 1: API Contract and Configuration

This phase involves scaffolding the necessary files that define the structure, data contracts, and documentation for the new endpoints.

### Step 1.1: Define Route Metadata in `constants/ErrorsConstants.py`

- **Purpose**: To decouple the OpenAPI documentation from the routing logic.
- **Action**: Create `constants/ErrorsConstants.py` and define a dictionary named `ERRORS_ROUTE_PARAMS` containing the metadata for each endpoint.
- **Endpoints to be Covered**:
  - `ERROR_MULDIV`
  - `ERROR_ADDSUB`
  - `PERCENTAGE_ERROR`
  - `ABSOLUTE_ERROR`
  - `MEAN_ABSOLUTE_ERROR`

### Step 1.2: Create Definitions in `dictionaries/ErrorsDictionary.py`

- **Purpose**: To enrich the API responses with user-friendly definitions.
- **Action**: Create `dictionaries/ErrorsDictionary.py` and define a dictionary named `ErrorsDict` with a plain-text definition for each calculation.

### Step 1.3: Define Request Schemas in `schemas/ErrorsSchema.py`

- **Purpose**: To ensure incoming request bodies are valid through Pydantic models.
- **Action**: Create `schemas/ErrorsSchema.py` and define a Pydantic `BaseModel` class for each endpoint's request body. Note that `absolute_error` and `meanabsolute_error` will accept a list of numbers.

---

## Phase 2: Business Logic Implementation

### Step 2.1: Create `controllers/ErrorsControllers.py`

- **Purpose**: To house the core business logic.
- **Action**: Create `controllers/ErrorsControllers.py`. For each endpoint, create a corresponding function that:
    1. Accepts a Pydantic schema object.
    2. Calls the relevant static method from the `Errors` class in `libs.phsipy.PhsipyEquations`.
    3. Returns a `GenericResponse` object.

---

## Phase 3: API Endpoint Exposure

### Step 3.1: Create `routes/ErrorsRoutes.py`

- **Purpose**: To define the API routes and connect them to the controller functions.
- **Action**: Create `routes/ErrorsRoutes.py`, instantiate an `APIRouter`, and create a `@Errors_Router.post(...)` decorator for each controller function.

---

## Phase 4: Application Integration

### Step 4.1: Register the Router in `main.py`

- **Purpose**: To make the new Errors API endpoints live.
- **Action**:
    1. Import the `Errors_Router` from `routes.ErrorsRoutes` into `main.py`.
    2. Use `app.include_router(Errors_Router, prefix="/errors")` to register all the defined routes.
