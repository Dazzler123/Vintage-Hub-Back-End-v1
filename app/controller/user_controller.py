from fastapi import APIRouter

from app.models.user_mst_dto import UserMstDTO
from app.service.user_service_impl import UserService

router = APIRouter()


@router.post('/api/user/v1-create-user')
async def createUser(user: UserMstDTO):
    return UserService.create_user(user)
