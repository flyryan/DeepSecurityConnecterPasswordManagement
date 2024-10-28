from __future__ import print_function
import deepsecurity
from deepsecurity.rest import ApiException

# Setup: Initialize the connection to your Deep Security Manager instance
configuration = deepsecurity.Configuration()
configuration.host = 'https://192.168.1.200:443/api'  # Replace with your Deep Security Manager URL

# Authentication: Insert your shared API key for authentication
configuration.api_key['api-secret-key'] = 'YOUR_API_KEY_HERE'  # Replace with your actual API key

# Initialize API instance for vSphere connector operations
api_instance_vsphere = deepsecurity.VmwareVsphereConnectorsApi(deepsecurity.ApiClient(configuration))

# Set the connector ID and new password
connector_id_vsphere = 1  # The unique ID of the vSphere connector. Retrieve using list_vmware_vsphere_connectors().
api_version = 'v1'  # API version to use

# Define the new password for the vSphere connector account
vsphere_connector = deepsecurity.VmwareVsphereConnector(password="NEW_PASSWORD_HERE")  # Replace with the new password

try:
    # Update the vSphere connector password
    api_response_vsphere = api_instance_vsphere.modify_vmware_vsphere_connector(connector_id_vsphere, vsphere_connector, api_version)
    print(api_response_vsphere)  # Print the response to verify success
except ApiException as e:
    # Catch and print any API errors
    print("An exception occurred when calling VmwareVsphereConnectorsApi.modify_vmware_vsphere_connector: %s\n" % e)
