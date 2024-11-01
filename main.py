from data_ingestion import load_data
from data_processing import preprocess_climate_data
from vulnerability_assessment import assess_vulnerability
from predictive_modeling import train_model
from visualization import visualize_vulnerabilities

def main():
    # Load climate and crop data
    climate_data, crop_data = load_data("data/climate_data.nc", "data/crop_locations.shp")
    print("Climate Data Loaded:", climate_data)
    print("Crop Data Loaded:", crop_data)

    # Preprocess climate data
    processed_climate_data = preprocess_climate_data(climate_data)
    print("Processed Climate Data:", processed_climate_data)

    # Assess vulnerability
    vulnerable_crops = assess_vulnerability(crop_data, processed_climate_data)
    print("Vulnerable Crops:", vulnerable_crops)

    # Visualize if there are vulnerable crops
    if not vulnerable_crops.empty:
        map_vulnerabilities = visualize_vulnerabilities(vulnerable_crops)
        if map_vulnerabilities:  # Check if map was created successfully
            map_vulnerabilities.save("vulnerable_crops_map.html")
        else:
            print("Map creation failed; no map object returned.")
    else:
        print("No vulnerable crops identified.")

if __name__ == "__main__":
    main()
