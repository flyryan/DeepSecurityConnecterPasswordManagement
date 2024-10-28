# Trend Micro Deep Security Connector Password Management Scripts

This repository contains four Python scripts for managing Trend Micro Deep Security connector passwords. These scripts allow you to:
- Retrieve a list of connector IDs (for AD Sync, vSphere, and NSX Manager) from Deep Security Manager.
- Change the password for each connector type.

> **Note:** These scripts are provided as examples and are untested. Please review and test them in a safe environment before applying them in production.

## Requirements

- **Python 3.x**
- **Deep Security Python SDK**: Install via pip:
  ```bash
  pip install deepsecurity
  ```

- **Trend Micro Deep Security Manager** with API access.

## Usage

Each script requires:
- Your Deep Security Manager’s API base URL (e.g., `https://your-dsm-url:443/api`)
- A valid Deep Security API key to authenticate API requests

### 1. Retrieve Connector IDs

**Script:** `get_connector_ids.py`

This script retrieves the connector IDs for AD Sync, vSphere, and NSX Manager connectors. Use it to gather the IDs needed for the password change scripts.

#### Example Output
The output will display connector IDs organized by type, like so:

```
AD Sync Connector IDs:
  ID: 1, Name: AD_Sync_Connector_1

vSphere Connector IDs:
  ID: 5, Name: vSphere_Connector_1

NSX Manager Connector IDs:
  ID: 8, Name: NSX_Manager_1
```

#### Usage
1. Update `YOUR_API_KEY_HERE` with your Deep Security API key.
2. Run the script:
   ```bash
   python get_connector_ids.py
   ```

### 2. Change AD Sync Connector Password

**Script:** `change_ad_sync_password.py`

This script updates the password for a specific AD Sync connector in Deep Security Manager.

#### Usage
1. Retrieve the connector ID using `get_connector_ids.py`.
2. Update `YOUR_API_KEY_HERE` with your API key and replace `connector_id_ldap` with the correct connector ID.
3. Set the new password in `NEW_PASSWORD_HERE`.
4. Run the script:
   ```bash
   python change_ad_sync_password.py
   ```

### 3. Change vSphere Connector Password

**Script:** `change_vsphere_password.py`

This script changes the password for a specific vSphere connector.

#### Usage
1. Retrieve the connector ID using `get_connector_ids.py`.
2. Update `YOUR_API_KEY_HERE` with your API key and replace `connector_id_vsphere` with the correct connector ID.
3. Set the new password in `NEW_PASSWORD_HERE`.
4. Run the script:
   ```bash
   python change_vsphere_password.py
   ```

### 4. Change NSX Manager Connector Password

**Script:** `change_nsx_manager_password.py`

This script changes the password for a specific NSX Manager connector.

#### Usage
1. Retrieve the connector ID using `get_connector_ids.py`.
2. Update `YOUR_API_KEY_HERE` with your API key and replace `nsx_manager_id` with the correct connector ID.
3. Set the new password in `NEW_PASSWORD_HERE`.
4. Run the script:
   ```bash
   python change_nsx_manager_password.py
   ```

## Important Notes

- **Untested Scripts**: These scripts are untested; validate them in a development environment before using them in production.
- **API Key Security**: Ensure your API key is kept secure and do not hard-code sensitive information in production scripts.

For more information on Trend Micro Deep Security API usage, refer to the official [Deep Security API documentation](https://automation.deepsecurity.trendmicro.com/20_0/api-reference/).