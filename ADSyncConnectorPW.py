from __future__ import print_function
import deepsecurity
from deepsecurity.rest import ApiException

# Setup: Initialize the connection to your Deep Security Manager instance
configuration = deepsecurity.Configuration()
configuration.host = 'https://192.168.1.200:443/api'  # Replace with your Deep Security Manager URL

# Authentication: Insert your shared API key for authentication
configuration.api_key['api-secret-key'] = 'YOUR_API_KEY_HERE'  # Replace with your actual API key

# Initialize API instance for AD Sync connector operations
api_instance_ldap = deepsecurity.LdapSyncConnectorsApi(deepsecurity.ApiClient(configuration))

# Set the connector ID and new password
connector_id_ldap = 1  # The unique ID of the AD Sync connector. Retrieve using list_ldap_sync_connectors().
api_version = 'v1'  # API version to use

# Define the new password for the AD Sync connector account
ldap_sync_connector = deepsecurity.LdapSyncConnector(password="NEW_PASSWORD_HERE")  # Replace with the new password

try:
    # Update the AD Sync connector password
    api_response_ldap = api_instance_ldap.modify_ldap_sync_connector(connector_id_ldap, ldap_sync_connector, api_version)
    print(api_response_ldap)  # Print the response to verify success
except ApiException as e:
    # Catch and print any API errors
    print("An exception occurred when calling LdapSyncConnectorsApi.modify_ldap_sync_connector: %s\n" % e)
