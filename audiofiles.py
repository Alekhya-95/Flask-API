from settings import *
from datetime import datetime

# Initializing our database
db = SQLAlchemy(app)

# the class Song will inherit the db.Model of SQLAlchemy
class Song(db.Model):
    __tablename__ = 'songs'
    id = db.Column(db.Integer, primary_key=True)
    name_of_the_song = db.Column(db.String(100), nullable=False)
    duration_in_number_of_seconds = db.Column(db.Integer, nullable=False)
    uploaded_time = db.Column(db.DateTime, default=datetime.utcnow(),nullable=False)

    def song_json(self):
        return {'id': self.id, 'name_of_the_song': self.name_of_the_song,
                'duration_in_number_of_seconds': self.duration_in_number_of_seconds,
                'uploaded_time': self.uploaded_time}

# the class Podcast will inherit the db.Model of SQLAlchemy
class Podcast(db.Model):
    __tablename__ = 'podcasts'
    id = db.Column(db.Integer, primary_key=True)
    name_of_the_podcast = db.Column(db.String(100), nullable=False)
    duration_in_number_of_seconds = db.Column(db.Integer, nullable=False)
    uploaded_time = db.Column(db.DateTime, default=datetime.utcnow(), nullable=False)
    host = db.Column(db.String(100), nullable=False)
    participants = db.Column(db.String(100), nullable=True)

    def podcast_json(self):
        return {'id': self.id, 'name_of_the_podcast': self.name_of_the_podcast,
                'duration_in_number_of_seconds': self.duration_in_number_of_seconds,
                'uploaded_time': self.uploaded_time, 'host': self.host,
                'participants': self.participants}

# the class Audiobook will inherit the db.Model of SQLAlchemy
class Audiobook(db.Model):
    __tablename__ = 'audiobooks'
    id = db.Column(db.Integer, primary_key=True)
    title_of_the_audiobook = db.Column(db.String(100), nullable=False)
    author_of_the_title = db.Column(db.String(100), nullable=False)
    narrator = db.Column(db.String(100), nullable=False)
    duration_in_number_of_seconds = db.Column(db.Integer, nullable=False)
    uploaded_time = db.Column(db.DateTime,default=datetime.utcnow(), nullable=False)

    def audiobook_json(self):
        return {'id': self.id, 'title_of_the_audiobook': self.title_of_the_audiobook,
                'author_of_the_title': self.author_of_the_title, 'narrator': self. narrator,
                'duration_in_number_of_seconds': self.duration_in_number_of_seconds,
                'uploaded_time': self.uploaded_time}

