from fastapi import APIRouter
from Helpers import Constants
from Controllers import NlmControllers
from Schemas.NlmSchema import *
from Schemas.GenericSchema import GenericResponse

NLMRouter = APIRouter()

NLM_ROUTE_PARAMS = Constants.ROUTE_PARAMS["NLM"]


@NLMRouter.post(
    "/force", **NLM_ROUTE_PARAMS["FORCE"], response_model=GenericResponse[float]
)
def force(req: ForceRequest):
    return NlmControllers.get_force(req)


@NLMRouter.post(
    "/momentum", **NLM_ROUTE_PARAMS["MOMENTUM"], response_model=GenericResponse[float]
)
def momentum(req: MomentumRequest):
    return NlmControllers.get_momentum(req)


@NLMRouter.post(
    "/recoil_velocity",
    **NLM_ROUTE_PARAMS["RECOIL_VELOCITY"],
    response_model=GenericResponse[float]
)
def recoil_velocity(req: Recoil_VelocityRequest):
    return NlmControllers.get_recoil_velocity(req)
