"""
    Imported Libraries
"""
import os
import warnings

from custom_transformers import transformations_pipeline
from load_data import loadingData
from predict import precit
from preprocess import robustScaler
from sklearn.metrics import classification_report
from train import training

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
URL = "C:\\Users\\jcriollo\\Desktop\\Respado\\ITESM\\Maestría "\
    "Inteligencia Artificial\\Z - MLOPS\\Proyect\\2. Conceptos "\
    "básicos y herramientas para el desarrollo de software\\"

df = loadingData(URL)

df = transformations_pipeline.fit_transform(df)

X_train, X_test, X_val, y_train, y_test, y_val = robustScaler(df)

log_reg = training(X_train, y_train)

y_pred_log_reg_val = precit(X_val)
print(classification_report(y_val, y_pred_log_reg_val, digits=4))
os.remove('creditcard.csv')
