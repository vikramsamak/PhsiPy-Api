from pydantic import BaseModel

class HydrostaticPressureRequest(BaseModel):
    density: float
    acceleration_due_to_gravity: float
    height: float

class SurfaceTensionRequest(BaseModel):
    surface_tension_coefficient: float
    contact_angle: float
    radius_of_curvature: float

class CapillaryPressureRequest(BaseModel):
    surface_tension: float
    radius_of_curvature: float

class BernoullisEquationRequest(BaseModel):
    static_pressure: float
    dynamic_pressure: float
    height: float
    density: float
    gravitational_acceleration: float

class PoiseuillesLawRequest(BaseModel):
    flow_rate: float
    viscosity: float
    length: float
    radius: float

class ReynoldsNumberRequest(BaseModel):
    density: float
    velocity: float
    length: float
    viscosity: float

class StokesLawRequest(BaseModel):
    drag_force: float
    viscosity: float
    particle_radius: float

class MachNumberRequest(BaseModel):
    speed_of_sound: float
    velocity: float

class CompressibilityFactorRequest(BaseModel):
    volume_change: float
    initial_volume: float
    pressure_change: float

class BoylesLawRequest(BaseModel):
    initial_pressure: float
    initial_volume: float
    final_pressure: float
    final_volume: float

class CharlesLawRequest(BaseModel):
    initial_volume: float
    final_volume: float
    initial_temperature: float
    final_temperature: float

class GayLussacsLawRequest(BaseModel):
    initial_pressure: float
    final_pressure: float
    initial_temperature: float
    final_temperature: float

class AvogadrosLawRequest(BaseModel):
    initial_volume: float
    final_volume: float
    initial_moles: float
    final_moles: float

class IdealGasLawRequest(BaseModel):
    pressure: float
    volume: float
    temperature: float
    gas_constant: float
