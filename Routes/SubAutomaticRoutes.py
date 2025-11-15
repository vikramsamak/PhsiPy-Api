from fastapi import APIRouter
from controllers import SubAutomaticControllers
from schemas.SubAutomaticSchema import *
from schemas.GenericSchema import GenericResponse
from constants import SubautomicConstants

SubAutomatic_Router = APIRouter(tags=["Subatomic"])

SUBAUTOMATIC_PARAMS = SubautomicConstants.SUBAUTOMIC_ROUTE_PARAMS


@SubAutomatic_Router.post(
    "/energy/mass-equivalence",
    **SUBAUTOMATIC_PARAMS["MASS_ENERGY_EQUIVALENCE"],
    response_model=GenericResponse[float]
)
def calculate_mass_energy_equivalence(req: MassEnergyEquivalenceSchema):
    return SubAutomaticControllers.calculate_mass_energy_equivalence(req)


@SubAutomatic_Router.post(
    "/energy/binding",
    **SUBAUTOMATIC_PARAMS["BINDING_ENERGY"],
    response_model=GenericResponse[float]
)
def calculate_binding_energy(req: BindingEnergySchema):
    return SubAutomaticControllers.calculate_binding_energy(req)


@SubAutomatic_Router.post(
    "/quantum/de-broglie-wavelength",
    **SUBAUTOMATIC_PARAMS["DE_BROGILE_WAVELENGTH"],
    response_model=GenericResponse[float]
)
def calculate_de_broglie_wavelength(req: DeBroglieWavelengthSchema):
    return SubAutomaticControllers.calculate_de_broglie_wavelength(req)


@SubAutomatic_Router.post(
    "/quantum/bohr-radius",
    **SUBAUTOMATIC_PARAMS["BOHR_RADIUS"],
    response_model=GenericResponse[float]
)
def calculate_bohr_radius(req: BohrRadiusSchema):
    return SubAutomaticControllers.calculate_bohr_radius(req)


@SubAutomatic_Router.post(
    "/quantum/energy-level-hydrogen",
    **SUBAUTOMATIC_PARAMS["ENERGY_LEVEL_HYDROGEN"],
    response_model=GenericResponse[float]
)
def calculate_energy_level_hydrogen(req: EnergyLevelHydrogenSchema):
    return SubAutomaticControllers.calculate_energy_level_hydrogen(req)


@SubAutomatic_Router.post(
    "/radioactivity/decay",
    **SUBAUTOMATIC_PARAMS["RADIOACTIVE_DECAY"],
    response_model=GenericResponse[float]
)
def calculate_radioactive_decay(req: RadioactiveDecaySchema):
    return SubAutomaticControllers.calculate_radioactive_decay(req)


@SubAutomatic_Router.post(
    "/radioactivity/half-life",
    **SUBAUTOMATIC_PARAMS["HALF_LIFE"],
    response_model=GenericResponse[float]
)
def calculate_half_life(req: HalfLifeSchema):
    return SubAutomaticControllers.calculate_half_life(req)
