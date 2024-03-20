# Microsoft Bookings Business Fetcher

This Python script allows you to fetch the list of Bookings businesses in a tenant using the Microsoft Graph API.

## Prerequisites

Before using this script, you need to have the following:

1. **Azure Active Directory Application**: Register your application in the Azure Active Directory and note down the client ID and client secret.

2. **Microsoft Graph API Permissions**: Assign the necessary permissions to your application to read Bookings businesses.

3. **Python Environment**: Ensure you have Python installed on your system.

4. **Required Libraries**: Install the `requests` library using the following command:
```
pip install requests
```

## Usage

1. Clone the repository to your local machine or download the Python script.

2. Open the script `get_bookings_businesses.py` in a text editor.

3. Replace the placeholder values with your actual values:
- `YOUR_CLIENT_ID`: Replace with your Azure Active Directory Application client ID.
- `YOUR_CLIENT_SECRET`: Replace with your Azure Active Directory Application client secret.
- `YOUR_TENANT_ID`: Replace with your Azure Active Directory tenant ID.

4. Save the changes.

5. Run the script using the following command:
```
python get_bookings_businesses.py
```


6. The script will authenticate with the Microsoft Graph API and fetch the list of Bookings businesses in the tenant.

## Example Request

The script sends a GET request to the following endpoint:

https://graph.microsoft.com/beta/bookingBusinesses


## Example Response

The response from the Microsoft Graph API would typically be a JSON object containing information about each business. Here's an example response structure:

```json
{
  "value": [
    {
      "id": "business_id_1",
      "displayName": "Business Name 1",
      "email": "business1@example.com",
      "phone": "+1234567890"
    },
    {
      "id": "business_id_2",
      "displayName": "Business Name 2",
      "email": "business2@example.com",
      "phone": "+9876543210"
    }
  ]
}
```


Each item in the "value" array represents a Bookings business. The fields include:

- "id": The unique identifier of the business.
- "displayName": The display name of the business.
- "email": The email associated with the business.
- "phone": The phone number associated with the business.

You would receive similar JSON data for each business in the tenant. This response can be parsed and processed accordingly in your Python script.

## Additional Information
- If you encounter any issues or errors, please check your Azure Active Directory settings, permissions, and ensure the provided credentials are correct.
- For more information about the Microsoft Graph API and Microsoft Bookings, refer to the [Microsoft Graph API documentation](https://docs.microsoft.com/en-us/graph/api/overview?view=graph-rest-beta).


This README.md file now includes examples of both the request sent by the script and the typical response received from the Microsoft Graph API when fetching Bookings businesses. Adjust the instructions and details as needed.
