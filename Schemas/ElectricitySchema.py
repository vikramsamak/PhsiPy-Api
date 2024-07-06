from pydantic import BaseModel


class Force_ElectrostaticsRequest(BaseModel):
    q1: float
    q2: float
    resistance: float


class ResistanceRequest(BaseModel):
    voltage: float
    current: float


class CurrentRequest(BaseModel):
    voltage: float
    resistance: float


class VoltageRequest(BaseModel):
    current: float
    resistance: float


class PowerRequest(BaseModel):
    voltage: float
    current: float


