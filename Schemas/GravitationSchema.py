from pydantic import BaseModel


class G(BaseModel):
    m1: float
    m2: float
    r: float


class G_Potential(BaseModel):
    M: float
    r: float


class g_in_depth(BaseModel):
    depth: float


class axial_velocity(BaseModel):
    area_swept: float
    time: float


class gravitational_force(BaseModel):
    mass1: float
    mass2: float
    distance: float


class gravitational_potential_energy(BaseModel):
    mass1: float
    mass2: float
    distance: float


class gravitational_field_strength(BaseModel):
    mass: float
    distance: float


class escape_velocity(BaseModel):
    mass: float
    radius: float


class orbital_velocity(BaseModel):
    mass: float
    radius: float


class period_of_orbit(BaseModel):
    mass: float
    radius: float


class gravitational_potential(BaseModel):
    mass: float
    distance: float


class weight(BaseModel):
    mass: float
    acceleration_due_to_gravity: float


class gravitational_acceleration(BaseModel):
    mass: float
    distance: float


class keplers_third_law(BaseModel):
    period: float
    semi_major_axis: float**3
