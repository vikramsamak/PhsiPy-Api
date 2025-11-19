from pydantic import BaseModel
from typing import List

class ErrorMulDivSchema(BaseModel):
    a: float
    b: float
    c: float
    d: float

class ErrorAddSubSchema(BaseModel):
    a: float
    b: float

class PercentageErrorSchema(BaseModel):
    M: float
    E: float

class AbsoluteErrorSchema(BaseModel):
    a: List[float]
    n: int

class MeanAbsoluteErrorSchema(BaseModel):
    a: List[float]
    n: int
