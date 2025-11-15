# Final, Detailed Plan for Quantum Mechanics API Implementation

## Introduction

This document provides a comprehensive, step-by-step blueprint for integrating the "Quantum Mechanics" domain into the PhsiPy-API project. The core objective is to create a robust, well-documented, and maintainable API layer that consumes the pre-existing `libs/phsipy` scientific library without modifying its source code.

The implementation will strictly adhere to the project's established architectural pattern, ensuring the new module is consistent with the existing codebase.

## Architectural Overview

The project follows a modular structure with a clear separation of concerns:

- **`main.py`**: The central entry point of the FastAPI application.
- **`routes/`**: Defines the HTTP API endpoints (e.g., `/quantum_mechanics/uncertainty_principle`).
- **`controllers/`**: Acts as the business logic layer, connecting routes to the scientific library.
- **`schemas/`**: Contains Pydantic models for robust data validation and clear API contracts.
- **`dictionaries/`**: Stores human-readable definitions for the scientific concepts.
- **`constants/`**: Holds static configuration and metadata for OpenAPI/Swagger documentation.

---

## Phase 1: API Contract and Configuration

This phase involves scaffolding the necessary files that define the structure, data contracts, and documentation for the new endpoints.

### Step 1.1: Define Route Metadata in `constants/QuantumMechanicsConstants.py`

- **Purpose**: To decouple the OpenAPI documentation from the routing logic.
- **Action**: Create `constants/QuantumMechanicsConstants.py` and define a dictionary named `QUANTUM_MECHANICS_ROUTE_PARAMS` containing the metadata for each endpoint.
- **Endpoints to be Covered**:
  - `UNCERTAINTY_PRINCIPLE`
  - `SCHRODINGERS_EQUATION`
  - `PROBABILITY_DENSITY`
  - `TUNNELING_PROBABILITY`
  - `BLACK_BODY_RADIATION_INTENSITY`
  - `BLACK_BODY_RADIATION_POWER`
  - `FERMI_DIRAC_DISTRIBUTION`
  - `BOSE_EINSTEIN_DISTRIBUTION`
  - `WAVE_PARTICLE_DUALITY`
  - `HEISENBERG_UNCERTAINTY_ENERGY_LIFETIME`
  - `HEISENBERG_UNCERTAINTY_POSITION_MOMENTUM`
  - `ATOMIC_ORBITAL_RADIUS`
  - `FINE_STRUCTURE_CONSTANT`
  - `DE_BROGLIE_WAVELENGTH_PHOTON`
  - `DE_BROGLIE_WAVELENGTH_PARTICLE`
  - `PLANK_DISTRIBUTION_RADIATION`
  - `PLANK_DISTRIBUTION`
  - `PLANK_LAW_INTENSITY`
  - `PLANK_LAW_POWER`
  - `EINSTEIN_LIGHT_QUANTA`
  - `EINSTEIN_LIGHT_INTENSITY`
  - `ATOMIC_SPECTRA`
  - `ABSORPTION_SPECTRUM`
  - `EMISSION_SPECTRUM`
  - `ELECTRON_SPIN_MAGNETIC_MOMENT`
  - `ELECTRON_G_FACTOR`
  - `ATOMIC_NUCLEUS_G_FACTOR`
  - `NUCLEAR_DECAY_CONSTANT`
  - `NUCLEAR_DECAY`

### Step 1.2: Create Definitions in `dictionaries/QuantumMechanicsDictionary.py`

- **Purpose**: To enrich the API responses with user-friendly definitions.
- **Action**: Create `dictionaries/QuantumMechanicsDictionary.py` and define a dictionary named `QuantumMechanicsDict` with a plain-text definition for each calculation.

### Step 1.3: Define Request Schemas in `schemas/QuantumMechanicsSchema.py`

- **Purpose**: To ensure incoming request bodies are valid through Pydantic models.
- **Action**: Create `schemas/QuantumMechanicsSchema.py` and define a Pydantic `BaseModel` class for each endpoint's request body.
- **Schemas to be Created**:
  - `UncertaintyPrincipleRequest`
  - `SchrodingersEquationRequest`
  - `ProbabilityDensityRequest`
  - `TunnelingProbabilityRequest`
  - `BlackBodyRadiationIntensityRequest`
  - `BlackBodyRadiationPowerRequest`
  - `FermiDiracDistributionRequest`
  - `BoseEinsteinDistributionRequest`
  - `WaveParticleDualityRequest`
  - `HeisenbergUncertaintyEnergyLifetimeRequest`
  - `HeisenbergUncertaintyPositionMomentumRequest`
  - `AtomicOrbitalRadiusRequest`
  - `FineStructureConstantRequest`
  - `DeBroglieWavelengthPhotonRequest`
  - `DeBroglieWavelengthParticleRequest`
  - `PlankDistributionRadiationRequest`
  - `PlankDistributionRequest`
  - `PlankLawIntensityRequest`
  - `PlankLawPowerRequest`
  - `EinsteinLightQuantaRequest`
  - `EinsteinLightIntensityRequest`
  - `AtomicSpectraRequest`
  - `AbsorptionSpectrumRequest`
  - `EmissionSpectrumRequest`
  - `ElectronSpinMagneticMomentRequest`
  - `ElectronGFactorRequest`
  - `AtomicNucleusGFactorRequest`
  - `NuclearDecayConstantRequest`
  - `NuclearDecayRequest`

---

## Phase 2: Business Logic Implementation

### Step 2.1: Create `controllers/QuantumMechanicsControllers.py`

- **Purpose**: To house the core business logic.
- **Action**: Create `controllers/QuantumMechanicsControllers.py`. For each endpoint, create a corresponding function that:
    1. Accepts a Pydantic schema object.
    2. Calls the relevant static method from the `QuantumMechanics` class in `libs.phsipy.PhsipyEquations`.
    3. Returns a `GenericResponse` object.

---

## Phase 3: API Endpoint Exposure

### Step 3.1: Create `routes/QuantumMechanicsRoutes.py`

- **Purpose**: To define the API routes and connect them to the controller functions.
- **Action**: Create `routes/QuantumMechanicsRoutes.py`, instantiate an `APIRouter`, and create a `@QuantumMechanics_Router.post(...)` decorator for each controller function.

---

## Phase 4: Application Integration

### Step 4.1: Register the Router in `main.py`

- **Purpose**: To make the new Quantum Mechanics API endpoints live.
- **Action**:
    1. Import the `QuantumMechanics_Router` from `routes.QuantumMechanicsRoutes` into `main.py`.
    2. Use `app.include_router(QuantumMechanics_Router, prefix="/quantum_mechanics")` to register all the defined routes.
