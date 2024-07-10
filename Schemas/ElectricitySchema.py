from pydantic import BaseModel


class Force_Electrostatics_Request(BaseModel):
    q1: float
    q2: float
    resistance: float


class Resistance_Request(BaseModel):
    voltage: float
    current: float


class Current_Request(BaseModel):
    voltage: float
    resistance: float


class Voltage_Request(BaseModel):
    current: float
    resistance: float


class Power_Request(BaseModel):
    voltage: float
    current: float


