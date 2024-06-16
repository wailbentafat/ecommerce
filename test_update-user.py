import requests

# URL for updating user info
url_put = 'http://127.0.0.1:8000/api/userinfo/update'

# Headers with the JWT token
headers = {
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE5OTMxNjQ4LCJpYXQiOjE3MTg0NjI4NDgsImp0aSI6IjRiNTFmMmEzZjJiODRmZDBhYjBkMWM2MjU5MjUzZWY1IiwidXNlcl9pZCI6M30.-yUPJNWj4skNJ3c2YhCSqa1fHpjfmXlmAXOvStm42_0'
}

# Data for updating user info
data = {
    'first_name': 'UpdatedFirstName',
    'last_name': 'UpdatedLastName',
    'email': 'updatedemail@example.com',
    'password': 'newpassword'  # Empty string '' if you don't want to change the password
}

# PUT request to update user info
response_put = requests.put(url_put, json=data, headers=headers)
print("PUT request:")
print("Status code:", response_put.status_code)
try:
    print("Response JSON:", response_put.json())
except requests.exceptions.JSONDecodeError:
    print("Response text:", response_put.text)
