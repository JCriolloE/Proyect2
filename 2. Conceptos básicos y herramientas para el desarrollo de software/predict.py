from joblib import load


def precit(X_val):
    """
    Loading the model and predicting with validation set
    """
    regression_model = load('regression.joblib')

    y_pred_log_reg_val = regression_model.predict(X_val)

    return (y_pred_log_reg_val)
