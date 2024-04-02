# Microsoft Booking API: Refresh Token to List Meeting Types

This Python script demonstrates how to use a refresh token to obtain a new access token and then list meeting types in the Microsoft Booking API.

## Prerequisites

- Python 3.x installed on your system.
- `requests` library. Install it using `pip install requests`.
- Refresh token obtained through the initial OAuth 2.0 authorization process.
- Client ID and Client Secret obtained by registering an application in Azure Active Directory (Azure AD).

## Configuration

1. Replace `"YOUR_REFRESH_TOKEN"`, `"YOUR_CLIENT_ID"`, and `"YOUR_CLIENT_SECRET"` with your actual refresh token, client ID, and client secret, respectively.
2. Optionally, adjust the Microsoft OAuth token endpoint URL (`token_url`) to use the common endpoint or specify a specific tenant if necessary.

## Usage

1. Run the script.
2. The script will use the refresh token to obtain a new access token.
3. The new access token is then used to list meeting types in the Microsoft Booking API.

## Important Notes

- Ensure that your Azure AD application is properly registered with the necessary permissions to access the Microsoft Booking API.
- Keep your refresh token, client ID, and client secret secure and do not expose them publicly.
- Handle errors and exceptions appropriately in a production environment.

## Example output of the access token response
```json
{
    "token_type": "Bearer",
    "expires_in": 3600,
    "access_token": "eyJhbGciOiJSUzI1NiIsImtpZCI6IjEwMDAxMjMwMDAwMDAwMDAxIiwidHlwIjoiSldUIn0.eyJuYmYiOjE1OTM3NTYwNDUsImV4cCI6MTU5Mzc1OTY0NSwiaXNzIjoiaHR0cHM6Ly9sb2dpbi5taWNyb3NvZnRvbmxpbmUuY29tL2UyNjJmYjg2LTg1YzQtNDMzNS05N2UwLThiZTQ2YmFhYmZmYy9hcGkvdjIvIiwiYXVkIjpbImh0dHBzOi8vbG9naW4ubWljcm9zb2Z0b25saW5lLmNvbS9lMjYyZmI4Ni04NWM0LTQzMzUtOTdlMC04YmU0NmJhYWJmZmMiLCJodHRwczovL2xvZ2luLm1pY3Jvc29mdG9ubGluZS5jb20vZXJyb3JzL3Jlc291cmNlcyIsImh0dHBzOi8vbG9naW4ubWljcm9zb2Z0b25saW5lLmNvbS9lMjYyZmI4Ni04NWM0LTQzMzUtOTdlMC04YmU0NmJhYWJmZmMvcHJvdmlkZXJzIl0sImNsaWVudF9pZCI6ImQ4OTU5M2Q2LTlhY2EtNDM1Yi1iYzZiLTczNzM1MjRlMzYzYiIsImNsaWVudF9jb3JzIjpbIm9wZW5pZCIsIm9wZW5pZC5hcGkiXSwic3ViIjoiZ3Vlc3QtdXNlciIsImF1dGhfdGltZSI6MTU5Mzc1NjA0NSwiaWRwIjoibG9jYWwiLCJyb2xlcyI6WyJhZG1pbiIsImFwaSIsInVtYV9hdXRoIl0sInVzZXJfaWQiOiJHVUVTVC11c2VyIn0.jzMcT5zG9bFfwfioGvzS21j8QaLNEtYU1hrVMBln2z5o2L-N7Fh1vUnWNqG2BosCHyDwZUVapOqfWjE-H4KZVXZtTR2e3pK77g91RvvoE_Ot7UoBxIfa3e2vVKxcyPPlvSoPzg8lGkI93F0zijJLzEYtCvDPhq1Zr76i_MaQem8MCFsRr4UuY6-S1w0FBuS9IdAD1KgsW2m31pAG0_LFX5MFe3g6ab2bvh1kiWfndgY5l1O8uAz99wWwiJbYcU2wll9tNRan4q71x2zlfI1dFc-2mjF1zj7OVPrhWb5gT_XvCkfbAFL82qG7TC0tcKQEFkFJJihQnI0cZqM9Xvvg",
    "refresh_token": "AQABAAAAAADX8GCi6JLlT5g4PgMWYaJkKwkwCMxK2XCBQRbDpb0I7...XZK9KUlyS0pPYx57b9Jiv1BAcLL7csRe_a1R_gNmBm8npAwi2AgAA",
    "scope": "openid email profile https://graph.microsoft.com/.default",
    "id_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJub25lIn0.eyJhdWQiOiJodHRwczovL2dyb3Vwcy5taWNyb3NvZnRvbmxpbmUuY29tLyIsImlzcyI6Imh0dHBzOi8vbG9jYWxob3N0OjQ0MzUxLyIsImV4cCI6MTU3MzEwMjYxNSwiaWF0IjoxNTczMTAwNjE1LCJub25jZSI6IjU1ZDBl"
}
```