from fastapi import APIRouter
from controllers import NlmControllers
from schemas.NlmSchema import *
from schemas.GenericSchema import GenericResponse
from constants import NLMConstants

NLM_Router = APIRouter()

NLM_ROUTE_PARAMS = NLMConstants.NLM_ROUTE_PARAMS


@NLM_Router.post(
    "/force", **NLM_ROUTE_PARAMS["FORCE"], response_model=GenericResponse[float]
)
def calculate_force(req: ForceSchema):
    return NlmControllers.calculate_force(req)


@NLM_Router.post(
    "/momentum", **NLM_ROUTE_PARAMS["MOMENTUM"], response_model=GenericResponse[float]
)
def calculate_momentum(req: MomentumSchema):
    return NlmControllers.calculate_momentum(req)


@NLM_Router.post(
    "/recoil_velocity",
    **NLM_ROUTE_PARAMS["RECOIL_VELOCITY"],
    response_model=GenericResponse[float]
)
def calculate_recoil_velocity(req: RecoilVelocitySchema):
    return NlmControllers.calculate_recoil_velocity(req)
