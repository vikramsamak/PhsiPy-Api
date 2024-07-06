from pydantic import BaseModel


class Mass_Energy_EquivalenceRequest(BaseModel):
    mass: float


class Binding_EnergyRequest(BaseModel):
    mass_parent: float


class De_Broglie_WavelengthRequest(BaseModel):
    momentum: float
    mass: float


class Bohr_radiusRequest(BaseModel):
    atomic_number: float


class Energy_Level_HydrogenRequest(BaseModel):
    n: float


class Radioactive_DecayRequest(BaseModel):
    initial_amount: float
    decay_constant: float
    time: float


class Half_lifeRequest(BaseModel):
    decay_constant: float
