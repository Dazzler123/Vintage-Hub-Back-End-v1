from fastapi import APIRouter

from app.models.vehicle_mst_dto import VehicleMstDTO
from app.service.vehicle_service_impl import VehicleService

router = APIRouter()


@router.put('/api/vehicle/v1-predict-vehicle-price')
async def suggestPrice(vehicle: VehicleMstDTO):
    try:
        print(vehicle, "Vehicle")
        return VehicleService.predict_price(vehicle)
    except Exception as e:
        print(f"An error occurred: {e}")
        return f"An error occurred: {e}"


@router.get('/api/vehicle/v1-get-vehicle-makes')
async def getVehicleMakes(self=None):
    try:
        return VehicleService.get_all_makes(self)
    except Exception as e:
        print(f"An error occurred: {e}")
        return f"An error occurred: {e}"


@router.get('/api/vehicle/v1-get-matching-vehicle-models')
async def getVehicleModels(make: str):
    try:
        return VehicleService.get_matching_models(make)
    except Exception as e:
        print(f"An error occurred: {e}")
        return f"An error occurred: {e}"
