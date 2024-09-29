# MEXC API Functions and Lambda Integration

This project contains Python modules and AWS Lambda functions designed to interact with the MEXC API for managing cryptocurrency accounts and performing internal transfers.

## Requirements

- Python 3.8 or later
- AWS Lambda
- `requests` library
- `hmac` and `hashlib` for API request signing
- AWS account with configured environment variables

## Installation

1. **Install Python**: Make sure Python 3.8 or later is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Install the `requests` library**: This project requires the `requests` library for making HTTP requests. Install it using pip:

   ```bash
   pip install requests
   ```

3. **AWS Configuration**:
   - Deploy the provided Lambda functions (`lambda_function.py` and `V2_lambda_function.py`) on AWS Lambda.
   - Set the following environment variables in your Lambda configuration:
     - `MEXC_API_KEY`: Your MEXC API key.
     - `MEXC_SECRET_KEY`: Your MEXC secret key.

## Project Structure

- `mexc_api_funcs.py` and `V2_mexc_api_funcs.py`: Modules containing classes and methods for making signed requests to the MEXC API.
- `lambda_function.py` and `V2_lambda_function.py`: AWS Lambda functions that utilize the `mexc_api_funcs` for operations like retrieving account info and processing transfers.

## Usage

1. **Lambda Functions**: The Lambda functions handle specific tasks:
   - `lambda_function.py`: Manages internal transfer requests and checks transaction statuses.
   - `V2_lambda_function.py`: Handles user transfers and balance checks, and provides detailed error responses for API interactions.

2. **API Functions**:
   - `mexc_account`: Retrieves account information.
   - `mexc_capital`: Performs and retrieves internal transfers.

3. **Execution**:
   - Deploy the Lambda functions to AWS.
   - Trigger the functions using events that provide necessary parameters such as user ID and transaction amounts.

## Features

- **Secure API Interaction**: Utilizes HMAC for API request signing, ensuring secure interaction with the MEXC API.
- **Flexible Account Management**: Supports various account-related operations, including balance checks and internal transfers.
- **Robust Error Handling**: Detailed error responses in Lambda functions to facilitate troubleshooting and improve reliability.

## Support

For support or to report issues, contact the maintainer at the provided email address or file an issue on the project's GitHub repository page.

---

Ensure your MEXC API credentials are secure and never expose them in your codebase. Adjust the AWS Lambda environment variables and test the setup thoroughly before using it in a production environment.
