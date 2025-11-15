from fastapi import APIRouter
from controllers import MechanicsController
from schemas.MechanicsSchema import *
from constants import MechanicsConstants

Mechanics_Router = APIRouter(tags=["Mechanics"])

MECHANICS_ROUTE_PARAMS = MechanicsConstants.MECHANICS_ROUTE_PARAMS


@Mechanics_Router.post("/motion/velocity", **MECHANICS_ROUTE_PARAMS["VELOCITY"])
def calculate_velocity(req: VelocitySchema):
    return MechanicsController.calculate_velocity(req)


@Mechanics_Router.post("/motion/displacement", **MECHANICS_ROUTE_PARAMS["DISPLACEMENT"])
def calculate_displacement(req: DisplacementSchema):
    return MechanicsController.calculate_displacement(req)


@Mechanics_Router.post("/motion/acceleration", **MECHANICS_ROUTE_PARAMS["ACCELERATION"])
def calculate_acceleration(req: AccelerationSchema):
    return MechanicsController.calculate_acceleration(req)


@Mechanics_Router.post(
    "/motion/uniform-accelerated",
    **MECHANICS_ROUTE_PARAMS["UNIFORM_ACCELERATED_MOTION"]
)
def calculate_uniform_accelerated_motion(req: UniformAcceleratedMotionSchema):
    return MechanicsController.calculate_uniform_accelerated_motion(req)


@Mechanics_Router.post("/dynamics/force", **MECHANICS_ROUTE_PARAMS["FORCE"])
def calculate_force(req: ForceSchema):
    return MechanicsController.calculate_force(req)


@Mechanics_Router.post("/energy/work", **MECHANICS_ROUTE_PARAMS["WORK"])
def calculate_work(req: WorkSchema):
    return MechanicsController.calculate_work(req)


@Mechanics_Router.post("/energy/kinetic", **MECHANICS_ROUTE_PARAMS["KINETIC_ENERGY"])
def calculate_kinetic_energy(req: KineticEnergySchema):
    return MechanicsController.calculate_kinetic_energy(req)


@Mechanics_Router.post(
    "/energy/potential", **MECHANICS_ROUTE_PARAMS["POTENTIAL_ENERGY"]
)
def calculate_potential_energy(req: PotentialEnergySchema):
    return MechanicsController.calculate_potential_energy(req)


@Mechanics_Router.post("/energy/power", **MECHANICS_ROUTE_PARAMS["POWER"])
def calculate_power(req: PowerSchema):
    return MechanicsController.calculate_power(req)


@Mechanics_Router.post("/dynamics/momentum", **MECHANICS_ROUTE_PARAMS["MOMENTUM"])
def calculate_momentum(req: MomentumSchema):
    return MechanicsController.calculate_momentum(req)


@Mechanics_Router.post("/dynamics/impulse", **MECHANICS_ROUTE_PARAMS["IMPULSE"])
def calculate_impulse(req: ImpulseSchema):
    return MechanicsController.calculate_impulse(req)


@Mechanics_Router.post(
    "/circular-motion/velocity", **MECHANICS_ROUTE_PARAMS["CIRCULAR_VELOCITY"]
)
def calculate_circular_velocity(req: CircularVelocitySchema):
    return MechanicsController.calculate_circular_velocity(req)


@Mechanics_Router.post(
    "/circular-motion/centripetal-acceleration",
    **MECHANICS_ROUTE_PARAMS["CENTRIPETAL_ACCELERATION"]
)
def calculate_centripetal_acceleration(req: CentripetalAccelerationSchema):
    return MechanicsController.calculate_centripetal_acceleration(req)


@Mechanics_Router.post("/rotational-motion/torque", **MECHANICS_ROUTE_PARAMS["TORQUE"])
def calculate_torque(req: TorqueSchema):
    return MechanicsController.calculate_torque(req)


@Mechanics_Router.post(
    "/rotational-motion/angular-velocity", **MECHANICS_ROUTE_PARAMS["ANGULAR_VELOCITY"]
)
def calculate_angular_velocity(req: AngularVelocitySchema):
    return MechanicsController.calculate_angular_velocity(req)


@Mechanics_Router.post(
    "/rotational-motion/angular-acceleration",
    **MECHANICS_ROUTE_PARAMS["ANGULAR_ACCELERATION"]
)
def calculate_angular_acceleration(req: AngularAccelerationSchema):
    return MechanicsController.calculate_angular_acceleration(req)
