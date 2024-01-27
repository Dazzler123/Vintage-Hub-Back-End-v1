import pickle
import pandas as pd
import numpy as np

from app.models.part_dto import PartDTO


class VehicleService:

    # This function is used to suggest user a price using given vehicle specifications.
    def predict_price(self: PartDTO):
        model = pickle.load(open('LinearRegressionModel.pkl', 'rb'))
        car = pd.read_csv('resources/datasets/Cleaned_Car_data.csv')

        company = request.form.get('company')
        car_model = request.form.get('car_models')
        year = request.form.get('year')
        fuel_type = request.form.get('fuel_type')
        mileage = request.form.get('kilo_driven')

        prediction = model.predict(pd.DataFrame(columns=['name', 'company', 'year', 'kms_driven', 'fuel_type'],
                                                data=np.array(
                                                    [car_model, company, year, mileage, fuel_type]).reshape(1, 5)))
        print(prediction)

        return str(np.round(prediction[0], 2))

