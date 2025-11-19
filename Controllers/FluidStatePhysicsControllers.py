from libs.phsipy.PhsipyEquations import FluidStatePhysics
from schemas.FluidStatePhysicsSchema import *
from schemas.GenericSchema import GenericResponse
from dictionaries import FluidStatePhysicsDictionary


def calculate_hydrostatic_pressure(req: HydrostaticPressureRequest) -> GenericResponse[float]:
    result = FluidStatePhysics.hydrostatic_pressure(req.density, req.acceleration_due_to_gravity, req.height)
    return GenericResponse(
        Definition=FluidStatePhysicsDictionary.FluidStatePhysicsDict["hydrostatic_pressure"],
        Given={
            "Density": req.density,
            "Acceleration Due To Gravity": req.acceleration_due_to_gravity,
            "Height": req.height,
        },
        Result=result,
    )

def calculate_surface_tension(req: SurfaceTensionRequest) -> GenericResponse[float]:
    result = FluidStatePhysics.surface_tension(req.surface_tension_coefficient, req.contact_angle, req.radius_of_curvature)
    return GenericResponse(
        Definition=FluidStatePhysicsDictionary.FluidStatePhysicsDict["surface_tension"],
        Given={
            "Surface Tension Coefficient": req.surface_tension_coefficient,
            "Contact Angle": req.contact_angle,
            "Radius of Curvature": req.radius_of_curvature,
        },
        Result=result,
    )

def calculate_capillary_pressure(req: CapillaryPressureRequest) -> GenericResponse[float]:
    result = FluidStatePhysics.capillary_pressure(req.surface_tension, req.radius_of_curvature)
    return GenericResponse(
        Definition=FluidStatePhysicsDictionary.FluidStatePhysicsDict["capillary_pressure"],
        Given={
            "Surface Tension": req.surface_tension,
            "Radius of Curvature": req.radius_of_curvature,
        },
        Result=result,
    )

def calculate_bernoullis_equation(req: BernoullisEquationRequest) -> GenericResponse[float]:
    result = FluidStatePhysics.bernoullis_equation(req.static_pressure, req.dynamic_pressure, req.height, req.density, req.gravitational_acceleration)
    return GenericResponse(
        Definition=FluidStatePhysicsDictionary.FluidStatePhysicsDict["bernoullis_equation"],
        Given={
            "Static Pressure": req.static_pressure,
            "Dynamic Pressure": req.dynamic_pressure,
            "Height": req.height,
            "Density": req.density,
            "Gravitational Acceleration": req.gravitational_acceleration,
        },
        Result=result,
    )

def calculate_poiseuilles_law(req: PoiseuillesLawRequest) -> GenericResponse[float]:
    result = FluidStatePhysics.poiseuilles_law(req.flow_rate, req.viscosity, req.length, req.radius)
    return GenericResponse(
        Definition=FluidStatePhysicsDictionary.FluidStatePhysicsDict["poiseuilles_law"],
        Given={
            "Flow Rate": req.flow_rate,
            "Viscosity": req.viscosity,
            "Length": req.length,
            "Radius": req.radius,
        },
        Result=result,
    )

def calculate_reynolds_number(req: ReynoldsNumberRequest) -> GenericResponse[float]:
    result = FluidStatePhysics.reynolds_number(req.density, req.velocity, req.length, req.viscosity)
    return GenericResponse(
        Definition=FluidStatePhysicsDictionary.FluidStatePhysicsDict["reynolds_number"],
        Given={
            "Density": req.density,
            "Velocity": req.velocity,
            "Length": req.length,
            "Viscosity": req.viscosity,
        },
        Result=result,
    )

def calculate_stokes_law(req: StokesLawRequest) -> GenericResponse[float]:
    result = FluidStatePhysics.stokes_law(req.drag_force, req.viscosity, req.particle_radius)
    return GenericResponse(
        Definition=FluidStatePhysicsDictionary.FluidStatePhysicsDict["stokes_law"],
        Given={
            "Drag Force": req.drag_force,
            "Viscosity": req.viscosity,
            "Particle Radius": req.particle_radius,
        },
        Result=result,
    )

