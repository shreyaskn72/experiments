# Microsoft Bookings Business Creator

This Python script allows you to create a new Microsoft Bookings business using the `msgraph` module.

## Prerequisites

Before using this script, you need to have the following:

1. **Azure Active Directory Application**: Register your application in the Azure Active Directory and note down the client ID and client secret.

2. **Microsoft Graph API Permissions**: Assign the necessary permissions to your application to create Bookings businesses.

3. **Python Environment**: Ensure you have Python installed on your system.

4. **Required Libraries**: Install the `msgraph` module using the following command:
```
pip install msgraph
```

## Usage

1. Clone the repository to your local machine or download the Python script.

2. Open the script `create_bookings_business_msgraph.py` in a text editor.

3. Replace the placeholder values with your actual values:
- `YOUR_CLIENT_ID`: Replace with your Azure Active Directory Application client ID.
- `YOUR_CLIENT_SECRET`: Replace with your Azure Active Directory Application client secret.
- `YOUR_TENANT_ID`: Replace with your Azure Active Directory tenant ID.
- Adjust the data in the `create_bookings_business` function according to your requirements, such as display name, email, phone number, and timezone.

4. Save the changes.

5. Run the script using the following command:

```
python create_bookings_business_msgraph.py
```

6. The script will authenticate with the Microsoft Graph API and create a new Bookings business.

## Additional Information

- If you encounter any issues or errors, please check your Azure Active Directory settings, permissions, and ensure the provided credentials are correct.
- For more information about the Microsoft Graph API and Microsoft Bookings, refer to the [Microsoft Graph API documentation](https://docs.microsoft.com/en-us/graph/api/overview?view=graph-rest-beta).
This README.md file provides instructions on how to use the Python script with the msgraph module to create a new Microsoft Bookings business, prerequisites, usage steps, and additional information about the Microsoft Graph API and Microsoft Bookings. Adjust the instructions and details as needed.