import pandas as pd
import json
from datetime import datetime
import openpyxl  # This is required to save the DataFrame to an Excel file
import ast
import numpy as np

# Load the JSON data from the specified file path
file_path = r'C:\Users\Almog\Desktop\testrides.json'

with open(file_path, 'r') as f:
    data = json.load(f)

# Normalize and extract location data
def extract_locations(locations):
    loc_list = []
    for loc in locations:
        if loc:
            # Extract latitude and longitude
            loc_list.append((loc['latitude'], loc['longitude']))
    return loc_list

# Prepare data for DataFrame creation
prepared_data = []
location_count = {}
for item in data:
    entry = item  # Assuming item is already a dictionary
    locations = extract_locations(entry.get('locations', []))

    # Track location visits
    for loc in locations:
        if loc in location_count:
            location_count[loc] += 1
        else:
            location_count[loc] = 1

    # Handle createdAt and updatedAt dates
    def parse_date(date_field):
        if isinstance(date_field, dict) and '$date' in date_field:
            return datetime.strptime(date_field['$date'], '%Y-%m-%dT%H:%M:%S.%fZ')
        if isinstance(date_field, str):
            try:
                return datetime.strptime(date_field, '%Y-%m-%dT%H:%M:%S.%fZ')
            except ValueError:
                return None
        return None

    start_time = parse_date(entry.get('createdAt'))
    end_time = parse_date(entry.get('updatedAt'))
    user_id = entry.get('user_id', {}).get('$oid', 'unknown')  # Extracting user ID

    if start_time and end_time:
        duration_hours = (end_time - start_time).total_seconds() / 3600
    else:
        duration_hours = entry.get('duration', 0)  # Default to 0 if no valid times are found

    granted_tokens = entry.get('grantedTokens', 0)  # Extract granted tokens, defaulting to 0 if missing

    prepared_data.append({
        'User ID': user_id,
        'Duration': duration_hours,
        'Distance': entry['distance'],
        'Locations': str(locations),  # Convert locations to string for further processing
        'Granted Tokens': granted_tokens  # Add granted tokens to each ride's data
    })

# Create DataFrame from prepared data
df = pd.DataFrame(prepared_data)

# Define bounds for geographic classification
israel_bounds = {"latitude": (29.5, 33.5), "longitude": (34.3, 35.9)}
cairo_cyprus_egypt_bounds = {
    "cairo": {"latitude": (29.8, 31.4), "longitude": (31.0, 32.0)},
    "cyprus": {"latitude": (34.6, 35.7), "longitude": (32.8, 34.6)},
    "egypt": {"latitude": (22, 32), "longitude": (24, 37)}
}

# Function to check if a location is within specified bounds
def is_in_bounds(lat, lon, bounds):
    return bounds["latitude"][0] <= lat <= bounds["latitude"][1] and bounds["longitude"][0] <= lon <= bounds["longitude"][1]

# Function to classify each ride
def classify_ride(locations):
    locations = ast.literal_eval(locations)  # Convert string of list to actual list
    regions = []
    for lat, lon in locations:
        if is_in_bounds(lat, lon, israel_bounds):
            regions.append("Israel")
        if is_in_bounds(lat, lon, cairo_cyprus_egypt_bounds["cairo"]):
            regions.append("Cairo")
        if is_in_bounds(lat, lon, cairo_cyprus_egypt_bounds["cyprus"]):
            regions.append("Cyprus")
        if is_in_bounds(lat, lon, cairo_cyprus_egypt_bounds["egypt"]):
            regions.append("Egypt")
    return ', '.join(sorted(set(regions))) if regions else "Other"

# Apply the classification function
df['Ride Locations'] = df['Locations'].apply(classify_ride)

# Summarize the results
summary = df['Ride Locations'].value_counts()

# Write DataFrames to Excel
with pd.ExcelWriter('RideData2.xlsx', engine='openpyxl') as writer:
    df.to_excel(writer, sheet_name='Ride Summary2', index=False)
    pd.DataFrame(list(location_count.items()), columns=['Location', 'Visit Count']).to_excel(writer, sheet_name='Location Visits', index=False)

print(f"Data written to Excel file 'RideDat2.xlsx' successfully.")
print(summary)
