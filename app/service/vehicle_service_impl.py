import pickle
import pandas as pd
import numpy as np

from app.models.vehicle_mst_dto import VehicleMstDTO


class VehicleService:

    # This function is used to suggest user a price using given vehicle specifications.
    def predict_price(self: VehicleMstDTO):
        print(self.make)
        model = pickle.load(open('../../LinearRegressionModel.pkl', 'rb'))
        car = pd.read_csv('../../Cleaned_Car_data.csv')

        prediction = model.predict(pd.DataFrame(columns=['name', 'company', 'year', 'kms_driven', 'fuel_type'],
                                                data=np.array(["Maruti Suzuki Swift", "Maruti", 2019, 100,
                                                               "Petrol"]).reshape(1, 5)))
        print(prediction)

        return str(np.round(prediction[0], 2))
