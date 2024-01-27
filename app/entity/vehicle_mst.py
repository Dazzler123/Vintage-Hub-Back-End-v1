from sqlalchemy import Column, String, Boolean, Float, Integer, CHAR
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class VehicleMst(Base):
    __tablename__ = "vehicle_mst"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    registrationNumber = Column("registration_no", String(length=50))
    model = Column("model", String(length=50))
    make = Column("make", String(length=50))
    yom = Column("yom", Integer)
    mileageKmpl = Column("mileage_kmpl", Float)
    fuelType = Column("fuel_type", CHAR)
    engineCapacityCc = Column("engine_capacity_cc", Float)
    transmission = Column("transmission", String(length=50))
    drivetrain = Column("drivetrain", String(length=50))
    horsepower = Column("horsepower", String(length=50))
    color = Column("color", String(length=100))
    bodyType = Column("body_type", String(length=50))


    def __init__(self, registrationNumber, model, make, yom, mileageKmpl, fuelType, engineCapacityCc, transmission,
                 drivetrain, horsepower, color, bodyType):
        self.registrationNumber = registrationNumber
        self.model = model
        self.make = make
        self.yom = yom
        self.mileageKmpl = mileageKmpl
        self.fuelType = fuelType
        self.engineCapacityCc = engineCapacityCc
        self.transmission = transmission
        self.drivetrain = drivetrain
        self.horsepower = horsepower
        self.color = color
        self.bodyType = bodyType
