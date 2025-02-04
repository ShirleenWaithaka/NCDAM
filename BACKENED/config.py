from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from flask_jwt_extended import JWTManager



DB_CONFIG={
    "dbname":"postgres",
    "user": "postgres.bmkjhzotrhchferoexsh",
    "password":"TsHtijPlPGN04e6t",
    "host":"aws-0-eu-central-1.pooler.supabase.com",
    "port":5432
}

app = Flask(__name__)
jwt = JWTManager()
 # Change this to a secure key in production

db = SQLAlchemy()

   
def create_app():
    app = Flask(__name__)
    # PostgreSQL connection string
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres.bmkjhzotrhchferoexsh:TsHtijPlPGN04e6t@aws-0-eu-central-1.pooler.supabase.com:5432/postgres'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = 'your-secret-key'  # Change this to a secure key in production
    db.init_app(app)
    CORS(app)
    db=SQLAlchemy(app)
    migrate=Migrate(app,db) #initialize migragtions
    ma=Marshmallow(app)
    jwt.init_app(app, secret_key='your-secret-key') #initialize JWT manager
    
    return app






    
