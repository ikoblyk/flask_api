import os
from flask import Flask
from flask import jsonify
from api.utils.database import db
from api.utils.responses import response_with
import api.utils.responses as resp
from api.routes.authors import author_routes
import api.config.config as cnf
import logging
from api.routes.books import book_routes
from api.routes.user import user_routes
from flask_jwt_extended import JWTManager
from api.utils.email import mail
from flask_migrate import Migrate
from flask import send_from_directory
from flask_swagger import swagger
from flask_swagger_ui import get_swaggerui_blueprint





app = Flask(__name__)
SWAGGER_URL = '/api/docs'


if os.environ.get('WORK_ENV') == 'PROD':
    app_config = cnf.ProductionConfig
elif os.environ.get('WORK_ENV') == 'TEST':
    app_config = cnf.TestingConfig
else:
    app_config = cnf.DevelopmentConfig
app.config.from_object(app_config)


@app.after_request
def add_header(response):
    return response
@app.errorhandler(400)
def bad_request(e):
    logging.error(e)
    return response_with(resp.BAD_REQUEST_400)

@app.errorhandler(500)
def server_error(e):
    logging.error(e)
    return response_with(resp.SERVER_ERROR_500)
@app.errorhandler(404)
def not_found(e):
    logging.error(e)
    return response_with(resp. SERVER_ERROR_404)


@app.route("/api/spec")
def spec():
    swag = swagger(app, prefix='/api')
    swag['info']['base'] = "http://localhost:5000"
    swag['info']['version'] = "1.0"
    swag['info']['title'] = "Sample API DB"
    return jsonify(swag)

jwt = JWTManager(app)

db.init_app(app)
mail.init_app(app)

with app.app_context():
    db.create_all()


migrate = Migrate(app, db)

swaggerui_blueprint = get_swaggerui_blueprint(SWAGGER_URL, '/api/spec', config={'app_name': "Sample API DB"})

app.register_blueprint(author_routes, url_prefix='/authors')
app.register_blueprint(book_routes, url_prefix='/api/books')
app.register_blueprint(user_routes, url_prefix='/api/users')
app.register_blueprint(swaggerui_blueprint,url_prefix=SWAGGER_URL)

@app.route('/avatar/<filename>', methods=['GET'])
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],filename)

if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0", use_reloader=False)
