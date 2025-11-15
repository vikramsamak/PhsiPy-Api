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
def wave_velocity(req: WaveVelocityRequest):
    return WavesControllers.get_wave_velocity(req)

@Waves_Router.post(
    "/period",
    **WAVES_ROUTE_PARAMS["WAVE_PERIOD"],
    response_model=GenericResponse[float]
)
def wave_period(req: WavePeriodRequest):
    return WavesControllers.get_wave_period(req)

@Waves_Router.post(
    "/number",
    **WAVES_ROUTE_PARAMS["WAVE_NUMBER"],
    response_model=GenericResponse[float]
)
def wave_number(req: WaveNumberRequest):
    return WavesControllers.get_wave_number(req)

@Waves_Router.post(
    "/intensity",
    **WAVES_ROUTE_PARAMS["INTENSITY"],
    response_model=GenericResponse[float]
)
def intensity(req: IntensityRequest):
    return WavesControllers.get_intensity(req)

@Waves_Router.post(
    "/refractive_index",
    **WAVES_ROUTE_PARAMS["REFRACTIVE_INDEX"],
    response_model=GenericResponse[float]
)
def refractive_index(req: RefractiveIndexRequest):
    return WavesControllers.get_refractive_index(req)

@Waves_Router.post(
    "/doppler_effect",
    **WAVES_ROUTE_PARAMS["DOPPLER_EFFECT"],
    response_model=GenericResponse[bool]
)
def doppler_effect(req: DopplerEffectRequest):
    return WavesControllers.get_doppler_effect(req)

@Waves_Router.post(
    "/angular_frequency",
    **WAVES_ROUTE_PARAMS["ANGULAR_FREQUENCY"],
    response_model=GenericResponse[float]
)
def angular_frequency(req: AngularFrequencyRequest):
    return WavesControllers.get_angular_frequency(req)

@Waves_Router.post(
    "/speed",
    **WAVES_ROUTE_PARAMS["WAVE_SPEED"],
    response_model=GenericResponse[float]
)
def wave_speed(req: WaveSpeedRequest):
    return WavesControllers.get_wave_speed(req)

@Waves_Router.post(
    "/sound_intensity",
    **WAVES_ROUTE_PARAMS["SOUND_INTENSITY"],
    response_model=GenericResponse[float]
)
def sound_intensity(req: SoundIntensityRequest):
    return WavesControllers.get_sound_intensity(req)

@Waves_Router.post(
    "/sound_level",
    **WAVES_ROUTE_PARAMS["SOUND_LEVEL"],
    response_model=GenericResponse[float]
)
def sound_level(req: SoundLevelRequest):
    return WavesControllers.get_sound_level(req)

@Waves_Router.post(
    "/beats_frequency",
    **WAVES_ROUTE_PARAMS["BEATS_FREQUENCY"],
    response_model=GenericResponse[float]
)
def beats_frequency(req: BeatsFrequencyRequest):
    return WavesControllers.get_beats_frequency(req)

@Waves_Router.post(
    "/beats_period",
    **WAVES_ROUTE_PARAMS["BEATS_PERIOD"],
    response_model=GenericResponse[float]
)
def beats_period(req: BeatsPeriodRequest):
    return WavesControllers.get_beats_period(req)

