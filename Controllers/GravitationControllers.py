from Libs.PhsiPy.PhsipyEquations import Gravitation
from Schemas.GravitationSchema import *
from Schemas.GenericSchema import GenericResponse
from Dictionaries import GravitationDictionary


def get_G(req: G_Request) -> GenericResponse[float]:
    g = Gravitation.G(req.m1, req.m2, req.r)
    return GenericResponse(
        Definition=GravitationDictionary.GravitationDict["G"],
        Given={"M1": req.m1, "M2": req.m2, "R": req.r},
        Result=g,
    )


def get_G_Potential(req: G_Potential_Request) -> GenericResponse[float]:
    g_potential = Gravitation.G_Potential(req.M, req.r)
    return GenericResponse(
        Definition=GravitationDictionary.GravitationDict["g_potential"],
        Given={"M": req.M, "r": req.r},
        Result=g_potential,
    )


def get_g_in_depth(req: G_In_Depth_Request) -> GenericResponse[float]:
    g_in_depth = Gravitation.g_in_depth(req.depth)
    return GenericResponse(
        Definition=GravitationDictionary.GravitationDict["g_in_depth"],
        Given={"Depth": req.depth},
        Result=g_in_depth,
    )


def get_axial_velocity(req: Axial_Velocity_Request) -> GenericResponse[float]:
    axial_velocity = Gravitation.axial_velocity(req.area_swept, req.time)
    return GenericResponse(
        Definition=GravitationDictionary.GravitationDict["axial_velocity"],
        Given={"Area Swept": req.area_swept, "Time": req.time},
        Result=axial_velocity,
    )


def get_gravitational_force(req: Gravitational_Force_Request) -> GenericResponse[float]:
    gravitational_force = Gravitation.gravitational_force(
        req.mass1, req.mass2, req.distance
    )
    return GenericResponse(
        Definition=GravitationDictionary.GravitationDict["gravitational_force"],
        Given={"Mass 1": req.mass1, "Mass 2": req.mass2, "Distance": req.distance},
        Result=gravitational_force,
    )


def get_gravitational_potential_energy(
    req: Gravitational_Potential_Energy_Request,
) -> GenericResponse[float]:
    gravitational_potential_energy = Gravitation.gravitational_potential_energy(
        req.mass1, req.mass2, req.distance
    )
    return GenericResponse(
        Definition=GravitationDictionary.GravitationDict[
            "gravitational_potential_energy"
        ],
        Given={"Mass 1": req.mass1, "Mass 2": req.mass2, "Distance": req.distance},
        Result=gravitational_potential_energy,
    )


def get_gravitational_field_strength(
    req: Gravitational_Field_Strength_Request,
) -> GenericResponse[float]:
    gravitational_field_strength = Gravitation.gravitational_field_strength(
        req.mass, req.distance
    )
    return GenericResponse(
        Definition=GravitationDictionary.GravitationDict[
            "gravitational_field_strength"
        ],
        Given={"Mass": req.mass, "Distance": req.distance},
        Result=gravitational_field_strength,
    )


def get_escape_velocity(req: Escape_Velocity_Request) -> GenericResponse[float]:
    escape_velocity = Gravitation.escape_velocity(req.mass, req.radius)
    return GenericResponse(
        Definition=GravitationDictionary.GravitationDict["escape_velocity"],
        Given={"Mass": req.mass, "Radius": req.radius},
        Result=escape_velocity,
    )


def get_orbital_velocity(req: Orbital_Velocity_Request) -> GenericResponse[float]:
    orbital_velocity = Gravitation.orbital_velocity(req.mass, req.radius)
    return GenericResponse(
        Definition=GravitationDictionary.GravitationDict["orbital_velocity"],
        Given={"Mass": req.mass, "Radius": req.radius},
        Result=orbital_velocity,
    )


def get_period_of_orbit(req: Period_Of_Orbit_Request) -> GenericResponse[float]:
    period_of_orbit = Gravitation.period_of_orbit(req.mass, req.radius)
    return GenericResponse(
        Definition=GravitationDictionary.GravitationDict["period_of_orbit"],
        Given={"Mass": req.mass, "Radius": req.radius},
        Result=period_of_orbit,
    )


def get_gravitational_potential(
    req: Gravitational_Potential_Request,
) -> GenericResponse[float]:
    gravitational_potential = Gravitation.gravitational_potential(
        req.mass, req.distance
    )
    return GenericResponse(
        Definition=GravitationDictionary.GravitationDict["gravitational_potential"],
        Given={"Mass": req.mass, "Distance": req.distance},
        Result=gravitational_potential,
    )


def get_weight(req: Weight_Request) -> GenericResponse[float]:
    weight = Gravitation.weight(req.mass, req.acceleration_due_to_gravity)
    return GenericResponse(
        Definition=GravitationDictionary.GravitationDict["weight"],
        Given={
            "Mass": req.mass,
            "Acceleration due to gravity": req.acceleration_due_to_gravity,
        },
        Result=weight,
    )


def get_gravitational_acceleration(
    req: Gravitational_Acceleration_Request,
) -> GenericResponse[float]:
    gravitational_acceleration = Gravitation.gravitational_acceleration(
        req.mass, req.distance
    )
    return GenericResponse(
        Definition=GravitationDictionary.GravitationDict["gravitational_acceleration"],
        Given={"Mass": req.mass, "Distance": req.distance},
        Result=gravitational_acceleration,
    )


def get_keplers_third_law(req: Keplers_Third_Law_Request) -> GenericResponse[float]:
    keplers_third_law = Gravitation.keplers_third_law(req.period, req.semi_major_axis)
    return GenericResponse(
        Definition=GravitationDictionary.GravitationDict["keplers_third_law"],
        Given={"Period": req.period, "Semi Major Axis": req.semi_major_axis},
        Result=keplers_third_law,
    )
