from fastapi import APIRouter, File, UploadFile, HTTPException

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


@router.post('/api/vehicle/v1-create-vehicle')
async def createVehicle(vehicle: VehicleMstDTO):
    try:
        return VehicleService.create_vehicle(vehicle)
    except Exception as e:
        print(f"An error occurred: {e}")
        return f"An error occurred: {e}"


@router.post("/api/vehicle/v1-upload-vehicle-image")
async def upload_images(fileName: str, file: UploadFile = File(...)):
    try:
        return VehicleService.upload_image_local(fileName, file)
    except Exception as e:
        print(f"An error occurred: {e}")
        return f"An error occurred: {e}"


@router.get("/api/vehicle/v1-get-vehicle-image")
async def get_image(filename: str):
    try:
        return VehicleService.load_image(filename)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Image not found")

@router.get("/api/vehicle/v1-get-vehicle-cards")
async def get_vehicle_card_detail():
    try:
        return VehicleService.fetch_vehicle_card_detail(None)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Image not found")
