from pydantic import BaseModel, constr


class VehicleMstDTO(BaseModel):
    registrationNumber: str
    model: str
    make: str
    yom: int
    mileageKmpl: float
    odometer: float
    fuelType: constr(min_length=1, max_length=1)
    engineCapacityCc: float
    transmission: str | None = None
    drivetrain: str | None = None
    horsepower: str | None = None
    color: str | None = None
    bodyType: str | None = None
