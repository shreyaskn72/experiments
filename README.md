# Obtaining Client ID, Client Secret, and Tenant ID for Your Azure AD Application

This guide outlines the steps to obtain the client ID, client secret, and tenant ID for your Azure Active Directory (Azure AD) application in the Azure portal.

## Prerequisites

Before you begin, ensure that you have:
- Access to the Azure portal with sufficient permissions to manage Azure AD applications.
- An Azure AD tenant under which your application will be registered.

## Steps

1. **Sign in to Azure portal**:
   - Go to [Azure portal](https://portal.azure.com/).
   - Sign in with your Azure account credentials.

2. **Navigate to Azure Active Directory**:
   - In the left-hand menu, click on "Azure Active Directory" to access the Azure AD section.

3. **Register Your Application**:
   - Under "Manage," select "App registrations" to register your application.
   - Click on "+ New registration" to create a new Azure AD application.
   - Enter a name for your application, choose the supported account types, and specify the Redirect URI (if applicable).
   - Click "Register" to create the application.

4. **Retrieve Client ID**:
   - Once your application is registered, you'll be redirected to its overview page.
   - Note down the "Application (client) ID" listed on this page. This is your client ID.

5. **Generate Client Secret**:
   - In your application's overview page, navigate to "Certificates & secrets" under "Manage."
   - Click on "+ New client secret" to create a new client secret.
   - Provide a description, select the desired expiration duration, and click "Add."
   - Copy the generated client secret immediately as it will be hidden later.

6. **Find Tenant ID**:
   - In the Azure portal, navigate to Azure Active Directory > Properties.
   - Note down the "Directory ID" listed on this page. This is your tenant ID.

## Next Steps

Now that you have obtained the client ID, client secret, and tenant ID for your Azure AD application, you can use them in your application for authentication and authorization with Azure AD services.

Make sure to keep the client secret secure and do not expose it publicly. If you suspect that the client secret has been compromised, you can regenerate it in the Azure portal.

For further assistance or troubleshooting, refer to the Azure AD documentation or reach out to Azure support.
