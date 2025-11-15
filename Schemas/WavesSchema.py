from pydantic import BaseModel

class WaveVelocitySchema(BaseModel):
    frequency: float
    wavelength: float

class WavePeriodSchema(BaseModel):
    frequency: float

class WaveNumberSchema(BaseModel):
    wavelength: float

class IntensitySchema(BaseModel):
    power: float
    area: float

class RefractiveIndexSchema(BaseModel):
    real_depth: float
    apparent_depth: float

class DopplerEffectSchema(BaseModel):
    observed_frequency: float
    source_frequency: float
    wave_velocity: float
    observer_velocity: float
    source_velocity: float

class AngularFrequencySchema(BaseModel):
    frequency: float

class WaveSpeedSchema(BaseModel):
    wavelength: float
    period: float

class SoundIntensitySchema(BaseModel):
    sound_power: float
    area: float

class SoundLevelSchema(BaseModel):
    intensity: float

class BeatsFrequencySchema(BaseModel):
    frequency1: float
    frequency2: float

class BeatsPeriodSchema(BaseModel):
    frequency1: float
    frequency2: float

