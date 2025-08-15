from pydantic import BaseModel


class VelocitySchema(BaseModel):
    initial_velocity: float
    acceleration: float
    time: float


class DisplacementSchema(BaseModel):
    initial_velocity: float
    acceleration: float
    time: float


class AccelerationSchema(BaseModel):
    final_velocity: float
    initial_velocity: float
    time: float


class UniformAcceleratedMotionSchema(BaseModel):
    initial_velocity: float
    time: float
    acceleration: float


class ForceSchema(BaseModel):
    mass: float
    acceleration: float


class WorkSchema(BaseModel):
    force: float
    displacement: float
    angle: float = 0


class KineticEnergySchema(BaseModel):
    mass: float
    velocity: float


class PotentialEnergySchema(BaseModel):
    mass: float
    height: float
    gravitational_field_strength: float


class PowerSchema(BaseModel):
    work: float
    time: float


class MomentumSchema(BaseModel):
    mass: float
    velocity: float


class ImpulseSchema(BaseModel):
    force: float
    time: float


class CircularVelocitySchema(BaseModel):
    radius: float
    period: float


class CentripetalAccelerationSchema(BaseModel):
    radius: float
    velocity: float


class TorqueSchema(BaseModel):
    force: float
    lever_arm: float


class AngularVelocitySchema(BaseModel):
    angular_displacement: float
    time: float


class AngularAccelerationSchema(BaseModel):
    angular_velocity: float
    time: float
