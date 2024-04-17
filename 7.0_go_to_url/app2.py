import requests

# Define your Microsoft Graph API credentials and endpoint
tenant_id = 'YOUR_TENANT_ID'
client_id = 'YOUR_CLIENT_ID'
client_secret = 'YOUR_CLIENT_SECRET'

# Get access token
token_url = f'https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token'
token_data = {
    'client_id': client_id,
    'client_secret': client_secret,
    'grant_type': 'client_credentials',
    'scope': 'https://graph.microsoft.com/.default'
}
token_response = requests.post(token_url, data=token_data)
access_token = token_response.json()['access_token']

# List all booking services
list_services_url = 'https://graph.microsoft.com/v1.0/bookingBusinesses'
headers = {
    'Authorization': f'Bearer {access_token}',
    'Content-Type': 'application/json'
}
services_response = requests.get(list_services_url, headers=headers)

if services_response.status_code == 200:
    services_data = services_response.json()['value']
    for service in services_data:
        service_name = service.get('displayName')
        booking_page_url = service.get('bookingPageUrl')
        if booking_page_url:
            print("Service:", service_name)
            print("Booking Page URL:", booking_page_url)
            print()
        else:
            print("Booking Page URL not found for the service:", service_name)
else:
    print("Error occurred while fetching booking services:")
    print("Status code:", services_response.status_code)
    print("Response:", services_response.json())
