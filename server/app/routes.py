from flask import Blueprint, request, jsonify, session

main = Blueprint('main', __name__)

# Simple in-memory user store
users = {}

@main.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    if not username or not password:
        return jsonify({'error': 'Username and password required'}), 400
    if username in users:
        return jsonify({'error': 'User already exists'}), 409
    users[username] = password
    return jsonify({'message': 'User created successfully'}), 201

@main.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    if users.get(username) == password:
        session['user'] = username
        return jsonify({'message': 'Login successful'}), 200
    return jsonify({'error': 'Invalid credentials'}), 401

@main.route('/', methods=['GET'])
def index():
    return jsonify({'message': 'Server is running'}), 200