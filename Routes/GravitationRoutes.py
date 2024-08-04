from fastapi import APIRouter
from Controllers import GravitationControllers
from Schemas.GravitationSchema import *
from Schemas.GenericSchema import GenericResponse

GravitationRouter = APIRouter()


@GravitationRouter.post("/G", response_model=GenericResponse[float])
def get_G(req: G_Request):
    return GravitationControllers.get_G(req)


@GravitationRouter.post("/gpotential", response_model=GenericResponse[float])
def get_g_potential(req: G_Potential_Request):
    return GravitationControllers.get_G_Potential(req)


@GravitationRouter.post("/gindepth", response_model=GenericResponse[float])
def get_g_in_depth(req: G_In_Depth_Request):
    return GravitationControllers.get_g_in_depth(req)


@GravitationRouter.post("/axialvelocity", response_model=GenericResponse[float])
def get_axial_velocity(req: Axial_Velocity_Request):
    return GravitationControllers.get_axial_velocity(req)


@GravitationRouter.post("/gravitationalforce", response_model=GenericResponse[float])
def get_gravitational_force(req: Gravitational_Force_Request):
    return GravitationControllers.get_gravitational_force(req)


@GravitationRouter.post(
    "/gravitationalpotentialenergy", response_model=GenericResponse[float]
)
def get_gravitational_potential_energy(req: Gravitational_Potential_Energy_Request):
    return GravitationControllers.get_gravitational_potential_energy(req)


@GravitationRouter.post(
    "/gravitationalfieldstrength", response_model=GenericResponse[float]
)
def get_gravitational_field_strength(req: Gravitational_Field_Strength_Request):
    return GravitationControllers.get_gravitational_field_strength(req)


@GravitationRouter.post("/escapevelocity", response_model=GenericResponse[float])
def get_escape_velocity(req: Escape_Velocity_Request):
    return GravitationControllers.get_escape_velocity(req)


@GravitationRouter.post("/orbitalvelocity", response_model=GenericResponse[float])
def get_orbital_velocity(req: Orbital_Velocity_Request):
    return GravitationControllers.get_orbital_velocity(req)


@GravitationRouter.post("/periodoforbit", response_model=GenericResponse[float])
@GravitationRouter.post(
    "/gravitationalpotential", response_model=GenericResponse[float]
)
def get_gravitational_potentail(req: Gravitational_Potential_Request):
    return GravitationControllers.get_gravitational_potential(req)


@GravitationRouter.post("/weight", response_model=GenericResponse[float])
def get_weight(req: Weight_Request):
    return GravitationControllers.get_weight(req)


@GravitationRouter.post("/keplersthirdlaw", response_model=GenericResponse[float])
def get_keplers_third_law(req: Keplers_Third_Law_Request):
    return GravitationControllers.get_keplers_third_law(req)
