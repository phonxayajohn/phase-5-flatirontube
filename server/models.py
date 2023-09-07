from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import validates

from config import db

class Video(db.Model):
    __tablename__ = 'videos'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    url = db.Column(db.String)
    timestamp = db.Column(db.String)
    thumbnail = db.Column(db.String)

class Channel(db.Model):
    pass
# Videos should have a Channel ID, Channel should have Channel Img

class Category(db.Model):
    pass
# Videos should have a Category ID and Categories should have a Video ID

class Users(db.Model):
    pass
# Users should be able to sign in or register. Signed in Users should be able to "Like" a video 
 