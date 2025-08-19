import requests

# Make a GET request to the API
url = "https://api.example.com/users"
response = requests.get(url)

# Process the response
if response.status_code == 200:
    data = response.json()
    # Do something with the data
    print(data)
else:
    print("Error:", response.status_code)

# ... existing code ...
import requests

data = {
    "name": "John Doe",
    "email": "johndoe@example.com"
}

# Make a POST request to the API
url = "https://api.example.com/users"
response = requests.post(url, json=data)

# Process the response
if response.status_code == 201:
    data = response.json()
    # Do something with the data
    print(data)
else:
    print("Error:", response.status_code)

# ... existing code ...
import requests

# Access token
access_token = "YOUR_ACCESS_TOKEN"

# Make a request to the authenticated API
url = "https://api.example.com/protected"
headers = {"Authorization": f"Bearer {access_token}"}
response = requests.get(url, headers=headers)

# Process the response
if response.status_code == 200:
    data = response.json()
    # Do something with the data
    print(data)
else:
    print("Error:", response.status_code) 