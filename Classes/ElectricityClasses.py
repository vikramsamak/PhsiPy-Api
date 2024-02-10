from pydantic import BaseModel


class Force_Electrostatics(BaseModel):
    q1: float
    q2: float
    resistance: float


class Resistance(BaseModel):
    voltage: float
    current: float


class Current(BaseModel):
    voltage: float
    resistance: float


class Voltage(BaseModel):
    current: float
    resistance: float


class Power(BaseModel):
    voltage: float
    current: float


class Ohms_Law(BaseModel):
    voltage: float
    resistance: float
