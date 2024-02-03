from fastapi import APIRouter

from app.models.price_prediction_requisites_dto import PricePredictionRequisitesDTO
from app.models.vehicle_mst_dto import VehicleMstDTO
from app.service.vehicle_service_impl import VehicleService

router = APIRouter()


@router.post('/api/vehicle/v1-predict-vehicle-price')
async def suggestPrice(pricePredictionDto: PricePredictionRequisitesDTO):
    try:
        print("Vehicle Details : ", pricePredictionDto)
        return VehicleService.predict_price(pricePredictionDto)
    except Exception as e:
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
