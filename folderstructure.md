# Tech Stack

The project is built using Python, likely as a web API, and is configured for deployment on Vercel.

## Core Directories

* `main.py`: The main entry point of the application, responsible for initializing and running the API.
* `constants/`:
  * Contains Python modules defining various physical constants, categorized by domain (e.g., `ElectricityConstants.py`, `GravitationConstants.py`).
* `controllers/`:
  * Houses the business logic for different API functionalities. Each module corresponds to a specific physics domain (e.g., `ElectricityControllers.py`, `NlmControllers.py`).
* `dictionaries/`:
  * Contains data structures or mappings, likely related to the physics domains, used for various calculations or data representations (e.g., `ElectricityDictionary.py`).
* `libs/`:
  * Contains custom libraries or utility modules.
  * `libs/phsipy/`: A dedicated package for core physics functionalities, including:
    * `PhsipyConstants.py`: Additional constants specific to the `phsipy` library.
    * `PhsipyEquations.py`: Implementations of physics equations.
* `routes/`:
  * Defines the API endpoints and maps them to the respective controller functions. Organized by physics domain (e.g., `ElectricityRoutes.py`, `SubAutomaticRoutes.py`).
* `schemas/`:
  * Defines data models for request and response validation, ensuring data integrity and consistency. Categorized by physics domain (e.g., `ElectricitySchema.py`, `GravitationSchema.py`) and includes a `GenericSchema.py` for common data structures.
