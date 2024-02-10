from fastapi import APIRouter
from Classes.Electricity import ElectricityClasses
from Controllers.Electricity import ElectricityControllers


Electricity_router = APIRouter()


@Electricity_router.post("/force_electrostatics")
def force_electrostatics(req: ElectricityClasses.Force_Electrostatics):
    return ElectricityControllers.get_force_electrostatics(req)


@Electricity_router.post("/resistance")
def resistance(req: ElectricityClasses.Resistance):
    return ElectricityControllers.get_resistance(req)


@Electricity_router.post("/current")
def current(req: ElectricityClasses.Current):
    return ElectricityControllers.get_current(req)


@Electricity_router.post("/voltage")
def voltage(req: ElectricityClasses.Voltage):
    return ElectricityControllers.get_voltage(req)


@Electricity_router.post("/power")
def power(req: ElectricityClasses.Power):
    return ElectricityControllers.get_power(req)


@Electricity_router.post("/ohms_law")
def ohms_law(req: ElectricityClasses.Power):
    return ElectricityControllers.get_ohms_law(req)
