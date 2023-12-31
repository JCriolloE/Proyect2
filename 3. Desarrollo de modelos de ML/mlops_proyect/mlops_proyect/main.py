"""
    Imported Libraries
"""
import os
import warnings

from classifier.predict import Prediction
from load.load_data import Loading
from preprocess.custom_transformers import transformations_pipeline
from preprocess.preprocess import Preprocessing
from sklearn.metrics import classification_report
from train.train import training

warnings.filterwarnings("ignore")

SEED_SPLIT = 42
TARGET = 'Class'
COLUMNS_NAME = [
    'Time',
    'V1',
    'V2',
    'V3',
    'V4',
    'V5',
    'V6',
    'V7',
    'V8',
    'V9',
    'V10',
    'V11',
    'V12',
    'V13',
    'V14',
    'V15',
    'V16',
    'V17',
    'V18',
    'V19',
    'V20',
    'V21',
    'V22',
    'V23',
    'V24',
    'V25',
    'V26',
    'V27',
    'V28',
    'Amount',
    'Class']
URL = "C:\\Users\\jcriollo\\Desktop\\Respado\\ITESM\\Maestría Inteligencia " \
    "Artificial\\Z - MLOPS\\Proyect\\3. Desarrollo de modelos de ML\\" \
    "mlops_proyect\\mlops_proyect\\data\\"

df = Loading.loadingData(URL)

df = transformations_pipeline.fit_transform(df)

X_train, X_test, X_val, y_train, y_test, y_val = Preprocessing.robustScaler(df)

log_reg = training(X_train, y_train)

y_pred_log_reg_val = Prediction.predict(X_val)
print(classification_report(y_val, y_pred_log_reg_val, digits=4))
os.remove('creditcard.csv')
