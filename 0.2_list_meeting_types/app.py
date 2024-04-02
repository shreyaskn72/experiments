import requests

def list_meeting_types(access_token):
    # Microsoft Booking API endpoint to list meeting types
    endpoint = "https://graph.microsoft.com/v1.0/me/bookingsBusinesses/{businessId}/bookingTypes"

    # Request headers including authorization with access token
    headers = {
        "Authorization": "Bearer " + access_token,
        "Content-Type": "application/json"
    }

    # Send GET request to list meeting types
    response = requests.get(endpoint, headers=headers)

    # Check if request was successful
    if response.status_code == 200:
        # Parse JSON response
        meeting_types = response.json().get('value', [])
        if meeting_types:
            print("Meeting Types:")
            for meeting_type in meeting_types:
                print("- ", meeting_type.get('displayName'))
        else:
            print("No meeting types found.")
    else:
        print("Failed to list meeting types.")
        print("Error:", response.status_code)
        print(response.text)

def main():
    # Access token obtained from the OAuth authentication process
    access_token = "YOUR_ACCESS_TOKEN"

    # List meeting types
    list_meeting_types(access_token)

if __name__ == "__main__":
    main()
