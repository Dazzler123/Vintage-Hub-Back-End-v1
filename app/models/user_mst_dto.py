from pydantic import BaseModel


class UserMstDTO(BaseModel):
    userFullName: str
    userAddress: str
    userNic: str
    userEmailAddress: str
    userContactNo: str
    userDLNo: str
    userGender: str
    userNewUserName: str
    userNewPassword: str
