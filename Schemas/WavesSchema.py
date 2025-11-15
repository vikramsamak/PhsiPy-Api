from pydantic import BaseModel

class WaveVelocityRequest(BaseModel):
    frequency: float
    wavelength: float

class WavePeriodRequest(BaseModel):
    frequency: float

class WaveNumberRequest(BaseModel):
    wavelength: float

class IntensityRequest(BaseModel):
    power: float
    area: float

class RefractiveIndexRequest(BaseModel):
    real_depth: float
    apparent_depth: float

class DopplerEffectRequest(BaseModel):
    observed_frequency: float
    source_frequency: float
    wave_velocity: float
    observer_velocity: float
    source_velocity: float

class AngularFrequencyRequest(BaseModel):
    frequency: float

class WaveSpeedRequest(BaseModel):
    wavelength: float
    period: float

class SoundIntensityRequest(BaseModel):
    sound_power: float
    area: float

class SoundLevelRequest(BaseModel):
    intensity: float

class BeatsFrequencyRequest(BaseModel):
    frequency1: float
    frequency2: float

class BeatsPeriodRequest(BaseModel):
    frequency1: float
    frequency2: float

