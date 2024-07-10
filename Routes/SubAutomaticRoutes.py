from fastapi import APIRouter
from Controllers import SubAutomaticControllers
from Schemas.SubAutomaticSchema import *
from Helpers import Constants
from Schemas.GenericSchema import GenericResponse

SubAutomatic_Router = APIRouter()

SUBAUTOMATIC_PARAMS = Constants.ROUTE_PARAMS["SUBAUTOMATIC"]


@SubAutomatic_Router.post(
    "/mass_energy_equivalence",
    **SUBAUTOMATIC_PARAMS["MASS_ENERGY_EQUIVALENCE"],
    response_model=GenericResponse[float]
)
def mass_energy_equivalence(req: Mass_Energy_EquivalenceRequest):
    return SubAutomaticControllers.get_mass_energy_equivalence(req)


@SubAutomatic_Router.post(
    "/binding_energy",
    **SUBAUTOMATIC_PARAMS["BINDING_ENERGY"],
    response_model=GenericResponse[float]
)
def binding_energy(req: Binding_EnergyRequest):
    return SubAutomaticControllers.get_binding_energy(req)


@SubAutomatic_Router.post(
    "/de_broglie_wavelength",
    **SUBAUTOMATIC_PARAMS["DE_BROGILE_WAVELENGTH"],
    response_model=GenericResponse[float]
)
def de_broglie_wavelength(req: De_Broglie_WavelengthRequest):
    return SubAutomaticControllers.get_de_broglie_wavelength(req)


@SubAutomatic_Router.post(
    "/bohr_radius",
    **SUBAUTOMATIC_PARAMS["BOHR_RADIUS"],
    response_model=GenericResponse[float]
)
def bohr_radius(req: Bohr_radiusRequest):
    return SubAutomaticControllers.get_bohr_radius(req)


@SubAutomatic_Router.post(
    "/energy_level_hydrogen",
    **SUBAUTOMATIC_PARAMS["ENERGY_LEVEL_HYDROGEN"],
    response_model=GenericResponse[float]
)
def energy_level_hydrogen(req: Energy_Level_HydrogenRequest):
    return SubAutomaticControllers.get_energy_level_hydrogen(req)


@SubAutomatic_Router.post(
    "/radioactive_decay",
    **SUBAUTOMATIC_PARAMS["RADIOACTIVE_DECAY"],
    response_model=GenericResponse[float]
)
def radioactive_decay(req: Radioactive_DecayRequest):
    return SubAutomaticControllers.get_radioactive_decay(req)


@SubAutomatic_Router.post(
    "/half_life",
    **SUBAUTOMATIC_PARAMS["HALF_LIFE"],
    response_model=GenericResponse[float]
)
def half_life(req: Half_lifeRequest):
    return SubAutomaticControllers.get_half_life(req)
