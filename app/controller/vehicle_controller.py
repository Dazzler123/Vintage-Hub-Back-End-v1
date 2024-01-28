from fastapi import APIRouter, HTTPException

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
        # raise HTTPException(status_code=500, detail="Internal Server Error")
        return "Error!!"
