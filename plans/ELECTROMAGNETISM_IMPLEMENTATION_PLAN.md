# Final, Detailed Plan for Electromagnetism API Implementation

## Introduction

This document provides a comprehensive, step-by-step blueprint for integrating the "Electromagnetism" domain into the PhsiPy-API project. The core objective is to create a robust, well-documented, and maintainable API layer that consumes the pre-existing `libs/phsipy` scientific library without modifying its source code.

The implementation will strictly adhere to the project's established architectural pattern, ensuring the new module is consistent with the existing codebase.

## Architectural Overview

The project follows a modular structure with a clear separation of concerns:

- **`main.py`**: The central entry point of the FastAPI application.
- **`routes/`**: Defines the HTTP API endpoints (e.g., `/electromagnetism/voltage`).
- **`controllers/`**: Acts as the business logic layer, connecting routes to the scientific library.
- **`schemas/`**: Contains Pydantic models for robust data validation and clear API contracts.
- **`dictionaries/`**: Stores human-readable definitions for the scientific concepts.
- **`constants/`**: Holds static configuration and metadata for OpenAPI/Swagger documentation.

---

## Phase 1: API Contract and Configuration

This phase involves scaffolding the necessary files that define the structure, data contracts, and documentation for the new endpoints.

### Step 1.1: Define Route Metadata in `constants/ElectromagnetismConstants.py`

- **Purpose**: To decouple the OpenAPI documentation from the routing logic.
- **Action**: Create `constants/ElectromagnetismConstants.py` and define a dictionary named `ELECTROMAGNETISM_ROUTE_PARAMS` containing the metadata for each endpoint.
- **Endpoints to be Covered**:
  - `VOLTAGE`
  - `POWER`
  - `RESISTANCE`
  - `RESISTIVITY`
  - `ELECTRIC_FIELD`
  - `ELECTRIC_POTENTIAL_ENERGY`
  - `ELECTRIC_POWER`
  - `MAGNETIC_FIELD_STRENGTH`
  - `MAGNETIC_FLUX_DENSITY`
  - `MAGNETIC_FLUX`
  - `MAGNETIC_FORCE`
  - `LORENTZ_FORCE`
  - `HALL_VOLTAGE`
  - `FARADAYS_LAW`
  - `SELF_INDUCTANCE`
  - `MUTUAL_INDUCTANCE`
  - `COULOMBS_LAW`
  - `CAPACITANCE`
  - `ELECTRIC_FIELD_STRENGTH`
  - `ELECTRIC_FLUX_DENSITY`
  - `OHMS_LAW`
  - `MAGNETIC_FLUX_QUANTUM`
  - `DE_BROGLIE_WAVELENGTH`
  - `COMPTON_WAVELENGTH_CHANGE`
  - `BOHR_ORBIT_RADIUS`
  - `FERMI_ENERGY`
  - `DE_BROGLIE_WAVELENGTH_MATTER_WAVE`
  - `NUMBER_OF_IONS`
  - `ACCELERATION_DUE_TO_GRAVITY`
  - `MAGNETIC_FIELD_INSIDE_A_SOLENOID`
  - `MAGNETIC_FIELD_AROUND_A_WIRE`
  - `INDUCED_EMF`
  - `MAXWELL_EQUATION`
  - `SNELLS_LAW`
  - `CRITICAL_ANGLE`
  - `PHOTOELECTRIC_EFFECT_WORK_FUNCTION`
  - `PHOTOELECTRIC_EFFECT_MAX_VELOCITY`
  - `DECAY_LAW`
  - `HALF_LIFE`
  - `NUCLEAR_BINDING_ENERGY`
  - `RADIOACTIVE_DECAY`
  - `EINSTEIN_MASS_ENERGY_EQUIVALENCE`
  - `COULOMB_LAW`

### Step 1.2: Create Definitions in `dictionaries/ElectromagnetismDictionary.py`

- **Purpose**: To enrich the API responses with user-friendly definitions.
- **Action**: Create `dictionaries/ElectromagnetismDictionary.py` and define a dictionary named `ElectromagnetismDict` with a plain-text definition for each calculation.

### Step 1.3: Define Request Schemas in `schemas/ElectromagnetismSchema.py`

- **Purpose**: To ensure incoming request bodies are valid through Pydantic models.
- **Action**: Create `schemas/ElectromagnetismSchema.py` and define a Pydantic `BaseModel` class for each endpoint's request body.

---

## Phase 2: Business Logic Implementation

### Step 2.1: Create `controllers/ElectromagnetismControllers.py`

- **Purpose**: To house the core business logic.
- **Action**: Create `controllers/ElectromagnetismControllers.py`. For each endpoint, create a corresponding function that:
    1. Accepts a Pydantic schema object.
    2. Calls the relevant static method from the `Electromagnetism` class in `libs.phsipy.PhsipyEquations`.
    3. Returns a `GenericResponse` object.

---

## Phase 3: API Endpoint Exposure

### Step 3.1: Create `routes/ElectromagnetismRoutes.py`

- **Purpose**: To define the API routes and connect them to the controller functions.
- **Action**: Create `routes/ElectromagnetismRoutes.py`, instantiate an `APIRouter`, and create a `@Electromagnetism_Router.post(...)` decorator for each controller function.

---

## Phase 4: Application Integration

### Step 4.1: Register the Router in `main.py`

- **Purpose**: To make the new Electromagnetism API endpoints live.
- **Action**:
    1. Import the `Electromagnetism_Router` from `routes.ElectromagnetismRoutes` into `main.py`.
    2. Use `app.include_router(Electromagnetism_Router, prefix="/electromagnetism")` to register all the defined routes.
