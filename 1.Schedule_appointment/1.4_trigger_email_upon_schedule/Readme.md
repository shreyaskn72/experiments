# Microsoft Bookings Appointment Scheduler

This Python script allows you to schedule an appointment in Microsoft Bookings with multiple recipients and a custom meeting type using the Microsoft Graph API. It also sends email notifications to the recipients after scheduling the appointment.

## Prerequisites

Before using this script, ensure you have the following:

1. **Azure Active Directory Application**: Register your application in the Azure Active Directory and note down the client ID and client secret.

2. **Microsoft Graph API Permissions**: Assign the necessary permissions to your application to create events in Bookings calendars and send email notifications.

3. **Python Environment**: Ensure you have Python installed on your system.

4. **Required Libraries**: Install the `requests` library using the following command:

