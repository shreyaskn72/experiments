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

