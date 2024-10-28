import os
import pandas as pd
from sklearn.preprocessing import OneHotEncoder, MinMaxScaler, LabelEncoder
from sklearn.pipeline import Pipeline

ROOT_PATH = os.path.dirname(os.path.dirname(__file__))

def model_mvp():
    model_path = os.path.join(ROOT_PATH,'../data/survey_lung_cancer.csv')
    lung_cancer_df = pd.read_csv(model_path)
    # seperating X and y (lung cancer target value) in case both are present
    if 'LUNG_CANCER' in lung_cancer_df.columns:
        #Create X,y
        X = lung_cancer_df.iloc[:,lung_cancer_df.columns!='LUNG_CANCER']
        y = lung_cancer_df.iloc[:,lung_cancer_df.columns=='LUNG_CANCER']
    else:
        X = lung_cancer_df

    pipeline = Pipeline(OneHotEncoder())
