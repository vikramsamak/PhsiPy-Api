from libs.phsipy.PhsipyEquations import Mechanics
from schemas.MechanicsSchema import *
from schemas.GenericSchema import GenericResponse
from dictionaries import MechanicsDictionary


def calculate_velocity(req: VelocitySchema) -> GenericResponse[float]:
    velocity = Mechanics.velocity(req.initial_velocity, req.acceleration, req.time)
    return GenericResponse(
        Definition=MechanicsDictionary.MechanicsDict["velocity"],
        Given={
            "Initial Velocity": req.initial_velocity,
            "Acceleration": req.acceleration,
            "Time": req.time,
        },
        Result=velocity,
    )


def calculate_displacement(req: DisplacementSchema) -> GenericResponse[float]:
    displacement = Mechanics.displacement(
        req.initial_velocity, req.acceleration, req.time
    )
    return GenericResponse(
        Definition=MechanicsDictionary.MechanicsDict["displacement"],
        Given={
            "Initial Velocity": req.initial_velocity,
            "Acceleration": req.acceleration,
            "Time": req.time,
        },
        Result=displacement,
    )


def calculate_acceleration(req: AccelerationSchema) -> GenericResponse[float]:
    acceleration = Mechanics.acceleration(
        req.final_velocity, req.initial_velocity, req.time
    )
    return GenericResponse(
        Definition=MechanicsDictionary.MechanicsDict["acceleration"],
        Given={
            "Final Velocity": req.final_velocity,
            "Initial Velocity": req.initial_velocity,
            "Time": req.time,
        },
        Result=acceleration,
    )


def calculate_uniform_accelerated_motion(
    req: UniformAcceleratedMotionSchema,
) -> GenericResponse[tuple[float, float]]:
    displacement, final_velocity = Mechanics.uniform_accelerated_motion(
        req.initial_velocity, req.time, req.acceleration
    )
    return GenericResponse(
        Definition=MechanicsDictionary.MechanicsDict["uniform_accelerated_motion"],
        Given={
            "Initial Velocity": req.initial_velocity,
            "Time": req.time,
            "Acceleration": req.acceleration,
        },
        Result={"Displacement": displacement, "Final Velocity": final_velocity},
    )


def calculate_force(req: ForceSchema) -> GenericResponse[float]:
    force = Mechanics.force(req.mass, req.acceleration)
    return GenericResponse(
        Definition=MechanicsDictionary.MechanicsDict["force"],
        Given={"Mass": req.mass, "Acceleration": req.acceleration},
        Result=force,
    )


def calculate_work(req: WorkSchema) -> GenericResponse[float]:
    work = Mechanics.work(req.force, req.displacement, req.angle)
    return GenericResponse(
        Definition=MechanicsDictionary.MechanicsDict["work"],
        Given={
            "Force": req.force,
            "Displacement": req.displacement,
            "Angle": req.angle,
        },
        Result=work,
    )


def calculate_kinetic_energy(req: KineticEnergySchema) -> GenericResponse[float]:
    kinetic_energy = Mechanics.kinetic_energy(req.mass, req.velocity)
    return GenericResponse(
        Definition=MechanicsDictionary.MechanicsDict["kinetic_energy"],
        Given={"Mass": req.mass, "Velocity": req.velocity},
        Result=kinetic_energy,
    )


def calculate_potential_energy(req: PotentialEnergySchema) -> GenericResponse[float]:
    potential_energy = Mechanics.potential_energy(
        req.mass, req.height, req.gravitational_field_strength
    )
    return GenericResponse(
        Definition=MechanicsDictionary.MechanicsDict["potential_energy"],
        Given={
            "Mass": req.mass,
            "Height": req.height,
            "Gravitational Field Strength": req.gravitational_field_strength,
        },
        Result=potential_energy,
    )


def calculate_power(req: PowerSchema) -> GenericResponse[float]:
    power = Mechanics.power(req.work, req.time)
    return GenericResponse(
        Definition=MechanicsDictionary.MechanicsDict["power"],
        Given={"Work": req.work, "Time": req.time},
        Result=power,
    )


def calculate_momentum(req: MomentumSchema) -> GenericResponse[float]:
    momentum = Mechanics.momentum(req.mass, req.velocity)
    return GenericResponse(
        Definition=MechanicsDictionary.MechanicsDict["momentum"],
        Given={"Mass": req.mass, "Velocity": req.velocity},
        Result=momentum,
    )


def calculate_impulse(req: ImpulseSchema) -> GenericResponse[float]:
    impulse = Mechanics.impulse(req.force, req.time)
    return GenericResponse(
        Definition=MechanicsDictionary.MechanicsDict["impulse"],
        Given={"Force": req.force, "Time": req.time},
        Result=impulse,
    )


def calculate_circular_velocity(req: CircularVelocitySchema) -> GenericResponse[float]:
    circular_velocity = Mechanics.circular_velocity(req.radius, req.period)
    return GenericResponse(
        Definition=MechanicsDictionary.MechanicsDict["circular_velocity"],
        Given={"Radius": req.radius, "Period": req.period},
        Result=circular_velocity,
    )


def calculate_centripetal_acceleration(
    req: CentripetalAccelerationSchema,
) -> GenericResponse[float]:
    centripetal_acceleration = Mechanics.centripetal_acceleration(
        req.radius, req.velocity
    )
    return GenericResponse(
        Definition=MechanicsDictionary.MechanicsDict["centripetal_acceleration"],
        Given={"Radius": req.radius, "Velocity": req.velocity},
        Result=centripetal_acceleration,
    )


def calculate_torque(req: TorqueSchema) -> GenericResponse[float]:
    torque = Mechanics.torque(req.force, req.lever_arm)
    return GenericResponse(
        Definition=MechanicsDictionary.MechanicsDict["torque"],
        Given={"Force": req.force, "Lever Arm": req.lever_arm},
        Result=torque,
    )


def calculate_angular_velocity(req: AngularVelocitySchema) -> GenericResponse[float]:
    angular_velocity = Mechanics.angular_velocity(req.angular_displacement, req.time)
    return GenericResponse(
        Definition=MechanicsDictionary.MechanicsDict["angular_velocity"],
        Given={"Angular Displacement": req.angular_displacement, "Time": req.time},
        Result=angular_velocity,
    )


def calculate_angular_acceleration(
    req: AngularAccelerationSchema,
) -> GenericResponse[float]:
    angular_acceleration = Mechanics.angular_acceleration(
        req.angular_velocity, req.time
    )
    return GenericResponse(
        Definition=MechanicsDictionary.MechanicsDict["angular_acceleration"],
        Given={"Angular Velocity": req.angular_velocity, "Time": req.time},
        Result=angular_acceleration,
    )
