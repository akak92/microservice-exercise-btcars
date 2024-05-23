from flask import Blueprint

btcars_bp = Blueprint('btcars', __name__)

@btcars_bp.route('/', methods=['GET'])
def home():
    return "Hello!"