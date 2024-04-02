import requests
import json

def get_new_access_token(refresh_token, client_id, client_secret):
    # Microsoft OAuth token endpoint
    token_url = "https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token"

    """
    or 
    # Format token URL with the common endpoint
    token_url = "https://login.microsoftonline.com/common/oauth2/v2.0/token"

    """

    # Request payload
    data = {
        "grant_type": "refresh_token",
        "refresh_token": refresh_token,
        "client_id": client_id,
        "client_secret": client_secret,
        "scope": "offline_access https://graph.microsoft.com/.default"
    }

    # Format token URL with the tenant ID
    token_url = token_url.format(tenant_id="common")

    # Send POST request to obtain new access token
    response = requests.post(token_url, data=data)

    # Check if request was successful
    if response.status_code == 200:
        # Parse JSON response
        token_data = response.json()
        access_token = token_data.get('access_token')
        return access_token
    else:
        print("Error refreshing access token:")
        print("Status code:", response.status_code)
        print("Response:", response.text)
        return None

def list_meeting_types(access_token):
    # Microsoft Booking API endpoint to list meeting types
    endpoint = "https://graph.microsoft.com/v1.0/me/bookingsBusinesses/{businessId}/bookingTypes"

    # Request headers including authorization with access token
    headers = {
        "Authorization": "Bearer " + access_token,
        "Content-Type": "application/json"
    }

    # Send GET request to list meeting types
    response = requests.get(endpoint, headers=headers)

    # Check if request was successful
    if response.status_code == 200:
        # Parse JSON response
        meeting_types = response.json().get('value', [])
        if meeting_types:
            print("Meeting Types:")
            for meeting_type in meeting_types:
                print("- ", meeting_type.get('displayName'))
        else:
            print("No meeting types found.")
    else:
        print("Failed to list meeting types.")
        print("Error:", response.status_code)
        print("Response:", response.text)

def main():
    # Refresh token obtained through the initial OAuth 2.0 authorization process
    refresh_token = "YOUR_REFRESH_TOKEN"

    # Your application's client ID and client secret
    client_id = "YOUR_CLIENT_ID"
    client_secret = "YOUR_CLIENT_SECRET"

    # Get a new access token using the refresh token
    access_token = get_new_access_token(refresh_token, client_id, client_secret)
    if access_token:
        # Use the new access token to list meeting types
        list_meeting_types(access_token)

if __name__ == "__main__":
    main()
