from fastapi import APIRouter

from app.models.part_dto import PartDTO
from app.service.part_service_impl import PartsService

router = APIRouter()


@router.post('/api/parts/v1-create-part')
async def createPart(part: PartDTO):
    return PartsService.create_part(part)
