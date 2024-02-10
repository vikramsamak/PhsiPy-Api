from fastapi import FastAPI

from Routes.ElectricityRoutes import Electricity_router

app = FastAPI()


@app.get("/")
def index():
    return {"res": "Welcome to the PhsiPy-API"}


# Electricity Route
app.include_router(Electricity_router, prefix="/electricity")
