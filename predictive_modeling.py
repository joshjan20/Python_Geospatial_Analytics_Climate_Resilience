from sklearn.ensemble import RandomForestRegressor
import numpy as np

def train_model(X_train, y_train):
    model = RandomForestRegressor()
    model.fit(X_train, y_train)
    return model

def predict_yield(model, X_test):
    return model.predict(X_test)
