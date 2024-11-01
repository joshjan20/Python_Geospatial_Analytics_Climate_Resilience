import folium
import geopandas as gpd

def visualize_vulnerabilities(vulnerable_crops):
    # Check if vulnerable_crops is not empty
    if vulnerable_crops.empty:
        print("No vulnerable crops to visualize.")
        return None  # Explicitly return None if there are no crops

    # Create a map centered around the average coordinates of the vulnerable crops
    m = folium.Map(location=[vulnerable_crops.geometry.y.mean(), vulnerable_crops.geometry.x.mean()], zoom_start=6, tiles="cartodb positron")

    # Add crop points to the map
    for idx, row in vulnerable_crops.iterrows():
        folium.Marker(
            location=[row.geometry.y, row.geometry.x],
            popup=f"{row['name']}: Risk Score {row['risk_score']:.2f}",
        ).add_to(m)

    return m  # Ensure the map is returned