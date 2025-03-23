from flask import Blueprint, jsonify

main_routes = Blueprint('main_routes', __name__)

# Example route
@main_routes.route('/api/test', methods=['GET'])
def test_api():
    return jsonify({'message': 'API is working!'})

# Sample menu route
@main_routes.route('/api/menu', methods=['GET'])
def get_menu():
    return jsonify({'menu': ['Pizza', 'Burger', 'Pasta']})  # Replace with DB data later
