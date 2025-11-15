from pydantic import BaseModel


class MassEnergyEquivalenceSchema(BaseModel):
    mass: float


class BindingEnergySchema(BaseModel):
    mass_parent: float
    mass_daughters: list[float]


class DeBroglieWavelengthSchema(BaseModel):
    momentum: float
    mass: float


class BohrRadiusSchema(BaseModel):
    atomic_number: float


class EnergyLevelHydrogenSchema(BaseModel):
    n: float


class RadioactiveDecaySchema(BaseModel):
    initial_amount: float
    decay_constant: float
    time: float


class HalfLifeSchema(BaseModel):
    decay_constant: float
