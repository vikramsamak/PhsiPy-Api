from pydantic import BaseModel


class ForceElectrostaticsSchema(BaseModel):
    q1: float
    q2: float
    resistance: float


class ResistanceSchema(BaseModel):
    voltage: float
    current: float


class CurrentSchema(BaseModel):
    voltage: float
    resistance: float


class VoltageSchema(BaseModel):
    current: float
    resistance: float


class PowerSchema(BaseModel):
    voltage: float
    current: float
