from Dictionaries import SubAutomaticDictionary


def get_mass_energy_equivalence(req):
    return {
        "definition": SubAutomaticDictionary.SubAtomicDict["mass_energy_equivalence"]
    }


def get_binding_energy(req):
    return {"definition": SubAutomaticDictionary.SubAtomicDict["binding_energy"]}


def get_de_broglie_wavelength(req):
    return {"definition": SubAutomaticDictionary.SubAtomicDict["de_broglie_wavelength"]}


def get_bohr_radius(req):
    return {"definition": SubAutomaticDictionary.SubAtomicDict["bohr_radius"]}


def get_energy_level_hydrogen(req):
    return {"definition": SubAutomaticDictionary.SubAtomicDict["energy_level_hydrogen"]}


def get_radioactive_decay(req):
    return {"definition": SubAutomaticDictionary.SubAtomicDict["radioactive_decay"]}


def get_half_life(req):
    return {"definition": SubAutomaticDictionary.SubAtomicDict["half_life"]}
