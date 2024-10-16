import json
import requests

# Constants for Splunk API
SPLUNK_URL = "https://your-splunk-instance:8089"
API_TOKEN = "your_splunk_api_token"

# Function to deploy JSON configuration to Splunk
def deploy_to_splunk(endpoint, filename):
    url = f"{SPLUNK_URL}{endpoint}"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}",
        "Content-Type": "application/json",
    }

    with open(filename, 'r') as f:
        data = json.load(f)

    response = requests.post(url, headers=headers, json=data, verify=False)

    if response.status_code == 201:
        print(f"Successfully deployed {filename} to {endpoint}")
    else:
        print(f"Failed to deploy {filename}. Status Code: {response.status_code}")
        print(f"Response: {response.text}")

# Deploy the dashboard and alert
deploy_to_splunk("/servicesNS/admin/search/data/ui/views", "dashboard.json")
deploy_to_splunk("/servicesNS/admin/search/saved/searches", "alert_config.json")
