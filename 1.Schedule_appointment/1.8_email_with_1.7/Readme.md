# Schedule Appointment in Microsoft Bookings

This Python script allows you to schedule an appointment in Microsoft Bookings and send email notifications to recipients. It interacts with the Microsoft Graph API to create the appointment and send emails.

## Prerequisites

Before using this script, make sure you have the following:

- Registered application with Microsoft Azure and obtained the client ID, client secret, and tenant ID.
- Required permissions for accessing Microsoft Bookings and sending emails using Microsoft Graph API.
- Python installed on your system.

## Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/your/repository.git
    ```

2. Navigate to the directory:

    ```bash
    cd directory_name
    ```

3. Install the required dependencies:

    ```bash
    pip install msgraph-python-sdk
    ```

## Usage

1. Replace the placeholder values for `YOUR_CLIENT_ID`, `YOUR_CLIENT_SECRET`, and `YOUR_TENANT_ID` in the script with your actual credentials.

2. Run the script:

    ```bash
    python schedule_appointment.py
    ```

3. Enter the requested information:

    - Meeting type: Enter the type of meeting or appointment.
    - Recipients: Enter the email addresses and names of the recipients.

## Example

### Request

- Meeting type: Team meeting
- Recipients:
    - Email: recipient1@example.com, Name: Recipient 1
    - Email: recipient2@example.com, Name: Recipient 2

### Response

The script will output the following:

Appointment scheduled successfully.
Email notification sent successfully to recipient1@example.com.
Email notification sent successfully to recipient2@example.com.


## Notes

- Ensure that your application has the necessary permissions to schedule appointments in Microsoft Bookings and send emails using Microsoft Graph API.
- Modify the script to customize the appointment duration, start time, end time, and other parameters as needed.

## Microsoft Graph API Endpoint

This script interacts with the following Microsoft Graph API endpoint:

- `https://graph.microsoft.com/v1.0/solutions/bookingBusinesses/appointments`: This endpoint is used to create a new appointment in Microsoft Bookings.
