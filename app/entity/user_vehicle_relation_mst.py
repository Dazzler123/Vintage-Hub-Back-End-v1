from sqlalchemy import Column, String, Boolean, Float, Integer
from sqlalchemy.ext.declarative import declarative_base

RelationBase = declarative_base()


class UserVehicleRelationMst(RelationBase):
    __tablename__ = "user_vehicle_relation_mst"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    userId = Column("user_id", Integer)
    vehicleId = Column("vehicle_mst_id", Integer)
    createdOn = Column("created_on", String(length=150))
    condition = Column("condition", String(length=10))
    serviceHistory = Column("service_history", String(length=255))
    accidentHistory = Column("accident_history", String(length=255))
    previousOwners = Column("previous_owners", Float)
    vehiclePrice = Column("vehicle_price", Float)
    negotiable = Column("negotiable", Boolean)
    includeContractors = Column("include_contractors", String(length=10))

    def __init__(self, userId, vehicleId, createdOn, condition, serviceHistory, accidentHistory, previousOwners,
                 vehiclePrice, negotiable, includeContractors):
        self.userId = userId
        self.vehicleId = vehicleId
        self.createdOn = createdOn
        self.condition = condition
        self.serviceHistory = serviceHistory
        self.accidentHistory = accidentHistory
        self.previousOwners = previousOwners
        self.vehiclePrice = vehiclePrice
        self.negotiable = negotiable
        self.includeContractors = includeContractors
