import requests
from datetime import datetime, timedelta

# Microsoft Graph API endpoints
token_endpoint = "https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token"
appointments_endpoint = "https://graph.microsoft.com/v1.0/solutions/bookingBusinesses/appointments"
send_mail_endpoint = "https://graph.microsoft.com/v1.0/me/sendMail"


# Function to get access token
def get_access_token(client_id, client_secret, tenant_id):
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


# Function to send email notification
def send_email_notification(access_token, recipient_email):
    headers = {
        'Authorization': 'Bearer ' + access_token,
        'Content-Type': 'application/json'
    }

    # Prepare email message
    data = {
        "message": {
            "subject": "Appointment Scheduled",
            "body": {
                "contentType": "Text",
                "content": "Your appointment has been scheduled successfully."
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

    # Send POST request to send email
    response = requests.post(send_mail_endpoint, headers=headers, json=data)

    if response.status_code == 202:
        print(f"Email notification sent successfully to {recipient_email}.")
    else:
        print("Failed to send email notification:", response.text)


# Function to schedule an appointment
def schedule_appointment(access_token, meeting_type, recipients):
    headers = {
        'Authorization': 'Bearer ' + access_token,
        'Content-Type': 'application/json'
    }

    # Prepare appointment data
    start_time = (datetime.now() + timedelta(days=1)).isoformat()
    end_time = (datetime.now() + timedelta(days=1, hours=1)).isoformat()
    data = {
        "start": {
            "dateTime": start_time,
            "timeZone": "UTC"
        },
        "end": {
            "dateTime": end_time,
            "timeZone": "UTC"
        },
        "serviceId": meeting_type,
        "customers": [
            {
                "email": recipient["email"],
                "name": recipient["name"]
            }
            for recipient in recipients
        ]
    }

    # Send POST request to create the appointment
    response = requests.post(appointments_endpoint, headers=headers, json=data)

    if response.status_code == 201:
        print("Appointment scheduled successfully.")
        for recipient in recipients:
            send_email_notification(access_token, recipient["email"])
    else:
        print("Failed to schedule appointment:", response.text)


if __name__ == "__main__":
    client_id = "YOUR_CLIENT_ID"
    client_secret = "YOUR_CLIENT_SECRET"
    tenant_id = "YOUR_TENANT_ID"

    meeting_type = "Input meeting type"

    recipients = [
        {"email": "recipient1@example.com", "name": "Recipient 1"},
        {"email": "recipient2@example.com", "name": "Recipient 2"}
    ]

    access_token = get_access_token(client_id, client_secret, tenant_id)
    if access_token:
        schedule_appointment(access_token, meeting_type, recipients)
    else:
        print("Failed to obtain access token.")
