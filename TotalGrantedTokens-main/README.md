
# TokenBot

TokenBot is a simple Python script that loads token data from a JSON file and calculates the total amount of tokens granted based on ride data.

## Requirements

- Python 3.6 or higher
- No external libraries are required beyond the standard Python libraries.

## Installation

No additional installation is required for running TokenBot, as it uses Python's standard libraries. Ensure that Python is installed on your system. You can download it from [python.org](https://www.python.org/downloads/) if it's not installed.

## Usage

1. **Prepare your JSON file**: Ensure your JSON file is formatted correctly and contains the `grantedTokens` fields. Example format:

```json
[
    {
        "rideId": "1",
        "grantedTokens": 150
    },
    {
        "rideId": "2",
        "grantedTokens": 100
    }
]
```

2. **Set the filepath**: Modify the `filepath` variable in the script to point to the location of your JSON file. Example:
    ```python
    filepath = "C:\\Users\\Almog\\Desktop\\test.rideshour.json"
    ```

3. **Run the script**: Execute the script with Python. Open your terminal or command prompt, navigate to the directory containing `token_bot.py`, and run:
    ```bash
    python token_bot.py
    ```

4. **View the results**: The script will print the total amount of granted tokens. Example output:
    ```
    Total Granted Tokens: 250
    ```

## Example Code

Below is the example code snippet included in this package:

```python
import json

class TokenBot:
    def __init__(self, filepath):
        self.filepath = filepath
        self.granted_tokens = []

    def load_data(self):
        """Load data from a JSON file."""
        with open(self.filepath, 'r') as file:
            data = json.load(file)
            self.granted_tokens = [ride['grantedTokens'] for ride in data if 'grantedTokens' in ride]

    def calculate_total_tokens(self):
        """Calculate and return the total amount of granted tokens."""
        return sum(self.granted_tokens)

# Example usage:
filepath = "C:\\Users\\Almog\\Desktop\\test.rideshour.json"
bot = TokenBot(filepath)
bot.load_data()
total_tokens = bot.calculate_total_tokens()
print("Total Granted Tokens:", total_tokens)
```

## Support

For support, contact the maintainer at the email address provided or open an issue on the GitHub repository page if applicable.
