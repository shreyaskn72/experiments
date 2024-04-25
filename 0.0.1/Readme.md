# Microsoft Graph API Access and Refresh Token Retrieval

This Python script demonstrates how to obtain access and refresh tokens from Azure Active Directory (Azure AD) for accessing the Microsoft Graph API. The tokens can be used to authenticate requests to various Microsoft services, such as Microsoft Bookings, Outlook, and more.

## Requirements

- Python 3.x
- `requests` library (install via `pip install requests`)

## Usage

1. Clone or download the provided Python script.

2. Update the following variables in the script with your Azure AD application details:
   - `TENANT_ID`: Your Azure AD tenant ID.
   - `CLIENT_ID`: Your Azure AD application (client) ID.
   - `CLIENT_SECRET`: Your Azure AD application client secret.
   - `REDIRECT_URI`: The redirect URI configured in your Azure AD application.

3. Ensure that your Azure AD application is configured with the necessary permissions to access the Microsoft Graph API. In particular, ensure that the required API permissions, such as `Bookings.ReadWrite.All`, are granted.

4. Run the Python script in your terminal or command prompt.

5. Follow the instructions printed in the terminal:
   - Open the provided authorization URL in your web browser.
   - Log in with your Azure AD credentials and grant consent to the application.
   - Copy the authorization code from the redirected URL and paste it into the terminal.

6. Upon successful authentication and authorization, the script will retrieve the access token and, if applicable, the refresh token from Azure AD.

## Script Explanation

- The script first constructs the authorization URL with the appropriate parameters and opens it in the default web browser.

- After the user logs in and grants consent, the script exchanges the authorization code for an access token and refresh token using the token endpoint.

- The retrieved tokens are printed to the terminal, allowing you to use them in your application to access Microsoft Graph API endpoints.

## Note

- Ensure that your application securely handles the obtained access and refresh tokens. Protect these tokens as sensitive information and avoid hardcoding them in your application source code.




# Microsoft Bookings API Token Response Parameters

When you request an access token from the Microsoft Bookings API, you receive a JSON response containing several parameters. Here's an explanation of each parameter:

- `token_type`: The type of token returned. Typically, it's `"Bearer"` for OAuth 2.0 tokens.

- `expires_in`: The duration, in seconds, for which the access token is valid.

- `ext_expires_in`: The duration, in seconds, for which the extended access token is valid.

- `access_token`: The access token that can be used to authenticate requests to the Microsoft Graph API.

- `refresh_token`: A token that can be used to obtain a new access token when the current access token expires, without requiring the user to re-authenticate.

- `scope`: The scope of the access token.

- `id_token`: If the request included the `openid` scope, this field contains an identity token for the authenticated user.

- `token_type`: The token type.

- `not_before`: The time before which the token cannot be used.

- `expires_on`: The time at which the token expires.

- `resource`: The resource identifier for the token.

- `profile_info`: Additional information about the user profile, if requested.

These parameters provide information about the access token, its expiration, scope, and associated user identity.

