import numpy as np
import pandas as pd
from sklearn import preprocessing,metrics,ensemble,pipeline
from sklearn.impute import MissingIndicator
from  sklearn_pandas import DataFrameMapper
import joblib
data=pd.read_csv('auto-mpg.csv')
print(data.head())
print(data.isnull().sum())
mapper =DataFrameMapper([
    (['cylinders','displacement','weight','acceleration','model year'],preprocessing.StandardScaler()),
    (['horsepower'],MissingIndicator()),
    (['origin'],preprocessing.OneHotEncoder(handle_unknown="ignore",sparse=False))
])
pipeline_obj=pipeline.Pipeline([
    ('mapper',mapper),
    ('model',ensemble.RandomForestRegressor())
])
print(data.columns)
X=['cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model year', 'origin']
Y=['mpg']
pipeline_obj.fit(data[X],data[Y].values.ravel())
print(pipeline_obj.predict(data[X]))
joblib.dump(pipeline_obj,'MPG_MODEL.pkl')
model_reload=joblib.load('MPG_MODEL.pkl')
print(data[X])
print(model_reload.predict(data[X]))
