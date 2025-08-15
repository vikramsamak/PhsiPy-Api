from fastapi import APIRouter
from schemas.ElectricitySchema import *
from controllers import ElectricityControllers
from schemas.GenericSchema import GenericResponse
from constants import ElectricityConstants

Electricity_Router = APIRouter()

ELECTRICITY_ROUTE_PARAMS = ElectricityConstants.ELECTRICITY_ROUTE_PARAMS


@Electricity_Router.post(
    "/force_electrostatics",
    **ELECTRICITY_ROUTE_PARAMS["FORCE_ELECTROSTATICS"],
    response_model=GenericResponse[float]
)
def calculate_force_electrostatics(req: ForceElectrostaticsSchema):
    return ElectricityControllers.calculate_force_electrostatics(req)


@Electricity_Router.post(
    "/resistance",
    **ELECTRICITY_ROUTE_PARAMS["RESISTANCE"],
    response_model=GenericResponse[float]
)
def calculate_resistance(req: ResistanceSchema):
    return ElectricityControllers.calculate_resistance(req)


@Electricity_Router.post(
    "/current",
    **ELECTRICITY_ROUTE_PARAMS["CURRENT"],
    response_model=GenericResponse[float]
)
def calculate_current(req: CurrentSchema):
    return ElectricityControllers.calculate_current(req)


@Electricity_Router.post(
    "/voltage",
    **ELECTRICITY_ROUTE_PARAMS["VOLTAGE"],
    response_model=GenericResponse[float]
)
def calculate_voltage(req: VoltageSchema):
    return ElectricityControllers.calculate_voltage(req)


@Electricity_Router.post(
    "/power", **ELECTRICITY_ROUTE_PARAMS["POWER"], response_model=GenericResponse[float]
)
def calculate_power(req: PowerSchema):
    return ElectricityControllers.calculate_power(req)
