# Final, Detailed Plan for Waves API Implementation

## Introduction

This document provides a comprehensive, step-by-step blueprint for integrating the "Waves" physics domain into the PhsiPy-API project. The core objective is to create a robust, well-documented, and maintainable API layer that consumes the pre-existing `libs/phsipy` scientific library without modifying its source code.

The implementation strictly adheres to the project's established architectural pattern, which emphasizes a clear separation of concerns. This ensures that the new module is consistent with the existing codebase and easy to maintain or extend in the future.

## Architectural Overview

The project follows a modular structure, where each component has a distinct responsibility:

- **`main.py`**: The central entry point of the FastAPI application. It initializes the app and includes all the domain-specific routers.
- **`routes/`**: Defines the HTTP API endpoints (e.g., `/waves/velocity`). This layer is responsible for URL routing and exposing the functionality to the outside world.
- **`controllers/`**: Acts as the business logic layer. It connects the API routes to the underlying scientific library (`phsipy`), processes requests, and formats responses.
- **`schemas/`**: Contains Pydantic models that define the data shape for API requests. This ensures robust data validation, type safety, and clear API contracts.
- **`dictionaries/`**: Stores human-readable definitions and descriptions for the scientific concepts, which are used to enrich the API responses.
- **`constants/`**: Holds static configuration and metadata, such as the parameters for the OpenAPI/Swagger documentation, decoupling this information from the application logic.

---

## Phase 1: API Contract and Configuration

This phase involves scaffolding the necessary files that define the structure, data contracts, and documentation for our new endpoints.

### Step 1.1: Define Route Metadata in `constants/WavesConstants.py`

- **Purpose**: To decouple the OpenAPI/Swagger documentation (tags, summaries, descriptions) from the routing logic. This makes the route definitions in `WavesRoutes.py` cleaner and the documentation easier to manage.
- **Action**: Create `constants/WavesConstants.py` and define a dictionary named `WAVES_ROUTE_PARAMS`. Each key in this dictionary corresponds to a specific API endpoint and contains its documentation.
- **Endpoints Covered**:
  - `WAVE_VELOCITY`
  - `ANGULAR_FREQUENCY`
  - `WAVE_PERIOD`
  - `WAVE_NUMBER`
  - `WAVE_SPEED`
  - `INTENSITY`
  - `SOUND_INTENSITY`
  - `SOUND_LEVEL`
  - `BEATS_FREQUENCY`
  - `BEATS_PERIOD`
  - `REFRACTIVE_INDEX`
  - `DOPPLER_EFFECT`

### Step 1.2: Create Definitions in `dictionaries/WavesDictionary.py`

- **Purpose**: To provide clear, user-friendly definitions for the physical concepts in the API's JSON response. This enriches the user experience by making the output self-explanatory.
- **Action**: Create `dictionaries/WavesDictionary.py` and define a dictionary named `WavesDict`. Each key corresponds to a calculation and its value is the plain-text definition.

### Step 1.3: Define Request Schemas in `schemas/WavesSchema.py`

- **Purpose**: To ensure incoming request bodies are valid. Pydantic models automatically handle data validation, type enforcement, and error messaging for invalid inputs, making the API robust.
- **Action**: Create `schemas/WavesSchema.py` and define a Pydantic `BaseModel` class for each endpoint's request body. Each class will have attributes corresponding to the required input parameters with their expected types (e.g., `float`).
- **Schemas Created**:
  - `WaveVelocityRequest`
  - `AngularFrequencyRequest`
  - `WavePeriodRequest`
  - `WaveNumberRequest`
  - `WaveSpeedRequest`
  - `IntensityRequest`
  - `SoundIntensityRequest`
  - `SoundLevelRequest`
  - `BeatsFrequencyRequest`
  - `BeatsPeriodRequest`
  - `RefractiveIndexRequest`
  - `DopplerEffectRequest`

---

## Phase 2: Business Logic Implementation

This phase focuses on creating the controller, which acts as the bridge between the API layer and the scientific library.

### Step 2.1: Create `controllers/WavesControllers.py`

- **Purpose**: To house the core business logic. The controller's functions orchestrate the process of taking a validated request, calling the appropriate scientific function from the `phsipy` library, and packaging the result into a standardized response format.
- **Action**: Create `controllers/WavesControllers.py`. For each endpoint, create a corresponding function (e.g., `get_wave_velocity`). Each function performs three steps:
    1. Accepts a Pydantic schema object (e.g., `req: WaveVelocityRequest`).
    2. Calls the relevant static method from the `Waves` class in `libs.phsipy.PhsipyEquations` (e.g., `Waves.wave_velocity(...)`).
    3. Returns a `GenericResponse` object, populating it with the definition from `WavesDict`, the given input values, and the calculated result. This ensures a consistent response structure across the entire API.

---

## Phase 3: API Endpoint Exposure

This phase makes the controller logic accessible via HTTP endpoints.

### Step 3.1: Create `routes/WavesRoutes.py`

- **Purpose**: To define the actual API routes and connect them to the controller functions. This file uses FastAPI's `APIRouter` to keep the Waves-related endpoints modular and organized.
- **Action**: Create `routes/WavesRoutes.py`.
    1. Instantiate an `APIRouter`.
    2. For each controller function, create a corresponding `@Waves_Router.post(...)` decorator.
    3. The decorator specifies the URL path (e.g., `/velocity`), unpacks the documentation from `WAVES_ROUTE_PARAMS`, and sets the `response_model` to `GenericResponse[float]` (or `bool`) to enforce the output schema.
    4. The decorated function simply takes the request schema and calls its corresponding controller function.

---

## Phase 4: Application Integration and Finalization

This final phase integrates the new module into the main application and improves the project structure.

### Step 4.1: Register the Router in `main.py`

- **Purpose**: To make the new Waves API endpoints live and accessible through the main application.
- **Action**:
    1. Import the `Waves_Router` from `routes.WavesRoutes` into `main.py`.
    2. Use `app.include_router(Waves_Router, prefix="/waves")` to register all the defined routes under the `/waves` URL prefix.
