from joblib import dump
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV


def training(X_train, y_train):
    # Let's implement simple classifiers
    {
        "LogisiticRegression": LogisticRegression()
    }

    # Logistic Regression
    log_reg_params = {
        "penalty": [
            'l1', 'l2'], 'C': [
            0.001, 0.01, 0.1, 1, 10, 100, 1000]}

    grid_log_reg = GridSearchCV(LogisticRegression(), log_reg_params)
    grid_log_reg.fit(X_train, y_train)
    # We automatically get the logistic regression with the best parameters.
    log_reg = grid_log_reg.best_estimator_

    """
        Saving the best model
    """
    dump(log_reg, 'regression.joblib')

    return log_reg
