from flask import Flask, Blueprint, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from models import Admin, Member, User, db
from datetime import datetime
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt_identity
)
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.exc import IntegrityError

app_blueprint = Blueprint('app', __name__)



# Helper function to serialize Admin objects
def serialize_admin(admin):
    return {
        "id": admin.id,
        "user_id": admin.user_id,
        "name": admin.name,
        "phonenumber": admin.phonenumber,
        "email": admin.email,
        "role": admin.role
    }

# Route to get all admins
@app_blueprint.route('/admins', methods=['GET'])
@jwt_required()  # Protect this route with JWT
def get_admins():
    admins = Admin.query.all()
    return jsonify([serialize_admin(admin) for admin in admins])

# Route to get a single admin by ID
@app_blueprint.route('/admins/<int:admin_id>', methods=['GET'])
@jwt_required()  # Protect this route with JWT
def get_admin(admin_id):
    admin = Admin.query.get_or_404(admin_id)
    return jsonify(serialize_admin(admin))

# Route to create a new admin
@app_blueprint.route('/admins', methods=['POST'])
@jwt_required()  # Protect this route with JWT
def create_admin():
    data = request.get_json()
    new_admin = Admin(
        user_id=data['user_id'],
        name=data['name'],
        phonenumber=data['phonenumber'],
        email=data['email'],
        role=data['role']
    )
    db.session.add(new_admin)
    db.session.commit()
    return jsonify(serialize_admin(new_admin)), 201

# Route to update an admin by ID
@app_blueprint.route('/admins/<int:admin_id>', methods=['PUT'])
@jwt_required()  # Protect this route with JWT
def update_admin(admin_id):
    admin = Admin.query.get_or_404(admin_id)
    data = request.get_json()
    admin.user_id = data.get('user_id', admin.user_id)
    admin.name = data.get('name', admin.name)
    admin.phonenumber = data.get('phonenumber', admin.phonenumber)
    admin.email = data.get('email', admin.email)
    admin.role = data.get('role', admin.role)
    db.session.commit()
    return jsonify(serialize_admin(admin))

# Route to delete an admin by ID
@app_blueprint.route('/admins/<int:admin_id>', methods=['DELETE'])
@jwt_required()  # Protect this route with JWT
def delete_admin(admin_id):
    admin = Admin.query.get_or_404(admin_id)
    db.session.delete(admin)
    db.session.commit()
    return jsonify({"message": "Admin deleted successfully"}), 200

# Helper function to serialize Member objects
def serialize_member(member):
    return {
        "id": member.id,
        "user_id": member.user_id,
        "name": member.name,
        "phonenumber": member.phonenumber,
        "email": member.email,
        "role": member.role,
        "residence": member.residence,
        "admin_id": member.admin_id
    }

# Route to get all members
@app_blueprint.route('/members', methods=['GET'])
@jwt_required()  # Protect this route with JWT
def get_members():
    members = Member.query.all()
    return jsonify([serialize_member(member) for member in members])

# Route to get a single member by ID
@app_blueprint.route('/members/<int:member_id>', methods=['GET'])
@jwt_required()  # Protect this route with JWT
def get_member(member_id):
    member = Member.query.get_or_404(member_id)
    return jsonify(serialize_member(member))

# Route to create a new member
@app_blueprint.route('/members', methods=['POST'])
@jwt_required()  # Protect this route with JWT
def create_member():
    data = request.get_json()
    new_member = Member(
        user_id=data['user_id'],
        name=data['name'],
        phonenumber=data['phonenumber'],
        email=data['email'],
        role=data['role'],
        residence=data['residence'],
        admin_id=data['admin_id']
    )
    db.session.add(new_member)
    db.session.commit()
    return jsonify(serialize_member(new_member)), 201

