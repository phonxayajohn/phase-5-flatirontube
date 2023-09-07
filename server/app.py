from flask import Flask, request, jsonify, make_response
from flask_migrate import Migrate
from flask_restful import Api, Resource
import os

from models import db, Video
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

class Videos(Resource):
    def get(self):
        try:
            videos = Video.query.all()

            video_list = []
            for video in videos:
                video_data = {
                    'id': video.id,
                    'title': video.title,
                    'url': video.url,
                    'timestamp': video.timestamp,
                    'thumbnail': video.thumbnail
                }
                video_list.append(video_data)

            return make_response(video_list, 200)
        
        except Exception as e:
            return make_response({'message': str(e)}, 500)

class VideosById(Resource):
    def get(self, id):
        video = Video.query.filter_by(id=id).first()

        if video:
            
            video_data = {
                'id': video.id,
                'title': video.title,
                'url': video.url,
                'timestamp': video.timestamp,
                'thumbnail': video.thumbnail
            }
            return make_response(jsonify(video_data), 200)
        
        return make_response({"error": "Video not found"}, 404)

api.add_resource(Videos, "/videos")
api.add_resource(VideosById, "/videos/<int:id>")

if __name__ == '__main__':
    app.run(port=5555, debug=True)