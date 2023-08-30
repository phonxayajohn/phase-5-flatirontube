from flask import Flask, request, make_response
from flask_migrate import Migrate
from flask_restful import Api, Resource
import os

from models import db, Comment
from config import app, db, api

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)

api = Api(app)

@app.route('/')
def index():
    return '<h1>Phase 5 Project Server</h1>'

class Comments(Resource):
    def get(self):
        comments = [comment.to_dict(rules=('-video',)) for comment in Comment.query.all()]
        return make_response(comments, 200)
    
    def post(self):
        try:
            new_comment = Comment(
                content = request.json['content'],
                created_at = request.json['created_at'],
                video_id = request.json['video_id']
            )
            db.session.add(new_comment)
            db.session.commit()

            return make_response(new_comment.to_dict(), 201)
        except ValueError:
            return make_response({"errors": ["validation errors"]}, 400)
api.add_resource(Comments, "/comments")

class CommentsById(Resource):
    def get(self, id):
        comment = Comment.query.filter_by(id=id).first()

        if comment:
            return make_response(comment.to_dict(), 200)
        return make_response({"error": "comment not found"}, 404)
api.add_resource(CommentsById, "/comments/<int:id>")

class Login(Resource):

    def get(self):
        pass

    def post(self):
        pass

api.add_resource(Login, "/login")

if __name__ == '__main__':
    app.run(port=5555, debug=True)