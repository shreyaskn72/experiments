import requests

# Your application details
client_id = "YOUR_CLIENT_ID"
client_secret = "YOUR_CLIENT_SECRET"
tenant_id = "YOUR_TENANT_ID"

# Microsoft Graph API endpoints
token_endpoint = f"https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token"
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

# Function to send email with meeting template
def send_email_with_template(access_token, recipient_email, start_time, end_time):
    headers = {
        'Authorization': 'Bearer ' + access_token,
        'Content-Type': 'application/json'
    }

    # Prepare email content with meeting template
    meeting_details = """
        <b>Meeting Details:</b><br>
        Start Time: {start_time}<br>
        End Time: {end_time}<br>
        Location: Virtual<br>
        Description: Discussion on project updates.<br>
    """.format(
        start_time=start_time,
        end_time=end_time
    )

    # Prepare email message
    data = {
        "message": {
            "subject": "Meeting Invitation",
            "body": {
                "contentType": "HTML",
                "content": f"<p>Hello,</p><p>You are invited to a meeting.</p>{meeting_details}"
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
        print(f"Email sent successfully to {recipient_email}.")
    else:
        print("Failed to send email:", response.text)

if __name__ == "__main__":
    access_token = get_access_token()
    if access_token:
        recipient_email = "recipient@example.com"
        start_time = input("Enter start time (format: YYYY-MM-DDTHH:MM:SS): ")
        end_time = input("Enter end time (format: YYYY-MM-DDTHH:MM:SS): ")
        send_email_with_template(access_token, recipient_email, start_time, end_time)
    else:
        print("Failed to obtain access token.")
