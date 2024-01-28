from fastapi import APIRouter

from app.models.other_accessory_mst_dto import OtherAccessoryMstDTO
from app.service.other_accessory_service_impl import OtherAccessoryService

router = APIRouter()


@router.post('/api/other/v1-create-other')
async def createOtherAccessory(item: OtherAccessoryMstDTO):
    return OtherAccessoryService.create_other_accessory(item)
