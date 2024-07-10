from Dictionaries import ElectricityDictionary
from Libs.PhsiPy.PhsipyEquations import Electricity
from Schemas.ElectricitySchema import *
from Schemas.GenericSchema import GenericResponse


def get_force_electrostatics(
    req: Force_Electrostatics_Request,
) -> GenericResponse[float]:
    force_electrostatics = Electricity.force_electrostatics(
        req.q1, req.q2, req.resistance
    )
    return GenericResponse(
        Definition=ElectricityDictionary.ElectricityDict["force_electrostatics"],
        Given={"Q1": req.q1, "Q2": req.q2, "Resistance": req.resistance},
        Result=force_electrostatics,
    )


def get_resistance(req: Resistance_Request) -> GenericResponse[float]:
    resistance = Electricity.resistance(req.voltage, req.current)
    return GenericResponse(
        Definition=ElectricityDictionary.ElectricityDict["resistance"],
        Given={"Voltage": req.voltage, "Current": req.current},
        Result=resistance,
    )


def get_current(req: Current_Request) -> GenericResponse[float]:
    current = Electricity.current(req.voltage, req.resistance)
    return GenericResponse(
        Definition=ElectricityDictionary.ElectricityDict["current"],
        Given={"Voltage": req.voltage, "Resistance": req.resistance},
        Result=current,
    )


def get_voltage(req: Voltage_Request) -> GenericResponse[float]:
    voltage = Electricity.voltage(req.current, req.resistance)
    return GenericResponse(
        Definition=ElectricityDictionary.ElectricityDict["voltage"],
        Given={"Current": req.current, "Resistance": req.resistance},
        Result=voltage,
    )


def get_power(req: Power_Request) -> GenericResponse[float]:
    power = Electricity.power(req.voltage, req.current)
    return GenericResponse(
        Definition=ElectricityDictionary.ElectricityDict["power"],
        Given={"Voltage": req.voltage, "Current": req.current},
        Result=power,
    )
