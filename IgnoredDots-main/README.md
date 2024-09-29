# Ride Data Analysis Script

This Python script is designed to process and analyze ride data from a JSON file. It specifically focuses on geographical data, calculating distances between recorded locations, identifying significant geographical jumps, and summarizing these details in an Excel spreadsheet. This script is particularly useful for understanding mobility patterns and compliance with geographic boundaries.

## Requirements

- **Python 3.6 or higher**: Ensure Python is installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).
- **Pandas**: A powerful data manipulation and analysis library.
- **Openpyxl**: A library to read/write Excel 2010 xlsx/xlsm/xltx/xltm files.
- **Geopy**: A library for accessing various geocoding services, used here to calculate distances.

## Installation

Install the necessary Python libraries using pip. Run the following command in your command prompt or terminal:

```bash
pip install pandas openpyxl geopy
```

## Setup

1. **Data Preparation**: Place your JSON file with the ride data in a known directory. The JSON should contain geographic coordinates (latitude and longitude) and other relevant attributes per ride.

2. **Script Configuration**:
   - Modify the `file_path` variable in the script to point to the location of your JSON file.
   ```python
   file_path = r'C:\Users\Almog\Desktop\Pythonbots\Locationfixed\test.rides19.6.json'
   ```

## Usage

To run the script, navigate to the directory containing your script file in the terminal or command prompt and execute:

```bash
python Ignoreddots.py
```

The script processes the JSON file, calculates the necessary geographic and ride data, and outputs the results to an Excel file.

## Features

- **Geographic Boundaries**: Defines boundaries for a specific area (e.g., Israel) and checks if locations fall within these bounds.
- **Distance Calculation**: Calculates the total distance traveled during each ride and the distance within the predefined boundaries.
- **Large Jumps Detection**: Identifies significant jumps or movements between two consecutive locations that exceed a certain threshold (e.g., 10 km), which might indicate errors in data or unusual ride activity.
- **Excel Output**: Summarizes all ride data and calculations in a structured Excel file, making it easy to analyze and share.

## Output

The script generates an Excel file (`test.rides19.6.xlsx`) with the following details for each ride:
- Ride ID
- User ID
- Number of interactions (Touch Count)
- Potential and calculated tokens based on various criteria (score, level, car)
- Total distance and distance within the specified boundaries
- Duration and type of transportation
- Notable geographical jumps

Each row in the Excel file represents a single ride's data, providing a comprehensive overview of the ride characteristics.

## Troubleshooting

- **JSON Format Errors**: Ensure that the JSON file is correctly formatted. Each entry should include latitude and longitude data.
- **Library Import Failures**: If the script fails due to a missing library, verify that all required libraries are installed correctly.
- **File Path Issues**: Make sure the file path in the script correctly points to the location of the JSON file. Use raw string notation in Python (prefix the string with `r`) to avoid errors in path handling.

## Support

For support or further assistance, consult the respective Python library documentation or the broader Python community forums. If you encounter specific issues related to this script, consider reaching out to developers with expertise in Python and geospatial analysis.

---

This README provides a detailed guide on how to setup and use the ride data analysis script, along with troubleshooting tips to ensure smooth operation. Adjust the file path and other configurations as needed based on your operating environment and specific data structure.
