import requests

url = 'http://127.0.0.1:8000/api/userinfo/'
headers = {
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE5OTMxNjQ4LCJpYXQiOjE3MTg0NjI4NDgsImp0aSI6IjRiNTFmMmEzZjJiODRmZDBhYjBkMWM2MjU5MjUzZWY1IiwidXNlcl9pZCI6M30.-yUPJNWj4skNJ3c2YhCSqa1fHpjfmXlmAXOvStm42_0'
}

response = requests.get(url, headers=headers)
print(response.status_code)
print(response.json())
