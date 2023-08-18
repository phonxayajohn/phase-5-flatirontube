from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import validates

from config import db

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    email = db.Column(db.String)
    password = db.Column(db.String)
    created_at = db.Column(db.Datetime)

    like = db.relationship("Like", cascade="all, delete", backref="user")
    watch_history = db.relationship("WatchHistory", cascade="all, delete", backref="user")
    following = db.relationship("Following", cascade="all, delete", backref="user")
    comments = db.relationship("Comment", cascade="all, delete", backref="user")

    serialize_rules = ("-like.user", "-watch_history.user", "-following.user", "-comment.user")
    
    # Add Validations
class Like(db.Model, SerializerMixin):
    __tablename__ = 'likes'

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.Datetime)

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    video_id = db.Column(db.Integer, db.ForeignKey("videos.id"))

    serialize_rules = ("-user.like", "-video.like")

class WatchHistory(db.Model, SerializerMixin):
    __tablename__ = 'watch_history'

    id = db.Column(db.Integer, primary_key=True)
    watched_at = db.Column(db.Datetime)

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    video_id = db.Column(db.Integer, db.ForeignKey("videos.id"))
    
    serialize_rules = ("-user.watch_history", "-video.watch_history")

class Following(db.Model, SerializerMixin):
    __tablename__ = 'following'

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    channel_id = db.Column(db.Integer, db.ForeignKey("channels.id"))

    serialize_rules = ("-user.following", "-channel.following")

class Channel(db.Model, SerializerMixin):
    __tablename__ = 'channels'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    created_at = db.Column(db.Datetime)

    following = db.relationship("Following", cascade="all, delete", backref="channel")
    videos = db.relationship("Video", cascade="all, delete", backref="channel")
    
    serialize_rules = ("-following.channel", "-video.channel")

class Comment(db.Model, SerializerMixin):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String)
    created_at = db.Column(db.Datetime)

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    video_id = db.Column(db.Integer, db.ForeignKey("videos.id"))

    serialize_rules = ("-user.comment", "-video.comment")

class Video(db.Model, SerializerMixin):
    __tablename__ = 'videos'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    url = db.Column(db.String)
    created_at = db.Column(db.Datetime)

    channel_id = db.Column(db.Integer, db.ForeignKey("channels.id"))

    like = db.relationship("Like", cascade="all, delete", backref="video")
    watch_history = db.relationship("WatchHistory", cascade="all, delete", backref="video")
    comments = db.relationship("Comment", cascade="all, delete", backref="video")
    video_category = db.relationship("VideoCategory", cacade="all, delete", backref="video")

    serialize_rules = ("-like.video", "-watch_history.video", "-comment.video", "-video_category.video")

class VideoCategory(db.Model, SerializerMixin):
    __tablename__ = 'video_categories'

    id = db.Column(db.Integer, primary_key=True)

    video_id = db.Column(db.Integer, db.ForeignKey("videos.id"))
    category_id = db.Column(db.Integer, db.ForeignKey("categories.id"))
    
    serialize_rules = ("-video.video_category", "-category.video_category")

class Category(db.Model, SerializerMixin):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    video_category = db.relationship("VideoCategory", cacade="all, delete", backref="category")

    serialize_rules = ("-video_category.category",)
