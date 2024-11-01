import pandas as pd

def preprocess_climate_data(climate_data):
    # Example of preprocessing climate data
    climate_data = climate_data.sel(time=slice("2000-01-01", "2020-12-31"))  # Select time range
    return climate_data
