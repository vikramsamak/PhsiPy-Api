from fastapi import APIRouter
from controllers import MechanicsController
from schemas.MechanicsSchema import *

Mechanics_Router = APIRouter(tags=["Mechanics"])


@Mechanics_Router.post("/velocity")
def calculate_velocity(req: VelocitySchema):
    return MechanicsController.calculate_velocity(req)


@Mechanics_Router.post("/displacement")
def calculate_displacement(req: DisplacementSchema):
    return MechanicsController.calculate_displacement(req)


@Mechanics_Router.post("/acceleration")
def calculate_acceleration(req: AccelerationSchema):
    return MechanicsController.calculate_acceleration(req)


@Mechanics_Router.post("/uniform-accelerated-motion")
def calculate_uniform_accelerated_motion(req: UniformAcceleratedMotionSchema):
    return MechanicsController.calculate_uniform_accelerated_motion(req)


@Mechanics_Router.post("/force")
def calculate_force(req: ForceSchema):
    return MechanicsController.calculate_force(req)


@Mechanics_Router.post("/work")
def calculate_work(req: WorkSchema):
    return MechanicsController.calculate_work(req)


@Mechanics_Router.post("/kinetic-energy")
def calculate_kinetic_energy(req: KineticEnergySchema):
    return MechanicsController.calculate_kinetic_energy(req)


@Mechanics_Router.post("/potential-energy")
def calculate_potential_energy(req: PotentialEnergySchema):
    return MechanicsController.calculate_potential_energy(req)


@Mechanics_Router.post("/power")
def calculate_power(req: PowerSchema):
    return MechanicsController.calculate_power(req)


@Mechanics_Router.post("/momentum")
def calculate_momentum(req: MomentumSchema):
    return MechanicsController.calculate_momentum(req)


@Mechanics_Router.post("/impulse")
def calculate_impulse(req: ImpulseSchema):
    return MechanicsController.calculate_impulse(req)


@Mechanics_Router.post("/circular-velocity")
def calculate_circular_velocity(req: CircularVelocitySchema):
    return MechanicsController.calculate_circular_velocity(req)


@Mechanics_Router.post("/centripetal-acceleration")
def calculate_centripetal_acceleration(req: CentripetalAccelerationSchema):
    return MechanicsController.calculate_centripetal_acceleration(req)


@Mechanics_Router.post("/torque")
def calculate_torque(req: TorqueSchema):
    return MechanicsController.calculate_torque(req)


@Mechanics_Router.post("/angular-velocity")
def calculate_angular_velocity(req: AngularVelocitySchema):
    return MechanicsController.calculate_angular_velocity(req)


@Mechanics_Router.post("/angular-acceleration")
def calculate_angular_acceleration(req: AngularAccelerationSchema):
    return MechanicsController.calculate_angular_acceleration(req)
