from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from backend.repositories.product_catalog.product_repository import ProductRepository

delete_product_controller = Blueprint('delete_product_controller', __name__)
product_repository = ProductRepository()

@delete_product_controller.route('/delete_product/<int:product_id>', methods=['DELETE'])
@login_required
def delete_product(product_id):
    # Ensure user is an admin
    if not current_user.is_admin:
        return jsonify({"error": "Only admins can delete products"}), 403

    data = request.get_json()
    confirmation = data.get('confirmation')
    if confirmation != "yes":
        return jsonify({"error": "Deletion requires confirmation"}), 400

    product = product_repository.get_product_by_id(product_id)
    if not product:
        return jsonify({"error": "Product not found"}), 404

    product_repository.delete_product(product)
    return jsonify({"message": "Product deleted successfully"}), 200