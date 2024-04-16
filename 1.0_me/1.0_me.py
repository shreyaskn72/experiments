import requests

# Your Azure AD (Active Directory) app's credentials
client_id = 'your_client_id'
client_secret = 'your_client_secret'
tenant_id = 'your_tenant_id'

# URL to obtain the access token
token_url = f'https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token'

# Microsoft Graph API endpoint
graph_url = 'https://graph.microsoft.com/v1.0/me'

# Request body for getting the access token
token_data = {
    'client_id': client_id,
    'scope': 'https://graph.microsoft.com/.default',
    'client_secret': client_secret,
    'grant_type': 'client_credentials'
}

# Getting the access token
token_response = requests.post(token_url, data=token_data)
access_token = token_response.json()['access_token']

# Request headers with the access token
headers = {
    'Authorization': 'Bearer ' + access_token,
    'Content-Type': 'application/json'
}

# Making a GET request to Microsoft Graph API
response = requests.get(graph_url, headers=headers)

# Checking if the request was successful
if response.status_code == 200:
    user_data = response.json()
    print("User Information:")
    print("Name:", user_data['displayName'])
    print("Email:", user_data['userPrincipalName'])
else:
    print("Failed to retrieve user information. Status code:", response.status_code)
