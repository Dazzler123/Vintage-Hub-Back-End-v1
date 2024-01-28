from pydantic import BaseModel, constr


class UserMstDTO(BaseModel):
    name: str
    address: str
    nic: str
    email: str
    contactNo: str
    drivingLicenseNo: str
    gender: constr(min_length=1, max_length=1)
    username: str
    password: str
