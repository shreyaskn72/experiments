from msgraph.client import GraphClient

# Your application details
client_id = "YOUR_CLIENT_ID"
client_secret = "YOUR_CLIENT_SECRET"
tenant_id = "YOUR_TENANT_ID"

# The Business ID you want to schedule the appointment for
business_id = "YOUR_BUSINESS_ID"

# Example appointment data
start_time = "2024-03-21T10:00:00Z"  # Start time
end_time = "2024-03-21T11:00:00Z"  # End time
customer_id = "CUSTOMER_ID"
service_id = "SERVICE_ID"

# Authenticate with Microsoft Graph API
client = GraphClient(client_id=client_id, client_secret=client_secret, tenant_id=tenant_id)

# Schedule appointment
response = client.post(f"/bookingBusinesses/{business_id}/appointments", json={
    "customerId": customer_id,
    "serviceId": service_id,
    "start": {
        "dateTime": start_time
    },
    "end": {
        "dateTime": end_time
    }
})

# Check response
if response.status_code == 201:
    print("Appointment scheduled successfully.")
else:
    print("Failed to schedule appointment:", response.text)
