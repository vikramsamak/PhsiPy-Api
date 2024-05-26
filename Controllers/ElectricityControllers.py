from Dictionaries import ElectricityDictionary
from PhysiPy.equations import Electricity


def get_force_electrostatics(req):
    force_electrostatics = Electricity.force_electrostatics(
        req.q1, req.q2, req.resistance
    )
    return {
        "Defintion": ElectricityDictionary.ElectricityDict["force_electrostatics"],
        "Given": {"Q1": req.q1, "Q2": req.q2, "Resistance": req.resistance},
        "Result": force_electrostatics,
    }


def get_resistance(req):
    resistance = Electricity.resistance(req.voltage, req.current)
    return {
        "Defintion": ElectricityDictionary.ElectricityDict["resistance"],
        "Given": {"Voltage": req.voltage, "Current": req.current},
        "Result": resistance,
    }


def get_current(req):
    current = Electricity.current(req.voltage, req.resistance)
    return {
        "Defintion": ElectricityDictionary.ElectricityDict["current"],
        "Given": {"Voltage": req.voltage, "Resistance": req.resistance},
        "Result": current,
    }


def get_voltage(req):
    voltage = Electricity.voltage(req.current, req.resistance)
    return {
        "Defintion": ElectricityDictionary.ElectricityDict["voltage"],
        "Given": {"Current": req.current, "Resistance": req.resistance},
        "Result": voltage,
    }


def get_power(req):
    power = Electricity.power(req.voltage, req.current)
    return {
        "Defintion": ElectricityDictionary.ElectricityDict["power"],
        "Given": {"Voltage": req.voltage, "Current": req.current},
        "Result": power,
    }


