# Final, Detailed Plan for Fluid State Physics API Implementation

## Introduction

This document provides a comprehensive, step-by-step blueprint for integrating the "Fluid State Physics" domain into the PhsiPy-API project. The core objective is to create a robust, well-documented, and maintainable API layer that consumes the pre-existing `libs/phsipy` scientific library without modifying its source code.

The implementation will strictly adhere to the project's established architectural pattern, ensuring the new module is consistent with the existing codebase.

## Architectural Overview

The project follows a modular structure with a clear separation of concerns:

- **`main.py`**: The central entry point of the FastAPI application.
- **`routes/`**: Defines the HTTP API endpoints (e.g., `/fluid_state_physics/hydrostatic_pressure`).
- **`controllers/`**: Acts as the business logic layer, connecting routes to the scientific library.
- **`schemas/`**: Contains Pydantic models for robust data validation and clear API contracts.
- **`dictionaries/`**: Stores human-readable definitions for the scientific concepts.
- **`constants/`**: Holds static configuration and metadata for OpenAPI/Swagger documentation.

---

## Phase 1: API Contract and Configuration

This phase involves scaffolding the necessary files that define the structure, data contracts, and documentation for the new endpoints.

### Step 1.1: Define Route Metadata in `constants/FluidStatePhysicsConstants.py`

- **Purpose**: To decouple the OpenAPI documentation from the routing logic.
- **Action**: Create `constants/FluidStatePhysicsConstants.py` and define a dictionary named `FLUID_STATE_PHYSICS_ROUTE_PARAMS` containing the metadata for each endpoint.
- **Endpoints to be Covered**:
  - `HYDROSTATIC_PRESSURE`
  - `SURFACE_TENSION`
  - `CAPILLARY_PRESSURE`
  - `BERNOULLIS_EQUATION`
  - `POISEUILLES_LAW`
  - `REYNOLDS_NUMBER`
  - `STOKES_LAW`
  - `MACH_NUMBER`
  - `COMPRESSIBILITY_FACTOR`
  - `BOYLES_LAW`
  - `CHARLES_LAW`
  - `GAYLUSSACS_LAW`
  - `AVOGADROS_LAW`
  - `IDEAL_GAS_LAW`

### Step 1.2: Create Definitions in `dictionaries/FluidStatePhysicsDictionary.py`

- **Purpose**: To enrich the API responses with user-friendly definitions.
- **Action**: Create `dictionaries/FluidStatePhysicsDictionary.py` and define a dictionary named `FluidStatePhysicsDict` with a plain-text definition for each calculation.

### Step 1.3: Define Request Schemas in `schemas/FluidStatePhysicsSchema.py`

- **Purpose**: To ensure incoming request bodies are valid through Pydantic models.
- **Action**: Create `schemas/FluidStatePhysicsSchema.py` and define a Pydantic `BaseModel` class for each endpoint's request body.
- **Schemas to be Created**:
  - `HydrostaticPressureRequest`
  - `SurfaceTensionRequest`
  - `CapillaryPressureRequest`
  - `BernoullisEquationRequest`
  - `PoiseuillesLawRequest`
  - `ReynoldsNumberRequest`
  - `StokesLawRequest`
  - `MachNumberRequest`
  - `CompressibilityFactorRequest`
  - `BoylesLawRequest`
  - `CharlesLawRequest`
  - `GayLussacsLawRequest`
  - `AvogadrosLawRequest`
  - `IdealGasLawRequest`

---

## Phase 2: Business Logic Implementation

This phase focuses on creating the controller to bridge the API layer and the scientific library.

### Step 2.1: Create `controllers/FluidStatePhysicsControllers.py`

- **Purpose**: To house the core business logic, orchestrating the flow from request to response.
- **Action**: Create `controllers/FluidStatePhysicsControllers.py`. For each endpoint, create a corresponding function (e.g., `get_hydrostatic_pressure`) that:
    1. Accepts a Pydantic schema object.
    2. Calls the relevant static method from the `FluidStatePhysics` class in `libs.phsipy.PhsipyEquations`.
    3. Returns a `GenericResponse` object, populated with the definition, input values, and the calculated result.

---

## Phase 3: API Endpoint Exposure

This phase makes the controller logic accessible via HTTP endpoints.

### Step 3.1: Create `routes/FluidStatePhysicsRoutes.py`

- **Purpose**: To define the API routes and connect them to the controller functions.
- **Action**: Create `routes/FluidStatePhysicsRoutes.py`.
    1. Instantiate an `APIRouter`.
    2. For each controller function, create a corresponding `@FluidStatePhysics_Router.post(...)` decorator, specifying the URL path, unpacking the documentation from `FLUID_STATE_PHYSICS_ROUTE_PARAMS`, and setting the `response_model`.
    3. The decorated function will call its corresponding controller function.

---

## Phase 4: Application Integration

This final phase integrates the new module into the main FastAPI application.

### Step 4.1: Register the Router in `main.py`

- **Purpose**: To make the new Fluid State Physics API endpoints live.
- **Action**:
    1. Import the `FluidStatePhysics_Router` from `routes.FluidStatePhysicsRoutes` into `main.py`.
    2. Use `app.include_router(FluidStatePhysics_Router, prefix="/fluid_state_physics")` to register all the defined routes.
