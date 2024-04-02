# Microsoft Booking API: Refresh Token to Access Token

This Python script demonstrates how to exchange a refresh token for an access token in Microsoft Booking API using OAuth 2.0 authentication. It utilizes the Microsoft OAuth token endpoint to obtain the access token.

## Prerequisites

- Python 3.x installed on your system.
- `requests` library. Install it using `pip install requests`.
- Microsoft Azure Active Directory (Azure AD) application registered with permissions to access the Microsoft Booking API.
- Refresh token obtained through the initial OAuth 2.0 authorization process.

## Configuration

1. Replace `"YOUR_CLIENT_ID"`, `"YOUR_CLIENT_SECRET"`, and `"YOUR_TENANT_ID"` in the script with your actual Microsoft Azure AD OAuth client credentials and tenant ID.
2. Adjust the `scope` parameter in the script based on the required permissions for accessing the Microsoft Booking API.
3. Run the script.

## Usage

1. Run the script.
2. Enter your refresh token when prompted.
3. The script will output the obtained access token.

## Important Notes

- Ensure that your Azure AD application is properly configured with the required permissions to access the Microsoft Booking API.
- Keep your client credentials and refresh token secure and do not expose them publicly.
- Handle errors and exceptions appropriately in a production environment.