from pydantic import BaseModel


class G_Request(BaseModel):
    m1: float
    m2: float
    r: float


class G_Potential_Request(BaseModel):
    M: float
    r: float


class G_In_Depth_Request(BaseModel):
    depth: float


class Axial_Velocity_Request(BaseModel):
    area_swept: float
    time: float


class Gravitational_Force_Request(BaseModel):
    mass1: float
    mass2: float
    distance: float


class Gravitational_Potential_Energy_Request(BaseModel):
    mass1: float
    mass2: float
    distance: float


class Gravitational_Field_Strength_Request(BaseModel):
    mass: float
    distance: float


class Escape_Velocity_Request(BaseModel):
    mass: float
    radius: float


class Orbital_Velocity_Request(BaseModel):
    mass: float
    radius: float


class Period_Of_Orbit_Request(BaseModel):
    mass: float
    radius: float


class Gravitational_Potential_Request(BaseModel):
    mass: float
    distance: float


class Weight_Request(BaseModel):
    mass: float
    acceleration_due_to_gravity: float


class Gravitational_Acceleration_Request(BaseModel):
    mass: float
    distance: float


class Keplers_Third_Law_Request(BaseModel):
    period: float
    semi_major_axis: float
