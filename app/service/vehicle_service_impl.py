import datetime
import os
import pickle
import shutil

import pandas as pd
import numpy as np
from fastapi import File, UploadFile, HTTPException
from fastapi.responses import FileResponse
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.entity.user_vehicle_relation_mst import UserVehicleRelationMst
from app.entity.vehicle_mst import Base, VehicleMst
from app.entity.user_vehicle_relation_mst import RelationBase
from app.models.price_prediction_requisites_dto import PricePredictionRequisitesDTO
from app.models.card_detail_dto import CardDetailDTO
from app.models.vehicle_mst_dto import VehicleMstDTO

file_path = os.path.abspath("cleaned car data.csv")
vehicle_img_directory = os.path.abspath("../images/vehicle")
car = pd.read_csv(file_path)

UPLOAD_FOLDER = vehicle_img_directory


class VehicleService:

    # This function is used to get all available vehicle makes
    def get_all_makes(self):

        makes = sorted(car['company'].unique())
        makes.insert(0, 'Select Make')
        return makes

    # This function is used to get matching vehicle models for given vehicle make
    def get_matching_models(self: str):
        makes = sorted(car['company'].unique())
        if self in makes:
            matching_models = car[car['company'] == self]['name'].unique()
            # remove the vehicle make
            matching_models = [model.split(' ', 1)[1] for model in matching_models]
            return sorted(matching_models)
        else:
            return []

    # This function is used to suggest user a price using given vehicle specifications.
    def predict_price(self: PricePredictionRequisitesDTO):
        print(self.make)

        file_path = os.path.abspath("LinearRegressionModel.pkl")
        print(file_path)
        model = pickle.load(open(file_path, 'rb'))

        prediction = model.predict(
            pd.DataFrame(
                columns=['name', 'company', 'year', 'kms_driven', 'fuel_type'],
                data=np.array(
                    [(self.make + " " + self.model), self.make, self.yom, self.odometer, self.fuelType]).reshape(1, 5)))
        # convert into LKR
        prediction = prediction * 3.76
        print(prediction)
        return str(np.round(prediction[0], 2))

    # ===== This function is used to create new vehicle =====
    def create_vehicle(self: VehicleMstDTO):
        engine = create_engine("mysql+mysqlconnector://root:1234@localhost:3306/vintage_hub_db", echo=True)
        Base.metadata.create_all(bind=engine)

        Session = sessionmaker(bind=engine)
        session = Session()

        # save vehicle master object
        vehicle = VehicleMst(self.registrationNo, self.model, self.make, self.yom, self.mileageKmpl,
                             self.odometer, self.fuelType, self.engineCapacityCc, self.transmission,
                             self.drivetrain, self.horsepower, self.color, self.bodyType)

        # Instantiate the VehicleService class
        vehicle_service = VehicleService()

        vehicleRelation = UserVehicleRelationMst("dasinduhewagamage@gmail.com", vehicle.id, datetime.date.today(),
                                                 self.condition, self.serviceHistory, self.accidentHistory,
                                                 self.previousOwners, self.vehiclePrice, self.negotiable,
                                                 self.includeContractors)

        # save user vehicle relation
        vehicle_service.record_user_vehicle_relation(vehicleRelation)

        session.add(vehicle)

        try:
            session.commit()
            return True
        except Exception as e:
            print(f"Error committing the transaction: {e}")
            session.rollback()  # Rollback the transaction in case of an error
            return False
        finally:
            session.close()

    # ===== This function is used record user vehicle relation with details =====
    def record_user_vehicle_relation(self: UserVehicleRelationMst, relation):
        engine = create_engine("mysql+mysqlconnector://root:1234@localhost:3306/vintage_hub_db", echo=True)
        RelationBase.metadata.create_all(bind=engine)

        Session = sessionmaker(bind=engine)
        session = Session()

        session.add(self)

        try:
            session.commit()
            return True
        except Exception as e:
            print(f"Error committing the transaction: {e}")
            session.rollback()  # Rollback the transaction in case of an error
            return False
        finally:
            session.close()

    # ===== This function is used save vehicle images in a local location =====
    def upload_image_local(fileName: str, file: UploadFile = File(...)):
        try:
            # Create the directory if it does not exist
            os.makedirs(UPLOAD_FOLDER, exist_ok=True)

            with open(os.path.join(UPLOAD_FOLDER, fileName), "wb") as image:
                shutil.copyfileobj(file.file, image)
            return {"message": "Image uploaded successfully"}
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error saving image: {str(e)}")

    # ===== This function is used save vehicle images in a local location =====
    def load_image(fileName: str):
        try:
            return FileResponse(os.path.join(UPLOAD_FOLDER, fileName))
        except Exception as e:
            raise HTTPException(status_code=404, detail="Image not found")

    # ===== This function is used get vehicle card details =====
    def fetch_vehicle_card_detail(self: None):
        try:

            # TODO get all available vehicle ids with their names for sale (create a loop
            #  ,push to an array and return)

            vehicleId = 1
            name = "Daihatsu Mira ES"
            fileNamePrefix = name + "_" + "1" + "First"  # get first name
            imageFile = FileResponse(os.path.join(UPLOAD_FOLDER, "Daihatsu Mira ES_1_First.png"))
            card1 = CardDetailDTO()
            card1.id = vehicleId
            card1.name = name
            card1.image = imageFile

            # vehicleId = 2
            # name = "Suzuki Swift RS"
            # fileNamePrefix = name + "_" + vehicleId + "First"  # get first name
            # imageFile = FileResponse(os.path.join(UPLOAD_FOLDER, fileNamePrefix + ".png"))
            # card2 = CardDetailDTO(vehicleId, name, imageFile)

            cards = {card1}

            return cards
        except Exception as e:
            raise HTTPException(status_code=404, detail=e)
