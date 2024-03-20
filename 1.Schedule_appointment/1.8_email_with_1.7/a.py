from msal import ConfidentialClientApplication
from datetime import datetime, timedelta
from msgraph.client import Client
from msgraph.calendar import Event
from msgraph.users import User
from msgraph.directoryObjects import DirectoryObject


# Function to obtain access token
def get_access_token(client_id, client_secret, tenant_id):
    authority = f"https://login.microsoftonline.com/{tenant_id}"
    app = ConfidentialClientApplication(client_id, authority=authority, client_credential=client_secret)
    result = app.acquire_token_for_client(scopes=["https://graph.microsoft.com/.default"])

    if "access_token" in result:
        return result["access_token"]
    else:
        print("Failed to obtain access token:", result.get("error_description", "Unknown error"))


# Function to send email notification
def send_email_notification(access_token, recipient_email):
    client = Client(access_token)

    # Prepare email data
    email_data = {
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
    response = client.me.send_mail(email_data)

    if response.status_code == 202:
        print(f"Email notification sent successfully to {recipient_email}.")
    else:
        print("Failed to send email notification:", response.text)


# Function to schedule an appointment
def schedule_appointment(access_token, meeting_type, recipients):
    client = Client(access_token)

    # Prepare appointment data
    start_time = datetime.now() + timedelta(days=1)
    end_time = start_time + timedelta(hours=1)

    event = Event(
        subject="Meeting with Multiple Recipients",
        start=start_time,
        end=end_time,
        location={"displayName": "Virtual"},
        categories=[meeting_type],
        attendees=[DirectoryObject(email_address=recipient["email"]) for recipient in recipients]
    )

    # Send POST request to create the appointment
    response = client.solutions.bookingBusinesses.appointments.post(event)

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

    meeting_type = input("Enter meeting type: ")

    recipients = [
        {"email": "recipient1@example.com", "name": "Recipient 1"},
        {"email": "recipient2@example.com", "name": "Recipient 2"}
    ]

    access_token = get_access_token(client_id, client_secret, tenant_id)
    if access_token:
        schedule_appointment(access_token, meeting_type, recipients)
    else:
        print("Failed to obtain access token.")
