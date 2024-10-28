import os
import pandas as pd
from sklearn.preprocessing import OneHotEncoder, MinMaxScaler, LabelEncoder
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LogisticRegression
import pickle

ROOT_PATH = os.path.dirname(os.path.dirname(__file__))

#Create a function to preprocess X
def preprocessing_model_tabular_data(df):

    if 'LUNG_CANCER' in df.columns:
        X = df.iloc[:,df.columns!='LUNG_CANCER']
        y = df.iloc[:,df.columns=='LUNG_CANCER']
        label_encoder = LabelEncoder() # we create the labelEncoder from Sklearn
        y_encoded = label_encoder.fit_transform(y) # We train and transform at the same time to obtain y_encoded
        y_encoded = pd.DataFrame(y_encoded, columns=['LUNG_CANCER'])
    else:
        X = df
        y_encoded = None

    cancer_column_transformer= ColumnTransformer(
    [('binary_data', OneHotEncoder(drop='if_binary'),['GENDER', 'SMOKING', 'YELLOW_FINGERS', 'ANXIETY',
       'PEER_PRESSURE', 'CHRONIC DISEASE', 'FATIGUE ', 'ALLERGY ', 'WHEEZING',
       'ALCOHOL CONSUMING', 'COUGHING', 'SHORTNESS OF BREATH',
       'SWALLOWING DIFFICULTY', 'CHEST PAIN']),
    ('continues_data', MinMaxScaler(), ['AGE'])]
)

    preprocessed_data_X= cancer_column_transformer.fit_transform(X)

    return preprocessed_data_X, y_encoded

#Encode the target and model with the preprocess data
def modeling(df):

    model_path = os.path.join(ROOT_PATH, 'models', 'mvp_model.pkl')
    model = LogisticRegression.fit(preprocessing_model_tabular_data(df)[0], preprocessing_model_tabular_data(df)[1])

    # Export the model as a pickle file, we might need to create a models folder on the taabolar data folder
    with open(model_path, 'wb') as file:
        pickle.dump(model, file)

def prediction_tabular_data(gender,age, smoking,yellow_fingers, anxiety, chronic_disease, fatigue, allergy, wheezing, alcoholl, coughing, shortness_breath,swalloging_difficulty, chest_pain):

    tabular_to_predict = pd.DataFrame((gender,smoking,yellow_fingers, anxiety, chronic_disease, fatigue, allergy, wheezing, alcoholl, coughing, shortness_breath,swalloging_difficulty, chest_pain, age), columns=['GENDER', 'SMOKING', 'YELLOW_FINGERS', 'ANXIETY',
       'PEER_PRESSURE', 'CHRONIC DISEASE', 'FATIGUE ', 'ALLERGY ', 'WHEEZING',
       'ALCOHOL CONSUMING', 'COUGHING', 'SHORTNESS OF BREATH',
       'SWALLOWING DIFFICULTY', 'CHEST PAIN','AGE'])

    model_path = os.path.join(ROOT_PATH, 'models', 'mvp_taboolar_data.pkl')

    #LOAD THE MODEL
    with open(model_path, 'rb') as file:

        model = pickle.load(file)

    #PREDICT
    prediction = model.predict(tabular_to_predict)

    return prediction