def calculate_mach_number(req: MachNumberRequest) -> GenericResponse[float]:
    result = FluidStatePhysics.mach_number(req.speed_of_sound, req.velocity)
    return GenericResponse(
        Definition=FluidStatePhysicsDictionary.FluidStatePhysicsDict["mach_number"],
        Given={
            "Speed of Sound": req.speed_of_sound,
            "Velocity": req.velocity,
        },
        Result=result,
    )

def calculate_compressibility_factor(req: CompressibilityFactorRequest) -> GenericResponse[float]:
    result = FluidStatePhysics.compressibility_factor(req.volume_change, req.initial_volume, req.pressure_change)
    return GenericResponse(
        Definition=FluidStatePhysicsDictionary.FluidStatePhysicsDict["compressibility_factor"],
        Given={
            "Volume Change": req.volume_change,
            "Initial Volume": req.initial_volume,
            "Pressure Change": req.pressure_change,
        },
        Result=result,
    )

def calculate_boyles_law(req: BoylesLawRequest) -> GenericResponse[float]:
    result = FluidStatePhysics.boyles_law(req.initial_pressure, req.initial_volume, req.final_pressure, req.final_volume)
    return GenericResponse(
        Definition=FluidStatePhysicsDictionary.FluidStatePhysicsDict["boyles_law"],
        Given={
            "Initial Pressure": req.initial_pressure,
            "Initial Volume": req.initial_volume,
            "Final Pressure": req.final_pressure,
            "Final Volume": req.final_volume,
        },
        Result=result,
    )

def calculate_charles_law(req: CharlesLawRequest) -> GenericResponse[float]:
    result = FluidStatePhysics.charles_law(req.initial_volume, req.final_volume, req.initial_temperature, req.final_temperature)
    return GenericResponse(
        Definition=FluidStatePhysicsDictionary.FluidStatePhysicsDict["charles_law"],
        Given={
            "Initial Volume": req.initial_volume,
            "Final Volume": req.final_volume,
            "Initial Temperature": req.initial_temperature,
            "Final Temperature": req.final_temperature,
        },
        Result=result,
    )

def calculate_gaylussacs_law(req: GayLussacsLawRequest) -> GenericResponse[float]:
    result = FluidStatePhysics.gaylussacs_law(req.initial_pressure, req.final_pressure, req.initial_temperature, req.final_temperature)
    return GenericResponse(
        Definition=FluidStatePhysicsDictionary.FluidStatePhysicsDict["gaylussacs_law"],
        Given={
            "Initial Pressure": req.initial_pressure,
            "Final Pressure": req.final_pressure,
            "Initial Temperature": req.initial_temperature,
            "Final Temperature": req.final_temperature,
        },
        Result=result,
    )

def calculate_avogadros_law(req: AvogadrosLawRequest) -> GenericResponse[float]:
    result = FluidStatePhysics.avogadros_law(req.initial_volume, req.final_volume, req.initial_moles, req.final_moles)
    return GenericResponse(
        Definition=FluidStatePhysicsDictionary.FluidStatePhysicsDict["avogadros_law"],
        Given={
            "Initial Volume": req.initial_volume,
            "Final Volume": req.final_volume,
            "Initial Moles": req.initial_moles,
            "Final Moles": req.final_moles,
        },
        Result=result,
    )

def calculate_ideal_gas_law(req: IdealGasLawRequest) -> GenericResponse[float]:
    result = FluidStatePhysics.ideal_gas_law(req.pressure, req.volume, req.temperature, req.gas_constant)
    return GenericResponse(
        Definition=FluidStatePhysicsDictionary.FluidStatePhysicsDict["ideal_gas_law"],
        Given={
            "Pressure": req.pressure,
            "Volume": req.volume,
            "Temperature": req.temperature,
            "Gas Constant": req.gas_constant,
        },
        Result=result,
    )
