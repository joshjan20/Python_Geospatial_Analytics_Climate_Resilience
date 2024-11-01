import geopandas as gpd
import xarray as xr

def load_data(climate_data_path, crop_data_path):
    climate_data = xr.open_dataset(climate_data_path)
    crop_data = gpd.read_file(crop_data_path)
    return climate_data, crop_data
