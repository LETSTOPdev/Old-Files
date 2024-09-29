# Yokneam Ride Data Analysis

This project provides a Python script that analyzes ride data to determine routes, distances, and geographic activity within specific bounds such as Yokneam and broader areas in Israel. It includes functionalities for geographic parsing, distance calculation, and exporting data to an Excel file with summaries and Google Maps URLs.

## Requirements

- Python 3.6 or higher
- `pandas` for data manipulation
- `openpyxl` to write data to Excel files
- `geopy` for calculating geodesic distances
- `shapely` for geometric operations

## Installation

Ensure you have Python installed on your system. Then, install the required Python libraries using pip:

```bash
pip install pandas openpyxl geopy shapely
```

## Setup

1. **Prepare Your Data**: Ensure your JSON file contains the required data fields such as `latitude`, `longitude`, `timestamp`, etc., formatted correctly. Save your JSON file in a known directory.

2. **Update File Path**: Modify the `file_path` variable in the script to point to your JSON file. Example:

```python
file_path = r'C:\Users\Almog\Desktop\Pythonbots\Locationfixed\test.ridesAll.json'
```

## Usage

Execute the script from your terminal or command prompt. Navigate to the directory containing the script and run:

```bash
python ride_data_analysis.py
```

The script will process the data and output results in an Excel file named `yokneam_rides.xlsx`, which includes detailed ride summaries and a separate summary sheet.

## Features

- **Distance Calculations**: Calculates the total distance of rides and specific distances within predefined geographic boundaries.
- **Geographic Analysis**: Checks whether rides pass through specific areas like Yokneam using polygonal geofencing.
- **Google Maps Integration**: Generates URLs for visualizing ride paths on Google Maps.
- **Excel Export**: Outputs detailed ride data and summaries into an Excel file for easy viewing and analysis.

## Troubleshooting

- **Data Loading Issues**: Ensure the JSON file is properly formatted and accessible at the specified file path.
- **Dependency Errors**: If you encounter module not found errors, verify that all required packages are installed.
- **Calculation Discrepancies**: Check for accurate coordinate data and valid timestamp entries in your JSON data.

## Support

For further assistance or to report issues, contact support via email or open an issue on the project's repository page.

