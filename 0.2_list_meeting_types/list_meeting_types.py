import requests

# Set your Microsoft Bookings OAuth access token
access_token = 'your_access_token_here'

# Set the Microsoft Graph API endpoint for listing meeting types
meeting_types_url = 'https://graph.microsoft.com/v1.0/me/bookingBusinesses'

# Set the request headers with the access token
headers = {
    'Authorization': f'Bearer {access_token}',
    'Content-Type': 'application/json'
}

# Make a GET request to the Microsoft Graph API endpoint to list meeting types
response = requests.get(meeting_types_url, headers=headers)

# Check if the request was successful
if response.ok:
    # Parse the response JSON to get meeting types data
    meeting_types_data = response.json()

    # Extract and print the meeting types
    if 'value' in meeting_types_data:
        meeting_types = meeting_types_data['value']
        print("Meeting Types:")
        for meeting_type in meeting_types:
            print(meeting_type.get('displayName'))
    else:
        print("No meeting types found.")
else:
    print("Failed to fetch meeting types. Status code:", response.status_code)
