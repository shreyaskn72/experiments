from msgraph.client import GraphClient

# Your application details
client_id = "YOUR_CLIENT_ID"
client_secret = "YOUR_CLIENT_SECRET"
tenant_id = "YOUR_TENANT_ID"

# Function to fetch Bookings businesses
def get_bookings_businesses():
    # Authenticate with Microsoft Graph API
    client = GraphClient(client_id=client_id, client_secret=client_secret, tenant_id=tenant_id)

    # Fetch Bookings businesses
    response = client.get("/bookingBusinesses")

    if response.status_code == 200:
        businesses = response.json().get('value', [])
        for business in businesses:
            print("Business ID:", business.get('id'))
            print("Display Name:", business.get('displayName'))
            print("Email:", business.get('email'))
            print("Phone:", business.get('phone'))
            print()
    else:
        print("Failed to get Bookings businesses:", response.text)

if __name__ == "__main__":
    get_bookings_businesses()
