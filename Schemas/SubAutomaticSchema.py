from pydantic import BaseModel


class Mass_Energy_Equivalence_Request(BaseModel):
    mass: float


class Binding_Energy_Request(BaseModel):
    mass_parent: float
    mass_daughters: list[float]


class De_Broglie_Wavelength_Request(BaseModel):
    momentum: float
    mass: float


class Bohr_radius_Request(BaseModel):
    atomic_number: float


class Energy_Level_Hydrogen_Request(BaseModel):
    n: float


class Radioactive_Decay_Request(BaseModel):
    initial_amount: float
    decay_constant: float
    time: float


class Half_lifeRequest(BaseModel):
    decay_constant: float
