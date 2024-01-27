from fastapi import APIRouter

from app.models.part_dto import PartDTO
from app.service.part_service_impl import PartsService

router = APIRouter()


@router.get('/api/vehicle/v1-predict-vehicle-price')
async def createPart(part: PartDTO):
    return PartsService.create_part(part)
