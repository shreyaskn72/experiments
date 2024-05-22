import requests
import json
import datetime
from msal import ConfidentialClientApplication

# Azure AD App Config
CLIENT_ID = 'your_client_id'
CLIENT_SECRET = 'your_client_secret'
TENANT_ID = 'your_tenant_id'
SCOPE = ['https://graph.microsoft.com/.default']

# Authentication
app = ConfidentialClientApplication(
    CLIENT_ID,
    authority=f"https://login.microsoftonline.com/{TENANT_ID}",
    client_credential=CLIENT_SECRET
)

result = app.acquire_token_for_client(scopes=SCOPE)
access_token = result['access_token']

# Booking API URL
BASE_URL = "https://graph.microsoft.com/v1.0"
BOOKING_BUSINESS_ID = "your_booking_business_id"

# Get Staff IDs
def get_staff_ids():
    url = f"{BASE_URL}/bookingBusinesses/{BOOKING_BUSINESS_ID}/staffMembers"
    headers = {
        'Authorization': 'Bearer ' + access_token,
        'Content-Type': 'application/json'
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    staff_ids = [staff['id'] for staff in data['value']]
    return staff_ids

# Check Staff Availability
def check_staff_availability(staff_id, start_time, end_time):
    url = f"{BASE_URL}/bookingBusinesses/{BOOKING_BUSINESS_ID}/staffMembers/{staff_id}/workTimeRanges"
    params = {
        'startDateTime': start_time.strftime("%Y-%m-%dT%H:%M:%S"),
        'endDateTime': end_time.strftime("%Y-%m-%dT%H:%M:%S")
    }
    headers = {
        'Authorization': 'Bearer ' + access_token,
        'Content-Type': 'application/json'
    }
    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    if 'value' in data and len(data['value']) > 0:
        return True
    return False

# Example usage
if __name__ == "__main__":
    start_time = datetime.datetime.now()
    end_time = start_time + datetime.timedelta(hours=2)
    staff_ids = get_staff_ids()
    for staff_id in staff_ids:
        availability = check_staff_availability(staff_id, start_time, end_time)
        print(f"Staff ID: {staff_id}, Available: {availability}")
