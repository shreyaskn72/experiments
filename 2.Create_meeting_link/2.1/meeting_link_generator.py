import requests
import json



# Function to obtain access token
def get_access_token(client_id, client_secret, tenant_id, scope):
    token_url = f'https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token'
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    payload = {
        'client_id': client_id,
        'client_secret': client_secret,
        'scope': scope,
        'grant_type': 'client_credentials'
    }

    response = requests.post(token_url, headers=headers, data=payload)
    if response.status_code == 200:
        return response.json().get('access_token')
    else:
        print("Error obtaining access token:", response.text)
        return None



def create_meeting_link(booking_id, meeting_type):
    url = f'https://graph.microsoft.com/v1.0/bookingBusinesses/{booking_id}/appointmentTypes/{meeting_type}/createOnlineMeeting'
    headers = {
        'Authorization': 'Bearer ' + access_token,
        'Content-Type': 'application/json'
    }
    payload = {
        "startDateTime": "2024-03-21T08:00:00",  # Replace with your start datetime
        "endDateTime": "2024-03-21T09:00:00",    # Replace with your end datetime
        "participant": {
            "emailAddress": {
                "address": "example@example.com"  # Replace with participant email
            }
        }
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 201:
        data = response.json()
        return data.get('joinWebUrl')
    else:
        print("Error creating meeting link:", response.text)
        return None

if __name__ == "__main__":
    # Microsoft Graph API credentials
    client_id = 'YOUR_CLIENT_ID'
    client_secret = 'YOUR_CLIENT_SECRET'
    tenant_id = 'YOUR_TENANT_ID'
    scope = 'https://graph.microsoft.com/.default'

    # Replace these values with your own
    access_token = get_access_token(client_id, client_secret, tenant_id, scope)
    booking_id = 'YOUR_BOOKING_ID'

    # Example usage
    meeting_type = 'YOUR_MEETING_TYPE_ID'  # Replace with the ID of your meeting type
    meeting_link = create_meeting_link(booking_id, meeting_type)

    if meeting_link:
        print("Meeting link:", meeting_link)
    else:
        print("Failed to create meeting link.")

