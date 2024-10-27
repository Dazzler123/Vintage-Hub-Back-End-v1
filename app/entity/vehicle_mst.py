from sqlalchemy import Column, String, Boolean, Float, Integer, CHAR
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class VehicleMst(Base):
    __tablename__ = "vehicle_mst"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    registrationNo = Column("registration_no", String(length=50))
    model = Column("model", String(length=50))
    make = Column("make", String(length=50))
    yom = Column("yom", Integer)
    mileageKmpl = Column("mileage_kmpl", String(length=50))
    odometer = Column("odometer_kms", Float)
    fuelType = Column("fuel_type", String(length=10))
    engineCapacityCc = Column("engine_capacity_cc", Float)
    transmission = Column("transmission", String(length=50))
    drivetrain = Column("drivetrain", String(length=50))
    horsepower = Column("horsepower", String(length=50))
    color = Column("color", String(length=100))
    bodyType = Column("body_type", String(length=50))

    def __init__(self, registrationNo, model, make, yom, mileageKmpl, odometer, fuelType, engineCapacityCc,
                 transmission,
                 drivetrain, horsepower, color, bodyType):
        self.registrationNo = registrationNo
        self.model = model
        self.make = make
        self.yom = yom
        self.mileageKmpl = mileageKmpl
        self.odometer = odometer
        self.fuelType = fuelType
        self.engineCapacityCc = engineCapacityCc
        self.transmission = transmission
        self.drivetrain = drivetrain
        self.horsepower = horsepower
        self.color = color
        self.bodyType = bodyType
