from fastapi import APIRouter
from controllers import SubAutomaticControllers
from schemas.SubAutomaticSchema import *
from schemas.GenericSchema import GenericResponse
from constants import SubautomicConstants

SubAutomatic_Router = APIRouter()

SUBAUTOMATIC_PARAMS = SubautomicConstants.SUBAUTOMIC_ROUTE_PARAMS


@SubAutomatic_Router.post(
    "/mass_energy_equivalence",
    **SUBAUTOMATIC_PARAMS["MASS_ENERGY_EQUIVALENCE"],
    response_model=GenericResponse[float]
)
def calculate_mass_energy_equivalence(req: Mass_Energy_Equivalence_Request):
    return SubAutomaticControllers.calculate_mass_energy_equivalence(req)


@SubAutomatic_Router.post(
    "/binding_energy",
    **SUBAUTOMATIC_PARAMS["BINDING_ENERGY"],
    response_model=GenericResponse[float]
)
def calculate_binding_energy(req: Binding_Energy_Request):
    return SubAutomaticControllers.calculate_binding_energy(req)


@SubAutomatic_Router.post(
    "/de_broglie_wavelength",
    **SUBAUTOMATIC_PARAMS["DE_BROGILE_WAVELENGTH"],
    response_model=GenericResponse[float]
)
def calculate_de_broglie_wavelength(req: De_Broglie_Wavelength_Request):
    return SubAutomaticControllers.calculate_de_broglie_wavelength(req)


@SubAutomatic_Router.post(
    "/bohr_radius",
    **SUBAUTOMATIC_PARAMS["BOHR_RADIUS"],
    response_model=GenericResponse[float]
)
def calculate_bohr_radius(req: Bohr_radius_Request):
    return SubAutomaticControllers.calculate_bohr_radius(req)


@SubAutomatic_Router.post(
    "/energy_level_hydrogen",
    **SUBAUTOMATIC_PARAMS["ENERGY_LEVEL_HYDROGEN"],
    response_model=GenericResponse[float]
)
def calculate_energy_level_hydrogen(req: Energy_Level_Hydrogen_Request):
    return SubAutomaticControllers.calculate_energy_level_hydrogen(req)


@SubAutomatic_Router.post(
    "/radioactive_decay",
    **SUBAUTOMATIC_PARAMS["RADIOACTIVE_DECAY"],
    response_model=GenericResponse[float]
)
def calculate_radioactive_decay(req: Radioactive_Decay_Request):
    return SubAutomaticControllers.calculate_radioactive_decay(req)


@SubAutomatic_Router.post(
    "/half_life",
    **SUBAUTOMATIC_PARAMS["HALF_LIFE"],
    response_model=GenericResponse[float]
)
def calculate_half_life(req: Half_lifeRequest):
    return SubAutomaticControllers.calculate_half_life(req)
