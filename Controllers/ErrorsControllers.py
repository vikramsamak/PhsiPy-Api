from libs.phsipy.PhsipyEquations import Errors
from schemas.ErrorsSchema import *
from schemas.GenericSchema import GenericResponse
from dictionaries import ErrorsDictionary

def calculate_error_muldiv(req: ErrorMulDivSchema) -> GenericResponse[float]:
    result = Errors.error_muldiv(req.a, req.b, req.c, req.d)
    return GenericResponse(
        Definition=ErrorsDictionary.ErrorsDict["error_muldiv"],
        Given={"a": req.a, "b": req.b, "c": req.c, "d": req.d},
        Result=result,
    )

def calculate_error_addsub(req: ErrorAddSubSchema) -> GenericResponse[float]:
    result = Errors.error_addsub(req.a, req.b)
    return GenericResponse(
        Definition=ErrorsDictionary.ErrorsDict["error_addsub"],
        Given={"a": req.a, "b": req.b},
        Result=result,
    )

def calculate_percentage_error(req: PercentageErrorSchema) -> GenericResponse[None]:
    Errors.percentage_error(req.M, req.E)
    return GenericResponse(
        Definition=ErrorsDictionary.ErrorsDict["percentage_error"],
        Given={"Measured Value": req.M, "Expected Value": req.E},
        Result="Calculation performed, check console for output.",
    )

def calculate_absolute_error(req: AbsoluteErrorSchema) -> GenericResponse[float]:
    result = Errors.absolute_error(req.a, req.n)
    return GenericResponse(
        Definition=ErrorsDictionary.ErrorsDict["absolute_error"],
        Given={"Values": req.a, "Count": req.n},
        Result=result,
    )

def calculate_mean_absolute_error(req: MeanAbsoluteErrorSchema) -> GenericResponse[float]:
    result = Errors.meanabsolute_error(req.a, req.n)
    return GenericResponse(
        Definition=ErrorsDictionary.ErrorsDict["mean_absolute_error"],
        Given={"Values": req.a, "Count": req.n},
        Result=result,
    )
