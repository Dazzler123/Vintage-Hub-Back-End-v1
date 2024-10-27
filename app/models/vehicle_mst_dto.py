from pydantic import BaseModel, constr


class VehicleMstDTO(BaseModel):
    registrationNo: str
    model: str
    make: str
    yom: int
    mileageKmpl: str | None = None
    odometer: float
    fuelType: str | None = None
    engineCapacityCc: float
    transmission: str | None = None
    drivetrain: str | None = None
    horsepower: str | None = None
    color: str | None = None
    bodyType: str | None = None

    wheelSize: str | None = None
    haveSunroof: bool
    isConvertible: bool
    interiorColor: str | None = None
    seatingCapacity: float
    infotainmentSys: str | None = None
    haveAirbags: bool
    absType: str | None = None
    escType: str | None = None
    casType: str | None = None

    condition: str | None = None
    serviceHistory: str | None = None
    accidentHistory: str | None = None
    previousOwners: float
    vehiclePrice: float
    negotiable: bool
    includeContractors: str | None = None
