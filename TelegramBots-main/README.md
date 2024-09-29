# Project Repository: Python Utilities and Telegram Bots

This repository contains a collection of Python scripts and Telegram bot functionalities designed to handle various tasks including data analysis, user interaction through Telegram, and ride data processing.

## Overview

Each script in this repository is designed for specific purposes:

1. **Data Analysis Scripts**: Process and analyze geographic and ride data from JSON files, calculating metrics like total distance, significant jumps in locations, and generating summaries in Excel files.
2. **Telegram Bots**: Interact with users via Telegram, handling commands, and messages to perform actions like fetching usernames, tracking message counts, and responding to user inputs.
3. **Location Tracking**: Analyze ride data to classify locations based on predefined geographic boundaries, and keep track of user movements and activities.

## Requirements

- Python 3.6+
- Libraries: `pandas`, `openpyxl`, `geopy`, `numpy`, `ast`, `telegram`, `python-telegram-bot`
- Telegram Bot API tokens (obtained via BotFather on Telegram)

## Installation

Install the required Python libraries using pip:

```bash
pip install pandas openpyxl geopy numpy python-telegram-bot
```

## Usage

Each script can be executed independently based on the required functionality. Below is a breakdown of key scripts:

### Data Analysis

- **Ride Data Analysis**: Load JSON data, calculate distances and metrics, and export the results to an Excel file.
- **Location Data Classification**: Classify ride data based on geographic locations and export summarized data to Excel.

### Telegram Bots

- **Echo Bot**: Responds to user messages by echoing the texts.
- **User Data Collection**: Collects and stores user data such as usernames and IDs.
- **Activity Tracker**: Tracks user messages and provides reports on activity levels.

### Location Tracking

- **Ride Tracker**: Extracts and tracks locations from ride data, providing insights into frequent routes and stops.

## Files and Directories

- `RideTracker.py`, `Alldatalocations.py`: Scripts for analyzing ride data and tracking locations.
- `Lastbotneeded.py`, `Importusername.py`, `LETSTOPActivityTrackerbot.py`: Telegram bots for various interactive functionalities.

## Configuration

1. Update the file paths and API tokens in each script as needed.
2. Ensure that each script points to the correct JSON data file or Telegram API as required.

## Running Scripts

Navigate to the script directory and run the Python script via the command line:

```bash
python <script_name>.py
```

## Troubleshooting

- Ensure all dependencies are installed.
- Verify that JSON data files are formatted correctly and accessible.
- Check API tokens and bot permissions on Telegram if bots fail to respond.

## Support

For issues, questions, or contributions, please open an issue in this repository or contact the maintainers.