# Route to update a member by ID
@app_blueprint.route('/members/<int:member_id>', methods=['PUT'])
@jwt_required()  # Protect this route with JWT
def update_member(member_id):
    member = Member.query.get_or_404(member_id)
    data = request.get_json()
    member.user_id = data.get('user_id', member.user_id)
    member.name = data.get('name', member.name)
    member.phonenumber = data.get('phonenumber', member.phonenumber)
    member.email = data.get('email', member.email)
    member.role = data.get('role', member.role)
    member.residence = data.get('residence', member.residence)
    member.admin_id = data.get('admin_id', member.admin_id)
    db.session.commit()
    return jsonify(serialize_member(member))

# Route to delete a member by ID
@app_blueprint.route('/members/<int:member_id>', methods=['DELETE'])
@jwt_required()  # Protect this route with JWT
def delete_member(member_id):
    member = Member.query.get_or_404(member_id)
    db.session.delete(member)
    db.session.commit()
    return jsonify({"message": "Member deleted successfully"}), 200

# Helper function to serialize User objects
def serialize_user(user):
    return {
        "id": user.id,
        "name": user.name,
        "phonenumber": user.phonenumber,
        "email": user.email,
        "role": user.role,
        "created_at": user.created_at.isoformat(),
        "updated_at": user.updated_at.isoformat()
    }

# Route to get all users
@app_blueprint.route('/users', methods=['GET'])
@jwt_required()  # Protect this route with JWT
def get_users():
    users = User.query.all()
    return jsonify([serialize_user(user) for user in users])

# Route to get a single user by ID
@app_blueprint.route('/users/<int:user_id>', methods=['GET'])
@jwt_required()  # Protect this route with JWT
def get_user(user_id):
    user = User.query.get_or_404(user_id)
    return jsonify(serialize_user(user))

# Route to create a new user
@app_blueprint.route('/users', methods=['POST'])
# def create_user():
#     data = request.get_json()

#     # Check if 'password' key exists in the payload
#     if 'password' not in data:
#         return jsonify({"message": "Password is required"}), 400

#     # Hash the password
#     hashed_password = generate_password_hash(data['password'])

#     # Create the new user
#     new_user = User(
#         name=data.get('name'),
#         phonenumber=data.get('phonenumber'),
#         email=data.get('email'),
#         role=data.get('role'),
#         password_hash=hashed_password  # Store the hashed password
#     )
#     db.session.add(new_user)
#     db.session.commit()
#     return jsonify(serialize_user(new_user)), 201

def create_user():
    try:
        data = request.get_json()
        new_user = User(
            name=data.get('name'),
            phonenumber=data.get('phonenumber'),
            email=data.get('email'),
            role=data.get('role'),
            password_hash=data.get('password_hash')
        )
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message": "User created successfully"}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Email already exists"}), 400

# @app_blueprint.route('/users', methods=['POST'])
# def create_user():
#     data = request.get_json()
#     hashed_password = generate_password_hash(data['password'], method='sha256')
#     new_user = User(
#         name=data['name'],
#         phonenumber=data['phonenumber'],
#         email=data['email'],
#         role=data['role'],
#         password_hash=hashed_password  # Store the hashed password
#     )
#     db.session.add(new_user)
#     db.session.commit()
#     return jsonify(serialize_user(new_user)), 201

# Route to update a user by ID
@app_blueprint.route('/users/<int:user_id>', methods=['PUT'])
@jwt_required()  # Protect this route with JWT
def update_user(user_id):
    user = User.query.get_or_404(user_id)
    data = request.get_json()
    user.name = data.get('name', user.name)
    user.phonenumber = data.get('phonenumber', user.phonenumber)
    user.email = data.get('email', user.email)
    user.role = data.get('role', user.role)
    if 'password' in data:
        user.password_hash = generate_password_hash(data['password'], method='sha256')
    db.session.commit()
    return jsonify(serialize_user(user))

# Route to delete a user by ID
@app_blueprint.route('/users/<int:user_id>', methods=['DELETE'])
@jwt_required()  # Protect this route with JWT
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "User deleted successfully"}), 200

# Login route
@app_blueprint.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    user = User.query.filter_by(email=email).first()

    if user and check_password_hash(user.password_hash, password):
        access_token = create_access_token(identity=user.id)
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"message": "Invalid email or password"}), 401



