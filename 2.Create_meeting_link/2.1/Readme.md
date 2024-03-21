# Microsoft Booking Meeting Link Generator

This Python script allows you to generate meeting links for Microsoft Bookings based on meeting types.

## Requirements

- Python 3.x
- `requests` library (install via `pip install requests`)
- Azure Active Directory App Registration with necessary permissions for Microsoft Graph API access

## Setup

1. Clone this repository or copy the provided Python script (`meeting_link_generator.py`) to your local machine.
2. Install the required Python packages:

pip install requests

3. Register an application in Azure Active Directory:
- Go to the [Azure portal](https://portal.azure.com/).
- Navigate to **Azure Active Directory** > **App registrations** and register a new application.
- Note down the Application (client) ID, Directory (tenant) ID, and create a client secret.
- Grant necessary permissions to the application to access the Microsoft Graph API, such as `OnlineMeetings.ReadWrite`, `BookingsAppointment.ReadWrite`, and `Bookings.ReadWrite.All`.
4. Obtain the Booking Business ID:
- Log in to Microsoft Bookings.
- Navigate to **Booking page** > **Booking settings** > **Business information**. Copy the Business ID.
5. Update the script:
- Replace `'YOUR_CLIENT_ID'`, `'YOUR_CLIENT_SECRET'`, `'YOUR_TENANT_ID'`, `'YOUR_BOOKING_ID'`, and `'YOUR_MEETING_TYPE_ID'` placeholders in the script with the corresponding values obtained in steps 3 and 4.
6. Run the script:

python meeting_link_generator.py


## Functionality and API Interaction

The script interacts with the Microsoft Graph API to create online meeting links for specific meeting types configured in Microsoft Bookings. Here's how it works:

- **Authentication**: The script uses OAuth 2.0 authentication to obtain an access token from Azure Active Directory. This access token is used to authenticate requests to the Microsoft Graph API.

- **Generating Meeting Links**: Using the obtained access token and provided Booking Business ID, the script sends a request to the Microsoft Graph API to create an online meeting for a specific meeting type.

- **Payload Structure**: The payload sent to the Microsoft Graph API includes the start and end date-time of the meeting, participant details (such as email address), and other necessary parameters.

- **Response Handling**: Upon successful creation of the meeting, the API returns a response containing the meeting link (`joinWebUrl`). The script parses this response and prints the meeting link to the console.

- **Error Handling**: If any errors occur during the API interaction, such as authentication failure or invalid input data, appropriate error messages are displayed.

## Usage

Once the script is set up and configured with your Microsoft Booking information, you can run it to generate meeting links for different meeting types. The generated meeting link will be printed to the console.

## Note

- Ensure that the Azure Active Directory application has the necessary permissions to access the Microsoft Graph API resources required by the script.
- The script assumes that you have already created meeting types in Microsoft Bookings. You need to provide the ID of the meeting type for which you want to generate a meeting link.
- Adjust the payload structure in the script if you want to include multiple participants or modify other properties of the meeting.
