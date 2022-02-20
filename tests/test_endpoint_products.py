import json
from tests import utils
from application import create_app

# =============================================================
# functionality tests
# =============================================================

environment = "development"
app = create_app(environment)
client = app.test_client()

headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}

token = ""
product_id = None


def test_token():
    global token
    url = '/security/get-token'
    data = {
        "username": "sucarrilloa@gmail.com",
        "password": "Zdemo2022$"
    }
    response = client.post(url, data=json.dumps(data), headers=headers)
    response_json = response.json
    token = response_json.get("jwt", "")

    assert response.status_code == 200
    assert response.json


def test_post_product():
    global product_id
    url = '/products'
    string_auth = 'Bearer {}'.format(token)
    headers['Authorization'] = string_auth

    sku = utils.random_lower_string()

    data = {
        "sku": sku,
        "name": "Computadora Asus",
        "brand": "TEST",
        "description": "Laptop Asus i5, 4g RAM 500GB SSD",
        "price": 6790.00,
        "qty": 10,
        "is_active": True
    }

    response = client.post(url, data=json.dumps(data), headers=headers)
    product_id = response.json.get("id")
    assert response.status_code == 200


def test_get_products():
    url = '/products'
    string_auth = 'Bearer {}'.format(token)
    headers['Authorization'] = string_auth
    response = client.get(url, headers=headers)
    assert response.status_code == 200


def test_get_product():
    url = f'/products/{product_id}'
    string_auth = 'Bearer {}'.format(token)
    headers['Authorization'] = string_auth
    response = client.get(url, headers=headers)
    assert response.status_code == 200


def test_get_total_searched():
    url = f'/products/{product_id}/total-searcheds'
    string_auth = 'Bearer {}'.format(token)
    headers['Authorization'] = string_auth
    response = client.get(url, headers=headers)
    assert response.status_code == 200