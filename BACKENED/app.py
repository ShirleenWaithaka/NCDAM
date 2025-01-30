from flask import Flask,jsonify,request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_cors import CORS


app=Flask(__name__)

DB_CONFIG={
    "dbname":"postgres",
    "user": "postgres.bmkjhzotrhchferoexsh",
    "password":"TsHtijPlPGN04e6t",
    "host":"aws-0-eu-central-1.pooler.supabase.com",
    "port":5432
}

app.config['SQLALCHEMY_DATABASE_URI']=f"postgresql://{DB_CONFIG['user']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['dbname']}"

CORS(app)

db=SQLAlchemy(app)

migrate=Migrate(app,db) #initialize migragtions

ma=Marshmallow(app)

# class User(db.Model):
#     __tablename__='user'

#     id=db.Column(db.Integer,primary_key=True,autoincrement=True)
#     name =db.Column(db.String(100),nullable=False)
#     phonenumber=db.Column(db.Integer,nullable=False)
#     email=db.Column(db.String(250),nullable=False,unique=True)
#     role=db.Column(db.String(50),nullable=False,unique=True)
#     password_hash=db.Column(db.Text, nullable=False)
#     created_at=db.Column(db.DateTime, nullable=False, server_default=db. func.now())
#     updated_at=db.Column(db.DateTime, nullable=False, server_default=db.func.now(), onupdate=db.func.now())

# def single_user(self):
#             return {"id":self.id,"name":self.name,"age":self.age,"email":self.email, "role":self.role}

# member= db.relationship("Member", back_populates="user", uselist=False)  # One-to-one relationship
# admin= db.relationship("Admin", back_populates="user", uselist=False)  # One-to-one relationship

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    phonenumber = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(250), nullable=False, unique=True)
    role = db.Column(db.String(50), nullable=False)
    password_hash = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, nullable=False, server_default=db.func.now(), onupdate=db.func.now())

    admin = db.relationship("Admin", back_populates="user", uselist=False)
    member = db.relationship("Member", back_populates="user", uselist=False)

def single_user(self):
    return {"id": self.id, "name": self.name, "phonenumber": self.phonenumber, "email": self.email, "role": self.role}

   

# class Admin(db.Model):
#     __tablename__='pastor'

#     id=db.Column(db.Integer,primary_key=True,autoincrement=True)
#     user_id=db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False,unique=True)
#     name =db.Column(db.String(100),nullable=False)
#     phonenumber=db.Column(db.Integer,nullable=False)
#     email=db.Column(db.String(250),nullable=False,unique=True)
#     role=db.Column(db.String(50),nullable=False,unique=True)
   
    
#     Member=db.relationship('Member',back_populates='user')
    
#     def single_admin(self):
#             return {"id":self.id,"name":self.name,"age":self.age,"email":self.email}

class Admin(db.Model):
    __tablename__ = 'pastor'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False, unique=True)
    name = db.Column(db.String(100), nullable=False)
    phonenumber = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(250), nullable=False, unique=True)
    role = db.Column(db.String(50), nullable=False)

    user = db.relationship('User', back_populates='admin')  # Corrected relationship
    members = db.relationship('Member', back_populates='admin')  # Fix to handle one-to-many

# class Member(db.Model):
#     __tablename__="member"
#     id=db.Column(db.Integer,primary_key=True,autoincrement=True)
#     user_id=db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False,unique=True)
#     name =db.Column(db.String(100),nullable=False)
#     phonenumber=db.Column(db.Integer,nullable=False)
#     email=db.Column(db.String(250),nullable=False,unique=True)
#     role=db.Column(db.String(50),nullable=False,unique=True)
#     residence=db.Column(db.String(100),nullable=False,unique=True)
#     Admin_id=db.Column(db.Integer,db.ForeignKey('pastor.id',ondelete="CASCADE"),nullable=False)
    

#     Admin=db.relationship("Admin",back_populates="user")

#     def single_member(self):
#             return {"id":self.id,"name":self.name,"age":self.age,"email":self.email}   

class Member(db.Model):
    __tablename__ = "member"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False, unique=True)
    name = db.Column(db.String(100), nullable=False)
    phonenumber = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(250), nullable=False, unique=True)
    role = db.Column(db.String(50), nullable=False)
    residence = db.Column(db.String(100), nullable=False, unique=True)
    admin_id = db.Column(db.Integer, db.ForeignKey('pastor.id', ondelete="CASCADE"), nullable=False)

    user = db.relationship("User", back_populates="member")  # Corrected relationship
    admin = db.relationship("Admin", back_populates="members")

    
