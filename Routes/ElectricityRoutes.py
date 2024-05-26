from fastapi import APIRouter
from Classes import ElectricityClasses
from Controllers import ElectricityControllers
from Classes.GenericResponse import GenericResponse
from Helpers import Constants

Electricity_router = APIRouter()

ELECTRICITY_ROUTE_PARAMS = Constants.ROUTE_PARAMS["ELECTRICITY"]


@Electricity_router.post(
    "/force_electrostatics",
    **ELECTRICITY_ROUTE_PARAMS["FORCE_ELECTROSTATICS"],
    response_model=GenericResponse[float]
)
def force_electrostatics(req: ElectricityClasses.Force_ElectrostaticsRequest):
    return ElectricityControllers.get_force_electrostatics(req)


@Electricity_router.post(
    "/resistance",
    **ELECTRICITY_ROUTE_PARAMS["RESISTANCE"],
    response_model=GenericResponse[float]
)
def resistance(req: ElectricityClasses.ResistanceRequest):
    return ElectricityControllers.get_resistance(req)


@Electricity_router.post(
    "/current",
    **ELECTRICITY_ROUTE_PARAMS["CURRENT"],
    response_model=GenericResponse[float]
)
def current(req: ElectricityClasses.CurrentRequest):
    return ElectricityControllers.get_current(req)


@Electricity_router.post(
    "/voltage",
    **ELECTRICITY_ROUTE_PARAMS["VOLTAGE"],
    response_model=GenericResponse[float]
)
def voltage(req: ElectricityClasses.VoltageRequest):
    return ElectricityControllers.get_voltage(req)


@Electricity_router.post(
    "/power", **ELECTRICITY_ROUTE_PARAMS["POWER"], response_model=GenericResponse[float]
)
def power(req: ElectricityClasses.PowerRequest):
    return ElectricityControllers.get_power(req)
