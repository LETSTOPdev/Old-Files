# Ride Data Analyzer

Ride Data Analyzer is a Python script that processes and analyzes ride data from a JSON file. It calculates the total distance traveled, identifies suspicious rides, and detects large geographical jumps in the data.

## Requirements

- Python 3.6 or higher
- `pandas`
- `openpyxl`
- `geopy`

## Installation

To set up your environment to run Ride Data Analyzer, follow these steps:

1. **Install Python**: Ensure Python 3.6+ is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Install required Python libraries**: Install the necessary Python packages using pip. Open your terminal or command prompt and run the following command:

   ```bash
   pip install pandas openpyxl geopy
   ```

## Usage

1. **Prepare your JSON file**: The script expects a JSON file that contains ride data with specific fields such as `latitude`, `longitude`, `createdAt`, and others. Place your JSON file in an accessible directory.

2. **Modify the script for your file path**: Update the `file_path` variable in the script to the path where your JSON file is located, such as:
    ```python
    file_path = r'C:\Users\Almog\Desktop\testrides.json'
    ```

3. **Run the script**: Navigate to the directory containing your script and execute it with Python:
    ```bash
    python ride_data_analyzer.py
    ```

4. **Check the output**: The script processes the ride data and outputs the results to an Excel file named `RideData.xlsx`, which will contain detailed information about each ride, including calculated distances, durations, and other metrics.

## Features

- **Total Distance Calculation**: Computes the total distance covered in each ride.
- **Suspicious Ride Detection**: Flags rides that meet specific suspicious criteria (e.g., high distance with very short duration).
- **Geographical Analysis**: Calculates the distance within specific bounds (e.g., within Israel) and identifies large jumps between consecutive coordinates.
- **Data Export**: Outputs a comprehensive Excel file with all the ride information, including calculated metrics and flags for unusual patterns.

## Support

For support or to report issues, contact the maintainer at the provided email address or file an issue on the project's GitHub repository page.
