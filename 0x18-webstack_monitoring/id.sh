# Replace YOUR_API_KEY and YOUR_APP_KEY with your actual Datadog API key and Application key
export DD_API_KEY=f71b19c8dc3d57800cc4937b58f4d836
export DD_APP_KEY=633f35c08697dfce945ca4c167eb070acf3928dc

# Replace YOUR_ORG_NAME with your actual Datadog organization name
export DD_ORG_NAME="Alx"

# List all dashboards
curl -X GET "https://api.datadoghq.com/api/v1/dashboard/lists/manual/${DD_ORG_NAME}?api_key=${DD_API_KEY}&application_key=${DD_APP_KEY}"
