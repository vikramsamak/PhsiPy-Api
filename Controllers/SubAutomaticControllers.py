from Dictionaries import SubAutomaticDictionary
from Schemas.SubAutomaticSchema import *
from Schemas.GenericSchema import GenericResponse
from Libs.PhsiPy.PhsipyEquations import Subatomic


def get_mass_energy_equivalence(
    req: Mass_Energy_EquivalenceRequest,
) -> GenericResponse[float]:
    energy_equivalence = Subatomic.mass_energy_equivalence(req.mass)

    return GenericResponse(
        Definition=SubAutomaticDictionary.SubAtomicDict["mass_energy_equivalence"],
        Given={"Mass": req.mass},
        Result=energy_equivalence,
    )


def get_binding_energy(req: Binding_EnergyRequest) -> GenericResponse[float]:
    return {"definition": SubAutomaticDictionary.SubAtomicDict["binding_energy"]}


def get_de_broglie_wavelength(
    req: De_Broglie_WavelengthRequest,
) -> GenericResponse[float]:
    return {"definition": SubAutomaticDictionary.SubAtomicDict["de_broglie_wavelength"]}


def get_bohr_radius(req: Bohr_radiusRequest) -> GenericResponse[float]:
    return {"definition": SubAutomaticDictionary.SubAtomicDict["bohr_radius"]}


def get_energy_level_hydrogen(
    req: Energy_Level_HydrogenRequest,
) -> GenericResponse[float]:
    return {"definition": SubAutomaticDictionary.SubAtomicDict["energy_level_hydrogen"]}


def get_radioactive_decay(req: Radioactive_DecayRequest) -> GenericResponse[float]:
    return {"definition": SubAutomaticDictionary.SubAtomicDict["radioactive_decay"]}


def get_half_life(req: Half_lifeRequest) -> GenericResponse[float]:
    return {"definition": SubAutomaticDictionary.SubAtomicDict["half_life"]}
