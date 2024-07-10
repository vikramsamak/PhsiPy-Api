from Dictionaries import NlmDictionary
from Schemas.NlmSchema import *
from Schemas.GenericSchema import GenericResponse
from Libs.PhsiPy.PhsipyEquations import Nlm


def get_force(req: Force_Request) -> GenericResponse[float]:
    force = Nlm.force(req.mass, req.acceleration)
    return GenericResponse(
        Definition=NlmDictionary.NlmDict["force"],
        Given={"Mass": req.mass, "Acceleration": req.acceleration},
        Result=force,
    )


def get_momentum(req: Momentum_Request) -> GenericResponse[float]:
    momentum = Nlm.momentum(req.mass, req.velocity)
    return GenericResponse(
        Definition=NlmDictionary.NlmDict["momentum"],
        Given={"Mass": req.mass, "Velocity": req.velocity},
        Result=momentum,
    )


def get_recoil_velocity(
    req: Recoil_Velocity_Request,
) -> GenericResponse[float]:
    recoil_velocity = Nlm.recoil_velocity(
        req.massofbullet, req.massofgun, req.initialvelocity
    )
    return GenericResponse(
        Definition=NlmDictionary.NlmDict["recoil_velocity"],
        Given={
            "Mass Of Bullet": req.massofbullet,
            "Mass Of Gun": req.massofgun,
            "Intial Velocity": req.initialvelocity,
        },
        Result=recoil_velocity,
    )
