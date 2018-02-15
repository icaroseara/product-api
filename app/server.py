from healthcheck import HealthCheck
from app.api_v1 import blueprint as apiv1
from app.app import application, elasticsearch

def elasticsearch_available():
    elasticsearch.info()
    return True, "elasticsearch ok"

def setup_api():
    application.register_blueprint(apiv1)
    health = health_check(application)
    health.add_check(elasticsearch_available)
    return application

def health_check(app):
    return HealthCheck(app, "/api/healthcheck")

if __name__ == "__main__":
    api = setup_api()
    api.run(host='0.0.0.0', port=5000)
