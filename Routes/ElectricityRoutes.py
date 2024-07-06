from fastapi import APIRouter
from Schemas.ElectricitySchema import *
from Controllers import ElectricityControllers
from Schemas.GenericSchema import GenericResponse
from Helpers import Constants

Electricity_router = APIRouter()

ELECTRICITY_ROUTE_PARAMS = Constants.ROUTE_PARAMS["ELECTRICITY"]


@Electricity_router.post(
    "/force_electrostatics",
    **ELECTRICITY_ROUTE_PARAMS["FORCE_ELECTROSTATICS"],
    response_model=GenericResponse[float]
)
def force_electrostatics(req: Force_ElectrostaticsRequest):
    return ElectricityControllers.get_force_electrostatics(req)


@Electricity_router.post(
    "/resistance",
    **ELECTRICITY_ROUTE_PARAMS["RESISTANCE"],
    response_model=GenericResponse[float]
)
def resistance(req: ResistanceRequest):
    return ElectricityControllers.get_resistance(req)


@Electricity_router.post(
    "/current",
    **ELECTRICITY_ROUTE_PARAMS["CURRENT"],
    response_model=GenericResponse[float]
)
def current(req: CurrentRequest):
    return ElectricityControllers.get_current(req)


@Electricity_router.post(
    "/voltage",
    **ELECTRICITY_ROUTE_PARAMS["VOLTAGE"],
    response_model=GenericResponse[float]
)
def voltage(req: VoltageRequest):
    return ElectricityControllers.get_voltage(req)


@Electricity_router.post(
    "/power", **ELECTRICITY_ROUTE_PARAMS["POWER"], response_model=GenericResponse[float]
)
def power(req: PowerRequest):
    return ElectricityControllers.get_power(req)
