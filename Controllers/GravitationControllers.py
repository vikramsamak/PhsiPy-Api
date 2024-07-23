from Libs.PhsiPy.PhsipyEquations import Gravitation
from Schemas.GravitationSchema import *
from Schemas.GenericSchema import GenericResponse


def get_G(req: G_Request) -> GenericResponse[float]:
    return ""


def get_G_Potential(req: G_Potential_Request) -> GenericResponse[float]:
    return ""


def get_g_in_depth(req: G_In_Depth_Request) -> GenericResponse[float]:
    return ""


def get_axial_velocity(req: Axial_Velocity_Request) -> GenericResponse[float]:
    return ""


def get_gravitational_force(req: Gravitational_Force_Request) -> GenericResponse[float]:
    return ""


def get_gravitational_potential_energy(
    req: Gravitational_Potential_Energy_Request,
) -> GenericResponse[float]:
    return ""


def get_gravitational_field_strength(
    req: Gravitational_Field_Strength_Request,
) -> GenericResponse[float]:
    return ""


def get_escape_velocity(req: Escape_Velocity_Request) -> GenericResponse[float]:
    return ""


def get_orbital_velocity(req: Orbital_Velocity_Request) -> GenericResponse[float]:
    return ""


def get_period_of_orbit(req: Period_Of_Orbit_Request) -> GenericResponse[float]:
    return ""


def get_gravitational_potential(
    req: Gravitational_Potential_Request,
) -> GenericResponse[float]:
    return ""


def get_weight(req: Weight_Request) -> GenericResponse[float]:
    return ""


def get_gravitational_acceleration(
    req: Gravitational_Acceleration_Request,
) -> GenericResponse[float]:
    return ""


def get_keplers_third_law(req: Keplers_Third_Law_Request) -> GenericResponse[float]:
    return ""
