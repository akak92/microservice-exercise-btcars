from flask import Flask

def create_app():
    app = Flask(__name__)
    from api.controllers.BTCars import btcars_bp
    app.register_blueprint(btcars_bp)
    return app