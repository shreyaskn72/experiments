import requests

# Microsoft Graph API endpoint for getting Bookings businesses
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

# Function to get Bookings businesses
def get_bookings_businesses(access_token):
    headers = {
        'Authorization': 'Bearer ' + access_token
    }

    response = requests.get(bookings_businesses_endpoint, headers=headers)

    if response.status_code == 200:
        businesses = response.json().get('value', [])
        for business in businesses:
            print("Business ID:", business.get('id'))
            print("Display Name:", business.get('displayName'))
            print("Email:", business.get('email'))
            print("Phone:", business.get('phone'))
            print()
    else:
        print("Failed to get Bookings businesses:", response.text)

if __name__ == "__main__":
    access_token = get_access_token()
    if access_token:
        get_bookings_businesses(access_token)
    else:
        print("Failed to obtain access token.")
