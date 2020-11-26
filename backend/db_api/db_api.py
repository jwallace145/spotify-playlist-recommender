from flask import Flask
from flask import request
from flask import jsonify
from flask_pymongo import PyMongo
from flask_cors import CORS
from bson.objectid import ObjectId
import datetime

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/songs_db"
mongo = PyMongo(app)

cors = CORS(app)


#---- HEALTH CHECK ----#
@app.route('/health', methods=['GET'])
def healtch_check():
    return jsonify({'status': 'healthy'})


#---- CREATE ----#
@app.route('/insert-song', methods=['POST'])
def insert_song():
    songs = mongo.db.songs.find(request.get_json())

    if songs:
        output = {
            'exists': 'true'
        }
    else:
        song = {
            'userId': request.get_json().get('userId'),
            'title': request.get_json().get('title'),
            'artist': request.get_json().get('artist'),
            'album': request.get_json().get('album'),
            'timestamp': datetime.datetime.utcnow()
        }

        song = mongo.db.songs.insert_one(song)
        song = mongo.db.songs.find_one(song.inserted_id)

        output = [{
            'userId': song['userId'],
            'songId': str(song['_id']),
            'title': song['title'],
            'artist': song['artist'],
            'album': song['album'],
            'timestamp': song['timestamp']
        }]

        return jsonify(output)


@ app.route('/insert-songs', methods=['POST'])
def insert_songs():
    inserted_songs = []
    for song in request.get_json():
        songs = mongo.db.songs.find(song)

        if not songs:
            mongo.db.songs.insert_one(song)
            inserted_songs.append(song)

    output = [{'numberOfInsertedSongs': len(inserted_songs)}]
    for song in inserted_songs:
        song = mongo.db.songs.find_one(song)

        output.append({
            'userId': song['userId'],
            'songId': str(song['_id']),
            'title': song['title'],
            'artist': song['artist'],
            'album': song['album'],
        })

    return jsonify(output)


#---- READ ----#
@app.route('/song/<song_id>', methods=['GET'])
def get_song_by_id(song_id):
    song = mongo.db.songs.find_one({
        '_id': ObjectId(song_id)
    })

    if song:
        output = [{
            'userId': song['userId'],
            'songId': str(song['_id']),
            'title': song['title'],
            'artist': song['artist'],
            'album': song['album']
        }]
    else:
        output = [{
            'songId': 'does not exist'
        }]

    return jsonify(output)


@ app.route('/song', methods=['GET'])
def get_song():
    userId = request.args['userId']
    title = request.args['title']
    artist = request.args['artist']
    album = request.args['album']

    song = mongo.db.songs.find_one({
        'userId': userId,
        'title': title,
        'artist': artist,
        'album': album
    })

    if song:
        output = {
            'userId': song['userId'],
            'songId': str(song['_id']),
            'title': song['title'],
            'artist': song['artist'],
            'album': song['album']
        }
    else:
        output = {
            'exists': 'false'
        }

    return jsonify(output)


@ app.route('/songs', methods=['GET'])
def get_songs():
    songs = mongo.db.songs.find()

    output = [{'numberOfSongs': songs.count()}]
    for song in songs:
        output.append({
            'songId': str(song['_id']),
            'title': song['title'],
            'artist': song['artist'],
            'album': song['album']
        })

    return jsonify(output)


#---- DELETE ----#
@ app.route('/delete-song', methods=['DELETE'])
def delete_song():
    mongo.db.songs.delete_one({
        'userId': request.args['userId'],
        'title': request.args['title'],
        'artist': request.args['artist'],
        'album': request.args['album']
    })

    output = [{'deleteSuccessful': 'true'}]
    output.append({
        'userId': request.args['userId'],
        'title': request.args['title'],
        'artist': request.args['artist'],
        'album': request.args['album']
    })

    return jsonify(output)


@ app.route('/delete-songs', methods=['DELETE'])
def delete_songs():
    mongo.db.songs.delete_many({})
    return jsonify({'deleteSuccessful': 'true'})


if __name__ == '__main__':
    app.run(debug=True)
