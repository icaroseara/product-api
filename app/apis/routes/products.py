from datetime import datetime

from flask import jsonify, request
from flask_restplus import Api, Resource, Api

from app.app import application, elasticsearch
from app.utils import INDEX_PATTERN, PRODUCT_DOCTYPE, query_builder

api = Api()

class ProductList(Resource):
    def post(self):
        product = request.get_json()
        product['created_at'] = datetime.now().isoformat()
        elasticsearch.index(
            index=INDEX_PATTERN,
            doc_type=PRODUCT_DOCTYPE,
            id=product.get("sku"),
            body=product
        )
        return jsonify(product)

class ProductSearch(Resource):
    def get(self):
        query = query_builder(request.args.get('q'))
        products = elasticsearch.search(
            index=INDEX_PATTERN,
            doc_type=PRODUCT_DOCTYPE,
            body=query
        )
        return jsonify(products)

api.add_resource(ProductList, '/products')
api.add_resource(ProductSearch, '/products/search')
