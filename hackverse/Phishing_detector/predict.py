import numpy as np
import pandas as pd
import pickle

def predict(features) :
    xgb = pickle.load(open('Phishing_detector/trained_model.model', 'rb'))
    features = np.array(features).reshape((1,-1))
    df = pd.DataFrame(features) 
    ans = xgb.predict(df)[0]
    return ans


# if __name__ == '__main__' :
    # features = [0, 0, 1, 2, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0]
    # predict(features)