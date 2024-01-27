from sqlalchemy import Column, String, Boolean, Float, Integer, CHAR
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Part(Base):
    __tablename__ = "part"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    title = Column("title", String(length=50))
    make = Column("make", String(length=50))
    partNumber = Column("part_number", String(length=150))
    manufacturer = Column("manufacturer", String(length=50))
    oem = Column("oem", Boolean)
    aftermarket = Column("aftermarket", Boolean)
    condition = Column("condition", CHAR)
    description = Column("description", String(length=255))
    compatibility = Column("compatibility", String(length=255))
    additionalInfo = Column("additionalInfo", String(length=255))
    price = Column("price", Float)
    negotiable = Column("negotiable", Boolean)

    def __init__(self, title, make, partNumber, manufacturer, oem, aftermarket, condition, description,
                 compatibility, additionalInfo, price, negotiable):
        self.title = title
        self.make = make
        self.partNumber = partNumber
        self.manufacturer = manufacturer
        self.oem = oem
        self.aftermarket = aftermarket
        self.condition = condition
        self.description = description
        self.compatibility = compatibility
        self.additionalInfo = additionalInfo
        self.price = price
        self.negotiable = negotiable
