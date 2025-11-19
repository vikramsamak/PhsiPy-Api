from fastapi import APIRouter
from controllers import ErrorsControllers
from schemas.ErrorsSchema import *
from constants import ErrorsConstants

Errors_Router = APIRouter(tags=["Errors"])

ERRORS_ROUTE_PARAMS = ErrorsConstants.ERRORS_ROUTE_PARAMS

@Errors_Router.post("/muldiv", **ERRORS_ROUTE_PARAMS["ERROR_MULDIV"])
def calculate_error_muldiv(req: ErrorMulDivSchema):
    return ErrorsControllers.calculate_error_muldiv(req)

@Errors_Router.post("/addsub", **ERRORS_ROUTE_PARAMS["ERROR_ADDSUB"])
def calculate_error_addsub(req: ErrorAddSubSchema):
    return ErrorsControllers.calculate_error_addsub(req)

@Errors_Router.post("/percentage", **ERRORS_ROUTE_PARAMS["PERCENTAGE_ERROR"])
def calculate_percentage_error(req: PercentageErrorSchema):
    return ErrorsControllers.calculate_percentage_error(req)

@Errors_Router.post("/absolute", **ERRORS_ROUTE_PARAMS["ABSOLUTE_ERROR"])
def calculate_absolute_error(req: AbsoluteErrorSchema):
    return ErrorsControllers.calculate_absolute_error(req)

@Errors_Router.post("/mean-absolute", **ERRORS_ROUTE_PARAMS["MEAN_ABSOLUTE_ERROR"])
def calculate_mean_absolute_error(req: MeanAbsoluteErrorSchema):
    return ErrorsControllers.calculate_mean_absolute_error(req)
