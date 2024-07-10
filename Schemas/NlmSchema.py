from pydantic import BaseModel


class Force_Request(BaseModel):
    mass: float
    acceleration: float


class Momentum_Request(BaseModel):
    mass: float
    velocity: float


class Recoil_Velocity_Request(BaseModel):
    massofbullet: float
    initialvelocity: float
    massofgun: float
