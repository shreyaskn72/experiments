import requests
from urllib.parse import urlencode

# Your Azure AD (Active Directory) app's credentials
client_id = 'your_client_id'
redirect_uri = 'https://localhost'
scopes = ['https://graph.microsoft.com/.default', 'offline_access']

# Authorization endpoint URL
authorization_url = f'https://login.microsoftonline.com/common/oauth2/v2.0/authorize'

# Constructing the authorization URL
params = {
    'client_id': client_id,
    'response_type': 'code',
    'redirect_uri': redirect_uri,
    'scope': ' '.join(scopes)
}

authorization_request_url = authorization_url + '?' + urlencode(params)

# Open the authorization URL in a browser for the user to login
print("Please login to your Microsoft account:")
print(authorization_request_url)
authorization_code = input("Enter the authorization code from the URL: ")

# URL to obtain the access token
token_url = f'https://login.microsoftonline.com/common/oauth2/v2.0/token'

# Request body for getting the access token with authorization code grant flow
token_data = {
    'client_id': client_id,
    'scope': ' '.join(scopes),
    'code': authorization_code,
    'redirect_uri': redirect_uri,
    'grant_type': 'authorization_code',
    'client_secret': 'your_client_secret'  # Only needed for confidential clients
}

# Getting the access token using authorization code
token_response = requests.post(token_url, data=token_data)
if token_response.status_code == 200:
    access_token = token_response.json().get('access_token')
    print("Access token obtained successfully!")
else:
    print("Failed to obtain access token. Status code:", token_response.status_code)
    print(token_response.json())
    exit()

# Microsoft Graph API endpoint to list bookings
graph_url = 'https://graph.microsoft.com/v1.0/me/bookings'

# Request headers with the access token
headers = {
    'Authorization': 'Bearer ' + access_token,
    'Content-Type': 'application/json'
}

# Making a GET request to Microsoft Graph API to list bookings
response = requests.get(graph_url, headers=headers)

# Checking if the request was successful
if response.status_code == 200:
    bookings_data = response.json().get('value', [])
    if bookings_data:
        print("List of Bookings:")
        for booking in bookings_data:
            print("Booking ID:", booking.get('id'))
            print("Start Time:", booking.get('start').get('dateTime'))
            print("End Time:", booking.get('end').get('dateTime'))
            print("Service:", booking.get('serviceId'))
            print()
    else:
        print("No bookings found.")
else:
    print("Failed to retrieve bookings. Status code:", response.status_code)
    print(response.json())
