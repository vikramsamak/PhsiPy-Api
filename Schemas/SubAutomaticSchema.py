from pydantic import BaseModel


class Mass_Energy_Equivalence(BaseModel):
    mass: float


class Binding_Energy(BaseModel):
    mass_parent: float


class De_Broglie_Wavelength(BaseModel):
    momentum: float
    mass: float


class Bohr_radius(BaseModel):
    atomic_number: float


class Energy_Level_Hydrogen(BaseModel):
    n: float


class Radioactive_Decay(BaseModel):
    initial_amount: float
    decay_constant: float
    time: float


class Half_life(BaseModel):
    decay_constant: float
