import requests
import json

# Azure AD Tenant ID
TENANT_ID = 'your_tenant_id'

# Client ID and secret obtained from Azure portal
CLIENT_ID = 'your_client_id'
CLIENT_SECRET = 'your_client_secret'
SCOPE = 'https://graph.microsoft.com/.default offline_access'  # Scope for Microsoft Graph API with offline_access
TOKEN_URL = f'https://login.microsoftonline.com/{TENANT_ID}/oauth2/v2.0/token'

# Refresh token obtained earlier
REFRESH_TOKEN = 'your_refresh_token_here'

# Step 1: Exchange Refresh Token for New Access Token
token_data = {
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
    'refresh_token': REFRESH_TOKEN,
    'grant_type': 'refresh_token',
    'scope': SCOPE
}

token_response = requests.post(TOKEN_URL, data=token_data)

if token_response.status_code == 200:
    token_json = token_response.json()
    access_token = token_json['access_token']
    print("New Access Token:", access_token)
else:
    print("Failed to retrieve access token:", token_response.text)
