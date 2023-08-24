from flask import Flask, request, make_response
from flask_migrate import Migrate
from flask_restful import Api, Resource
import os
from models import db, User, Like, WatchHistory, Following, Channel, Comment, Video, VideoCategory, Category
from config import app, db, api

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATABASE = os.environ.get(
    "DB_URI", f"sqlite:///{os.path.join(BASE_DIR, 'app.db')}")

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app,db)

db.init_app(app)
api = Api(app)


@app.route('/')
def index():
    return '<h1>Phase 5 Project Server</h1>'

class Users(Resource):
    def get(self):
        users = [user.to_dict(rules=('-like', '-watch_history', '-following', '-comment')) for user in User.query.all()]
        return make_response(users, 200)
    
    def post(self):
        try:
            new_user = User(
                username = request.json['username'],
                email = request.json['email'],
                password = request.json['password'],
                created_at = request.json['created_at']
            )
            db.session.add(new_user)
            db.session.commit()

            return make_response(new_user.to_dict(), 201)
        
        except ValueError:
            return make_response({"errors": ["validation errors"]}, 400)

api.add_resource(Users, "/users")
