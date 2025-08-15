from dictionaries import ElectricityDictionary
from libs.phsipy.PhsipyEquations import Electricity
from schemas.ElectricitySchema import *
from schemas.GenericSchema import GenericResponse


def get_force_electrostatics(
    req: ForceElectrostaticsSchema,
) -> GenericResponse[float]:
    force_electrostatics = Electricity.force_electrostatics(
        req.q1, req.q2, req.resistance
    )
    return GenericResponse(
        Definition=ElectricityDictionary.ElectricityDict["force_electrostatics"],
        Given={"Q1": req.q1, "Q2": req.q2, "Resistance": req.resistance},
        Result=force_electrostatics,
    )


def get_resistance(req: ResistanceSchema) -> GenericResponse[float]:
    resistance = Electricity.resistance(req.voltage, req.current)
    return GenericResponse(
        Definition=ElectricityDictionary.ElectricityDict["resistance"],
        Given={"Voltage": req.voltage, "Current": req.current},
        Result=resistance,
    )


def get_current(req: CurrentSchema) -> GenericResponse[float]:
    current = Electricity.current(req.voltage, req.resistance)
    return GenericResponse(
        Definition=ElectricityDictionary.ElectricityDict["current"],
        Given={"Voltage": req.voltage, "Resistance": req.resistance},
        Result=current,
    )


def get_voltage(req: VoltageSchema) -> GenericResponse[float]:
    voltage = Electricity.voltage(req.current, req.resistance)
    return GenericResponse(
        Definition=ElectricityDictionary.ElectricityDict["voltage"],
        Given={"Current": req.current, "Resistance": req.resistance},
        Result=voltage,
    )


def get_power(req: PowerSchema) -> GenericResponse[float]:
    power = Electricity.power(req.voltage, req.current)
    return GenericResponse(
        Definition=ElectricityDictionary.ElectricityDict["power"],
        Given={"Voltage": req.voltage, "Current": req.current},
        Result=power,
    )
