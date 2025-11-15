from fastapi import APIRouter
from schemas.WavesSchema import *
from controllers import WavesControllers
from schemas.GenericSchema import GenericResponse
from constants import WavesConstants

Waves_Router = APIRouter()
WAVES_ROUTE_PARAMS = WavesConstants.WAVES_ROUTE_PARAMS

@Waves_Router.post(
    "/velocity",
    **WAVES_ROUTE_PARAMS["WAVE_VELOCITY"],
    response_model=GenericResponse[float]
)
def calculate_wave_velocity(req: WaveVelocitySchema):
    return WavesControllers.calculate_wave_velocity(req)

@Waves_Router.post(
    "/period",
    **WAVES_ROUTE_PARAMS["WAVE_PERIOD"],
    response_model=GenericResponse[float]
)
def calculate_wave_period(req: WavePeriodSchema):
    return WavesControllers.calculate_wave_period(req)

@Waves_Router.post(
    "/number",
    **WAVES_ROUTE_PARAMS["WAVE_NUMBER"],
    response_model=GenericResponse[float]
)
def calculate_wave_number(req: WaveNumberSchema):
    return WavesControllers.calculate_wave_number(req)

@Waves_Router.post(
    "/intensity",
    **WAVES_ROUTE_PARAMS["INTENSITY"],
    response_model=GenericResponse[float]
)
def calculate_intensity(req: IntensitySchema):
    return WavesControllers.calculate_intensity(req)

@Waves_Router.post(
    "/refractive_index",
    **WAVES_ROUTE_PARAMS["REFRACTIVE_INDEX"],
    response_model=GenericResponse[float]
)
def calculate_refractive_index(req: RefractiveIndexSchema):
    return WavesControllers.calculate_refractive_index(req)

@Waves_Router.post(
    "/doppler_effect",
    **WAVES_ROUTE_PARAMS["DOPPLER_EFFECT"],
    response_model=GenericResponse[bool]
)
def calculate_doppler_effect(req: DopplerEffectSchema):
    return WavesControllers.calculate_doppler_effect(req)

@Waves_Router.post(
    "/angular_frequency",
    **WAVES_ROUTE_PARAMS["ANGULAR_FREQUENCY"],
    response_model=GenericResponse[float]
)
def calculate_angular_frequency(req: AngularFrequencySchema):
    return WavesControllers.calculate_angular_frequency(req)

@Waves_Router.post(
    "/speed",
    **WAVES_ROUTE_PARAMS["WAVE_SPEED"],
    response_model=GenericResponse[float]
)
def calculate_wave_speed(req: WaveSpeedSchema):
    return WavesControllers.calculate_wave_speed(req)

@Waves_Router.post(
    "/sound_intensity",
    **WAVES_ROUTE_PARAMS["SOUND_INTENSITY"],
    response_model=GenericResponse[float]
)
def calculate_sound_intensity(req: SoundIntensitySchema):
    return WavesControllers.calculate_sound_intensity(req)

@Waves_Router.post(
    "/sound_level",
    **WAVES_ROUTE_PARAMS["SOUND_LEVEL"],
    response_model=GenericResponse[float]
)
def calculate_sound_level(req: SoundLevelSchema):
    return WavesControllers.calculate_sound_level(req)

@Waves_Router.post(
    "/beats_frequency",
    **WAVES_ROUTE_PARAMS["BEATS_FREQUENCY"],
    response_model=GenericResponse[float]
)
def calculate_beats_frequency(req: BeatsFrequencySchema):
    return WavesControllers.calculate_beats_frequency(req)

@Waves_Router.post(
    "/beats_period",
    **WAVES_ROUTE_PARAMS["BEATS_PERIOD"],
    response_model=GenericResponse[float]
)
def calculate_beats_period(req: BeatsPeriodSchema):
    return WavesControllers.calculate_beats_period(req)

