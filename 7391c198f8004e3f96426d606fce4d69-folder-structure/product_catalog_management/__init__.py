from flask import Blueprint

product_blueprint = Blueprint('product', __name__)
category_blueprint = Blueprint('category', __name__)

from . import routes, models