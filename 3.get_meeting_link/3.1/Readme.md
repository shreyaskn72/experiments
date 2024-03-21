# Microsoft Booking Meeting Details Retriever

This Python script retrieves meeting details, including the meeting date, meeting time, and meeting URL, based on a recipient's email address and event type in Microsoft Bookings.

## Requirements

- Python 3.x
- `requests` library (install via `pip install requests`)
- Azure Active Directory App Registration with necessary permissions for Microsoft Graph API access

## Setup

1. Clone this repository or copy the provided Python script (`meeting_details_retriever.py`) to your local machine.
2. Install the required Python packages:


pip install requests

3. Register an application in Azure Active Directory:
- Go to the [Azure portal](https://portal.azure.com/).
- Navigate to **Azure Active Directory** > **App registrations** and register a new application.
- Note down the Application (client) ID, Directory (tenant) ID, and create a client secret.
- Grant necessary permissions to the application to access the Microsoft Graph API, such as `Calendars.Read` and `Calendars.Read.Shared`.
4. Update the script:
- Replace `'YOUR_CLIENT_ID'`, `'YOUR_CLIENT_SECRET'`, `'YOUR_TENANT_ID'`, and `'recipient@example.com'` placeholders in the script with the corresponding values obtained in steps 3.
5. Run the script:


python meeting_details_retriever.py


## Functionality and API Interaction

The script interacts with the Microsoft Graph API to retrieve meeting details based on the recipient's email address and event type. Here's how it works:

- **Authentication**: The script uses OAuth 2.0 authentication to obtain an access token from Azure Active Directory. This access token is used to authenticate requests to the Microsoft Graph API.

- **Retrieving Meeting Details**: Using the obtained access token, recipient's email address, and event type, the script sends a request to the Microsoft Graph API to fetch calendar events.

- **Parsing Events**: The script parses the response from the API and filters events based on the event type. It then extracts the meeting date, meeting time, and meeting URL from the matching event.

- **Output**: If a matching event is found, the script prints the meeting date, meeting time, and meeting URL to the console. Otherwise, it displays a message indicating no matching event was found.

## Usage

Once the script is set up and configured with your Microsoft Booking information, you can run it to retrieve meeting details for a specific recipient's email address and event type.

## Note

- Ensure that the Azure Active Directory application has the necessary permissions to access the Microsoft Graph API resources required by the script.
- Adjust the recipient's email address and event type in the script to match your scenario.


