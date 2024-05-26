from fastapi import APIRouter
from Helpers import Constants
from Controllers import NlmControllers
from Classes import NlmClasses
from Classes.GenericResponse import GenericResponse

NLMRouter = APIRouter()

NLM_ROUTE_PARAMS = Constants.ROUTE_PARAMS["NLM"]


@NLMRouter.post(
    "/force", **NLM_ROUTE_PARAMS["FORCE"], response_model=GenericResponse[float]
)
def force(req: NlmClasses.Force):
    return NlmControllers.get_force(req)


@NLMRouter.post(
    "/momentum", **NLM_ROUTE_PARAMS["FORCE"], response_model=GenericResponse[float]
)
def momentum(req: NlmClasses.Momentum):
    return NlmControllers.get_momentum(req)


@NLMRouter.post(
    "/recoil_velocity",
    **NLM_ROUTE_PARAMS["FORCE"],
    response_model=GenericResponse[float]
)
def recoil_velocity(req: NlmClasses.Recoil_Velocity):
    return NlmControllers.get_recoil_velocity(req)
