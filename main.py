from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from Routes.ElectricityRoutes import Electricity_router
from Routes.SubAutomaticRoutes import SubAutomatic_Router

app = FastAPI()


@app.get("/", tags=["Welcome"])
def index():
    return {"res": "Welcome to the PhsiPy-API"}


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="PhsiPy-API",
        version="1.0.0",
        description="Rest API for making scientific calculations easy.",
        routes=app.routes,
    )

    openapi_schema["info"]["x-logo"] = {
        "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi

# Electricity Route
app.include_router(Electricity_router, prefix="/electricity")

# SubAutomatic Route
app.include_router(SubAutomatic_Router, prefix="/subautomatic")
