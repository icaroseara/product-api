from datetime import datetime
from flask import Flask, jsonify
from flask_elasticsearch import FlaskElasticsearch

es = FlaskElasticsearch()

app = Flask(__name__)
app.config.setdefault('ELASTICSEARCH_HOST', 'elasticsearch:9200')
es.init_app(app)

@app.route("/")
def health_check():
    return jsonify(es.cluster.health())

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
