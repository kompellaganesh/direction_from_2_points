from flask import Flask
from config.config import  configurations
from flasgger import Swagger
from routes.Route_handler import route
 
app = Flask(__name__)
app.add_url_rule(configurations['server']['apipath']+"/api/v1/route","route",route,methods=['POST'])  
swagger_config = {
    "headers": [
    ],
    "specs": [
        {
            "endpoint": 'apispec_1',
            "route": '/apispec_1.json',
            "rule_filter": lambda rule: True, 
            "model_filter": lambda tag: True, 
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/api/v1/swagger",
    "url_prefix": configurations['server']['apipath']
}
app.config['SWAGGER'] = {
    'openapi': '3.0.2',
    'title':"Videos Service"
}
swagger = Swagger(app, config=swagger_config)
