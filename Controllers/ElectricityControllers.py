from Dictionaries import ElectricityDictionary
from Libs.PhsiPy.PhsipyEquations import Electricity
from Classes.ElectricityClasses import Force_ElectrostaticsRequest
from Classes.ElectricityClasses import ResistanceRequest
from Classes.ElectricityClasses import CurrentRequest
from Classes.ElectricityClasses import VoltageRequest
from Classes.ElectricityClasses import PowerRequest
from Classes.GenericResponse import GenericResponse


def get_force_electrostatics(
    req: Force_ElectrostaticsRequest,
) -> GenericResponse[float]:
    force_electrostatics = Electricity.force_electrostatics(
        req.q1, req.q2, req.resistance
    )
    return GenericResponse(
        Definition=ElectricityDictionary.ElectricityDict["force_electrostatics"],
        Given={"Q1": req.q1, "Q2": req.q2, "Resistance": req.resistance},
        Result=force_electrostatics,
    )


def get_resistance(req: ResistanceRequest) -> GenericResponse[float]:
    resistance = Electricity.resistance(req.voltage, req.current)
    return GenericResponse(
        Definition=ElectricityDictionary.ElectricityDict["resistance"],
        Given={"voltage": req.voltage, "current": req.current},
        Result=resistance,
    )


def get_current(req: CurrentRequest) -> GenericResponse[float]:
    current = Electricity.current(req.voltage, req.resistance)
    return GenericResponse(
        Defintion=ElectricityDictionary.ElectricityDict["current"],
        Given={"Voltage": req.voltage, "Resistance": req.resistance},
        Result=current,
    )


def get_voltage(req: VoltageRequest) -> GenericResponse[float]:
    voltage = Electricity.voltage(req.current, req.resistance)
    return GenericResponse(
        Defintion=ElectricityDictionary.ElectricityDict["voltage"],
        Given={"Current": req.current, "Resistance": req.resistance},
        Result=voltage,
    )


def get_power(req: PowerRequest) -> GenericResponse[float]:
    power = Electricity.power(req.voltage, req.current)
    return GenericResponse(
        Defintion=ElectricityDictionary.ElectricityDict["power"],
        Given={"Voltage": req.voltage, "Current": req.current},
        Result=power,
    )
