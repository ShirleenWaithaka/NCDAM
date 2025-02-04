from flask import Flask
from config import db
from models import Admin, Member, User
from route import app_blueprint

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres.bmkjhzotrhchferoexsh:TsHtijPlPGN04e6t@aws-0-eu-central-1.pooler.supabase.com:5432/postgres'
db.init_app(app)

app.register_blueprint(app_blueprint)

if __name__ == '__main__':
    app.run(debug=True)