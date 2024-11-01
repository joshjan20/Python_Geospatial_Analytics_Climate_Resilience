import numpy as np
import pandas as pd
import xarray as xr
import geopandas as gpd
from shapely.geometry import Point

# Generate Synthetic Climate Data
def generate_climate_data():
    # Define dimensions
    times = pd.date_range('2000-01-01', periods=100, freq='M')
    lats = np.linspace(49, 53, num=10)  # 10 latitude points
    lons = np.linspace(9, 13, num=10)   # 10 longitude points

    # Generate synthetic temperature and precipitation data
    temperature = np.random.uniform(low=10, high=35, size=(len(times), len(lats), len(lons)))
    precipitation = np.random.uniform(low=0, high=100, size=(len(times), len(lats), len(lons)))

    # Create xarray Dataset
    climate_data = xr.Dataset(
        {
            'temperature': (['time', 'lat', 'lon'], temperature),
            'precipitation': (['time', 'lat', 'lon'], precipitation),
        },
        coords={
            'time': times,
            'lat': lats,
            'lon': lons,
        }
    )

    # Save to NetCDF
    climate_data.to_netcdf('data/climate_data.nc')
    print("Synthetic climate data saved as 'data/climate_data.nc'.")

# Generate Synthetic Crop Location Data
def generate_crop_data():
    # Define crop data
    data = {
        'name': ['Wheat', 'Corn', 'Rice'],
        'geometry': [
            Point(10.0, 50.0),  # Wheat
            Point(11.0, 51.0),  # Corn
            Point(12.0, 52.0)   # Rice
        ]
    }

    # Create GeoDataFrame
    crop_locations = gpd.GeoDataFrame(data, crs="EPSG:4326")

    # Save to Shapefile
    crop_locations.to_file('data/crop_locations.shp', driver='ESRI Shapefile')
    print("Synthetic crop location data saved as 'data/crop_locations.shp'.")

# Create data directory and generate data
import os

if not os.path.exists('data'):
    os.makedirs('data')

generate_climate_data()
generate_crop_data()
