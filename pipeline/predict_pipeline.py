import os
import sys
import pandas as pd
from src.exception import CustomException
from src.utils import load_object

class PredictPipeline:
    def __init__(self):
        pass

    def predict(self, features):
        try:
            # Use os.path.join to ensure correct path separators
            model_path = os.path.join('artifacts', 'modeltraining.pkl')
            preprocessor_path = os.path.join('artifacts', 'preprocessor.pkl')
            
            model = load_object(file_path=model_path)
            preprocessor = load_object(file_path=preprocessor_path)
            data_scaled = preprocessor.transform(features)
            return model.predict(data_scaled)
        
        except Exception as e:
            raise CustomException(e, sys)

class CustomData:
    def __init__(self,
                 age: int,
                 sex: str,
                 bmi: float,
                 children: int,
                 smoker: str,
                 region: str):
        self.age = age
        self.sex = sex
        self.bmi = bmi
        self.children = children
        self.smoker = smoker
        self.region = region

    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "age": [self.age],
                "sex": [self.sex],
                "bmi": [self.bmi],
                "children": [self.children],
                "smoker": [self.smoker],
                "region": [self.region]
            }
        
            return pd.DataFrame(custom_data_input_dict)
        
        except Exception as e:
            raise CustomException(e, sys)
