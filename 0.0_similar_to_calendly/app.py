from requests_oauthlib import OAuth2Session

# Set your Microsoft Bookings OAuth client credentials
client_id = 'your_client_id'
client_secret = 'your_client_secret'

# Set the redirect URL for your application
redirect_uri = 'https://example.com/oauth/callback'  # Change this to your desired redirect URL

# Set the OAuth endpoints specific to Microsoft Bookings
authorization_base_url = 'https://login.microsoftonline.com/common/oauth2/v2.0/authorize'
token_url = 'https://login.microsoftonline.com/common/oauth2/v2.0/token'

# Create an OAuth2Session object with your client credentials
oauth = OAuth2Session(client_id, redirect_uri=redirect_uri, scope=['offline_access'])

# Obtain the authorization URL
authorization_url, state = oauth.authorization_url(authorization_base_url)

# Print the authorization URL for the user to visit and authorize the application
print("Please visit the following URL and authorize the application:")
print(authorization_url)

# After the user authorizes the application, they will be redirected back to the redirect URL
# Extract the authorization response from the redirected URL
redirect_response = input("Paste the full URL you were redirected to: ")

# Parse the authorization response to extract the authorization code
authorization_response = oauth.parse_authorization_response(redirect_response)

# Exchange the authorization code for tokens
token = oauth.fetch_token(token_url, authorization_response=authorization_response, client_secret=client_secret)

# Access token and refresh token are available in the token dictionary
access_token = token['access_token']
refresh_token = token.get('refresh_token')

# Now you can use the access token to make requests to the Microsoft Bookings API
# For example, you can fetch user details
bookings_api_url = 'https://graph.microsoft.com/v1.0/me'
headers = {
    'Authorization': f'Bearer {access_token}'
}
user_response = oauth.get(bookings_api_url, headers=headers)
if user_response.ok:
    user_data = user_response.json()
    print("User Details:")
    print(user_data)
else:
    print("Failed to fetch user details. Status code:", user_response.status_code)
