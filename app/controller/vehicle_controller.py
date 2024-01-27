from fastapi import APIRouter

from app.models.vehicle_mst_dto import VehicleMstDTO
from app.service.vehicle_service_impl import VehicleService

router = APIRouter()


@router.get('/api/vehicle/v1-predict-vehicle-price')
async def suggestPrice(vehicle: VehicleMstDTO):
    return VehicleService.predict_price(vehicle)
