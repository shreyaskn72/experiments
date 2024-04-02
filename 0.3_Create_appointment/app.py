import requests
import json
from datetime import datetime

def schedule_appointment(access_token, meeting_type, attendees):
    # Microsoft Booking API endpoint to create an appointment
    endpoint = "https://graph.microsoft.com/v1.0/me/bookings/appointments"

    # Appointment details
    start_time = "2024-04-10T10:00:00"  # Start time of the appointment in ISO 8601 format
    end_time = "2024-04-10T11:00:00"    # End time of the appointment in ISO 8601 format
    subject = "Meeting with Clients"    # Subject of the appointment
    location = "Office 123"             # Location of the appointment

    # Request headers including authorization with access token
    headers = {
        "Authorization": "Bearer " + access_token,
        "Content-Type": "application/json"
    }

    # Prepare a list of attendees with their email addresses and names
    attendees_list = []
    for attendee in attendees:
        attendees_list.append({
            "emailAddress": {"address": attendee["email"]},
            "type": "required",
            "displayName": attendee["name"]
        })

    # Request payload with appointment details including attendees and meeting type
    payload = {
        "start": {
            "dateTime": start_time,
            "timeZone": "UTC"
        },
        "end": {
            "dateTime": end_time,
            "timeZone": "UTC"
        },
        "subject": subject,
        "location": {
            "displayName": location
        },
        "attendees": attendees_list,
        "meetingType": meeting_type
    }

    # Send POST request to create appointment
    response = requests.post(endpoint, headers=headers, data=json.dumps(payload))

    # Check if request was successful
    if response.status_code == 201:
        print("Appointment scheduled successfully.")
    else:
        print("Failed to schedule appointment.")
        print("Error:", response.status_code)
        print(response.text)

def main():
    # Access token obtained from the previous step
    access_token = "YOUR_ACCESS_TOKEN"

    # Input meeting type
    meeting_type = input("Enter meeting type: ")

    # Input attendees' email addresses and names as a list of dictionaries
    attendees = [
        {"email": "attendee1@example.com", "name": "John Doe"},
        {"email": "attendee2@example.com", "name": "Jane Doe"}
    ]

    # Schedule appointment with meeting type and multiple attendees
    schedule_appointment(access_token, meeting_type, attendees)

if __name__ == "__main__":
    main()
