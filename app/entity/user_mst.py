from sqlalchemy import Column, String, Integer, CHAR
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class UserMst(Base):
    __tablename__ = "user_mst"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    name = Column("name", String(length=100))
    address = Column("address", String(length=255))
    nic = Column("nic", String(length=50))
    email = Column("email", String(length=100))
    contactNo = Column("contact", String(length=50))
    drivingLicenseNo = Column("driving_license_no", String(length=50))
    gender = Column("gender", CHAR)
    username = Column("username", String(length=255))
    password = Column("enc_password", String(length=255))

    def __init__(self, name, address, nic, email, contactNo, drivingLicenseNo, gender,
                 username, password):
        self.name = name
        self.address = address
        self.nic = nic
        self.email = email
        self.contactNo = contactNo
        self.drivingLicenseNo = drivingLicenseNo
        self.gender = gender
        self.username = username
        self.password = password