class Audiotype(db.Model):
    __tablename__ = 'AudioType'
    id = db.Column(db.Integer, primary_key=True)
    type_of_audio = db.Column(db.String(50), nullable=False)


    def get_all_songs():
        """function to get all songs in our database"""
        return [Song.song_json(song) for song in Song.query.all()]

    def get_all_podcasts():
        """function to get all podcasts in our database"""
        return [Podcast.podcast_json(podcast) for podcast in Podcast.query.all()]

    def get_all_audiobooks():
        """function to get all audiobooks in our database"""
        return [Audiobook.audiobook_json(audiobook) for audiobook in Audiobook.query.all()]

    def get_song(_id):
        """function to get song using the id of the song as parameter"""
        return [Song.song_json(Song.query.filter_by(id=_id).first())]
        # Song.song_json() coverts our output to the json format defined earlier
        # the filter_by method filters the query by the id
        # since our id is unique we will only get one result
        # the .first() method will get that first value returned

    def get_podcast(_id):
        """function to get podcast using the id of the podcast as parameter"""
        return [Podcast.podcast_json(Podcast.query.filter_by(id=_id).first())]
        # Podcast.podcast_json() coverts our output to the json format defined earlier
        # the filter_by method filters the query by the id
        # since our id is unique we will only get one result
        # the .first() method will get that first value returned

    def get_audiobook(_id):
        """function to get audiobook using the id of the audiobook as parameter"""
        return [Audiobook.audiobook_json(Audiobook.query.filter_by(id=_id).first())]
        # Audiobook.audiobook_json() coverts our output to the json format defined earlier
        # the filter_by method filters the query by the id
        # since our id is unique we will only get one result
        # the .first() method will get that first value returned

    def add_song(_name_of_the_song, _duration_in_number_of_seconds):
        """function to add song to database using _name_of_the_song,
        _duration_in_number_of_seconds
        as parameters"""
        # creating an instance of our Song constructor
        new_song = Song(name_of_the_song=_name_of_the_song,
                        duration_in_number_of_seconds=_duration_in_number_of_seconds)
        db.session.add(new_song)  # add new song to database session
        db.session.commit()  # commit changes to session

    def add_podcast(_name_of_the_podcast, _duration_in_number_of_seconds,
                    _host, _participants):
        """function to add podcast to database using _name_of_the_podcast,
        _duration_in_number_of_seconds, _host, _participants
        as parameters"""
        # creating an instance of our Podcast constructor
        new_podcast = Podcast(name_of_the_podcast=_name_of_the_podcast,
                              duration_in_number_of_seconds=_duration_in_number_of_seconds,
                              host=_host, participants=_participants)
        db.session.add(new_podcast)  # add new Podcast to database session
        db.session.commit()  # commit changes to session

    def add_audiobook(_title_of_the_audiobook, _author_of_the_title, _narrator,
                      _duration_in_number_of_seconds):
        """function to add audio book to database using _title_of_the_audiobook,
        _author_of_the_title, _narrator, _duration_in_number_of_seconds
        as parameters"""
        # creating an instance of our Audiobook constructor
        new_audiobook = Audiobook(title_of_the_audiobook=_title_of_the_audiobook,
                                  author_of_the_title=_author_of_the_title,
                                  narrator=_narrator,
                                  duration_in_number_of_seconds=_duration_in_number_of_seconds)
        db.session.add(new_audiobook)  # add new audio book to database session
        db.session.commit()  # commit changes to session

    def update_song(_id, _name_of_the_song, _duration_in_number_of_seconds):
        """function to update the details of a song using the id, name of the song,
        and duration in number of seconds as parameters"""
        song_to_update = Song.query.filter_by(id=_id).first()
        song_to_update.name_of_the_song = _name_of_the_song
        song_to_update.duration_in_number_of_seconds = _duration_in_number_of_seconds
        db.session.commit()

    def update_podcast(_id, _name_of_the_podcast, _duration_in_number_of_seconds,
                       _host, _participants):
        """function to update the details of a podcast using the id, name of the podcast,
        duration in number of seconds, host and participants as parameters"""
        podcast_to_update = Podcast.query.filter_by(id=_id).first()
        podcast_to_update.name_of_the_podcast = _name_of_the_podcast
        podcast_to_update.duration_in_number_of_seconds = _duration_in_number_of_seconds
        podcast_to_update.host = _host
        podcast_to_update.participants = _participants
        db.session.commit()

    def update_audiobook(_id, _title_of_the_audiobook, _author_of_the_title, _narrator,
                         _duration_in_number_of_seconds):
        """function to update the details of a audio book using the id, title of the audiobook,
        author of the title, narrator and duration in number of seconds as parameters"""
        audiobook_to_update = Audiobook.query.filter_by(id=_id).first()
        audiobook_to_update.title_of_the_audiobook = _title_of_the_audiobook
        audiobook_to_update.author_of_the_title = _author_of_the_title
        audiobook_to_update.narrator = _narrator
        audiobook_to_update.duration_in_number_of_seconds = _duration_in_number_of_seconds
        db.session.commit()

    def delete_song(_id):
        """function to delete a song from our database using
           the id of the song as a parameter"""
        Song.query.filter_by(id=_id).delete()
        # filter song by id and delete
        db.session.commit()  # commiting the new change to our database

    def delete_podcast(_id):
        """function to delete a podcast from our database using
           the id of the podcast as a parameter"""
        Podcast.query.filter_by(id=_id).delete()
        # filter podcast by id and delete
        db.session.commit()  # commiting the new change to our database

    def delete_audiobook(_id):
        """function to delete a audio book from our database using
           the id of the audio book as a parameter"""
        Audiobook.query.filter_by(id=_id).delete()
        # filter audio book by id and delete
        db.session.commit()  # commiting the new change to our database
