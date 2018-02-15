from flask import Blueprint
from flask_restplus import Api

from app.apis.routes.products import api as products

blueprint = Blueprint('api', __name__, url_prefix='/api/v1')
api = Api(blueprint,
    title='Product Catalog API',
    version='1.0',
    description='Product Catalog API'
)
api.add_namespace(products)
