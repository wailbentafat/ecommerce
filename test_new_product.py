import requests

# Define the URL and JWT token
url = 'http://127.0.0.1:8000/api/products/add/'
jwt_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE5OTMxNjQ4LCJpYXQiOjE3MTg0NjI4NDgsImp0aSI6IjRiNTFmMmEzZjJiODRmZDBhYjBkMWM2MjU5MjUzZWY1IiwidXNlcl9pZCI6M30.-yUPJNWj4skNJ3c2YhCSqa1fHpjfmXlmAXOvStm42_0'

# Data for creating a new product
data = {
    'name': 'New Product',
    'description': 'This is a new product.',
    'price': 99.99,
    'brand': 'New Brand',
    'stock': 10,
    'categorie': 'Computer',
    'rate': 4.5
}

# Headers with JWT token
headers = {
    'Authorization': f'Bearer {jwt_token}'
}
try:
    response = requests.post(url, json=data, headers=headers)
    print("Status code:", response.status_code)
    print("Response content:", response.content)

    if response.status_code == 200:
        print("Response JSON:", response.json())

except Exception as e:
    print("An error occurred:", e)