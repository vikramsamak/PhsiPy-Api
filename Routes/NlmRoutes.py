from fastapi import APIRouter
from Helpers import Constants
from Controllers import NlmControllers
from Classes import NlmClasses

NLMRouter = APIRouter()

NLM_TAGS = [Constants.TAGS["NLM"]]


@NLMRouter.post("/force", tags=NLM_TAGS)
def force(req: NlmClasses.Force):
    return NlmControllers.get_force(req)


@NLMRouter.post("/momentum", tags=NLM_TAGS)
def momentum(req: NlmClasses.Momentum):
    return NlmControllers.get_momentum(req)


@NLMRouter.post("/recoil_velocity", tags=NLM_TAGS)
def recoil_velocity(req: NlmClasses.Recoil_Velocity):
    return NlmControllers.get_recoil_velocity(req)
