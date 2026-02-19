import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_add_single_product_to_cart(client):
    response = client.post('/add', json={"product_id": 1, "quantity": 2})
    assert response.status_code == 201
    assert response.get_json() == {"message": "Product added to cart successfully"}


def test_add_multiple_products_to_cart(client):
    response = client.post('/add', json={"product_id": 1, "quantity": 2})
    assert response.status_code == 201
    assert response.get_json() == {"message": "Product added to cart successfully"}
    
    response = client.post('/add', json={"product_id": 2, "quantity": 1})
    assert response.status_code == 201
    assert response.get_json() == {"message": "Product added to cart successfully"}


def test_remove_product_from_cart(client):
    client.post('/add', json={"product_id": 1, "quantity": 2})
    response = client.post('/delete', json={"product_id": 1})
    assert response.status_code == 200
    assert response.get_json() == {"message": "Product removed from cart successfully"}


def test_clear_shopping_cart(client):
    client.post('/add', json={"product_id": 1, "quantity": 2})
    response = client.post('/clear')
    assert response.status_code == 200
    assert response.get_json() == {"message": "All products removed from cart successfully"}


def test_increase_product_quantity(client):
    client.post('/add', json={"product_id": 1, "quantity": 1})
    response = client.post('/update_quantity', json={"product_id": 1, "quantity": 3})
    assert response.status_code == 200
    assert response.get_json() == {"message": "Product quantity updated successfully"}


def test_decrease_product_quantity_to_zero(client):
    client.post('/add', json={"product_id": 1, "quantity": 2})
    response = client.post('/update_quantity', json={"product_id": 1, "quantity": 0})
    assert response.status_code == 400
    assert response.get_json() == {"message": "Quantity must be a positive integer"}


def test_save_cart_on_logout(client):
    client.post('/add', json={"product_id": 1, "quantity": 2})
    response = client.post('/save')
    assert response.status_code == 200
    assert response.get_json() == {"message": "Cart saved successfully"}


def test_load_cart_on_login(client):
    client.post('/add', json={"product_id": 1, "quantity": 2})
    client.post('/save')
    response = client.get('/load')
    assert response.status_code == 200
    cart_items = response.get_json()
    assert cart_items is not None
