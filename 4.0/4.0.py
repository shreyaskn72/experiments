import requests

# Your Azure AD (Active Directory) app's credentials
client_id = 'your_client_id'
client_secret = 'your_client_secret'
tenant_id = 'your_tenant_id'

# URL to obtain the access token
token_url = f'https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token'

# Microsoft Graph API endpoint to list users
graph_url = 'https://graph.microsoft.com/v1.0/users'

# Request body for getting the access token with client credentials flow
token_data = {
    'client_id': client_id,
    'scope': 'https://graph.microsoft.com/.default',
    'client_secret': client_secret,
    'grant_type': 'client_credentials'
}

# Getting the access token using client credentials flow
token_response = requests.post(token_url, data=token_data)
access_token = token_response.json().get('access_token')

# Request headers with the access token
headers = {
    'Authorization': 'Bearer ' + access_token,
    'Content-Type': 'application/json'
}

# Making a GET request to Microsoft Graph API to list users
response = requests.get(graph_url, headers=headers)

# Checking if the request was successful
if response.status_code == 200:
    users_data = response.json()['value']
    print("List of Users:")
    for user in users_data:
        print("Name:", user['displayName'])
        print("Email:", user['userPrincipalName'])
        print()
else:
    print("Failed to retrieve user list. Status code:", response.status_code)
