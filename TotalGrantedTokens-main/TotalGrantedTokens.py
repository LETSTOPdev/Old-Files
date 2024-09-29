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
