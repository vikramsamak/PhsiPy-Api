from fastapi import APIRouter
from Classes import ElectricityClasses
from Controllers import ElectricityControllers
from Helpers import Constants

Electricity_router = APIRouter()

ELECTRICITY_TAGS = [Constants.TAGS["ELECTRICITY"]]


@Electricity_router.post("/force_electrostatics", tags=ELECTRICITY_TAGS)
def force_electrostatics(req: ElectricityClasses.Force_Electrostatics):
    return ElectricityControllers.get_force_electrostatics(req)


@Electricity_router.post("/resistance", tags=ELECTRICITY_TAGS)
def resistance(req: ElectricityClasses.Resistance):
    return ElectricityControllers.get_resistance(req)


@Electricity_router.post("/current", tags=ELECTRICITY_TAGS)
def current(req: ElectricityClasses.Current):
    return ElectricityControllers.get_current(req)


@Electricity_router.post("/voltage", tags=ELECTRICITY_TAGS)
def voltage(req: ElectricityClasses.Voltage):
    return ElectricityControllers.get_voltage(req)


@Electricity_router.post("/power", tags=ELECTRICITY_TAGS)
def power(req: ElectricityClasses.Power):
    return ElectricityControllers.get_power(req)
