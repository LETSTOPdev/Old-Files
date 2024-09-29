import pandas as pd
import json
from datetime import datetime
import openpyxl  # Required for saving the DataFrame to an Excel file
from geopy.distance import geodesic  # Importing geopy for distance calculation

# Load the JSON data from the specified file path
file_path = r'C:\Users\Almog\Desktop\testrides.json'

with open(file_path, 'r') as f:
    data = json.load(f)

# Define bounds for Israel
israel_bounds = {"latitude": (29.5, 33.5), "longitude": (34.3, 35.9)}

# Function to extract locations from the JSON data
def extract_locations(locations):
    loc_list = []
    for loc in locations:
        if loc:
            loc_list.append((loc['latitude'], loc['longitude']))
    return loc_list

# Function to check if a location is within Israel's bounds
def is_in_bounds(lat, lon, bounds):
    return bounds["latitude"][0] <= lat <= bounds["latitude"][1] and bounds["longitude"][0] <= lon <= bounds["longitude"][1]

# Function to calculate total distance and distance within Israel, and report large jumps
def calculate_distances(locations):
    locations = extract_locations(locations)
    distance_total = 0
    distance_within_israel = 0
    prev_loc = None
    prev_loc_israel = None
    large_jumps = []

    for i, (lat, lon) in enumerate(locations):
        if prev_loc:
            segment_distance = geodesic(prev_loc, (lat, lon)).kilometers
            distance_total += segment_distance
            if segment_distance > 50:  # Threshold for large jumps
                jump_description = f"Large jump from {prev_loc} to {lat, lon}, Distance: {segment_distance:.2f} km"
                large_jumps.append(jump_description)
        if is_in_bounds(lat, lon, israel_bounds):
            if prev_loc_israel:
                distance_within_israel += geodesic(prev_loc_israel, (lat, lon)).kilometers
            prev_loc_israel = (lat, lon)
        else:
            prev_loc_israel = None
        prev_loc = (lat, lon)

    return distance_total, distance_within_israel, large_jumps

# Prepare data for DataFrame creation
prepared_data = []
for item in data:
    total_distance, distance_within_israel, large_jumps = calculate_distances(item.get('locations', []))

    # Parse dates
    created_at = datetime.strptime(item['createdAt']['$date'], "%Y-%m-%dT%H:%M:%S.%fZ")
    updated_at = datetime.strptime(item['updatedAt']['$date'], "%Y-%m-%dT%H:%M:%S.%fZ")
    ride_duration_minutes = (updated_at - created_at).total_seconds() / 60

    # Check ride conditions
    suspicious_ride = 'Yes' if item.get('distance', 0) > 10 and item.get('duration', 0) < 2.00 else 'No'

    # Include all data fields from the JSON
    ride_data = {
        'Ride ID': item.get('_id', {}).get('$oid', 'unknown'),
        'User ID': item.get('user_id', {}).get('$oid', 'unknown'),
        'Touch Count': item.get('touchCount', 0),
        'Potential Tokens': item.get('potentialTokens', 0),
        'Calculated Tokens': item.get('calculatedTokens', 0),
        'Calculated Tokens By Score': item.get('calculatedTokensByScore', 0),
        'Calculated Tokens By Level': item.get('calculatedTokensByLevel', 0),
        'Calculated Tokens By Car': item.get('calculatedTokensByCar', 0),
        'Granted Tokens': item.get('grantedTokens', 0),
        'Monthly Remaining Tokens': item.get('monthlyRemainingTokens', 0),
        'Score': item.get('score', 100),
        'XP': item.get('xp', 0),
        'Distance from JSON (km)': item.get('distance', 0),
        'Calculated Total Distance (km)': total_distance,
        'Distance Within Israel (km)': distance_within_israel,
        'Duration (hours)': item.get('duration', 0.03),
        'Ride Duration (minutes)': ride_duration_minutes,
        'Transportation Type': item.get('transportation_type', 'car'),
        'Created At': created_at.strftime('%Y-%m-%d %H:%M:%S'),
        'Updated At': updated_at.strftime('%Y-%m-%d %H:%M:%S'),
        'Large Jumps': '; '.join(large_jumps),
        'Suspicious Ride': suspicious_ride
    }

    prepared_data.append(ride_data)

# Create DataFrame from prepared data
df = pd.DataFrame(prepared_data)

# Write DataFrames to Excel
with pd.ExcelWriter('RideData.xlsx', engine='openpyxl') as writer:
    df.to_excel(writer, sheet_name='Ride Summary', index=False)

print("Data written to Excel file 'RideData.xlsx' successfully.")
