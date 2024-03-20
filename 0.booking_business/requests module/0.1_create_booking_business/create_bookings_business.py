import requests
import json

# Microsoft Graph API endpoint for creating a new Bookings business
bookings_businesses_endpoint = "https://graph.microsoft.com/beta/bookingBusinesses"

# Your application details
client_id = "YOUR_CLIENT_ID"
client_secret = "YOUR_CLIENT_SECRET"
tenant_id = "YOUR_TENANT_ID"

# Function to get access token
def get_access_token():
    token_url = f"https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token"
    data = {
        'client_id': client_id,
        'client_secret': client_secret,
        'scope': 'https://graph.microsoft.com/.default',
        'grant_type': 'client_credentials'
    }
    response = requests.post(token_url, data=data)
    access_token = response.json().get('access_token')
    return access_token

# Function to create a new Microsoft Bookings business
def create_bookings_business(access_token):
    headers = {
        'Authorization': 'Bearer ' + access_token,
        'Content-Type': 'application/json'
    }

    # Data for creating the new business
    data = {
        "displayName": "My Bookings Business",
        "email": "bookings@example.com",
        "phone": "+1234567890",
        "timeZone": "Pacific Standard Time"  # Replace with your desired timezone
    }

    response = requests.post(bookings_businesses_endpoint, headers=headers, json=data)

    if response.status_code == 201:
        print("New Bookings business created successfully.")
    else:
        print("Failed to create Bookings business:", response.text)

if __name__ == "__main__":
    access_token = get_access_token()
    if access_token:
        create_bookings_business(access_token)
    else:
        print("Failed to obtain access token.")
