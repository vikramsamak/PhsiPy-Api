from pydantic import BaseModel


class ForceRequest(BaseModel):
    mass: float
    acceleration: float


class MomentumRequest(BaseModel):
    mass: float
    velocity: float


class Recoil_VelocityRequest(BaseModel):
    massofbullet: float
    initialvelocity: float
    massofgun: float
