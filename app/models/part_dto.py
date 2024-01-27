from pydantic import BaseModel


class PartDTO(BaseModel):
    title: str
    make: str
    partNumber: str
    manufacturer: str
    oem: bool | None = False
    aftermarket: bool | None = False
    condition: str
    description: str | None = None
    compatibility: str | None = None
    additionalInfo: str | None = None
    price: float | None = None
    negotiable: bool | None = False
