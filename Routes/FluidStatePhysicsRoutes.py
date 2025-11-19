from fastapi import APIRouter
from controllers import FluidStatePhysicsControllers
from schemas.FluidStatePhysicsSchema import *
from constants import FluidStatePhysicsConstants

FluidStatePhysics_Router = APIRouter(tags=["Fluid State Physics"])

FLUID_STATE_PHYSICS_ROUTE_PARAMS = FluidStatePhysicsConstants.FLUID_STATE_PHYSICS_ROUTE_PARAMS

@FluidStatePhysics_Router.post("/hydrostatic-pressure", **FLUID_STATE_PHYSICS_ROUTE_PARAMS["HYDROSTATIC_PRESSURE"])
def calculate_hydrostatic_pressure(req: HydrostaticPressureRequest):
    return FluidStatePhysicsControllers.calculate_hydrostatic_pressure(req)

@FluidStatePhysics_Router.post("/surface-tension", **FLUID_STATE_PHYSICS_ROUTE_PARAMS["SURFACE_TENSION"])
def calculate_surface_tension(req: SurfaceTensionRequest):
    return FluidStatePhysicsControllers.calculate_surface_tension(req)

@FluidStatePhysics_Router.post("/capillary-pressure", **FLUID_STATE_PHYSICS_ROUTE_PARAMS["CAPILLARY_PRESSURE"])
def calculate_capillary_pressure(req: CapillaryPressureRequest):
    return FluidStatePhysicsControllers.calculate_capillary_pressure(req)

@FluidStatePhysics_Router.post("/bernoullis-equation", **FLUID_STATE_PHYSICS_ROUTE_PARAMS["BERNOULLIS_EQUATION"])
def calculate_bernoullis_equation(req: BernoullisEquationRequest):
    return FluidStatePhysicsControllers.calculate_bernoullis_equation(req)

@FluidStatePhysics_Router.post("/poiseuilles-law", **FLUID_STATE_PHYSICS_ROUTE_PARAMS["POISEUILLES_LAW"])
def calculate_poiseuilles_law(req: PoiseuillesLawRequest):
    return FluidStatePhysicsControllers.calculate_poiseuilles_law(req)

@FluidStatePhysics_Router.post("/reynolds-number", **FLUID_STATE_PHYSICS_ROUTE_PARAMS["REYNOLDS_NUMBER"])
def calculate_reynolds_number(req: ReynoldsNumberRequest):
    return FluidStatePhysicsControllers.calculate_reynolds_number(req)

@FluidStatePhysics_Router.post("/stokes-law", **FLUID_STATE_PHYSICS_ROUTE_PARAMS["STOKES_LAW"])
def calculate_stokes_law(req: StokesLawRequest):
    return FluidStatePhysicsControllers.calculate_stokes_law(req)

@FluidStatePhysics_Router.post("/mach-number", **FLUID_STATE_PHYSICS_ROUTE_PARAMS["MACH_NUMBER"])
def calculate_mach_number(req: MachNumberRequest):
    return FluidStatePhysicsControllers.calculate_mach_number(req)

@FluidStatePhysics_Router.post("/compressibility-factor", **FLUID_STATE_PHYSICS_ROUTE_PARAMS["COMPRESSIBILITY_FACTOR"])
def calculate_compressibility_factor(req: CompressibilityFactorRequest):
    return FluidStatePhysicsControllers.calculate_compressibility_factor(req)

@FluidStatePhysics_Router.post("/boyles-law", **FLUID_STATE_PHYSICS_ROUTE_PARAMS["BOYLES_LAW"])
def calculate_boyles_law(req: BoylesLawRequest):
    return FluidStatePhysicsControllers.calculate_boyles_law(req)

@FluidStatePhysics_Router.post("/charles-law", **FLUID_STATE_PHYSICS_ROUTE_PARAMS["CHARLES_LAW"])
def calculate_charles_law(req: CharlesLawRequest):
    return FluidStatePhysicsControllers.calculate_charles_law(req)

@FluidStatePhysics_Router.post("/gaylussacs-law", **FLUID_STATE_PHYSICS_ROUTE_PARAMS["GAYLUSSACS_LAW"])
def calculate_gaylussacs_law(req: GayLussacsLawRequest):
    return FluidStatePhysicsControllers.calculate_gaylussacs_law(req)

@FluidStatePhysics_Router.post("/avogadros-law", **FLUID_STATE_PHYSICS_ROUTE_PARAMS["AVOGADROS_LAW"])
def calculate_avogadros_law(req: AvogadrosLawRequest):
    return FluidStatePhysicsControllers.calculate_avogadros_law(req)

@FluidStatePhysics_Router.post("/ideal-gas-law", **FLUID_STATE_PHYSICS_ROUTE_PARAMS["IDEAL_GAS_LAW"])
def calculate_ideal_gas_law(req: IdealGasLawRequest):
    return FluidStatePhysicsControllers.calculate_ideal_gas_law(req)
