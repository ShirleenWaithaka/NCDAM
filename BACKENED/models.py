from config import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class Admin(db.Model):
    __tablename__ = 'admin'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False, unique=True)
    name = db.Column(db.String(100), nullable=False)
    phonenumber = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(250), nullable=False, unique=True)
    role = db.Column(db.String(50), nullable=False)

    user = db.relationship('User', back_populates='admin')  # Corrected relationship
    members = relationship('Member', back_populates='admin')  # Fix to handle one-to-many


class Member(db.Model):
    __tablename__ = 'member'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False, unique=True)
    name = db.Column(db.String(50), nullable=False)
    phonenumber = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(250), nullable=False, unique=True)
    role = db.Column(db.String(50), nullable=False)
    residence = db.Column(db.String(100), nullable=False, unique=True)
    admin_id = db.Column(db.Integer, db.ForeignKey('admin.id', ondelete="CASCADE"), nullable=False)

    user = db.relationship('User', back_populates= 'member')  # Corrected relationship
    admin = db.relationship('Admin', back_populates= 'members')


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

    admin = relationship('Admin', back_populates='user', uselist=False)
    member = db.relationship('Member', back_populates='user', uselist=False)

def single_user(self):
    return {"id": self.id, "name": self.name, "phonenumber": self.phonenumber, "email": self.email, "role": self.role}    