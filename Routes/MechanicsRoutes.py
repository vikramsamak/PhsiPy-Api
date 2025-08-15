from fastapi import APIRouter
from controllers import MechanicsController
from schemas.MechanicsSchema import *

Mechanics_Router = APIRouter(tags=["Mechanics"])


@Mechanics_Router.post("/motion/velocity")
def calculate_velocity(req: VelocitySchema):
    return MechanicsController.calculate_velocity(req)


@Mechanics_Router.post("/motion/displacement")
def calculate_displacement(req: DisplacementSchema):
    return MechanicsController.calculate_displacement(req)


@Mechanics_Router.post("/motion/acceleration")
def calculate_acceleration(req: AccelerationSchema):
    return MechanicsController.calculate_acceleration(req)


@Mechanics_Router.post("/motion/uniform-accelerated")
def calculate_uniform_accelerated_motion(req: UniformAcceleratedMotionSchema):
    return MechanicsController.calculate_uniform_accelerated_motion(req)


@Mechanics_Router.post("/dynamics/force")
def calculate_force(req: ForceSchema):
    return MechanicsController.calculate_force(req)


@Mechanics_Router.post("/energy/work")
def calculate_work(req: WorkSchema):
    return MechanicsController.calculate_work(req)


@Mechanics_Router.post("/energy/kinetic")
def calculate_kinetic_energy(req: KineticEnergySchema):
    return MechanicsController.calculate_kinetic_energy(req)


@Mechanics_Router.post("/energy/potential")
def calculate_potential_energy(req: PotentialEnergySchema):
    return MechanicsController.calculate_potential_energy(req)


@Mechanics_Router.post("/energy/power")
def calculate_power(req: PowerSchema):
    return MechanicsController.calculate_power(req)


@Mechanics_Router.post("/dynamics/momentum")
def calculate_momentum(req: MomentumSchema):
    return MechanicsController.calculate_momentum(req)


@Mechanics_Router.post("/dynamics/impulse")
def calculate_impulse(req: ImpulseSchema):
    return MechanicsController.calculate_impulse(req)


@Mechanics_Router.post("/circular-motion/velocity")
def calculate_circular_velocity(req: CircularVelocitySchema):
    return MechanicsController.calculate_circular_velocity(req)


@Mechanics_Router.post("/circular-motion/centripetal-acceleration")
def calculate_centripetal_acceleration(req: CentripetalAccelerationSchema):
    return MechanicsController.calculate_centripetal_acceleration(req)


@Mechanics_Router.post("/rotational-motion/torque")
def calculate_torque(req: TorqueSchema):
    return MechanicsController.calculate_torque(req)


@Mechanics_Router.post("/rotational-motion/angular-velocity")
def calculate_angular_velocity(req: AngularVelocitySchema):
    return MechanicsController.calculate_angular_velocity(req)


@Mechanics_Router.post("/rotational-motion/angular-acceleration")
def calculate_angular_acceleration(req: AngularAccelerationSchema):
    return MechanicsController.calculate_angular_acceleration(req)
