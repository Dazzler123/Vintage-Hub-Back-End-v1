from fastapi import APIRouter

from app.models.parts import Part
from app.service.PartServiceImpl import PartsService

router = APIRouter()


@router.post('/api/parts/v1-create-part')
async def createPart(part: Part):
    print(part)
    status = PartsService.create_part(part)

    return status
