from msgraph.client import GraphClient

# Your application details
client_id = "YOUR_CLIENT_ID"
client_secret = "YOUR_CLIENT_SECRET"
tenant_id = "YOUR_TENANT_ID"

# Function to create a new Microsoft Bookings business
def create_bookings_business():
    # Authenticate with Microsoft Graph API
    client = GraphClient(client_id=client_id, client_secret=client_secret, tenant_id=tenant_id)

    # Data for creating the new business
    data = {
        "displayName": "My Bookings Business",
        "email": "bookings@example.com",
        "phone": "+1234567890",
        "timeZone": "Pacific Standard Time"  # Replace with your desired timezone
    }

    response = client.post("/bookingBusinesses", json=data)

    if response.status_code == 201:
        print("New Bookings business created successfully.")
    else:
        print("Failed to create Bookings business:", response.text)

if __name__ == "__main__":
    create_bookings_business()
