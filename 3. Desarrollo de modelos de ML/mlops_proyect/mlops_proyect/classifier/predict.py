from joblib import load

class Prediction:

    def __init__(self, model_path):
        self.model_path = model_path

    def predict(X_val):
        """
        Loading the model and predicting with validation set
        """
        regression_model = load('regression.joblib')

        y_pred_log_reg_val = regression_model.predict(X_val)

        return (y_pred_log_reg_val)
