import numpy as np
import pandas as pd
import pickle
from xgboost import XGBClassifier

def predict(features) :
    xgb = pickle.load(open('Phishing_detector/trained_model.model', 'rb'))
    features = np.array(features).reshape((1,-1))
    cols_when_model_builds = xgb.get_booster().feature_names
    df = pd.DataFrame(features) 
    df.columns = ['Have_IP', 'Have_At', 'URL_Length', 'URL_Depth', 'Redirection', 'https_Domain', 'TinyURL', 'Prefix/Suffix', 'DNS_Record', 'Web_Traffic', 'Domain_Age', 'Domain_End', 'iFrame', 'Mouse_Over', 'Right_Click', 'Web_Forwards']
    print(xgb.predict(df))


# if __name__ == '__main__' :
    # features = [0, 0, 1, 2, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0]
    # predict(features)