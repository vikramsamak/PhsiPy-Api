from pydantic import BaseModel


class Force_Electrostatics(BaseModel):
    q1: float
    q2: float
    r: float
