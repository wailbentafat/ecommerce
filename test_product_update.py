import requests

# URL for updating a product with a specific ID (replace 'your_product_id' with an actual product ID)
product_id = '4'
url_put = f'http://127.0.0.1:8000/api/products/update/{product_id}'

# Headers with the JWT token
headers = {
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE5OTMxNjQ4LCJpYXQiOjE3MTg0NjI4NDgsImp0aSI6IjRiNTFmMmEzZjJiODRmZDBhYjBkMWM2MjU5MjUzZWY1IiwidXNlcl9pZCI6M30.-yUPJNWj4skNJ3c2YhCSqa1fHpjfmXlmAXOvStm42_0'
}

# Data for updating the product
data = {
    'name': 'New Product',
    'description': 'This is a new product.',
    'price': 99.99,
    'brand': 'New Brand',
    'stock': 9,
    'categorie': 'Computer',
    'rate': 4.5
}


# PUT request to update the product
response_put = requests.put(url_put, json=data, headers=headers)
print("PUT request:")
print("Status code:", response_put.status_code)
try:
    print("Response JSON:", response_put.json())
except requests.exceptions.JSONDecodeError:
    print("Response text:", response_put.text)
