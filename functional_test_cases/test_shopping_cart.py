import pytest
import requests

BASE_URL = "http://localhost:8000"

# Test Cases for Add Item to Cart

def test_add_item_to_cart_success():
    data = {
        "product_id": 1,
        "quantity": 2
    }
    response = requests.post(f"{BASE_URL}/cart", json=data)
    assert response.status_code == 201
    assert response.json()["message"] == "Item added to cart"

def test_add_item_to_cart_invalid_data():
    data = {
        "product_id": "invalid",
        "quantity": 2
    }
    response = requests.post(f"{BASE_URL}/cart", json=data)
    assert response.status_code == 400
    assert "Invalid data" in response.json()["error"]

# Test Cases for Get All Items in Cart

def test_get_all_items_in_cart_success():
    params = {
        "user_id": 1
    }
    response = requests.get(f"{BASE_URL}/cart", params=params)
    assert response.status_code == 200
    assert "items" in response.json()

def test_get_all_items_in_cart_empty():
    params = {
        "user_id": 999
    }
    response = requests.get(f"{BASE_URL}/cart", params=params)
    assert response.status_code == 404
    assert "Cart empty" in response.json()["error"]

# Test Cases for Update Item in Cart

def test_update_item_in_cart_success():
    data = {
        "item_id": 1,
        "quantity": 3
    }
    response = requests.put(f"{BASE_URL}/cart", json=data)
    assert response.status_code == 200
    assert response.json()["message"] == "Item updated"

def test_update_item_in_cart_invalid_data():
    data = {
        "item_id": 1,
        "quantity": "invalid"
    }
    response = requests.put(f"{BASE_URL}/cart", json=data)
    assert response.status_code == 400
    assert "Invalid data" in response.json()["error"]

# Test Cases for Remove Item from Cart

def test_remove_item_from_cart_success():
    url = f"{BASE_URL}/cart?item_id=1"
    response = requests.delete(url)
    assert response.status_code == 200
    assert response.json()["message"] == "Item removed"

def test_remove_item_from_cart_not_found():
    url = f"{BASE_URL}/cart?item_id=999"
    response = requests.delete(url)
    assert response.status_code == 404
    assert "Item not found" in response.json()["error"]