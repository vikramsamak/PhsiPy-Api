from dictionaries import SubAutomaticDictionary
from schemas.SubAutomaticSchema import *
from schemas.GenericSchema import GenericResponse
from libs.phsipy.PhsipyEquations import Subatomic


def calculate_mass_energy_equivalence(
    req: MassEnergyEquivalenceSchema,
) -> GenericResponse[float]:

    energy_equivalence = Subatomic.mass_energy_equivalence(req.mass)

    return GenericResponse(
        Definition=SubAutomaticDictionary.SubAtomicDict["mass_energy_equivalence"],
        Given={"Mass": req.mass},
        Result=energy_equivalence,
    )


def calculate_binding_energy(req: BindingEnergySchema) -> GenericResponse[float]:

    binding_energy = Subatomic.binding_energy(req.mass_parent, req.mass_daughters)

    return GenericResponse(
        Definition=SubAutomaticDictionary.SubAtomicDict["binding_energy"],
        Given={"Mass Parent": req.mass_parent, "Mass Daughters": req.mass_daughters},
        Result=binding_energy,
    )


def calculate_de_broglie_wavelength(
    req: DeBroglieWavelengthSchema,
) -> GenericResponse[float]:

    de_broglie_wavelength = Subatomic.de_broglie_wavelength(req.momentum, req.mass)

    return GenericResponse(
        Definition=SubAutomaticDictionary.SubAtomicDict["de_broglie_wavelength"],
        Given={"Momentum": req.momentum, "Mass": req.mass},
        Result=de_broglie_wavelength,
    )


def calculate_bohr_radius(req: BohrRadiusSchema) -> GenericResponse[float]:

    bohr_radius = Subatomic.bohr_radius(req.atomic_number)

    return GenericResponse(
        Definition=SubAutomaticDictionary.SubAtomicDict["bohr_radius"],
        Given={"Atomic Number": req.atomic_number},
        Result=bohr_radius,
    )


def calculate_energy_level_hydrogen(
    req: EnergyLevelHydrogenSchema,
) -> GenericResponse[float]:

    energy_level_hydrogen = Subatomic.energy_level_hydrogen(req.n)

    return GenericResponse(
        Definition=SubAutomaticDictionary.SubAtomicDict["energy_level_hydrogen"],
        Given={"n": req.n},
        Result=energy_level_hydrogen,
    )


def calculate_radioactive_decay(req: RadioactiveDecaySchema) -> GenericResponse[float]:

    radioactive_decay = Subatomic.radioactive_decay(
        req.initial_amount, req.decay_constant, req.time
    )

    return GenericResponse(
        Definition=SubAutomaticDictionary.SubAtomicDict["radioactive_decay"],
        Given={
            "Initial Amount": req.initial_amount,
            "Decay Constant": req.decay_constant,
            "Time": req.time,
        },
        Result=radioactive_decay,
    )


def calculate_half_life(req: HalfLifeSchema) -> GenericResponse[float]:

    half_life = Subatomic.half_life(req.decay_constant)

    return GenericResponse(
        Definition=SubAutomaticDictionary.SubAtomicDict["half_life"],
        Given={"Decay Constant": req.decay_constant},
        Result=half_life,
    )
