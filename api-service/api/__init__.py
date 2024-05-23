from flask import Flask
from flask_mongoengine import MongoEngine
import os
#   Pedro Díaz | 23-05-2024
#   create_app
#       Función que retorna el objeto app (Flask)
#       Es utilizado en run.py para dar inicio a la REST API
#       
#       Se realizan todas las definiciones necesarias para satisfacer el ejercicio.
#

db = MongoEngine()

def create_app():
    app = Flask(__name__)
    mongo_uri = os.getenv('MONGO_URI')
    
    app.config['MONGODB_SETTINGS'] = {
        'host' : mongo_uri
    }
    from api.models import BTCars
    db.init_app(app)

    from api.controllers.BTCars import btcars_bp
    app.register_blueprint(btcars_bp)
    return app