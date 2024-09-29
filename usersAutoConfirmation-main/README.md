# AWS Cognito Lambda Trigger for User Auto-Confirmation and Email Verification

This AWS Lambda function automatically confirms new user registrations and verifies their emails when they sign up using AWS Cognito. This guide will provide you with the steps to set up and deploy this function, and how to handle any issues that may arise during its execution.

## Requirements

- AWS Account
- AWS Lambda
- AWS Cognito User Pool

## Setup

### Step 1: Prepare Your AWS Environment

1. **AWS Lambda**:
   - Navigate to the AWS Lambda console.
   - Click "Create function".
   - Choose "Author from scratch".
   - Enter a function name, e.g., `AutoConfirmCognitoUser`.
   - Choose the runtime as Node.js (ensure it matches the version compatible with the code).
   - Set the appropriate role under "Permissions" that has basic Lambda execution permissions and access to Cognito.

2. **AWS Cognito User Pool**:
   - Ensure you have a Cognito User Pool created.
   - Note down the User Pool ID.

### Step 2: Deploy the Lambda Function

- Copy and paste the provided JavaScript code into the Lambda function's code editor.
- Save the changes.

### Step 3: Connect Lambda to Cognito

- Go to the AWS Cognito console and select your User Pool.
- Navigate to "Triggers" in the sidebar.
- Scroll to the "Pre sign-up" trigger.
- Select the deployed Lambda function (`AutoConfirmCognitoUser`).
- Save the changes.

## Usage

Once the Lambda function is deployed and linked to your Cognito User Pool, it will automatically execute during the sign-up process of a new user. The function:
- Sets `autoConfirmUser` to `true` to bypass manual confirmation.
- Sets `autoVerifyEmail` to `true` to automatically verify the user's email.

## Troubleshooting

- **Function Not Triggering**: Ensure the Lambda function is correctly connected in the Cognito Triggers settings. Check IAM permissions.
- **Errors in Lambda Execution**: 
  - Check the CloudWatch logs for any error messages.
  - Ensure that the Lambda function has sufficient permissions to interact with Cognito.
- **Unexpected Behaviour in User Registration**:
  - Verify the input and output transformation settings in Cognito Triggers.
  - Test the function manually by simulating the pre-sign-up event in Lambda.

## Support

If you encounter any issues during setup or execution, consult the AWS documentation or reach out to AWS support for more detailed guidance and troubleshooting.

---

This README should guide you through setting up and troubleshooting the Lambda function for automating user confirmation and email verification in AWS Cognito. Adjust the configurations and permissions according to your specific AWS environment and security policies.
