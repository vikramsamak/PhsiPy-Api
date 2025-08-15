from pydantic import BaseModel


class ForceSchema(BaseModel):
    mass: float
    acceleration: float


class MomentumSchema(BaseModel):
    mass: float
    velocity: float


class RecoilVelocitySchema(BaseModel):
    massofbullet: float
    initialvelocity: float
    massofgun: float
