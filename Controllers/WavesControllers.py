from dictionaries.WavesDictionary import WavesDict
from libs.phsipy.PhsipyEquations import Waves
from schemas.WavesSchema import *
from schemas.GenericSchema import GenericResponse

def calculate_wave_velocity(req: WaveVelocitySchema) -> GenericResponse[float]:
    velocity = Waves.wave_velocity(req.frequency, req.wavelength)
    return GenericResponse(
        Definition=WavesDict["wave_velocity"],
        Given={"Frequency": req.frequency, "Wavelength": req.wavelength},
        Result=velocity,
    )

def calculate_wave_period(req: WavePeriodSchema) -> GenericResponse[float]:
    period = Waves.wave_period(req.frequency)
    return GenericResponse(
        Definition=WavesDict["wave_period"],
        Given={"Frequency": req.frequency},
        Result=period,
    )

def calculate_wave_number(req: WaveNumberSchema) -> GenericResponse[float]:
    wave_number = Waves.wave_number(req.wavelength)
    return GenericResponse(
        Definition=WavesDict["wave_number"],
        Given={"Wavelength": req.wavelength},
        Result=wave_number,
    )

def calculate_intensity(req: IntensitySchema) -> GenericResponse[float]:
    intensity = Waves.intensity(req.power, req.area)
    return GenericResponse(
        Definition=WavesDict["intensity"],
        Given={"Power": req.power, "Area": req.area},
        Result=intensity,
    )

def calculate_refractive_index(req: RefractiveIndexSchema) -> GenericResponse[float]:
    refractive_index = Waves.refractive_index(req.real_depth, req.apparent_depth)
    return GenericResponse(
        Definition=WavesDict["refractive_index"],
        Given={"Real Depth": req.real_depth, "Apparent Depth": req.apparent_depth},
        Result=refractive_index,
    )

def calculate_doppler_effect(req: DopplerEffectSchema) -> GenericResponse[bool]:
    doppler_effect_result = Waves.doppler_effect(
        req.observed_frequency,
        req.source_frequency,
        req.wave_velocity,
        req.observer_velocity,
        req.source_velocity,
    )
    return GenericResponse(
        Definition=WavesDict["doppler_effect"],
        Given={
            "Observed Frequency": req.observed_frequency,
            "Source Frequency": req.source_frequency,
            "Wave Velocity": req.wave_velocity,
            "Observer Velocity": req.observer_velocity,
            "Source Velocity": req.source_velocity,
        },
        Result=doppler_effect_result,
    )

def calculate_angular_frequency(req: AngularFrequencySchema) -> GenericResponse[float]:
    angular_frequency = Waves.angular_frequency(req.frequency)
    return GenericResponse(
        Definition=WavesDict["angular_frequency"],
        Given={"Frequency": req.frequency},
        Result=angular_frequency,
    )

def calculate_wave_speed(req: WaveSpeedSchema) -> GenericResponse[float]:
    wave_speed = Waves.wave_speed(req.wavelength, req.period)
    return GenericResponse(
        Definition=WavesDict["wave_speed"],
        Given={"Wavelength": req.wavelength, "Period": req.period},
        Result=wave_speed,
    )

def calculate_sound_intensity(req: SoundIntensitySchema) -> GenericResponse[float]:
    sound_intensity = Waves.sound_intensity(req.sound_power, req.area)
    return GenericResponse(
        Definition=WavesDict["sound_intensity"],
        Given={"Sound Power": req.sound_power, "Area": req.area},
        Result=sound_intensity,
    )

def calculate_sound_level(req: SoundLevelSchema) -> GenericResponse[float]:
    sound_level = Waves.sound_level(req.intensity)
    return GenericResponse(
        Definition=WavesDict["sound_level"],
        Given={"Intensity": req.intensity},
        Result=sound_level,
    )

def calculate_beats_frequency(req: BeatsFrequencySchema) -> GenericResponse[float]:
    beats_frequency = Waves.beats_frequency(req.frequency1, req.frequency2)
    return GenericResponse(
        Definition=WavesDict["beats_frequency"],
        Given={"Frequency 1": req.frequency1, "Frequency 2": req.frequency2},
        Result=beats_frequency,
    )

def calculate_beats_period(req: BeatsPeriodSchema) -> GenericResponse[float]:
    beats_period = Waves.beats_period(req.frequency1, req.frequency2)
    return GenericResponse(
        Definition=WavesDict["beats_period"],
        Given={"Frequency 1": req.frequency1, "Frequency 2": req.frequency2},
        Result=beats_period,
    )
