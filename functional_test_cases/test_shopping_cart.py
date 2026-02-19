import pytest
from backend.controllers.cart_controller import cart_bp
from flask import Flask, session
from backend.services.cart_service import CartService

app = Flask(__name__)
app.register_blueprint(cart_bp)
app.config['TESTING'] = True

# Fixtures to set up app context
test_client = app.test_client()  # Create a test client for the Flask app

@pytest.fixture(scope='module')
def client():
    return test_client

# Test cases for shopping cart functionality
def test_add_single_product_to_cart(client, mocker):
    mocker.patch.object(CartService, 'add_to_cart', return_value={'status': 'success'})
    with client.session_transaction() as sess:
        sess['user_id'] = 1
    response = client.post('/add', json={'product_id': 1, 'quantity': 1})
    assert response.status_code == 201
    assert response.json['message'] == 'Product added to cart successfully'

def test_remove_product_from_cart(client, mocker):
    mocker.patch.object(CartService, 'remove_from_cart', return_value={'status': 'success'})
    with client.session_transaction() as sess:
        sess['user_id'] = 1
    response = client.post('/delete', json={'product_id': 1})
    assert response.status_code == 200
    assert response.json['message'] == 'Product removed from cart successfully'

def test_update_product_quantity(client, mocker):
    mocker.patch.object(CartService, 'update_quantity', return_value={'status': 'success'})
    with client.session_transaction() as sess:
        sess['user_id'] = 1
    response = client.post('/update_quantity', json={'product_id': 1, 'quantity': 2})
    assert response.status_code == 200
    assert response.json['message'] == 'Product quantity updated successfully'

def test_save_cart(client, mocker):
    mocker.patch.object(CartService, 'save_cart', return_value={'status': 'success'})
    with client.session_transaction() as sess:
        sess['user_id'] = 1
    response = client.post('/save')
    assert response.status_code == 200
    assert response.json['message'] == 'Cart saved successfully'

def test_load_cart(client, mocker):
    mocker.patch.object(CartService, 'load_cart', return_value={'status': 'success', 'cart_items': []})
    with client.session_transaction() as sess:
        sess['user_id'] = 1
    response = client.get('/load')
    assert response.status_code == 200
    assert 'cart_items' in response.json
