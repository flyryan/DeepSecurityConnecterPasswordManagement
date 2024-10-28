from __future__ import print_function
import deepsecurity
from deepsecurity.rest import ApiException

# Setup: Initialize the connection to your Deep Security Manager instance
configuration = deepsecurity.Configuration()
configuration.host = 'https://192.168.1.200:443/api'  # Replace with your Deep Security Manager URL

# Authentication: Insert your API key for authentication
configuration.api_key['api-secret-key'] = 'YOUR_API_KEY_HERE'  
# Replace with your actual API key

# Initialize API instances for each connector type
ldap_sync_api_instance = deepsecurity.LdapSyncConnectorsApi(deepsecurity.ApiClient(configuration))
vsphere_api_instance = deepsecurity.VmwareVsphereConnectorsApi(deepsecurity.ApiClient(configuration))
nsx_api_instance = deepsecurity.NsxManagersApi(deepsecurity.ApiClient(configuration))

api_version = 'v1'  # API version to use

try:
    # Get list of AD Sync connectors
    print("AD Sync Connector IDs:")
    ad_sync_connectors = ldap_sync_api_instance.list_ldap_sync_connectors(api_version)
    for connector in ad_sync_connectors.ldap_sync_connectors:
        print(f"  ID: {connector.id}, Name: {connector.name}")
    
    print("\n")

    # Get list of vSphere connectors
    print("vSphere Connector IDs:")
    vsphere_connectors = vsphere_api_instance.list_vmware_vsphere_connectors(api_version)
    for connector in vsphere_connectors.vmware_vsphere_connectors:
        print(f"  ID: {connector.id}, Name: {connector.name}")
    
    print("\n")

    # Get list of NSX Manager connectors
    print("NSX Manager Connector IDs:")
    nsx_connectors = nsx_api_instance.list_nsx_managers(api_version)
    for nsx_manager in nsx_connectors.nsx_managers:
        print(f"  ID: {nsx_manager.id}, Name: {nsx_manager.name}")

except ApiException as e:
    print("An exception occurred: %s\n" % e)