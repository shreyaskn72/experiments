# Microsoft Bookings Meeting Types and Booking Page URLs

This Python script uses Microsoft Graph API to list meeting types and their corresponding booking page URLs for a Microsoft Bookings account.

## Prerequisites

- Python 3.x
- `requests` library (`pip install requests`)
- Microsoft Graph API credentials (client ID, client secret, tenant ID)

## Usage

1. Replace the placeholders in the script with your Microsoft Graph API credentials.
2. Run the script.
3. The script will retrieve the access token and then list all the meeting types along with their booking page URLs.

## Configuration

Make sure to replace the following placeholders in the script with your actual Microsoft Graph API credentials:

- `YOUR_TENANT_ID`: Your Azure AD tenant ID.
- `YOUR_CLIENT_ID`: Your registered application's client ID.
- `YOUR_CLIENT_SECRET`: Your registered application's client secret.

## Output

The script will print the meeting type name and the corresponding booking page URL for each meeting type found.

## Notes

- Ensure that your Azure AD application has the necessary permissions to access Microsoft Bookings data via Microsoft Graph API.

