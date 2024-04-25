import requests
import webbrowser
import json
from urllib.parse import urlencode

# Azure AD Tenant ID
TENANT_ID = 'your_tenant_id'

# Client ID and secret obtained from Azure portal
CLIENT_ID = 'your_client_id'
CLIENT_SECRET = 'your_client_secret'
REDIRECT_URI = 'http://localhost:8080'  # Redirect URI configured in Azure portal
SCOPE = 'https://graph.microsoft.com/.default'  # Scope for Microsoft Graph API
AUTH_URL = f'https://login.microsoftonline.com/{TENANT_ID}/oauth2/v2.0/authorize'
TOKEN_URL = f'https://login.microsoftonline.com/{TENANT_ID}/oauth2/v2.0/token'

# Step 1: Get Authorization Code
auth_params = {
    'client_id': CLIENT_ID,
    'redirect_uri': REDIRECT_URI,
    'response_type': 'code',
    'scope': SCOPE
}

auth_url = AUTH_URL + '?' + urlencode(auth_params)

print("Please open the following URL in your browser to login and authorize the application:")
print(auth_url)
webbrowser.open(auth_url)

authorization_code = input("Enter the authorization code from the URL redirect: ")

# Step 2: Exchange Authorization Code for Access Token
token_data = {
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
    'code': authorization_code,
    'redirect_uri': REDIRECT_URI,
    'grant_type': 'authorization_code'
}

token_response = requests.post(TOKEN_URL, data=token_data)

if token_response.status_code == 200:
    token_json = token_response.json()
    print("Token Response:", json.dumps(token_json, indent=4))
else:
    print("Failed to retrieve access token:", token_response.text)
