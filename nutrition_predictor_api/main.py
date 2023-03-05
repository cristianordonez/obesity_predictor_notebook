import os
import warnings

import joblib
# from dotenv import load_dotenv
from elasticsearch import Elasticsearch

import utils

warnings.filterwarnings("ignore")
# load_dotenv(override=True)


# create map dictionaries
# gender_map = {"Male": 0, "Female": 1}
# family_history_map = {"yes": 1, "no": 0}
# favc_map = {"yes": 1, "no": 0}
# caec_map = {"Always": 1.00, "Frequently": 0.67, "Sometimes": 0.33, "no": 0.00 }
# smoke_map = {"yes": 1, "no": 0}
# scc_map = {"yes": 1, "no": 0}
# calc_map = {"Always": 1.00, "Frequently": 0.67, "Sometimes": 0.33, "no": 0.00 }
# mtrans_map = {"Automobile": 1.00, "Motorbike": 0.75, "Bike": 0.50, "Public_Transportation": 0.25, "Walking": 0.00}
# nobesity_map = {"Obesity_Type_III": 0, "Obesity_Type_II": 1, "Obesity_Type_I": 2, "Overweight_Level_II": 3, "Overweight_Level_I": 4, "Normal_Weight": 5, "Insufficient_Weight": 6}
# feature_col_names = ['Gender', 'Age', 'Height', 'Weight', 'family_history_with_overweight', 'FAVC', 'FCVC', 'NCP', 'CAEC', 'SMOKE', 'CH2O', 'SCC', 'FAF', 'TUE', 'CALC', 'MTRANS']

def predict_obesity_risk(attributes): 
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, 'rf_model.joblib')
    rf = joblib.load(file_path)
    prediction = rf.predict(attributes)
    return prediction 

def main():
    try:
        client_local = Elasticsearch("http://localhost:9200")
    except ConnectionError as err:
        print("Unable to connect to local Elasticsearch db: ", err)
        client_local = None
    if client_local != None: 
        utils.read_data()
        prediction = predict_obesity_risk([[1, 27, 1.7018, 68, 0, 1, 2.0, 2.0, 0.67, 0, 1.0, 0, 4.0, 4.0, 0.33, 0]])
        print('prediction: ', prediction)

if __name__ == "__main__":
    main()