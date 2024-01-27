from fastapi import APIRouter

from app.models.part_mst_dto import PartMstDTO
from app.service.part_service_impl import PartsService

router = APIRouter()


@router.post('/api/parts/v1-create-part')
async def createPart(part: PartMstDTO):
    return PartsService.create_part(part)
