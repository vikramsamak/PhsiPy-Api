# Final, Detailed Plan for Solid State Physics API Implementation

## Introduction

This document provides a comprehensive, step-by-step blueprint for integrating the "Solid State Physics" domain into the PhsiPy-API project. The core objective is to create a robust, well-documented, and maintainable API layer that consumes the pre-existing `libs/phsipy` scientific library without modifying its source code.

The implementation will strictly adhere to the project's established architectural pattern, ensuring the new module is consistent with the existing codebase.

## Architectural Overview

The project follows a modular structure with a clear separation of concerns:

-   **`main.py`**: The central entry point of the FastAPI application.
-   **`routes/`**: Defines the HTTP API endpoints (e.g., `/solid_state_physics/electrical_resistivity`).
-   **`controllers/`**: Acts as the business logic layer, connecting routes to the scientific library.
-   **`schemas/`**: Contains Pydantic models for robust data validation and clear API contracts.
-   **`dictionaries/`**: Stores human-readable definitions for the scientific concepts.
-   **`constants/`**: Holds static configuration and metadata for OpenAPI/Swagger documentation.

---

## Phase 1: API Contract and Configuration

This phase involves scaffolding the necessary files that define the structure, data contracts, and documentation for the new endpoints.

### Step 1.1: Define Route Metadata in `constants/SolidStatePhysicsConstants.py`

-   **Purpose**: To decouple the OpenAPI documentation from the routing logic.
-   **Action**: Create `constants/SolidStatePhysicsConstants.py` and define a dictionary named `SOLID_STATE_PHYSICS_ROUTE_PARAMS` containing the metadata for each endpoint.
-   **Endpoints to be Covered**:
    -   `ELECTRICAL_RESISTIVITY`
    -   `HALL_EFFECT`
    -   `ELECTRON_MOBILITY`
    -   `FERMI_ENERGY`
    -   `BAND_GAP`
    -   `ENERGY_BAND`
    -   `ENERGY_BAND_CONDUCTION`
    -   `INTRINSIC_CARRIER_CONCENTRATION`
    -   `DEPLETION_LAYER_WIDTH`
    -   `SOLAR_CELL_EFFICIENCY`
    -   `ENERGY_DENSITY`
    -   `YOUNGS_MODULUS`
    -   `POISSON_RATIO`
    -   `THERMAL_CONDUCTIVITY`
    -   `SUPERCONDUCTIVITY_CRITICAL_TEMPERATURE`
    -   `SUPERCONDUCTIVITY_COHERENCE_LENGTH`

### Step 1.2: Create Definitions in `dictionaries/SolidStatePhysicsDictionary.py`

-   **Purpose**: To enrich the API responses with user-friendly definitions.
-   **Action**: Create `dictionaries/SolidStatePhysicsDictionary.py` and define a dictionary named `SolidStatePhysicsDict` with a plain-text definition for each calculation.

### Step 1.3: Define Request Schemas in `schemas/SolidStatePhysicsSchema.py`

-   **Purpose**: To ensure incoming request bodies are valid through Pydantic models.
-   **Action**: Create `schemas/SolidStatePhysicsSchema.py` and define a Pydantic `BaseModel` class for each endpoint's request body.
-   **Schemas to be Created**:
    -   `ElectricalResistivityRequest`
    -   `HallEffectRequest`
    -   `ElectronMobilityRequest`
    -   `FermiEnergyRequest`
    -   `BandGapRequest`
    -   `EnergyBandRequest`
    -   `EnergyBandConductionRequest`
    -   `IntrinsicCarrierConcentrationRequest`
    -   `DepletionLayerWidthRequest`
    -   `SolarCellEfficiencyRequest`
    -   `EnergyDensityRequest`
    -   `YoungsModulusRequest`
    -   `PoissonRatioRequest`
    -   `ThermalConductivityRequest`
    -   `SuperconductivityCriticalTemperatureRequest`
    -   `SuperconductivityCoherenceLengthRequest`

---

## Phase 2: Business Logic Implementation

This phase focuses on creating the controller to bridge the API layer and the scientific library.

### Step 2.1: Create `controllers/SolidStatePhysicsControllers.py`

-   **Purpose**: To house the core business logic, orchestrating the flow from request to response.
-   **Action**: Create `controllers/SolidStatePhysicsControllers.py`. For each endpoint, create a corresponding function (e.g., `get_electrical_resistivity`) that:
    1.  Accepts a Pydantic schema object.
    2.  Calls the relevant static method from the `SolidStatePhysics` class in `libs.phsipy.PhsipyEquations`.
    3.  Returns a `GenericResponse` object, populated with the definition, input values, and the calculated result.

---

## Phase 3: API Endpoint Exposure

This phase makes the controller logic accessible via HTTP endpoints.

### Step 3.1: Create `routes/SolidStatePhysicsRoutes.py`

-   **Purpose**: To define the API routes and connect them to the controller functions.
-   **Action**: Create `routes/SolidStatePhysicsRoutes.py`.
    1.  Instantiate an `APIRouter`.
    2.  For each controller function, create a corresponding `@SolidStatePhysics_Router.post(...)` decorator, specifying the URL path, unpacking the documentation from `SOLID_STATE_PHYSICS_ROUTE_PARAMS`, and setting the `response_model`.
    3.  The decorated function will call its corresponding controller function.

---

## Phase 4: Application Integration

This final phase integrates the new module into the main FastAPI application.

### Step 4.1: Register the Router in `main.py`

-   **Purpose**: To make the new Solid State Physics API endpoints live.
-   **Action**:
    1.  Import the `SolidStatePhysics_Router` from `routes.SolidStatePhysicsRoutes` into `main.py`.
    2.  Use `app.include_router(SolidStatePhysics_Router, prefix="/solid_state_physics")` to register all the defined routes.
