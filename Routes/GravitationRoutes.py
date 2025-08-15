from fastapi import APIRouter
from controllers import GravitationControllers
from schemas.GravitationSchema import *
from schemas.GenericSchema import GenericResponse
from constants import GravitationConstants

Gravitation_Router = APIRouter()

GRAVIATATION_ROUTE_PARAMS = GravitationConstants.GRAVITATION_ROUTE_PARAMS


@Gravitation_Router.post(
    "/G", **GRAVIATATION_ROUTE_PARAMS["G"], response_model=GenericResponse[float]
)
def calculate_g(req: GravitationalForceSchema):
    return GravitationControllers.calculate_g(req)


@Gravitation_Router.post(
    "/gpotential",
    **GRAVIATATION_ROUTE_PARAMS["G_POTENTIAL"],
    response_model=GenericResponse[float]
)
def calculate_g_potential(req: GravitationalPotentialSchema):
    return GravitationControllers.calculate_g_potential(req)


@Gravitation_Router.post(
    "/gindepth",
    **GRAVIATATION_ROUTE_PARAMS["G_IN_DEPTH"],
    response_model=GenericResponse[float]
)
def calculate_g_in_depth(req: GravitationalFieldInDepthSchema):
    return GravitationControllers.calculate_g_in_depth(req)


@Gravitation_Router.post(
    "/axialvelocity",
    **GRAVIATATION_ROUTE_PARAMS["AXIAL_VELOCITY"],
    response_model=GenericResponse[float]
)
def calculate_axial_velocity(req: AxialVelocitySchema):
    return GravitationControllers.calculate_axial_velocity(req)


@Gravitation_Router.post(
    "/gravitationalforce",
    **GRAVIATATION_ROUTE_PARAMS["GRAVITATIONAL_FORCE"],
    response_model=GenericResponse[float]
)
def calculate_gravitational_force(req: GravitationalForceSchema2):
    return GravitationControllers.calculate_gravitational_force(req)


@Gravitation_Router.post(
    "/gravitationalpotentialenergy",
    **GRAVIATATION_ROUTE_PARAMS["GRAVITATIONAL_POTENTIAL_ENERGY"],
    response_model=GenericResponse[float]
)
def calculate_gravitational_potential_energy(
    req: GravitationalPotentialEnergySchema,
):
    return GravitationControllers.calculate_gravitational_potential_energy(req)


@Gravitation_Router.post(
    "/gravitationalfieldstrength",
    **GRAVIATATION_ROUTE_PARAMS["GRAVITATIONAL_FIELD_STRENGTH"],
    response_model=GenericResponse[float]
)
def calculate_gravitational_field_strength(
    req: GravitationalFieldStrengthSchema,
):
    return GravitationControllers.calculate_gravitational_field_strength(req)


@Gravitation_Router.post(
    "/escapevelocity",
    **GRAVIATATION_ROUTE_PARAMS["ESCAPE_VELOCITY"],
    response_model=GenericResponse[float]
)
def calculate_escape_velocity(req: EscapeVelocitySchema):
    return GravitationControllers.calculate_escape_velocity(req)


@Gravitation_Router.post(
    "/orbitalvelocity",
    **GRAVIATATION_ROUTE_PARAMS["ORBITAL_VELOCITY"],
    response_model=GenericResponse[float]
)
def calculate_orbital_velocity(req: OrbitalVelocitySchema):
    return GravitationControllers.calculate_orbital_velocity(req)


@Gravitation_Router.post(
    "/periodoforbit",
    **GRAVIATATION_ROUTE_PARAMS["PERIOD_OF_ORBIT"],
    response_model=GenericResponse[float]
)
def calculate_period_of_orbit(req: PeriodOfOrbitSchema):
    return GravitationControllers.calculate_period_of_orbit(req)


@Gravitation_Router.post(
    "/gravitationalpotential",
    **GRAVIATATION_ROUTE_PARAMS["GRAVITATIONAL_POTENTIAL"],
    response_model=GenericResponse[float]
)
def calculate_gravitational_potential(req: GravitationalPotentialSchema2):
    return GravitationControllers.calculate_gravitational_potential(req)


@Gravitation_Router.post(
    "/weight",
    **GRAVIATATION_ROUTE_PARAMS["WEIGHT"],
    response_model=GenericResponse[float]
)
def calculate_weight(req: WeightSchema):
    return GravitationControllers.calculate_weight(req)


@Gravitation_Router.post(
    "/keplersthirdlaw",
    **GRAVIATATION_ROUTE_PARAMS["KEPLERS_THIRD_LAW"],
    response_model=GenericResponse[float]
)
def calculate_keplers_third_law(req: KeplersThirdLawSchema):
    return GravitationControllers.calculate_keplers_third_law(req)
