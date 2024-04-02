# Microsoft Booking API: Schedule Appointments

This Python script allows you to schedule appointments in the Microsoft Booking API. It uses OAuth 2.0 authentication and requires an access token to interact with the API.

## Prerequisites

- Python 3.x installed on your system.
- `requests` library. Install it using `pip install requests`.
- Access token obtained through the OAuth 2.0 authentication process.
- Registered Azure Active Directory (Azure AD) application with appropriate permissions to access the Microsoft Booking API.

## Configuration

1. Replace `"YOUR_ACCESS_TOKEN"` with the actual access token obtained from the OAuth 2.0 authentication process.
2. Optionally, modify the appointment details such as start time, end time, subject, and location according to your requirements.
3. Input meeting type and attendees' email addresses and names as needed.

## Usage

1. Run the script.
2. Input meeting type when prompted.
3. Input attendees' email addresses and names as a list of dictionaries.
4. The script will schedule the appointment in the Microsoft Booking API.

## Important Notes

- Ensure that your Azure AD application is properly configured with the necessary permissions to create appointments in the Microsoft Booking API.
- Keep your access token and client credentials secure and do not expose them publicly.
- Handle errors and exceptions appropriately in a production environment.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
