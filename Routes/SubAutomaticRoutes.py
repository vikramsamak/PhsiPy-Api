from fastapi import APIRouter
from Controllers import SubAutomaticControllers
from Schemas.SubAutomaticSchema import *
from Helpers import Constants

SubAutomatic_Router = APIRouter()

SUBAUTOMATIC_TAGS = [Constants.TAGS["SUBAUTOMATIC"]]


@SubAutomatic_Router.post("/mass_energy_equivalence", tags=SUBAUTOMATIC_TAGS)
def mass_energy_equivalence(req: Mass_Energy_EquivalenceRequest):
    return SubAutomaticControllers.get_mass_energy_equivalence(req)


@SubAutomatic_Router.post("/binding_energy", tags=SUBAUTOMATIC_TAGS)
def binding_energy(req: Mass_Energy_EquivalenceRequest):
    return SubAutomaticControllers.get_binding_energy(req)


@SubAutomatic_Router.post("/de_broglie_wavelength", tags=SUBAUTOMATIC_TAGS)
def de_broglie_wavelength(req: De_Broglie_WavelengthRequest):
    return SubAutomaticControllers.get_de_broglie_wavelength(req)


@SubAutomatic_Router.post("/bohr_radius", tags=SUBAUTOMATIC_TAGS)
def bohr_radius(req: Bohr_radiusRequest):
    return SubAutomaticControllers.get_bohr_radius(req)


@SubAutomatic_Router.post("/energy_level_hydrogen", tags=SUBAUTOMATIC_TAGS)
def energy_level_hydrogen(req: Energy_Level_HydrogenRequest):
    return SubAutomaticControllers.get_energy_level_hydrogen(req)


@SubAutomatic_Router.post("/radioactive_decay", tags=SUBAUTOMATIC_TAGS)
def radioactive_decay(req: Radioactive_DecayRequest):
    return SubAutomaticControllers.get_radioactive_decay(req)


@SubAutomatic_Router.post("/half_life", tags=SUBAUTOMATIC_TAGS)
def half_life(req: Half_lifeRequest):
    return SubAutomaticControllers.get_half_life(req)
