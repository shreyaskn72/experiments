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

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
