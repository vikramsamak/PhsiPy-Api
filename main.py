from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from Routes.ElectricityRoutes import Electricity_router
from Routes.SubAutomaticRoutes import SubAutomatic_Router
from Routes.NlmRoutes import NLMRouter
import uvicorn
from os import getenv
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="PhsiPy API",
    description="Rest API for making scientific calculations easy.",
    version="1.0.0",
)

origins = [
    "http://localhost:8081",
    "*",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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


@app.get("/", tags=["Welcome"])
def index():
    return {"res": "Welcome to the PhsiPy-API"}


app.openapi = custom_openapi

# Electricity Route
app.include_router(Electricity_router, prefix="/electricity")

# SubAutomatic Route
# app.include_router(SubAutomatic_Router, prefix="/subautomatic")

# NLM Routes
app.include_router(NLMRouter, prefix="/nlm")

if __name__ == "__main__":
    port = int(getenv("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)
