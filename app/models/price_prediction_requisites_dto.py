from pydantic import BaseModel


class PricePredictionRequisitesDTO(BaseModel):
    model: str | None = None
    make: str | None = None
    yom: str | None = None
    odometer: int | None = 0
    fuelType: str | None = None
