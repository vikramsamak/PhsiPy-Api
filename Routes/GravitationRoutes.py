from fastapi import APIRouter
from Controllers import GravitationControllers
from Schemas.GravitationSchema import *
from Schemas.GenericSchema import GenericResponse
from Constants import GravitationConstants

Gravitation_Router = APIRouter()

GRAVIATATION_ROUTE_PARAMS = GravitationConstants.GRAVITATION_ROUTE_PARAMS


@Gravitation_Router.post(
    "/G", **GRAVIATATION_ROUTE_PARAMS["G"], response_model=GenericResponse[float]
)
def get_G(req: G_Request):
    return GravitationControllers.get_G(req)


@Gravitation_Router.post(
    "/gpotential",
    **GRAVIATATION_ROUTE_PARAMS["G_POTENTIAL"],
    response_model=GenericResponse[float]
)
def get_g_potential(req: G_Potential_Request):
    return GravitationControllers.get_G_Potential(req)


@Gravitation_Router.post(
    "/gindepth",
    **GRAVIATATION_ROUTE_PARAMS["G_IN_DEPTH"],
    response_model=GenericResponse[float]
)
def get_g_in_depth(req: G_In_Depth_Request):
    return GravitationControllers.get_g_in_depth(req)


@Gravitation_Router.post(
    "/axialvelocity",
    **GRAVIATATION_ROUTE_PARAMS["AXIAL_VELOCITY"],
    response_model=GenericResponse[float]
)
def get_axial_velocity(req: Axial_Velocity_Request):
    return GravitationControllers.get_axial_velocity(req)


@Gravitation_Router.post(
    "/gravitationalforce",
    **GRAVIATATION_ROUTE_PARAMS["GRAVITATIONAL_FORCE"],
    response_model=GenericResponse[float]
)
def get_gravitational_force(req: Gravitational_Force_Request):
    return GravitationControllers.get_gravitational_force(req)


@Gravitation_Router.post(
    "/gravitationalpotentialenergy",
    **GRAVIATATION_ROUTE_PARAMS["GRAVITATIONAL_POTENTIAL_ENERGY"],
    response_model=GenericResponse[float]
)
def get_gravitational_potential_energy(req: Gravitational_Potential_Energy_Request):
    return GravitationControllers.get_gravitational_potential_energy(req)


@Gravitation_Router.post(
    "/gravitationalfieldstrength",
    **GRAVIATATION_ROUTE_PARAMS["GRAVITATIONAL_FIELD_STRENGTH"],
    response_model=GenericResponse[float]
)
def get_gravitational_field_strength(req: Gravitational_Field_Strength_Request):
    return GravitationControllers.get_gravitational_field_strength(req)


@Gravitation_Router.post(
    "/escapevelocity",
    **GRAVIATATION_ROUTE_PARAMS["ESCAPE_VELOCITY"],
    response_model=GenericResponse[float]
)
def get_escape_velocity(req: Escape_Velocity_Request):
    return GravitationControllers.get_escape_velocity(req)


@Gravitation_Router.post(
    "/orbitalvelocity",
    **GRAVIATATION_ROUTE_PARAMS["ORBITAL_VELOCITY"],
    response_model=GenericResponse[float]
)
def get_orbital_velocity(req: Orbital_Velocity_Request):
    return GravitationControllers.get_orbital_velocity(req)


@Gravitation_Router.post(
    "/periodoforbit",
    **GRAVIATATION_ROUTE_PARAMS["PERIOD_OF_ORBIT"],
    response_model=GenericResponse[float]
)
def get_period_of_orbit(req: Period_Of_Orbit_Request):
    return GravitationControllers.get_period_of_orbit(req)


@Gravitation_Router.post(
    "/gravitationalpotential",
    **GRAVIATATION_ROUTE_PARAMS["GRAVITATIONAL_POTENTIAL"],
    response_model=GenericResponse[float]
)
def get_gravitational_potentail(req: Gravitational_Potential_Request):
    return GravitationControllers.get_gravitational_potential(req)


@Gravitation_Router.post(
    "/weight",
    **GRAVIATATION_ROUTE_PARAMS["WEIGHT"],
    response_model=GenericResponse[float]
)
def get_weight(req: Weight_Request):
    return GravitationControllers.get_weight(req)


@Gravitation_Router.post(
    "/keplersthirdlaw",
    **GRAVIATATION_ROUTE_PARAMS["KEPLERS_THIRD_LAW"],
    response_model=GenericResponse[float]
)
def get_keplers_third_law(req: Keplers_Third_Law_Request):
    return GravitationControllers.get_keplers_third_law(req)
