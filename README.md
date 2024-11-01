# Geospatial Data-Driven Analytics for Climate Resilience

Lets create a project to understand and utilizes geospatial data for climate analytics to assess the vulnerability of various crops to climate change. It leverages machine learning and data visualization techniques to provide insights and help foster climate resilience in agriculture.

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Data Sources](#data-sources)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Project Overview

The project aims to:
- Analyze climate data and crop locations.
- Assess the vulnerability of crops based on climate metrics such as temperature and precipitation.
- Visualize vulnerable crops on an interactive map.

## Features

- Load and preprocess climate data from NetCDF files.
- Load crop location data from shapefiles.
- Analyze crop vulnerability based on defined thresholds for climate variables.
- Visualize vulnerable crops on a map using Folium.

## Technologies Used

- **Python**: The primary programming language.
- **Xarray**: For handling multi-dimensional arrays (climate data).
- **GeoPandas**: For geospatial data manipulation.
- **Folium**: For interactive map visualizations.
- **Pandas**: For data manipulation and analysis.
- **Jupyter Notebook**: For interactive development and testing (if used).

## Data Sources

- **Climate Data**: NetCDF files containing historical climate data (temperature and precipitation).
- **Crop Locations**: Shapefiles containing geographic coordinates of crops.

### Sample Data Files

The project includes example data files for testing:

run gen.py tp generate the data files. 
- `data/climate_data.nc`: Sample NetCDF file with climate data.
- `data/crop_locations.shp`: Sample shapefile with crop locations.

## Installation

To set up the project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/geospatial-climate-resilience.git
   cd geospatial-climate-resilience
