import requests
import json
from datetime import datetime, timedelta

# Microsoft Graph API endpoints
bookings_endpoint = "https://graph.microsoft.com/beta/bookingBusinesses/{business_id}/appointments"
token_endpoint = "https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token"

# Your application details
client_id = "YOUR_CLIENT_ID"
client_secret = "YOUR_CLIENT_SECRET"
tenant_id = "YOUR_TENANT_ID"

# The Business ID you want to schedule the appointment for
business_id = "YOUR_BUSINESS_ID"

# Function to get access token
def get_access_token():
    token_url = token_endpoint.format(tenant_id=tenant_id)
    data = {
        'client_id': client_id,
        'client_secret': client_secret,
        'scope': 'https://graph.microsoft.com/.default',
        'grant_type': 'client_credentials'
    }
    response = requests.post(token_url, data=data)
    access_token = response.json().get('access_token')
    return access_token

# Function to schedule appointment
def schedule_appointment(access_token):
    headers = {
        'Authorization': 'Bearer ' + access_token,
        'Content-Type': 'application/json'
    }

    # Example appointment data
    start_time = (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%dT%H:%M:%SZ')  # Start time is set to tomorrow
    end_time = (datetime.now() + timedelta(days=1, hours=1)).strftime('%Y-%m-%dT%H:%M:%SZ')  # End time is set to 1 hour later
    data = {
        "customerId": "CUSTOMER_ID",
        "serviceId": "SERVICE_ID",
        "start": {
            "dateTime": start_time
        },
        "end": {
            "dateTime": end_time
        }
    }

    response = requests.post(bookings_endpoint.format(business_id=business_id), headers=headers, data=json.dumps(data))
    if response.status_code == 201:
        print("Appointment scheduled successfully.")
    else:
        print("Failed to schedule appointment:", response.text)

if __name__ == "__main__":
    access_token = get_access_token()
    if access_token:
        schedule_appointment(access_token)
    else:
        print("Failed to obtain access token.")
