from audiofiles import *

#  READ
# route to get all songs
@app.route('/songs', methods=['GET'])
def get_songs():
    """Function to get all the songs in the database"""
    return jsonify({'Songs': Audiotype.get_all_songs()})

# route to get all podcasts
@app.route('/podcasts', methods=['GET'])
def get_podcasts():
    """Function to get all the podcasts in the database"""
    return jsonify({'Podcasts': Audiotype.get_all_podcasts()})

# route to get all audio books
@app.route('/audiobooks', methods=['GET'])
def get_audiobooks():
    """Function to get all the audio books in the database"""
    return jsonify({'Audiobooks': Audiotype.get_all_audiobooks()})

#  READ by id
# route to get song by id
@app.route('/songs/<int:id>', methods=['GET'])
def get_song_by_id(id):
    """Function to get song by its id from database"""
    return_value = Audiotype.get_song(id)
    return jsonify(return_value)

# route to get podcast by id
@app.route('/podcasts/<int:id>', methods=['GET'])
def get_podcast_by_id(id):
    """Function to get podcast by its id from database"""
    return_value = Audiotype.get_podcast(id)
    return jsonify(return_value)

# route to get audio book by id
@app.route('/audiobooks/<int:id>', methods=['GET'])
def get_audiobook_by_id(id):
    """Function to get audio book by its id from database"""
    return_value = Audiotype.get_audiobook(id)
    return jsonify(return_value)

# CREATE
# route to add new song
@app.route('/songs', methods=['POST'])
def add_song():
    """Function to add new song to our database"""
    request_data = request.get_json()  # getting data from client
    Audiotype.add_song(request_data["name_of_the_song"],
                       request_data["duration_in_number_of_seconds"])
    response = Response("Song added", 201, mimetype='application/json')
    return response

# route to add new podcast
@app.route('/podcasts', methods=['POST'])
def add_podcast():
    """Function to add new podcast to our database"""
    request_data = request.get_json()  # getting data from client
    Audiotype.add_podcast(request_data["name_of_the_podcast"],
                          request_data["duration_in_number_of_seconds"],
                          request_data["host"],
                          request_data["participants"])
    response = Response("Podcast added", 201, mimetype='application/json')
    return response

# route to add new audio book
@app.route('/audiobooks', methods=['POST'])
def add_audiobook():
    """Function to add new audio book to our database"""
    request_data = request.get_json()  # getting data from client
    Audiotype.add_audiobook(request_data["title_of_the_audiobook"],
                            request_data["author_of_the_title"],
                            request_data["narrator"],
                            request_data["duration_in_number_of_seconds"])
    response = Response("Audio book added", 201, mimetype='application/json')
    return response

#  UPDATE
# route to update song with PUT method
@app.route('/songs/<int:id>', methods=['PUT'])
def update_songs(id):
    """Function to edit song in our database using song id"""
    request_data = request.get_json()
    Audiotype.update_song(id, request_data['name_of_the_song'],
                          request_data['duration_in_number_of_seconds'])
    response = Response("Song Updated", status=200, mimetype='application/json')
    return response

# route to update podcast with PUT method
@app.route('/podcasts/<int:id>', methods=['PUT'])
def update_podcast(id):
    """Function to edit podcast in our database using podcast id"""
    request_data = request.get_json()
    Audiotype.update_podcast(id, request_data['name_of_the_podcast'],
                             request_data['duration_in_number_of_seconds'],
                             request_data['host'],
                             request_data['participants'])
    response = Response("podcast Updated", status=200, mimetype='application/json')
    return response

# route to update audio book with PUT method
@app.route('/audiobooks/<int:id>', methods=['PUT'])
def update_audiobook(id):
    """Function to edit audio book in our database using audio book id"""
    request_data = request.get_json()
    Audiotype.update_audiobook(id, request_data['title_of_the_audiobook'],
                               request_data['author_of_the_title'],
                               request_data['narrator'],
                               request_data['duration_in_number_of_seconds'])
    response = Response("Audio book Updated", status=200, mimetype='application/json')
    return response

#  DELETE
# route to delete song using the DELETE method
@app.route('/songs/<int:id>', methods=['DELETE'])
def remove_song(id):
    """Function to delete song from our database"""
    Audiotype.delete_song(id)
    response = Response("Song Deleted", status=200, mimetype='application/json')
    return response

# route to delete podcast using the DELETE method
@app.route('/podcasts/<int:id>', methods=['DELETE'])
def remove_podcast(id):
    """Function to delete podcast from our database"""
    Audiotype.delete_podcast(id)
    response = Response("Podcast Deleted", status=200, mimetype='application/json')
    return response

# route to delete audio book using the DELETE method
@app.route('/audiobooks/<int:id>', methods=['DELETE'])
def remove_audiobook(id):
    """Function to delete audio book from our database"""
    Audiotype.delete_audiobook(id)
    response = Response("Audio Book Deleted", status=200, mimetype='application/json')
    return response

if __name__ == "__main__":
    app.run(port=1235, debug=True)