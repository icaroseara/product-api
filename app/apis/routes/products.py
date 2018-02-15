from datetime import datetime

from flask import jsonify
from flask_restplus import Api, Resource, Api

from app.app import application, elasticsearch

api = Api()

PRODUCTS = [{
    "sku": "BATMAN-123",
    "price": "122.99",
    "name": "Batmobile",
    "brand": "Marvel",
    "type": "accessories",
    "categories": ["Super Heroes", "Flying Cars", "Cars"],
    "product_image_url": "http://static.dafiti.com.br/9527534/1-zoom.jpg",
}]

class ProductList(Resource):
    def post(self):
        product = PRODUCTS[0]
        product['created_at'] = datetime.now().isoformat()
        elasticsearch.index(index='api', doc_type='products', id=product.get("sku"), body=product)
        given_product = elasticsearch.get(index='api', doc_type='products', id=product.get("sku"))
        return jsonify(given_product.get("_source"))

class Product(Resource):
    def get(self, sku):
        given_product = elasticsearch.get(index='api', doc_type='products', id=product.get("sku"))
        return jsonify(given_product)

api.add_resource(ProductList, '/products')
api.add_resource(Product, '/products/<sku>')
