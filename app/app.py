from flask import Flask
from flask_elasticsearch import FlaskElasticsearch

def create_app():
    app = Flask(__name__)
    app.config.setdefault('ELASTICSEARCH_HOST', 'elasticsearch:9200')
    return app

def setup_elasticsearch(app):
    es = FlaskElasticsearch()
    es.init_app(app)
    return es

application = create_app()
elasticsearch = setup_elasticsearch(application)
