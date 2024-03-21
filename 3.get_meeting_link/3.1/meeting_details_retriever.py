import requests
from datetime import datetime



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

# Function to get meeting details based on recipient's email address and event type
def get_meeting_details(access_token, recipient_email, event_type):
    url = f'https://graph.microsoft.com/v1.0/users/{recipient_email}/calendar/events'
    headers = {
        'Authorization': 'Bearer ' + access_token,
        'Content-Type': 'application/json'
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        events = response.json().get('value', [])
        for event in events:
            if event.get('type') == event_type:
                meeting_date = datetime.fromisoformat(event.get('start').get('dateTime')).date()
                meeting_time = datetime.fromisoformat(event.get('start').get('dateTime')).time()
                meeting_url = event.get('onlineMeetingUrl')
                return meeting_date, meeting_time, meeting_url
        print("No matching event found.")
        return None, None, None
    else:
        print("Error fetching events:", response.text)
        return None, None, None

if __name__ == "__main__":

    # Microsoft Graph API credentials
    client_id = 'YOUR_CLIENT_ID'
    client_secret = 'YOUR_CLIENT_SECRET'
    tenant_id = 'YOUR_TENANT_ID'
    scope = 'https://graph.microsoft.com/.default'

    # Example usage
    recipient_email = 'recipient@example.com'
    event_type = 'meeting'  # Replace with your event type
    access_token = get_access_token(client_id, client_secret, tenant_id, scope)

    if access_token:
        meeting_date, meeting_time, meeting_url = get_meeting_details(access_token, recipient_email, event_type)
        if meeting_date and meeting_time and meeting_url:
            print("Meeting Date:", meeting_date)
            print("Meeting Time:", meeting_time)
            print("Meeting URL:", meeting_url)
        else:
            print("Failed to fetch meeting details.")
    else:
        print("Failed to obtain access token.")


