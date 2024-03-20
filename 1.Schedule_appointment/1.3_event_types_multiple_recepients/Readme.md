# Microsoft Bookings Appointment Scheduler

This Python script allows you to schedule an appointment in Microsoft Bookings with multiple recipients and a custom meeting type using the Microsoft Graph API.

## Prerequisites

Before using this script, ensure you have the following:

1. **Azure Active Directory Application**: Register your application in the Azure Active Directory and note down the client ID and client secret.

2. **Microsoft Graph API Permissions**: Assign the necessary permissions to your application to create events in Bookings calendars.

3. **Python Environment**: Ensure you have Python installed on your system.

4. **Required Libraries**: Install the `requests` library using the following command:

```
pip install requests
```


## Usage

1. Clone the repository to your local machine or download the Python script.

2. Open the script `schedule_appointment.py` in a text editor.

3. Replace the placeholder values with your actual values:
- `YOUR_CLIENT_ID`: Replace with your Azure Active Directory Application client ID.
- `YOUR_CLIENT_SECRET`: Replace with your Azure Active Directory Application client secret.
- `YOUR_TENANT_ID`: Replace with your Azure Active Directory tenant ID.

4. Customize the recipient details and meeting type:
- Modify the `recipients` list to include the email addresses and names of the recipients.
- Adjust the value of `meeting_type` to specify your desired meeting type.

5. Save the changes.

6. Run the script using the following command:
```
python schedule_appointment.py
```


7. The script will authenticate with the Microsoft Graph API and schedule an appointment with the specified recipients and meeting type.

## Example Request

The script sends a POST request to the Microsoft Graph API endpoint to create the appointment. The request body contains the appointment details such as subject, start time, end time, attendees (recipients), and meeting type.

Example request body:
```json
{
 "subject": "Appointment with Clients",
 "start": {
     "dateTime": "2024-03-25T09:00:00Z",
     "timeZone": "UTC"
 },
 "end": {
     "dateTime": "2024-03-25T10:00:00Z",
     "timeZone": "UTC"
 },
 "attendees": [
     {
         "emailAddress": {
             "address": "recipient1@example.com",
             "name": "Recipient 1"
         },
         "type": "required"
     },
     {
         "emailAddress": {
             "address": "recipient2@example.com",
             "name": "Recipient 2"
         },
         "type": "required"
     }
 ],
 "categories": [
     {
         "displayName": "Your Custom Meeting Type"
     }
 ]
}
```

## Example Response
If the appointment is scheduled successfully, the script will display a success message. Otherwise, it will display an error message.

## Example response:
```
Appointment scheduled successfully.
```

## Additional Information

- If you encounter any issues or errors, please check your Azure Active Directory settings, permissions, and ensure the provided credentials are correct.
- For more information about the Microsoft Graph API and Microsoft Bookings, refer to the [Microsoft Graph API documentation](https://docs.microsoft.com/en-us/graph/api/overview?view=graph-rest-beta).
