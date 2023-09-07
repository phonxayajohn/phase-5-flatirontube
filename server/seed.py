from app import app
from models import db, Video

if __name__ == '__main__':
    with app.app_context():

        Video.query.delete()

        video1 = Video(
            title="The Rolling Stones - Angry (Official Video)", 
            url="https://youtu.be/_mEC54eTuGw?si=kyfW8bTiK_lOERhJ", 
            timestamp="3:46", 
            thumbnail="https://puu.sh/JPwaz.png")
        
        video2 = Video(
            title="THE BOY AND THE HERON | Official Teaser Trailer", 
            url="https://youtu.be/f7EDFdA10pg?si=O2iw8FFDRA90m675", 
            timestamp="1:12", 
            thumbnail="https://puu.sh/JPwaO.png")
        
        video3 = Video(
            title="Starfield in a Nutshell", 
            url="https://youtu.be/rCAuf674yuk?si=KRcCc9IhE3LwNdid", 
            timestamp="11:31", 
            thumbnail="https://puu.sh/JPwaZ.png")
        
        videos = [video1, video2, video3]

        db.session.add_all(videos)
        db.session.commit()