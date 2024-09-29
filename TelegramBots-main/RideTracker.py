import pandas as pd
import json
from datetime import datetime
import openpyxl  # This is required to save the DataFrame to an Excel file

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

    if start_time and end_time:
        duration_hours = (end_time - start_time).total_seconds() / 3600
    else:
        duration_hours = entry.get('duration', 0)  # Default to 0 if no valid times are found

    granted_tokens = entry.get('grantedTokens', 0)  # Extract granted tokens, defaulting to 0 if missing

    prepared_data.append({
        'Duration': duration_hours,
        'Distance': entry['distance'],
        'Locations': locations,
        'Granted Tokens': granted_tokens  # Add granted tokens to each ride's data
    })

# Create DataFrame from prepared data
df = pd.DataFrame(prepared_data)

# Calculate average ride time and pace
average_ride_time = df['Duration'].mean()
average_pace = df['Distance'].sum() / df['Duration'].sum() if df['Duration'].sum() > 0 else 0

# Extract all locations
all_locations = [loc for sublist in df['Locations'].tolist() for loc in sublist]

# Create a DataFrame for location visits
location_visits_df = pd.DataFrame(list(location_count.items()), columns=['Location', 'Visit Count'])

# Write DataFrames to Excel
with pd.ExcelWriter('RideData.xlsx', engine='openpyxl') as writer:
    df.to_excel(writer, sheet_name='Ride Summary', index=False)
    location_visits_df.to_excel(writer, sheet_name='Location Visits', index=False)

print(f"Average Ride Time: {average_ride_time:.2f} hours")
print(f"Average Pace: {average_pace:.2f} km/h")
print(f"Locations Driven: {all_locations}")
print(f"Data written to Excel file 'RideData.xlsx' successfully.")
