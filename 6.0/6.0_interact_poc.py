from msal import ConfidentialClientApplication
import requests

# Azure AD (Active Directory) app's credentials
client_id = 'your_client_id'
client_secret = 'your_client_secret'
redirect_uri = 'http://localhost:8080'  # Must match the Redirect URI configured in Azure AD app

# Microsoft Graph API endpoint
graph_url = 'https://graph.microsoft.com/v1.0/me'

# Initialize MSAL Confidential Client Application
app = ConfidentialClientApplication(
    client_id,
    authority='https://login.microsoftonline.com/common',
    client_credential=client_secret,
    redirect_uri=redirect_uri
)

# Get the authorization request URL
auth_url = app.get_authorization_request_url(
    scopes=['User.Read'],  # Add required scopes here
)

# Print the authorization URL
print("Authorization URL:", auth_url)

# After visiting the authorization URL, the user will be redirected to the Redirect URI
# Extract the authorization code from the Redirect URI (typically done manually)

# Example of getting the authorization code from the Redirect URI manually
authorization_code = input("Enter the authorization code from the Redirect URI: ")

# Get the access token using the authorization code
result = app.acquire_token_by_authorization_code(
    authorization_code,
    scopes=['User.Read'],  # Add required scopes here
)

# Get the access token from the result
access_token = result.get('access_token')

# Make a GET request to Microsoft Graph API
headers = {
    'Authorization': 'Bearer ' + access_token,
    'Content-Type': 'application/json'
}
response = requests.get(graph_url, headers=headers)

# Print user information if the request was successful
if response.status_code == 200:
    user_data = response.json()
    print("User Information:")
    print("Name:", user_data['displayName'])
    print("Email:", user_data['userPrincipalName'])
else:
    print("Failed to retrieve user information. Status code:", response.status_code)
    print(response.text)
