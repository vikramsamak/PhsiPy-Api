from pydantic import BaseModel


class Force(BaseModel):
    mass: float
    acceleration: float


class Momentum(BaseModel):
    mass: float
    velocity: float


class Recoil_Velocity(BaseModel):
    massofbullet: float
    initialvelocity: float
    massofgun: float
