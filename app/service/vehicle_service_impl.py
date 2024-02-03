import os
import pickle
import pandas as pd
import numpy as np

from app.models.vehicle_mst_dto import VehicleMstDTO

file_path = os.path.abspath("cleaned car data.csv")
car = pd.read_csv(file_path)


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
    def predict_price(self: VehicleMstDTO):
        print(self.make)

        file_path = os.path.abspath("LinearRegressionModel.pkl")
        print(file_path)
        model = pickle.load(open(file_path, 'rb'))

        prediction = model.predict(pd.DataFrame(columns=['name', 'company', 'year', 'kms_driven', 'fuel_type'],
                                                data=np.array(["Maruti Suzuki Swift", "Maruti", 2019, 100, "Petrol"]).
                                                reshape(1, 5)))
        print(prediction)
        return str(np.round(prediction[0], 2))
