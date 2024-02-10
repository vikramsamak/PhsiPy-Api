from Dictionaries.Electricity import ElectricityDictionary


def get_force_electrostatics(req):
    return {"defintion": ElectricityDictionary.ElectricityDict["force_electrostatics"]}


def get_resistance(req):
    return {"defintion": ElectricityDictionary.ElectricityDict["resistance"]}


def get_current(req):
    return {"defintion": ElectricityDictionary.ElectricityDict["current"]}


def get_voltage(req):
    return {"defintion": ElectricityDictionary.ElectricityDict["voltage"]}


def get_power(req):
    return {"defintion": ElectricityDictionary.ElectricityDict["power"]}


def get_ohms_law(req):
    return {"defintion": ElectricityDictionary.ElectricityDict["ohms_law"]}
