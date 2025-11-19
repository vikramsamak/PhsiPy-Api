# Final, Detailed Plan for Thermodynamics API Implementation

## Introduction

This document provides a comprehensive, step-by-step blueprint for integrating the "Thermodynamics" domain into the PhsiPy-API project. The core objective is to create a robust, well-documented, and maintainable API layer that consumes the pre-existing `libs/phsipy` scientific library without modifying its source code.

The implementation will strictly adhere to the project's established architectural pattern, ensuring the new module is consistent with the existing codebase.

## Architectural Overview

The project follows a modular structure with a clear separation of concerns:

- **`main.py`**: The central entry point of the FastAPI application.
- **`routes/`**: Defines the HTTP API endpoints (e.g., `/thermodynamics/ideal_gas_law`).
- **`controllers/`**: Acts as the business logic layer, connecting routes to the scientific library.
- **`schemas/`**: Contains Pydantic models for robust data validation and clear API contracts.
- **`dictionaries/`**: Stores human-readable definitions for the scientific concepts.
- **`constants/`**: Holds static configuration and metadata for OpenAPI/Swagger documentation.

---

## Phase 1: API Contract and Configuration

This phase involves scaffolding the necessary files that define the structure, data contracts, and documentation for the new endpoints.

### Step 1.1: Define Route Metadata in `constants/ThermodynamicsConstants.py`

- **Purpose**: To decouple the OpenAPI documentation from the routing logic.
- **Action**: Create `constants/ThermodynamicsConstants.py` and define a dictionary named `THERMODYNAMICS_ROUTE_PARAMS` containing the metadata for each endpoint.
- **Endpoints to be Covered**:
  - `TEMPERATURE_CONVERSION_CELSIUS_TO_KELVIN`
  - `TEMPERATURE_CONVERSION_KELVIN_TO_CELSIUS`
  - `IDEAL_GAS_LAW`
  - `THERMAL_EXPANSION_COEFFICIENT`
  - `HEAT_TRANSFER_CONDUCTION`
  - `HEAT_TRANSFER_CONVECTION`
  - `HEAT_TRANSFER_RADIATION`
  - `FIRST_LAW_THERMODYNAMICS`
  - `EFFICIENCY_CARNOT`
  - `EFFICIENCY_HEAT_ENGINE`
  - `ENTROPY_CHANGE`
  - `ENTROPY_CHANGE_IRREVERSIBLE`
  - `ENTROPY_CHANGE_ADIABATIC`
  - `ENTROPY_CHANGE_PHASE`
  - `WORK_DONE_BY_IDEAL_GAS`
  - `ROOT_MEAN_SQUARE_SPEED`
  - `AVERAGE_KINETIC_ENERGY`
  - `SPEED_OF_SOUND`
  - `SPECIFIC_HEAT_CAPACITY`
  - `LATENT_HEAT`

### Step 1.2: Create Definitions in `dictionaries/ThermodynamicsDictionary.py`

- **Purpose**: To enrich the API responses with user-friendly definitions.
- **Action**: Create `dictionaries/ThermodynamicsDictionary.py` and define a dictionary named `ThermodynamicsDict` with a plain-text definition for each calculation.

### Step 1.3: Define Request Schemas in `schemas/ThermodynamicsSchema.py`

- **Purpose**: To ensure incoming request bodies are valid through Pydantic models.
- **Action**: Create `schemas/ThermodynamicsSchema.py` and define a Pydantic `BaseModel` class for each endpoint's request body.
- **Schemas to be Created**:
  - `TemperatureConversionCelsiusToKelvinRequest`
  - `TemperatureConversionKelvinToCelsiusRequest`
  - `IdealGasLawRequest`
  - `ThermalExpansionCoefficientRequest`
  - `HeatTransferConductionRequest`
  - `HeatTransferConvectionRequest`
  - `HeatTransferRadiationRequest`
  - `FirstLawThermodynamicsRequest`
  - `EfficiencyCarnotRequest`
  - `EfficiencyHeatEngineRequest`
  - `EntropyChangeRequest`
  - `EntropyChangeIrreversibleRequest`
  - `EntropyChangeAdiabaticRequest`
  - `EntropyChangePhaseRequest`
  - `WorkDoneByIdealGasRequest`
  - `RootMeanSquareSpeedRequest`
  - `AverageKineticEnergyRequest`
  - `SpeedOfSoundRequest`
  - `SpecificHeatCapacityRequest`
  - `LatentHeatRequest`

---

## Phase 2: Business Logic Implementation

### Step 2.1: Create `controllers/ThermodynamicsControllers.py`

- **Purpose**: To house the core business logic.
- **Action**: Create `controllers/ThermodynamicsControllers.py`. For each endpoint, create a corresponding function that:
    1. Accepts a Pydantic schema object.
    2. Calls the relevant static method from the `Thermodynamics` class in `libs.phsipy.PhsipyEquations`.
    3. Returns a `GenericResponse` object.

---

## Phase 3: API Endpoint Exposure

### Step 3.1: Create `routes/ThermodynamicsRoutes.py`

- **Purpose**: To define the API routes and connect them to the controller functions.
- **Action**: Create `routes/ThermodynamicsRoutes.py`, instantiate an `APIRouter`, and create a `@Thermodynamics_Router.post(...)` decorator for each controller function.

---

## Phase 4: Application Integration

### Step 4.1: Register the Router in `main.py`

- **Purpose**: To make the new Thermodynamics API endpoints live.
- **Action**:
    1. Import the `Thermodynamics_Router` from `routes.ThermodynamicsRoutes` into `main.py`.
    2. Use `app.include_router(Thermodynamics_Router, prefix="/thermodynamics")` to register all the defined routes.
