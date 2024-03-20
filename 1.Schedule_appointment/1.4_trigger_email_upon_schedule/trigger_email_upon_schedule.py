import requests
from datetime import datetime, timedelta

# Your application details
client_id = "YOUR_CLIENT_ID"
client_secret = "YOUR_CLIENT_SECRET"
tenant_id = "YOUR_TENANT_ID"

# Microsoft Graph API endpoints
token_endpoint = f"https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token"
events_endpoint = f"https://graph.microsoft.com/beta/me/calendar/events"
send_mail_endpoint = f"https://graph.microsoft.com/v1.0/me/sendMail"

# Function to get access token
def get_access_token():
    token_url = token_endpoint
    data = {
        'client_id': client_id,
        'client_secret': client_secret,
        'scope': 'https://graph.microsoft.com/.default',
        'grant_type': 'client_credentials'
    }
    response = requests.post(token_url, data=data)
    access_token = response.json().get('access_token')
    return access_token

# Function to send email notification
def send_email_notification(access_token, recipient_email, subject, body):
    headers = {
        'Authorization': 'Bearer ' + access_token,
        'Content-Type': 'application/json'
    }

    data = {
        "message": {
            "subject": subject,
            "body": {
                "contentType": "Text",
                "content": body
            },
            "toRecipients": [
                {
                    "emailAddress": {
                        "address": recipient_email
                    }
                }
            ]
        }
    }

    response = requests.post(send_mail_endpoint, headers=headers, json=data)

    if response.status_code == 202:
        print(f"Email notification sent successfully to {recipient_email}.")
    else:
        print("Failed to send email notification:", response.text)

# Function to schedule an appointment with custom meeting type
def schedule_appointment(access_token, recipients, meeting_type):
    headers = {
        'Authorization': 'Bearer ' + access_token,
        'Content-Type': 'application/json'
    }

    # Prepare appointment data
    start_time = (datetime.now() + timedelta(days=1)).isoformat()
    end_time = (datetime.now() + timedelta(days=1, hours=1)).isoformat()
    data = {
        "subject": "Appointment with Clients",
        "start": {
            "dateTime": start_time,
            "timeZone": "UTC"
        },
        "end": {
            "dateTime": end_time,
            "timeZone": "UTC"
        },
        "attendees": [
            {
                "emailAddress": {
                    "address": recipient["email"],
                    "name": recipient["name"]
                },
                "type": "required"
            }
            for recipient in recipients
        ],
        "categories": [
            {
                "displayName": meeting_type
            }
        ]
    }

    # Send POST request to create the appointment
    response = requests.post(events_endpoint, headers=headers, json=data)

    if response.status_code == 201:
        print("Appointment scheduled successfully.")
        # Send email notification to each recipient
        for recipient in recipients:
            send_email_notification(access_token, recipient["email"], "Appointment Scheduled", "You have a new appointment scheduled.")
    else:
        print("Failed to schedule appointment:", response.text)

if __name__ == "__main__":
    access_token = get_access_token()
    if access_token:
        recipients = [
            {"email": "recipient1@example.com", "name": "Recipient 1"},
            {"email": "recipient2@example.com", "name": "Recipient 2"},
            # Add more recipients as needed
        ]
        meeting_type = "Your Custom Meeting Type"
        schedule_appointment(access_token, recipients, meeting_type)
    else:
        print("Failed to obtain access token.")
