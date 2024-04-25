import requests

# Microsoft Bookings API endpoint
BOOKINGS_API_URL = 'https://graph.microsoft.com/v1.0/me/bookings'

# Access token obtained earlier
ACCESS_TOKEN = 'your_access_token_here'

# Set up headers with access token for authorization
headers = {
    'Authorization': f'Bearer {ACCESS_TOKEN}',
    'Content-Type': 'application/json'
}

# Make a GET request to retrieve meeting types
response = requests.get(f"{BOOKINGS_API_URL}/appointmentTypes", headers=headers)

if response.status_code == 200:
    meeting_types = response.json()
    print("Meeting Types:")
    for meeting_type in meeting_types['value']:
        print("- Name:", meeting_type['displayName'])
        print("  ID:", meeting_type['id'])
else:
    print("Failed to retrieve meeting types:", response.text)
