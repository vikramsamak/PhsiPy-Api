from pydantic import BaseModel


class GravitationalForceSchema(BaseModel):
    m1: float
    m2: float
    r: float


class GravitationalPotentialSchema(BaseModel):
    M: float
    r: float


class GravitationalFieldInDepthSchema(BaseModel):
    depth: float


class AxialVelocitySchema(BaseModel):
    area_swept: float
    time: float


class GravitationalForceSchema2(BaseModel):
    mass1: float
    mass2: float
    distance: float


class GravitationalPotentialEnergySchema(BaseModel):
    mass1: float
    mass2: float
    distance: float


class GravitationalFieldStrengthSchema(BaseModel):
    mass: float
    distance: float


class EscapeVelocitySchema(BaseModel):
    mass: float
    radius: float


class OrbitalVelocitySchema(BaseModel):
    mass: float
    radius: float


class PeriodOfOrbitSchema(BaseModel):
    mass: float
    radius: float


class GravitationalPotentialSchema2(BaseModel):
    mass: float
    distance: float


class WeightSchema(BaseModel):
    mass: float
    acceleration_due_to_gravity: float


class GravitationalAccelerationSchema(BaseModel):
    mass: float
    distance: float


class KeplersThirdLawSchema(BaseModel):
    period: float
    semi_major_axis: float
