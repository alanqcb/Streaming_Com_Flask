from flask import Flask
# from flask_formulario.blueprints.public import simple_page
# from flask_formulario.blueprints.admin import admin_page
from streaming_service.modules.streaming_mod import streaming_mod
from streaming_service.modules.home_mod import home_mod



app = Flask(__name__)

app.register_blueprint(blueprint=streaming_mod,url_prefix="/streaming_mod", template_folder="templates")

app.register_blueprint(blueprint=home_mod,url_prefix="/", template_folder="templates")

# app.register_blueprint(blueprint=simple_page,url_prefix="/simple_page", template_folder="templates")

# app.register_blueprint(blueprint=admin_page,url_prefix="/admin_page", template_folder="templates")

a=1
