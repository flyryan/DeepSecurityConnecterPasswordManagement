from __future__ import print_function
import deepsecurity
from deepsecurity.rest import ApiException

# Setup: Initialize the connection to your Deep Security Manager instance
configuration = deepsecurity.Configuration()
configuration.host = 'https://192.168.1.200:443/api'  # Replace with your Deep Security Manager URL

# Authentication: Insert your shared API key for authentication
configuration.api_key['api-secret-key'] = 'YOUR_API_KEY_HERE'  # Replace with your actual API key

# Initialize API instance for NSX Manager connector operations
api_instance_nsx = deepsecurity.NsxManagersApi(deepsecurity.ApiClient(configuration))

# Set the NSX Manager ID and new password
nsx_manager_id = 1  # The unique ID of the NSX Manager. Retrieve using list_nsx_managers().
api_version = 'v1'  # API version to use

# Define the new password for the NSX Manager account
nsx_manager = deepsecurity.NsxManager(password="NEW_PASSWORD_HERE")  # Replace with the new password

try:
    # Update the NSX Manager password
    api_response_nsx = api_instance_nsx.modify_nsx_manager(nsx_manager_id, nsx_manager, api_version)
    print(api_response_nsx)  # Print the response to verify success
except ApiException as e:
    # Catch and print any API errors
    print("An exception occurred when calling NsxManagersApi.modify_nsx_manager: %s\n" % e)
